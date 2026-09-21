#!/usr/bin/env python3
"""Materialize official best-available PRGC vector archives for V2-1.

This stage does not generate candidates. It only resolves real vector artifacts
behind the Phase-3 coverage and records hashes/status for the later S1-S5 hierarchy.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import acquire_validate_current_urban_planning_chat3_8_v01 as core


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def existing_path(raw: str) -> Path:
    p = Path(raw)
    if p.exists():
        return p
    marker = "\\UniUD\\Tesi\\5_HUB_FVG\\"
    if marker in raw:
        tail = raw.split(marker, 1)[1]
        alt = Path(r"C:\Users\visen\OneDrive\UNIVER~1\UniUD\Tesi\5_HUB_FVG") / tail
        if alt.exists():
            return alt
    return p


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def process_row(row: dict, cache_root: Path) -> tuple[dict, list[dict]]:
    code = row["istat_code"]
    base = {
        "istat_code": code,
        "comune": row["comune"],
        "currentness_status": row["currentness_status"],
        "irdat_dataset_id": row.get("irdat_dataset_id", ""),
        "source_tier_preliminary": "",
        "materialization_status": "",
        "source_url": row.get("irdat_detail_url", "") or row.get("institutional_source_url", ""),
        "archive_path": "",
        "archive_sha256": "",
        "archive_bytes": "",
        "archive_integrity": "",
        "geometry_crs_metadata": row.get("geometry_crs", ""),
        "notes": "",
    }

    if row["currentness_status"] == "CURRENT_VECTOR_VERIFIED":
        p = existing_path(row.get("vector_artifact_path", ""))
        if p.exists():
            base.update({
                "source_tier_preliminary": "S1",
                "materialization_status": "EXISTING_VERIFIED_VECTOR",
                "archive_path": str(p),
                "archive_sha256": row.get("vector_sha256", "") or sha256_file(p),
                "archive_bytes": p.stat().st_size,
                "archive_integrity": row.get("vector_archive_integrity", ""),
            })
            return base, []
        base["materialization_status"] = "S1_ARCHIVE_MISSING"
        base["notes"] = "Phase-3 verified vector path is not readable."
        return base, []

    did = row.get("irdat_dataset_id", "").strip()
    if not did:
        base["materialization_status"] = "NO_IRDAT_DATASET_ID"
        return base, []

    local_manifest: list[dict] = []
    try:
        item, _ = core.ir_detail(did)
        base["source_url"] = item.get("detail_url", "") or base["source_url"]
        if not item.get("download_url"):
            base["materialization_status"] = "IRDAT_NO_VECTOR_DOWNLOAD"
            base["notes"] = "Official IRDAT record found, no downloadable vector link exposed."
            return base, local_manifest
        folder = cache_root / "irdat" / f"{code}_{did}"
        qa = core.download_vector(item, folder, local_manifest)
        if qa.get("download_status") == "DOWNLOADED":
            base.update({
                "source_tier_preliminary": "S2",
                "materialization_status": "DOWNLOADED_OFFICIAL_VECTOR",
                "archive_path": qa.get("artifact_path", ""),
                "archive_sha256": str(qa.get("sha256", "")).upper(),
                "archive_bytes": qa.get("bytes", ""),
                "archive_integrity": qa.get("archive_integrity", ""),
            })
        else:
            base["materialization_status"] = qa.get("download_status", "DOWNLOAD_FAILED")
            base["notes"] = "Official vector download failed or was unavailable."
        return base, local_manifest
    except Exception as e:
        base["materialization_status"] = f"ERROR:{type(e).__name__}"
        base["notes"] = str(e)[:500]
        return base, local_manifest


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--coverage", type=Path, required=True)
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    cfg = json.loads(args.config.read_text(encoding="utf-8"))
    output_root = Path(cfg["output_root"])
    cache_root = output_root / cfg["source_cache_subdir"]
    cache_root.mkdir(parents=True, exist_ok=True)

    rows = read_csv(args.coverage)
    if len(rows) != 215:
        raise RuntimeError(f"Expected 215 municipalities, found {len(rows)}")

    results: list[dict] = []
    manifest: list[dict] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(process_row, row, cache_root): row["istat_code"] for row in rows}
        done = 0
        for fut in as_completed(futs):
            result, items = fut.result()
            results.append(result)
            manifest.extend(items)
            done += 1
            if done % 20 == 0 or done == len(futs):
                print(f"materialized {done}/{len(futs)}", flush=True)

    results.sort(key=lambda r: r["istat_code"])
    inv_path = output_root / "CANDIDATE_SOURCE_VECTOR_INVENTORY_v01.csv"
    write_csv(inv_path, results)

    manifest_path = output_root / "CANDIDATE_SOURCE_VECTOR_MANIFEST_v01.json"
    manifest_path.write_text(json.dumps({
        "producer": Path(__file__).name,
        "coverage": str(args.coverage),
        "config": cfg,
        "artifacts": manifest,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    counts: dict[str, int] = {}
    for r in results:
        key = r["materialization_status"]
        counts[key] = counts.get(key, 0) + 1
    print(json.dumps({
        "municipalities": len(results),
        "status_counts": counts,
        "S1": sum(r["source_tier_preliminary"] == "S1" for r in results),
        "S2": sum(r["source_tier_preliminary"] == "S2" for r in results),
        "inventory": str(inv_path),
        "manifest": str(manifest_path),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
