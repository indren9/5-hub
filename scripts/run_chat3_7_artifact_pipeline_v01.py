from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

GENERATED = [
    "TENT_FVG_ROUTE_MATCH_DIAGNOSTIC_v01.csv",
    "TENT_FVG_ROUTE_CROSSWALK_v01.csv",
    "TENT_FVG_OSM_ACCESS_DIAGNOSTIC_v01.csv",
    "TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv",
    "TENT_FVG_CROSSWALK_QA_v01.json",
]


def parse_args():
    p = argparse.ArgumentParser(
        description="Run Chat 3.7 artifact production in the only supported deterministic order."
    )
    p.add_argument("--project-root", type=Path, required=True)
    p.add_argument("--osm-gpkg", type=Path, required=True)
    return p.parse_args()


def run(cmd: list[str]) -> None:
    print("RUN:", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main():
    a = parse_args()
    scripts = Path(__file__).resolve().parent
    source_dir = (
        a.project_root
        / "02_external_sources"
        / "F3_CHAT_3_7"
        / "TEN_T_CURRENT_v01"
    )
    operator_dir = (
        a.project_root
        / "02_external_sources"
        / "F3_CHAT_3_7"
        / "operator_evidence"
    )
    output_dir = a.project_root / "05_intermediate_outputs" / "F3_CHAT_3_7"
    roadgraph = (
        a.project_root
        / "01_raw_data"
        / "F3_CHAT_3_3"
        / "GRAFO_STRADALE_FVG_WFS_20260918.geojson"
    )
    manifest = (
        a.project_root
        / "02_external_sources"
        / "F3_CHAT_3_7"
        / "FINAL_EVIDENCE_MANIFEST_v01.json"
    )
    qa = output_dir / "TENT_FVG_CROSSWALK_QA_v01.json"

    output_dir.mkdir(parents=True, exist_ok=True)

    # Remove generated-state markers first. If any stage fails, stale QA/manifest
    # cannot survive and masquerade as a successful current package.
    for name in GENERATED:
        p = output_dir / name
        if p.exists():
            p.unlink()
    if manifest.exists():
        manifest.unlink()

    run(
        [
            sys.executable,
            str(scripts / "build_tent_fvg_crosswalk_chat3_7_v01.py"),
            "--source-dir",
            str(source_dir),
            "--roadgraph",
            str(roadgraph),
            "--osm-gpkg",
            str(a.osm_gpkg),
            "--output-dir",
            str(output_dir),
        ]
    )

    run(
        [
            sys.executable,
            str(scripts / "build_tent_exit_relevance_audit_chat3_7_v01.py"),
            "--crosswalk",
            str(output_dir / "TENT_FVG_ROUTE_CROSSWALK_v01.csv"),
            "--osm-diagnostic",
            str(output_dir / "TENT_FVG_OSM_ACCESS_DIAGNOSTIC_v01.csv"),
            "--operator-evidence-dir",
            str(operator_dir),
            "--output",
            str(output_dir / "TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv"),
        ]
    )

    run(
        [
            sys.executable,
            str(scripts / "finalize_tent_artifacts_chat3_7_v01.py"),
            "--project-root",
            str(a.project_root),
            "--source-dir",
            str(source_dir),
            "--operator-evidence-dir",
            str(operator_dir),
            "--roadgraph",
            str(roadgraph),
            "--osm-gpkg",
            str(a.osm_gpkg),
            "--output-dir",
            str(output_dir),
            "--manifest",
            str(manifest),
            "--qa",
            str(qa),
        ]
    )

    print("PIPELINE_STATUS=PASS")


if __name__ == "__main__":
    main()
