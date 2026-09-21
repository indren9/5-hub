from __future__ import annotations

import hashlib
import json
from pathlib import Path

import geopandas as gpd
import pandas as pd

REPO = Path(__file__).resolve().parents[1]
CFG = json.loads((REPO / "config" / "candidate_universe_v01.json").read_text(encoding="utf-8"))
OUT = Path(CFG["output_root"])
GPKG = OUT / "CANDIDATE_UNIVERSE_v01.gpkg"
QA = OUT / "V2_1_CANDIDATE_UNIVERSE_QA_v01.json"


def load_candidates() -> gpd.GeoDataFrame:
    return gpd.read_file(GPKG, layer="candidate_universe_v01", engine="pyogrio")


def test_machine_qa_passes() -> None:
    qa = json.loads(QA.read_text(encoding="utf-8"))
    assert qa["qa_checks"]["all_required_checks_pass"] is True
    assert qa["determinism_verified"] is True
    assert qa["candidate_count"] == 3993


def test_candidate_contract() -> None:
    g = load_candidates()
    expected_classes = {
        "G1_PRODUCTIVE",
        "G2_COMMERCIAL_TERTIARY",
        "G3_LOGISTICS_TRANSPORT",
        "G4_MIXED_RELEVANT",
        "G5_TECHNICAL_UTILITY_ENERGY",
    }
    assert len(g) == 3993
    assert g.crs.to_epsg() == 6708
    assert g.geometry.notna().all()
    assert (~g.geometry.is_empty).all()
    assert g.geom_type.eq("Polygon").all()
    assert g.is_valid.all()
    assert (g["area_m2"] >= float(CFG["min_area_m2"])).all()
    assert g["candidate_id"].notna().all()
    assert g["candidate_id"].is_unique
    assert g["geometry_hash"].str.fullmatch(r"[0-9A-F]{64}").all()
    assert g["generator_class"].isin(expected_classes).all()
    assert g["source_tier"].isin({"S1", "S2", "S3", "S4"}).all()

    assert g["candidate_version"].notna().all()
    assert g["universe_version"].eq(CFG["universe_version"]).all()
    forbidden_prefixes = ("score", "weight", "normalized", "indicator_", "objective")
    assert not any(c.lower().startswith(forbidden_prefixes) for c in g.columns)


def test_exclusions_gaps_and_lineage() -> None:
    g = load_candidates()
    exclusions = pd.read_csv(OUT / "CANDIDATE_EXCLUSIONS_v01.csv", encoding="utf-8-sig")
    gaps = pd.read_csv(
        OUT / "CANDIDATE_SOURCE_GAPS_v01.csv", dtype={"municipality_code": str},
        encoding="utf-8-sig",
    )
    lineage = pd.read_csv(OUT / "CANDIDATE_LINEAGE_v01.csv", encoding="utf-8-sig")
    min_area = exclusions[exclusions["exclusion_reason"] == "MIN_AREA_8000_NOT_MET"]
    observed = pd.to_numeric(min_area["observed_value"], errors="raise")
    assert len(min_area) == 5125
    assert (observed < float(CFG["min_area_m2"])).all()
    assert len(gaps) == 215 and gaps["municipality_code"].nunique() == 215
    assert int((gaps["gap_code"] == "NO_USABLE_POLYGON_SOURCE").sum()) == 5
    assert set(g["candidate_id"]).issubset(set(lineage["candidate_id"]))



def test_manifest_integrity() -> None:
    manifest = json.loads(
        (OUT / "CANDIDATE_UNIVERSE_MANIFEST_v01.json").read_text(encoding="utf-8")
    )
    for item in manifest["inputs"] + manifest["artifacts"]:
        path = Path(item["path"])
        assert path.exists(), path
        digest = hashlib.sha256(path.read_bytes()).hexdigest().upper()
        assert digest == item["sha256"], path
        assert path.stat().st_size == int(item["bytes"])
