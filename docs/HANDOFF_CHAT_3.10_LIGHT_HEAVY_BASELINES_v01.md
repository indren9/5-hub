# HANDOFF — Chat 3.10 — Baseline stradali e domanda Light/Heavy

**Chat:** 3.10 — Baseline stradali e domanda Light/Heavy  
**Data chiusura:** 2026-09-20  
**Regia:** Chat 0.2 — Chat Madre 5 HUB  
**Stato attività:** COMPLETED / REVIEW  
**Quality gate tecnico:** PASS WITH LIMITATIONS  
**Raccomandazione ISS-0004:** PROPOSE_RESOLVED_PROCEDURALLY  
**Decisione finale ISS-0004:** non presa da Chat 3.10; resta alla Chat 0.2 / utente.

## 1. Obiettivo

Verificare la riusabilità macro nel 5 HUB delle baseline tesi Light/Heavy già esistenti, senza ricostruire reti o matrici e senza modificare artifact FROZEN.

## 2. Baseline lette e governance

Letti integralmente il dispatch Chat 3.10, le baseline FROZEN Fase 1 e Fase 2, la review Chat 3.3 e il relativo handoff.

Verificati live PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER; DEC-0054 = ACCEPTED; ISS-0004 = OPEN all'avvio e ancora OPEN alla chiusura.

## 3. Lavoro svolto

LIGHT:
- verificato G_OSM_operativo FROZEN e relativo final gate;
- verificato Gamma_OSM FROZEN;
- verificato OD_PATH_SYSTEM_OSM FROZEN;
- verificato LIGHT_DIRTY_OD_v01 come input macro provvisorio con k=0,15;
- confermata lineage LIGHT_DIRTY_OD_v01 -> OSM_OD_municipal_summary_v01 del package F57.

HEAVY:
- verificato HEAVY_0B_delivery_v01.zip;
- ri-hashati i tre membri principali;
- verificati conteggi OD e path;
- verificata conversione annuale/giornaliero /365;
- confermato uso di Speth/ETISplus per domanda, path-flow e corridoi macro.

Non sono stati ricalibrati Light, ANAS o Speth; non sono state costruite reti, matrici o candidate di Fase 4.

## 4. Risultati tecnici principali

- G_OSM è sufficiente come baseline Light rete/path macro; non dimostra accesso locale candidato.
- Gamma_OSM copre accessi/impedenze comunali, non accessi dei futuri Hub.
- OD_PATH_SYSTEM_OSM copre il path system Light macro, non la domanda.
- LIGHT_DIRTY_OD_v01 è sufficiente come PROVISIONAL_MACRO_INPUT; resta non-canonico nella tesi.
- Heavy 6.0 Speth è sufficiente per domanda, path-flow e corridoi Heavy macro.
- Heavy 6.0 non dimostra accessibilità fisica/legale locale; la verifica dettagliata può essere rinviata ai finalisti.
- Non emerge necessità di un nuovo grafo Heavy region-wide per la pianificazione macro.

Raccomandazione tecnica su ISS-0004: PROPOSE_RESOLVED_PROCEDURALLY.

## 5. Anomalia emersa

La copia TESI_BASELINE_SAFE di G_OSM_operativo_v01.gpkg ha SHA-256 eb2953df...cab37, diverso dal FROZEN atteso f1d87245...97ef3.

Due copie indipendenti preservate coincidono con l'hash FROZEN atteso; quindi l'artifact non è perso. Nessuna copia FROZEN è stata sovrascritta. Il problema è stato registrato come ISS-0014 = OPEN.

## 6. Artifact creati

Repository / branch chat-3.10-light-heavy-routing-demand:
- docs/FASE_3_LIGHT_HEAVY_BASELINE_VALIDATION_REVIEW_v01.md;
- docs/FASE_3_LIGHT_HEAVY_SOURCE_MATRIX_v01.csv;
- docs/HANDOFF_CHAT_3.10_LIGHT_HEAVY_BASELINES_v01.md.

Nessun nuovo dataset pesante è stato duplicato nel namespace OneDrive 5 HUB.

Primo commit artifact:
- 14df41041dccc7801002d70075d5e8fd320350db — docs(f3): validate light heavy routing demand baselines.

## 7. PROJECT_CONTROL_REGISTER

DATA_REGISTRY aggiornato con sei record in stato REVIEW:
- F3_SRC_LIGHT_OSM_GRAPH_001;
- F3_SRC_LIGHT_GAMMA_001;
- F3_SRC_LIGHT_OD_PATH_001;
- F3_SRC_LIGHT_DEMAND_001;
- F3_SRC_HEAVY_OD_001;
- F3_SRC_HEAVY_PATH_001.

ISSUES aggiornato:
- ISS-0004 resta OPEN; prossima azione aggiornata con proposta PROPOSE_RESOLVED_PROCEDURALLY e review Chat 0.2 richiesta;
- ISS-0014 creato OPEN per il mismatch della preservation copy G_OSM.

PROJECT_SOURCE_OF_TRUTH non modificato: nessuna nuova decisione metodologica sostanziale è stata approvata dalla Chat 3.10.

## 8. Controlli ed esito

PASS:
- Light CSV: 46.010 righe / 46.010 OD uniche; hash match; k=0,15 e identità numeriche verificate;
- Heavy ZIP: hash match; tre membri principali hash-match; 81.555 OD e 81.555 path; nessun path vuoto o distanza non positiva;
- manifest G_OSM, Gamma_OSM e OD_PATH_SYSTEM_OSM coerenti con i riferimenti FROZEN;
- separazione rete / domanda / path-flow / corridoio / accessibilità locale documentata;
- nessun artifact FROZEN modificato;
- nessuna Fase 4 aperta.

LIMITATION:
- una preservation copy G_OSM in TESI_BASELINE_SAFE è byte-difforme; due copie hash-corrette sono disponibili. Non tutti i membri multi-GB del package F57 sono stati ri-hashati nuovamente in questa chat; l'Artifact Register tesi li registra VERIFIED al 2026-09-17.

## 9. Problemi aperti

- ISS-0004: attende decisione Chat 0.2 / utente sulla risoluzione procedurale.
- ISS-0014: mismatch preservation copy G_OSM da investigare senza sovrascrivere artifact FROZEN.
- La verifica candidate-specifica di accessibilità Light/Heavy resta futura e distinta dalla baseline macro.

## 10. Stato finale e prossimo passo

Stato Chat 3.10: COMPLETED / REVIEW, technical gate PASS WITH LIMITATIONS.

Prossimo passo raccomandato per Chat 0.2:
1. review degli artifact Chat 3.10;
2. decidere se portare ISS-0004 a RESOLVED proceduralmente;
3. se approvato, formalizzare che la pianificazione macro riusa le baseline Light/Heavy esistenti e che l'accessibilità locale dei candidati/finalisti resta verifica successiva obbligatoria;
4. mantenere ISS-0014 separato come issue di preservation e non come blocker metodologico della rete.

La Chat 3.10 si ferma qui e non apre la Fase 4.

## 11. SESSION CLOSE — change-driven

NOTEBOOK_CHANGE = NO

Motivo: nessun notebook è stato usato come fonte autorevole o modificato.

REGISTER_CHANGE = YES

Motivo: DATA_REGISTRY ha ricevuto sei riferimenti Light/Heavy in stato REVIEW; ISS-0004 è stato aggiornato senza cambiarne lo stato OPEN; ISS-0014 è stato creato OPEN per il mismatch di preservation.

GIT_COMMIT_REQUIRED = YES

Motivo: review, source matrix e handoff sono artifact leggeri versionabili. Commit eseguiti durante la chiusura: 14df41041dccc7801002d70075d5e8fd320350db e ef37b29f51b9759d43cebd2b7db270cb34ae0803.

PROJECT_SOURCE_OF_TRUTH_CHANGE = NO

Motivo: Chat 3.10 formula una raccomandazione tecnica ma non approva autonomamente la risoluzione di ISS-0004 o nuove decisioni metodologiche sostanziali.

Artifact check:
- nessun artifact tesi FROZEN modificato;
- nessun dataset pesante duplicato nel 5 HUB;
- registry live verificato dopo la scrittura;
- branch dedicata pulita dopo i commit;
- review e source matrix conservate in Git;
- Fase 4 non aperta.

Build notebook: N/A.
