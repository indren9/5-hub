# HANDOFF BREVE — Chat 3.7 — Rework post review Chat Madre

**Data:** 2026-09-19
**Stato:** REWORK COMPLETED — NEW CHAT MADRE REVIEW REQUIRED
**Branch:** `chat-3.7-tent-crosswalk`

## Correzioni eseguite

- eliminato il doppio writer di `TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv`;
- introdotto `TENT_FVG_OSM_ACCESS_DIAGNOSTIC_v01.csv` per la sola diagnostica automatica OSM;
- mantenuto `TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv` come unico audit finale validato con evidenza gestore + review documentale;
- pipeline resa deterministica: crosswalk/diagnostiche -> audit -> manifest -> QA;
- vecchi package/manifests pre-rework archiviati;
- package TEN-T corrente unico: `02_external_sources\F3_CHAT_3_7\TEN_T_CURRENT_v01`;
- crosswalk corretto: **6 record di assi che aggregano 11 sezioni TENtec ufficiali**;
- lineage OSM / ANAS-concessionari / conclusione validata separata;
- ASPI A23 corrente materializzata come evidenza gestore;
- QA e manifest rigenerati solo dopo gli artifact finali.

## Artifact finali e hash SHA-256

- `TENT_FVG_ROUTE_MATCH_DIAGNOSTIC_v01.csv` — 35 record, 11 sezioni incluse —
  `A2EABB19748DFB6836279CF8D30E44E2289FF37B39FF1EDE3F97BBB597283CC2`
- `TENT_FVG_ROUTE_CROSSWALK_v01.csv` — 6 assi / 11 sezioni aggregate —
  `BFE5985915CA5169E762E66E603334EC1F8DB36AC10EEBC49297C139CDAF3CE9`
- `TENT_FVG_OSM_ACCESS_DIAGNOSTIC_v01.csv` — 6 record —
  `4F518CE69EC3782EE41490428ED8237C7350C2C358AA4936E4560BBD1B540A9F`
- `TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv` — 6 record —
  `153052D726960F798C28933527521956A103740C7B60698BACAE7C8F1F6D6D24`
- `FINAL_EVIDENCE_MANIFEST_v01.json` —
  `A20D0090C1C71EFBE65BC364B5CE56ACB92657EC90C5A8FD9E5349FAC9DEF642`
- `TENT_FVG_CROSSWALK_QA_v01.json` —
  `97F16DA5F579539AD0E48BE1F8AB4519416D4390C2961234C52CCACB2453E903`

Gli hash sono stati verificati contro i file finali OneDrive. La pipeline è stata rieseguita sugli stessi input e gli hash degli artifact sono rimasti invariati; manifest e QA sono anch'essi deterministici.

## Governance

Invariata:
- `ISS-0005 = OPEN`;
- `Q-METH-3.3-A = OPEN`;
- `F3_SRC_TENTEC_001 = REVIEW`;
- nessun candidato;
- nessuna distanza candidato–TEN-T;
- nessun `TENT_EXIT_SET_v01`;
- FASE 1 e FASE 2 non modificate.

## Git

Commit implementazione/review:
`d1a622e61330833a5ff45a83a0c4b21c1f1a7de2`
`fix(fase3): make TEN-T artifacts deterministic`

## Richiesta alla Chat Madre

Eseguire una nuova review indipendente, verificando:
1. writer univoci;
2. schema e record count;
3. 6 record crosswalk / 11 sezioni aggregate;
4. separazione diagnostica OSM vs audit validato;
5. corrispondenza hash tra file, manifest, QA, review e handoff;
6. Git clean.

La Chat 3.7 non propone la chiusura autonoma di `ISS-0005` o `Q-METH-3.3-A`.
