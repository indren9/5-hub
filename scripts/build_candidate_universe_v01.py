#!/usr/bin/env python3
"""Build the DQ-01 / DEC-0065 V2-1 candidate universe."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import uuid
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pyogrio

from candidate_universe_rules_v01 import (
    first_value,
    geometry_hash,
    map_category,
    repair_and_split,
    semantic_evidence_text,
)

GENERATOR_CLASSES = {
    "G1_PRODUCTIVE", "G2_COMMERCIAL_TERTIARY", "G3_LOGISTICS_TRANSPORT",
    "G4_MIXED_RELEVANT", "G5_TECHNICAL_UTILITY_ENERGY",
}
NATIVE_ID_FIELDS = ["ID", "FID", "GID", "OBJECTID", "ID1", "PKUID", "PK_UID"]
TIER_RANK = {"S1": 1, "S2": 2, "S3": 3, "S4": 4, "S5": 5}

def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8-sig")


def write_csv(path: Path, frame: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False, encoding="utf-8-sig", lineterminator="\n")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def stable_hash(frame: pd.DataFrame, columns: list[str]) -> str:
    if frame.empty:
        return hashlib.sha256(b"").hexdigest().upper()
    data = frame[columns].astype(str).sort_values(columns, kind="stable")
    raw = data.to_csv(index=False, lineterminator="\n").encode("utf-8")
    return hashlib.sha256(raw).hexdigest().upper()


def code6(value: object) -> str:
    s = str(value or "").strip()
    if s.endswith(".0"):
        s = s[:-2]
    digits = "".join(ch for ch in s if ch.isdigit())
    return digits.zfill(6) if digits else ""

def layer_selection_score(row: pd.Series) -> int:
    if "polygon" not in str(row.get("geometry_type", "")).lower():
        return -999
    rel = str(row.get("layer_rel", "")).lower().replace("\\", "/")
    base = rel.rsplit("/", 1)[-1].rsplit(".", 1)[0]
    fields = str(row.get("fields", "")).lower()
    score = 0
    if re.search(r"zonizz|azzon", base):
        score += 180
    if re.search(
        r"zone[_ -]?prg|zoneprg|prgc[_ -]?zone|zone[_ -]?omogen|"
        r"zonaomogen|prgzone|zone[_ -]?ps[_ -]?prgc",
        base,
    ):
        score += 170
    if re.fullmatch(r"(zona|zona1|zone|zto|zto_villa|zone1)(?:_6708)?", base):
        score += 150
    if re.search(r"\bzona\b|\bzone\b", base):
        score += 80
    if "zona_om" in fields or "zona_omoge" in fields:
        score += 60
    if any(x in fields for x in ("dest_prev", "legenda", "zona_desc", "descriz", "zto", "zona_prgc")):
        score += 35
    if re.search(r"ppr/|pgra/|pai/|vincol|acustic|prati|rispetto|rischio|pericol|fasce|boschi|acque|idro|archeolog", rel):
        score -= 260
    if re.search(r"viabil|strad|ferrov|marginatur|servizi|servizio", base):
        score -= 120
    if base.endswith("_s"):
        score -= 120
    if re.search(r"piani_attuativi|prpc|pac_", base):
        score -= 150
    return score

def choose_layers(layer_inv: pd.DataFrame, overrides: pd.DataFrame) -> tuple[dict, pd.DataFrame]:
    inv = layer_inv.copy()
    inv["selection_score"] = inv.apply(layer_selection_score, axis=1)
    inv["feature_count_num"] = pd.to_numeric(inv["feature_count"], errors="coerce").fillna(0)
    override_by_code = {r["municipality_code"]: r for _, r in overrides.iterrows()}
    selected, audit = {}, []
    for code, group in inv.groupby("istat_code", sort=True):
        group = group.sort_values(
            ["selection_score", "feature_count_num", "layer_rel"],
            ascending=[False, False, True],
        )
        top = group.iloc[0]
        second = group.iloc[1] if len(group) > 1 else None
        ov = override_by_code.get(code)
        chosen, status, reason, forced = None, "", "", ""
        if ov is not None:
            exact = group[group["layer_rel"] == ov["layer_rel"]]
            if exact.empty:
                raise RuntimeError(f"Override layer missing for {code}: {ov['layer_rel']}")
            chosen = exact.iloc[0]
            forced = ov["generator_class_override"]
            status = "SELECTED_AUDITED_OVERRIDE" if ov["mode"] == "SELECT_FULL" else "SELECTED_ADDITIVE_CLASS"
            reason = ov["reason"]
            mode = "FULL" if ov["mode"] == "SELECT_FULL" else "ADDITIVE_CLASS"
        elif int(top["selection_score"]) >= 100 and (
            second is None or int(top["selection_score"]) > int(second["selection_score"])
        ):
            chosen = top
            status, reason, mode = "SELECTED_DETERMINISTIC_RULE", "Unique top score >=100", "FULL"
        else:
            status, reason, mode = "NO_UNAMBIGUOUS_FULL_LAYER", "Low or tied top score", "NONE"
        if chosen is not None:
            selected[code] = {
                "mode": mode,
                "layer_path": chosen["layer_path"],
                "layer_rel": chosen["layer_rel"],
                "forced_class": forced,
                "selection_score": int(chosen["selection_score"]),
            }
        audit.append({
            "municipality_code": code,
            "municipality_name": top["comune"],
            "selection_status": status,
            "selected_layer": chosen["layer_rel"] if chosen is not None else "",
            "selected_score": int(chosen["selection_score"]) if chosen is not None else "",
            "top_proposed_layer": top["layer_rel"],
            "top_score": int(top["selection_score"]),
            "second_layer": second["layer_rel"] if second is not None else "",
            "second_score": int(second["selection_score"]) if second is not None else "",
            "reason": reason,
        })
    return selected, pd.DataFrame(audit)


def prepare_gdf(path: Path, operational_crs: str, metadata_crs: str = "") -> tuple[gpd.GeoDataFrame, str, list[str]]:
    gdf = gpd.read_file(path, engine="pyogrio", on_invalid="fix")
    transforms = ["READ_ON_INVALID_FIX_ENABLED"]
    source_crs = str(gdf.crs) if gdf.crs else ""
    if gdf.crs is None:
        meta = (metadata_crs or "").upper()
        if "6708" in meta or "RDN2008" in meta or "TM33" in meta or "6708" in path.name:
            gdf = gdf.set_crs(operational_crs)
            source_crs = operational_crs
            transforms.append("ASSIGN_CRS_FROM_SOURCE_METADATA")
        else:
            raise RuntimeError(f"CRS_UNRESOLVED: {path}")
    if str(gdf.crs).upper() != operational_crs.upper():
        gdf = gdf.to_crs(operational_crs)
        transforms.append(f"REPROJECT_TO_{operational_crs.replace(':', '_')}")
    return gdf, source_crs, transforms

def native_feature_id(row: pd.Series, index: object) -> tuple[str, str]:
    cols = {str(c).upper(): c for c in row.index}
    for key in NATIVE_ID_FIELDS:
        c = cols.get(key)
        if c and pd.notna(row[c]) and str(row[c]).strip():
            return str(row[c]).strip(), str(c)
    return f"ROW_{index}", "ROW_INDEX_FALLBACK"


def tier_flags(tier: str) -> tuple[str, bool, bool, str]:
    if tier == "S1":
        return "TRUE", False, False, ""
    if tier == "S2":
        return "UNKNOWN", True, False, "PLANNING_CURRENTNESS_NOT_VERIFIED"
    if tier == "S3":
        return "TRUE", True, True, "CURRENT_PLAN_VERIFIED_GEOMETRY_PROXY"
    if tier == "S4":
        return "FALSE", True, True, "HISTORICAL_GEOMETRY_PROXY"
    return "UNKNOWN", False, False, "NO_USABLE_POLYGON_SOURCE"


def fallback_tier(currentness_status: str) -> str:
    if currentness_status in {"CURRENT_PLAN_VERIFIED_NO_VECTOR", "CURRENT_VECTOR_VERIFIED"}:
        return "S3"
    return "S4"


def process_source(
    gdf: gpd.GeoDataFrame,
    meta: dict,
    min_area: float,
    namespace: uuid.UUID,
) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    candidates, lineage, exclusions, mappings = [], [], [], []
    mapping_counter = {}
    for idx, row in gdf.iterrows():
        native_code = first_value(row)
        evidence = semantic_evidence_text(row)
        if meta.get("forced_class"):
            generator, rule, status = (
                meta["forced_class"],
                "EXPLICIT_CATEGORY_SPECIFIC_LAYER",
                "RESOLVED_INCLUDED",
            )
        else:
            generator, rule, status = map_category(
                native_code, evidence, meta["source_kind"]
            )
        map_key = (native_code, evidence, generator, rule, status)
        if map_key not in mapping_counter:
            mapping_counter[map_key] = {
                "source_dataset_id": meta["source_dataset_id"],
                "municipality_code": meta["municipality_code"],
                "source_layer": meta["source_layer"],
                "native_zone_code": native_code,
                "native_zone_description": evidence,
                "generator_class": generator,
                "mapping_rule": rule,
                "mapping_status": status,
                "evidence": meta["mapping_evidence"],
                "notes": "",
                "source_feature_count": 0,
            }
        mapping_counter[map_key]["source_feature_count"] += 1

        fid, fid_field = native_feature_id(row, idx)
        original = row.geometry
        parts, transforms = repair_and_split(original)
        if not parts:
            exclusions.append({
                "municipality_code": meta["municipality_code"],
                "municipality_name": meta["municipality_name"],
                "source_dataset_id": meta["source_dataset_id"],
                "source_tier": meta["source_tier"],
                "source_layer": meta["source_layer"],
                "native_feature_id": fid,
                "source_row_index": idx,
                "part_index": "",
                "native_zone_code": native_code,
                "generator_class": generator,
                "exclusion_reason": "NO_POLYGON_AFTER_REPAIR",
                "observed_value": "",
                "geometry_hash": "",
                "detail": "|".join(transforms),
            })
            continue

        for part_index, part in enumerate(parts, start=1):
            gh = geometry_hash(part)
            area = float(part.area)
            base_excl = {
                "municipality_code": meta["municipality_code"],
                "municipality_name": meta["municipality_name"],
                "source_dataset_id": meta["source_dataset_id"],
                "source_tier": meta["source_tier"],
                "source_layer": meta["source_layer"],
                "native_feature_id": fid,
                "source_row_index": idx,
                "part_index": part_index,
                "native_zone_code": native_code,
                "generator_class": generator,
                "observed_value": area,
                "geometry_hash": gh,
            }
            if status == "RESOLVED_EXCLUDED":
                exclusions.append({
                    **base_excl,
                    "exclusion_reason": "NOT_APPROVED_GENERATOR_CLASS",
                    "detail": rule,
                })
                continue
            if status != "RESOLVED_INCLUDED" or generator not in GENERATOR_CLASSES:
                exclusions.append({
                    **base_excl,
                    "exclusion_reason": "GENERATOR_CLASS_UNRESOLVED",
                    "detail": rule,
                })
                continue
            if area < min_area:
                exclusions.append({
                    **base_excl,
                    "exclusion_reason": "MIN_AREA_8000_NOT_MET",
                    "detail": f"threshold_m2={min_area}",
                })
                continue

            identity = "|".join([
                meta["source_dataset_id"],
                meta["municipality_code"],
                meta["source_layer"],
                f"{fid_field}={fid}",
                f"ROW={idx}",
                f"PART={part_index}",
                generator,
            ])
            candidate_id = "CAND-" + str(uuid.uuid5(namespace, identity)).upper()
            verified, proxy, historical, quality_flag = tier_flags(
                meta["source_tier"]
            )
            candidates.append({
                "candidate_id": candidate_id,
                "candidate_version": meta["candidate_version"],
                "universe_version": meta["universe_version"],
                "canonical_identity_key": identity,
                "supersedes_candidate_id": "",
                "geometry_hash": gh,
                "municipality_code": meta["municipality_code"],
                "municipality_name": meta["municipality_name"],
                "generator_class": generator,
                "source_tier": meta["source_tier"],
                "source_dataset_id": meta["source_dataset_id"],
                "source_layer": meta["source_layer"],
                "source_snapshot_path": meta["source_snapshot_path"],
                "source_snapshot_sha256": meta["source_snapshot_sha256"],
                "native_feature_id": fid,
                "native_zone_code": native_code,
                "mapping_rule": rule,
                "currentness_status": meta["currentness_status"],
                "planning_currentness_verified": verified,
                "geometry_proxy_flag": proxy,
                "historical_proxy_flag": historical,
                "quality_flags": quality_flag,
                "area_m2": area,
                "geometry": part,
            })
            lineage.append({
                "candidate_id": candidate_id,
                "precanonical_candidate_id": candidate_id,
                "source_dataset_id": meta["source_dataset_id"],
                "municipality_code": meta["municipality_code"],
                "source_tier": meta["source_tier"],
                "source_layer": meta["source_layer"],
                "source_snapshot_path": meta["source_snapshot_path"],
                "source_snapshot_sha256": meta["source_snapshot_sha256"],
                "native_feature_id": fid,
                "native_id_field": fid_field,
                "source_row_index": idx,
                "part_index": part_index,
                "source_crs": meta["source_crs"],
                "operational_crs": meta["operational_crs"],
                "transformations": "|".join(
                    meta["read_transforms"] + transforms + ["AREA_CHECK"]
                ),
                "geometry_hash": gh,
                "candidate_version": meta["candidate_version"],
                "universe_version": meta["universe_version"],
            })
    mappings.extend(mapping_counter.values())
    return candidates, lineage, exclusions, mappings


def canonicalize(candidates, lineage, exclusions):
    groups = {}
    for row in candidates:
        key = (
            row["municipality_code"],
            row["geometry_hash"],
            row["generator_class"],
        )
        groups.setdefault(key, []).append(row)
    kept, replacement, ndup = [], {}, 0
    for _, rows in sorted(groups.items()):
        rows = sorted(
            rows,
            key=lambda r: (
                TIER_RANK.get(r["source_tier"], 99),
                r["canonical_identity_key"],
            ),
        )
        winner = rows[0]
        kept.append(winner)
        for loser in rows[1:]:
            ndup += 1
            replacement[loser["candidate_id"]] = winner["candidate_id"]
            exclusions.append({
                "municipality_code": loser["municipality_code"],
                "municipality_name": loser["municipality_name"],
                "source_dataset_id": loser["source_dataset_id"],
                "source_tier": loser["source_tier"],
                "source_layer": loser["source_layer"],
                "native_feature_id": loser["native_feature_id"],
                "source_row_index": "",
                "part_index": "",
                "native_zone_code": loser["native_zone_code"],
                "generator_class": loser["generator_class"],
                "exclusion_reason": "DUPLICATE_EXACT_GEOMETRY_CANONICALIZED",
                "observed_value": loser["area_m2"],
                "geometry_hash": loser["geometry_hash"],
                "detail": f"canonical_candidate_id={winner['candidate_id']}",
            })
    for row in lineage:
        old = row["candidate_id"]
        if old in replacement:
            row["candidate_id"] = replacement[old]
            row["transformations"] += "|DUPLICATE_EXACT_GEOMETRY_CANONICALIZED"
    return kept, lineage, exclusions, ndup


def overlap_audit(gdf: gpd.GeoDataFrame) -> pd.DataFrame:
    columns = [
        "candidate_id_a", "candidate_id_b", "municipality_code_a",
        "municipality_code_b", "generator_class_a", "generator_class_b",
        "overlap_area_m2",
    ]
    if gdf.empty:
        return pd.DataFrame(columns=columns)
    rows = []
    sindex = gdf.sindex
    for i, geom in enumerate(gdf.geometry):
        for j in sindex.query(geom, predicate="intersects"):
            j = int(j)
            if j <= i:
                continue
            if gdf.iloc[i]["geometry_hash"] == gdf.iloc[j]["geometry_hash"]:
                continue
            inter = geom.intersection(gdf.geometry.iloc[j])
            area = float(inter.area) if not inter.is_empty else 0.0
            if area > 0:
                rows.append({
                    "candidate_id_a": gdf.iloc[i]["candidate_id"],
                    "candidate_id_b": gdf.iloc[j]["candidate_id"],
                    "municipality_code_a": gdf.iloc[i]["municipality_code"],
                    "municipality_code_b": gdf.iloc[j]["municipality_code"],
                    "generator_class_a": gdf.iloc[i]["generator_class"],
                    "generator_class_b": gdf.iloc[j]["generator_class"],
                    "overlap_area_m2": area,
                })
    return pd.DataFrame(rows, columns=columns)


def load_cer(root: Path, operational_crs: str) -> tuple[dict, dict[str, gpd.GeoDataFrame]]:
    manifest_path = root / "_source_cache" / "cer2018" / "CER_2018_SOURCE_MANIFEST_v01.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    out = {}
    for key in ("D", "H"):
        info = manifest["layers"][key]
        gdf = gpd.read_file(info["path"], engine="pyogrio", on_invalid="fix")
        if gdf.crs is None:
            gdf = gdf.set_crs(operational_crs)
        if str(gdf.crs).upper() != operational_crs.upper():
            gdf = gdf.to_crs(operational_crs)
        gdf["COD_COM"] = gdf["COD_COM"].map(code6)
        out[key] = gdf
    return manifest, out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--coverage", type=Path, required=True)
    ap.add_argument("--source-inventory", type=Path, required=True)
    ap.add_argument("--layer-inventory", type=Path, required=True)
    ap.add_argument("--overrides", type=Path, required=True)
    ap.add_argument("--mapping-output", type=Path, required=True)
    ap.add_argument("--summary-output", type=Path, required=True)
    ap.add_argument("--determinism-reference", type=Path)
    args = ap.parse_args()

    cfg = json.loads(args.config.read_text(encoding="utf-8"))
    root = Path(cfg["output_root"])
    root.mkdir(parents=True, exist_ok=True)
    operational_crs = cfg["operational_crs"]
    min_area = float(cfg["min_area_m2"])
    namespace = uuid.UUID(cfg["uuid_namespace"])

    coverage = read_csv(args.coverage)
    source_inv = read_csv(args.source_inventory)
    layer_inv = read_csv(args.layer_inventory)
    overrides = read_csv(args.overrides)
    if len(coverage) != 215 or coverage["istat_code"].nunique() != 215:
        raise RuntimeError("Coverage must contain 215 unique municipalities")

    selected, selection_df = choose_layers(layer_inv, overrides)
    src_by_code = source_inv.set_index("istat_code").to_dict("index")
    cer_manifest, cer = load_cer(root, operational_crs)

    candidates, lineage, exclusions, mappings, gaps = [], [], [], [], []
    for _, cov in coverage.sort_values("istat_code").iterrows():
        code, comune = cov["istat_code"], cov["comune"]
        selection = selected.get(code)
        src = src_by_code.get(code, {})
        used_tiers, used_sources = [], []

        if selection is not None:
            tier = src.get("source_tier_preliminary", "") or "S2"
            path = Path(selection["layer_path"])
            crs_evidence = "|".join([
                src.get("geometry_crs_metadata", ""),
                src.get("archive_path", ""),
            ])
            gdf, source_crs, read_transforms = prepare_gdf(
                path, operational_crs, crs_evidence
            )
            meta = {
                "municipality_code": code,
                "municipality_name": comune,
                "source_tier": tier,
                "source_dataset_id": cfg["source_dataset_current"],
                "source_layer": selection["layer_rel"],
                "source_snapshot_path": src.get("archive_path", ""),
                "source_snapshot_sha256": src.get("archive_sha256", ""),
                "source_kind": "CURRENT",
                "mapping_evidence": "Official current/best-available PRGC vector; native attributes preserved",
                "forced_class": selection.get("forced_class", ""),
                "currentness_status": cov["currentness_status"],
                "source_crs": source_crs,
                "operational_crs": operational_crs,
                "read_transforms": read_transforms,
                "candidate_version": cfg["candidate_version"],
                "universe_version": cfg["universe_version"],
            }
            c, l, e, m = process_source(gdf, meta, min_area, namespace)
            candidates += c
            lineage += l
            exclusions += e
            mappings += m
            used_tiers.append(tier)
            used_sources.append(selection["layer_rel"])

        full_current = selection is not None and selection["mode"] == "FULL"
        if not full_current:
            for key, kind, klass, dataset_id, layer_name in (
                ("D", "CER_D", "G1_PRODUCTIVE", cfg["source_dataset_cer_ind"], "CER:ZONE_INDUSTRIALI_ARTIG_D"),
                ("H", "CER_H", "G2_COMMERCIAL_TERTIARY", cfg["source_dataset_cer_com"], "CER:ZONE_COMMERCIALI_H"),
            ):
                if selection is not None and selection.get("forced_class") == klass:
                    continue
                sub = cer[key][cer[key]["COD_COM"] == code].copy()
                if sub.empty:
                    continue
                tier = fallback_tier(cov["currentness_status"])
                info = cer_manifest["layers"][key]
                meta = {
                    "municipality_code": code,
                    "municipality_name": comune,
                    "source_tier": tier,
                    "source_dataset_id": dataset_id,
                    "source_layer": layer_name,
                    "source_snapshot_path": info["path"],
                    "source_snapshot_sha256": info["sha256"],
                    "source_kind": kind,
                    "mapping_evidence": (
                        "CER/Mosaicatura PRG 2018 historical geometry fallback; "
                        "S3 only where current plan is verified but vector geometry is unavailable"
                    ),
                    "forced_class": "",
                    "currentness_status": cov["currentness_status"],
                    "source_crs": str(sub.crs),
                    "operational_crs": operational_crs,
                    "read_transforms": ["CER2018_FALLBACK"],
                    "candidate_version": cfg["candidate_version"],
                    "universe_version": cfg["universe_version"],
                }
                c, l, e, m = process_source(sub, meta, min_area, namespace)
                candidates += c
                lineage += l
                exclusions += e
                mappings += m
                used_tiers.append(tier)
                used_sources.append(layer_name)

        status = "USABLE_POLYGON_SOURCE" if used_sources else "NO_USABLE_POLYGON_SOURCE"
        gaps.append({
            "municipality_code": code,
            "municipality_name": comune,
            "phase3_currentness_status": cov["currentness_status"],
            "materialized_current_vector": "YES" if src.get("source_tier_preliminary") in {"S1", "S2"} else "NO",
            "effective_source_tier": "|".join(sorted(set(used_tiers), key=lambda x: TIER_RANK.get(x, 99))) if used_tiers else "S5",
            "source_status": status,
            "selected_sources": "|".join(used_sources),
            "gap_code": "" if used_sources else "NO_USABLE_POLYGON_SOURCE",
            "notes": (
                "CER 2018 is a declared historical/proxy geometry where used."
                if any(x in {"S3", "S4"} for x in used_tiers)
                else ""
            ),
        })

    candidates, lineage, exclusions, duplicate_count = canonicalize(
        candidates, lineage, exclusions
    )
    candidate_gdf = gpd.GeoDataFrame(
        candidates, geometry="geometry", crs=operational_crs
    ).sort_values("candidate_id", kind="stable").reset_index(drop=True)
    lineage_df = pd.DataFrame(lineage).sort_values(
        ["candidate_id", "source_dataset_id", "source_layer", "native_feature_id", "part_index"],
        kind="stable",
    )
    exclusions_df = pd.DataFrame(exclusions)
    if not exclusions_df.empty:
        exclusions_df = exclusions_df.sort_values(
            ["municipality_code", "source_dataset_id", "source_layer", "native_feature_id", "part_index", "exclusion_reason"],
            kind="stable",
        )

    mapping_df = pd.DataFrame(mappings)
    if not mapping_df.empty:
        group_cols = [
            "source_dataset_id", "municipality_code", "source_layer",
            "native_zone_code", "native_zone_description", "generator_class",
            "mapping_rule", "mapping_status", "evidence", "notes",
        ]
        mapping_df = (
            mapping_df.groupby(group_cols, dropna=False, as_index=False)["source_feature_count"]
            .sum()
            .sort_values(
                ["municipality_code", "source_layer", "native_zone_code", "native_zone_description"],
                kind="stable",
            )
        )
    gap_df = pd.DataFrame(gaps).sort_values("municipality_code", kind="stable")
    selection_df = selection_df.sort_values("municipality_code", kind="stable")
    overlaps_df = overlap_audit(candidate_gdf)

    core_cols = [
        "candidate_id", "candidate_version", "universe_version",
        "canonical_identity_key", "geometry_hash", "municipality_code",
        "generator_class", "source_tier", "source_dataset_id", "source_layer",
        "native_feature_id", "native_zone_code", "mapping_rule",
        "currentness_status", "planning_currentness_verified",
        "geometry_proxy_flag", "historical_proxy_flag", "quality_flags", "area_m2",
    ]
    logical_hashes = {
        "universe": stable_hash(candidate_gdf.drop(columns="geometry"), core_cols),
        "lineage": stable_hash(lineage_df, list(lineage_df.columns)),
        "exclusions": stable_hash(exclusions_df, list(exclusions_df.columns)),
        "mapping": stable_hash(mapping_df, list(mapping_df.columns)),
        "source_gaps": stable_hash(gap_df, list(gap_df.columns)),
    }

    determinism_verified = False
    if args.determinism_reference:
        ref = json.loads(args.determinism_reference.read_text(encoding="utf-8"))
        determinism_verified = ref.get("logical_hashes") == logical_hashes

    excl_reason = exclusions_df["exclusion_reason"] if not exclusions_df.empty else pd.Series(dtype=str)
    generator_dist = {
        g: int((candidate_gdf["generator_class"] == g).sum())
        for g in sorted(GENERATOR_CLASSES)
    }
    tier_dist = {
        tier: int((candidate_gdf["source_tier"] == tier).sum())
        for tier in ("S1", "S2", "S3", "S4", "S5")
    }
    muni_tier_presence = {
        tier: int(gap_df["effective_source_tier"].str.split("|").map(lambda xs: tier in xs).sum())
        for tier in ("S1", "S2", "S3", "S4", "S5")
    }
    no_source = gap_df[gap_df["source_status"] == "NO_USABLE_POLYGON_SOURCE"]
    candidate_ids = set(candidate_gdf["candidate_id"])
    lineage_ids = set(lineage_df["candidate_id"]) if not lineage_df.empty else set()

    checks = {
        "candidate_id_unique_non_null": bool(
            candidate_gdf["candidate_id"].notna().all()
            and candidate_gdf["candidate_id"].is_unique
        ),
        "version_fields_complete": bool(
            candidate_gdf["candidate_version"].notna().all()
            and candidate_gdf["universe_version"].notna().all()
        ),
        "geometry_hash_complete": bool(
            candidate_gdf["geometry_hash"].astype(str).str.fullmatch(r"[0-9A-F]{64}").all()
        ),
        "geometry_nonempty_polygon": bool(
            candidate_gdf.geometry.notna().all()
            and (~candidate_gdf.geometry.is_empty).all()
            and candidate_gdf.geom_type.eq("Polygon").all()
        ),
        "geometry_valid": bool(candidate_gdf.is_valid.all()),
        "area_minimum_respected": bool(
            (candidate_gdf["area_m2"] >= min_area).all()
        ),
        "generator_class_resolved": bool(
            candidate_gdf["generator_class"].isin(GENERATOR_CLASSES).all()
        ),
        "currentness_proxy_complete": bool(
            candidate_gdf["currentness_status"].astype(str).str.len().gt(0).all()
            and candidate_gdf["planning_currentness_verified"].astype(str).str.len().gt(0).all()
        ),
        "lineage_complete_for_candidates": candidate_ids.issubset(lineage_ids),
        "source_gap_report_215": bool(
            len(gap_df) == 215 and gap_df["municipality_code"].nunique() == 215
        ),
        "source_tiers_valid": bool(
            candidate_gdf["source_tier"].isin(["S1", "S2", "S3", "S4"]).all()
        ),
        "no_dq02_fields": not any(
            c.lower().startswith(
                ("score", "weight", "normalized", "indicator_", "objective")
            )
            for c in candidate_gdf.columns
        ),
        "determinism_verified": determinism_verified,
    }
    checks["all_required_checks_pass"] = bool(all(checks.values()))

    qa = {
        "universe_version": cfg["universe_version"],
        "operational_crs": operational_crs,
        "min_area_m2": min_area,
        "candidate_count": int(len(candidate_gdf)),
        "excluded_min_area_count": int((excl_reason == "MIN_AREA_8000_NOT_MET").sum()),
        "generator_unresolved_count": int((excl_reason == "GENERATOR_CLASS_UNRESOLVED").sum()),
        "not_generator_excluded_count": int((excl_reason == "NOT_APPROVED_GENERATOR_CLASS").sum()),
        "exact_duplicates_canonicalized": int(duplicate_count),
        "generator_distribution": generator_dist,
        "source_tier_distribution_candidates": tier_dist,
        "source_tier_presence_municipalities": muni_tier_presence,
        "municipalities_no_usable_polygon_source": int(len(no_source)),
        "municipalities_no_usable_polygon_source_codes": no_source["municipality_code"].tolist(),
        "municipalities_no_usable_polygon_source_names": no_source["municipality_name"].tolist(),
        "overlap_pairs_positive_area": int(len(overlaps_df)),
        "overlap_area_m2_sum_pairwise": (
            float(overlaps_df["overlap_area_m2"].sum())
            if not overlaps_df.empty
            else 0.0
        ),
        "layer_selection_status": selection_df["selection_status"].value_counts().to_dict(),
        "mapping_status": mapping_df["mapping_status"].value_counts().to_dict(),
        "logical_hashes": logical_hashes,
        "determinism_reference": str(args.determinism_reference or ""),
        "determinism_verified": determinism_verified,
        "qa_checks": checks,
    }

    gpkg = root / "CANDIDATE_UNIVERSE_v01.gpkg"
    if gpkg.exists():
        gpkg.unlink()
    pyogrio.write_dataframe(
        candidate_gdf, gpkg, layer="candidate_universe_v01", driver="GPKG"
    )
    lineage_path = root / "CANDIDATE_LINEAGE_v01.csv"
    exclusions_path = root / "CANDIDATE_EXCLUSIONS_v01.csv"
    gaps_path = root / "CANDIDATE_SOURCE_GAPS_v01.csv"
    selection_path = root / "CANDIDATE_SOURCE_LAYER_SELECTION_v01.csv"
    overlap_path = root / "CANDIDATE_OVERLAP_QA_v01.csv"
    qa_path = root / "V2_1_CANDIDATE_UNIVERSE_QA_v01.json"

    write_csv(lineage_path, lineage_df)
    write_csv(exclusions_path, exclusions_df)
    write_csv(gaps_path, gap_df)
    write_csv(selection_path, selection_df)
    write_csv(overlap_path, overlaps_df)
    write_csv(args.mapping_output, mapping_df)
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    summary_rows = [
        {"metric": "candidate_count", "value": len(candidate_gdf)},
        {"metric": "excluded_min_area_count", "value": qa["excluded_min_area_count"]},
        {"metric": "generator_unresolved_count", "value": qa["generator_unresolved_count"]},
        {"metric": "exact_duplicates_canonicalized", "value": duplicate_count},
        {"metric": "overlap_pairs_positive_area", "value": len(overlaps_df)},
        {"metric": "municipalities_no_usable_polygon_source", "value": len(no_source)},
    ]
    for key, value in generator_dist.items():
        summary_rows.append({"metric": f"generator_{key}", "value": value})
    for key, value in tier_dist.items():
        summary_rows.append({"metric": f"candidate_source_tier_{key}", "value": value})
    for key, value in muni_tier_presence.items():
        summary_rows.append({"metric": f"municipality_source_tier_{key}", "value": value})
    for key, value in logical_hashes.items():
        summary_rows.append({"metric": f"logical_sha256_{key}", "value": value})
    write_csv(args.summary_output, pd.DataFrame(summary_rows))

    input_paths = [
        args.config, args.coverage, args.source_inventory,
        args.layer_inventory, args.overrides,
        root / "_source_cache" / "cer2018" / "CER_2018_SOURCE_MANIFEST_v01.json",
    ]
    if args.determinism_reference:
        input_paths.append(args.determinism_reference)
    artifact_paths = [
        gpkg, lineage_path, exclusions_path, gaps_path, selection_path,
        overlap_path, qa_path, args.mapping_output, args.summary_output,
    ]
    manifest = {
        "producer": Path(__file__).name,
        "universe_version": cfg["universe_version"],
        "inputs": [
            {"path": str(x), "sha256": sha256_file(x), "bytes": x.stat().st_size}
            for x in input_paths
        ],
        "artifacts": [
            {"path": str(x), "sha256": sha256_file(x), "bytes": x.stat().st_size}
            for x in artifact_paths
        ],
        "logical_hashes": logical_hashes,
    }
    manifest_path = root / "CANDIDATE_UNIVERSE_MANIFEST_v01.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print(json.dumps({
        "candidate_count": len(candidate_gdf),
        "excluded_min_area_count": qa["excluded_min_area_count"],
        "generator_distribution": generator_dist,
        "source_tier_distribution_candidates": tier_dist,
        "source_tier_presence_municipalities": muni_tier_presence,
        "municipalities_no_usable_polygon_source": len(no_source),
        "municipalities_no_usable_polygon_source_codes": no_source["municipality_code"].tolist(),
        "municipalities_no_usable_polygon_source_names": no_source["municipality_name"].tolist(),
        "generator_unresolved_count": qa["generator_unresolved_count"],
        "exact_duplicates_canonicalized": duplicate_count,
        "overlap_pairs_positive_area": len(overlaps_df),
        "qa_all_pass": checks["all_required_checks_pass"],
        "determinism_verified": determinism_verified,
        "logical_hashes": logical_hashes,
        "gpkg_sha256": sha256_file(gpkg),
        "manifest_sha256": sha256_file(manifest_path),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
