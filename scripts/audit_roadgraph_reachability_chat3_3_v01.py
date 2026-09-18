from __future__ import annotations

import json
import os
from pathlib import Path

import networkx as nx
from pyproj import Transformer
from scipy.spatial import cKDTree
from shapely.geometry import shape

os.environ.setdefault("PROJ_DATA", r"C:\Program Files\QGIS 3.44.14\share\proj")
RAW = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\01_raw_data\F3_CHAT_3_3\GRAFO_STRADALE_FVG_WFS_20260918.geojson")
OUT = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\05_intermediate_outputs\F3_CHAT_3_3\ROADGRAPH_REACHABILITY_TEST_v01.json")

# Representative city-centre coordinates are only test probes, not model origins.
PROBES = {
    "Pordenone": (12.6605, 45.9564),
    "Udine": (13.2346, 46.0711),
    "Gorizia": (13.6200, 45.9411),
    "Trieste": (13.7768, 45.6495),
    "Tolmezzo": (13.0150, 46.4010),
    "Tarvisio": (13.5780, 46.5050),
    "Lignano_Sabbiadoro": (13.1260, 45.6870),
}
def main() -> None:
    data = json.load(RAW.open(encoding="utf-8"))
    g = nx.Graph()
    for feat in data["features"]:
        geom = shape(feat["geometry"])
        for part in ([geom] if geom.geom_type == "LineString" else geom.geoms):
            a0, b0 = part.coords[0], part.coords[-1]
            a = (round(a0[0], 3), round(a0[1], 3))
            b = (round(b0[0], 3), round(b0[1], 3))
            length = float(part.length)
            if g.has_edge(a, b):
                g[a][b]["weight"] = min(g[a][b]["weight"], length)
            else:
                g.add_edge(a, b, weight=length)

    nodes = list(g.nodes)
    tree = cKDTree(nodes)
    tr = Transformer.from_crs(4326, 6708, always_xy=True)
    anchors = {}
    for name, (lon, lat) in PROBES.items():
        x, y = tr.transform(lon, lat)
        d, idx = tree.query((x, y), k=1)
        anchors[name] = {
            "probe_lon": lon, "probe_lat": lat,
            "nearest_graph_node": nodes[int(idx)],
            "probe_to_node_m": float(d),
        }

    distances = {}
    names = list(PROBES)
    for a in names:
        distances[a] = {}
        src = tuple(anchors[a]["nearest_graph_node"])
        lengths = nx.single_source_dijkstra_path_length(g, src, weight="weight")
        for b in names:
            dst = tuple(anchors[b]["nearest_graph_node"])
            distances[a][b] = None if dst not in lengths else lengths[dst] / 1000.0
    result = {
        "method": "Undirected endpoint graph, edge weight = geometry length.",
        "warning": (
            "This is a connectivity sanity check only. It ignores one-way and "
            "vehicle restrictions and cannot be used as production routing."
        ),
        "probes": anchors,
        "route_distance_km": distances,
        "all_probe_pairs_reachable": all(
            distances[a][b] is not None for a in names for b in names
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    json.dump(result, OUT.open("w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
