from __future__ import annotations

import argparse
import csv
import os
import tempfile
from pathlib import Path

EVIDENCE = {
    "A4": {
        "files": "Autostrade_Alto_Adriatico_network_20260918.html",
        "summary": (
            "Autostrade Alto Adriatico identifies A4 Venezia-Trieste as a "
            "concession motorway; TENtec classifies the FVG sections as Core."
        ),
        "manual_note": (
            "The two OSM raw non-link adjacencies associated with the Bretella "
            "di Latisana were reviewed as interchange/link context rather than "
            "ordinary at-grade intersections of the TEN-T mainline."
        ),
        "morphology": "CONTROLLED_ACCESS_GRADE_SEPARATED",
    },
    "A23": {
        "files": (
            "Autostrade_Alto_Adriatico_network_20260918.html;"
            "ASPI_A23_Pontebba_confine_20260914.html"
        ),
        "summary": (
            "Autostrade Alto Adriatico identifies A23 Palmanova-Udine as a "
            "concession motorway; Autostrade per l'Italia current A23 evidence "
            "for Udine-Tarvisio explicitly refers to stations, entrances, exits "
            "and svincoli."
        ),
        "manual_note": (
            "The automatic OSM diagnostic found no raw non-link adjacency "
            "requiring escalation; operator evidence is consistent with access "
            "through motorway junctions/interchanges."
        ),
        "morphology": "CONTROLLED_ACCESS_GRADE_SEPARATED",
    },
    "RA13": {
        "files": "ANAS_soccorso_stradale_unita_FVG_2026.pdf",
        "summary": (
            "ANAS official FVG road-rescue documentation describes RA13 through "
            "named svincoli and motorway/interconnected-motorway operational context."
        ),
        "manual_note": (
            "The automatic OSM diagnostic found no raw non-link adjacency; the "
            "documentary review did not identify an ordinary at-grade TEN-T "
            "mainline access replacing a true junction/ramp."
        ),
        "morphology": "GRADE_SEPARATED_RAMP_INTERCHANGES",
    },
    "RA14": {
        "files": "ANAS_soccorso_stradale_unita_FVG_2026.pdf",
        "summary": (
            "ANAS official FVG road-rescue documentation identifies RA14 between "
            "the RA13 connection and Fernetti using junction/interchange context."
        ),
        "manual_note": (
            "The automatic OSM diagnostic found no raw non-link adjacency; the "
            "documentary review is consistent with grade-separated junction access."
        ),
        "morphology": "GRADE_SEPARATED_RAMP_INTERCHANGES",
    },
    "A/SS202": {
        "files": "ANAS_soccorso_stradale_unita_FVG_2026.pdf",
        "summary": (
            "ANAS official FVG road-rescue documentation describes the SS202/A "
            "axis through named svincoli and interconnected-road context."
        ),
        "manual_note": (
            "The OSM raw non-link candidate at Via della Rampa was reviewed in "
            "context as a ramp/link structure of the Nuova Sopraelevata, not an "
            "ordinary at-grade intersection of the TEN-T mainline."
        ),
        "morphology": "GRADE_SEPARATED_RAMP_INTERCHANGES",
    },
    "A28": {
        "files": "Autostrade_Alto_Adriatico_network_20260918.html",
        "summary": (
            "Autostrade Alto Adriatico identifies A28 Portogruaro-Conegliano as "
            "a concession motorway; it is the comprehensive-only FVG axis in the "
            "current crosswalk."
        ),
        "manual_note": (
            "The automatic OSM diagnostic found no raw non-link adjacency; the "
            "operator classification and motorway-junction context do not indicate "
            "an ordinary at-grade TEN-T mainline access."
        ),
        "morphology": "CONTROLLED_ACCESS_GRADE_SEPARATED",
    },
}


def parse_args():
    p = argparse.ArgumentParser(
        description="Build the validated TEN-T FVG exit-relevance audit."
    )
    p.add_argument("--crosswalk", type=Path, required=True)
    p.add_argument("--osm-diagnostic", type=Path, required=True)
    p.add_argument("--operator-evidence-dir", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    return p.parse_args()


def read_csv(path: Path) -> list[dict]:
    with path.open("r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def atomic_write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    os.close(fd)
    tmp_path = Path(tmp)
    try:
        with tmp_path.open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(rows)
        os.replace(tmp_path, path)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def main():
    a = parse_args()
    if a.output.name != "TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv":
        raise ValueError(
            "This script is the sole authoritative writer for "
            "TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv"
        )
    crosswalk = read_csv(a.crosswalk)
    osm_rows = read_csv(a.osm_diagnostic)

    if len(crosswalk) != 6:
        raise RuntimeError(f"Expected 6 crosswalk route-axis records, got {len(crosswalk)}")
    official_sections = sum(int(r["official_section_count"]) for r in crosswalk)
    if official_sections != 11:
        raise RuntimeError(
            f"Expected 11 official TENtec sections aggregated in crosswalk, got {official_sections}"
        )
    if len(osm_rows) != 6:
        raise RuntimeError(f"Expected 6 OSM diagnostic records, got {len(osm_rows)}")

    osm_by_route = {r["tent_route_axis"]: r for r in osm_rows}
    if set(osm_by_route) != set(EVIDENCE):
        raise RuntimeError(
            f"OSM diagnostic route set mismatch: {sorted(osm_by_route)}"
        )

    for info in EVIDENCE.values():
        for filename in info["files"].split(";"):
            path = a.operator_evidence_dir / filename
            if not path.exists():
                raise FileNotFoundError(f"Missing operator evidence: {path}")

    audit_rows = []
    for cw in crosswalk:
        route = cw["tent_route_axis"]
        info = EVIDENCE[route]
        osm = osm_by_route[route]
        audit_rows.append(
            {
                "tent_tier": cw["tent_tier"],
                "tent_route_axis": route,
                "official_section_count": cw["official_section_count"],
                "tentec_feature_ids": cw["tentec_feature_ids"],
                "tentec_types": cw["tentec_types"],
                "automatic_osm_machine_status": osm["machine_status"],
                "automatic_osm_raw_nonlink_adjacency_count": osm[
                    "osm_raw_nonlink_adjacency_count"
                ],
                "automatic_osm_raw_nonlink_examples": osm[
                    "osm_raw_nonlink_examples"
                ],
                "operator_evidence_files": info["files"],
                "operator_evidence_summary": info["summary"],
                "manual_documentary_validation": info["manual_note"],
                "validated_access_morphology": info["morphology"],
                "ordinary_at_grade_intersection_validated": "NO",
                "true_exit_or_ramp_access_validated": "YES",
                "afir_nearest_exit_issue_materially_relevant_fvg": "NO",
                "validation_status": "VALIDATED_NO_MATERIAL_EXIT_AMBIGUITY",
                "lineage": (
                    "TEN-T membership/tier: TENtec 2024; "
                    "automatic topology diagnostic: frozen OSM; "
                    "access morphology: operator/ANAS evidence + manual review; "
                    "final conclusion: validated audit"
                ),
            }
        )

    audit_rows.sort(
        key=lambda r: (
            {"CORE": 0, "EXTENDED_CORE": 1, "COMPREHENSIVE": 2}[r["tent_tier"]],
            r["tent_route_axis"],
        )
    )
    atomic_write_csv(a.output, audit_rows, list(audit_rows[0].keys()))
    print(
        f"wrote={a.output}\n"
        f"route_axis_records={len(audit_rows)}\n"
        f"official_tentec_sections={sum(int(r['official_section_count']) for r in audit_rows)}"
    )


if __name__ == "__main__":
    main()
