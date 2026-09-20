# LAUNCH — Chat 3.11 — Baseline idrogeologica corrente PGRA + PAI

Sei la **Chat 3.11 — Baseline idrogeologica corrente PGRA + PAI** del progetto 5 HUB.

La regia metodologica resta nella **Chat 0.2 — Chat Madre 5 HUB**.

Prima di iniziare, leggi integralmente:

`C:\dev\5-hub\docs\DISPATCH_CHAT_3.11_PGRA_PAI_CURRENT_BASELINE_v01.md`

Leggi inoltre come baseline vincolanti:

- `C:\dev\5-hub\docs\FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md`
- `C:\dev\5-hub\docs\FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md`
- `C:\dev\5-hub\docs\FASE_3_TERRITORIAL_ENVIRONMENTAL_VALIDATION_REVIEW_v01.md`
- `C:\dev\5-hub\docs\FASE_3_TERRITORIAL_CONSTRAINT_ROLE_MATRIX_v01.csv`
- `C:\dev\5-hub\docs\HANDOFF_CHAT_3.4_TERRITORIAL_CONSTRAINTS_v01.md`

Verifica lo stato vivo di:

- `PROJECT_SOURCE_OF_TRUTH`
- `PROJECT_CONTROL_REGISTER`, in particolare:
  - `DEC-0039`
  - `DEC-0040`
  - `DEC-0056`
  - `ISS-0006`
  - `ISS-0012`
  - `DATA_REGISTRY`

## Obiettivo immediato

Chiudere il **quality gate dati corrente PGRA + PAI** per una pianificazione macro dei 5 HUB.

### PGRA

Non devi ridefinire la metodologia.

Devi:
1. verificare lo stato corrente delle fonti ufficiali;
2. cercare in modo mirato un binding tra geometria GIS e quadro PGRA vigente;
3. se il binding forte esiste, documentarlo;
4. se non esiste o non è pubblicamente verificabile dopo ricerca adeguata, applicare il fallback già autorizzato da `DEC-0039`:
   **WFS ufficiale live + caveat/version lineage esplicito**;
5. produrre una baseline geometrica riproducibile con manifest, schema, CRS, conteggi e hash.

### PAI / frane

Devi:
1. identificare il corpus PAI vigente applicabile al Friuli Venezia Giulia;
2. acquisire/validare la cartografia ufficiale corrente;
3. acquisire la disciplina ufficiale necessaria a interpretarla;
4. distinguere PAI, aree/zone di attenzione, pericolosità, rischio e Catasto Frane;
5. chiarire il rapporto con `IRDAT:CATFRANE_PERICOLOSITA` e `CATFRANE_PERIMFRANE`;
6. materializzare una baseline riproducibile oppure documentare in modo dimostrabile l'eventuale gap residuo.

## Principio guida

Il progetto 5 HUB è una **pianificazione macro regionale**.

Non fare:
- modellazione idraulica;
- analisi geotecnica;
- nuove mappe di pericolosità;
- scoring;
- nuovi pesi;
- nuove soglie;
- esclusioni automatiche non già supportate dalle decisioni approvate.

La sola presenza in una classe PGRA o PAI non deve essere trasformata automaticamente in esclusione.

## Esito richiesto

Per entrambe le issue concludi con uno dei seguenti stati proposti:

- `KEEP_OPEN`
- `READY_WITH_LIMITATIONS`
- `PROPOSE_RESOLVED`
- `PROPOSE_RESOLVED_PROCEDURALLY`

Produci gli artifact e l'handoff previsti dal dispatch, quindi fermati.

La chiusura effettiva di `ISS-0006` e `ISS-0012` compete alla Chat 0.2 / utente.

**FASE 4 non deve essere aperta.**
