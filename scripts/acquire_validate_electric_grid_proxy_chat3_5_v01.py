from __future__ import annotations
import csv, hashlib, json, re, ssl, time, urllib.parse, urllib.request, urllib.error
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import certifi
from pyproj import Transformer
from shapely.geometry import Point, shape, mapping
from shapely.ops import transform as shp_transform

ROOT = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_5")
WFS_DIR = ROOT / "fvg_wfs"
OSM_DIR = ROOT / "osm_overpass"
QA_DIR = ROOT / "derived_qa"
DSO_DIR = ROOT / "dso_official"
for p in (WFS_DIR, OSM_DIR, QA_DIR, DSO_DIR):
    p.mkdir(parents=True, exist_ok=True)

ACCESS_DATE = "2026-09-20"
BBOX = (45.55, 12.15, 46.75, 14.05)  # south, west, north, east; extraction envelope only
WFS_URL = ("https://serviziogc.regione.fvg.it/geoserver/ows?"
           "service=WFS&version=2.0.0&request=GetFeature&"
           "typeNames=CER:AREECONVENZIONALI_CP&outputFormat=application%2Fjson&srsName=EPSG%3A4326")
OVERPASS_PRIMARY = "https://overpass-api.de/api/interpreter"
OVERPASS_FALLBACK = "https://overpass.kumi.systems/api/interpreter"
SSL_CTX = ssl.create_default_context(cafile=certifi.where())
UA = "5-hub-fvg-chat3.5/1.0 (research; reproducible QA)"

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def fetch_bytes(url: str, timeout: int = 90) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
        return r.read()

def post_overpass(endpoint: str, query: str, timeout: int = 120) -> dict:
    data = urllib.parse.urlencode({"data": query}).encode()
    req = urllib.request.Request(
        endpoint, data=data,
        headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
        return json.loads(r.read())

def query_overpass(query: str, retries: int = 3) -> tuple[dict, str]:
    last = None
    for attempt in range(retries):
        try:
            return post_overpass(OVERPASS_PRIMARY, query), OVERPASS_PRIMARY
        except Exception as e:
            last = e
            time.sleep(12 + 12 * attempt)
    try:
        return post_overpass(OVERPASS_FALLBACK, query), OVERPASS_FALLBACK
    except Exception as e:
        raise RuntimeError(f"Overpass failed primary={last!r}; fallback={e!r}") from e

def center_of_element(el: dict):
    if el["type"] == "node":
        return el.get("lon"), el.get("lat")
    c = el.get("center") or {}
    return c.get("lon"), c.get("lat")

def parse_voltages(raw: str | None) -> list[int]:
    if not raw:
        return []
    vals = []
    for token in re.split(r"[;,/ ]+", str(raw)):
        token = token.strip()
        if token.isdigit():
            v = int(token)
            if 100 <= v <= 1_000_000:
                vals.append(v)
    return sorted(set(vals))

def norm_operator(raw: str | None) -> str:
    s = (raw or "").strip().lower()
    s2 = re.sub(r"[^a-z0-9]+", "", s)
    if "edistribuzione" in s2 or s2 in {"enel", "eneldistribuzione"}:
        return "e-distribuzione"
    if "acegasapsamga" in s2 or "acegas" in s2:
        return "AcegasApsAmga"
    if "secab" in s2:
        return "SECAB"
    if "terna" in s2:
        return "Terna"
    return raw or ""

def classify(tags: dict) -> tuple[str, bool, int | None]:
    role = (tags.get("substation") or "").strip().lower()
    volts = parse_voltages(tags.get("voltage"))
    vmax = max(volts) if volts else None
    if role == "transmission":
        return "MAJOR_TRANSMISSION", True, vmax
    if role == "distribution":
        return "DISTRIBUTION_SUBSTATION", True, vmax
    if vmax is not None and vmax >= 100000:
        return "HV_STATION_UNTYPED", True, vmax
    return "OTHER_SUBSTATION", False, vmax

def classify_cp_proxy(tags: dict) -> tuple[str, bool]:
    role = (tags.get("substation") or "").strip().lower()
    volts = parse_voltages(tags.get("voltage"))
    vmax = max(volts) if volts else None
    op = norm_operator(tags.get("operator"))
    dso = {"e-distribuzione", "AcegasApsAmga", "SECAB"}
    if vmax is not None and vmax >= 60000 and op in dso and role not in {"traction", "generation"}:
        return "A_DSO_HV_PLAUSIBLE", True
    if vmax is not None and vmax >= 60000 and not op and role == "distribution":
        return "B_DISTRIBUTION_HV_OPERATOR_MISSING", True
    return "NOT_CP_PROXY", False

def tile_grid():
    south, west, north, east = BBOX
    ys = [south, 46.00, 46.40, north]
    xs = [west, 12.80, 13.45, east]
    ncols = len(xs) - 1
    for yi in range(len(ys) - 1):
        for xi in range(ncols):
            yield yi * ncols + xi + 1, (ys[yi], xs[xi], ys[yi+1], xs[xi+1])

def osm_row(el: dict, endpoint: str, osm_ts: str) -> dict | None:
    lon, lat = center_of_element(el)
    if lon is None or lat is None:
        return None
    tags = el.get("tags") or {}
    qclass, qflag, vmax = classify(tags)
    cpclass, cpflag = classify_cp_proxy(tags)
    return {
        "osm_type": el["type"], "osm_id": el["id"],
        "lon": lon, "lat": lat,
        "name": tags.get("name", ""), "ref": tags.get("ref", ""),
        "voltage": tags.get("voltage", ""), "max_voltage_v": vmax or "",
        "substation": tags.get("substation", ""),
        "operator": tags.get("operator", ""),
        "operator_norm": norm_operator(tags.get("operator")),
        "location": tags.get("location", ""),
        "frequency": tags.get("frequency", ""),
        "qc_relevance_class": qclass,
        "qc_relevant_flag": int(qflag),
        "cp_proxy_class": cpclass,
        "cp_proxy_flag": int(cpflag),
        "source_endpoint": endpoint,
        "osm_base_timestamp": osm_ts,
        "tags_json": json.dumps(tags, ensure_ascii=False, sort_keys=True),
    }

def write_csv(path: Path, rows: list[dict]):
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

def query_mirror_tile(query: str, retries: int = 3):
    last = None
    for attempt in range(retries):
        try:
            return post_overpass(OVERPASS_FALLBACK, query, timeout=90)
        except Exception as e:
            last = e
            time.sleep(5 + attempt * 5)
    raise RuntimeError(f"Mirror tile failed after {retries} attempts: {last!r}")


def acquire_sources():
    wfs_path = WFS_DIR / "CER_AREECONVENZIONALI_CP_20260920.geojson"
    if not wfs_path.exists():
        wfs_path.write_bytes(fetch_bytes(WFS_URL, timeout=120))
    wfs = json.loads(wfs_path.read_text(encoding="utf-8"))

    # Complete inventory over an envelope that contains FVG plus border areas needed
    # by official EXTRAFVG service polygons. Raw responses retain endpoint/query/timestamp.
    all_by_id = {}
    tile_meta = []
    for tile_id, b in tile_grid():
        q = ('[out:json][timeout:120];'
             f'nwr["power"="substation"]({b[0]},{b[1]},{b[2]},{b[3]});'
             'out center tags qt;')
        raw_path = OSM_DIR / f"osm_power_substation_tile_{tile_id:02d}_v01.json"
        if raw_path.exists():
            obj = json.loads(raw_path.read_text(encoding="utf-8"))
        else:
            print(f"FULL_TILE_START {tile_id}", flush=True)
            obj = query_mirror_tile(q, retries=3)
            obj["_chat35_endpoint"] = OVERPASS_FALLBACK
            obj["_chat35_query"] = q
            raw_path.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
            print(f"FULL_TILE_DONE {tile_id} elements={len(obj.get('elements', []))}", flush=True)
        endpoint = obj.get("_chat35_endpoint", OVERPASS_FALLBACK)
        osm_ts = (obj.get("osm3s") or {}).get("timestamp_osm_base", "")
        tile_meta.append({"tile": tile_id, "endpoint": endpoint,
                          "osm_base_timestamp": osm_ts, "elements": len(obj.get("elements", [])),
                          "file": str(raw_path)})
        for el in obj.get("elements", []):
            row = osm_row(el, endpoint, osm_ts)
            if row:
                all_by_id[(row["osm_type"], row["osm_id"])] = row

    all_rows = sorted(all_by_id.values(), key=lambda r: (r["osm_type"], int(r["osm_id"])))
    write_csv(QA_DIR / "osm_substations_all_v01.csv", all_rows)

    # Derive QA subsets from the same complete raw extraction; no second live query.
    broad_relevant = [r for r in all_rows if r["qc_relevant_flag"] == 1]
    cp_proxy = [r for r in all_rows if r["cp_proxy_flag"] == 1]
    write_csv(QA_DIR / "osm_substations_relevant_qc_v01.csv", broad_relevant)
    write_csv(QA_DIR / "osm_substations_cp_proxy_qc_v01.csv", cp_proxy)
    return wfs_path, wfs, all_rows, cp_proxy, tile_meta

def make_relevant_geojson(rows: list[dict]):
    feats = []
    for r in rows:
        props = {k: v for k, v in r.items() if k not in {"lon", "lat", "tags_json"}}
        props["tags_json"] = r["tags_json"]
        feats.append({"type": "Feature", "geometry": {
            "type": "Point", "coordinates": [float(r["lon"]), float(r["lat"])]},
            "properties": props})
    out = {"type": "FeatureCollection", "features": feats}
    path = QA_DIR / "osm_substations_cp_proxy_qc_v01.geojson"
    path.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    return path

def service_areas(wfs: dict):
    rows = []
    for f in wfs.get("features", []):
        p = f.get("properties") or {}
        rows.append({
            "feature_id": f.get("id", ""),
            "AC_CODICE": p.get("AC_CODICE", ""),
            "GESTORE": p.get("GESTORE", ""),
            "EXTRAFVG": p.get("EXTRAFVG", ""),
            "ID1": p.get("ID1", ""),
            "geometry": shape(f["geometry"]),
        })
    return rows

def coverage_analysis(wfs: dict, all_rows: list[dict], relevant: list[dict]):
    areas = service_areas(wfs)
    to_utm = Transformer.from_crs("EPSG:4326", "EPSG:32633", always_xy=True).transform
    rel_points = [(r, Point(float(r["lon"]), float(r["lat"]))) for r in relevant]
    all_points = [(r, Point(float(r["lon"]), float(r["lat"]))) for r in all_rows]
    rel_utm = [(r, shp_transform(to_utm, p)) for r, p in rel_points]
    out = []
    for a in areas:
        geom = a["geometry"]
        geom_utm = shp_transform(to_utm, geom)
        inside_all = [r for r, p in all_points if geom.covers(p)]
        inside_rel = [r for r, p in rel_points if geom.covers(p)]
        gest = norm_operator(a["GESTORE"])
        inside_match = [r for r in inside_rel if norm_operator(r["operator"]) == gest]
        nearest_r, nearest_m = None, None
        if rel_utm:
            nearest_r, nearest_m = min(
                ((r, geom_utm.distance(pu)) for r, pu in rel_utm),
                key=lambda x: x[1])

        rec = {k: v for k, v in a.items() if k != "geometry"}
        rec.update({
            "GESTORE_NORM": gest,
            "osm_substations_any_inside": len(inside_all),
            "osm_qc_relevant_inside": len(inside_rel),
            "osm_qc_relevant_operator_match_inside": len(inside_match),
            "coverage_flag": "HAS_PLAUSIBLE_INSIDE" if inside_rel else "NO_PLAUSIBLE_INSIDE",
            "nearest_qc_relevant_distance_m": round(nearest_m, 1) if nearest_m is not None else "",
            "nearest_osm_type": nearest_r["osm_type"] if nearest_r else "",
            "nearest_osm_id": nearest_r["osm_id"] if nearest_r else "",
            "nearest_name": nearest_r["name"] if nearest_r else "",
            "nearest_operator": nearest_r["operator"] if nearest_r else "",
            "nearest_substation": nearest_r["substation"] if nearest_r else "",
            "nearest_voltage": nearest_r["voltage"] if nearest_r else "",
            "nearest_qc_class": nearest_r["qc_relevance_class"] if nearest_r else "",
        })
        out.append(rec)
    write_csv(QA_DIR / "cer_cp_osm_coverage_v01.csv", out)
    return out

def summarize(wfs, all_rows, relevant, coverage, tile_meta):
    mgr = Counter(str((f.get("properties") or {}).get("GESTORE", ""))
                  for f in wfs.get("features", []))
    ext = Counter(str((f.get("properties") or {}).get("EXTRAFVG", ""))
                  for f in wfs.get("features", []))
    internal = [r for r in coverage
                if str(r["EXTRAFVG"]) in {"0", "0.0", "False", "false"}]
    external = [r for r in coverage if r not in internal]
    summary = {
        "access_date": ACCESS_DATE,
        "official_service_areas": len(wfs.get("features", [])),
        "official_managers": dict(mgr),
        "official_extrafvg": dict(ext),
        "osm_substations_extracted_deduplicated": len(all_rows),
        "osm_cp_proxy_count": len(relevant),
        "osm_cp_proxy_classes": dict(Counter(r["cp_proxy_class"] for r in relevant)),
        "osm_cp_proxy_operator_counts": dict(Counter(
            r["operator_norm"] or "<missing>" for r in relevant).most_common()),
        "coverage_all_areas_with_plausible_inside": sum(
            r["coverage_flag"] == "HAS_PLAUSIBLE_INSIDE" for r in coverage),
        "coverage_all_areas_without_plausible_inside": sum(
            r["coverage_flag"] == "NO_PLAUSIBLE_INSIDE" for r in coverage),

        "coverage_internal_areas_total": len(internal),
        "coverage_internal_with_plausible_inside": sum(
            r["coverage_flag"] == "HAS_PLAUSIBLE_INSIDE" for r in internal),
        "coverage_internal_without_plausible_inside": sum(
            r["coverage_flag"] == "NO_PLAUSIBLE_INSIDE" for r in internal),
        "coverage_internal_with_operator_match_inside": sum(
            int(r["osm_qc_relevant_operator_match_inside"]) > 0 for r in internal),
        "coverage_internal_without_operator_match_inside": sum(
            int(r["osm_qc_relevant_operator_match_inside"]) == 0 for r in internal),
        "coverage_external_areas_total": len(external),
        "tile_metadata": tile_meta,
    }
    path = QA_DIR / "coverage_summary_v01.json"
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary, path

def manifest(paths: list[Path], extra: dict):
    records = []
    for path in paths:
        records.append({
            "path": str(path),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        })
    obj = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "access_date": ACCESS_DATE,
        "records": records,
        **extra,
    }
    path = ROOT / "source_manifest_v01.json"
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    return path

def main():
    wfs_path, wfs, all_rows, relevant, tile_meta = acquire_sources()
    rel_geo = make_relevant_geojson(relevant)
    coverage = coverage_analysis(wfs, all_rows, relevant)
    summary, summary_path = summarize(wfs, all_rows, relevant, coverage, tile_meta)
    paths = [wfs_path, QA_DIR / "osm_substations_all_v01.csv",
             QA_DIR / "osm_substations_relevant_qc_v01.csv",
             QA_DIR / "osm_substations_cp_proxy_qc_v01.csv", rel_geo,
             QA_DIR / "cer_cp_osm_coverage_v01.csv", summary_path]
    paths += [Path(x["file"]) for x in tile_meta]
    paths += sorted(DSO_DIR.glob("*"))
    paths += [QA_DIR / "dso_official_crosscheck_v01.csv"]

    man = manifest(paths, {
        "wfs_url": WFS_URL,
        "overpass_primary": OVERPASS_PRIMARY,
        "overpass_fallback": OVERPASS_FALLBACK,
        "dso_reference_urls": {
            "e-distribuzione": "https://www.e-distribuzione.it/content/dam/e-distribuzione/documenti/aree_critiche/Inversioni_di_flusso_2025.pdf",
            "AcegasApsAmga": "https://www.acegasapsamga.it/documents/d/acegasapsamga/piano-di-sviluppo-aaa-2025-29-definitivo-pdf",
            "SECAB": "https://www.secab.it/it/servizi/distribuzione"
        },
        "analysis_crs": "EPSG:32633",
        "qc_note": "The >=60 kV high-side rule is QA-only for identifying plausible AT/MT primary-substation geometries. It is not an approved model threshold, capacity threshold, or connection rule.",
    })
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print("MANIFEST", man)

if __name__ == "__main__":
    main()
