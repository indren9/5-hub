#!/usr/bin/env python3
"""Chat 3.8 runner: IRDAT catalogue census + metadata validation, no candidates."""
from __future__ import annotations

import argparse
import html
import http.cookiejar
import json
import re
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import acquire_validate_current_urban_planning_chat3_8_v01 as core

RESULT_RE = re.compile(
    r'<span>([^<]+?)\s*-\s*DATASET</span>.*?'
    r'<strong>Admin structure:</strong>\s*<span>(.*?)</span>.*?'
    r'<strong>Abstract:</strong>\s*<span>(.*?)</span>.*?'
    r'href="/consultatore-dati-ambientali-territoriali/detail/irdat/dataset/(\d+)"',
    re.I | re.S,
)


def all_variants(text: str) -> set[str]:
    return set(re.findall(r"\b(?:variant[ei]?)\s*(?:n\.?\s*)?(\d+[A-Za-z]?)", text or "", re.I))


def catalogue_census(heavy_dir: Path) -> tuple[dict[str, dict], list[dict]]:
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    opener.addheaders = [("User-Agent", core.UA)]
    body = urllib.parse.urlencode({
        "network": "", "lang": "ita",
        "searchInDatasets": "true", "_searchInDatasets": "on",
        "searchInServices": "false", "_searchInServices": "on",
        "textToSearch": "PRGC", "avviaRicerca": "",
    }).encode()
    first = opener.open(core.SEARCH_URL, data=body, timeout=60).read()
    pages = [first]
    texts = [first.decode("utf-8", "ignore")]
    for _ in range(1, 30):
        if "otherResults_" not in texts[-1]:
            break
        raw = opener.open(core.BASE + "/result-list/md/next-block", timeout=60).read()
        pages.append(raw)
        texts.append(raw.decode("utf-8", "ignore"))
        if "otherResults_" not in texts[-1]:
            break

    manifest: list[dict] = []
    cat_dir = heavy_dir / "irdat_catalog"
    for i, raw in enumerate(pages):
        core.save_bytes(
            cat_dir / f"prgc_search_block_{i:02d}.html",
            raw,
            core.SEARCH_URL if i == 0 else core.BASE + "/result-list/md/next-block",
            manifest,
        )

    out: dict[str, dict] = {}
    for text in texts:
        for title, admin, abstract, did in RESULT_RE.findall(text):
            title = core.clean(title)
            if not title.upper().startswith("PRGC "):
                continue
            out[core.norm(title)] = {
                "dataset_id": did,
                "title": title,
                "admin_structure": core.clean(admin),
                "abstract": core.clean(abstract),
                "detail_url": f"{core.BASE}/detail/irdat/dataset/{did}",
            }
    return out, manifest


def sample_confirms(item: dict, sample: dict | None) -> bool:
    if not item or not sample:
        return False
    status = sample.get("current_status", "").upper()
    if "VARIANT_TO_VERIFY" in status or not sample.get("source_url"):
        return False
    iv = all_variants(item.get("edition") or item.get("abstract", ""))
    evidence = sample.get("current_evidence", "")
    sv = all_variants(evidence)
    explicit_number_match = any(re.search(rf"(?<!\\d){re.escape(v)}(?!\\d)", evidence) for v in iv)
    return bool(iv and (iv.intersection(sv) or explicit_number_match))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--baseline-coverage", type=Path, required=True)
    p.add_argument("--sample-evidence", type=Path, required=True)
    p.add_argument("--output-csv", type=Path, required=True)
    p.add_argument("--output-json", type=Path, required=True)
    p.add_argument("--heavy-dir", type=Path, required=True)
    p.add_argument("--workers", type=int, default=8)
    args = p.parse_args()

    base_rows = core.read_csv(args.baseline_coverage)
    if len(base_rows) != 215:
        raise RuntimeError(f"Attesi 215 Comuni, trovati {len(base_rows)}")
    samples = {r["istat_code"]: r for r in core.read_csv(args.sample_evidence)}
    args.heavy_dir.mkdir(parents=True, exist_ok=True)

    catalogue, manifest = catalogue_census(args.heavy_dir)
    print(f"IRDAT exact PRGC catalogue records: {len(catalogue)}", flush=True)
    aliases = {
        "030120": core.norm("PRGC Terzo di Aquileia"),
        "032004": core.norm("PRGC San Dorligo della Valle - Dolina"),
    }

    wanted: dict[str, str] = {}
    for base in base_rows:
        key = aliases.get(base["istat_code"], core.norm("PRGC " + base["comune"]))
        if key in catalogue and base["istat_code"] in samples:
            wanted[catalogue[key]["dataset_id"]] = base["istat_code"]

    details: dict[str, dict] = {}
    detail_raws: dict[str, bytes] = {}
    detail_errors: dict[str, str] = {}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(core.ir_detail, did): did for did in wanted}
        done = 0
        for fut in as_completed(futs):
            did = futs[fut]
            try:
                item, raw = fut.result()
                details[did], detail_raws[did] = item, raw
            except Exception as e:
                detail_errors[did] = f"{type(e).__name__}: {e}"
            done += 1
            if done % 25 == 0 or done == len(futs):
                print(f"IRDAT details {done}/{len(futs)}", flush=True)

    rows, evidence = [], {}
    for base in base_rows:
        code, name = base["istat_code"], base["comune"]
        sample = samples.get(code)
        key = aliases.get(code, core.norm("PRGC " + name))
        cat = catalogue.get(key)
        item = details.get(cat["dataset_id"]) if cat else None
        if cat and not item:
            item = dict(cat)
            item.update({
                "edition": "", "edition_date": "", "metadata_date": "", "publication_date": "",
                "crs": "", "spatial_type": "", "distribution_format": "", "additional_info": "",
                "download_url": "",
            })

        cdir = args.heavy_dir / "municipalities" / f"{code}_{core.norm(name)}"
        if item and item.get("dataset_id") in detail_raws:
            core.save_bytes(
                cdir / f"irdat_detail_{item['dataset_id']}.html",
                detail_raws[item["dataset_id"]],
                item["detail_url"],
                manifest,
            )

        confirmed = sample_confirms(item, sample)
        vqa = {
            "download_status": "NOT_ACQUIRED_CURRENTNESS_UNVERIFIED",
            "artifact_path": "", "bytes": "", "sha256": "", "archive_integrity": "",
            "shp_present": "", "prj_present": "", "prj_excerpt": "",
        }
        if confirmed and item and item.get("download_url"):
            vqa = core.download_vector(item, cdir, manifest)

        if confirmed and vqa.get("download_status") == "DOWNLOADED":
            status = "CURRENT_VECTOR_VERIFIED"
            align = "VERIFIED_TO_CURRENT_VARIANT"
            gap = ""
        elif item:
            status = "CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE"
            align = "VECTOR_AVAILABLE_CURRENTNESS_NOT_VERIFIED" if item.get("download_url") else "IRDAT_RECORD_DETAIL_INCOMPLETE"
            gap = "Verificare assenza di varianti efficaci successive e allineamento puntuale del vettore."
        elif sample and sample.get("source_url"):
            status = "CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE"
            align = "NO_IRDAT_EXACT_VECTOR_MATCH"
            gap = "Fonte comunale corrente nota; variante/geometria corrente da completare."
        else:
            status = "TO_VERIFY"
            align = "NO_IRDAT_EXACT_VECTOR_MATCH"
            gap = "Ricerca su fonte comunale/BUR necessaria; Eagle/CER non costituiscono prova di vigenza."

        abstract = (item or {}).get("abstract", "") or (cat or {}).get("abstract", "")
        row = {
            "istat_code": code,
            "comune": name,
            "provincia": base.get("sigla_provincia", ""),
            "current_plan": (item or {}).get("title", "") or (cat or {}).get("title", ""),
            "current_variant": (item or {}).get("edition", "") or ("Variant " + next(iter(all_variants(abstract)), "") if all_variants(abstract) else ""),
            "procedural_status": "APPROVED_PUBLISHED" if re.search(r"approv|approved|pubblic", abstract, re.I) else "",
            "act_and_date": (item or {}).get("edition_date", ""),
            "bur_publication": core.bur_ref(abstract),
            "institutional_source_url": (sample or {}).get("source_url", "") or (item or {}).get("detail_url", "") or (cat or {}).get("detail_url", ""),
            "access_date": datetime.now().date().isoformat(),
            "irdat_dataset_id": (item or {}).get("dataset_id", "") or (cat or {}).get("dataset_id", ""),
            "irdat_detail_url": (item or {}).get("detail_url", "") or (cat or {}).get("detail_url", ""),
            "irdat_admin_structure": (cat or {}).get("admin_structure", ""),
            "irdat_metadata_date": (item or {}).get("metadata_date", ""),
            "irdat_publication_date": (item or {}).get("publication_date", ""),
            "geometry_source": "IRDAT/Comune" if item else "",
            "geometry_format": (item or {}).get("distribution_format", ""),
            "geometry_crs": (item or {}).get("crs", ""),
            "geometry_layer_service_id": (item or {}).get("dataset_id", ""),
            "geometry_alignment_status": align,
            "currentness_status": status,
            "evidence_used": (sample or {}).get("current_evidence", "") or abstract,
            "independent_current_source": (sample or {}).get("source_url", ""),
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
            "detail_error": detail_errors.get((cat or {}).get("dataset_id", ""), ""),
        }
        rows.append(row)
        evidence[code] = {
            "comune": name, "catalogue": cat, "detail": item, "sample": sample,
            "sample_confirms_variant": confirmed, "vector_qa": vqa,
            "status": status, "alignment": align, "gap": gap,
        }

    core.write_csv(args.output_csv, rows)
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["currentness_status"]] = counts.get(r["currentness_status"], 0) + 1
    summary = {
        "municipalities": len(rows),
        "irdat_exact_records": sum(bool(r["irdat_dataset_id"]) for r in rows),
        "irdat_detail_success": len(details),
        "irdat_detail_errors": len(detail_errors),
        "status_counts": counts,
        "current_vectors_acquired": sum(r["vector_download_status"] == "DOWNLOADED" for r in rows),
        "vector_integrity_pass": sum(r["vector_archive_integrity"] == "PASS" for r in rows),
    }
    args.output_json.write_text(json.dumps({
        "generated_at_utc": core.now_utc(),
        "method": "DEC-0032 current-first/hybrid; IRDAT catalogue census + municipal sample cross-check",
        "rules": [
            "Exact IRDAT PRGC record is official source discovery, not automatic proof of 2026 currentness.",
            "Only independently matched current variants may be promoted to CURRENT_VECTOR_VERIFIED.",
            "CER 2018 remains historical/support only.",
            "No candidate generation or admissibility decisions.",
        ],
        "summary": summary,
        "municipalities": evidence,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.heavy_dir / "source_manifest_v01.json").write_text(json.dumps({
        "generated_at_utc": core.now_utc(),
        "producer": Path(__file__).name,
        "artifacts": manifest,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
