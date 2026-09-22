# CONFIGURATION OBJECTIVE ARCHITECTURE v01

**Data:** 2026-09-22
**Stato:** ACCEPTED
**Autorità:** DEC-0086

## 1. Principio

Il MODEL_v2 resta un problema **single-objective**.

I criteri site-level vengono prima aggregati sulla cinquina mediante media dei cinque Hub. La copertura territoriale è invece un criterio calcolato direttamente sulla configurazione. Tutti i criteri entrano una sola volta nella ponderazione finale.

Non viene introdotto un secondo obiettivo autonomo e non è richiesto un fronte di Pareto.

## 2. Aggregazione dei criteri site-level

Per ogni criterio site-level `j` e per una cinquina `H` di cinque Hub:

`Z_j(H) = (1/5) * sum_{i in H} z_ij`

dove `z_ij` è lo score normalizzato del candidato `i` per il criterio `j`.

Esempi di criteri site-level attualmente ammessi:
- LIGHT;
- HEAVY;
- GRID;
- LOG;
- PGRA;
- H2.

## 3. Copertura territoriale

La copertura territoriale è un criterio di configurazione e produce:

`Z_COV(H)`

con scala normalizzata da definire separatamente.

La formula raw della copertura e il relativo metodo di normalizzazione non sono ancora approvati da DEC-0086.

## 4. Funzione obiettivo finale

Quando saranno assegnate le importanze `r_j` e `r_COV`, la funzione obiettivo è:

`Q(H) = [sum_j r_j * Z_j(H) + r_COV * Z_COV(H)] / [sum_j r_j + r_COV]`

equivalente a una media ponderata con pesi normalizzati.

Ogni criterio entra una sola volta nella ponderazione finale.

Non si deve:
- calcolare prima uno score candidato pesato e poi ripesarlo con la copertura;
- trattare copertura e qualità MCDA come due obiettivi separati;
- introdurre automaticamente un fronte di Pareto.

## 5. Decisioni ancora sospese

- valori concreti di importanza 1–5;
- formula raw della copertura territoriale;
- normalizzazione di `Z_COV(H)`;
- eventuale trattamento finale del requisito storico di distanza minima 10 km tra Hub.

## 6. Relazione con AFIR

I vincoli AFIR/TEN-T restano separati dalla funzione obiettivo e operano come configuration constraints / quality gate secondo le decisioni già approvate e le future formalizzazioni.
