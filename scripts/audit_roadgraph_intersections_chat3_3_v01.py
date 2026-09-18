from __future__ import annotations

import collections
import csv
import json
from pathlib import Path

from shapely.geometry import shape
from shapely.strtree import STRtree

RAW_PATH = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\01_raw_data\F3_CHAT_3_3\GRAFO_STRADALE_FVG_WFS_20260918.geojson")
OUT_ROOT = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\05_intermediate_outputs\F3_CHAT_3_3")
METRICS_PATH = OUT_ROOT / "ROADGRAPH_INTERSECTION_AUDIT_v01.json"
EXAMPLES_PATH = OUT_ROOT / "ROADGRAPH_NONNODED_INTERSECTION_EXAMPLES_v01.csv"
TOL = 0.001


def is_endpoint(line, pt) -> bool:
    c0 = line.coords[0]
    c1 = line.coords[-1]
    x, y = pt.x, pt.y
    return (
        (abs(c0[0] - x) <= TOL and abs(c0[1] - y) <= TOL)
        or (abs(c1[0] - x) <= TOL and abs(c1[1] - y) <= TOL)
    )


def point_parts(geom):
    if geom.geom_type == "Point":
        return [geom]
    if geom.geom_type == "MultiPoint":
        return list(geom.geoms)
    if geom.geom_type == "GeometryCollection":
        return [g for g in geom.geoms if g.geom_type == "Point"]
    return []
def main() -> None:
    with RAW_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)
    feats = data["features"]
    geoms = [shape(f["geometry"]) for f in feats]
    tree = STRtree(geoms)

    counts = collections.Counter()
    examples = []
    overlap_examples = []
    checked_pairs = 0

    for i, g in enumerate(geoms):
        for j in tree.query(g, predicate="intersects"):
            j = int(j)
            if j <= i:
                continue
            checked_pairs += 1
            h = geoms[j]
            inter = g.intersection(h)
            if inter.is_empty:
                continue
            if inter.geom_type in ("LineString", "MultiLineString"):
                counts["linear_overlap_pairs"] += 1
                if len(overlap_examples) < 20:
                    overlap_examples.append((i, j, inter.length))
                continue
            pts = point_parts(inter)
            if not pts:
                counts[f"other_{inter.geom_type}"] += 1
                continue
            for pt in pts:
                a = is_endpoint(g, pt)
                b = is_endpoint(h, pt)
                if a and b:
                    counts["endpoint_endpoint"] += 1
                elif a or b:
                    counts["endpoint_interior"] += 1
                    kind = "endpoint_interior"
                else:
                    counts["interior_interior"] += 1
                    kind = "interior_interior"
                if not (a and b) and len(examples) < 200:
                    examples.append((i, j, kind, pt.x, pt.y))
        if i and i % 10000 == 0:
            print(f"processed {i}/{len(geoms)}", flush=True)
    rows = []
    for i, j, kind, x, y in examples:
        pi = feats[i]["properties"]
        pj = feats[j]["properties"]
        rows.append({
            "idx_a": i,
            "id1_a": pi.get("ID1"),
            "class_a": pi.get("CLASSE"),
            "road_a": pi.get("TRIM_STR_CODE_1"),
            "dir_a": pi.get("DIR"),
            "idx_b": j,
            "id1_b": pj.get("ID1"),
            "class_b": pj.get("CLASSE"),
            "road_b": pj.get("TRIM_STR_CODE_1"),
            "dir_b": pj.get("DIR"),
            "kind": kind,
            "x": x,
            "y": y,
        })

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    with EXAMPLES_PATH.open("w", newline="", encoding="utf-8-sig") as f:
        if rows:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)

    metrics = {
        "source_raw_path": str(RAW_PATH),
        "features": len(feats),
        "candidate_intersecting_pairs_checked": checked_pairs,
        "intersection_point_counts": dict(counts),
        "potential_nonnoded_point_intersections": (
            counts["endpoint_interior"] + counts["interior_interior"]
        ),
        "interpretation": (
            "Endpoint-interior and interior-interior intersections are candidates "
            "for non-noded crossings in an endpoint-only graph. They are not "
            "automatically errors because grade-separated crossings can be valid."
        ),
        "examples_csv": str(EXAMPLES_PATH),
        "linear_overlap_examples": overlap_examples,
    }
    with METRICS_PATH.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
