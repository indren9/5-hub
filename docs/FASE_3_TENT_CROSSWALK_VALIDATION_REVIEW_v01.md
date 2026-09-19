# FASE 3 — TEN-T FVG CROSSWALK VALIDATION REVIEW v01

**Chat:** 3.7 — Crosswalk TEN-T FVG e rilevanza delle uscite AFIR
**Review correction date:** 2026-09-19
**Stato:** REWORK COMPLETED — READY FOR NEW CHAT MADRE REVIEW
**Regia metodologica:** Chat Madre 5 HUB
**Branch:** `chat-3.7-tent-crosswalk`

## 1. Scopo del rework

La review indipendente della Chat Madre ha confermato come sostanzialmente coerente il contenuto geografico e normativo, ma ha respinto il precedente PASS tecnico-operativo per difetti di riproducibilità degli artifact.

Il rework interviene esclusivamente su:
- unicità dei writer;
- separazione fra diagnostica automatica OSM e audit validato;
- ordine deterministico di produzione;
- rigenerazione finale di manifest e QA;
- correzione dei conteggi del crosswalk;
- allineamento di path e hash;
- chiarezza della lineage probatoria.

Non sono state riaperte FASE 1 o FASE 2. Non sono stati creati candidati, distanze candidato–TEN-T o `TENT_EXIT_SET_v01`. Nessuna decisione metodologica è stata chiusa.

## 2. Correzione dell'architettura degli artifact

La precedente collisione fra due writer dello stesso file è stata eliminata.

Writer autorevoli correnti:
- `scripts/build_tent_fvg_crosswalk_chat3_7_v01.py`
  - `TENT_FVG_ROUTE_MATCH_DIAGNOSTIC_v01.csv`
  - `TENT_FVG_ROUTE_CROSSWALK_v01.csv`
  - `TENT_FVG_OSM_ACCESS_DIAGNOSTIC_v01.csv`
- `scripts/build_tent_exit_relevance_audit_chat3_7_v01.py`
  - unico writer di `TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv`
- `scripts/finalize_tent_artifacts_chat3_7_v01.py`
  - `FINAL_EVIDENCE_MANIFEST_v01.json`
  - `TENT_FVG_CROSSWALK_QA_v01.json`

L'orchestrazione è affidata a:
`scripts/run_chat3_7_artifact_pipeline_v01.py`

Ordine obbligatorio:
1. diagnostica match TEN-T/FVG;
2. crosswalk per asse;
3. diagnostica automatica OSM;
4. audit finale validato;
5. manifest finale;
6. QA finale.

All'avvio della pipeline QA e manifest precedenti vengono rimossi, impedendo che un'esecuzione incompleta lasci indicatori di successo obsoleti.

## 3. Package sorgente corrente

Package TEN-T corrente:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_7\TEN_T_CURRENT_v01`

Il package contiene i metadati del servizio `TENT_Regulation_2024` e i subset materializzati dei layer:
- 8 — Core;
- 9 — Extended Core;
- 10 — Comprehensive.

I package/manifests precedenti `TEN_T`, `TEN_T_2024_API` e `evidence_manifest_v01.json` sono conservati solo nell'archivio pre-rework e non sono più riferimenti correnti.

Manifest corrente:
`02_external_sources\F3_CHAT_3_7\FINAL_EVIDENCE_MANIFEST_v01.json`

SHA-256:
`A20D0090C1C71EFBE65BC364B5CE56ACB92657EC90C5A8FD9E5349FAC9DEF642`

## 4. Crosswalk corretto

Il crosswalk corrente rappresenta:
- **11 sezioni TENtec ufficiali** materialmente rilevanti per il FVG;
- **aggregate in 6 record di assi stradali FVG**.

Il CSV `TENT_FVG_ROUTE_CROSSWALK_v01.csv` contiene quindi **6 record**, non 11.

| Livello | Asse FVG | Sezioni TENtec aggregate |
|---|---|---:|
| CORE | A/SS202 | 1 |
| CORE | A23 | 3 |
| CORE | A4 | 2 |
| CORE | RA13 | 2 |
| CORE | RA14 | 1 |
| COMPREHENSIVE | A28 | 2 |
| **Totale** | **6 assi** | **11 sezioni** |

Non risultano assi Extended Core in FVG nel package corrente.

Artifact:
`05_intermediate_outputs\F3_CHAT_3_7\TENT_FVG_ROUTE_CROSSWALK_v01.csv`

Record count: **6**
SHA-256:
`BFE5985915CA5169E762E66E603334EC1F8DB36AC10EEBC49297C139CDAF3CE9`

La diagnostica feature-level che identifica le 11 sezioni ufficiali resta separata:
`TENT_FVG_ROUTE_MATCH_DIAGNOSTIC_v01.csv`

Record count: **35 feature esaminate**, di cui **11 marcate come sezioni ufficiali incluse nel crosswalk**.
SHA-256:
`A2EABB19748DFB6836279CF8D30E44E2289FF37B39FF1EDE3F97BBB597283CC2`

## 5. Separazione OSM / evidenza gestore / conclusione validata

### 5.1 Diagnostica automatica OSM

Artifact:
`05_intermediate_outputs\F3_CHAT_3_7\TENT_FVG_OSM_ACCESS_DIAGNOSTIC_v01.csv`

Record count: **6**
SHA-256:
`4F518CE69EC3782EE41490428ED8237C7350C2C358AA4936E4560BBD1B540A9F`

Questo file contiene esclusivamente:
- riferimento OSM usato;
- classi mainline;
- numero di segmenti mainline;
- numero di link adiacenti;
- adiacenze non-link grezze;
- esempi;
- flag `requires_documentary_review`.

Non contiene una conclusione algoritmica sull'esistenza o meno di intersezioni ordinarie a raso.

### 5.2 Evidenze ufficiali gestori

Package:
`02_external_sources\F3_CHAT_3_7\operator_evidence`

Principali evidenze:
- ANAS — `ANAS_soccorso_stradale_unita_FVG_2026.pdf`;
- Autostrade Alto Adriatico — `Autostrade_Alto_Adriatico_network_20260918.html`;
- Autostrade per l'Italia — `ASPI_A23_Pontebba_confine_20260914.html`;
- MIT — `MIT_elenco_strade_TEN_principali_2024.pdf`.

La fonte ASPI è stata materializzata nel rework per rendere riproducibile l'evidenza gestore sul tratto A23 Udine–Tarvisio.

### 5.3 Audit finale validato

Artifact:
`05_intermediate_outputs\F3_CHAT_3_7\TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv`

Record count: **6**
SHA-256:
`153052D726960F798C28933527521956A103740C7B60698BACAE7C8F1F6D6D24`

La lineage del file distingue esplicitamente:
1. appartenenza/classe TEN-T — TENtec 2024;
2. diagnostica topologica automatica — OSM frozen;
3. morfologia/accesso — evidenza ANAS/concessionario + revisione documentale;
4. conclusione — audit validato.

La conclusione sulla presenza/assenza di intersezioni ordinarie a raso **non è presentata come output dell'algoritmo OSM**.

## 6. Esito tecnico sostanziale

Il rework non modifica il risultato geografico già sottoposto alla Chat Madre.

Nel dominio stradale TEN-T FVG corrente non è stato validato alcun asse in cui l'accesso pertinente alla TEN-T debba essere rappresentato mediante una normale intersezione a raso priva di vera uscita/rampa.

Questo resta un **risultato tecnico dell'audit documentale**, non una chiusura metodologica.

Pertanto:
- `ISS-0005` resta **OPEN**;
- `Q-METH-3.3-A` resta **OPEN**;
- `F3_SRC_TENTEC_001` resta **REVIEW**.

La disposizione finale compete alla Chat Madre/utente.

## 7. Manifest e QA finali

Manifest finale:
`02_external_sources\F3_CHAT_3_7\FINAL_EVIDENCE_MANIFEST_v01.json`
SHA-256:
`A20D0090C1C71EFBE65BC364B5CE56ACB92657EC90C5A8FD9E5349FAC9DEF642`

QA finale:
`05_intermediate_outputs\F3_CHAT_3_7\TENT_FVG_CROSSWALK_QA_v01.json`
SHA-256:
`97F16DA5F579539AD0E48BE1F8AB4519416D4390C2961234C52CCACB2453E903`

Il manifest è prodotto solo dopo i quattro CSV finali. Il QA è prodotto solo dopo il manifest.

## 8. Verifica deterministica

La pipeline è stata eseguita ripetutamente sugli stessi input materializzati.

Gli hash dei quattro CSV finali sono rimasti identici tra esecuzioni:
- route-match diagnostic: `A2EABB19748DFB6836279CF8D30E44E2289FF37B39FF1EDE3F97BBB597283CC2`;
- crosswalk: `BFE5985915CA5169E762E66E603334EC1F8DB36AC10EEBC49297C139CDAF3CE9`;
- OSM access diagnostic: `4F518CE69EC3782EE41490428ED8237C7350C2C358AA4936E4560BBD1B540A9F`;
- exit relevance audit: `153052D726960F798C28933527521956A103740C7B60698BACAE7C8F1F6D6D24`.

Manifest e QA non contengono timestamp variabili di esecuzione e sono deterministici a parità di input.

## 9. Quality gate rework

| Controllo | Esito |
|---|---|
| un solo writer autorevole per artifact finale | PASS |
| diagnostica automatica OSM separata dall'audit validato | PASS |
| produzione in ordine deterministico | PASS |
| vecchi QA/manifest non sopravvivono a run incompleta | PASS |
| crosswalk = 6 record / 11 sezioni aggregate | PASS |
| Extended Core FVG = 0 | PASS |
| manifest generato dopo artifact finali | PASS |
| QA generato dopo manifest | PASS |
| hash artifact = manifest = QA | PASS |
| path corrente unico TEN-T | PASS |
| nessun riferimento corrente a manifest legacy | PASS |
| nessuna conclusione a raso attribuita all'algoritmo OSM | PASS |
| candidati non costruiti | PASS |
| distanze candidato–TEN-T non calcolate | PASS |
| `TENT_EXIT_SET_v01` non costruito | PASS |
| ISS-0005 invariato OPEN | PASS |
| Q-METH-3.3-A invariata OPEN | PASS |
| F3_SRC_TENTEC_001 invariato REVIEW | PASS |

## 10. Stato

**Rework Chat 3.7 completato.**

Il quality gate di riproducibilità interno è PASS, ma il precedente PASS tecnico-operativo non viene auto-ripristinato: il lavoro è **READY FOR NEW CHAT MADRE REVIEW**.
