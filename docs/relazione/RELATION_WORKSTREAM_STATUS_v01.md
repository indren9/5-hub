# RELATION WORKSTREAM STATUS v01

**Chat:** 90.0 — Relazione Builder  
**Data:** 2026-09-21  
**Governance:** DEC-0060 — ACCEPTED  
**Review:** REVIEW_CHAT_90.0_RELATION_BUILDER_v01.md — ACCEPTED_WITH_EDITORIAL_GUARDRAILS

## Stato generale

La Chat 90.0 è attiva come workstream editoriale trasversale.

La baseline editoriale accettata resta:
- RELATION_ARCHITECTURE_v01.md;
- RELATION_TRACEABILITY_MATRIX_v01.csv;
- EXTERNAL_SOURCE_REGISTER_TEMPLATE_v01.csv;
- EDITORIAL_GAPS_v01.md;
- CLAUDE_BASELINE_EDITORIAL_USE_v01.md;
- REVIEW_CHAT_90.0_RELATION_BUILDER_v01.md.

Gli artifact sopra non vengono riscritti retroattivamente per incorporare l'accettazione: DEC-0060 e la review ne costituiscono il layer di governance successivo.

## Stato scientifico di riferimento

- Fase 1: PASS / CLOSED / FROZEN.
- Fase 2: PASS / CLOSED / FROZEN.
- Fase 3: IN CORSO.
- Fasi 4–15: NON AVVIATE.
- Issue OPEN verificate al 2026-09-21: ISS-0002, ISS-0009, ISS-0013.

## Workstream editoriali

| Chat | Nome | Stato editoriale | Dipendenze | Output principale |
|---|---|---|---|---|
| 90.1 | Fonti esterne e bibliografia | DISPATCHED / SEED_STARTED | governance viva + fonti originali | EXTERNAL_SOURCE_REGISTER_v01.csv normalizzato/verificato + handoff |
| 90.2 | Matrice di tracciabilità interna | DISPATCHED | SOT + PCR + baseline/review correnti | RELATION_TRACEABILITY_MATRIX_v02.csv + handoff |
| 90.3 | Redazione capitoli consolidati F1/F2 | DISPATCHED_WITH_DEPENDENCIES | seed fonti 90.1 + audit 90.2 | bozze consolidate capp. 1, 3, 4 + handoff |

## Regole operative

1. Nessuna chat 90.x ha autorità metodologica.
2. Le fonti esterne non devono essere confuse con la tracciabilità interna.
3. Claude/QGIS storico può essere consultato solo secondo CLAUDE_BASELINE_EDITORIAL_USE_v01.md.
4. Un contenuto NOT_READY non viene trasformato in testo definitivo.
5. Un contenuto PARTIAL viene scritto solo nella porzione già consolidata.
6. Contraddizioni o nuove necessità metodologiche vengono riportate alla Chat 90.0 e, se sostanziali, alla Chat 0.2.
7. Ogni workstream significativo produce artifact persistenti e handoff.

## Prossimo controllo della Chat 90.0

Dopo i primi handoff 90.1 e 90.2:
- verificare coerenza tra fonte esterna e claim;
- aggiornare readiness solo se lo stato scientifico lo consente;
- autorizzare la stabilizzazione editoriale delle bozze 90.3;
- non anticipare candidati, ranking o risultati.
