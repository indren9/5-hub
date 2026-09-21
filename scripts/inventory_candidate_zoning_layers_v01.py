#!/usr/bin/env python3
"""Inventory polygon layers in materialized official PRGC archives for V2-1."""
from __future__ import annotations

import argparse
import csv
import json
import re
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import pyogrio


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def existing_path(raw: str) -> Path:
    p = Path(raw)
    if p.exists():
        return p
    marker = "\\UniUD\\Tesi\\5_HUB_FVG\\"
    if marker in raw:
        alt = Path(r"C:\Users\visen\OneDrive\UNIVER~1\UniUD\Tesi\5_HUB_FVG") / raw.split(marker, 1)[1]
        if alt.exists():
            return alt
    return p


def safe_extract(archive: Path, dest: Path) -> None:
    if dest.exists() and any(dest.iterdir()):
        return
    dest.mkdir(parents=True, exist_ok=True)
    root = dest.resolve()
    with zipfile.ZipFile(archive) as z:
        for member in z.infolist():
            target = (dest / member.filename).resolve()
            if root not in target.parents and target != root:
                raise RuntimeError(f"Unsafe ZIP member: {member.filename}")
        z.extractall(dest)


def classify_name(rel: str, geom: str) -> tuple[str, int]:
    s = rel.lower().replace("\\", "/")
    base = Path(rel).stem.lower()
    if "polygon" not in (geom or "").lower():
        return "NON_POLYGON", -100
    if re.search(r"centro.*(testo|label)|testo|simbol|linea|punto|centroid", base):
        return "EXCLUDE_LABEL_OR_SYMBOL", -50
    score, rule = 0, "NO_NAME_SIGNAL"
    if re.search(r"zonizz|azzon", base):
        score, rule = 100, "STRONG_ZONING_NAME"
    elif re.search(r"zona.?omog|zone.?omog|zoning", base):
        score, rule = 90, "STRONG_ZONE_NAME"
    elif re.search(r"destin.*urban|uso.?suolo.*prg|piano.?operativo", base):
        score, rule = 70, "MEDIUM_PLANNING_NAME"
    elif re.search(r"\bzone?\b|zona", base):
        score, rule = 40, "WEAK_ZONE_NAME"
    depth = len(Path(rel).parts) - 1
    score -= depth * 5
    if re.search(r"(^|/)(var|variante)[_ -]?\d+", s):
        score -= 20
        rule += "_VARIANT_SUBFOLDER_PENALTY"
    return rule, score


def inspect_source(src: dict, extracted_root: Path) -> list[dict]:
    rows: list[dict] = []
    archive = existing_path(src["archive_path"])
    dest = extracted_root / src["istat_code"]
    try:
        safe_extract(archive, dest)
    except Exception as e:
        return [{
            "istat_code": src["istat_code"], "comune": src["comune"],
            "source_tier": src["source_tier_preliminary"],
            "archive_path": str(archive), "layer_path": "", "layer_rel": "",
            "geometry_type": "", "feature_count": "", "crs": "",
            "fields": "", "name_rule": "ARCHIVE_EXTRACT_ERROR",
            "heuristic_score": -999, "read_error": f"{type(e).__name__}: {e}",
        }]

    for shp in sorted(dest.rglob("*.shp")):
        rel = str(shp.relative_to(dest))
        try:
            info = pyogrio.read_info(shp)
            geom = str(info.get("geometry_type", ""))
            rule, score = classify_name(rel, geom)
            fields = "|".join(map(str, info.get("fields", [])))
            count = info.get("features", "")
            crs = info.get("crs", "")
            err = ""
        except Exception as e:
            geom, fields, count, crs = "", "", "", ""
            rule, score = "LAYER_READ_ERROR", -999
            err = f"{type(e).__name__}: {e}"

        rows.append({
            "istat_code": src["istat_code"], "comune": src["comune"],
            "source_tier": src["source_tier_preliminary"],
            "archive_path": str(archive), "layer_path": str(shp), "layer_rel": rel,
            "geometry_type": geom, "feature_count": count, "crs": crs,
            "fields": fields, "name_rule": rule, "heuristic_score": score,
            "read_error": err,
        })
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-inventory", type=Path, required=True)
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    cfg = json.loads(args.config.read_text(encoding="utf-8"))
    root = Path(cfg["output_root"])
    extracted_root = root / cfg["source_cache_subdir"] / "extracted"
    source_rows = read_csv(args.source_inventory)
    vector_rows = [r for r in source_rows if r["source_tier_preliminary"] in {"S1", "S2"}]

    rows_out: list[dict] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(inspect_source, src, extracted_root): src["istat_code"] for src in vector_rows}
        done = 0
        for fut in as_completed(futs):
            rows_out.extend(fut.result())
            done += 1
            if done % 10 == 0 or done == len(vector_rows):
                print(f"inventoried {done}/{len(vector_rows)} vector municipalities", flush=True)
    rows_out.sort(key=lambda r: (r["istat_code"], r["layer_rel"]))

    out = root / "CANDIDATE_ZONING_LAYER_INVENTORY_v01.csv"
    write_csv(out, rows_out)
    polygons = [r for r in rows_out if "polygon" in r["geometry_type"].lower()]
    strong = [r for r in polygons if int(r["heuristic_score"]) >= 70]
    muni_strong = sorted({r["istat_code"] for r in strong})
    print(json.dumps({
        "vector_municipalities": len(vector_rows),
        "layer_records": len(rows_out),
        "polygon_layers": len(polygons),
        "strong_or_medium_layers": len(strong),
        "municipalities_with_strong_or_medium": len(muni_strong),
        "municipalities_without_strong_or_medium": len(vector_rows) - len(muni_strong),
        "output": str(out),
    }, indent=2))


if __name__ == "__main__":
    main()
