# HANDOFF — Chat 0.3 — Re-baseline strategica e semplificazione metodologica v01

**Chat:** 0.3 — Re-baseline strategica e semplificazione metodologica
**Mandante:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Branch:** chat-0.3-strategic-rebaseline
**Worktree:** C:\dev\5-hub\_worktrees\chat-0.3-strategic-rebaseline
**Stato proposto:** PASS / READY FOR CHAT 0.2 + USER REVIEW
**Fase 4 / V2-1:** NON APERTA

## 1. Obiettivo

Ridisegnare baseline metodologica e roadmap dopo DEC-0061, preservando storia e decisioni precedenti e separando il modello GIS multicriterio strategico dalla futura due diligence dei siti.

Il risultato proposto è una configurazione di cinque poligoni territorialmente preferibile secondo il modello approvato; non è una certificazione di disponibilità, autorizzabilità, connessione o cantierabilità.

## 2. Materiali letti e verificati

- dispatch ufficiale Chat 0.3;
- istruzioni persistenti e README_PROJECT_ARCHITECTURE;
- PROJECT_SOURCE_OF_TRUTH vivo su Google Drive;
- PROJECT_CONTROL_REGISTER vivo: DECISIONS, DATA_REGISTRY, ISSUES;
- tutte le 61 DEC fino a DEC-0061 e tutte le 14 ISS;
- ROADMAP_METODOLOGICA_v1;
- FASE_1_HUB_DEFINITION_CONSOLIDATED_v02 — FROZEN;
- FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01 — FROZEN;
- Chat 3.1 inventario dati e Chat 3.2/3.8/3.9 urbanistica;
- Chat 3.3 e Chat 3.7 rete/TEN-T;
- Chat 3.4 ambiente, Chat 3.5 energia, Chat 3.10 Light/Heavy, Chat 3.11 PGRA/PAI;
- Chat 3.12 Natura 2000, inclusi review e handoff letti dal worktree principale senza modificarlo;
- RELATION_ARCHITECTURE_v01 e REVIEW_CHAT_90.0_RELATION_BUILDER_v01.
## 3. Lavoro svolto

Il model contract PROPOSED:
- conferma scala di pianificazione strategica e poligono come unità;
- separa score individuale e qualità della cinquina;
- rende centrale HARD / SOFT / FLAG;
- esplicita ruoli proposti per urbanistica, mobilità, energia, PGRA, PAI, PPR, Natura 2000, aree protette, biotopi e prati stabili;
- non approva indicatori, formule, soglie, normalizzazione, pesi, score o funzione obiettivo.

La roadmap v2 è stata riscritta in 10 stadi V2-0…V2-9. Ogni stadio contiene esplicitamente obiettivo, input, output, decisioni necessarie, quality gate e artifact persistente.

La impact matrix contiene 281 elementi:
- 16 fasi roadmap v1;
- 12 subfasi/chat;
- 61 DEC;
- 14 ISS;
- 31 dataset;
- 103 artifact del worktree 0.3;
- 15 branch artifact aggiuntivi;
- 9 requisiti;
- 9 controlli;
- 11 future attività.

La issue disposition copre ISS-0001…ISS-0014. La decision queue contiene 10 sole decisioni materialmente rilevanti.

È stato inoltre creato il successore Fase 1 PROPOSED, senza toccare la v02 FROZEN:
FASE_1_HUB_DEFINITION_REBASELINED_v03_PROPOSED.md.

## 4. Principali semplificazioni proposte

Fuori dal core: proprietà/catasto/disponibilità commerciale, verifica urbanistica definitiva del finalista, progettazione/accesso locale, capacità/punto/costo reale di connessione, VINCA/autorizzazioni/deroghe formali, verifica PAI/PPR sito-specifica, layout e cantierabilità.

Restano core: mobilità Light/Heavy macro, TEN-T e rete principale, proxy elettrico territoriale, urbanistica utile a generare/classificare poligoni, territorio e ambiente proporzionati alla scala strategica, robustezza e selezione della configurazione di cinque.
## 5. Elementi mantenuti, storici e post-model

**KEEP:** F1-D1…F1-D7 nel loro nucleo funzionale; Fase 2 FROZEN; baseline Light/Heavy; TEN-T; proxy elettrico; fonti ambientali/territoriali validate; governance e requisiti di riproducibilità.

**HISTORICAL_SUPPORT:** roadmap v1 dopo eventuale approvazione v2; baseline Claude/QGIS; audit superati da baseline successive; vecchi blocker che documentano lineage e limiti.

**DEFER_POST_MODEL:** proprietà/disponibilità, verifica urbanistica puntuale, accessi locali, connessione reale, autorizzazioni/VINCA/deroghe, due diligence PAI/PPR, layout e cantierabilità.

## 6. Stato proposto Roadmap v1 e Fasi 1–3

- Roadmap v1: SUPERSEDED_PROPOSED / HISTORICAL_BASELINE; nessuna cancellazione o riscrittura retroattiva.
- Fase 1: F1-D1…F1-D7 KEEP; v02 resta FROZEN; v03 re-baselined PROPOSED creata.
- Fase 2: KEEP / FROZEN; nessun successore necessario.
- Fase 3: PROPOSED PASS / CLOSED WITH DECLARED LIMITATIONS solo dopo approvazione della re-baseline, disposizione ISS-0009/ISS-0013 e integrazione governata Chat 3.12 se approvata.

## 7. DEC che richiedono disposizione o successor decision

- DEC-0016: roadmap v1 → supersessione proposta dalla v2.
- DEC-0013/Fase 1 v02: storico FROZEN preservato; nuovo successore v03 richiede approvazione.
- DEC-0032: SIMPLIFY come principio di gerarchia/lineage; non richiede audit region-wide completo come prerequisito.
- DEC-0033: successor per spostare proprietà/disponibilità commerciale post-model.
- DEC-0042: successor/clarification per mantenere DEROGA_REQUIRED ma rinviare verifiche finali e non pre-approvare una penalizzazione.
- DEC-0048: successor per mantenere il flag currentness e spostare la verifica urbanistica definitiva post-model.
- DEC-0050 + DEC-0053: proxy KEEP; successor/clarification per MW/punto/costo/studio reale post-model.
- DEC-0055: successor per LOCAL_ROAD_ACCESS_CHECK come flag/post-model, mantenendo le baseline macro.
- DEC-0058: fallback PAI KEEP; pointwise finalista post-model salvo futura regola hard approvata.
- DEC-0060: workstream editoriale KEEP; RELATION_ARCHITECTURE_v02 da produrre dopo approvazione.
- DEC-0061: KEEP, principio fondante della v2.
## 8. Disposizione proposta delle issue

- ISS-0002: PROPOSE_RESOLVED_AS_HISTORICAL.
- ISS-0009: PROPOSE_CLOSED_OUT_OF_SCOPE_CORE / DEFER_POST_MODEL.
- ISS-0013: PROPOSE_RESOLVED_PROCEDURALLY; rule-set 3.12 classificato come support/flag con limitazioni.
- ISS-0004, 0007, 0010, 0011 e 0012: restano RESOLVED ma il relativo obbligo puntuale viene riclassificato tramite successor decision dove necessario.
- Le altre issue mantengono lo stato corrente e il ruolo indicato nella issue disposition.

## 9. Decision queue futura ordinata

1. DQ-01 — universo dei poligoni e prefiltri indispensabili.
2. DQ-02 — variabili e ruolo HARD / SOFT / FLAG.
3. DQ-03 — costruzione degli indicatori raw.
4. DQ-04 — trasformazioni e normalizzazione.
5. DQ-05 — metodo e valori dei pesi.
6. DQ-06 — formula dello score individuale.
7. DQ-07 — qualità/funzione della configurazione di cinque.
8. DQ-08 — vincoli di configurazione.
9. DQ-09 — algoritmo/procedura di selezione.
10. DQ-10 — piano di sensitivity/robustness.

Nessuna voce della queue è approvata dalla Chat 0.3.

## 10. File creati/modificati

Deliverable obbligatori:
- docs/PROJECT_MODEL_CONTRACT_REBASELINE_v01_PROPOSED.md
- docs/ROADMAP_METODOLOGICA_v2_PROPOSED.md
- docs/REBASELINE_IMPACT_MATRIX_v01.csv
- docs/REBASELINE_ISSUE_DISPOSITION_v01.csv
- docs/REBASELINE_DECISION_QUEUE_v01.md
- docs/REBASELINE_EDITORIAL_IMPACT_CHAT90_v01.md
- docs/HANDOFF_CHAT_0.3_STRATEGIC_REBASELINE_v01.md

Artifact aggiuntivo necessario:
- docs/FASE_1_HUB_DEFINITION_REBASELINED_v03_PROPOSED.md
## 11. Git e commit

Commit già presenti e preservati:
- 28df1d0 — docs(rebaseline): propose strategic multicriteria model v2
- 31ede79 — docs(rebaseline): add Chat 0.3 handoff

Commit di revisione sostanziale:
- 8f51d87 — docs(rebaseline): strengthen strategic audit and phase contracts

Il presente handoff è committato separatamente alla chiusura. Nessun merge su main è eseguito dalla Chat 0.3. Il branch Chat 3.12 e gli altri worktree non sono modificati.

## 12. Quality gate

- DEC-0061 integralmente rispettata: PASS.
- Audit senza cancellazioni implicite: PASS.
- Core model separato dalla fattibilità/due diligence: PASS.
- Roadmap v2 significativamente più semplice della v1: PASS.
- Proprietà/catasto/disponibilità commerciale fuori dal core: PASS PROPOSED.
- Capacità elettrica reale fuori dal requisito macro: PASS PROPOSED.
- Verifiche autorizzative puntuali non confuse con scoring: PASS.
- Mobilità Light/Heavy centrale: PASS.
- Energia come proxy territoriale centrale: PASS.
- Ambiente proporzionato alla scala macro: PASS.
- Unità di analisi = poligono: PASS.
- Scoring/pesi/formula cinquina non approvati implicitamente: PASS.
- Decision queue breve e materialmente rilevante: PASS, 10 voci.
- Impatto Chat 90.0 esplicito: PASS.
- Impact matrix: PASS, 281 righe e tutte le categorie richieste.
- Issue disposition: PASS, 14/14.
- F1/F2 FROZEN originali non modificati: PASS.
- Fase 4/V2-1 non aperta: PASS.
- git diff --check: PASS al gate di chiusura.
- branch pulito e pushato: PASS al gate di chiusura.

## 13. Problemi aperti e limiti

Le proposte non sono state scritte nella governance viva perché richiedono approvazione utente. ISS-0013 resta ufficialmente OPEN; il branch 3.12 resta separato. Nessuna decisione futura della queue è stata risolta.

## 14. Prossimo passo minimo

**Chat 0.2 sottopone all'utente un unico pacchetto di approvazione della re-baseline e delle successor decisions sostanziali.**

Solo dopo tale approvazione può essere valutata l'apertura di V2-1 / Fase 4.

STOP — nessun candidato, indicatore, peso, score o algoritmo è stato implementato.
