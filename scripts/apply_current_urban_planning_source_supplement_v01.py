#!/usr/bin/env python3
"""Apply curated official-source evidence to Chat 3.8 coverage, preserving provenance."""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

import acquire_validate_current_urban_planning_chat3_8_v01 as core


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--coverage", type=Path, required=True)
    p.add_argument("--evidence", type=Path, required=True)
    p.add_argument("--supplement", type=Path, required=True)
    p.add_argument("--heavy-dir", type=Path, required=True)
    args = p.parse_args()

    rows = read_csv(args.coverage)
    by_code = {r["istat_code"]: r for r in rows}
    supp = read_csv(args.supplement)
    evidence = json.loads(args.evidence.read_text(encoding="utf-8"))
    manifest_path = args.heavy_dir / "source_manifest_v01.json"
    manifest_doc = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest = manifest_doc.setdefault("artifacts", [])

    for r in rows:
        r["supplement_source_url"] = ""
        r["supplement_fetch_status"] = ""
        r["supplement_sha256"] = ""

    success = failed = promoted = 0
    for s in supp:
        code = s["istat_code"]
        row = by_code.get(code)
        if row is None:
            raise RuntimeError(f"ISTAT code non presente in coverage: {code}")
        url = s["source_url"]
        folder = args.heavy_dir / "supplement_sources" / f"{code}_{core.norm(s['comune'])}"
        status = ""
        digest = ""
        artifact = ""
        try:
            data, headers, final_url = core.fetch_bytes(url, timeout=60)
            ctype = (headers.get("Content-Type") or "").lower()
            is_pdf = data[:4] == b"%PDF" or "pdf" in ctype or url.lower().endswith(".pdf")
            ext = ".pdf" if is_pdf else ".html"
            out = folder / ("official_source" + ext)
            core.save_bytes(out, data, final_url, manifest)
            digest = core.sha256_bytes(data)
            artifact = str(out)
            if not is_pdf:
                txt = data.decode("utf-8", "ignore")
                if not re.search(r"\bPRGC\b|Piano\s+Regolatore", txt, re.I):
                    status = "HTTP_OK_KEYWORD_NOT_FOUND"
                else:
                    status = "HTTP_OK_KEYWORD_CONFIRMED"
            else:
                status = "HTTP_OK_PDF_CURATED"
            success += 1
        except Exception as e:
            status = f"FETCH_ERROR:{type(e).__name__}"
            failed += 1

        row["supplement_source_url"] = url
        row["supplement_fetch_status"] = status
        row["supplement_sha256"] = digest
        ev = evidence["municipalities"].setdefault(code, {"comune": s["comune"]})
        ev["supplement"] = {
            "source_url": url,
            "evidence_summary": s["evidence_summary"],
            "proposed_status": s["proposed_status"],
            "fetch_status": status,
            "artifact_path": artifact,
            "sha256": digest,
        }

        if status.startswith("HTTP_OK") and row["currentness_status"] == "TO_VERIFY":
            row["currentness_status"] = s["proposed_status"]
            row["institutional_source_url"] = url
            row["evidence_used"] = s["evidence_summary"]
            row["notes_gap"] = (
                "Fonte istituzionale corrente individuata; ricostruire latest effective variant e "
                "geometria/lineage prima di qualunque uso in Fase 4."
                if s["proposed_status"] != "CURRENT_PLAN_VERIFIED_NO_VECTOR"
                else "Piano corrente documentato su fonte comunale; geometria ufficiale vettoriale non acquisita."
            )
            row["geometry_alignment_status"] = (
                "NO_CURRENT_VECTOR_ACQUIRED"
                if s["proposed_status"] == "CURRENT_PLAN_VERIFIED_NO_VECTOR"
                else "CURRENT_SOURCE_FOUND_GEOMETRY_TO_VERIFY"
            )
            promoted += 1

    core.write_csv(args.coverage, rows)
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["currentness_status"]] = counts.get(r["currentness_status"], 0) + 1
    evidence["summary"]["status_counts_after_supplement"] = counts
    evidence["summary"]["supplement_rows"] = len(supp)
    evidence["summary"]["supplement_fetch_success"] = success
    evidence["summary"]["supplement_fetch_failed"] = failed
    evidence["summary"]["supplement_status_promotions"] = promoted
    args.evidence.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")

    manifest_doc["generated_at_utc"] = core.now_utc()
    manifest_doc["supplement_producer"] = Path(__file__).name
    manifest_path.write_text(json.dumps(manifest_doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "supplement_rows": len(supp),
        "fetch_success": success,
        "fetch_failed": failed,
        "promoted_from_TO_VERIFY": promoted,
        "status_counts": counts,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
