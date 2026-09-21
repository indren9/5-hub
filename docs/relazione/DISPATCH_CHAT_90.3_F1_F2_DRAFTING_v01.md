# DISPATCH — Chat 90.3 — Redazione capitoli consolidati F1/F2

**Parent:** Chat 90.0 — Relazione Builder  
**Data:** 2026-09-21  
**Mandato:** esclusivamente editoriale/documentale  
**Autorità metodologica:** nessuna  
**Stato:** DISPATCHED_WITH_DEPENDENCIES  
**Governance:** DEC-0060; REVIEW_CHAT_90.0_RELATION_BUILDER_v01.md

## Obiettivo

Produrre le prime bozze consolidate dei capitoli già READY:
- Capitolo 1 — Contesto, obiettivi e problema di localizzazione;
- Capitolo 3 — Definizione funzionale degli Hub Energetici Green;
- Capitolo 4 — Perimetro territoriale e unità di analisi.

Le bozze devono essere leggibili da un soggetto esterno e non raccontare la cronologia delle chat.

## Dipendenze

Prima della stabilizzazione editoriale:
- usare il primo seed verificato di EXTERNAL_SOURCE_REGISTER_v01.csv prodotto dalla Chat 90.1;
- usare la lineage verificata della RELATION_TRACEABILITY_MATRIX_v02.csv prodotta dalla Chat 90.2.

È possibile predisporre una bozza interna basata sui documenti FROZEN, ma non chiudere il quality gate finché le dipendenze sopra non sono disponibili.

## Input vincolanti

- docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md — FROZEN;
- docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md — FROZEN;
- relative review accettate;
- docs/relazione/RELATION_ARCHITECTURE_v01.md;
- docs/relazione/REVIEW_CHAT_90.0_RELATION_BUILDER_v01.md;
- registro fonti e matrice di tracciabilità aggiornati quando disponibili.

## Regole di scrittura

1. Scrivere per lettore esterno.
2. Non usare DEC, ISS, nomi chat o commit nel corpo principale salvo eccezione motivata.
3. Distinguere chiaramente:
   - requisito normativo;
   - definizione progettuale;
   - assunzione;
   - proxy;
   - limite.
4. Non anticipare candidati, indicatori, pesi, ranking o risultati.
5. Non trasformare elementi PARTIAL/NOT_READY in contenuto consolidato.
6. Non aggiungere requisiti tecnici non presenti nelle baseline FROZEN.
7. Citare fonti esterne solo dopo verifica editoriale.

## Output richiesti

Preferibilmente file separati:
- docs/relazione/drafts/CHAPTER_01_CONTEXT_OBJECTIVES_v01.md;
- docs/relazione/drafts/CHAPTER_03_HUB_DEFINITION_v01.md;
- docs/relazione/drafts/CHAPTER_04_UNIT_OF_ANALYSIS_v01.md;
- HANDOFF_CHAT_90.3_F1_F2_DRAFTING_v01.md.

## Quality gate

PASS solo se:
- i testi sono autosufficienti per lettore esterno;
- ogni claim tecnico è coperto dalla baseline FROZEN o da fonte esterna verificata;
- nessuna governance interna invade la narrazione;
- terminologia F1/F2 è preservata;
- nessuna nuova metodologia è introdotta;
- le tre bozze sono coerenti tra loro;
- git diff --check PASS.

## Stop condition

Se la scrittura richiede una scelta metodologica non presente nelle baseline FROZEN, non inventarla: registrare il punto e riportarlo alla Chat 90.0.
