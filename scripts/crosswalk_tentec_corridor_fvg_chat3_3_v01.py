from __future__ import annotations

import collections
import csv
import json
import os
from pathlib import Path

from pyproj import Transformer
from shapely.geometry import LineString, MultiLineString, Point, shape
from shapely.strtree import STRtree

os.environ.setdefault("PROJ_DATA", r"C:\Program Files\QGIS 3.44.14\share\proj")
ROOT = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG")
ROAD = ROOT / r"01_raw_data\F3_CHAT_3_3\GRAFO_STRADALE_FVG_WFS_20260918.geojson"
TENT = ROOT / r"02_external_sources\F3_CHAT_3_3\TEN_T"
OUT = ROOT / r"05_intermediate_outputs\F3_CHAT_3_3\TENTEC_CORRIDOR_TO_FVG_ROAD_CROSSWALK_v01.csv"
LAYER_FILES = {
    52: TENT / "corridor_roads_layer_52_FVG_bbox_20260918.json",
    74: TENT / "corridor_roads_layer_74_FVG_bbox_20260918.json",
}
MAX_MATCH_M = 500.0
SAMPLE_STEP_M = 1000.0


def arc_geometry(obj):
    paths = obj.get("paths", [])
    lines = [LineString(p) for p in paths if len(p) >= 2]
    return lines[0] if len(lines) == 1 else MultiLineString(lines)
def iter_lines(geom):
    if geom.geom_type == "LineString":
        yield geom
    else:
        yield from geom.geoms


def main() -> None:
    road_data = json.load(ROAD.open(encoding="utf-8"))
    road_geoms = [shape(f["geometry"]) for f in road_data["features"]]
    road_props = [f["properties"] for f in road_data["features"]]
    tree = STRtree(road_geoms)
    tr = Transformer.from_crs(4326, 6708, always_xy=True)

    rows = []
    for layer_id, path in LAYER_FILES.items():
        data = json.load(path.open(encoding="utf-8-sig"))
        for feat in data.get("features", []):
            attrs = feat["attributes"]
            geo = arc_geometry(feat["geometry"])
            route_counts = collections.Counter()
            class_counts = collections.Counter()
            dists = []
            used = 0
            total = 0
            for line in iter_lines(geo):
                xy = [tr.transform(x, y) for x, y in line.coords]
                proj = LineString(xy)
                n = max(2, int(proj.length // SAMPLE_STEP_M) + 1)
                for k in range(n):
                    total += 1
                    p = proj.interpolate(k / (n - 1), normalized=True)
                    idx = int(tree.nearest(p))
                    d = p.distance(road_geoms[idx])
                    if d <= MAX_MATCH_M:
                        used += 1
                        dists.append(d)
                        pr = road_props[idx]
                        route_counts[pr.get("TRIM_STR_CODE_1")] += 1
                        class_counts[pr.get("CLASSE")] += 1
            top_routes = "; ".join(
                f"{name}:{cnt}" for name, cnt in route_counts.most_common(8)
            )
            top_classes = "; ".join(
                f"{name}:{cnt}" for name, cnt in class_counts.most_common()
            )
            rows.append({
                "tentec_layer_id": layer_id,
                "objectid": attrs.get("OBJECTID"),
                "corridors": attrs.get("CORRIDORS"),
                "core_network": attrs.get("CORE_NETWORK"),
                "type": attrs.get("TYPE"),
                "samples_total": total,
                "samples_matched_le_500m": used,
                "match_share": used / total if total else 0.0,
                "median_nearest_distance_m": (
                    sorted(dists)[len(dists) // 2] if dists else None
                ),
                "top_fvg_route_labels": top_routes,
                "top_fvg_classes": top_classes,
            })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(json.dumps(rows, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
