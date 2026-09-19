#!/usr/bin/env python3
"""QA strutturale dei vettori urbanistici correnti verificati da Chat 3.8."""
from __future__ import annotations

import argparse
import csv
import zipfile
from pathlib import Path


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--coverage", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()

    rows = [
        r for r in read_csv(args.coverage)
        if r["currentness_status"] == "CURRENT_VECTOR_VERIFIED"
    ]
    out = []
    for r in rows:
        path = Path(r["vector_artifact_path"])
        names: list[str] = []
        bad = ""
        error = ""
        try:
            with zipfile.ZipFile(path) as z:
                bad = z.testzip() or ""
                names = z.namelist()
        except Exception as e:
            error = f"{type(e).__name__}: {e}"

        lower = {n.lower(): n for n in names}
        shp = [n for n in names if n.lower().endswith(".shp")]
        layer_checks = []
        all_core = bool(shp)
        for name in shp:
            stem = name[:-4].lower()
            dbf = stem + ".dbf" in lower
            shx = stem + ".shx" in lower
            prj = stem + ".prj" in lower
            cpg = stem + ".cpg" in lower
            all_core &= dbf and shx
            layer_checks.append(
                f"{name}:dbf={dbf};shx={shx};prj={prj};cpg={cpg}"
            )

        metadata_crs = r["geometry_crs"].strip()
        any_prj = any(n.lower().endswith(".prj") for n in names)
        crs_control = (
            "SELF_DESCRIBED_PRJ_AND_METADATA"
            if any_prj and metadata_crs
            else "METADATA_CRS_ONLY_PRJ_ABSENT"
            if metadata_crs
            else "CRS_UNRESOLVED"
        )
        integrity = (
            "PASS"
            if not error and not bad and all_core
            else "FAIL"
        )
        out.append({
            "istat_code": r["istat_code"],
            "comune": r["comune"],
            "variant": r["current_variant"],
            "archive_path": str(path),
            "archive_exists": path.exists(),
            "zip_integrity": "PASS" if not bad and not error else f"FAIL:{bad or error}",
            "shp_layer_count": len(shp),
            "all_shp_have_dbf_shx": all_core,
            "any_prj": any_prj,
            "metadata_crs": metadata_crs,
            "crs_control": crs_control,
            "layer_component_checks": " | ".join(layer_checks),
            "technical_integrity": integrity,
        })

    if len(out) != 4:
        raise RuntimeError(f"Attesi 4 vettori verificati, trovati {len(out)}")
    write_csv(args.output, out)
    failures = [r for r in out if r["technical_integrity"] != "PASS"]
    print(f"verified_vectors={len(out)}")
    print(f"technical_integrity_pass={len(out)-len(failures)}")
    print(f"technical_integrity_fail={len(failures)}")
    print(f"metadata_crs_only={sum(r['crs_control']=='METADATA_CRS_ONLY_PRJ_ABSENT' for r in out)}")
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
