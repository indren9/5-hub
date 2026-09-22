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

La copertura territoriale è un criterio di configurazione e produce `Z_COV(H)`.

Con DEC-0087, su una griglia regolare del FVG, per ogni cella `g` con centro `c_g` si calcola:

`d_g(H) = min_{h∈H} d(c_g,h)`

dove `d` è la distanza geometrica minima euclidea, in CRS metrico, tra il centro della cella e il poligono Hub.

Le celle di confine sono pesate per la sola area `a_g` ricadente nel FVG:

`D_COV(H) = Σ_g a_g d_g(H) / Σ_g a_g`.

Il benchmark geografico è:

`D_COV* = min_{|H|=5} D_COV(H)`

sull'universo candidati.

Lo score normalizzato è:

`Z_COV(H) = D_COV* / D_COV(H)`.

La dimensione operativa della griglia resta un parametro tecnico da definire con verifica di convergenza/sensitivity.

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
- dimensione operativa della griglia, da fissare con verifica di convergenza/sensitivity.

Con DEC-0087 formula raw e normalizzazione di `Z_COV(H)` sono ACCEPTED. Con DEC-0088 la soglia storica minima di 10 km tra Hub è eliminata dal MODEL_v2.

## 6. Relazione con AFIR

I vincoli AFIR/TEN-T restano separati dalla funzione obiettivo e operano come configuration constraints / quality gate secondo le decisioni già approvate e le future formalizzazioni.
