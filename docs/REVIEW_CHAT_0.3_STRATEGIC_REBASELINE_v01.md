# REVIEW — Chat 0.3 — Re-baseline strategica e semplificazione metodologica

**Reviewer:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Stato:** TECHNICAL PASS / USER APPROVAL REQUIRED
**Autorità:** DEC-0061 ACCEPTED

## 1. Esito

La review indipendente della Chat 0.3 è positiva.

La proposta traduce correttamente DEC-0061 in una nuova architettura metodologica strategica e multicriterio, separando il core model dalla due diligence proprietaria, catastale, autorizzativa, elettrica e progettuale.

Non sono stati approvati implicitamente indicatori, soglie, normalizzazione, pesi, score, funzione obiettivo, vincoli della cinquina o algoritmo.

## 2. Controlli indipendenti

Verificati branch, deliverable, Git e struttura degli artifact.

- branch: chat-0.3-strategic-rebaseline;
- HEAD specialistico originario: 3fccc4e;
- working tree specialistico inizialmente pulito;
- git diff --check iniziale: PASS;
- 8 artifact principali presenti, inclusa Fase 1 v03 PROPOSED;
- roadmap v2: 10 stadi V2-0...V2-9;
- decision queue: 10 decisioni sostanziali DQ-01...DQ-10;
- impact matrix: 281 righe;
- decisioni censite: 61/61, univoche;
- issue censite: 14/14, univoche;
- dataset censiti: 31;
- subfasi/chat censite: 12;
- nessuna modifica retroattiva alle baseline FROZEN.

La matrice classifica gli elementi in KEEP, SIMPLIFY, DEFER_POST_MODEL, HISTORICAL_SUPPORT e SUPERSEDE_PROPOSED.

## 3. Correzioni applicate durante la review

Sono stati rilevati e corretti esclusivamente difetti formali/strutturali, senza modificare la sostanza metodologica:

- una sequenza letterale \n in ROADMAP_METODOLOGICA_v2_PROPOSED.md;
- due heading Markdown attaccati al paragrafo precedente in FASE_1_HUB_DEFINITION_REBASELINED_v03_PROPOSED.md;
- una riga CTRL-PAI-POINT della impact matrix con slittamento di colonne.

La riga CTRL-PAI-POINT è stata normalizzata come:
- disposizione: DEFER_POST_MODEL;
- ruolo v2: post_model_pai_check;
- user approval required: YES;
- successor: DEC-0058.

## 4. Valutazione metodologica
Il PROJECT_MODEL_CONTRACT_REBASELINE è coerente con DEC-0061 e può diventare la baseline concettuale del MODEL_v2 previa approvazione utente.

La Fase 2 resta coerente e non necessita di successore.

La Fase 1 necessita del successore v03 perché la v02 FROZEN contiene formulazioni che possono essere lette come gate di fattibilità del singolo lotto. Il successore preserva F1-D1...F1-D7 e separa funzione dell'Hub da due diligence del terreno.

La roadmap v2 è sostanzialmente più snella e mantiene una sequenza metodologicamente corretta: universo candidati, contratto criteri, raw indicators, normalizzazione, pesi/score, contratto cinquina, selezione, robustness, freeze/relazione.

La decision queue è adeguatamente corta e non anticipa le scelte che devono essere sottoposte all'utente.

## 5. Successor dispositions supportate dalla review

La review supporta la proposta di:
- spostare proprietà/disponibilità commerciale fuori dal core;
- mantenere la currentness urbanistica come informazione/flag e rinviare la verifica definitiva post-model;
- mantenere Light/Heavy macro nel core e rinviare l'accesso locale definitivo post-model;
- mantenere il proxy elettrico nel core e rinviare MW/punto/costo/studio reale post-model;
- mantenere PAI/PPR/Natura 2000 e altre tutele nel core solo nel ruolo che sarà approvato in DQ-02/DQ-03, senza mini-due-diligence obbligatoria;
- mantenere DEROGA_REQUIRED come flag senza penalizzazione pre-approvata;
- integrare Chat 3.12 come supporto/flag dopo decisione su ISS-0013.

## 6. Issue disposition supportata
La review supporta:
- ISS-0002 -> resolved as historical/non-authoritative baseline gap;
- ISS-0009 -> closed out of scope core / deferred post-model;
- ISS-0013 -> resolved procedurally, con rule-set Natura 2000 come support/flag e nessun VINCA_PASSED;
- ISS già RESOLVED -> stato invariato, con riclassificazione degli obblighi puntuali dove prevista dai successor clauses.

## 7. Stato delle roadmap e fasi

Proposta supportata:
- ROADMAP_METODOLOGICA_v1 -> DEPRECATED come roadmap operativa, preservata come historical baseline;
- ROADMAP_METODOLOGICA_v2 -> nuova roadmap operativa dopo approvazione;
- Fase 1 v02 -> FROZEN historical predecessor;
- Fase 1 v03 -> nuovo successore attivo dopo approvazione;
- Fase 2 -> KEEP / FROZEN;
- Fase 3 -> PASS / CLOSED WITH DECLARED LIMITATIONS dopo governance di ISS-0009, ISS-0013 e integrazione della Chat 3.12.

## 8. Decisione utente richiesta

La review tecnica è PASS.

Resta necessaria approvazione esplicita dell'utente per il pacchetto di re-baseline, le successor dispositions e le chiusure di issue sopra descritte.

Nessuna DQ-01...DQ-10 è approvata da questa review.

Fase 4 / V2-1 resta chiusa fino all'approvazione del pacchetto.
