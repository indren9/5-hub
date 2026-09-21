from __future__ import annotations
import csv, hashlib, json, re, unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import fitz

ROOT = Path(r"C:\dev\5-hub")
DOCS = ROOT / "docs"
OUT = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_12")
SRC = OUT / "official_sources"
QA = OUT / "qa"
BASE34 = Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_4\fvg_wfs")

A2 = SRC / "DGR30_2026_Allegato_A2_regione_alpina.pdf"
A3 = SRC / "DGR30_2026_Allegato_A3_regione_continentale.pdf"
SIC = BASE34 / "SITI_PROT__SIC_20260919.geojson"
ZPS = BASE34 / "SITI_PROT__ZPS_20260919.geojson"
RULESET = DOCS / "FASE_3_NATURA2000_RULESET_v01.csv"
CROSSWALK = DOCS / "FASE_3_NATURA2000_SITE_RULE_CROSSWALK_v01.csv"
MANIFEST = OUT / "source_manifest_v01.json"
QA_JSON = QA / "natura2000_prescreen_qa_v01.json"

GREEN = (0.655, 0.855, 0.306)
RED = (1.000, 0.761, 0.055)
YELLOW = (0.847, 0.847, 0.847)
PALETTE = {
    GREEN: ("PREASSESSED_NO_SIGNIFICANT_INCIDENCE", "CORRESPONDENCE_CHECK_REQUIRED", "POTENTIALLY_COVERED_BY_PREASSESSMENT"),
    RED: ("SCREENING_REQUIRED", "SPECIFIC_VINCA_SCREENING_REQUIRED", ""),
    YELLOW: ("NOT_APPLICABLE", "MANUAL_REVIEW_REQUIRED", ""),
}
ACTIVITY_RE = re.compile(r"^\s*(\d+\.\d+(?:\.[ab])?)\.?\s", re.I)
MEASURE_RE = re.compile(r"\bREP[A-Z]\d+(?:[\.,]\d+)?\b", re.I)

FIELDS = [
    "rule_id","rule_type","rule_priority","source_id","legal_basis","effective_date",
    "site_scope","site_code","project_or_activity_scope","activity_code","spatial_condition",
    "functional_interference_condition","required_conditions","correspondence_check_required",
    "source_outcome","intermediate_classification","model_action","limitations","evidence_reference",
    "measure_refs","source_page"
]

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+"," ",s).strip()

def clean(s: str, limit: int = 900) -> str:
    s = s.replace("\ufffd","").replace("\n"," ")
    s = re.sub(r"\s+"," ",s).strip()
    return s[:limit]

def load_sites():
    by_code = {}
    name_map = {}
    for kind, path in [("SIC",SIC),("ZPS",ZPS)]:
        data = json.loads(path.read_text(encoding="utf-8"))
        for f in data["features"]:
            p = f["properties"]
            code = p["CODICE_SITO"]
            rec = by_code.setdefault(code,{
                "site_code": code, "site_name": p["NOME"],
                "bioregion": p.get("REGIONE_BIOGEOGRAFICA",""),
                "sic_tipo": "", "zps_tipo": "", "in_sic": False, "in_zps": False
            })
            rec["site_name"] = p["NOME"] or rec["site_name"]
            rec["bioregion"] = p.get("REGIONE_BIOGEOGRAFICA") or rec["bioregion"]
            rec[f"in_{kind.lower()}"] = True
            rec[f"{kind.lower()}_tipo"] = p.get("TIPO_SITO","")
            name_map[norm(p["NOME"])] = code
    # One wording discrepancy between the current DGR30 PDF header and the validated WFS name.
    name_map[norm("Torbiera di Casasola e Andreuzza")] = "IT3320021"
    return by_code, name_map

def designation(rec):
    s = (rec["sic_tipo"] or "").lower()
    has_zps = rec["in_zps"]
    if "zsc" in s:
        return "ZSC+ZPS" if has_zps else "ZSC"
    if "psic" in s:
        return "pSIC+ZPS" if has_zps else "pSIC"
    if "sic" in s:
        return "SIC+ZPS" if has_zps else "SIC"
    if has_zps:
        return "ZPS"
    return "UNKNOWN"

def current_measure_basis(code, rec):
    if code == "IT3320037":
        return "DPReg 065/2025 Piano di gestione Laguna di Marano e Grado (in vigore dal 10/07/2025)"
    if code == "IT3341002":
        return "DGR 1760/2025 per ZPS IT3341002; verificare anche misure della componente ZSC ove applicabili"
    parts = []
    if rec["in_zps"]:
        parts.append("DGR 594/2025 per componente ZPS")
    if "zsc" in (rec["sic_tipo"] or "").lower():
        parts.append("DGR 1148/2024 o DGR 1149/2024 per componente ZSC secondo regione biogeografica")
    if not parts:
        parts.append("Verifica obbligatoria nel registro regionale corrente delle misure/piani del sito")
    return "; ".join(parts)

def parse_pdf(path: Path, annex: str, name_map: dict):
    doc = fitz.open(path)
    current_site = None
    current_code = None
    current_blocks = []
    rows = []
    canonical_scope = {}
    seen_keys = set()
    site_headers = {}

    for pi, page in enumerate(doc):
        blocks = page.get_text("blocks")
        lines = [x.strip() for x in page.get_text("text").splitlines() if x.strip()]
        if lines and lines[0].startswith("Prevalutazioni di incidenza") and len(lines) > 1:
            candidate = lines[1]
            n = norm(candidate)
            if n in name_map:
                if current_site and name_map[n] != current_site:
                    current_code = None
                    current_blocks = []
                current_site = name_map[n]
                site_headers[current_site] = candidate
        if not current_site:
            continue

        events = []
        for b in blocks:
            x0,y0,x1,y1,txt,*_ = b
            txtc = txt.strip()
            if not txtc:
                continue
            m = ACTIVITY_RE.match(txtc)
            events.append((y0,0,"text",txtc,m.group(1) if m else None))
        for dr in page.get_drawings():
            fill = dr.get("fill"); rect = dr.get("rect")
            if fill is None or rect is None:
                continue
            color = tuple(round(x,3) for x in fill)
            if color in PALETTE and rect.width > 400 and 10 <= rect.height <= 18:
                events.append((rect.y0,1,"bar",color,None))
        events.sort(key=lambda x:(x[0],x[1]))

        for _,_,typ,val,activity in events:
            if typ == "text":
                if activity:
                    current_code = activity
                    current_blocks = [val]
                    canonical_scope.setdefault(activity, clean(val, 1200))
                elif current_code:
                    current_blocks.append(val)
            else:
                if not current_code:
                    continue
                key = (current_site,current_code)
                if key in seen_keys:
                    continue
                source_outcome, model_action, intermediate = PALETTE[val]
                text_all = " ".join(current_blocks)
                measures = sorted({m.group(0).upper().replace(",",".") for m in MEASURE_RE.finditer(text_all)})
                evidence = clean(current_blocks[-1] if current_blocks else "", 650)
                scope = canonical_scope.get(current_code, clean(current_blocks[0] if current_blocks else current_code))
                rows.append({
                    "rule_id": f"DGR30_{annex}_{current_site}_{current_code.replace('.','_')}",
                    "rule_type": "SITE_ACTIVITY_PREASSESSMENT",
                    "rule_priority": "200",
                    "source_id": f"DGR30_2026_{annex}",
                    "legal_basis": "DGR 30/2026 Allegato A; DGR 1183/2022 Allegato A punto 4",
                    "effective_date": "2026-01-28",
                    "site_scope": current_site,
                    "site_code": current_site,
                    "project_or_activity_scope": scope,
                    "activity_code": current_code,
                    "spatial_condition": "Inside site, contiguous area, or applicable external functional-interference area; preassessment also valid in functional-interference areas",
                    "functional_interference_condition": "If external, determine scope from DGR30/2026 Allegato C or site-specific plan/measure override before use",
                    "required_conditions": "Exact correspondence with the preassessed P/I/A definition; comply with current conservation measures and any site-specific conditions; no automatic inference from generic similarity",
                    "correspondence_check_required": "YES" if source_outcome=="PREASSESSED_NO_SIGNIFICANT_INCIDENCE" else "NO",
                    "source_outcome": source_outcome,
                    "intermediate_classification": intermediate,
                    "model_action": model_action,
                    "limitations": "This is a procedural pre-screen rule, not a formal VINCA outcome. NOT_APPLICABLE never becomes automatic site exclusion.",
                    "evidence_reference": f"DGR30/2026 Allegato {annex}; site {current_site}; PDF page {pi+1}; activity {current_code}; site evidence: {evidence}",
                    "measure_refs": ";".join(measures),
                    "source_page": str(pi+1),
                })
                seen_keys.add(key)
                current_code = None
                current_blocks = []
    return rows, site_headers, canonical_scope

def scan_activity_pages(path: Path, name_map: dict):
    doc = fitz.open(path)
    current_site = None
    found = {}
    for pi, page in enumerate(doc):
        lines = [x.strip() for x in page.get_text("text").splitlines() if x.strip()]
        if lines and lines[0].startswith("Prevalutazioni di incidenza") and len(lines) > 1:
            n = norm(lines[1])
            if n in name_map:
                current_site = name_map[n]
        if not current_site:
            continue
        for b in page.get_text("blocks"):
            txt = b[4].strip()
            m = ACTIVITY_RE.match(txt)
            if m:
                found.setdefault((current_site,m.group(1)), pi+1)
    return found

def static_rules():
    rows = []
    def add(rule_id, rule_type, priority, source_id, legal_basis, site_scope, scope, spatial, functional, required, corr, outcome, action, limits, evidence):
        rows.append(dict(zip(FIELDS,[
            rule_id,rule_type,str(priority),source_id,legal_basis,"2026-01-28",site_scope,"",scope,"",
            spatial,functional,required,corr,outcome,"",action,limits,evidence,"",""
        ])))
    # Guardrails / correspondence
    add("N2K_GLOBAL_001","GLOBAL_GUARDRAIL",10,"DEC-0041+DGR30_2026_A1",
        "DEC-0041; DGR 30/2026 Allegato A.1","ALL","All P/P/P/I/A",
        "Any Natura 2000 relation","",
        "The model determines required depth only; never output a formal positive VINCA determination and never exclude solely for intersection/proximity",
        "CONDITIONAL","PROCEDURAL_GUARDRAIL","MANUAL_REVIEW_REQUIRED",
        "No scoring or penalty; no ecological assumption without source evidence","DEC-0041; DGR30/2026 A.1")
    add("N2K_CORR_001","CORRESPONDENCE_PROCEDURE",300,"DGR30_2026_A1","DGR 30/2026 Allegato A.1","ALL",
        "Permesso di costruire","N/A","N/A","Comune verifies and records correspondence in permit; information transmitted to Servizio biodiversita",
        "YES","CORRESPONDENCE_AUTHORITY_DEFINED","CORRESPONDENCE_CHECK_REQUIRED","Only after a green source outcome; authority/procedure must match actual case","A.1 p.4")
    add("N2K_CORR_002","CORRESPONDENCE_PROCEDURE",300,"DGR30_2026_A1","DGR 30/2026 Allegato A.1","ALL",
        "SCIA/CILA","N/A","N/A","Professional attestation; municipality performs sample controls",
        "YES","CORRESPONDENCE_AUTHORITY_DEFINED","CORRESPONDENCE_CHECK_REQUIRED","Only after a green source outcome","A.1 p.4")
    add("N2K_CORR_003","CORRESPONDENCE_PROCEDURE",300,"DGR30_2026_A1","DGR 30/2026 Allegato A.1","ALL",
        "Edilizia libera","N/A","N/A","Proponent verifies correspondence",
        "YES","CORRESPONDENCE_AUTHORITY_DEFINED","CORRESPONDENCE_CHECK_REQUIRED","Only after a green source outcome","A.1 p.4")
    add("N2K_CORR_004","CORRESPONDENCE_PROCEDURE",300,"DGR30_2026_A1","DGR 30/2026 Allegato A.1","ALL",
        "Conferenza di servizi","N/A","N/A","Entity responsible for urban-planning conformity verifies correspondence",
        "YES","CORRESPONDENCE_AUTHORITY_DEFINED","CORRESPONDENCE_CHECK_REQUIRED","Only after a green source outcome","A.1 p.4")
    add("N2K_CORR_005","CORRESPONDENCE_PROCEDURE",300,"DGR30_2026_A1","DGR 30/2026 Allegato A.1","ALL",
        "Forestry declarations/schemes/PRFA","N/A","N/A","Competent regional forestry service verifies correspondence",
        "YES","CORRESPONDENCE_AUTHORITY_DEFINED","CORRESPONDENCE_CHECK_REQUIRED","Only after a green source outcome","A.1 p.4")
    add("N2K_CORR_006","CORRESPONDENCE_PROCEDURE",300,"DGR30_2026_A1","DGR 30/2026 Allegato A.1","ALL",
        "Other public authorization","N/A","N/A","Authorizing entity verifies correspondence",
        "YES","CORRESPONDENCE_AUTHORITY_DEFINED","CORRESPONDENCE_CHECK_REQUIRED","Only after a green source outcome","A.1 p.4")
    add("N2K_CORR_007","CORRESPONDENCE_PROCEDURE",300,"DGR30_2026_A1","DGR 30/2026 Allegato A.1","ALL",
        "No authorization/administrative procedure","N/A","N/A","Proponent verifies correspondence",
        "YES","CORRESPONDENCE_AUTHORITY_DEFINED","CORRESPONDENCE_CHECK_REQUIRED","Only after a green source outcome","A.1 p.4")
    add("N2K_CORR_008","CORRESPONDENCE_INFERENCE",250,"DGR30_2026_A1","DGR 30/2026 Allegato A.1","ALL",
        "P/I/A of lower dimensional or typological magnitude than a preassessed item","N/A","N/A",
        "Use only if lower dimensional/typological correspondence is demonstrable from explicit project data; free-text similarity alone is insufficient",
        "YES","LOWER_ORDER_CORRESPONDENCE_ALLOWED_BY_SOURCE","MANUAL_REVIEW_REQUIRED",
        "No automatic semantic inference in the 5 HUB model unless explicit comparable attributes exist","A.1 p.3")

    # DGR30 Annex C general functional interference
    generic = [
        ("N2K_IF_001","ZSC_OR_ZPS_EXCEPT_IT3320037","Major project subject to VIA screening/VIA, generic","radius <= 1000 m from ZSC or ZPS","Major/minor classification proven under D.Lgs. 152/2006", "C p.3 / summary p.6"),
        ("N2K_IF_002","ZSC_OR_ZPS_EXCEPT_IT3320037","Major ski slope/lift meeting Annex C thresholds","radius <= 2000 m from ZSC or ZPS","Thresholds in Annex C p.3 must all be evaluated", "C p.3 / summary p.6"),
        ("N2K_IF_003","ZPS_EXCEPT_IT3320037","Major overhead electric line >100 kV and route >3 km","radius <= 2000 m from ZPS","Both voltage and length thresholds must be proven", "C p.3 / summary p.6"),
        ("N2K_IF_004","ZPS_EXCEPT_IT3320037","Airport or airstrip","radius <= 2000 m from ZPS","Project category must be proven", "C p.3 / summary p.6"),
        ("N2K_IF_005","ZPS_EXCEPT_IT3320037","Industrial wind >1 MW on land or offshore wind","radius <= 5000 m from ZPS","Project category/power must be proven", "C p.3 / summary p.6"),
        ("N2K_IF_006","ZSC_OR_ZPS_EXCEPT_IT3320037","Hydrocarbon prospecting/research/extraction land or sea","radius <= 3000 m from ZSC or ZPS","Project category must be proven", "C p.3 / summary p.6"),
        ("N2K_IF_007","ZSC_OR_ZPS_EXCEPT_IT3320037","Minor project, generic","radius <= 300 m from ZSC or ZPS","Minor-project classification must be proven; urban-zone exception requires proof of prior VINCA", "C p.4"),
        ("N2K_IF_008","ZSC_OR_ZPS_EXCEPT_IT3320037","Other intervention/activity, generic","radius <= 50 m from ZSC or ZPS","Urban-zone exception requires proof of prior VINCA", "C p.5"),
        ("N2K_IF_009","ZSC_OR_ZPS_EXCEPT_IT3320037","Specified motor/sport/flight manifestations","radius <= 300 m from ZSC or ZPS","Dedicated-structure exception must be verified", "C p.5"),
        ("N2K_IF_010","IT3341002;IT3340006;SAPPADA_SPECIAL_CONTEXT","Carso/Sappada minor projects/interventions/activities","radius <= 50 m","Applies only to special Carso/Sappada context in Annex C point 6; urban-zone exception requires proof", "C p.6.1"),
        ("N2K_IF_011","IT3341002;IT3340006;SAPPADA_SPECIAL_CONTEXT","Carso/Sappada new permanent extraurban/forest roads, pond/stagnant-water alteration, hydraulic reclamation of natural wetland","radius <= 300 m","Exact special category and Carso/Sappada context must be proven", "C p.6.2"),
        ("N2K_IF_012","FLUVIAL_WET_COASTAL_CONTEXT_EXCEPT_IT3320037","Project affecting water regime or watercourse morphology, excluding maintenance of pre-existing works","within 1 km upstream/downstream of affected Natura 2000 site along watercourse","Hydrological relation must be established; not Euclidean proxy", "C p.7.1"),
        ("N2K_IF_013","IT3310005;IT3320021;IT3320022;IT3310010;IT3320026;IT3320027;IT3320028;IT3320031;IT3320032;IT3330001;IT3310011;IT3310012;IT3320033;IT3320034;IT3320035","Groundwater derivation for the 15 sites listed in Annex C","radius <= 300 m from listed site boundary","Site code must be in explicit Annex C point 7.2 list", "C p.7.2 / summary p.6"),
        ("N2K_IF_014","MARINE_COASTAL_CONTEXT_EXCEPT_IT3320037","Marine/coastal project categories listed in Annex C","radius <= 1000 m from ZSC or ZPS","Project category must be proven", "C p.7.3"),
        ("N2K_IF_015","ZSC_CONNECTED_BY_RER_EXCEPT_IT3320037","Minor project in PPR/RER connectivity component affecting or connecting >=2 ZSC","distance < 2500 m from at least two ZSC","Requires official RER component and >=2-ZSC relationship; no proximity-only proxy", "C p.8"),
    ]
    for rid,site_scope,scope,spatial,required,evidence in generic:
        add(rid,"FUNCTIONAL_INTERFERENCE",100,"DGR30_2026_C","DGR 30/2026 Allegato C",site_scope,
            scope,spatial,"Trigger determines external functional-interference scope",
            required,"NO","FUNCTIONAL_INTERFERENCE_TRIGGER","SPECIFIC_VINCA_SCREENING_REQUIRED",
            "This action is terminal only if no applicable green preassessment covers the same P/I/A after correspondence and conservation-measure checks; VIA/VAS may trigger assessment beyond listed distances",evidence)

    # Halving rule is deliberately conditional, never automatic.
    add("N2K_IF_016","FUNCTIONAL_INTERFERENCE_CONDITIONAL_REDUCTION",90,"DGR30_2026_C","DGR 30/2026 Allegato C point 2.2","ALL_EXCEPT_IT3320037",
        "Potential halving of an otherwise applicable external-interference distance",
        "Only where the adjacent site portion is proven, within 300 m from site perimeter, to lack EU-interest habitat and mapped fauna-interest areas and is outside park/reserve/MPA/biotope",
        "Conditional modification of another distance",
        "All source conditions must be verified from authoritative habitat/fauna/protected-area data; UNKNOWN => no halving",
        "NO","CONDITIONAL_DISTANCE_REDUCTION","MANUAL_REVIEW_REQUIRED",
        "Never halve from missing data or simple map impression","C p.2.2")

    # Site-specific Laguna override.
    lag = [
        ("N2K_LAG_001","VIA/screening-VIA project not in level-II list","radius <= 1000 m","Level-I screening"),
        ("N2K_LAG_002","Overhead electric transmission line","radius <= 3000 m","Level-I screening"),
        ("N2K_LAG_003","Wind plant on land or sea","radius <= 10000 m","Level-I screening"),
        ("N2K_LAG_004","Hydrocarbon drilling for research/extraction","radius <= 20000 m","Level-I screening"),
        ("N2K_LAG_005","P/I/A modifying/altering/discharging/withdrawing in listed lagoon-basin ecological-corridor watercourses","Official corridor: Stella, Turgnano, Cormor, Zellina, Corno, Ausa, Natissa, Zemole from lagoon shoreline to SR14 intersection","Level-I screening"),
        ("N2K_LAG_006","Any intervention on external sandbanks/perilagoon beaches","Official barrier-island / perilagoon-sand system from plan cartography","Level-I screening"),
        ("N2K_LAG_007","Other P/P/P/I/A","radius <= 300 m","Level-I screening; urban-zone and event exceptions require exact source proof"),
        ("N2K_LAG_008","Listed industrial/logistic/urban/coastal/electric/waste/water etc. project in 300 m buffer","radius <= 300 m","Level-II appropriate assessment according to plan list"),
        ("N2K_LAG_009","New external port/tourist landing or expansion >10 berths","Site-specific areas/measures; >10 berths","Level-II appropriate assessment"),
    ]
    for rid,scope,spatial,outcome in lag:
        action = "SPECIFIC_VINCA_SCREENING_REQUIRED" if "Level-I" in outcome else "MANUAL_REVIEW_REQUIRED"
        add(rid,"SITE_SPECIFIC_FUNCTIONAL_INTERFERENCE",80,"DPREG65_2025_ANNEX14",
            "DPReg 065/2025 Piano di gestione IT3320037, Allegato 14","IT3320037",scope,spatial,
            "Overrides generic DGR30/2026 Annex C where site plan is more specific",
            "Use official plan cartography/criteria and exact project category", "NO", outcome.upper().replace("-","_").replace(" ","_"), action,
            "Level-II source requirement is recorded as MANUAL_REVIEW_REQUIRED because the 5 HUB pre-screen does not simulate formal VINCA level-II decisions","Annex 14 pp.3-5")

    return rows

def build():
    OUT.mkdir(parents=True, exist_ok=True); QA.mkdir(parents=True, exist_ok=True)
    by_code,name_map = load_sites()
    r2,h2,c2 = parse_pdf(A2,"A2",name_map)
    r3,h3,c3 = parse_pdf(A3,"A3",name_map)
    pre = r2+r3

    # Explicitly preserve source gaps instead of guessing a color/outcome.
    catalog = sorted(set(c2) | set(c3))
    present = {(r["site_code"],r["activity_code"]) for r in pre}
    page_map = scan_activity_pages(A2,name_map)
    page_map.update(scan_activity_pages(A3,name_map))
    for code in sorted(by_code):
        annex = "A2" if code in h2 else ("A3" if code in h3 else "")
        scopes = c2 if annex=="A2" else c3
        for activity in catalog:
            if (code,activity) in present:
                continue
            pg = page_map.get((code,activity),"")
            pre.append({
                "rule_id":f"DGR30_{annex}_{code}_{activity.replace('.','_')}_UNKNOWN",
                "rule_type":"SITE_ACTIVITY_PREASSESSMENT","rule_priority":"200",
                "source_id":f"DGR30_2026_{annex}","legal_basis":"DGR 30/2026 Allegato A; DGR 1183/2022 Allegato A punto 4",
                "effective_date":"2026-01-28","site_scope":code,"site_code":code,
                "project_or_activity_scope":scopes.get(activity,activity),"activity_code":activity,
                "spatial_condition":"Inside site, contiguous area, or applicable external functional-interference area",
                "functional_interference_condition":"If external, determine scope from DGR30/2026 Allegato C or site-specific plan/measure override before use",
                "required_conditions":"Source cell/outcome could not be deterministically recovered; no assumption allowed",
                "correspondence_check_required":"UNKNOWN","source_outcome":"UNKNOWN","intermediate_classification":"",
                "model_action":"NOT_DETERMINABLE_FROM_AVAILABLE_RULES",
                "limitations":"Explicit source-structure gap. Requires manual review of the cited DGR30 annex cell; no inferred outcome.",
                "evidence_reference":f"DGR30/2026 Allegato {annex}; site {code}; activity {activity}; PDF page {pg or 'not-resolved'}; no status bar detected between this activity and the next activity",
                "measure_refs":"","source_page":str(pg)
            })
    rows = static_rules()+pre

    with RULESET.open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(rows)

    by_site = defaultdict(list)
    for r in pre: by_site[r["site_code"]].append(r)
    cw_fields = [
        "site_code","site_name","biogeographic_region","current_designation","sic_layer_presence","zps_layer_presence",
        "sic_tipo_sito_raw","zps_tipo_sito_raw","dgr30_preassessment_annex","dgr30_site_header",
        "preassessment_activity_count","preassessed_green_count","screening_required_red_count","not_applicable_yellow_count","unknown_count",
        "current_conservation_basis","current_measure_check_required","functional_interference_basis","site_specific_override",
        "crosswalk_method","geometry_source","geometry_sha256_sic","geometry_sha256_zps","limitations"
    ]
    cross=[]
    for code in sorted(by_code):
        rec=by_code[code]; rr=by_site.get(code,[])
        counts=Counter(x["source_outcome"] for x in rr)
        annex = "A2" if code in h2 else ("A3" if code in h3 else "")
        special=""
        if code=="IT3320037": special="DPReg 065/2025 Annex 14 controls external functional-interference criteria for this site"
        if code=="IT3341002": special="DGR 1760/2025 is the current ZPS conservation-measure update"
        cross.append({
            "site_code":code,"site_name":rec["site_name"],"biogeographic_region":rec["bioregion"],
            "current_designation":designation(rec),"sic_layer_presence":"YES" if rec["in_sic"] else "NO",
            "zps_layer_presence":"YES" if rec["in_zps"] else "NO","sic_tipo_sito_raw":rec["sic_tipo"],"zps_tipo_sito_raw":rec["zps_tipo"],
            "dgr30_preassessment_annex":annex,"dgr30_site_header":h2.get(code,h3.get(code,"")),
            "preassessment_activity_count":len(rr),"preassessed_green_count":counts["PREASSESSED_NO_SIGNIFICANT_INCIDENCE"],
            "screening_required_red_count":counts["SCREENING_REQUIRED"],"not_applicable_yellow_count":counts["NOT_APPLICABLE"],
            "unknown_count":counts["UNKNOWN"],"current_conservation_basis":current_measure_basis(code,rec),
            "current_measure_check_required":"YES","functional_interference_basis":"DPReg 065/2025 Annex 14" if code=="IT3320037" else "DGR 30/2026 Allegato C",
            "site_specific_override":special,
            "crosswalk_method":"Validated Chat 3.4 site code/name + DGR30 A2/A3 site header normalized-name match; explicit alias only for Torbiera/Torbiere di Casasola e Andreuzza",
            "geometry_source":"Chat 3.4 validated WFS snapshot 2026-09-19; geometry not recreated",
            "geometry_sha256_sic":"772dabc52d720eaedfc5bd8de6649d2be915c01a88d2686d553137e3ebaa2e06" if rec["in_sic"] else "",
            "geometry_sha256_zps":"949724e039aac197490c80e0ebbdfb6fbb46bf2a12f3b457e3989af0bc032660" if rec["in_zps"] else "",
            "limitations":"Crosswalk establishes rule applicability lineage, not a formal VINCA determination."
        })
    with CROSSWALK.open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=cw_fields); w.writeheader(); w.writerows(cross)

    source_urls = {
        "DGR30_2026_testo_integrale.pdf":"https://mtom.regione.fvg.it/storage/2026_30/Testo%20integrale%20della%20Delibera%20n%2030-2026.pdf",
        "DGR30_2026_Allegato_A1_criteri_verifica_corrispondenza.pdf":"https://www.regione.fvg.it/rafvg/export/sites/default/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/FOGLIA02/allegati/Prevalutazioni_criteri_e_ver_corr.pdf",
        "DGR30_2026_Allegato_A2_regione_alpina.pdf":"https://www.regione.fvg.it/rafvg/export/sites/default/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/FOGLIA02/allegati/Prevalutazioni_regione_alpina_gen.pdf",
        "DGR30_2026_Allegato_A3_regione_continentale.pdf":"https://www.regione.fvg.it/rafvg/export/sites/default/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/FOGLIA02/allegati/Prevalutazioni_regione_continentale_gen.pdf",
        "DGR30_2026_Allegato_B_osservazioni.pdf":"https://bur.regione.fvg.it/newbur/downloadPDF?doc=0&name=2026%2F01%2F28%2F26_SO5_1_DGR_30_3_ALL2.pdf",
        "DGR30_2026_Allegato_C_interferenza_funzionale.pdf":"https://mtom.regione.fvg.it/storage/2026_30/Allegato%203%20alla%20Delibera%2030-2026.pdf",
        "DPReg65_2025_Allegato14_Laguna_interferenza.pdf":"https://bur.regione.fvg.it/newbur/downloadPDF?doc=0&name=2025%2F07%2F09%2F25_SO15_1_DPR_65_15_ALL14.pdf",
        "DGR1183_2022_Allegato_A.pdf":"https://www.regione.fvg.it/rafvg/export/sites/default/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/allegati/DGR_1183_2022_TABELLA_ALLEGATO_A.pdf",
        "DGR1183_2022_CON_ALLEGATI.pdf":"https://www.regione.fvg.it/rafvg/export/sites/default/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/allegati/DGR_1183_2022_CON_ALLEGATI.pdf",
        "Decreto72016_2025_Condizioni_obbligo.pdf":"https://www.regione.fvg.it/rafvg/export/sites/default/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/FOGLIA03/allegati/Decreto_adozione_Condizioni_obbligo_.pdf",
        "Decreto72016_2025_Allegato1_Condizioni_obbligo.pdf":"https://www.regione.fvg.it/rafvg/export/sites/default/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/FOGLIA03/allegati/Allegato_1_-_Condizioni_obbligo_per_screening_valutazione_incidenza_.pdf",
    }
    artifacts=[]
    for fn,url in source_urls.items():
        p=SRC/fn
        if p.exists():
            artifacts.append({"source_id":fn.rsplit(".",1)[0],"url":url,"path":str(p),"bytes":p.stat().st_size,"sha256":sha256(p),"retrieved_or_verified_date":"2026-09-21"})
        else:
            artifacts.append({"source_id":fn.rsplit(".",1)[0],"url":url,"path":str(p),"status":"MISSING"})
    artifacts += [
        {"source_id":"CHAT3_4_SIC_WFS","path":str(SIC),"sha256":sha256(SIC),"status":"REUSED_FROZEN_VALIDATED_SOURCE"},
        {"source_id":"CHAT3_4_ZPS_WFS","path":str(ZPS),"sha256":sha256(ZPS),"status":"REUSED_FROZEN_VALIDATED_SOURCE"},
        {"source_id":"FVG_NATURA_CURRENT_PAGE","url":"https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/tutela-ambiente-gestione-risorse-naturali/FOGLIA203/","verified_date":"2026-09-21","materialized":False},
        {"source_id":"FVG_DGR30_PREASSESSMENT_PAGE","url":"https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/FOGLIA02/","verified_date":"2026-09-21","materialized":False},
        {"source_id":"FVG_FUNCTIONAL_INTERFERENCE_PAGE","url":"https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/FOGLIA01/","verified_date":"2026-09-21","materialized":False},
        {"source_id":"FVG_VINCA_CURRENT_PAGE","url":"https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/","verified_date":"2026-09-21","materialized":False},
        {"source_id":"FVG_VINCA_FORMS_PAGE","url":"https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/modulistica/modulistica.html","verified_date":"2026-09-21","materialized":False},
        {"source_id":"FVG_SCREENING_CONDITIONS_PAGE","url":"https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/valutazione-ambientale-autorizzazioni-contributi/FOGLIA5/FOGLIA03/","verified_date":"2026-09-21","materialized":False},
    ]
    manifest={
        "generated_utc":datetime.now(timezone.utc).isoformat(),
        "purpose":"Chat 3.12 Natura 2000 operational pre-screen corpus and lineage",
        "as_of_date":"2026-09-21",
        "artifacts":artifacts,
        "notes":[
            "DGR30/2026 Annex B is retained as provenance/context but does not generate executable rules.",
            "No new Natura 2000 site geometries were created; Chat 3.4 validated WFS geometry is reused by hash.",
            "No standalone machine-readable official functional-interference geometry was identified in the reviewed DGR30 corpus; some criteria depend on official PPR/RER, watercourse, habitat/fauna, urban-zoning or Laguna plan cartography inputs."
        ]
    }
    MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")

    qa = {
        "as_of_date":"2026-09-21",
        "site_count_geometry_union":len(by_code),
        "site_count_a2":len(h2),"site_count_a3":len(h3),"site_count_preassessment_union":len(by_site),
        "activity_rows":len(pre),"ruleset_total_rows":len(rows),
        "activities_per_site_min":min(map(len,by_site.values())) if by_site else 0,
        "activities_per_site_max":max(map(len,by_site.values())) if by_site else 0,
        "source_outcome_counts":dict(Counter(r["source_outcome"] for r in pre)),
        "unmatched_geometry_sites":sorted(set(by_code)-set(by_site)),
        "unknown_source_outcome_rows":sum(1 for r in pre if r["source_outcome"] not in {"PREASSESSED_NO_SIGNIFICANT_INCIDENCE","SCREENING_REQUIRED","NOT_APPLICABLE"}),
        "palette_validation":{
            "GREEN":"validated as source green/preassessed",
            "RED_ORANGE":"validated using IT3330005 activity 1.02, whose text explicitly says screening remains required",
            "YELLOW_GRAY":"validated using IT3340007 activity 1.01, whose text says intervention not applicable because marine site"
        }
    }
    QA_JSON.write_text(json.dumps(qa,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(qa,ensure_ascii=False,indent=2))

if __name__ == "__main__":
    build()
