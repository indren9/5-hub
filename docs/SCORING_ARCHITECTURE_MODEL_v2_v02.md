**Data:** 2026-09-22
**Stato:** ACCEPTED
**Autorità:** DEC-0070 + DEC-0086
**Predecessore:** `SCORING_ARCHITECTURE_MODEL_v2_v01.md` — preservato come baseline storica

# SCORING ARCHITECTURE MODEL_v2 v02

## 1. Principio generale

Il MODEL_v2 resta un problema **single-objective**.

Non viene introdotto un secondo obiettivo autonomo per la distribuzione territoriale e non è richiesto un fronte di Pareto.

I criteri site-level vengono aggregati sulla cinquina mediante media dei cinque Hub. I criteri propri della configurazione, come la copertura territoriale, vengono calcolati direttamente sulla cinquina. Tutti confluiscono una sola volta nella funzione obiettivo finale.

## 2. Importanza dei criteri

Per ogni criterio finale k verrà assegnata un'importanza intera:

`r_k ∈ {1,2,3,4,5}`

I valori concreti sono **SUSPENDED / non ancora approvati**.

Quando saranno assegnati, i pesi normalizzati saranno:

`w_k = r_k / Σ_k r_k`

con `Σ_k w_k = 1`.

## 3. Criteri site-level

Per ogni candidato i e criterio site-level j si indica con:

`z_ij`

lo score normalizzato del candidato per quel criterio.

Per una cinquina H di cinque Hub, il valore del criterio j è:

`Z_j(H) = (1/5) * Σ_{i∈H} z_ij`

Quindi prima si fa la media dei cinque Hub **criterio per criterio**.

## 4. Criteri configuration-level

Un criterio configuration-level non appartiene al singolo candidato e viene calcolato direttamente sulla cinquina.

Il criterio approvato in principio con DEC-0086 è la copertura territoriale:

`Z_COV(H)`

La formula raw e la normalizzazione specifica di `Z_COV(H)` restano da approvare separatamente.

## 5. Funzione obiettivo unica

La funzione obiettivo finale è una sola media ponderata dei criteri finali:

`Q(H) = [Σ_j r_j * Z_j(H) + r_COV * Z_COV(H)] / [Σ_j r_j + r_COV]`

equivalente a:

`Q(H) = Σ_k w_k * Z_k(H)`

dove k comprende sia i criteri site-level già mediati sui cinque Hub sia i criteri configuration-level.

Ogni criterio entra **una sola volta** nella ponderazione finale.

## 6. Conseguenza rispetto alla v01

DEC-0086 raffina DEC-0070.

Non si usa più come formulazione primaria:

`S_i = Σ_j w_j z_ij` seguito da `Q(H)=(1/5)Σ_i S_i`

quando è presente almeno un criterio configuration-level, perché tale lettura porterebbe a una seconda ponderazione poco trasparente.

Lo score complessivo del singolo candidato può essere calcolato come output descrittivo se utile, ma non è l'oggetto che viene ripesato nella funzione finale della cinquina.

## 7. Vincoli di configurazione

La funzione obiettivo non rende automaticamente valida una cinquina.

I vincoli HARD / quality gate di configurazione, in particolare AFIR/TEN-T, restano separati da Q(H).

Il modello confronta/massimizza Q(H) soltanto tra configurazioni che superano i vincoli approvati.

## 8. Stato

ACCEPTED:
- modello single-objective;
- media sui cinque Hub criterio per criterio per i criteri site-level;
- criteri configuration-level calcolati direttamente sulla cinquina;
- unica ponderazione finale;
- nessun fronte di Pareto necessario;
- separazione tra funzione obiettivo e vincoli HARD di configurazione.

SUSPENDED / PENDING:
- valori concreti di importanza 1–5;
- dimensione operativa della griglia della copertura, da fissare con verifica di convergenza/sensitivity;
- formalizzazione computazionale completa dei vincoli AFIR/TEN-T;
- eventuale trattamento finale della storica soglia minima 10 km Hub–Hub.

Con DEC-0087 formula raw e normalizzazione di `Z_COV(H)` sono ACCEPTED.
