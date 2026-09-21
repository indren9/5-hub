#!/usr/bin/env python3
"""Materialize CER/Mosaicatura PRG 2018 D/H WFS as declared S4 fallback."""
from __future__ import annotations

import argparse
import hashlib
import json
import urllib.parse
import urllib.request
from pathlib import Path

import geopandas as gpd


BASE_URL = "https://serviziogc.regione.fvg.it/geoserver/wfs"
LAYERS = {
    "D": "CER:ZONE_INDUSTRIALI_ARTIG_D",
    "H": "CER:ZONE_COMMERCIALI_H",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def fetch_layer(type_name: str, out: Path) -> dict:
    params = {
        "service": "WFS",
        "version": "2.0.0",
        "request": "GetFeature",
        "typeNames": type_name,
        "outputFormat": "application/json",
        "srsName": "EPSG:6708",
    }
    url = BASE_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "5-HUB-FVG-chat-4.1/1.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        data = r.read()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    gdf = gpd.read_file(out)
    return {
        "type_name": type_name,
        "source_url": url,
        "path": str(out),
        "sha256": sha256_file(out),
        "bytes": out.stat().st_size,
        "features": len(gdf),
        "crs": str(gdf.crs),
        "geometry_types": sorted(gdf.geom_type.dropna().unique().tolist()),
        "columns": [c for c in gdf.columns if c != "geometry"],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, required=True)
    args = ap.parse_args()
    cfg = json.loads(args.config.read_text(encoding="utf-8"))
    root = Path(cfg["output_root"]) / cfg["source_cache_subdir"] / "cer2018"
    results = {}
    for key, type_name in LAYERS.items():
        out = root / f"CER_{key}_2018.geojson"
        results[key] = fetch_layer(type_name, out)
        print(json.dumps(results[key], ensure_ascii=False), flush=True)
    manifest = root / "CER_2018_SOURCE_MANIFEST_v01.json"
    manifest.write_text(json.dumps({
        "producer": Path(__file__).name,
        "role": "S4 historical fallback only",
        "layers": results,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"manifest": str(manifest), "layers": results}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
