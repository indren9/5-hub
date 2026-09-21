# DISPATCH — Chat 4.2 — Chiusura mapping urbanistico unresolved

**Mandante:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Stato:** AUTHORIZED
**Issue:** ISS-0015 OPEN
**Branch:** `chat-4.2-candidate-mapping-closure`

## 1. Obiettivo

Chiudere il solo blocker emerso dalla review della Chat 4.1: le categorie urbanistiche `GENERATOR_CLASS_UNRESOLVED` che possono materialmente modificare l'universo candidato V2-1.

Non riaprire DQ-01 e non aprire DQ-02.

## 2. Worktree

Lavora esclusivamente in:

`C:\dev\5-hub\_worktrees\chat-4.2-candidate-mapping-closure`

## 3. Baseline vincolanti

Leggere integralmente:
- `docs/CANDIDATE_UNIVERSE_CONTRACT_v01.md`;
- `docs/DQ01_APPROVAL_v01.md`;
- `docs/REVIEW_CHAT_4.1_CANDIDATE_UNIVERSE_BUILD_v01.md`;
- `docs/V2_1_CANDIDATE_UNIVERSE_QA_v01.md`;
- `docs/HANDOFF_CHAT_4.1_CANDIDATE_UNIVERSE_BUILD_v01.md`;
- Fase 1 v03 FROZEN;
- Fase 2 FROZEN;
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER, in particolare ISS-0015.

## 4. Stato di partenza

La build v01 è tecnicamente corretta ma resta REVIEW.

Dati verificati indipendentemente dalla Chat 0.2:
- 3.993 candidati;
- 703 combinazioni native `GENERATOR_CLASS_UNRESOLVED`;
- 3.933 feature sorgente unresolved;
- 4.016 parti post-repair unresolved;
- **1.128 parti unresolved con area >= 8.000 m²**;
- **70 Comuni coinvolti**;
- superficie lorda di tali parti: circa **161,335 km²**.

Queste geometrie sono oggi escluse solo perché la semantica della zona non è sufficientemente risolta.

## 5. Regola metodologica

Le classi approvate restano esclusivamente:
- G1_PRODUCTIVE;
- G2_COMMERCIAL_TERTIARY;
- G3_LOGISTICS_TRANSPORT;
- G4_MIXED_RELEVANT;
- G5_TECHNICAL_UTILITY_ENERGY.

Non creare nuove classi.

Per ogni categoria unresolved materialmente rilevante:
1. consultare prima attributi/legenda/NTA ufficiali già acquisiti;
2. se necessario cercare la fonte ufficiale comunale/regionale pertinente;
3. non inferire la classe dal solo codice urbanistico;
4. se l'evidenza dimostra una classe G1–G5 → `RESOLVED_INCLUDED` + classe;
5. se l'evidenza dimostra una categoria non generatrice → `RESOLVED_EXCLUDED`;
6. se l'evidenza resta insufficiente dopo ricerca documentata → `UNRESOLVED_MATERIAL`.

Ogni decisione semantica deve avere evidence/URL/path/articolo NTA o altra traccia verificabile.

## 6. Priorità

Priorità obbligatoria: tutte le combinazioni unresolved che producono almeno una parte post-repair con `area_m2 >= 8000`.

Le categorie unresolved che producono esclusivamente parti < 8.000 m² possono restare fuori dal blocker V2-1, purché siano mantenute nel mapping e chiaramente marcate come non materialmente incidenti sull'universo corrente.

## 7. Output di mapping

Produrre:

`docs/CANDIDATE_GENERATOR_CLASS_MAPPING_v02.csv`

e almeno:

`docs/CANDIDATE_SEMANTIC_CLOSURE_QA_v01.md`

La tabella deve permettere il confronto v01→v02 e contenere:
- chiave semantica;
- Comune;
- layer;
- codice/descrizione nativa;
- stato v01;
- stato v02;
- generator_class v02;
- evidenza;
- source reference;
- motivazione;
- material_parts_ge8000;
- material_area_m2.

## 8. Rebuild

Preservare integralmente la build v01.

NON sovrascrivere silenziosamente:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\04_geodatabases\V2_1_CANDIDATE_UNIVERSE`

Costruire nuova versione in:

`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\04_geodatabases\V2_1_CANDIDATE_UNIVERSE_v02`

Output principali:
- `CANDIDATE_UNIVERSE_v02.gpkg`;
- `CANDIDATE_LINEAGE_v02.csv`;
- `CANDIDATE_EXCLUSIONS_v02.csv`;
- `CANDIDATE_SOURCE_GAPS_v02.csv`;
- `CANDIDATE_OVERLAP_QA_v02.csv`;
- `CANDIDATE_DISTRIBUTION_QA_v02.csv`;
- machine QA;
- manifest/hash.

## 9. Stabilità degli ID

Per i candidati già presenti in v01 e non modificati semanticamente:
- candidate_id deve restare identico;
- geometry_hash deve restare identico;
- lineage deve preservare continuità.

Nuovi candidati derivati da categorie ora risolte ricevono candidate_id secondo la stessa canonical_identity_key/UUIDv5 già approvata.

## 10. Confronto v01→v02

Produrre un delta audit con almeno:
- candidati v01;
- candidati v02;
- added;
- removed;
- unchanged;
- reclassified;
- distribuzione delta G1–G5;
- delta per Comune;
- unresolved material residui;
- source tier invariati/variati.

Nessun candidato v01 deve sparire per motivi estranei alla chiusura semantica.

## 11. Source gaps e overlap

I 5 Comuni S5 non sono il focus della Chat 4.2.
Non inventare geometrie e non ampliare il perimetro salvo evidenza ufficiale già immediatamente disponibile.

Gli overlap restano gestiti secondo DQ-01: nessun merge per sola sovrapposizione.

## 12. Quality gate

PASS solo se:
- tutti i casi materialmente unresolved (>=8.000 m²) sono stati riesaminati;
- ogni risoluzione ha evidenza verificabile;
- nessuna inferenza è basata sul solo codice;
- `UNRESOLVED_MATERIAL` residui = 0, oppure la chat deve proporre REVIEW/BLOCKED e quantificarli;
- v01 preservato;
- v02 deterministico;
- 100% candidati v02 >= 8.000 m²;
- mapping G1–G5 auditabile;
- ID stabili per gli unchanged;
- manifest/hash PASS;
- test PASS;
- git diff --check PASS;
- branch pulito e pushato;
- DQ-02 non aperta.

## 13. Output repository

Produrre almeno:
- `docs/CANDIDATE_GENERATOR_CLASS_MAPPING_v02.csv`;
- `docs/CANDIDATE_SEMANTIC_CLOSURE_QA_v01.md`;
- `docs/V2_1_CANDIDATE_UNIVERSE_V02_QA_v01.md`;
- `docs/V2_1_CANDIDATE_UNIVERSE_V01_V02_DELTA_v01.csv`;
- `docs/HANDOFF_CHAT_4.2_CANDIDATE_MAPPING_CLOSURE_v01.md`;
- script/config/test necessari.

## 14. Chiusura

Riportare in modo sintetico:
- quanti dei 1.128 casi materialmente unresolved sono stati risolti;
- quanti G1–G5;
- quanti RESOLVED_EXCLUDED;
- eventuali UNRESOLVED_MATERIAL residui;
- candidati finali v02;
- delta rispetto ai 3.993 v01;
- hash principali;
- esito PASS/REVIEW/BLOCKED.

Poi fermarsi per review Chat 0.2.

NON aprire DQ-02.
