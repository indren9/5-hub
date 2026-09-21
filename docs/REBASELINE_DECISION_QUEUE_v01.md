# REBASELINE DECISION QUEUE v01

**Stato:** PROPOSED — nessuna voce è approvata da questo documento.
**Criterio di inclusione:** solo decisioni che possono cambiare materialmente universo, punteggi o cinquina finale.

| Ordine | Decisione | Perché può cambiare il risultato | Output che la congela |
|---|---|---|---|
| DQ-01 | Come si costruisce l'universo dei poligoni: fonti/categorie, eventuale superficie minima e soli prefiltri indispensabili | Cambia direttamente le alternative disponibili | CANDIDATE_UNIVERSE_CONTRACT_v01 |
| DQ-02 | Quali variabili entrano nel modello e quali sono HARD, SOFT o FLAG | Decide cosa può escludere, premiare o soltanto segnalare | CRITERIA_INDICATOR_CONTRACT_v01 |
| DQ-03 | Trasformazioni e normalizzazione degli indicatori soft | Cambia comparabilità e forma delle preferenze | TRANSFORMATION_NORMALIZATION_CONFIG_v01 |
| DQ-04 | Metodo di assegnazione dei pesi e valori dei pesi | Cambia l'importanza relativa dei domini | WEIGHT_CONFIG_v01 |
| DQ-05 | Formula di aggregazione dello score individuale | Cambia il ranking dei poligoni anche a pesi invariati | SITE_SCORE_CONFIG_v01 |
| DQ-06 | Definizione della qualità della configurazione di 5 Hub | Determina cosa si ottimizza a livello di cinquina | FIVE_HUB_CONFIGURATION_CONTRACT_v01 |
| DQ-07 | Vincoli di configurazione: eventuale copertura, distanza, equilibrio/province/TEN-T | Può rendere ammissibili o inammissibili intere cinquine | FIVE_HUB_CONFIGURATION_CONTRACT_v01 |
| DQ-08 | Procedura/algoritmo di selezione e criterio di ottimalità/stop | Determina come si esplora e verifica lo spazio delle cinquine | SELECTION_METHOD_v01 |
| DQ-09 | Piano di sensitivity/robustness: assunzioni da variare e range/scenari | Determina quanto è forte l'evidenza di robustezza | ROBUSTNESS_PLAN_v01 |

## Non riportare all'utente salvo nuova evidenza

Naming, logging, formato manifest, librerie software equivalenti, procedure Git già governate, metriche QA puramente tecniche, conservazione di artifact storici e dettagli editoriali che non cambiano il significato scientifico.

## Guardrail

La queue non pre-decide indicatori, soglie, pesi, normalizzazione, penalizzazioni ambientali, vincoli provinciali, diversificazione geografica, aggregazione della cinquina o algoritmo.

Le disposizioni su decisioni ACCEPTED incompatibili con DEC-0061 devono essere approvate prima di DQ-01.
