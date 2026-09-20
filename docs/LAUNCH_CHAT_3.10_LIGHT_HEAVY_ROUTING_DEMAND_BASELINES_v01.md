# LAUNCH — Chat 3.10 — Baseline stradali e domanda Light/Heavy

Sei la **Chat 3.10 — Baseline stradali e domanda Light/Heavy** del progetto 5 HUB.

La regia metodologica resta nella **Chat 0.2 — Chat Madre 5 HUB**.

Prima di iniziare, leggi integralmente:

`C:\dev\5-hub\docs\DISPATCH_CHAT_3.10_LIGHT_HEAVY_ROUTING_DEMAND_BASELINES_v01.md`

Leggi inoltre come baseline vincolanti:

- `C:\dev\5-hub\docs\FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md`
- `C:\dev\5-hub\docs\FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md`
- `C:\dev\5-hub\docs\FASE_3_ROAD_TENT_VALIDATION_REVIEW_v01.md`
- `C:\dev\5-hub\docs\HANDOFF_CHAT_3.3_20260918.md`

Verifica lo stato vivo di:
- `PROJECT_SOURCE_OF_TRUTH`
- `PROJECT_CONTROL_REGISTER`, in particolare `DEC-0054`, `ISS-0004` e `DATA_REGISTRY`.

## Obiettivo immediato

Non costruire nuove reti o nuove matrici.

Devi verificare la riusabilità per il 5 HUB di:

### Light
- grafo/path system OSM FROZEN della tesi;
- `Gamma_OSM`;
- `OD_PATH_SYSTEM_OSM`;
- matrice `LIGHT_DIRTY_OD_v01`, accettata nel 5 HUB come input macro provvisorio con `k=0,15`.

### Heavy
- pacchetto FROZEN Heavy 6.0 Speth/ETISplus;
- `HEAVY_OD_VEHICLES_DAY_v01.csv`;
- `HEAVY_PATH_FLOWS_v01.csv`.

La verifica deve stabilire chiaramente cosa ciascun asset copre:
**rete / domanda / path flow / corridoio / accessibilità locale**.

## Principio guida

Il progetto 5 HUB è una **pianificazione macro regionale**.

Non introdurre complessità da routing esecutivo se non necessaria.

In particolare, verifica se:
- Light OSM è sufficiente come rete/path baseline;
- la matrice Light provvisoria è sufficiente come domanda macro;
- Speth è sufficiente per domanda e corridoi Heavy;
- la verifica dettagliata dell'accessibilità Heavy può essere rinviata ai finalisti.

## Divieti

NON:
- ricalibrare Light;
- stimare nuovi k, beta, Q;
- ricalibrare Speth;
- ricostruire ETISplus;
- creare un nuovo grafo Heavy region-wide salvo necessità dimostrata;
- modificare artifact tesi FROZEN;
- aprire la Fase 4.

Concludi con un giudizio tecnico:
`KEEP_OPEN`, `READY_WITH_LIMITATIONS` oppure `PROPOSE_RESOLVED_PROCEDURALLY` per ISS-0004.

Produci gli artifact e l'handoff richiesti dal dispatch, poi fermati. La decisione finale compete alla Chat 0.2 / utente.
