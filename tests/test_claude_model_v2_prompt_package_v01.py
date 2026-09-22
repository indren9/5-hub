import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "docs" / "INPUT_PIPELINE_CLAUDE_MODEL_v2_FVG_v01.md"
MANIFEST = ROOT / "docs" / "CLAUDE_MODEL_v2_PACKAGE_MANIFEST_v01.csv"

EXPECTED_WEIGHTS = ["LIGHT", "HEAVY", "GRID", "LOG", "PGRA", "H2", "COVERAGE"]


def test_weight_placeholders_are_exactly_blank():
    text = PROMPT.read_text(encoding="utf-8")
    assignments = re.findall(
        r"^(LIGHT|HEAVY|GRID|LOG|PGRA|H2|COVERAGE) = (____)$",
        text,
        flags=re.MULTILINE,
    )
    assert [name for name, _ in assignments] == EXPECTED_WEIGHTS
    assert all(value == "____" for _, value in assignments)


def test_prompt_has_no_internal_governance_codes():
    text = PROMPT.read_text(encoding="utf-8")
    forbidden = [
        r"\bDEC-\d+\b",
        r"\bDQ-\d+\b",
        r"\bChat\s+\d+(?:\.\d+)?\b",
        r"\bFASE\s+\d+\b",
    ]
    for pattern in forbidden:
        assert re.search(pattern, text, flags=re.IGNORECASE) is None


def test_prompt_contains_core_model_contract():
    text = PROMPT.read_text(encoding="utf-8")
    required = [
        "D_COV(H) = sum_g[a_g * d_g(H)] / sum_g[a_g]",
        "D_COV* = min_{|H|=5} D_COV(H)",
        "Z_COV(H) = D_COV* / D_COV(H)",
        "Z_j(H) = (1/5) * sum_{i in H} z_ij",
        "Q(H) = [sum_j r_j * Z_j(H) + r_COV * Z_COV(H)] / [sum_j r_j + r_COV]",
        "road_distance_to_nearest_TENT_exit <= 10 km",
        "distanza massima di 200 km",
        "Comune di Trieste",
        "Comune di Udine",
        "Monfalcone/Lisert",
        "non calcolare lo score finale ponderato",
    ]
    for snippet in required:
        assert snippet in text


def test_manifest_is_minimal_and_has_expected_roles():
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter=";"))
    assert len(rows) == 14
    package_paths = [row["package_path"] for row in rows]
    assert len(package_paths) == len(set(package_paths))

    roles = "|".join(row["role"] for row in rows)
    for role in [
        "CANDIDATE_UNIVERSE",
        "LIGHT_EDGE_FLOWS",
        "OSM_ROAD_GRAPH",
        "HEAVY_PATH_FLOWS",
        "HEAVY_EDGE_GEOMETRY",
        "FVG_BOUNDARY",
        "GRID_CP_PROXY",
        "LOGISTICS_POINTS",
        "PGRA_HAZARD",
        "H2_INVENTORY",
        "TENT_CORE",
        "TENT_ROUTE_CROSSWALK",
        "TENT_EXIT_AUDIT",
    ]:
        assert role in roles

    forbidden_fragments = ["00_baseline", "claude_qgis", "conversation", "governance"]
    flat = "\n".join(";".join(row.values()) for row in rows).lower()
    for fragment in forbidden_fragments:
        assert fragment not in flat


def test_candidate_artifacts_fail_closed_until_accepted():
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter=";"))
    candidate_rows = [row for row in rows if row["role"].startswith("CANDIDATE_")]
    assert len(candidate_rows) == 3
    assert all(row["readiness"] == "BLOCKING_PENDING" for row in candidate_rows)
