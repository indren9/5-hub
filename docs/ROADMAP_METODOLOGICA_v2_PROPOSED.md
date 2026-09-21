# ROADMAP METODOLOGICA v2 — PROPOSED

**Chat:** 0.3 — Re-baseline strategica e semplificazione metodologica
**Data:** 2026-09-21
**Stato:** PROPOSED
**Vincolo:** DEC-0061 ACCEPTED

Questa roadmap non apre alcuna nuova fase operativa. L'avvio della prima fase futura richiede decisione separata della Chat 0.2 / utente.

## 1. Principio di semplificazione

La v2 conserva poligono come unità di analisi, tracciabilità dati, distinzione tra ammissibilità e merito, score individuale distinto dalla configurazione, sensibilità/robustezza e freeze riproducibile.

La v2 elimina dal core due diligence proprietaria/catastale, verifica commerciale dei terreni, progettazione dell'accesso locale, capacità e connessione elettrica reali, verifica autorizzativa completa e verifica puntuale finale come fase obbligatoria.

## 2. Prerequisiti già acquisiti

Non vengono riaperte automaticamente Fase 0, Fase 1, Fase 2 e il lavoro Fase 3 validato e utile alla nuova scala.

La re-baseline deve stabilire formalmente quali elementi di Fase 3 diventano baseline dati del modello e quali restano supporto/post-model.

## 3. Sequenza v2 proposta

### V2-0 — Approvazione della re-baseline

**Obiettivo:** rendere operativo il nuovo model contract e le disposizioni su DEC/ISS/dati.
**Output:** model contract ACCEPTED, roadmap v2 ACCEPTED, aggiornamenti governance approvati.
**Gate:** nessun conflitto non dichiarato con FROZEN/ACCEPTED; decision queue esplicita.
**Decisione utente:** sì.

### V2-1 — Universo dei poligoni candidati

**Obiettivo:** costruire un universo tracciabile di alternative territoriali coerenti con la scala strategica.
**Attività minime:** fonti dei poligoni, regole di generazione, canonicalizzazione, split/merge, ID/versione, eventuali prefiltri indispensabili, gestione currentness/proxy.
**Output:** CANDIDATE_UNIVERSE_v01 + lineage + QA.
**Gate:** ogni poligono ricostruibile dalla fonte; nessun punteggio; nessuna disponibilità proprietaria richiesta.
**Decisioni sostanziali:** fonti/categorie generatrici, eventuale superficie minima, eventuali prefiltri hard.

### V2-2 — Contratto di criteri e indicatori

**Obiettivo:** definire cosa misura il modello e il ruolo di ogni variabile.
**Attività minime:** selezione indicatori, significato, fonte, geometria, unità, direzione, missing values, classificazione hard/soft/flag, ridondanza e capacità discriminante.
**Output:** CRITERIA_INDICATOR_CONTRACT_v01.
**Gate:** ogni indicatore risponde a una domanda decisionale; nessun criterio entra solo perché il dato esiste.
**Decisione utente:** sì.

### V2-3 — Misura grezza e QA degli indicatori

**Obiettivo:** calcolare i valori osservati senza ancora attribuire preferenze.
**Output:** INDICATOR_RAW_TABLE_v01 + INDICATOR_QA_REPORT_v01.
**Gate:** formule raw riproducibili, unità coerenti, errori/missing espliciti.

### V2-4 — Trasformazioni e normalizzazione

**Obiettivo:** rendere confrontabili le misure con regole trasparenti.
**Output:** TRANSFORMATION_NORMALIZATION_CONFIG_v01.
**Gate:** trasformazioni ricostruibili e motivate; nessuna dipendenza occulta dal campione.
**Decisione utente:** sì.

### V2-5 — Pesi e score individuale

**Obiettivo:** definire e calcolare la qualità individuale dei poligoni.
**Output:** SITE_SCORE_CONFIG_v01 + SITE_SUITABILITY_v01.
**Gate:** score completamente ricostruibile, contributi elementari disponibili, ranking non confuso con la cinquina.
**Decisione utente:** sì.

### V2-6 — Contratto della configurazione di cinque Hub

**Obiettivo:** definire cosa rende buona una cinquina oltre ai punteggi dei singoli siti.
**Attività minime:** qualità della configurazione, eventuale copertura/domanda, ridondanza/diversificazione, vincoli geografici o funzionali, cardinalità = 5.
**Output:** FIVE_HUB_CONFIGURATION_CONTRACT_v01.
**Gate:** funzione e vincoli espliciti; nessun vincolo provinciale o diversificazione introdotto implicitamente.
**Decisione utente:** sì.

### V2-7 — Selezione / ottimizzazione

**Obiettivo:** individuare la configurazione che soddisfa il contratto approvato.
**Output:** FIVE_HUB_SOLUTION_v01 + SELECTION_RUN_MANIFEST_v01.
**Gate:** soluzione riproducibile; chiaro perché la cinquina è selezionata; nessuna proclamazione di fattibilità immobiliare.

### V2-8 — Sensibilità e robustezza

**Obiettivo:** misurare quanto il risultato dipende dalle assunzioni sostanziali.
**Output:** ROBUSTNESS_REPORT_v01.
**Gate:** robustezza quantitativa; alternative ricorrenti e driver di instabilità identificati.
**Decisione utente:** approvazione del piano di sensitivity prima dell'esecuzione.

### V2-9 — Freeze, risultati e relazione

**Obiettivo:** congelare modello e output, quindi alimentare la relazione esterna.
**Output:** MODEL_v2_FROZEN, package risultati, input editoriali aggiornati.
**Gate:** dati/config/codice/commit ricostruibili; nessun blocker core aperto; relazione coerente con model contract.
**Decisione utente:** freeze finale.

## 4. Cosa scompare come fase core autonoma

**Fattibilità energetica di dettaglio:** non è più una fase autonoma. Il proxy energetico entra nei criteri se approvato; capacità, punto/costo di connessione e studio tecnico restano post-model.

**Verifica puntuale dei cinque siti:** non è più necessaria per chiudere il modello. Diventa POST-MODEL / DUE DILIGENCE.

**Confronto Claude:** non è necessario alla validità del modello. Resta confronto storico opzionale.

## 5. Quality gate trasversale

Ogni fase futura deve verificare input/versioni identificati, procedure riproducibili, nessun dato inventato, proxy dichiarati, hard/soft/flag distinti, artifact salvati, test/QA espliciti, git diff --check PASS, commit coerente, handoff e nessuna decisione sostanziale promossa senza approvazione utente.

## 6. Stato proposto della roadmap v1

ROADMAP_METODOLOGICA_v1.md → SUPERSEDED_PROPOSED / HISTORICAL SUPPORT.

Non viene cancellata né riscritta. Dopo approvazione esplicita della v2 dovrebbe essere marcata DEPRECATED / SUPERSEDED BY ROADMAP_METODOLOGICA_v2, preservando commit e storia.

## 7. Stato proposto delle Fasi 1–3

- **FASE 1:** contenuto funzionale KEEP; baseline v02 resta FROZEN come storico autorevole; proposto successore v03 per rimuovere dal core le implicazioni di due diligence puntuale senza cambiare F1-D1…F1-D7.
- **FASE 2:** KEEP / FROZEN; nessun successore necessario.
- **FASE 3:** proposta PASS / CLOSED WITH DECLARED LIMITATIONS dopo approvazione re-baseline, disposizione di ISS-0009, decisione su ISS-0013 e integrazione governata del lavoro Chat 3.12. I dataset non scelti come indicatori non devono restare blocker.

## 8. Prossimo passo minimo

Review Chat 0.2 + approvazione utente della re-baseline e delle sole disposizioni che modificano decisioni ACCEPTED.

Non aprire V2-1/Fase 4 prima di tale approvazione.
