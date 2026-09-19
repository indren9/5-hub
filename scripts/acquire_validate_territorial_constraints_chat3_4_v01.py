"""Chat 3.4 - acquisizione e validazione tecnica dei vincoli territoriali/ambientali.
Non applica esclusioni, buffer, soglie o overlay ai candidati.
Output pesanti su OneDrive; manifest/QA riproducibili.
"""
from __future__ import annotations
import hashlib, json, re, sys, time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

RUN_DATE="20260919"
RAW=Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_4")
QA=Path(r"C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\05_intermediate_outputs\F3_CHAT_3_4")
FVG_WFS="https://serviziogc.regione.fvg.it/geoserver/wfs"
PPR_WFS="https://serviziogc.regione.fvg.it/geoserver/PPR/wfs"
SIGMA_WFS="https://sigma.distrettoalpiorientali.it/sigma/geo/sigma/wfs"
SIGMA_API="https://sigma.distrettoalpiorientali.it/sigma/pgra/"
UA="5-HUB-FVG Chat-3.4 reproducible-source-acquisition/1.0"
TIMEOUT=180
RAW.mkdir(parents=True,exist_ok=True); QA.mkdir(parents=True,exist_ok=True)
MANIFEST_PATH=RAW/"source_manifest_v01.json"
if MANIFEST_PATH.exists():
    try:
        _existing_manifest=json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        MANIFEST_GENERATED_UTC=_existing_manifest.get("generated_utc")
    except Exception:
        MANIFEST_GENERATED_UTC=None
else:
    MANIFEST_GENERATED_UTC=None
if not MANIFEST_GENERATED_UTC:
    MANIFEST_GENERATED_UTC=datetime.now(timezone.utc).isoformat()

def url(base, params=None):
    return base if not params else base+"?"+urlencode(params, doseq=True)

def fetch_bytes(target, params=None, method="GET", data=None, retries=3):
    full=url(target,params)
    payload=urlencode(data).encode() if data else None
    err=None
    for i in range(retries):
        try:
            req=Request(full,data=payload,headers={"User-Agent":UA})
            with urlopen(req,timeout=TIMEOUT) as r:
                return r.read(), dict(r.headers), r.geturl()
        except Exception as e:
            err=e
            if i+1<retries: time.sleep(2*(i+1))
    raise RuntimeError(f"fetch failed {full}: {err}")

def save_fetch(target, dest, params=None):
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists() and dest.stat().st_size>0:
        b=dest.read_bytes()
        return {"url":url(target,params),"path":str(dest),"bytes":len(b),
                "sha256":hashlib.sha256(b).hexdigest(),"content_type":None,
                "retrieved_utc":datetime.fromtimestamp(dest.stat().st_mtime,tz=timezone.utc).isoformat(),
                "reused_existing":True}
    b,h,final=fetch_bytes(target,params)
    dest.write_bytes(b)
    return {"url":final,"path":str(dest),"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),
            "content_type":h.get("Content-Type"),"retrieved_utc":datetime.now(timezone.utc).isoformat(),
            "reused_existing":False}

def wfs_params(layer, request="GetFeature", **extra):
    p={"service":"WFS","version":"1.1.0","request":request}
    if layer: p["typeName"]=layer
    p.update(extra); return p

def safe_name(layer):
    return layer.replace(":","__").replace("/","_")

manifest={"run_date":RUN_DATE,"generated_utc":MANIFEST_GENERATED_UTC,
          "purpose":"Chat 3.4 technical source validation; no methodological exclusion rules approved.",
          "artifacts":[],"layers":{},"findings":{}}

# 1) Endpoint evidence / capabilities
for label,base in [("FVG_WFS",FVG_WFS),("PPR_WFS",PPR_WFS),("SIGMA_WFS",SIGMA_WFS)]:
    rec=save_fetch(base,RAW/"capabilities"/f"{label}_GetCapabilities_{RUN_DATE}.xml",
                   {"service":"WFS","request":"GetCapabilities"})
    manifest["artifacts"].append(rec)

# 2) Regional landslide + protected-area vector snapshots
fvg_layers=[
 "IRDAT:CATFRANE_PERICOLOSITA","IRDAT:CATFRANE_PERIMFRANE",
 "SITI_PROT:SIC","SITI_PROT:ZPS","SITI_PROT:BIOTOPI",
 "SITI_PROT:PARCHI_NATURALI_REG","SITI_PROT:RISERVE_NATURALI_REG",
 "SITI_PROT:RIS_NATURALI_STATALI","SITI_PROT:PARCHI_COMUNALI_RAFVG",
 "SITI_PROT:PRATISTABILI"
]
for layer in fvg_layers:
    fn=RAW/"fvg_wfs"/f"{safe_name(layer)}_{RUN_DATE}.geojson"
    rec=save_fetch(FVG_WFS,fn,wfs_params(layer,outputFormat="application/json"))
    obj=json.loads(fn.read_text(encoding="utf-8"))
    feats=obj.get("features",[])
    props=[f.get("properties") or {} for f in feats]
    crs=((obj.get("crs") or {}).get("properties") or {}).get("name")
    geom=Counter((f.get("geometry") or {}).get("type","NULL") for f in feats)
    summary={"feature_count":len(feats),"crs":crs,"geometry_types":dict(geom),"artifact":rec}
    if layer=="IRDAT:CATFRANE_PERICOLOSITA":
        summary["class_counts"]=dict(Counter(str(p.get("PERICOLOSI")) for p in props))
    if layer in {"SITI_PROT:SIC","SITI_PROT:ZPS"}:
        summary["site_type_counts"]=dict(Counter(str(p.get("TIPO_SITO")) for p in props))
        summary["site_codes"]=sorted({str(p.get("CODICE_SITO")) for p in props if p.get("CODICE_SITO")})
    if layer=="SITI_PROT:BIOTOPI":
        summary["names"]=sorted(str(p.get("NOME")) for p in props if p.get("NOME"))
        summary["institution_bur"]=sorted({str(p.get("BUR_ISTITUZIONE")) for p in props if p.get("BUR_ISTITUZIONE")})
    if layer=="SITI_PROT:PRATISTABILI":
        summary["protected_flag_counts"]=dict(Counter(str(p.get("PRATO_TUTELATO")) for p in props))
        dates=[str(p.get("DATA_AGG")) for p in props if p.get("DATA_AGG")]
        summary["data_agg_minmax"]=[min(dates),max(dates)] if dates else None
    manifest["layers"][layer]=summary; manifest["artifacts"].append(rec)

# 3) Current PPR: statutory/relevant subset + update lineage layer
ppr_layers=[
 "PPR:v_aggiornamenti_ppr","PPR:v_paesaggi_delimitazione_art_136",
 "PPR:v_corsi_acqua_aree_tutelate","PPR:v_laghi_aree_tutelate",
 "PPR:v_fascia_rispetto_battigia_marittima","PPR:v_fascia_rispetto_battigia_lagunare",
 "PPR:v_ghiacciai","PPR:v_montagne_oltre_1600_m",
 "PPR:v_territori_coperti_da_foreste_e_boschi",
 "PPR:v_parchi_e_riserve_naturali_nazionali_o_regionali",
 "PPR:v_aree_umide","PPR:v_usi_civici","PPR:v_zone_interesse_archeologico",
 "PPR:v_ulteriori_contesti_archeologici",
 "PPR:v_uc_immobili_int_storico_artistico_architettonico",
 "PPR:v_ulteriori_contesti_immobili_decretati"
]
for layer in ppr_layers:
    nm=safe_name(layer)
    # Record schema for geometry/attribute semantics.
    schema_rec=save_fetch(PPR_WFS,RAW/"ppr_wfs"/f"{nm}_schema_{RUN_DATE}.xsd",
                          wfs_params(layer,"DescribeFeatureType"))
    manifest["artifacts"].append(schema_rec)
    # Count from WFS hits independently from materialized geometry.
    hits_rec=save_fetch(PPR_WFS,RAW/"ppr_wfs"/f"{nm}_hits_{RUN_DATE}.xml",
                        wfs_params(layer,resultType="hits"))
    manifest["artifacts"].append(hits_rec)
    txt=Path(hits_rec["path"]).read_text(encoding="utf-8",errors="replace")
    m=re.search(r'numberOfFeatures="([^"]+)"',txt)
    count=int(m.group(1)) if m and m.group(1).isdigit() else None
    if layer=="PPR:v_aggiornamenti_ppr":
        fn=RAW/"ppr_wfs"/f"{nm}_{RUN_DATE}.geojson"
        rec=save_fetch(PPR_WFS,fn,wfs_params(layer,outputFormat="application/json"))
        obj=json.loads(fn.read_text(encoding="utf-8")); feats=obj.get("features",[])
        props=[f.get("properties") or {} for f in feats]
        summary={"feature_count":len(feats),
                 "crs":((obj.get("crs") or {}).get("properties") or {}).get("name"),
                 "geometry_types":dict(Counter((f.get("geometry") or {}).get("type","NULL") for f in feats)),
                 "artifact":rec,
                 "variant_counts":dict(Counter(str(p.get("numero_variante")) for p in props)),
                 "variant2_2025_records":sum(1 for p in props if str(p.get("numero_variante"))=="2/2025"),
                 "variant2_2025_examples":[p for p in props if str(p.get("numero_variante"))=="2/2025"][:5]}
    else:
        get_params=wfs_params(layer,outputFormat="shape-zip")
        fn=RAW/"ppr_wfs"/f"{nm}_{RUN_DATE}.zip"
        rec=save_fetch(PPR_WFS,fn,get_params)
        summary={"feature_count":count,"crs":"EPSG:6708 (native PPR WFS; .prj included in archive)",
                 "geometry_available":True,"format":"ESRI Shapefile in ZIP",
                 "materialization_status":"MATERIALIZED",
                 "artifact":rec,"schema_artifact":schema_rec,"hits_artifact":hits_rec}
        manifest["artifacts"].append(rec)
    if layer=="PPR:v_aggiornamenti_ppr":
        summary["materialization_status"]="MATERIALIZED"
    manifest["layers"][layer]=summary

# 4) PGRA legal/current map-set evidence + live vector service snapshot
pgra_dir=RAW/"pgra_sigma"
for name,target,params in [
 ("PGRA_update_notice_20260122.html","https://sigma.distrettoalpiorientali.it/portal/index.php/2026/01/22/pgra_aggiornamento/",None),
 ("PGRA_set_catalog.json",SIGMA_API+"getSetCartografici",None),
 ("PGRA2027_map_index.json",SIGMA_API+"getPgra",{"setCartograficoId":40}),
 ("PGRA2027_sheet_index.geojson.json",SIGMA_API+"getPgraQuadroUnioneFeatures",{"setCartograficoId":40}),
]:
    rec=save_fetch(target,pgra_dir/f"{Path(name).stem}_{RUN_DATE}{Path(name).suffix}",params)
    manifest["artifacts"].append(rec)

setcat=json.loads((pgra_dir/f"PGRA_set_catalog_{RUN_DATE}.json").read_text(encoding="utf-8"))
sets=setcat.get("result") or []
manifest["findings"]["pgra_set_40"]=next((x for x in sets if x.get("id")==40),None)
idx=json.loads((pgra_dir/f"PGRA2027_map_index_{RUN_DATE}.json").read_text(encoding="utf-8")).get("result") or []
manifest["findings"]["pgra_map_index_count"]=len(idx)
manifest["findings"]["pgra_map_types"]=dict(Counter(str(x.get("nome")) for x in idx))

# Native SIGMA WFS hazard/risk: current live service snapshot, FVG envelope (not administrative clip)
cql="BBOX(the_geom,12.20,45.50,14.00,46.75,'EPSG:4326')"
for layer in ["sigma:Pericolo_direttiva_alluvioni","sigma:Rischio"]:
    nm=safe_name(layer)
    # schema
    rec=save_fetch(SIGMA_WFS,pgra_dir/f"{nm}_DescribeFeatureType_{RUN_DATE}.xsd",
                   wfs_params(layer,"DescribeFeatureType"))
    manifest["artifacts"].append(rec)
    # small semantic sample
    rec=save_fetch(SIGMA_WFS,pgra_dir/f"{nm}_sample100_{RUN_DATE}.geojson",
                   wfs_params(layer,outputFormat="application/json",maxFeatures=100,CQL_FILTER=cql))
    manifest["artifacts"].append(rec)
    # Count current live vector service over an FVG envelope; do not bulk-materialize before version binding is proven.
    hits_rec=save_fetch(SIGMA_WFS,pgra_dir/f"{nm}_FVG_ENVELOPE_hits_{RUN_DATE}.xml",
                        wfs_params(layer,resultType="hits",CQL_FILTER=cql))
    manifest["artifacts"].append(hits_rec)
    txt=Path(hits_rec["path"]).read_text(encoding="utf-8",errors="replace")
    m=re.search(r'numberOfFeatures="([^"]+)"',txt)
    cnt=int(m.group(1)) if m and m.group(1).isdigit() else None
    full_params=wfs_params(layer,outputFormat="shape-zip",CQL_FILTER=cql)
    manifest["layers"][layer]={"scope":"FVG geographic envelope; NOT clipped to administrative boundary",
        "filter":cql,"crs_native":"EPSG:3035","feature_count_envelope":cnt,
        "materialization_status":"SCHEMA_HITS_SAMPLE_ONLY_VERSION_BINDING_UNPROVEN",
        "reproducible_full_vector_url":url(SIGMA_WFS,full_params),
        "version_binding_note":"Live official SIGMA WFS; WFS schema/capabilities do not expose an explicit identifier binding these vectors to Delibera 12/2025. Bulk geometry is deliberately not promoted as current legal PGRA until that binding is proven."}

# 5) Two 2026 biotopes missing from live BIOTOPI WFS: preserve legal acts and cartographic annexes.
for num in ["065","066"]:
    remote_names={
        "TESTO_INTEGRALE":f"TESTO INTEGRALE DEL DPREG {num}-2026.PDF",
        "ALLEGATO2":f"ALLEGATO2 AL DPREG {num}-2026.PDF",
    }
    for label,remote_name in remote_names.items():
        remote=f"https://decreti.regione.fvg.it/Storage/2026_{int(num)}/{remote_name}".replace(" ","%20")
        dest=RAW/"protected_areas_legal"/f"DPReg_{num}_2026_{label}_{RUN_DATE}.pdf"
        rec=save_fetch(remote,dest)
        manifest["artifacts"].append(rec)

# 6) Current institutional pages as provenance snapshots
for name,source in [
 ("FVG_Natura2000_current","https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/tutela-ambiente-gestione-risorse-naturali/FOGLIA203/"),
 ("FVG_protected_areas_current","https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/tutela-ambiente-gestione-risorse-naturali/FOGLIA41/"),
 ("FVG_landslides_current","https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/geologia/FOGLIA20/"),
 ("FVG_PPR_current","https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/pianificazione-gestione-territorio/FOGLIA21"),
]:
    rec=save_fetch(source,RAW/"institutional_pages"/f"{name}_{RUN_DATE}.html")
    manifest["artifacts"].append(rec)

# 7) QA findings
bio=manifest["layers"]["SITI_PROT:BIOTOPI"]
manifest["findings"]["biotopi_wfs_count"]=bio["feature_count"]
manifest["findings"]["biotopi_missing_2026_names"]=[
    "Monte Joanaz","Prati di Spignon/Varh e Monte Craguenza/Kraguojnca"
]
manifest["findings"]["landslide_hazard_classes"]=manifest["layers"]["IRDAT:CATFRANE_PERICOLOSITA"]["class_counts"]
sic=set(manifest["layers"]["SITI_PROT:SIC"]["site_codes"]); zps=set(manifest["layers"]["SITI_PROT:ZPS"]["site_codes"])
manifest["findings"]["natura_unique_codes_wfs"]=len(sic|zps)
manifest["findings"]["natura_overlap_codes_wfs"]=len(sic&zps)
manifest["findings"]["ppr_variant2_2025_records"]=manifest["layers"]["PPR:v_aggiornamenti_ppr"]["variant2_2025_records"]
manifest["findings"]["license_regional_default"]="IODL 2.0 unless specific metadata states otherwise; verify per-layer metadata for exceptions."
manifest["findings"]["pgra_license"]="No reuse license asserted from WFS/map-download evidence captured here; treat as TO_VERIFY before redistribution."

# Manifest itself
mp=RAW/"source_manifest_v01.json"
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
manifest_hash=hashlib.sha256(mp.read_bytes()).hexdigest()
qa={"run_date":RUN_DATE,"manifest":str(mp),"manifest_sha256":manifest_hash,
    "checks":{
      "fvg_layers_materialized":all(x in manifest["layers"] for x in fvg_layers),
      "ppr_layers_materialized":all(manifest["layers"].get(x,{}).get("materialization_status")=="MATERIALIZED" for x in ppr_layers),
      "ppr_variant2_present":manifest["findings"]["ppr_variant2_2025_records"]>0,
      "landslide_classes_exact":set(manifest["findings"]["landslide_hazard_classes"])=={"P1","P2","P3","P4"},
      "biotope_wfs_gap_detected":manifest["findings"]["biotopi_wfs_count"]==40,
      "pgra_current_set_detected":(manifest["findings"]["pgra_set_40"] or {}).get("codice")=="PGRA2027",
      "pgra_live_vector_endpoints_validated":all(x in manifest["layers"] and manifest["layers"][x].get("feature_count_envelope") is not None for x in ["sigma:Pericolo_direttiva_alluvioni","sigma:Rischio"])
    },
    "residual_gaps":[
      "PGRA: live SIGMA WFS vectors lack explicit machine-readable version binding to Delibera 12/2025 / PGRA2027 map set; legal-current equivalence not asserted and bulk vector geometry not promoted.",
      "Biotopi: regional WFS exposes 40 geometries while current institutional total is 42; DPReg 065/2026 and 066/2026 legal/cartographic PDFs preserved, but updated vector geometry is not yet exposed by the checked WFS."
    ]}
qa["technical_checks_pass"]=all(qa["checks"].values())
qp=QA/"TERRITORIAL_CONSTRAINTS_QA_v01.json"
qp.write_text(json.dumps(qa,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"manifest":str(mp),"manifest_sha256":manifest_hash,"qa":str(qp),
                  "technical_checks_pass":qa["technical_checks_pass"],"checks":qa["checks"]},ensure_ascii=False,indent=2))
