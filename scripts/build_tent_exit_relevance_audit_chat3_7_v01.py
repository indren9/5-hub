from __future__ import annotations
import csv, hashlib, json
from pathlib import Path

ROOT=Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG")
OUT=ROOT/r"05_intermediate_outputs\F3_CHAT_3_7"
SRC=ROOT/r"02_external_sources\F3_CHAT_3_7"

rows=[
{
"audit_id":"EXITREL-FVG-001","tent_level":"CORE","fvg_route":"A4",
"tent_sections":"OID 999 Palmanova–Sistiana; OID 370 Palmanova–Portogruaro",
"morphology":"CONTROLLED_ACCESS_GRADE_SEPARATED","ordinary_at_grade_intersections_observed":"NO",
"true_exit_ramp_present":"YES","afir_nearest_exit_interpretation_material":"NO",
"normative_source":"TENtec TENT_Regulation_2024 Roads/Core; TENtec TYPE=Motorways",
"operator_source":"Autostrade Alto Adriatico current network/interchange list",
"topology_support":"Prior Chat 3.7 screening: Bretella di Latisana node resolved through link/ramp structure, not ordinary mainline at-grade intersection",
"evidence_notes":"Current TEN-T classification plus motorway operator evidence identifies access through motorway interchanges.",
"validation_status":"VERIFIED_NO_MATERIAL_EXIT_AMBIGUITY"},
{
"audit_id":"EXITREL-FVG-002","tent_level":"CORE","fvg_route":"A23",
"tent_sections":"OID 3632 Palmanova–Udine; OID 4550 Udine–Tarvisio; OID 3640 Tarvisio–AT border",
"morphology":"CONTROLLED_ACCESS_GRADE_SEPARATED","ordinary_at_grade_intersections_observed":"NO",
"true_exit_ramp_present":"YES","afir_nearest_exit_interpretation_material":"NO",
"normative_source":"TENtec TENT_Regulation_2024 Roads/Core; TENtec TYPE=Motorways",
"operator_source":"Autostrade Alto Adriatico / Autostrade per l'Italia current motorway/exit evidence",
"topology_support":"Prior screening found no suspicious ordinary at-grade direct connections.",
"evidence_notes":"Entire FVG TEN-T A23 is motorway; accesses are motorway exits/interchanges.",
"validation_status":"VERIFIED_NO_MATERIAL_EXIT_AMBIGUITY"},
{
"audit_id":"EXITREL-FVG-003","tent_level":"CORE","fvg_route":"RA13",
"tent_sections":"OID 2416 Sistiana–Villa Opicina; OID 472 Villa Opicina–Padriciano",
"morphology":"GRADE_SEPARATED_RAMP_INTERCHANGES","ordinary_at_grade_intersections_observed":"NO",
"true_exit_ramp_present":"YES","afir_nearest_exit_interpretation_material":"NO",
"normative_source":"TENtec TENT_Regulation_2024 Roads/Core; TENtec TYPE=Rural road with separate directions",
"operator_source":"ANAS official FVG road-rescue regulation identifies RA13 between named svincoli and as motorway/interconnected motorway section",
"topology_support":"Frozen OSM support screening found no ordinary at-grade direct connection on RA13.",
"evidence_notes":"No evidence of a TEN-T mainline segment whose usable connection must be interpreted as an ordinary at-grade intersection.",
"validation_status":"VERIFIED_NO_MATERIAL_EXIT_AMBIGUITY"},
{
"audit_id":"EXITREL-FVG-004","tent_level":"CORE","fvg_route":"RA14",
"tent_sections":"OID 4504 Fernetti–Villa Opicina",
"morphology":"GRADE_SEPARATED_RAMP_INTERCHANGES","ordinary_at_grade_intersections_observed":"NO",
"true_exit_ramp_present":"YES","afir_nearest_exit_interpretation_material":"NO",
"normative_source":"TENtec TENT_Regulation_2024 Roads/Core; TENtec TYPE=Rural road with separate directions",
"operator_source":"ANAS official FVG road-rescue regulation identifies RA14 between innesto RA13 and Fernetti and treats it as motorway/interconnected motorway section",
"topology_support":"Frozen OSM support screening found no ordinary at-grade direct connection on RA14.",
"evidence_notes":"Access morphology is consistent with genuine interchange/ramp access.",
"validation_status":"VERIFIED_NO_MATERIAL_EXIT_AMBIGUITY"},
{
"audit_id":"EXITREL-FVG-005","tent_level":"CORE","fvg_route":"A/SS202",
"tent_sections":"OID 862 Rabuiese–Padriciano (Trieste porto R13)",
"morphology":"GRADE_SEPARATED_RAMP_INTERCHANGES","ordinary_at_grade_intersections_observed":"NO",
"true_exit_ramp_present":"YES","afir_nearest_exit_interpretation_material":"NO",
"normative_source":"TENtec TENT_Regulation_2024 Roads/Core; TENtec TYPE=Rural road with separate directions",
"operator_source":"ANAS official FVG road-rescue regulation describes SS202/A sections by named svincoli and motorway/interconnected-motorway context",
"topology_support":"Frozen OSM support screening: Nuova Sopraelevata/Via della Rampa connection represented through link/ramp structure, not ordinary at-grade mainline intersection.",
"evidence_notes":"No ordinary at-grade TEN-T access case was identified on the Trieste axis.",
"validation_status":"VERIFIED_NO_MATERIAL_EXIT_AMBIGUITY"},
{
"audit_id":"EXITREL-FVG-006","tent_level":"COMPREHENSIVE","fvg_route":"A28",
"tent_sections":"OID 1508 Conegliano–Schiavoi (FVG overlap); OID 2725 Schiavoi–Portogruaro (FVG overlap)",
"morphology":"CONTROLLED_ACCESS_GRADE_SEPARATED","ordinary_at_grade_intersections_observed":"NO",
"true_exit_ramp_present":"YES","afir_nearest_exit_interpretation_material":"NO",
"normative_source":"TENtec TENT_Regulation_2024 Roads/Comprehensive; OID1508 TYPE=Motorways; same national route A28 for OID2725",
"operator_source":"Autostrade Alto Adriatico current network identifies A28 Portogruaro–Conegliano and lists its motorway interchanges",
"topology_support":"Not needed to infer TEN-T class; operator evidence independently establishes motorway/interchange morphology.",
"evidence_notes":"A28 is the only comprehensive-only FVG route identified by the complete current crosswalk and does not create an at-grade exit ambiguity.",
"validation_status":"VERIFIED_NO_MATERIAL_EXIT_AMBIGUITY"},
{
"audit_id":"EXITREL-FVG-007","tent_level":"EXTENDED_CORE","fvg_route":"NONE",
"tent_sections":"No current TENT_Regulation_2024 Roads/Extended Core feature materially overlaps FVG",
"morphology":"N/A","ordinary_at_grade_intersections_observed":"N/A",
"true_exit_ramp_present":"N/A","afir_nearest_exit_interpretation_material":"NO_SEGMENT",
"normative_source":"TENtec TENT_Regulation_2024 Roads/Extended Core layer 9; FVG query returned empty feature set",
"operator_source":"N/A","topology_support":"N/A",
"evidence_notes":"No extended-core FVG road segment exists in the queried current official dataset, so no morphology case arises.",
"validation_status":"VERIFIED_ABSENCE_IN_CURRENT_FVG_CROSSWALK"}
]

OUT.mkdir(parents=True,exist_ok=True)
p=OUT/"TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv"
with p.open("w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""): h.update(b)
    return h.hexdigest().upper()

manifest={"scope":"Chat 3.7 TEN-T FVG crosswalk and exit relevance evidence","files":{}}
for base in [SRC,OUT]:
    if base.exists():
        for q in sorted(base.rglob("*")):
            if q.is_file():
                manifest["files"][str(q.relative_to(ROOT))]={"bytes":q.stat().st_size,"sha256":sha(q)}
mp=SRC/"evidence_manifest_v01.json"
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
print(p)
print("audit_sha256",sha(p))
print("manifest_sha256",sha(mp))
print("rows",len(rows))
