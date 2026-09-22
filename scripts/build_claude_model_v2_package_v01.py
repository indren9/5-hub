from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
import tempfile
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = REPO_ROOT / "docs" / "CLAUDE_MODEL_v2_PACKAGE_MANIFEST_v01.csv"
DEFAULT_PROMPT = REPO_ROOT / "docs" / "INPUT_PIPELINE_CLAUDE_MODEL_v2_FVG_v01.md"
DEFAULT_OUTPUT = Path(
    r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG"
    r"\07_deliverables\CLAUDE_MODEL_v2_PACKAGE_v01.zip"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_stream(stream) -> str:
    digest = hashlib.sha256()
    for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
        digest.update(chunk)
    return digest.hexdigest().upper()


def load_manifest(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter=";"))
    if not rows:
        raise RuntimeError("Manifest is empty.")
    required = {"role", "package_path", "source_path", "source_selector", "source_sha256", "readiness"}
    missing = required.difference(rows[0])
    if missing:
        raise RuntimeError(f"Manifest columns missing: {sorted(missing)}")
    return rows


def preflight(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    package_paths: set[str] = set()
    for row in rows:
        role = row["role"].strip()
        package_path = row["package_path"].strip()
        source = Path(row["source_path"].strip())
        readiness = row["readiness"].strip().upper()
        if readiness.startswith("BLOCKING"):
            errors.append(f"{role}: readiness={readiness}")
        if package_path in package_paths:
            errors.append(f"{role}: duplicate package_path={package_path}")
        package_paths.add(package_path)
        if not source.exists():
            errors.append(f"{role}: source missing: {source}")
            continue
        expected_hash = row["source_sha256"].strip().upper()
        selector = row["source_selector"].strip()
        if source.suffix.lower() == ".zip" and selector:
            try:
                with zipfile.ZipFile(source) as archive:
                    info = archive.getinfo(selector)
                    with archive.open(info) as member:
                        actual_hash = sha256_stream(member)
            except Exception as exc:
                errors.append(f"{role}: ZIP member check failed: {exc}")
                continue
        else:
            actual_hash = sha256_file(source)
        if expected_hash and actual_hash != expected_hash:
            errors.append(
                f"{role}: SHA256 mismatch expected={expected_hash} actual={actual_hash}"
            )
    return errors


def materialize_row(row: dict[str, str], staging_root: Path) -> dict[str, str]:
    source = Path(row["source_path"].strip())
    selector = row["source_selector"].strip()
    destination = staging_root / Path(row["package_path"])
    destination.parent.mkdir(parents=True, exist_ok=True)

    if source.suffix.lower() == ".zip" and selector:
        with zipfile.ZipFile(source) as archive:
            with archive.open(selector) as src, destination.open("wb") as dst:
                shutil.copyfileobj(src, dst)
    else:
        shutil.copy2(source, destination)

    resolved = dict(row)
    resolved["source_bytes"] = str(destination.stat().st_size)
    resolved["source_sha256"] = sha256_file(destination)
    return resolved


def write_resolved_manifest(rows: list[dict[str, str]], destination: Path) -> None:
    fieldnames = list(rows[0].keys())
    with destination.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def build_package(
    rows: list[dict[str, str]],
    manifest_path: Path,
    prompt_path: Path,
    output_zip: Path,
) -> None:
    errors = preflight(rows)
    if errors:
        joined = "\n - ".join(errors)
        raise RuntimeError(f"Package preflight failed:\n - {joined}")

    output_zip.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="claude_model_v2_") as tmp:
        staging = Path(tmp)
        resolved_rows = [materialize_row(row, staging) for row in rows]

        control = staging / "00_prompt"
        control.mkdir(parents=True, exist_ok=True)
        shutil.copy2(prompt_path, control / prompt_path.name)
        write_resolved_manifest(
            resolved_rows,
            control / manifest_path.name,
        )

        if output_zip.exists():
            output_zip.unlink()
        with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            for file_path in sorted(p for p in staging.rglob("*") if p.is_file()):
                archive.write(file_path, file_path.relative_to(staging).as_posix())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fail-closed preflight/build for the Claude MODEL_v2 input package."
    )
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--prompt", type=Path, default=DEFAULT_PROMPT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--build",
        action="store_true",
        help="Create the ZIP only if every manifest row passes preflight.",
    )
    args = parser.parse_args()

    rows = load_manifest(args.manifest)
    errors = preflight(rows)
    if errors:
        print("PACKAGE_PREFLIGHT=FAIL")
        for error in errors:
            print(f"- {error}")
        return 2

    print(f"PACKAGE_PREFLIGHT=PASS rows={len(rows)}")
    if not args.build:
        print("ZIP_NOT_CREATED: run again with --build after governance acceptance and manifest binding.")
        return 0

    build_package(rows, args.manifest, args.prompt, args.output)
    print(f"ZIP_CREATED={args.output}")
    print(f"ZIP_SHA256={sha256_file(args.output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
