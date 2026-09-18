from __future__ import annotations

import argparse
import collections
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import networkx as nx
import requests
from scipy.spatial import cKDTree
from shapely import normalize
from shapely.geometry import shape

WFS = "https://serviziogc.regione.fvg.it/geoserver/wfs"
TYPE_NAME = "RETI_TRASP:GRAFO_STRADALE_FVG"
PAGE_SIZE = 5000
RAW_ROOT = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\01_raw_data\F3_CHAT_3_3")
OUT_ROOT = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\05_intermediate_outputs\F3_CHAT_3_3")
RAW_PATH = RAW_ROOT / "GRAFO_STRADALE_FVG_WFS_20260918.geojson"
METRICS_PATH = OUT_ROOT / "ROADGRAPH_AUDIT_METRICS_v01.json"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()
def source_count(session: requests.Session) -> int:
    params = {
        "service": "WFS", "version": "2.0.0", "request": "GetFeature",
        "typeNames": TYPE_NAME, "resultType": "hits",
    }
    r = session.get(WFS, params=params, timeout=60)
    r.raise_for_status()
    text = r.text
    marker = 'numberMatched="'
    return int(text.split(marker, 1)[1].split('"', 1)[0])


def download_pages(session: requests.Session, total: int):
    RAW_ROOT.mkdir(parents=True, exist_ok=True)
    first = True
    crs = None
    with RAW_PATH.open("w", encoding="utf-8") as out:
        out.write('{"type":"FeatureCollection","features":[')
        for start in range(0, total, PAGE_SIZE):
            params = {
                "service": "WFS", "version": "2.0.0", "request": "GetFeature",
                "typeNames": TYPE_NAME, "outputFormat": "application/json",
                "count": PAGE_SIZE, "startIndex": start,
            }
            r = session.get(WFS, params=params, timeout=180)
            r.raise_for_status()
            page = r.json()
            crs = crs or page.get("crs")
            for feat in page["features"]:
                if not first:
                    out.write(",")
                json.dump(feat, out, ensure_ascii=False, separators=(",", ":"))
                first = False
                yield feat
            print(f"downloaded {min(start + PAGE_SIZE, total)}/{total}", flush=True)
        out.write('],"crs":')
        json.dump(crs, out, ensure_ascii=False, separators=(",", ":"))
        out.write("}")
def stored_features():
    with RAW_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)
    for feat in data["features"]:
        yield feat


def counter_json(counter: collections.Counter) -> dict[str, int]:
    return {str(k): int(v) for k, v in counter.most_common()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force-download", action="store_true")
    args = parser.parse_args()

    RAW_ROOT.mkdir(parents=True, exist_ok=True)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    total = source_count(session)
    use_download = args.force_download or not RAW_PATH.exists()
    features = download_pages(session, total) if use_download else stored_features()

    graph = nx.MultiGraph()
    counts = {name: collections.Counter() for name in [
        "geometry_type", "classe", "dir", "entext", "allowance",
        "lanes", "geometry_reversed", "fonte_int", "dbprior_stato",
        "dbprior_tipo_tratto", "data_inizio", "data_fine",
    ]}
    nulls = collections.Counter()
    geom_hashes = collections.Counter()
    total_length_m = 0.0
    invalid = empty = zero_length = 0
    n_features = 0
    n_parts = 0
    fields = [
        "DIR", "ENTEXT", "CLASSE", "ENTE_GESTORE", "TRIM_USAGE_ALLOWANCE",
        "DBPRIOR_TIPO_TRATTO", "DBPRIOR_STATO", "TRIM_LANES",
        "FONTE_INT", "DATA_INIZIO", "DATA_FINE", "GEOMETRY_REVERSED",
    ]

    for feat in features:
        n_features += 1
        props = feat.get("properties", {})
        geom = shape(feat["geometry"]) if feat.get("geometry") else None
        for fld in fields:
            if props.get(fld) is None:
                nulls[fld] += 1
        counts["classe"][props.get("CLASSE")] += 1
        counts["dir"][props.get("DIR")] += 1
        counts["entext"][props.get("ENTEXT")] += 1
        counts["allowance"][props.get("TRIM_USAGE_ALLOWANCE")] += 1
        counts["lanes"][props.get("TRIM_LANES")] += 1
        counts["geometry_reversed"][props.get("GEOMETRY_REVERSED")] += 1
        counts["fonte_int"][props.get("FONTE_INT")] += 1
        counts["dbprior_stato"][props.get("DBPRIOR_STATO")] += 1
        counts["dbprior_tipo_tratto"][props.get("DBPRIOR_TIPO_TRATTO")] += 1
        counts["data_inizio"][props.get("DATA_INIZIO")] += 1
        counts["data_fine"][props.get("DATA_FINE")] += 1
        if geom is None:
            empty += 1
            continue
        counts["geometry_type"][geom.geom_type] += 1
        if geom.is_empty:
            empty += 1
            continue
        if not geom.is_valid:
            invalid += 1
        if geom.length == 0:
            zero_length += 1
        total_length_m += geom.length
        try:
            geom_hashes[hashlib.sha256(normalize(geom).wkb).hexdigest()] += 1
        except Exception:
            pass

        parts = list(geom.geoms) if geom.geom_type == "MultiLineString" else [geom]
        for part in parts:
            if part.is_empty or len(part.coords) < 2:
                continue
            n_parts += 1
            a0 = part.coords[0]
            b0 = part.coords[-1]
            a = (round(float(a0[0]), 3), round(float(a0[1]), 3))
            b = (round(float(b0[0]), 3), round(float(b0[1]), 3))
            graph.add_edge(a, b, length=float(part.length), classe=props.get("CLASSE"))

    components = list(nx.connected_components(graph))
    components.sort(key=len, reverse=True)
    node_to_comp = {}
    for idx, comp in enumerate(components):
        for node in comp:
            node_to_comp[node] = idx
    comp_edges = collections.Counter()
    comp_length = collections.Counter()
    for u, v, data in graph.edges(data=True):
        c = node_to_comp[u]
        comp_edges[c] += 1
        comp_length[c] += float(data["length"])
    degrees = dict(graph.degree())
    dangling = [n for n, d in degrees.items() if d == 1]
    isolated_edges = sum(
        1 for u, v in graph.edges()
        if degrees.get(u) == 1 and degrees.get(v) == 1
    )

    near_gap = {"le_0_1m": 0, "le_1m": 0, "le_5m": 0}
    if len(graph) > 1 and dangling:
        nodes = list(graph.nodes())
        tree = cKDTree(nodes)
        dists, _ = tree.query(dangling, k=2)
        nearest = dists[:, 1]
        near_gap["le_0_1m"] = int((nearest <= 0.1).sum())
        near_gap["le_1m"] = int((nearest <= 1.0).sum())
        near_gap["le_5m"] = int((nearest <= 5.0).sum())

    duplicate_groups = [v for v in geom_hashes.values() if v > 1]
    duplicate_features = int(sum(duplicate_groups))
    giant_edges = int(comp_edges.get(0, 0))
    giant_length = float(comp_length.get(0, 0.0))
    metrics = {
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source": {
            "wfs": WFS,
            "type_name": TYPE_NAME,
            "number_matched": total,
            "raw_path": str(RAW_PATH),
            "raw_sha256": sha256_file(RAW_PATH),
            "reported_crs": "urn:ogc:def:crs:EPSG::6708",
        },
        "features_processed": n_features,
        "geometry": {
            "types": counter_json(counts["geometry_type"]),
            "invalid": invalid,
            "empty_or_missing": empty,
            "zero_length": zero_length,
            "total_length_km": total_length_m / 1000.0,
            "normalized_duplicate_groups": len(duplicate_groups),
            "normalized_duplicate_features": duplicate_features,
        },
        "attributes": {
            "class": counter_json(counts["classe"]),
            "dir": counter_json(counts["dir"]),
            "entext": counter_json(counts["entext"]),
            "trim_usage_allowance": counter_json(counts["allowance"]),
            "trim_lanes": counter_json(counts["lanes"]),
            "geometry_reversed": counter_json(counts["geometry_reversed"]),
            "fonte_int": counter_json(counts["fonte_int"]),
            "dbprior_stato": counter_json(counts["dbprior_stato"]),
            "dbprior_tipo_tratto": counter_json(counts["dbprior_tipo_tratto"]),
            "null_counts": counter_json(nulls),
        },
        "topology_endpoint_graph_1mm": {
            "parts": n_parts,
            "nodes": graph.number_of_nodes(),
            "edges": graph.number_of_edges(),
            "connected_components": len(components),
            "giant_component_nodes": len(components[0]) if components else 0,
            "giant_component_edges": giant_edges,
            "giant_component_edge_share": giant_edges / graph.number_of_edges() if graph.number_of_edges() else 0,
            "giant_component_length_km": giant_length / 1000.0,
            "giant_component_length_share": giant_length / total_length_m if total_length_m else 0,
            "dangling_nodes_degree1": len(dangling),
            "isolated_edges": isolated_edges,
            "degree_distribution": counter_json(collections.Counter(degrees.values())),
            "dangling_nearest_other_node": near_gap,
            "largest_components": [
                {
                    "component": i,
                    "nodes": len(comp),
                    "edges": int(comp_edges.get(i, 0)),
                    "length_km": float(comp_length.get(i, 0.0)) / 1000.0,
                }
                for i, comp in enumerate(components[:20])
            ],
        },
        "method_notes": [
            "Topologia misurata sugli endpoint delle feature/parti, arrotondati a 1 mm.",
            "I dangling includono cul-de-sac e limiti reali: non sono automaticamente errori.",
            "Il controllo near-gap misura la distanza al nodo distinto più vicino, non prova connessione stradale.",
            "DIR e TRIM_USAGE_ALLOWANCE sono censiti ma non interpretati semanticamente dal codice.",
        ],
    }
    with METRICS_PATH.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)
    print(json.dumps(metrics["topology_endpoint_graph_1mm"], indent=2))
    print("metrics:", METRICS_PATH)
    print("raw:", RAW_PATH, metrics["source"]["raw_sha256"])


if __name__ == "__main__":
    main()
