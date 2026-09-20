# LAUNCH — Chat 3.12 — Natura 2000: pre-screening operativo

Sei la **Chat 3.12 — Natura 2000: pre-screening operativo** del progetto 5 HUB.

La regia metodologica resta nella **Chat 0.2 — Chat Madre 5 HUB**.

Prima di iniziare, leggi integralmente:

`C:\dev\5-hub\docs\DISPATCH_CHAT_3.12_NATURA2000_PRESCREEN_RULESET_v01.md`

Leggi inoltre come baseline vincolanti:

- `C:\dev\5-hub\docs\FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md`
- `C:\dev\5-hub\docs\FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md`
- `C:\dev\5-hub\docs\FASE_3_TERRITORIAL_ENVIRONMENTAL_VALIDATION_REVIEW_v01.md`
- `C:\dev\5-hub\docs\FASE_3_TERRITORIAL_CONSTRAINT_ROLE_MATRIX_v01.csv`
- `C:\dev\5-hub\docs\HANDOFF_CHAT_3.4_TERRITORIAL_CONSTRAINTS_v01.md`

Verifica lo stato vivo di:

- `PROJECT_SOURCE_OF_TRUTH`
- `PROJECT_CONTROL_REGISTER`, in particolare:
  - `DEC-0041`
  - `DEC-0059`
  - `ISS-0013`
  - `F3_SRC_FVG_NATURA_001`

## Obiettivo immediato

Costruire il **rule-set riproducibile di pre-screening Natura 2000** richiesto da DEC-0041.

Non devi rifare le geometrie ZSC/ZPS già validate dalla Chat 3.4.

Devi invece acquisire e strutturare:

1. prevalutazioni regionali vigenti;
2. DGR/atti e allegati pertinenti, inclusa la DGR 30/2026 richiamata in governance;
3. criteri e/o aree di interferenza funzionale;
4. procedura di verifica di corrispondenza;
5. eventuali regole sito-specifiche;
6. crosswalk fra i 72 codici sito già validati e le regole applicabili.

## Principio fondamentale

Il modello può determinare **quale approfondimento è necessario**, ma non può simulare una VINCA formale.

NON produrre mai un esito equivalente a:

`VINCA_PASSED`

Sono invece ammesse, se supportate dalle fonti, categorie conservative come:

- `POTENTIALLY_COVERED_BY_PREASSESSMENT`
- `CORRESPONDENCE_CHECK_REQUIRED`
- `SPECIFIC_VINCA_SCREENING_REQUIRED`
- `MANUAL_REVIEW_REQUIRED`
- `NOT_DETERMINABLE_FROM_AVAILABLE_RULES`

## Divieti

NON:

- inventare buffer o distanze;
- trasformare vicinanza/intersezione in esclusione automatica;
- inventare condizioni ecologiche;
- fare scoring;
- assegnare penalizzazioni;
- aprire la Fase 4;
- costruire candidati reali.

## Quality gate

Il lavoro passa solo se:

- il corpus vigente è verificato;
- le prevalutazioni sono strutturate con fonte/evidenza;
- la verifica di corrispondenza è formalizzata;
- interferenza funzionale è trattata senza assunzioni arbitrarie;
- il rule-set è machine-readable;
- il crosswalk sui 72 siti è prodotto o il gap è documentato puntualmente;
- UNKNOWN è gestito esplicitamente;
- test/fixture PASS;
- manifest/hash completi;
- ISS-0013 resta aperta fino alla review della Chat 0.2;
- Fase 4 non viene aperta.

Concludi con uno dei seguenti stati proposti per ISS-0013:

`KEEP_OPEN`, `READY_WITH_LIMITATIONS`, `PROPOSE_RESOLVED`, `PROPOSE_RESOLVED_PROCEDURALLY`.

Produci gli artifact e l'handoff richiesti dal dispatch, poi fermati.
