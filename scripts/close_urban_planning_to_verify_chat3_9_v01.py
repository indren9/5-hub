from __future__ import annotations
import csv, hashlib, json, mimetypes, os
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(r"C:\dev\5-hub")
DOCS = ROOT / "docs"
BASELINE = DOCS / "FASE_3_CURRENT_URBAN_PLANNING_TO_VERIFY_BASELINE_v01.csv"
COVERAGE_V01 = DOCS / "FASE_3_CURRENT_URBAN_PLANNING_COVERAGE_v01.csv"
EVIDENCE_SEED = ROOT / "scripts" / "chat3_9_source_evidence_v01.jsonl"
RESULTS = DOCS / "FASE_3_URBAN_PLANNING_TO_VERIFY_RESULTS_v01.csv"
COVERAGE_V02 = DOCS / "FASE_3_CURRENT_URBAN_PLANNING_COVERAGE_v02.csv"
EVIDENCE_JSON = DOCS / "FASE_3_URBAN_PLANNING_TO_VERIFY_EVIDENCE_v01.json"
QA_JSON = DOCS / "FASE_3_URBAN_PLANNING_TO_VERIFY_QA_v01.json"
HEAVY = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_9")
SOURCES = HEAVY / "sources"
MANIFEST = HEAVY / "source_manifest_v01.json"
EXPECTED_SHA256 = "EEDFD368D1B1182E73124D6C816383E25EE178E5B81FB0051F2A15EC4FC9D2C6"
ACCESS_DATE = "2026-09-19"

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()

def read_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))
def write_csv(path: Path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

def read_jsonl(path: Path):
    items = []
    with path.open("r", encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            if line.strip():
                obj = json.loads(line)
                obj["_seed_line"] = n
                items.append(obj)
    return items

def fetch_one(item):
    url = item["source_url"]
    suffix = ".pdf" if url.lower().split("?")[0].endswith(".pdf") else ".html"
    target = SOURCES / f'{item["istat_code"]}_{item["comune"].replace(" ", "_").replace("/", "_")}{suffix}'
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 Chat3.9 source preservation"})
    try:
        with urlopen(req, timeout=25) as r:
            data = r.read(30 * 1024 * 1024 + 1)
            if len(data) > 30 * 1024 * 1024:
                raise RuntimeError("SOURCE_OVER_30MB_LIMIT")
            target.write_bytes(data)
            return {"istat_code": item["istat_code"], "url": url, "status": "MATERIALIZED",
                    "path": str(target), "bytes": len(data), "sha256": sha256_file(target),
                    "content_type": r.headers.get("Content-Type", "")}
    except Exception as e:
        return {"istat_code": item["istat_code"], "url": url, "status": "NOT_MATERIALIZED",
                "error": f"{type(e).__name__}: {e}"[:500]}
def main():
    baseline_hash = sha256_file(BASELINE)
    if baseline_hash != EXPECTED_SHA256:
        raise RuntimeError(f"Baseline SHA mismatch: {baseline_hash}")
    scope_rows = read_csv(BASELINE)
    coverage = read_csv(COVERAGE_V01)
    evidence = read_jsonl(EVIDENCE_SEED)
    scope_ids = {r["istat_code"] for r in scope_rows}
    evidence_ids = {e["istat_code"] for e in evidence}
    if len(scope_rows) != 43 or len(scope_ids) != 43:
        raise RuntimeError("Baseline scope is not exactly 43 unique municipalities")
    if len(evidence) != 43 or evidence_ids != scope_ids:
        raise RuntimeError(f"Evidence scope mismatch: evidence={len(evidence)} missing={scope_ids-evidence_ids} extra={evidence_ids-scope_ids}")
    if len(coverage) != 215 or len({r["istat_code"] for r in coverage}) != 215:
        raise RuntimeError("Coverage v01 is not 215 unique municipalities")
    old_by_id = {r["istat_code"]: dict(r) for r in coverage}
    ev_by_id = {e["istat_code"]: e for e in evidence}
    SOURCES.mkdir(parents=True, exist_ok=True)

    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = [ex.submit(fetch_one, e) for e in evidence]
        manifest_items = [f.result() for f in as_completed(futures)]
    manifest_items.sort(key=lambda x: x["istat_code"])
    fetch_by_id = {x["istat_code"]: x for x in manifest_items}
    MANIFEST.write_text(json.dumps({
        "chat": "3.9", "access_date": ACCESS_DATE,
        "baseline_sha256": baseline_hash,
        "items": manifest_items
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    updated = []
    result_rows = []
    for row in coverage:
        code = row["istat_code"]
        if code not in scope_ids:
            updated.append(dict(row))
            continue
        e = ev_by_id[code]
        new = dict(row)
        new["current_plan"] = "PRGC " + e["comune"]
        new["current_variant"] = e.get("observed_variant", "")
        new["procedural_status"] = e.get("procedural_status", "")
        new["act_and_date"] = e.get("act_and_date", "")
        new["bur_publication"] = e.get("bur_publication", "")
        new["institutional_source_url"] = e["source_url"]
        new["access_date"] = ACCESS_DATE
        new["geometry_source"] = e.get("geometry_source", "")
        new["geometry_format"] = e.get("geometry_format", "")
        new["geometry_alignment_status"] = (
            "CURRENT_PLAN_VERIFIED_NO_VECTOR"
            if e["new_status"] == "CURRENT_PLAN_VERIFIED_NO_VECTOR"
            else "LINEAGE_NOT_FULLY_VERIFIED"
        )
        new["currentness_status"] = e["new_status"]
        new["evidence_used"] = e.get("evidence_used", "")
        new["independent_current_source"] = e["source_url"]
        new["vector_download_status"] = (
            "NOT_ACQUIRED_NO_CURRENT_VECTOR_FOUND"
            if e["new_status"] == "CURRENT_PLAN_VERIFIED_NO_VECTOR"
            else "NOT_ACQUIRED_LINEAGE_INCOMPLETE"
        )
        new["notes_gap"] = e.get("notes_gap", "")
        new["supplement_source_url"] = e["source_url"]
        fetch = fetch_by_id[code]
        new["supplement_fetch_status"] = fetch["status"]
        new["supplement_sha256"] = fetch.get("sha256", "")
        updated.append(new)
        result = dict(e)
        result["provincia"] = row["provincia"]
        result["old_status"] = row["currentness_status"]
        result["materialization_status"] = fetch["status"]
        result["materialized_sha256"] = fetch.get("sha256", "")
        result_rows.append(result)

    updated_by_id = {r["istat_code"]: r for r in updated}
    outside_changes = []
    for code, old in old_by_id.items():
        if code not in scope_ids and updated_by_id[code] != old:
            outside_changes.append(code)
    if outside_changes:
        raise RuntimeError("Out-of-scope rows changed: " + ",".join(outside_changes))
    if any(old_by_id[c]["currentness_status"] != "TO_VERIFY" for c in scope_ids):
        raise RuntimeError("Scope baseline includes non-TO_VERIFY rows")
    if any(updated_by_id[c]["currentness_status"] == "TO_VERIFY" for c in scope_ids):
        raise RuntimeError("Residual TO_VERIFY after processing scope")
    if any(not ev_by_id[c].get("source_url") or not ev_by_id[c].get("notes_gap") for c in scope_ids):
        raise RuntimeError("Missing source URL or explicit gap for at least one scope municipality")

    coverage_fields = list(coverage[0].keys())
    write_csv(COVERAGE_V02, updated, coverage_fields)
    result_fields = [
        "istat_code", "comune", "provincia", "old_status", "new_status",
        "observed_variant", "procedural_status", "act_and_date", "bur_publication",
        "source_title", "source_type", "source_url", "evidence_used",
        "geometry_source", "geometry_format", "notes_gap",
        "materialization_status", "materialized_sha256"
    ]
    write_csv(RESULTS, result_rows, result_fields)

    counts_before = Counter(r["currentness_status"] for r in coverage)
    counts_after = Counter(r["currentness_status"] for r in updated)
    materialized = [x for x in manifest_items if x["status"] == "MATERIALIZED"]
    failed_fetch = [x for x in manifest_items if x["status"] != "MATERIALIZED"]
    preservation_errors = []
    for item in materialized:
        path = Path(item["path"])
        if not path.exists() or sha256_file(path) != item["sha256"]:
            preservation_errors.append(item["istat_code"])
    if preservation_errors:
        raise RuntimeError("Preservation hash failures: " + ",".join(preservation_errors))

    evidence_payload = {
        "chat": "3.9",
        "access_date": ACCESS_DATE,
        "method": "DEC-0032 current-first; official municipal/regional evidence; no silent promotion",
        "baseline_path": str(BASELINE),
        "baseline_sha256": baseline_hash,
        "scope_count": len(scope_ids),
        "evidence": [{k: v for k, v in e.items() if k != "_seed_line"} for e in evidence],
        "materialization_manifest_path": str(MANIFEST),
        "materialization_summary": {
            "materialized": len(materialized),
            "not_materialized": len(failed_fetch),
            "preservation_hash_failures": len(preservation_errors)
        }
    }
    EVIDENCE_JSON.write_text(json.dumps(evidence_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    qa = {
        "technical_quality_gate": "PASS",
        "baseline_sha256_expected": EXPECTED_SHA256,
        "baseline_sha256_observed": baseline_hash,
        "scope_rows": len(scope_rows),
        "scope_unique_istat": len(scope_ids),
        "coverage_rows": len(updated),
        "coverage_unique_istat": len({r["istat_code"] for r in updated}),
        "outside_scope_changes": outside_changes,
        "counts_before": dict(counts_before),
        "counts_after": dict(counts_after),
        "residual_to_verify": counts_after.get("TO_VERIFY", 0),
        "materialized_sources": len(materialized),
        "source_fetch_failures": len(failed_fetch),
        "preservation_hash_failures": len(preservation_errors),
        "phase_4_readiness_assessment": "NOT_READY",
        "phase_4_reason": "Residual lineage gaps remain for 207 municipalities and current vector gaps remain; Chat 3.9 cannot open Phase 4."
    }
    QA_JSON.write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(qa, ensure_ascii=False, indent=2))
    print("RESULTS", RESULTS)
    print("COVERAGE_V02", COVERAGE_V02)
    print("EVIDENCE_JSON", EVIDENCE_JSON)
    print("MANIFEST", MANIFEST)

if __name__ == "__main__":
    main()
