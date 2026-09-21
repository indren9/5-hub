# HANDOFF — Chat 0.3 — Re-baseline strategica e semplificazione metodologica v01

**Chat:** 0.3 — Re-baseline strategica e semplificazione metodologica
**Mandante:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Branch:** chat-0.3-strategic-rebaseline
**Stato proposto:** PASS / READY FOR CHAT 0.2 + USER REVIEW
**Fase 4:** NON APERTA

## 1. Obiettivo

Riadattare l'intera architettura metodologica del progetto al nuovo scopo approvato con DEC-0061: modello GIS multicriterio dimostrativo a scala di pianificazione strategica, con output finale costituito da una configurazione di cinque poligoni territorialmente preferibile secondo criteri e pesi dichiarati, senza trasformare il modello in due diligence catastale, proprietaria, autorizzativa o progettuale.

## 2. Fonti e stato vivo verificati

Sono stati verificati:
- dispatch ufficiale Chat 0.3 nel worktree corretto;
- PROJECT_SOURCE_OF_TRUTH vivo su Google Drive;
- PROJECT_CONTROL_REGISTER vivo su Google Drive;
- tutte le 61 DEC registrate fino a DEC-0061;
- tutte le 14 ISS;
- tutte le 31 voci DATA_REGISTRY;
- ROADMAP_METODOLOGICA_v1;
- baseline Fase 1 e Fase 2 FROZEN;
- principali review/handoff Fase 3;
- architettura e review della Chat 90.0;
- branch chat-3.12-natura2000-prescreen-ruleset e review indipendente PASS WITH LIMITATIONS;
- artifact tracciati nei worktree/branch rilevanti.

La Chat 3.12 risulta tecnicamente supportata con PASS WITH LIMITATIONS, ma ISS-0013 resta OPEN nella governance viva e il branch non viene integrato da questa chat.

## 3. Lavoro svolto

Prodotto un nuovo model contract che:
- fissa scala strategica e significato della cinquina;
- conferma il poligono come unità di analisi;
- separa qualità individuale e qualità della configurazione;
- definisce solo la semantica di hard constraint, soft criterion e flag;
- sposta proprietà, disponibilità commerciale, due diligence, capacità/connessione reale e progettazione locale fuori dal core;
- non introduce indicatori, formule, pesi, normalizzazione, funzione obiettivo o algoritmo.

Prodotta una roadmap v2 a 10 stadi V2-0…V2-9, sostanzialmente più snella della sequenza v1 a 16 fasi:
- elimina la fattibilità energetica di dettaglio come fase autonoma;
- elimina la verifica puntuale dei finalisti come gate del modello;
- rende il confronto Claude opzionale/storico;
- concentra il core su universo candidati, criteri, misura, normalizzazione, pesi/score, configurazione, selezione, robustezza e freeze.

Prodotta una impact matrix esaustiva con 240 righe:
- 16 fasi roadmap v1;
- 61 DEC;
- 14 ISS;
- 31 dataset DATA_REGISTRY;
- 103 artifact tracciati nel worktree Chat 0.3;
- 15 artifact aggiuntivi presenti sui branch Chat 3.12 e Chat 90.0 ma non nel worktree 0.3.

Prodotta una issue disposition completa per ISS-0001…ISS-0014.

Prodotta una decision queue di sole 9 decisioni sostanziali future.

Prodotta la nota di riallineamento per Chat 90.0 senza modificare i suoi artifact.

## 4. Proposte metodologiche principali

### Roadmap v1
Proposta: SUPERSEDED_PROPOSED / HISTORICAL SUPPORT.
Dopo approvazione utente della v2: DEPRECATED / SUPERSEDED BY ROADMAP_METODOLOGICA_v2.

### Fase 1
Il nucleo F1-D1…F1-D7 resta valido.

Proposta di successore, senza modificare il FROZEN v02:
FASE_1_HUB_DEFINITION_CONSOLIDATED_v03_PROPOSED.md

Modifiche previste:
- mantenere integralmente F1-D1…F1-D7;
- conservare AFIR/TEN-T quando materialmente rilevante alla funzione strategica;
- spostare progettazione accessi, sicurezza sito-specifica, capacità/connessione elettrica reale e verifiche esecutive a post-model;
- distinguere requisiti funzionali dell'Hub da due diligence del terreno.

### Fase 2
KEEP / FROZEN.
Nessun successore proposto.

### Fase 3
Proposta futura: PASS / CLOSED WITH DECLARED LIMITATIONS, solo dopo:
- approvazione della re-baseline;
- disposizione di ISS-0009 come post-model;
- decisione su ISS-0013;
- integrazione governata del lavoro Chat 3.12, se approvata.

I dataset non selezionati come indicatori non devono restare blocker della chiusura.

## 5. DEC che richiedono nuova disposizione/approvazione

Le proposte che modificano il ruolo operativo di decisioni ACCEPTED/FROZEN richiedono esplicita approvazione utente.

Principali:
- DEC-0016 — roadmap v1 da superare formalmente;
- baseline Fase 1 / DEC-0013 — nuovo successore v03, senza modifica del FROZEN;
- DEC-0032 — current-first semplificato come gerarchia/preferenza, non due diligence region-wide;
- DEC-0033 — proprietà/disponibilità commerciale spostate fuori dal core;
- DEC-0042 — rimuovere l'implicita approvazione anticipata di una futura penalizzazione dei prati stabili; ruolo da decidere in DQ-02;
- DEC-0048 — currentness urbanistica puntuale del finalista non più gate di chiusura del modello;
- DEC-0050 e DEC-0053 — proxy energetico KEEP, capacità/punto/costo reale post-model;
- DEC-0055 — baseline Light/Heavy KEEP, local road access check non più gate del modello strategico;
- DEC-0058 — fallback PAI KEEP, pointwise check post-model salvo futura regola hard esplicitamente approvata;
- DEC-0060 — Chat 90.0 KEEP, architettura editoriale da riallineare con v02.

DEC-0061 resta KEEP ed è il vincolo fondante.

## 6. ISS che richiedono nuova disposizione

- ISS-0002: proposta RESOLVED_AS_HISTORICAL; l'universo Claude non verrà riusato come universo autorevole.
- ISS-0007: resta RESOLVED; esplicitare che il dettaglio di connessione è post-model.
- ISS-0009: proposta CLOSED_OUT_OF_SCOPE_CORE / DEFER_POST_MODEL.
- ISS-0010: resta RESOLVED; currentness come flag/limite, due diligence puntuale post-model.
- ISS-0011: resta RESOLVED; gap biotopi come flag/limite salvo futura regola.
- ISS-0012: resta RESOLVED; pointwise PAI post-model salvo futura regola.
- ISS-0013: proposta RESOLVED_PROCEDURALLY, coerente con la review indipendente PASS WITH LIMITATIONS della Chat 3.12; decisione e merge restano a Chat 0.2/utente.

Le altre ISS restano risolte/storiche secondo il registro corrente.

## 7. Decision queue futura minima

Le sole decisioni che possono cambiare materialmente il risultato sono:
1. universo dei poligoni e prefiltri indispensabili;
2. set criteri/indicatori e ruolo HARD/SOFT/FLAG;
3. trasformazioni e normalizzazione;
4. metodo e valori dei pesi;
5. formula dello score individuale;
6. qualità/funzione della configurazione di 5;
7. eventuali vincoli di configurazione;
8. algoritmo/procedura di selezione;
9. piano di sensitivity/robustness.

Nessuna di queste è approvata dalla Chat 0.3.

## 8. Artifact creati

Commit metodologico principale:
28df1d0 — docs(rebaseline): propose strategic multicriteria model v2

File:
- docs/PROJECT_MODEL_CONTRACT_REBASELINE_v01_PROPOSED.md
- docs/ROADMAP_METODOLOGICA_v2_PROPOSED.md
- docs/REBASELINE_IMPACT_MATRIX_v01.csv
- docs/REBASELINE_ISSUE_DISPOSITION_v01.csv
- docs/REBASELINE_DECISION_QUEUE_v01.md
- docs/REBASELINE_EDITORIAL_IMPACT_CHAT90_v01.md
- docs/HANDOFF_CHAT_0.3_STRATEGIC_REBASELINE_v01.md

Il presente handoff viene committato separatamente dopo il commit metodologico principale.

## 9. Quality gate

- DEC-0061 rispettata: PASS.
- Intero progetto mappato senza cancellazioni implicite: PASS, 240 elementi.
- Aree fuori scope esplicitamente separate: PASS.
- FROZEN/ACCEPTED non modificati silenziosamente: PASS.
- F1/F2 originali non modificati: PASS.
- Roadmap v2 sostanzialmente più snella: PASS.
- Ogni fase futura ha output e gate verificabili: PASS.
- Scoring/pesi/F.O./vincoli/algoritmo non approvati implicitamente: PASS.
- Ruolo del poligono coerente: PASS.
- Proprietà/disponibilità riclassificate post-model: PASS PROPOSED, soggetto ad approvazione.
- Urbanistica distinta tra generazione/classificazione e due diligence puntuale: PASS.
- Energia mantenuta come proxy macro senza MW/connessione/costi: PASS.
- Mobilità macro separata da accesso locale progettuale: PASS.
- Ambiente/tutele preservati senza nuove interpretazioni normative: PASS.
- Chat 3.12 considerata senza chiudere ISS-0013 o fare merge: PASS.
- Impatto Chat 90.0 documentato senza modificarne gli artifact: PASS.
- CSV impact matrix: 240 righe, disposizioni tutte nel vocabolario consentito: PASS.
- Issue disposition: 14/14 issue: PASS.
- Fase 4 non aperta: PASS.
- git diff --check sul commit metodologico: PASS.
- branch clean: da verificare dopo commit del presente handoff.

## 10. Problemi aperti / limiti

- La governance viva non è stata modificata dalla Chat 0.3: le disposizioni restano PROPOSED.
- ISS-0013 resta OPEN fino a decisione esplicita.
- Il branch Chat 3.12 non è stato merged.
- Nessun successore F1 v03 è stato creato: è solo proposto.
- Nessuna decisione della queue futura è stata risolta.
- Nessuna Fase 4/V2-1 è stata aperta.

## 11. Prossimo passo minimo consigliato

Chat 0.2 deve eseguire review della re-baseline e sottoporre all'utente un unico pacchetto decisionale compatto:
1. approvazione model contract + roadmap v2;
2. approvazione delle disposizioni sulle DEC ACCEPTED/FROZEN elencate al §5;
3. disposizione ISS-0009 e ISS-0013;
4. autorizzazione a predisporre il successore Fase 1 v03 e aggiornare la governance viva.

Solo dopo questo passaggio potrà essere valutata l'apertura della nuova fase di costruzione dell'universo candidato.

STOP — la Chat 0.3 non apre la Fase 4 e non implementa scoring, pesi, candidati o ottimizzazione.
