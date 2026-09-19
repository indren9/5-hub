#!/usr/bin/env python3
"""Chat 3.8: acquisizione/validazione urbanistica corrente FVG.

Pipeline prudente current-first:
- parte dalla coverage Chat 3.2 (215 Comuni);
- cerca record PRGC ufficiali nel Catalogo IRDAT;
- legge metadati di variante, atti, CRS e distribuzione vettoriale;
- opzionalmente materializza i vettori originali con SHA-256 e QA ZIP;
- usa il campione comunale Chat 3.2 solo come evidenza indipendente già verificata;
- NON costruisce candidati, NON decide categorie ammissibili, NON usa CER 2018 come corrente.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://irdat.regione.fvg.it/consultatore-dati-ambientali-territoriali"
SEARCH_URL = BASE + "/search"
UA = "5-HUB-FVG-chat-3.8-current-urban-planning/1.0"


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def fetch(url: str, data: bytes | None = None, timeout: int = 45):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=timeout)


def fetch_bytes(url: str, data: bytes | None = None, timeout: int = 45):
    with fetch(url, data=data, timeout=timeout) as r:
        return r.read(), dict(r.headers), r.geturl()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def clean(fragment: str) -> str:
    fragment = re.sub(r"<br\s*/?>", " ", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(fragment)).strip()


def field(page: str, label: str) -> str:
    pat = rf"<strong>\s*{re.escape(label)}\s*</strong>\s*<span[^>]*>(.*?)</span>"
    m = re.search(pat, page, flags=re.I | re.S)
    return clean(m.group(1)) if m else ""


def page_title(page: str) -> str:
    m = re.search(r"<h3>\s*(PRGC.*?)</h3>", page, flags=re.I | re.S)
    return clean(m.group(1)) if m else ""


def abstract(page: str) -> str:
    return field(page, "Abstract:")


def first_variant(text: str) -> str:
    m = re.search(r"\b(?:variante|variant)\s*(?:n\.?\s*)?(\d+[A-Za-z]?)", text or "", flags=re.I)
    return m.group(1) if m else ""


def bur_ref(text: str) -> str:
    m = re.search(
        r"\bBUR\b.{0,35}?(?:n\.?\s*)?(\d+).{0,35}?(\d{1,2}[-/.]\d{1,2}[-/.]\d{4})",
        text or "", flags=re.I,
    )
    return f"BUR n. {m.group(1)} del {m.group(2)}" if m else ""


def ir_search(name: str) -> tuple[list[str], bytes]:
    body = urllib.parse.urlencode({
        "network": "", "lang": "ita",
        "searchInDatasets": "true", "_searchInDatasets": "on",
        "searchInServices": "true", "_searchInServices": "on",
        "textToSearch": f"PRGC {name}", "avviaRicerca": "",
    }).encode()
    raw, _, _ = fetch_bytes(SEARCH_URL, body, timeout=60)
    text = raw.decode("utf-8", "ignore")
    ids = sorted(set(re.findall(r"/detail/irdat/dataset/(\d+)", text)))
    return ids, raw


def ir_detail(dataset_id: str) -> tuple[dict, bytes]:
    url = f"{BASE}/detail/irdat/dataset/{dataset_id}"
    raw, _, final_url = fetch_bytes(url, timeout=60)
    text = raw.decode("utf-8", "ignore")
    dl = re.search(r'href="([^"]+/download/\d+\?[^"]+)"', text, flags=re.I)
    download_url = urllib.parse.urljoin(BASE + "/", html.unescape(dl.group(1))) if dl else ""
    item = {
        "dataset_id": dataset_id,
        "detail_url": final_url,
        "title": page_title(text),
        "abstract": abstract(text),
        "edition": field(text, "Edition:"),
        "edition_date": field(text, "Edition date:"),
        "metadata_date": field(text, "Metadata date:"),
        "publication_date": field(text, "Pubblication:") or field(text, "Publication:"),
        "crs": field(text, "Original reference system:"),
        "spatial_type": field(text, "Tipology:"),
        "distribution_format": field(text, "Distribution format:"),
        "additional_info": field(text, "Additional info:"),
        "download_url": download_url,
    }
    return item, raw


def select_exact(name: str, ids: list[str], delay: float) -> tuple[dict | None, dict[str, bytes]]:
    raws: dict[str, bytes] = {}
    target = norm("PRGC " + name)
    for did in ids:
        try:
            item, raw = ir_detail(did)
            raws[did] = raw
            if norm(item["title"]) == target:
                return item, raws
        except Exception:
            continue
        finally:
            if delay:
                time.sleep(delay)
    return None, raws


def save_bytes(path: Path, data: bytes, source_url: str, manifest: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    manifest.append({
        "path": str(path),
        "source_url": source_url,
        "accessed_at_utc": now_utc(),
        "bytes": len(data),
        "sha256": sha256_bytes(data),
    })


def download_vector(item: dict, folder: Path, manifest: list[dict]) -> dict:
    out = {"download_status": "NOT_ATTEMPTED", "artifact_path": "", "bytes": "", "sha256": "",
           "archive_integrity": "", "shp_present": "", "prj_present": "", "prj_excerpt": ""}
    if not item.get("download_url"):
        out["download_status"] = "NO_DOWNLOAD_LINK"
        return out
    try:
        data, headers, final_url = fetch_bytes(item["download_url"], timeout=120)
        cd = headers.get("Content-Disposition", "")
        m = re.search(r'filename="?([^";]+)', cd, flags=re.I)
        name = m.group(1) if m else f"prgc_irdat_{item['dataset_id']}.zip"
        if data[:2] == b"PK" and not name.lower().endswith(".zip"):
            name += ".zip"
        path = folder / name
        save_bytes(path, data, final_url, manifest)
        out.update({
            "download_status": "DOWNLOADED",
            "artifact_path": str(path),
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        })
        if data[:2] == b"PK":
            try:
                with zipfile.ZipFile(path) as z:
                    bad = z.testzip()
                    names = z.namelist()
                    shp = [n for n in names if n.lower().endswith(".shp")]
                    prj = [n for n in names if n.lower().endswith(".prj")]
                    out["archive_integrity"] = "PASS" if bad is None else f"FAIL:{bad}"
                    out["shp_present"] = bool(shp)
                    out["prj_present"] = bool(prj)
                    if prj:
                        out["prj_excerpt"] = z.read(prj[0]).decode("utf-8", "ignore")[:500]
            except Exception as e:
                out["archive_integrity"] = f"FAIL:{type(e).__name__}"
        return out
    except Exception as e:
        out["download_status"] = f"ERROR:{type(e).__name__}"
        return out


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    cols = list(rows[0].keys())
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def classify(base: dict, item: dict | None, sample: dict | None, vqa: dict) -> tuple[str, str, str]:
    if item:
        iv = first_variant(item.get("edition") or item.get("abstract", ""))
        sv = first_variant((sample or {}).get("current_evidence", ""))
        sample_ok = bool(sample and sample.get("source_url") and
                         sample.get("current_status", "").upper() not in {"", "TO_VERIFY_MUNICIPAL_CURRENTNESS"})
        if sample_ok and iv and sv and iv == sv and vqa.get("download_status") == "DOWNLOADED":
            return "CURRENT_VECTOR_VERIFIED", "VERIFIED_TO_CURRENT_VARIANT", ""
        return (
            "CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE",
            "VECTOR_AVAILABLE_CURRENTNESS_NOT_VERIFIED" if item.get("download_url") else "NO_VECTOR_LINK_IN_IRDAT",
            "Verificare che non esistano varianti efficaci successive al record IRDAT."
        )
    if sample and sample.get("source_url"):
        return (
            "CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE",
            "NO_IRDAT_EXACT_VECTOR_MATCH",
            "Fonte comunale corrente già nota; geometria corrente/allineamento da completare."
        )
    return (
        "TO_VERIFY",
        "NO_IRDAT_EXACT_VECTOR_MATCH",
        "Ricerca corrente comunale/BUR necessaria; Eagle/CER non promossi a prova di vigenza."
    )


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--baseline-coverage", type=Path, required=True)
    p.add_argument("--sample-evidence", type=Path, required=True)
    p.add_argument("--output-csv", type=Path, required=True)
    p.add_argument("--output-json", type=Path, required=True)
    p.add_argument("--heavy-dir", type=Path, required=True)
    p.add_argument("--download-vectors", action="store_true")
    p.add_argument("--delay", type=float, default=0.05)
    args = p.parse_args()

    base_rows = read_csv(args.baseline_coverage)
    if len(base_rows) != 215:
        raise RuntimeError(f"Coverage baseline attesa 215 righe, trovate {len(base_rows)}")
    sample_rows = read_csv(args.sample_evidence)
    samples = {r["istat_code"]: r for r in sample_rows}
    args.heavy_dir.mkdir(parents=True, exist_ok=True)

    manifest: list[dict] = []
    output: list[dict] = []
    evidence: dict = {
        "generated_at_utc": now_utc(),
        "method": "DEC-0032 current-first/hybrid; IRDAT official discovery + independent municipal sample cross-check",
        "rules": [
            "IRDAT/Eagle vector access does not by itself prove currentness.",
            "CER 2018 is historical/support only.",
            "No candidate generation, admissibility category selection, dissolving or minimum-area filtering.",
        ],
        "municipalities": {},
    }

    for i, base in enumerate(base_rows, start=1):
        code = base["istat_code"]
        name = base["comune"]
        sample = samples.get(code)
        ids: list[str] = []
        search_raw = b""
        search_error = ""
        item = None
        detail_raws: dict[str, bytes] = {}
        try:
            ids, search_raw = ir_search(name)
            item, detail_raws = select_exact(name, ids, args.delay)
        except Exception as e:
            search_error = f"{type(e).__name__}: {e}"

        cdir = args.heavy_dir / "municipalities" / f"{code}_{re.sub(r'[^A-Za-z0-9]+','_',norm(name))}"
        if search_raw:
            save_bytes(cdir / "irdat_search.html", search_raw, SEARCH_URL, manifest)
        if item and item["dataset_id"] in detail_raws:
            save_bytes(cdir / f"irdat_detail_{item['dataset_id']}.html",
                       detail_raws[item["dataset_id"]], item["detail_url"], manifest)

        vqa = {"download_status": "NOT_REQUESTED", "artifact_path": "", "bytes": "", "sha256": "",
               "archive_integrity": "", "shp_present": "", "prj_present": "", "prj_excerpt": ""}
        if item and args.download_vectors:
            vqa = download_vector(item, cdir, manifest)

        status, align, gap = classify(base, item, sample, vqa)
        abs_text = item.get("abstract", "") if item else ""
        variant = item.get("edition", "") if item else ""
        row = {
            "istat_code": code,
            "comune": name,
            "provincia": base.get("sigla_provincia", ""),
            "current_plan": item.get("title", "") if item else "",
            "current_variant": variant,
            "procedural_status": "APPROVED_PUBLISHED" if re.search(r"approv|approved|pubblic", abs_text, re.I) else "",
            "act_and_date": item.get("edition_date", "") if item else "",
            "bur_publication": bur_ref(abs_text),
            "institutional_source_url": (sample or {}).get("source_url", "") or (item.get("detail_url", "") if item else ""),
            "access_date": datetime.now().date().isoformat(),
            "irdat_dataset_id": item.get("dataset_id", "") if item else "",
            "irdat_detail_url": item.get("detail_url", "") if item else "",
            "irdat_metadata_date": item.get("metadata_date", "") if item else "",
            "irdat_publication_date": item.get("publication_date", "") if item else "",
            "geometry_source": "IRDAT/Comune" if item and item.get("download_url") else "",
            "geometry_format": item.get("distribution_format", "") if item else "",
            "geometry_crs": item.get("crs", "") if item else "",
            "geometry_layer_service_id": item.get("dataset_id", "") if item else "",
            "geometry_alignment_status": align,
            "currentness_status": status,
            "evidence_used": (sample or {}).get("current_evidence", "") or abs_text,
            "independent_current_source": (sample or {}).get("source_url", ""),
            "irdat_search_ids": "|".join(ids),
            "eagle_access_status_baseline": base.get("access_status", ""),
            "cer_2018_reference": f"D:{base.get('cer_D_latest_data_val','')} H:{base.get('cer_H_latest_data_val','')}".strip(),
            "vector_download_status": vqa.get("download_status", ""),
            "vector_artifact_path": vqa.get("artifact_path", ""),
            "vector_bytes": vqa.get("bytes", ""),
            "vector_sha256": vqa.get("sha256", ""),
            "vector_archive_integrity": vqa.get("archive_integrity", ""),
            "vector_shp_present": vqa.get("shp_present", ""),
            "vector_prj_present": vqa.get("prj_present", ""),
            "notes_gap": gap or (sample or {}).get("notes", ""),
            "search_error": search_error,
        }
        output.append(row)
        evidence["municipalities"][code] = {
            "comune": name, "search_ids": ids, "selected": item,
            "sample": sample, "vector_qa": vqa,
            "status": status, "alignment": align, "gap": gap, "search_error": search_error,
        }
        if i % 20 == 0 or i == 215:
            print(f"Processed {i}/215", flush=True)

    write_csv(args.output_csv, output)
    counts: dict[str, int] = {}
    for r in output:
        counts[r["currentness_status"]] = counts.get(r["currentness_status"], 0) + 1
    evidence["summary"] = {
        "municipalities": len(output),
        "status_counts": counts,
        "irdat_exact_records": sum(bool(r["irdat_dataset_id"]) for r in output),
        "vectors_downloaded": sum(r["vector_download_status"] == "DOWNLOADED" for r in output),
        "vector_integrity_pass": sum(r["vector_archive_integrity"] == "PASS" for r in output),
        "search_errors": sum(bool(r["search_error"]) for r in output),
    }
    args.output_json.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
    manifest_path = args.heavy_dir / "source_manifest_v01.json"
    manifest_path.write_text(json.dumps({
        "generated_at_utc": now_utc(),
        "producer": Path(__file__).name,
        "artifacts": manifest,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(evidence["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
