# HANDOFF — Chat 3.7 — Crosswalk TEN-T FVG e rilevanza delle uscite AFIR

**Data attività originaria:** 2026-09-18
**Rework post review:** 2026-09-19
**Stato:** REWORK COMPLETED — READY FOR NEW CHAT MADRE REVIEW
**Stato FASE 3:** IN CORSO — NON CLOSED, NON FROZEN
**Branch:** `chat-3.7-tent-crosswalk`

## 1. Esito sostanziale invariato

La rete stradale TEN-T corrente FVG comprende **11 sezioni TENtec ufficiali aggregate in 6 assi stradali**:
- CORE: A4, A23, RA13, RA14, A/SS202;
- EXTENDED CORE: nessun asse FVG;
- COMPREHENSIVE-only: A28.

Il CSV di crosswalk ha quindi **6 record di assi**, non 11 record.

L'audit validato non ha individuato un asse FVG in cui la questione AFIR della “nearest TEN-T exit” debba essere risolta tramite una normale intersezione a raso priva di vera rampa/svincolo. Questa conclusione deriva dalla combinazione di TENtec, diagnostica OSM e verifica documentale dei gestori, non dal solo algoritmo OSM.

La conclusione resta sottoposta alla Chat Madre.

## 2. Rework di riproducibilità

Problema corretto: due script scrivevano lo stesso `TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv` con schemi diversi.

Architettura corrente:
- `build_tent_fvg_crosswalk_chat3_7_v01.py`
  - route-match diagnostic;
  - crosswalk;
  - OSM access diagnostic;
- `build_tent_exit_relevance_audit_chat3_7_v01.py`
  - unico writer dell'audit finale;
- `finalize_tent_artifacts_chat3_7_v01.py`
  - manifest finale;
  - QA finale;
- `run_chat3_7_artifact_pipeline_v01.py`
  - esegue i passaggi nel solo ordine supportato.

La pipeline rimuove QA/manifest precedenti prima di partire; quindi un run fallito non può lasciare un QA vecchio apparentemente valido.

## 3. Lineage corrente

### TEN-T corrente
`02_external_sources\F3_CHAT_3_7\TEN_T_CURRENT_v01`

### Evidenze gestori
`02_external_sources\F3_CHAT_3_7\operator_evidence`

Include:
- ANAS;
- Autostrade Alto Adriatico;
- ASPI A23 Udine–Tarvisio;
- MIT.

### Manifest
`02_external_sources\F3_CHAT_3_7\FINAL_EVIDENCE_MANIFEST_v01.json`

I package/manifests pre-rework sono conservati in:
`90_archive\F3_CHAT_3_7_PRE_REWORK_20260919`

e non costituiscono riferimenti correnti.

## 4. Artifact finali verificati

| Artifact | Record | SHA-256 |
|---|---:|---|
| `TENT_FVG_ROUTE_MATCH_DIAGNOSTIC_v01.csv` | 35, con 11 sezioni incluse | `A2EABB19748DFB6836279CF8D30E44E2289FF37B39FF1EDE3F97BBB597283CC2` |
| `TENT_FVG_ROUTE_CROSSWALK_v01.csv` | 6 assi / 11 sezioni aggregate | `BFE5985915CA5169E762E66E603334EC1F8DB36AC10EEBC49297C139CDAF3CE9` |
| `TENT_FVG_OSM_ACCESS_DIAGNOSTIC_v01.csv` | 6 | `4F518CE69EC3782EE41490428ED8237C7350C2C358AA4936E4560BBD1B540A9F` |
| `TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv` | 6 | `153052D726960F798C28933527521956A103740C7B60698BACAE7C8F1F6D6D24` |
| `FINAL_EVIDENCE_MANIFEST_v01.json` | JSON | `A20D0090C1C71EFBE65BC364B5CE56ACB92657EC90C5A8FD9E5349FAC9DEF642` |
| `TENT_FVG_CROSSWALK_QA_v01.json` | JSON | `97F16DA5F579539AD0E48BE1F8AB4519416D4390C2961234C52CCACB2453E903` |

Gli hash dei CSV sono risultati identici in esecuzioni ripetute sugli stessi input.

## 5. Separazione della prova

`TENT_FVG_OSM_ACCESS_DIAGNOSTIC_v01.csv` registra solo risultati automatici:
- segmenti mainline;
- link adiacenti;
- adiacenze non-link grezze;
- necessità di review documentale.

`TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv` aggiunge:
- evidenze ANAS/concessionario;
- revisione manuale/documentale;
- morfologia validata;
- conclusione finale.

Pertanto l'assenza validata di un caso ordinario a raso non viene attribuita all'algoritmo OSM.

## 6. Governance invariata

- `ISS-0005`: **OPEN**;
- `Q-METH-3.3-A`: **OPEN**;
- `F3_SRC_TENTEC_001`: **REVIEW**;
- `TENT_EXIT_SET_v01`: non creato;
- candidati: non creati;
- distanze candidato–TEN-T: non calcolate;
- FASE 1 e FASE 2: non modificate;
- PROJECT_SOURCE_OF_TRUTH: non modificato nel rework.

## 7. Quality gate rework

PASS:
- writer univoci;
- schema verificato;
- record count verificato;
- hash verificati;
- manifest coerente;
- QA coerente;
- source package corrente univoco;
- lineage OSM / gestori / conclusione separata;
- pipeline deterministica;
- nessun artifact fuori mandato.

## 8. SESSION CLOSE REWORK

**NOTEBOOK_CHANGE = NO**
**REGISTER_CHANGE = NO** — gli stati richiesti restano invariati.
**PROJECT_SOURCE_OF_TRUTH_CHANGE = NO**
**GIT_COMMIT_REQUIRED = YES**

Commit implementazione/review rework: `d1a622e61330833a5ff45a83a0c4b21c1f1a7de2` — `fix(fase3): make TEN-T artifacts deterministic`.

## 9. Prossimo passo

Richiesta una **nuova review indipendente della Chat Madre**.

La Chat Madre dovrà verificare in particolare:
1. unicità dei writer;
2. separazione diagnostica OSM / audit validato;
3. corrispondenza 6 record crosswalk ↔ 11 sezioni ufficiali aggregate;
4. hash di CSV, manifest e QA;
5. Git clean.

Nessuna chiusura di ISS-0005 o Q-METH-3.3-A è proposta da questa chat.
