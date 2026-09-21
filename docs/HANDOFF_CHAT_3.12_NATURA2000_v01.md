# HANDOFF — Chat 3.12 — Natura 2000: pre-screening operativo v01

**Chat:** 3.12 — Natura 2000: pre-screening operativo  
**Data:** 2026-09-21  
**Stato proposto:** PASS TECNICO CON LIMITAZIONI / READY FOR CHAT 0.2 REVIEW  
**Fase 4:** NON APERTA

## 1. Obiettivo

Costruire il rule-set riproducibile di pre-screening Natura 2000 richiesto da `DEC-0041` e autorizzato da `DEC-0059`, senza riaprire la metodologia FROZEN e senza ricostruire le geometrie ZSC/ZPS già validate dalla Chat 3.4.

## 2. Lavoro svolto

- Letti integralmente dispatch, Fase 1, Fase 2, review ambientale Fase 3, role matrix e handoff Chat 3.4.
- Verificati `PROJECT_SOURCE_OF_TRUTH` e `PROJECT_CONTROL_REGISTER`, inclusi `DEC-0041`, `DEC-0059`, `ISS-0013` e `F3_SRC_FVG_NATURA_001`.
- Ricostruito e verificato il corpus regionale corrente Natura 2000 pertinente al pre-screening.
- Materializzati gli atti/allegati necessari in `F3_CHAT_3_12/official_sources` e registrati URL, dimensioni e SHA-256 nel manifest.
- Implementato parser riproducibile delle prevalutazioni DGR 30/2026 A.2/A.3.
- Formalizzate verifica di corrispondenza, interferenza funzionale generale e override sito-specifico IT3320037.
- Prodotto crosswalk sui 72 codici sito validati.
- Implementati test automatici e cinque fixture sintetiche richieste dal mandato.
- Aggiornati `DATA_REGISTRY` e `ISS-0013` nel registro vivo; `ISS-0013` resta OPEN.
## 3. Corpus e fonti principali

Corpus materializzato in:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_12\official_sources\`

Include almeno:
- DGR 1183/2022 con allegati e tabella Allegato A;
- DGR 30/2026 testo integrale, Allegati A.1, A.2, A.3, B e C;
- DPReg 065/2025 Allegato 14 per IT3320037 Laguna di Marano e Grado;
- Decreto 72016/GRFVG del 30/12/2025 + Allegato 1 sulle condizioni d'obbligo downstream.

Le geometrie restano reference-by-manifest alla baseline Chat 3.4:
- SIC SHA-256 `772dabc52d720eaedfc5bd8de6649d2be915c01a88d2686d553137e3ebaa2e06`;
- ZPS SHA-256 `949724e039aac197490c80e0ebbdfb6fbb46bf2a12f3b457e3989af0bc032660`.

## 4. Output repository

- `docs/FASE_3_NATURA2000_PRESCREEN_VALIDATION_REVIEW_v01.md`
- `docs/FASE_3_NATURA2000_RULESET_v01.csv`
- `docs/FASE_3_NATURA2000_SITE_RULE_CROSSWALK_v01.csv`
- `docs/HANDOFF_CHAT_3.12_NATURA2000_v01.md`
- `scripts/build_natura2000_prescreen_ruleset_chat3_12_v01.py`
- `tests/test_natura2000_prescreen_ruleset_chat3_12_v01.py`
## 5. Output OneDrive / evidence

- `F3_CHAT_3_12/source_manifest_v01.json`
- `F3_CHAT_3_12/qa/natura2000_prescreen_qa_v01.json`
- `F3_CHAT_3_12/qa/natura2000_prescreen_test_results_v01.json`
- fonti ufficiali materializzate in `F3_CHAT_3_12/official_sources`.

Il manifest conserva gli hash delle fonti e, dopo il test finale, anche gli hash degli artifact generati disponibili.

## 6. Risultati quantitativi

- siti Natura 2000 nel crosswalk: **72**;
- siti Allegato A.2: **30**;
- siti Allegato A.3: **42**;
- attività per sito: **50**;
- righe sito × attività: **3.600**;
- righe complessive del rule-set: **3.634**;
- esiti fonte: **2.512** `PREASSESSED_NO_SIGNIFICANT_INCIDENCE`, **1.043** `NOT_APPLICABLE`, **40** `SCREENING_REQUIRED`, **5** `UNKNOWN`;
- siti geometrici senza match di prevalutazione: **0**.

Le cinque celle `UNKNOWN` riguardano l'attività `3.06` nei siti `IT3330009`, `IT3330010`, `IT3340006`, `IT3340007`, `IT3341002`.
Controllo puntuale del PDF: la banda sorgente è effettivamente bianca/non classificata; nessuna inferenza è stata introdotta.
## 7. Regole operative implementate

- La sola distanza/intersezione con Natura 2000 non esclude e non penalizza.
- Il verde della fonte non diventa `VINCA_PASSED`: richiede verifica di corrispondenza e misure di conservazione.
- Il rosso conduce a `SPECIFIC_VINCA_SCREENING_REQUIRED`.
- Il giallo/non pertinente conduce conservativamente a `MANUAL_REVIEW_REQUIRED`, non a esclusione automatica.
- `UNKNOWN` resta esplicito e non implica né prevalutazione applicabile né VINCA automaticamente necessaria.
- Le soglie di interferenza funzionale codificate derivano solo da DGR 30/2026 Allegato C o dall'override DPReg 065/2025 per IT3320037.
- Le regole distinguono ZPS da ZSC/ZPS quando la fonte lo richiede.
- La regola PPR/RER non è sostituita da un buffer generico.
- La riduzione condizionale delle distanze resta `MANUAL_REVIEW_REQUIRED` se gli input ufficiali necessari non sono disponibili.
- Una prevalutazione verde applicabile viene verificata prima di usare un trigger esterno come esito terminale, coerentemente con `DEC-0041`.

## 8. QA e quality gate

Build eseguita con `C:\dev\5-hub\.venv\Scripts\python.exe` e completata con exit code 0.
QA build: 72/30/42 siti coerenti, 3.600 righe, 5 UNKNOWN, nessun sito non matchato.
Test automatici: **19 PASS / 0 FAIL**.
Copertura test: matrice 72×50, conteggi fonte, cinque UNKNOWN, green/red/yellow branches, assenza `VINCA_PASSED`, enum azioni, interferenza funzionale, Laguna, lineage geometrico, manifest/hash, procedura di corrispondenza e cinque fixture richieste.
`py_compile`: PASS.
`git diff --check`: PASS.
## 9. Registri vivi

`DATA_REGISTRY` aggiornato con `F3_SRC_FVG_NATURA_PRESCREEN_001`, stato `REVIEW`, separato dalla precedente fonte geometrica `F3_SRC_FVG_NATURA_001`.
`ISS-0013` aggiornato con gli artifact e il QA, ma lasciato **OPEN**.
Proposta della Chat 3.12: **`PROPOSE_RESOLVED_PROCEDURALLY`**.
La chiusura o il cambio stato ufficiale spettano a Chat 0.2 / utente.

## 10. Git

Branch: `chat-3.12-natura2000-prescreen-ruleset`.
Commit implementazione principale: `166a83da2e15e4c0430cfba4ee84e7525da720cd` — `Implement Natura 2000 prescreen ruleset and QA`.
Il presente handoff e l'aggiornamento del test/finalizer del manifest sono inclusi nel commit di chiusura successivo; il manifest vive su OneDrive e non è versionato in Git.

## 11. Limiti e questioni residue

- Il rule-set non esegue una VINCA e non può attestare formalmente il superamento della VINCA.
- Alcune condizioni di interferenza richiedono in applicazione dati ufficiali PPR/RER, idrologici, habitat/fauna, urbanistici o cartografia del Piano Laguna.
- I dettagli progettuali necessari alla corrispondenza possono essere assenti alla scala macro; in tal caso resta un flag di approfondimento.
- Le cinque celle sorgente `UNKNOWN` richiedono review solo se materialmente coinvolte da un futuro candidato.
- Le condizioni d'obbligo 2025 sono downstream dello screening e non sostituiscono la verifica di prevalutazione.

## 12. Prossimo passo

Chat 0.2 / utente: review del quality gate e decisione su `ISS-0013`.
Se approvato, registrare l'esito di governance senza modificare le baseline FROZEN.
**Non aprire la Fase 4 sulla base di questo handoff: l'apertura resta decisione separata della regia.**
