# ROADMAP METODOLOGICA v2 — PROPOSED

**Chat:** 0.3 — Re-baseline strategica e semplificazione metodologica
**Data:** 2026-09-21
**Stato:** PROPOSED — richiede approvazione esplicita dell'utente
**Autorità:** DEC-0061 ACCEPTED
**Vincolo:** questa roadmap non apre la Fase 4 né alcuna fase v2.

## 1. Principio di semplificazione

La v2 conserva: poligono come unità di analisi, tracciabilità dei dati, distinzione hard/soft/flag, qualità individuale distinta dalla qualità della configurazione, selezione esplicita di esattamente cinque Hub, sensitivity/robustness e freeze riproducibile.

Escono dal core: proprietà/catasto/disponibilità commerciale, progettazione dell'accesso locale, capacità/punto/costo reale di connessione elettrica, verifica autorizzativa completa e due diligence puntuale finale.

Le verifiche post-model possono essere raccomandate, ma non sono condizioni per chiudere il modello strategico.

## 2. Prerequisiti già acquisiti

- Fase 0: infrastruttura e governance — acquisita.
- Fase 1: definizione funzionale Hub — FROZEN; successore re-baselined proposto.
- Fase 2: unità di analisi — FROZEN e compatibile.
- Fase 3: fonti/dati validate da riusare secondo il ruolo assegnato dalla re-baseline.
- DEC-0061: principio guida vincolante.

## 3. Sequenza v2 proposta

### V2-0 — Approvazione della re-baseline
**Obiettivo:** rendere operativo il nuovo model contract e chiudere la transizione documentale dalla v1.
**Input:** DEC-0061, Fasi 1–3, registri vivi, deliverable Chat 0.3.
**Output:** baseline metodologica v2 approvata e disposizioni su DEC/ISS formalizzate.
**Decisioni necessarie:** approvazione utente di model contract, roadmap e successor decisions sostanziali.
**Quality gate:** nessun conflitto implicito con ACCEPTED/FROZEN; nessuna decisione futura pre-approvata.
**Artifact persistente:** PROJECT_MODEL_CONTRACT_REBASELINE + ROADMAP_METODOLOGICA_v2 + governance aggiornata dalla Chat Madre.

### V2-1 — Universo dei poligoni candidati
**Obiettivo:** costruire alternative territoriali tracciabili coerenti con la scala strategica.
**Input:** Fase 2 FROZEN; baseline urbanistiche/territoriali validate; decisione DQ-01.
**Output:** universo dei poligoni con lineage, ID/versione e QA; nessun punteggio.
**Decisioni necessarie:** fonti/categorie generatrici, eventuale superficie minima, soli prefiltri hard indispensabili.
**Quality gate:** ogni poligono ricostruibile; proxy/currentness dichiarati; proprietà commerciale non richiesta.
**Artifact persistente:** CANDIDATE_UNIVERSE_v01 + CANDIDATE_LINEAGE_v01 + QA.

### V2-2 — Contratto di criteri e indicatori
**Obiettivo:** definire cosa misura il modello e il ruolo HARD / SOFT / FLAG di ogni variabile.
**Input:** universo candidato, dataset Fase 3 accettati, model contract, decisioni DQ-02 e DQ-03.
**Output:** dizionario dei criteri con formula raw proposta, geometria, unità, direzione, missing e ruolo.
**Decisioni necessarie:** variabili ammesse; hard constraints; indicatori soft; flag; formule raw sostanziali.
**Quality gate:** ogni variabile risponde a una domanda decisionale; nessun dato entra solo perché disponibile; nessun hard filter implicito.
**Artifact persistente:** CRITERIA_INDICATOR_CONTRACT_v01.

### V2-3 — Calcolo raw e QA
**Obiettivo:** calcolare valori osservati degli indicatori senza ancora applicare preferenze/pesi.
**Input:** CANDIDATE_UNIVERSE_v01 e CRITERIA_INDICATOR_CONTRACT_v01 approvati.
**Output:** tabella raw completa con missing/errori espliciti e diagnostica discriminante.
**Decisioni necessarie:** solo eventuali eccezioni metodologiche emerse dal QA; nessuna nuova scelta implicita.
**Quality gate:** formule riproducibili; unità coerenti; join/overlay verificati; missing non trasformati arbitrariamente.
**Artifact persistente:** INDICATOR_RAW_TABLE_v01 + INDICATOR_QA_REPORT_v01.
### V2-4 — Trasformazioni e normalizzazione
**Obiettivo:** rendere confrontabili gli indicatori soft con regole trasparenti.
**Input:** valori raw verificati e decisione DQ-04.
**Output:** valori trasformati/normalizzati e configurazione completa.
**Decisioni necessarie:** funzioni di preferenza, normalizzazione, trattamento estremi/missing quando materialmente rilevante.
**Quality gate:** trasformazioni ricostruibili; nessuna dipendenza occulta dal campione; test numerici su casi noti.
**Artifact persistente:** TRANSFORMATION_NORMALIZATION_CONFIG_v01 + NORMALIZED_INDICATORS_v01.

### V2-5 — Pesi e score individuale
**Obiettivo:** definire e calcolare l'idoneità individuale dei poligoni.
**Input:** indicatori normalizzati; decisioni DQ-05 e DQ-06.
**Output:** score individuale con contributi elementari tracciabili.
**Decisioni necessarie:** metodo/valori dei pesi e formula di aggregazione individuale.
**Quality gate:** score ricostruibile; contributi disponibili; nessuna confusione fra ranking individuale e cinquina.
**Artifact persistente:** WEIGHT_CONFIG_v01 + SITE_SCORE_CONFIG_v01 + SITE_SUITABILITY_v01.

### V2-6 — Contratto della configurazione di cinque Hub
**Obiettivo:** definire cosa rende preferibile una cinquina oltre agli score dei singoli poligoni.
**Input:** SITE_SUITABILITY_v01; DEC-0061; decisioni DQ-07 e DQ-08.
**Output:** funzione di qualità della configurazione e vincoli di configurazione formalizzati.
**Decisioni necessarie:** aggregazione della cinquina; eventuali coperture, distanze, equilibrio territoriale, TEN-T o altre relazioni.
**Quality gate:** cardinalità = 5; funzione e vincoli espliciti; nessun vincolo provinciale/diversificazione implicito.
**Artifact persistente:** FIVE_HUB_CONFIGURATION_CONTRACT_v01.

### V2-7 — Selezione / ottimizzazione
**Obiettivo:** individuare la configurazione conforme al contratto approvato.
**Input:** universo ammissibile, score individuali e configuration contract.
**Output:** soluzione selezionata, alternative rilevanti e manifest di esecuzione.
**Decisioni necessarie:** procedura/algoritmo e criterio di ottimalità/stop, DQ-09.
**Quality gate:** soluzione riproducibile; verifica indipendente del valore obiettivo/vincoli; nessuna proclamazione di fattibilità immobiliare.
**Artifact persistente:** FIVE_HUB_SOLUTION_v01 + SELECTION_METHOD_v01 + SELECTION_RUN_MANIFEST_v01.
### V2-8 — Sensitivity e robustness
**Obiettivo:** quantificare la dipendenza della cinquina dalle assunzioni sostanziali.
**Input:** modello selettivo completo e decisione DQ-10 sul piano di sensitivity.
**Output:** scenari, frequenze di selezione, alternative ricorrenti e driver di instabilità.
**Decisioni necessarie:** assunzioni da variare, range/scenari e metriche di robustezza.
**Quality gate:** robustezza supportata da numeri; scenario base separato dagli stress test.
**Artifact persistente:** ROBUSTNESS_PLAN_v01 + ROBUSTNESS_REPORT_v01.

### V2-9 — Freeze, risultati e relazione
**Obiettivo:** congelare il modello riproducibile e trasferire i risultati alla relazione esterna.
**Input:** output V2-1…V2-8 verificati, registri aggiornati, codice/config/test.
**Output:** baseline MODEL_v2_FROZEN, package risultati e input editoriali.
**Decisioni necessarie:** approvazione utente del freeze; nessuna nuova metodologia introdotta in fase editoriale.
**Quality gate:** input/versioni/codice/config/commit ricostruibili; issue core non bloccanti; relazione coerente con il model contract.
**Artifact persistente:** MODEL_v2_FROZEN + RESULT_PACKAGE_v01 + handoff finale + aggiornamento Chat 90.0.

## 4. Approfondimenti post-model

Non costituiscono una fase necessaria per chiudere MODEL_v2:
- verifica catastale/proprietaria/commerciale;
- verifica urbanistica puntuale del finalista;
- progettazione e autorizzazione dell'accesso locale;
- capacità MW, punto/costo e studio reale di connessione;
- VINCA/autorizzazioni/deroghe formali;
- PAI/PPR e altre verifiche sito-specifiche di due diligence;
- layout, sicurezza esecutiva e cantierabilità.

Possono essere svolti successivamente sui poligoni selezionati prima di investimento/progettazione.

## 5. Stato proposto della roadmap v1
ROADMAP_METODOLOGICA_v1.md → **SUPERSEDED_PROPOSED / HISTORICAL_BASELINE**.

Non viene cancellata né riscritta. Solo dopo approvazione esplicita della v2 la Chat Madre potrà registrarla come DEPRECATED/SUPERSEDED, preservando storia e commit.

## 6. Stato proposto delle Fasi 1–3

- **Fase 1:** nucleo funzionale F1-D1…F1-D7 KEEP; v02 resta FROZEN; necessario un successore proposto per separare requisiti funzionali da due diligence puntuale.
- **Fase 2:** KEEP / FROZEN; nessun successore necessario.
- **Fase 3:** **PROPOSED PASS / CLOSED WITH DECLARED LIMITATIONS**, subordinato all'approvazione della re-baseline, alla disposizione di ISS-0009 e ISS-0013 e alla normale integrazione degli artifact Chat 3.12. I gap diventati post-model non restano blocker del core.

## 7. Regola trasversale

Ogni fase futura deve: identificare input/versioni; distinguere dato/proxy/assunzione; applicare HARD/SOFT/FLAG solo come approvato; salvare artifact; eseguire QA/test; aggiornare registri quando dovuto; superare git diff --check; lasciare commit e handoff.

## 8. Prossimo passo minimo

**Review della Chat 0.2 e approvazione esplicita dell'utente della re-baseline.**

Non aprire V2-1 / Fase 4 prima di tale approvazione.
