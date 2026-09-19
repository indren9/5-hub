from __future__ import annotations

import argparse
import collections
import csv
import json
import math
import os
import sqlite3
import tempfile
from pathlib import Path

from pyproj import Transformer
from shapely.geometry import shape
from shapely.ops import transform
from shapely.strtree import STRtree

LAYERS = {8: "CORE", 9: "EXTENDED_CORE", 10: "COMPREHENSIVE"}
EXPECTED = {
    "CORE": {"A4", "A23", "RA13", "RA14", "A/SS202"},
    "EXTENDED_CORE": set(),
    "COMPREHENSIVE": {"A28"},
}
REAL_CODES = {
    "A4": ["AS A4"],
    "A23": ["AS A23"],
    "RA13": ["RA 13"],
    "RA14": ["RA 14"],
    "A/SS202": ["SS 202", "NSA 326", "NSA 314"],
    "A28": ["AS A28"],
}
OSM_CFG = {
    "A4": ("A4", {"motorway"}),
    "A23": ("A23", {"motorway"}),
    "A28": ("A28", {"motorway"}),
    "RA13": ("RA13", {"motorway"}),
    "RA14": ("RA14", {"motorway"}),
    "A/SS202": ("SS202", {"trunk"}),
}
SCOPE = {
    "A4": "confine regionale occidentale / area Portogruaro-Latisana -> Palmanova -> Sistiana-Visogliano",
    "A23": "Palmanova -> Udine -> Tarvisio -> confine IT/AT",
    "RA13": "Sistiana-Visogliano -> Villa Opicina -> Padriciano",
    "RA14": "Villa Opicina -> Fernetti / confine IT/SI",
    "A/SS202": "Padriciano -> asse SS202/GVT -> Rabuiese / confine IT/SI",
    "A28": "confine Veneto/FVG presso Sacile-Schiavoi -> Pordenone -> Portogruaro/A4",
}
SOURCE_FILES = {
    8: "TENT_REGULATION_2024_LAYER_08_CORE_FVG_SCREEN.geojson",
    9: "TENT_REGULATION_2024_LAYER_09_EXTENDED_CORE_FVG_SCREEN.geojson",
    10: "TENT_REGULATION_2024_LAYER_10_COMPREHENSIVE_FVG_SCREEN.geojson",
}


def parse_args():
    p = argparse.ArgumentParser(
        description="Build deterministic TEN-T/FVG route crosswalk and OSM-only access diagnostic."
    )
    p.add_argument("--source-dir", type=Path, required=True)
    p.add_argument("--roadgraph", type=Path, required=True)
    p.add_argument("--osm-gpkg", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    return p.parse_args()


def atomic_write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    os.close(fd)
    tmp_path = Path(tmp)
    try:
        with tmp_path.open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(rows)
        os.replace(tmp_path, path)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def densify(line, step=200.0):
    n = max(1, int(math.ceil(line.length / step)))
    return [line.interpolate(i / n, normalized=True) for i in range(n + 1)]


def norm_ref(value):
    return (value or "").replace(" ", "").upper()


def feature_id(feature):
    value = feature.get("id")
    if value is None:
        value = feature.get("properties", {}).get("OBJECTID")
    try:
        return int(value)
    except (TypeError, ValueError):
        return str(value)


def main():
    a = parse_args()
    a.output_dir.mkdir(parents=True, exist_ok=True)

    raw_by_layer = {}
    for layer, filename in SOURCE_FILES.items():
        p = a.source_dir / filename
        if not p.exists():
            raise FileNotFoundError(f"Missing canonical TEN-T source: {p}")
        raw_by_layer[layer] = json.loads(p.read_text(encoding="utf-8-sig"))

    road = json.loads(a.roadgraph.read_text(encoding="utf-8-sig"))
    tr_rg = Transformer.from_crs(6708, 32633, always_xy=True).transform
    tr_t = Transformer.from_crs(4326, 32633, always_xy=True).transform

    major = {"AS", "RA", "SS", "NSA", "SR"}
    rg_geoms = []
    rg_props = []
    for f in road["features"]:
        if f["properties"].get("CLASSE") not in major:
            continue
        rg_geoms.append(transform(tr_rg, shape(f["geometry"])))
        rg_props.append(f["properties"])
    tree = STRtree(rg_geoms)

    route_match_rows = []
    relevant = collections.defaultdict(list)

    for layer, tier in LAYERS.items():
        features = sorted(raw_by_layer[layer].get("features", []), key=feature_id)
        for feat in features:
            props = feat["properties"]
            geom = transform(tr_t, shape(feat["geometry"]))
            counts = collections.Counter()
            close = 0
            samples = densify(geom)
            for pt in samples:
                idx = int(tree.nearest(pt))
                dist = pt.distance(rg_geoms[idx])
                if dist <= 100:
                    close += 1
                    counts[rg_props[idx].get("TRIM_STR_CODE_1")] += 1

            share = close / len(samples)
            core_flag = str(props.get("CORE_NETWORK")) == "1"
            exclusive_tier = tier
            if layer == 10 and core_flag:
                exclusive_tier = "CORE_DUPLICATE_IN_COMPREHENSIVE_LAYER"

            is_relevant = (
                close >= 5
                and exclusive_tier != "CORE_DUPLICATE_IN_COMPREHENSIVE_LAYER"
            )
            route_match_rows.append(
                {
                    "layer": layer,
                    "layer_tier": tier,
                    "exclusive_tier": exclusive_tier,
                    "feature_id": feature_id(feat),
                    "description": props.get("DESCRIPTION"),
                    "nationalro": props.get("NATIONALRO"),
                    "type": props.get("TYPE"),
                    "gis_status": props.get("GIS_STATUS"),
                    "sample_count": len(samples),
                    "close_sample_count": close,
                    "close_sample_share": f"{share:.6f}",
                    "nearest_fvg_codes": "; ".join(
                        f"{k}:{v}" for k, v in counts.most_common(8)
                    ),
                    "official_section_in_fvg_crosswalk": "YES" if is_relevant else "NO",
                    "diagnostic_role": "GEOMETRIC_MATCH_SUPPORT_ONLY",
                }
            )
            if is_relevant:
                route = props.get("NATIONALRO")
                if route:
                    relevant[(exclusive_tier, route)].append(feat)

    discovered = collections.defaultdict(set)
    for tier, route in relevant:
        discovered[tier].add(route)
    for tier in LAYERS.values():
        got = discovered.get(tier, set())
        if got != EXPECTED[tier]:
            raise RuntimeError(
                f"Unexpected TEN-T FVG route set for {tier}: "
                f"got={sorted(got)} expected={sorted(EXPECTED[tier])}"
            )

    route_match_rows.sort(
        key=lambda r: (
            int(r["layer"]),
            str(r["feature_id"]),
        )
    )
    route_match_path = a.output_dir / "TENT_FVG_ROUTE_MATCH_DIAGNOSTIC_v01.csv"
    atomic_write_csv(
        route_match_path,
        route_match_rows,
        list(route_match_rows[0].keys()),
    )

    crosswalk_rows = []
    for tier in ("CORE", "EXTENDED_CORE", "COMPREHENSIVE"):
        for route in sorted(EXPECTED[tier]):
            feats = sorted(relevant[(tier, route)], key=feature_id)
            ids = [str(feature_id(x)) for x in feats]
            descriptions = [x["properties"].get("DESCRIPTION") or "" for x in feats]
            types = sorted({x["properties"].get("TYPE") or "NULL" for x in feats})
            statuses = sorted(
                {x["properties"].get("GIS_STATUS") or "NULL" for x in feats}
            )
            crosswalk_rows.append(
                {
                    "tent_tier": tier,
                    "tent_route_axis": route,
                    "official_section_count": len(feats),
                    "tentec_feature_ids": ";".join(ids),
                    "tentec_descriptions": " | ".join(descriptions),
                    "tentec_types": ";".join(types),
                    "tentec_gis_statuses": ";".join(statuses),
                    "fvg_real_road_codes": ";".join(REAL_CODES[route]),
                    "fvg_scope": SCOPE[route],
                    "membership_authority": (
                        "EC DG MOVE TENtec public GIS - TENT_Regulation_2024"
                    ),
                    "geometry_crosswalk_support": (
                        "FVG regional road graph WFS; 200 m sampling; "
                        "nearest major-road support <=100 m"
                    ),
                    "crosswalk_status": "VERIFIED",
                }
            )

    if len(crosswalk_rows) != 6:
        raise RuntimeError(f"Expected 6 route-axis records, got {len(crosswalk_rows)}")
    if sum(int(r["official_section_count"]) for r in crosswalk_rows) != 11:
        raise RuntimeError("Expected 11 official TENtec sections in the 6 route-axis records")

    crosswalk_path = a.output_dir / "TENT_FVG_ROUTE_CROSSWALK_v01.csv"
    atomic_write_csv(
        crosswalk_path,
        crosswalk_rows,
        list(crosswalk_rows[0].keys()),
    )

    con = sqlite3.connect(a.osm_gpkg)
    table = "G_OSM_operativo_segments_v01"
    all_ref_rows = con.execute(
        f"select fid,osm_u,osm_v,highway,name,ref,length_m "
        f"from {table} where ref is not null order by fid"
    ).fetchall()

    osm_rows = []
    for row in crosswalk_rows:
        route = row["tent_route_axis"]
        osm_ref, main_classes = OSM_CFG[route]
        mainrows = [
            r
            for r in all_ref_rows
            if norm_ref(r[5]) == norm_ref(osm_ref)
            and (r[3] or "") in main_classes
        ]
        main_fids = {r[0] for r in mainrows}
        nodes = sorted({n for r in mainrows for n in (r[1], r[2]) if n is not None})

        adjacent = []
        for start in range(0, len(nodes), 300):
            chunk = nodes[start : start + 300]
            placeholders = ",".join(["?"] * len(chunk))
            q = (
                f"select fid,osm_u,osm_v,highway,name,ref,length_m from {table} "
                f"where osm_u in ({placeholders}) or osm_v in ({placeholders}) "
                f"order by fid"
            )
            adjacent.extend(con.execute(q, chunk + chunk).fetchall())

        seen = set()
        links = []
        nonlink = []
        for r in sorted(adjacent, key=lambda x: x[0]):
            if r[0] in main_fids or r[0] in seen:
                continue
            seen.add(r[0])
            highway = r[3] or ""
            if highway.endswith("_link"):
                links.append(r)
            elif highway not in main_classes:
                nonlink.append(r)

        examples = " | ".join(
            f"fid={r[0]};highway={r[3]};name={r[4]};ref={r[5]};len_m={r[6]:.1f}"
            for r in nonlink[:8]
        )
        machine_status = (
            "NO_RAW_NONLINK_ADJACENCY"
            if not nonlink
            else "RAW_NONLINK_ADJACENCY_REQUIRES_DOCUMENTARY_REVIEW"
        )
        osm_rows.append(
            {
                "tent_tier": row["tent_tier"],
                "tent_route_axis": route,
                "fvg_real_road_codes": row["fvg_real_road_codes"],
                "osm_ref_used": osm_ref,
                "osm_mainline_classes": ";".join(sorted(main_classes)),
                "osm_mainline_segment_count": len(mainrows),
                "osm_adjacent_link_segment_count": len(links),
                "osm_raw_nonlink_adjacency_count": len(nonlink),
                "osm_raw_nonlink_examples": examples,
                "machine_status": machine_status,
                "requires_documentary_review": "YES" if nonlink else "NO",
                "role_of_osm": (
                    "AUTOMATIC_TOPOLOGY_DIAGNOSTIC_ONLY; "
                    "NOT_TENT_MEMBERSHIP; NOT_FINAL_AT_GRADE_CONCLUSION"
                ),
            }
        )
    con.close()

    osm_path = a.output_dir / "TENT_FVG_OSM_ACCESS_DIAGNOSTIC_v01.csv"
    atomic_write_csv(osm_path, osm_rows, list(osm_rows[0].keys()))

    print(
        json.dumps(
            {
                "route_axis_records": len(crosswalk_rows),
                "official_tentec_sections": sum(
                    int(r["official_section_count"]) for r in crosswalk_rows
                ),
                "osm_diagnostic_records": len(osm_rows),
                "outputs": [
                    str(route_match_path),
                    str(crosswalk_path),
                    str(osm_path),
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
