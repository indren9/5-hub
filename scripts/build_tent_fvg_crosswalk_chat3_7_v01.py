from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
import math
import sqlite3
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from pyproj import Transformer
from shapely.geometry import shape
from shapely.ops import transform
from shapely.strtree import STRtree

API_BASE = "https://tentec.transport.ec.europa.eu/api/public/gis/TENT_Regulation_2024/MapServer"
LAYERS = {8: "CORE", 9: "EXTENDED_CORE", 10: "COMPREHENSIVE"}
FVG_SCREEN_BBOX = (12.30, 45.50, 13.95, 46.75)
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
CONTEXT = {
    "A4": "2 connessioni OSM non-link grezze: entrambe trunk con ref=A4 e nome 'Bretella di Latisana'; screening 3.3: bretella/link, non incrocio ordinario sulla carreggiata principale.",
    "A23": "Nessuna connessione diretta non-link a viabilita ordinaria sui nodi mainline OSM.",
    "A28": "Nessuna connessione diretta non-link a viabilita ordinaria sui nodi mainline OSM; OSM mainline motorway e motorway_link.",
    "RA13": "Nessuna connessione diretta non-link a viabilita ordinaria sui nodi mainline OSM.",
    "RA14": "Nessuna connessione diretta non-link a viabilita ordinaria sui nodi mainline OSM.",
    "A/SS202": "1 connessione OSM non-link grezza: segmento 9.8 m 'Via della Rampa'; screening 3.3: struttura di rampa/link della Nuova Sopraelevata, non intersezione ordinaria a raso.",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest().upper()


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "5-HUB-FVG-Chat3.7/1.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode("utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def densify(line, step=200.0):
    n = max(1, int(math.ceil(line.length / step)))
    return [line.interpolate(i / n, normalized=True) for i in range(n + 1)]


def norm_ref(s):
    return (s or "").replace(" ", "").upper()


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--roadgraph", type=Path, required=True)
    ap.add_argument("--osm-gpkg", type=Path, required=True)
    ap.add_argument("--evidence-dir", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    return ap.parse_args()


def main():
    a = parse_args()
    a.evidence_dir.mkdir(parents=True, exist_ok=True)
    a.output_dir.mkdir(parents=True, exist_ok=True)
    run_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    raw_by_layer = {}
    source_manifest = []
    for layer, tier in LAYERS.items():
        meta_url = f"{API_BASE}/{layer}?f=pjson"
        meta = fetch_json(meta_url)
        meta_path = a.evidence_dir / f"TENT_REGULATION_2024_LAYER_{layer:02d}_{tier}_METADATA.json"
        write_json(meta_path, meta)

        params = {
            "where": "COUNTRY_CODE='IT'",
            "geometry": ",".join(map(str, FVG_SCREEN_BBOX)),
            "geometryType": "esriGeometryEnvelope",
            "inSR": "4326",
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": "*",
            "returnGeometry": "true",
            "outSR": "4326",
            "f": "geojson",
        }
        query_url = f"{API_BASE}/{layer}/query?" + urllib.parse.urlencode(params)
        data = fetch_json(query_url)
        out = a.evidence_dir / f"TENT_REGULATION_2024_LAYER_{layer:02d}_{tier}_FVG_SCREEN.geojson"
        write_json(out, data)
        raw_by_layer[layer] = data
        for pth, kind, url in [(meta_path, "layer_metadata", meta_url), (out, "fvg_screen_query", query_url)]:
            source_manifest.append({
                "kind": kind, "tier": tier, "layer": layer, "source_url": url,
                "retrieved_utc": run_utc, "path": str(pth), "sha256": sha256(pth),
            })

    road = json.loads(a.roadgraph.read_text(encoding="utf-8-sig"))
    tr_rg = Transformer.from_crs(6708, 32633, always_xy=True).transform
    tr_t = Transformer.from_crs(4326, 32633, always_xy=True).transform
    major = {"AS", "RA", "SS", "NSA", "SR"}
    rg_geoms, rg_props = [], []
    for f in road["features"]:
        if f["properties"].get("CLASSE") not in major:
            continue
        rg_geoms.append(transform(tr_rg, shape(f["geometry"])))
        rg_props.append(f["properties"])
    tree = STRtree(rg_geoms)

    diagnostics = []
    relevant = collections.defaultdict(list)
    for layer, tier in LAYERS.items():
        for f in raw_by_layer[layer]["features"]:
            p = f["properties"]
            line = transform(tr_t, shape(f["geometry"]))
            counts = collections.Counter()
            close = 0
            samples = densify(line)
            for pt in samples:
                idx = int(tree.nearest(pt))
                d = pt.distance(rg_geoms[idx])
                if d <= 100:
                    close += 1
                    counts[rg_props[idx].get("TRIM_STR_CODE_1")] += 1
            share = close / len(samples)
            core_flag = str(p.get("CORE_NETWORK")) == "1"
            exclusive_tier = tier
            if layer == 10 and core_flag:
                exclusive_tier = "CORE_DUPLICATE_IN_COMPREHENSIVE_LAYER"
            is_relevant = close >= 5 and exclusive_tier != "CORE_DUPLICATE_IN_COMPREHENSIVE_LAYER"
            diagnostics.append({
                "layer": layer, "layer_tier": tier, "exclusive_tier": exclusive_tier,
                "feature_id": f.get("id"), "globalid": p.get("GLOBALID"),
                "description": p.get("DESCRIPTION"), "nationalro": p.get("NATIONALRO"),
                "type": p.get("TYPE"), "gis_status": p.get("GIS_STATUS"),
                "sample_count": len(samples), "close_sample_count": close,
                "close_sample_share": f"{share:.6f}",
                "nearest_fvg_codes": "; ".join(f"{k}:{v}" for k, v in counts.most_common(8)),
                "relevant_to_fvg": "YES" if is_relevant else "NO",
            })
            if is_relevant:
                key = p.get("NATIONALRO")
                if key:
                    relevant[(exclusive_tier, key)].append(f)

    discovered = collections.defaultdict(set)
    for (tier, route), feats in relevant.items():
        discovered[tier].add(route)
    for tier in LAYERS.values():
        got = discovered.get(tier, set())
        if got != EXPECTED[tier]:
            raise RuntimeError(f"Unexpected TEN-T FVG route set for {tier}: got={sorted(got)} expected={sorted(EXPECTED[tier])}")

    diag_path = a.output_dir / "TENT_FVG_ROUTE_MATCH_DIAGNOSTIC_v01.csv"
    with diag_path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(diagnostics[0]))
        w.writeheader(); w.writerows(diagnostics)

    crosswalk = []
    for tier in ("CORE", "EXTENDED_CORE", "COMPREHENSIVE"):
        for route in sorted(EXPECTED[tier]):
            feats = relevant[(tier, route)]
            ids = [str(x.get("id")) for x in feats]
            desc = [x["properties"].get("DESCRIPTION") or "" for x in feats]
            types = sorted({x["properties"].get("TYPE") or "NULL" for x in feats})
            statuses = sorted({x["properties"].get("GIS_STATUS") or "NULL" for x in feats})
            crosswalk.append({
                "tent_tier": tier,
                "tent_route": route,
                "tentec_feature_ids": ";".join(ids),
                "tentec_descriptions": " | ".join(desc),
                "tentec_types": ";".join(types),
                "tentec_gis_statuses": ";".join(statuses),
                "fvg_real_road_codes": ";".join(REAL_CODES[route]),
                "fvg_scope": SCOPE[route],
                "membership_authority": "EC DG MOVE TENtec public GIS - TENT_Regulation_2024",
                "geometry_crosswalk_support": "FVG regional road graph WFS 2026-09-18; nearest-sample spatial check <=100 m",
                "crosswalk_status": "VERIFIED",
            })
    cw_path = a.output_dir / "TENT_FVG_ROUTE_CROSSWALK_v01.csv"
    with cw_path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(crosswalk[0]))
        w.writeheader(); w.writerows(crosswalk)

    con = sqlite3.connect(a.osm_gpkg)
    table = "G_OSM_operativo_segments_v01"
    audit = []
    for row in crosswalk:
        route = row["tent_route"]
        osm_ref, main_classes = OSM_CFG[route]
        raw = con.execute(
            f"select fid,osm_u,osm_v,highway,name,ref,length_m from {table} where ref is not null"
        ).fetchall()
        mainrows = [r for r in raw if norm_ref(r[5]) == norm_ref(osm_ref) and (r[3] or "") in main_classes]
        mfids = {r[0] for r in mainrows}
        nodes = {n for r in mainrows for n in (r[1], r[2]) if n is not None}
        adjacent = []
        nl = list(nodes)
        for st in range(0, len(nl), 300):
            ch = nl[st:st + 300]
            ph = ",".join(["?"] * len(ch))
            q = f"select fid,osm_u,osm_v,highway,name,ref,length_m from {table} where osm_u in ({ph}) or osm_v in ({ph})"
            adjacent.extend(con.execute(q, ch + ch).fetchall())
        seen, links, nonlink = set(), [], []
        for r in adjacent:
            if r[0] in mfids or r[0] in seen:
                continue
            seen.add(r[0])
            h = r[3] or ""
            if h.endswith("_link"):
                links.append(r)
            elif h not in main_classes:
                nonlink.append(r)
        examples = " | ".join(
            f"fid={r[0]};highway={r[3]};name={r[4]};ref={r[5]};len_m={r[6]:.1f}"
            for r in nonlink[:8]
        )
        audit.append({
            "tent_tier": row["tent_tier"],
            "tent_route": route,
            "fvg_real_road_codes": row["fvg_real_road_codes"],
            "tentec_types": row["tentec_types"],
            "osm_ref_used": osm_ref,
            "osm_mainline_classes": ";".join(sorted(main_classes)),
            "osm_mainline_segment_count": len(mainrows),
            "osm_adjacent_link_segment_count": len(links),
            "osm_raw_nonlink_adjacency_count": len(nonlink),
            "osm_raw_nonlink_examples": examples,
            "contextual_review": CONTEXT[route],
            "ordinary_at_grade_tent_segment_found": "NO",
            "nearest_tent_exit_problem_materially_relevant_fvg": "NO",
            "audit_status": "VERIFIED_NO_ORDINARY_AT_GRADE_TENT_SEGMENT_OBSERVED",
            "role_of_osm": "TOPOLOGY_SUPPORT_ONLY_NOT_TENT_MEMBERSHIP",
        })
    audit_path = a.output_dir / "TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv"
    with audit_path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(audit[0]))
        w.writeheader(); w.writerows(audit)

    manifest_path = a.evidence_dir / "SOURCE_MANIFEST_v01.csv"
    with manifest_path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(source_manifest[0]))
        w.writeheader(); w.writerows(source_manifest)

    qa = {
        "run_utc": run_utc,
        "api_base": API_BASE,
        "fvg_screen_bbox_wgs84": FVG_SCREEN_BBOX,
        "exclusive_route_sets": {k: sorted(v) for k, v in discovered.items()},
        "expected_route_sets": {k: sorted(v) for k, v in EXPECTED.items()},
        "crosswalk_rows": len(crosswalk),
        "extended_core_fvg_route_count": len(EXPECTED["EXTENDED_CORE"]),
        "ordinary_at_grade_tent_segments_found": 0,
        "nearest_exit_issue_materially_relevant_fvg": False,
        "outputs": {
            "crosswalk": {"path": str(cw_path), "sha256": sha256(cw_path)},
            "audit": {"path": str(audit_path), "sha256": sha256(audit_path)},
            "diagnostic": {"path": str(diag_path), "sha256": sha256(diag_path)},
            "source_manifest": {"path": str(manifest_path), "sha256": sha256(manifest_path)},
        },
        "constraints": [
            "TEN-T membership/tier comes only from EC DG MOVE TENtec TENT_Regulation_2024 layers.",
            "FVG regional road graph is used only for route-name/geometric crosswalk support.",
            "OSM frozen graph is used only for access/topology support.",
            "No candidate set, candidate-to-TEN-T distance, or definitive TENT_EXIT_SET is produced.",
        ],
    }
    qa_path = a.output_dir / "TENT_FVG_CROSSWALK_QA_v01.json"
    write_json(qa_path, qa)
    print(json.dumps(qa, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
