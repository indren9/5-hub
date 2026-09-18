#!/usr/bin/env python3
"""Audit riproducibile fonti urbanistiche FVG per Chat 3.2.

Non costruisce candidati e non attribuisce ammissibilità. Verifica:
- elenco Comuni FVG da fonte ISTAT;
- presenza di configurazioni pubbliche EagleFVG PRG (accesso, non vigenza);
- copertura e datazione interna dei layer CER basati su Mosaicatura PRG 2018;
- presenza di layer WFS con naming urbanistico/PRG nel GeoServer regionale.
"""
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ISTAT_URL = "https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv"
WFS_URL = "https://serviziogc.regione.fvg.it/geoserver/wfs"
EAGLE_URL = "https://eaglefvg.regione.fvg.it/eagle/main.aspx?configuration={config}"
UA = "5-HUB-FVG-urban-planning-validation/1.0"
def fetch(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_istat(source: Path | None) -> tuple[list[dict], bytes]:
    data = source.read_bytes() if source else fetch(ISTAT_URL, timeout=60)
    text = data.decode("cp1252")
    reader = csv.DictReader(text.splitlines(), delimiter=";")
    rows = [r for r in reader if r["Codice Regione"] == "06"]
    if len(rows) != 215:
        raise RuntimeError(f"Attesi 215 Comuni FVG, ottenuti {len(rows)}")
    return rows, data


def normalize_words(name: str) -> list[str]:
    value = unicodedata.normalize("NFKD", name)
    value = "".join(c for c in value if not unicodedata.combining(c))
    return re.findall(r"[A-Za-z0-9]+", value)


def eagle_candidates(name: str) -> list[str]:
    bases = [name]
    if " - " in name:
        bases.append(name.split(" - ", 1)[0])
    configs: list[str] = []
    for base in bases:
        words = normalize_words(base)
        title = "".join(w[:1].upper() + w[1:].lower() for w in words)
        original_case = "".join(words)
        lower_articles = "".join(
            (w.lower() if i and w.lower() in {
                "a", "al", "alla", "alle", "da", "dal", "dalla", "delle",
                "del", "della", "dei", "degli", "di", "in", "sul", "sulla"
            } else w[:1].upper() + w[1:].lower())
            for i, w in enumerate(words)
        )
        for suffix in (title, original_case, lower_articles):
            cfg = "Guest_PRG" + suffix
            if cfg not in configs:
                configs.append(cfg)
    return configs


def probe_eagle(name: str, delay: float) -> dict:
    for config in eagle_candidates(name):
        try:
            html = fetch(EAGLE_URL.format(config=urllib.parse.quote(config)), timeout=4).decode(
                "utf-8", "ignore"
            )
            match = re.search(r'<eagle inputParams="([^"]+)"', html)
            if not match:
                continue
            raw = match.group(1)
            payload = json.loads(base64.b64decode(raw + "=" * (-len(raw) % 4)))
            contexts = payload.get("Contexts") or []
            plan_codes = []
            ambiti = []
            for context in contexts:
                if context.get("Label") == "Piani regolatori":
                    plan_codes.extend(context.get("ElencoCodComuni") or [])
                for key, cfg in (context.get("Ds_catalogs") or {}).items():
                    if "prg" in key.lower():
                        ambiti.extend(cfg.get("Ambiti") or [])
            return {
                "eagle_probe_status": "PUBLIC_CONFIG_DETECTED",
                "eagle_config": config,
                "eagle_project": payload.get("Progetto", ""),
                "eagle_plan_codes": "|".join(sorted(set(plan_codes))),
                "eagle_ambiti": "|".join(sorted(set(ambiti))),
            }
        except Exception:
            pass
        finally:
            if delay:
                time.sleep(delay)
    return {
        "eagle_probe_status": "NOT_DETECTED_BY_STANDARD_PROBE",
        "eagle_config": "",
        "eagle_project": "",
        "eagle_plan_codes": "",
        "eagle_ambiti": "",
    }


def get_wfs_features(type_name: str) -> list[dict]:
    query = urllib.parse.urlencode({
        "service": "WFS", "version": "2.0.0", "request": "GetFeature",
        "typeNames": type_name, "outputFormat": "application/json", "count": 10000,
    })
    payload = json.loads(fetch(f"{WFS_URL}?{query}", timeout=90))
    return payload.get("features", [])
def summarize_cer(features: list[dict]) -> dict[str, dict]:
    grouped: dict[str, dict] = defaultdict(lambda: {
        "count": 0, "dates": set(), "variants": set()
    })
    for feature in features:
        p = feature.get("properties") or {}
        code = str(p.get("COD_COM") or "").strip()
        if not code:
            continue
        g = grouped[code]
        g["count"] += 1
        if p.get("DATA_VAL"):
            g["dates"].add(str(p["DATA_VAL"]))
        if p.get("VARIANTE") not in (None, ""):
            g["variants"].add(str(p["VARIANTE"]))
    out = {}
    for code, g in grouped.items():
        dates = sorted(g["dates"])
        out[code] = {
            "count": g["count"],
            "latest_data_val": dates[-1] if dates else "",
            "earliest_data_val": dates[0] if dates else "",
            "variants": "|".join(sorted(g["variants"])),
        }
    return out


def get_wfs_urban_names() -> list[str]:
    query = urllib.parse.urlencode({"service": "WFS", "request": "GetCapabilities"})
    root = ET.fromstring(fetch(f"{WFS_URL}?{query}", timeout=60))
    names = []
    for elem in root.iter():
        if elem.tag.endswith("Name") and elem.text and ":" in elem.text:
            value = elem.text.strip()
            if any(k in value.upper() for k in ("PRG", "URBAN", "ZON", "MOSAIC", "PIAN")):
                names.append(value)
    return sorted(set(names))
def write_csv(path: Path, rows: list[dict], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--istat-csv", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("docs"))
    parser.add_argument("--delay", type=float, default=0.02)
    parser.add_argument("--sample-evidence", type=Path)
    args = parser.parse_args()

    sample_by_code: dict[str, dict] = {}
    if args.sample_evidence:
        with args.sample_evidence.open(encoding="utf-8-sig", newline="") as f:
            sample_by_code = {r["istat_code"]: r for r in csv.DictReader(f)}

    communes, istat_bytes = load_istat(args.istat_csv)
    industrial = summarize_cer(get_wfs_features("CER:ZONE_INDUSTRIALI_ARTIG_D"))
    commercial = summarize_cer(get_wfs_features("CER:ZONE_COMMERCIALI_H"))
    urban_names = get_wfs_urban_names()

    eagle_by_code: dict[str, dict] = {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        future_map = {}
        for r in communes:
            code = r["Codice Comune formato alfanumerico"]
            name = r["Denominazione in italiano"]
            future_map[pool.submit(probe_eagle, name, args.delay)] = code
        for idx, future in enumerate(as_completed(future_map), start=1):
            eagle_by_code[future_map[future]] = future.result()
            if idx % 25 == 0:
                print(f"Probed {idx}/{len(communes)} municipalities", flush=True)

    audit_rows = []
    for r in communes:
        code = r["Codice Comune formato alfanumerico"]
        d = industrial.get(code, {})
        h = commercial.get(code, {})
        eagle = eagle_by_code[code]
        sample = sample_by_code.get(code, {})
        detected = eagle["eagle_probe_status"] == "PUBLIC_CONFIG_DETECTED"
        audit_rows.append({
            "istat_code": code,
            "comune": r["Denominazione in italiano"],
            "sigla_provincia": r["Sigla automobilistica"],
            **eagle,
            "source_candidate": (
                "EagleFVG PRG public configuration" if detected
                else "Official municipal/Regional source to locate"
            ),
            "source_format_access": (
                "Public WebGIS configuration; vector services behind application"
                if detected else "TO_VERIFY"
            ),
            "access_status": (
                "PUBLIC_CONFIG_DETECTED" if detected
                else "STANDARD_CONFIG_NOT_DETECTED_NOT_A_NEGATIVE_PROOF"
            ),
            "cer_D_count": d.get("count", 0),
            "cer_D_latest_data_val": d.get("latest_data_val", ""),
            "cer_D_variants": d.get("variants", ""),
            "cer_H_count": h.get("count", 0),
            "cer_H_latest_data_val": h.get("latest_data_val", ""),
            "cer_H_variants": h.get("variants", ""),
            "current_prgc_date_or_variant": sample.get("current_evidence", ""),
            "current_prgc_source": sample.get("source_url", ""),
            "current_prgc_validation_status": sample.get(
                "current_status", "TO_VERIFY_MUNICIPAL_CURRENTNESS"
            ),
            "sample_comparison_result": sample.get("comparison_result", ""),
            "quality_note": (
                sample.get("notes", "") or
                "Eagle probe proves public configuration only; CER dates/variants are source attributes, "
                "not proof of 2026 currentness."
            ),
        })

    columns = list(audit_rows[0].keys())
    coverage_path = args.output_dir / "FASE_3_URBAN_PLANNING_MUNICIPAL_COVERAGE_v01.csv"
    write_csv(coverage_path, audit_rows, columns)
    metadata = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "purpose": "Chat 3.2 source validation only; no candidate generation or admissibility.",
        "istat": {
            "url": ISTAT_URL,
            "sha256": sha256_bytes(istat_bytes),
            "fvg_municipalities": len(communes),
        },
        "cer": {
            "industrial_features": sum(x.get("count", 0) for x in industrial.values()),
            "commercial_features": sum(x.get("count", 0) for x in commercial.values()),
            "industrial_municipalities": len(industrial),
            "commercial_municipalities": len(commercial),
        },
        "eagle": {
            "public_configs_detected": sum(
                r["eagle_probe_status"] == "PUBLIC_CONFIG_DETECTED" for r in audit_rows
            ),
            "probe_limit": (
                "A missed standard configuration is not evidence that a municipality lacks an official plan "
                "or an EagleFVG publication."
            ),
        },
        "regional_wfs_urban_named_layers": urban_names,
        "wfs_url": WFS_URL,
    }
    meta_path = args.output_dir / "FASE_3_URBAN_PLANNING_VALIDATION_EVIDENCE_v01.json"
    meta_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(metadata, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
