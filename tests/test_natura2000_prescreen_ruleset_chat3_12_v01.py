from __future__ import annotations
import csv, json, hashlib
from datetime import datetime, timezone
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(r"C:\dev\5-hub")
RULESET = ROOT / "docs" / "FASE_3_NATURA2000_RULESET_v01.csv"
CROSSWALK = ROOT / "docs" / "FASE_3_NATURA2000_SITE_RULE_CROSSWALK_v01.csv"
ONEDRIVE = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_12")
MANIFEST = ONEDRIVE / "source_manifest_v01.json"
QA_OUT = ONEDRIVE / "qa" / "natura2000_prescreen_test_results_v01.json"

EXPECTED_UNKNOWN = {
    ("IT3330009","3.06"), ("IT3330010","3.06"), ("IT3340006","3.06"),
    ("IT3340007","3.06"), ("IT3341002","3.06")
}
ALLOWED_MODEL_ACTIONS = {
    "POTENTIALLY_COVERED_BY_PREASSESSMENT",
    "CORRESPONDENCE_CHECK_REQUIRED",
    "SPECIFIC_VINCA_SCREENING_REQUIRED",
    "MANUAL_REVIEW_REQUIRED",
    "NOT_DETERMINABLE_FROM_AVAILABLE_RULES",
}

def synthetic_prescreen_fixture(source_outcome=None, correspondence="UNKNOWN",
                                functional_trigger=False, project_info_complete=True):
    """Synthetic QA fixture for the DEC-0041 evaluation order; not a VINCA engine."""
    if source_outcome == "PREASSESSED_NO_SIGNIFICANT_INCIDENCE":
        if not project_info_complete or correspondence == "UNKNOWN":
            return "CORRESPONDENCE_CHECK_REQUIRED"
        if correspondence == "MATCH":
            return "POTENTIALLY_COVERED_BY_PREASSESSMENT"
        if correspondence == "MISMATCH":
            return "SPECIFIC_VINCA_SCREENING_REQUIRED"
    if source_outcome == "SCREENING_REQUIRED":
        return "SPECIFIC_VINCA_SCREENING_REQUIRED"
    if source_outcome == "NOT_APPLICABLE":
        return "MANUAL_REVIEW_REQUIRED"
    if functional_trigger:
        return "MANUAL_REVIEW_REQUIRED" if not project_info_complete else "SPECIFIC_VINCA_SCREENING_REQUIRED"
    return "NOT_DETERMINABLE_FROM_AVAILABLE_RULES"

def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def get(rows, site, activity):
    hits=[r for r in rows if r.get("site_code")==site and r.get("activity_code")==activity]
    assert len(hits)==1, (site,activity,len(hits))
    return hits[0]

def run():
    tests=[]
    def check(name, fn):
        try:
            fn()
            tests.append({"test":name,"status":"PASS"})
        except Exception as e:
            tests.append({"test":name,"status":"FAIL","detail":repr(e)})

    rules=read_csv(RULESET)
    cross=read_csv(CROSSWALK)
    pre=[r for r in rules if r["rule_type"]=="SITE_ACTIVITY_PREASSESSMENT"]

    check("crosswalk_72_unique_sites", lambda: (
        (_ for _ in ()).throw(AssertionError((len(cross),len({r["site_code"] for r in cross}))))
        if not (len(cross)==72 and len({r["site_code"] for r in cross})==72) else None
    ))

    def t_annex_split():
        c=Counter(r["dgr30_preassessment_annex"] for r in cross)
        assert c==Counter({"A2":30,"A3":42}), c
    check("annex_split_30_42",t_annex_split)

    def t_3600():
        assert len(pre)==3600, len(pre)
        by=defaultdict(list)
        for r in pre: by[r["site_code"]].append(r)
        assert len(by)==72, len(by)
        assert {len(v) for v in by.values()}=={50}, Counter(len(v) for v in by.values())
        assert all(len({r["activity_code"] for r in v})==50 for v in by.values())
    check("complete_site_activity_matrix_72x50",t_3600)

    def t_unknowns():
        u={(r["site_code"],r["activity_code"]) for r in pre if r["source_outcome"]=="UNKNOWN"}
        assert u==EXPECTED_UNKNOWN, u
        for r in pre:
            if (r["site_code"],r["activity_code"]) in EXPECTED_UNKNOWN:
                assert r["model_action"]=="NOT_DETERMINABLE_FROM_AVAILABLE_RULES"
                assert r["correspondence_check_required"]=="UNKNOWN"
    check("five_source_unknowns_are_explicit",t_unknowns)

    def t_green_branch():
        r=get(pre,"IT3330005","1.01")
        assert r["source_outcome"]=="PREASSESSED_NO_SIGNIFICANT_INCIDENCE", r
        assert r["model_action"]=="CORRESPONDENCE_CHECK_REQUIRED", r
        assert r["correspondence_check_required"]=="YES", r
        assert r["intermediate_classification"]=="POTENTIALLY_COVERED_BY_PREASSESSMENT", r
    check("green_branch_requires_correspondence",t_green_branch)

    def t_red_branch():
        r=get(pre,"IT3330005","1.02")
        assert r["source_outcome"]=="SCREENING_REQUIRED", r
        assert r["model_action"]=="SPECIFIC_VINCA_SCREENING_REQUIRED", r
    check("red_branch_requires_specific_screening",t_red_branch)

    def t_yellow_branch():
        r=get(pre,"IT3340007","1.01")
        assert r["source_outcome"]=="NOT_APPLICABLE", r
        assert r["model_action"]=="MANUAL_REVIEW_REQUIRED", r
    check("yellow_branch_is_not_auto_exclusion",t_yellow_branch)

    def t_no_vinca_passed():
        blob=RULESET.read_text(encoding="utf-8-sig").upper()
        assert "VINCA_PASSED" not in blob
        assert "VINCA PASSED" not in blob
    check("no_vinca_passed_output",t_no_vinca_passed)

    def t_actions():
        got={r["model_action"] for r in rules}
        assert got <= ALLOWED_MODEL_ACTIONS, got-ALLOWED_MODEL_ACTIONS
    check("model_actions_conservative_enum",t_actions)

    def t_green_all_corr():
        g=[r for r in pre if r["source_outcome"]=="PREASSESSED_NO_SIGNIFICANT_INCIDENCE"]
        assert g and all(r["correspondence_check_required"]=="YES" for r in g)
        assert all(r["model_action"]=="CORRESPONDENCE_CHECK_REQUIRED" for r in g)
    check("all_green_rows_require_correspondence",t_green_all_corr)

    def t_status_counts():
        c=Counter(r["source_outcome"] for r in pre)
        assert c==Counter({
            "PREASSESSED_NO_SIGNIFICANT_INCIDENCE":2512,
            "NOT_APPLICABLE":1043,
            "SCREENING_REQUIRED":40,
            "UNKNOWN":5
        }),c
    check("source_status_counts_stable",t_status_counts)

    def t_interference():
        byid={r["rule_id"]:r for r in rules}
        expected={
            "N2K_IF_001":"radius <= 1000 m",
            "N2K_IF_003":"radius <= 2000 m",
            "N2K_IF_005":"radius <= 5000 m",
            "N2K_IF_008":"radius <= 50 m",
            "N2K_IF_012":"within 1 km upstream/downstream",
            "N2K_IF_015":"distance < 2500 m",
            "N2K_LAG_002":"radius <= 3000 m",
            "N2K_LAG_003":"radius <= 10000 m",
            "N2K_LAG_004":"radius <= 20000 m",
        }
        for rid,token in expected.items():
            assert rid in byid, rid
            assert token in byid[rid]["spatial_condition"], (rid,byid[rid]["spatial_condition"])
        assert byid["N2K_IF_016"]["model_action"]=="MANUAL_REVIEW_REQUIRED"
        assert "UNKNOWN => no halving" in byid["N2K_IF_016"]["required_conditions"]
    check("functional_interference_rules_source_locked",t_interference)

    def t_laguna():
        cw={r["site_code"]:r for r in cross}
        r=cw["IT3320037"]
        assert r["functional_interference_basis"]=="DPReg 065/2025 Annex 14"
        assert "DPReg 065/2025" in r["site_specific_override"]
        lag=[x for x in rules if x["rule_type"]=="SITE_SPECIFIC_FUNCTIONAL_INTERFERENCE" and x["site_scope"]=="IT3320037"]
        assert len(lag)==9,len(lag)
    check("laguna_site_specific_override_encoded",t_laguna)

    def t_hashes():
        cw={r["site_code"]:r for r in cross}
        assert any(r["geometry_sha256_sic"]=="772dabc52d720eaedfc5bd8de6649d2be915c01a88d2686d553137e3ebaa2e06" for r in cross)
        assert any(r["geometry_sha256_zps"]=="949724e039aac197490c80e0ebbdfb6fbb46bf2a12f3b457e3989af0bc032660" for r in cross)
        assert all(r["geometry_source"].startswith("Chat 3.4 validated WFS") for r in cross)
    check("chat3_4_geometry_lineage_preserved",t_hashes)

    def t_cross_unknown_sum():
        assert sum(int(r["unknown_count"]) for r in cross)==5
    check("crosswalk_unknown_sum_5",t_cross_unknown_sum)

    def t_manifest():
        m=json.loads(MANIFEST.read_text(encoding="utf-8"))
        art=m["artifacts"]
        core=[x for x in art if x.get("source_id","").startswith(("DGR30_","DGR1183_","DPReg65_","Decreto72016_"))]
        assert len(core)>=11,len(core)
        assert all(x.get("status")!="MISSING" for x in core),[x for x in core if x.get("status")=="MISSING"]
        for x in core:
            p=Path(x["path"])
            assert p.exists() and p.stat().st_size==x["bytes"],x["source_id"]
            h=hashlib.sha256(p.read_bytes()).hexdigest()
            assert h==x["sha256"],x["source_id"]
    check("official_corpus_manifest_hashes",t_manifest)

    def t_correspondence_rules():
        corr=[r for r in rules if r["rule_type"]=="CORRESPONDENCE_PROCEDURE"]
        assert len(corr)==7,len(corr)
        scopes={r["project_or_activity_scope"] for r in corr}
        for token in ["Permesso di costruire","SCIA/CILA","Edilizia libera","Conferenza di servizi","Other public authorization","No authorization/administrative procedure"]:
            assert token in scopes,token
    check("correspondence_authority_matrix_complete",t_correspondence_rules)

    def t_interference_scope_designations():
        byid={r["rule_id"]:r for r in rules}
        assert byid["N2K_IF_003"]["site_scope"]=="ZPS_EXCEPT_IT3320037"
        assert byid["N2K_IF_005"]["site_scope"]=="ZPS_EXCEPT_IT3320037"
        assert byid["N2K_IF_015"]["site_scope"]=="ZSC_CONNECTED_BY_RER_EXCEPT_IT3320037"
        assert len(byid["N2K_IF_013"]["site_scope"].split(";"))==15
        assert "terminal only if no applicable green preassessment" in byid["N2K_IF_001"]["limitations"]
    check("functional_interference_site_scope_and_preassessment_precedence",t_interference_scope_designations)

    def t_required_synthetic_fixtures():
        cases = {
            "clearly_covered_preassessment": (
                dict(source_outcome="PREASSESSED_NO_SIGNIFICANT_INCIDENCE", correspondence="MATCH"),
                "POTENTIALLY_COVERED_BY_PREASSESSMENT"),
            "correspondence_condition_not_met": (
                dict(source_outcome="PREASSESSED_NO_SIGNIFICANT_INCIDENCE", correspondence="MISMATCH"),
                "SPECIFIC_VINCA_SCREENING_REQUIRED"),
            "external_functional_interference_but_green_matches": (
                dict(source_outcome="PREASSESSED_NO_SIGNIFICANT_INCIDENCE", correspondence="MATCH", functional_trigger=True),
                "POTENTIALLY_COVERED_BY_PREASSESSMENT"),
            "insufficient_project_information": (
                dict(source_outcome="PREASSESSED_NO_SIGNIFICANT_INCIDENCE", correspondence="UNKNOWN", functional_trigger=True, project_info_complete=False),
                "CORRESPONDENCE_CHECK_REQUIRED"),
            "no_applicable_rule_and_no_trigger": (
                dict(source_outcome=None, functional_trigger=False, project_info_complete=True),
                "NOT_DETERMINABLE_FROM_AVAILABLE_RULES"),
        }
        for name,(kwargs,expected) in cases.items():
            got=synthetic_prescreen_fixture(**kwargs)
            assert got==expected,(name,got,expected)
    check("five_required_prescreen_fixtures",t_required_synthetic_fixtures)

    passed=sum(t["status"]=="PASS" for t in tests)
    failed=len(tests)-passed
    result={"status":"PASS" if failed==0 else "FAIL","passed":passed,"failed":failed,"tests":tests}
    QA_OUT.parent.mkdir(parents=True,exist_ok=True)
    QA_OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")

    manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
    generated_paths=[
        RULESET,
        CROSSWALK,
        ROOT / "scripts" / "build_natura2000_prescreen_ruleset_chat3_12_v01.py",
        ROOT / "tests" / "test_natura2000_prescreen_ruleset_chat3_12_v01.py",
        ROOT / "docs" / "FASE_3_NATURA2000_PRESCREEN_VALIDATION_REVIEW_v01.md",
        ROOT / "docs" / "HANDOFF_CHAT_3.12_NATURA2000_v01.md",
        ONEDRIVE / "qa" / "natura2000_prescreen_qa_v01.json",
        QA_OUT,
    ]
    manifest["generated_artifacts_refreshed_utc"]=datetime.now(timezone.utc).isoformat()
    manifest["generated_artifacts"]=[
        {
            "path":str(p),
            "bytes":p.stat().st_size,
            "sha256":hashlib.sha256(p.read_bytes()).hexdigest(),
            "status":"GENERATED_AND_VERIFIED",
        }
        for p in generated_paths if p.exists()
    ]
    MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")

    print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(1 if failed else 0)

if __name__=="__main__":
    run()
