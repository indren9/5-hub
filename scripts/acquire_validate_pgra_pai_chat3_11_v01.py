from __future__ import annotations
import csv, hashlib, json, re, subprocess, sys, zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

ROOT = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_11")
PGRA = ROOT / "pgra"
PAI = ROOT / "pai"
SUPPORT = ROOT / "regional_support"
DISC = ROOT / "official_discipline"
for p in (ROOT, PGRA, PAI, SUPPORT, DISC):
    p.mkdir(parents=True, exist_ok=True)

UA = "5-HUB-FVG-Chat3.11/1.0 reproducible research"
S = requests.Session()
S.headers.update({"User-Agent": UA})
NOW = datetime.now(timezone.utc).isoformat()
MANIFEST = []
QA = {"generated_utc": NOW, "checks": {}, "notes": []}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()
def download(url: str, path: Path, params: dict | None = None, timeout: int = 180):
    if path.exists() and path.stat().st_size > 0:
        prepared = requests.Request("GET", url, params=params).prepare().url
        MANIFEST.append({
            "path": str(path.relative_to(ROOT)), "url": prepared,
            "bytes": path.stat().st_size, "sha256": sha256(path),
            "retrieved_utc": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
            "content_type": None, "reused_existing": True,
        })
        return
    host = urlparse(url).hostname or ""
    if host == "distrettoalpiorientali.it" and not params:
        subprocess.run(["curl.exe", "-L", "--fail", "--silent", "--show-error",
                        "--max-time", str(timeout), "-o", str(path), url], check=True)
        final_url, content_type = url, None
    else:
        r = S.get(url, params=params, timeout=timeout, stream=True)
        r.raise_for_status()
        with path.open("wb") as f:
            for block in r.iter_content(1024 * 1024):
                if block:
                    f.write(block)
        final_url, content_type = r.url, r.headers.get("content-type")
    MANIFEST.append({
        "path": str(path.relative_to(ROOT)),
        "url": final_url,
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "content_type": content_type,
    })

SIGMA_WFS = "https://sigma.distrettoalpiorientali.it/sigma/geo/sigma/wfs"
FVG_WFS = "https://serviziogc.regione.fvg.it/geoserver/wfs"
bbox_filter = "BBOX(the_geom,12.20,45.50,14.00,46.75,'EPSG:4326')"

# PGRA: capabilities, schema, hits and materialized FVG-envelope geometry.
download(SIGMA_WFS, PGRA / "sigma_wfs_capabilities_20260920.xml",
         {"service":"WFS","version":"2.0.0","request":"GetCapabilities"})
for layer, stem in [
    ("sigma:Pericolo_direttiva_alluvioni", "pgra_pericolosita"),
    ("sigma:Rischio", "pgra_rischio"),
]:
    download(SIGMA_WFS, PGRA / f"{stem}_schema_20260920.xsd",
             {"service":"WFS","version":"2.0.0","request":"DescribeFeatureType","typeNames":layer})
    download(SIGMA_WFS, PGRA / f"{stem}_hits_20260920.xml",
             {"service":"WFS","version":"2.0.0","request":"GetFeature","typeNames":layer,
              "resultType":"hits","CQL_FILTER":bbox_filter})
    download(SIGMA_WFS, PGRA / f"{stem}_fvg_envelope_20260920.zip",
             {"service":"WFS","version":"2.0.0","request":"GetFeature","typeNames":layer,
              "outputFormat":"shape-zip","CQL_FILTER":bbox_filter}, timeout=600)

# Official pages/documents for current legal/cartographic lineage.
pgra_lineage_pages = {
    "pgra_update_20260122_sigma.html": "https://sigma.distrettoalpiorientali.it/portal/index.php/2026/01/22/pgra_aggiornamento/",
    "pgra_observations_20260302.html": "https://distrettoalpiorientali.it/news-eventi/aggiornamento-pgra-trasmissione-delle-osservazioni/",
    "pgra_2027_2033_participation.html": "https://distrettoalpiorientali.it/piano-gestione-rischio-alluvioni/pgra-2027-2033/partecipazione-pubblica-alluvioni/",
}
for name, url in pgra_lineage_pages.items():
    download(url, PGRA / name, timeout=120)

official_pages = {
    "pai_main.html": "https://distrettoalpiorientali.it/piano-assetto-idrogeologico/",
    "pai4.html": "https://distrettoalpiorientali.it/pai-4-bacini/",
    "pai_isonzo_maps.html": "https://distrettoalpiorientali.it/piano-assetto-idrogeologico/bacino-del-fiume-isonzo-uom-itn004/tavole-di-pericolosita-e-rischio-geologico/",
    "pai_tagliamento_maps.html": "https://distrettoalpiorientali.it/piano-assetto-idrogeologico/bacino-del-fiume-tagliamento-uom-itn009/tavole-di-pericolosita-e-rischio-geologico/",
    "pai_piave_maps.html": "https://distrettoalpiorientali.it/piano-assetto-idrogeologico/bacino-del-fiume-piave-uom-itn007/tavole-di-pericolosita-e-rischio-geologico/",
    "pai_livenza_maps.html": "https://distrettoalpiorientali.it/piano-assetto-idrogeologico/bacino-del-fiume-livenza-uom-itn006/tavole-di-pericolosita-e-rischio-geologico/",
    "pai_fella_maps.html": "https://distrettoalpiorientali.it/piano-assetto-idrogeologico/sottobacino-del-fiume-fella/tavole-di-pericolosita-e-rischio-geologico/",
    "pai_fvg_itr061_maps.html": "https://distrettoalpiorientali.it/piano-assetto-idrogeologico/bacino-dei-fiumi-della-regione-del-friuli-venezia-giulia-uom-itr061/tavole-di-pericolosita-e-rischio-geologico/",
    "fvg_pai.html": "https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/geologia/FOGLIA25/",
    "fvg_pai_faq.html": "https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/geologia/FOGLIA25/faq/",
    "fvg_frane.html": "https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/geologia/FOGLIA20/",
}
map_link_rows = []
for name, url in official_pages.items():
    target = PAI / name
    download(url, target, timeout=120)
    if "_maps" in name:
        text = target.read_text(encoding="utf-8", errors="ignore")
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', text, flags=re.I)
        pdfs = sorted({urljoin(url, h) for h in hrefs if ".pdf" in h.lower()})
        for h in pdfs:
            map_link_rows.append([name, h])

with (PAI / "pai_official_map_links_v01.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["index_page", "pdf_url"])
    w.writerows(map_link_rows)

# Core official disciplines. These documents remain subject to subsequent art. 6 updates.
discipline = {
    "PAI4_NORME_ATTUAZIONE.pdf": "https://distrettoalpiorientali.it/wp-content/uploads/2023/02/norme_Attuazione_PAI_4bacini.pdf",
    "PAI_FELLA_NORME_ATTUAZIONE.pdf": "https://distrettoalpiorientali.it/wp-content/uploads/2023/02/PAI_Fella_Norme_attuazione.pdf",
    "PAI_LIVENZA_PRIMA_VARIANTE_RELAZIONE_NORME.pdf": "https://distrettoalpiorientali.it/wp-content/uploads/2023/02/Relazione_PAIL_Ivariante_2015_a.pdf",
    "PAIR_FVG_RELAZIONE_NORME.pdf": "https://distrettoalpiorientali.it/wp-content/uploads/2023/02/PAIR_Allegato_01_relazione_FVG.pdf",
}
for name, url in discipline.items():
    download(url, DISC / name, timeout=240)
# Regional landslide support: metadata/capabilities and current public WFS snapshots.
download(FVG_WFS, SUPPORT / "fvg_wfs_capabilities_20260920.xml",
         {"service":"WFS","version":"2.0.0","request":"GetCapabilities"})
support_layers = [
    ("UTIL_TER:VW_DATA_FRANE_PERICOLOSITA", "vw_data_frane_pericolosita"),
    ("UTIL_TER:VW_DATA_FRANE_PERIMETRO", "vw_data_frane_perimetro"),
    ("IRDAT:VW_FR_IFFI", "vw_fr_iffi"),
    ("IRDAT:CATFRANE_PERICOLOSITA", "catfrane_pericolosita"),
    ("IRDAT:CATFRANE_PERIMFRANE", "catfrane_perimfrane"),
]
for layer, stem in support_layers:
    download(FVG_WFS, SUPPORT / f"{stem}_schema_20260920.xsd",
             {"service":"WFS","version":"2.0.0","request":"DescribeFeatureType","typeNames":layer})
    download(FVG_WFS, SUPPORT / f"{stem}_hits_20260920.xml",
             {"service":"WFS","version":"2.0.0","request":"GetFeature","typeNames":layer,"resultType":"hits"})
    if stem in {"vw_data_frane_pericolosita", "vw_data_frane_perimetro", "vw_fr_iffi"}:
        download(FVG_WFS, SUPPORT / f"{stem}_20260920.zip",
                 {"service":"WFS","version":"2.0.0","request":"GetFeature","typeNames":layer,
                  "outputFormat":"shape-zip"}, timeout=600)

# QA: counts from hits, ZIP integrity, explicit PGRA binding search.
def number_matched(path: Path):
    s = path.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r'numberMatched=["\']([^"\']+)', s)
    return int(m.group(1)) if m and m.group(1).isdigit() else (m.group(1) if m else None)
counts = {}
for path in list(PGRA.glob("*_hits_20260920.xml")) + list(SUPPORT.glob("*_hits_20260920.xml")):
    counts[path.name] = number_matched(path)
QA["checks"]["feature_counts"] = counts

zip_checks = {}
for path in list(PGRA.glob("*.zip")) + list(SUPPORT.glob("*.zip")):
    ok = zipfile.is_zipfile(path)
    bad = None
    if ok:
        with zipfile.ZipFile(path) as z:
            bad = z.testzip()
    zip_checks[path.name] = {"is_zip": ok, "testzip_bad_member": bad}
QA["checks"]["zip_integrity"] = zip_checks

cap = (PGRA / "sigma_wfs_capabilities_20260920.xml").read_text(encoding="utf-8", errors="ignore")
schemas = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in PGRA.glob("*_schema_20260920.xsd"))
needles = ["PGRA2027", "Delibera 12", "18.12.2025", "18/12/2025", "2027-33"]
QA["checks"]["pgra_strong_binding_strings"] = {n: (n.lower() in (cap+"\n"+schemas).lower()) for n in needles}
QA["checks"]["pgra_strong_binding_found"] = any(QA["checks"]["pgra_strong_binding_strings"].values())
QA["checks"]["pai_map_link_count"] = len(map_link_rows)
QA["notes"].append("PAI official vector files are not exposed as a public download in the FVG FAQ; the FAQ directs users to request them from the District.")
QA["notes"].append("Regional landslide WFS snapshots are support datasets and are not promoted here as complete/equivalent PAI current geometry.")
# Add derived files to manifest after their creation.
for path in [PAI / "pai_official_map_links_v01.csv"]:
    MANIFEST.append({
        "path": str(path.relative_to(ROOT)), "url": None,
        "bytes": path.stat().st_size, "sha256": sha256(path),
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "content_type": "text/csv; charset=utf-8",
    })

qa_path = ROOT / "qa_validation_v01.json"
qa_path.write_text(json.dumps(QA, ensure_ascii=False, indent=2), encoding="utf-8")
MANIFEST.append({
    "path": str(qa_path.relative_to(ROOT)), "url": None,
    "bytes": qa_path.stat().st_size, "sha256": sha256(qa_path),
    "retrieved_utc": datetime.now(timezone.utc).isoformat(),
    "content_type": "application/json",
})

manifest_path = ROOT / "source_manifest_v01.json"
manifest_path.write_text(json.dumps({
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Chat 3.11 PGRA + PAI current baseline",
    "files": MANIFEST,
}, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(QA, ensure_ascii=False, indent=2))
print("MANIFEST", manifest_path, sha256(manifest_path))
