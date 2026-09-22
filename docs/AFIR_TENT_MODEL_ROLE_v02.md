# AFIR / TEN-T — ROLE IN MODEL_v2 v02

**Data:** 2026-09-21
**Stato:** ACCEPTED
**Autorità:** DEC-0069 + DEC-0072
**Predecessore:** AFIR_TENT_MODEL_ROLE_v01.md — preservato come baseline storica

## 1. Principio

AFIR/TEN-T resta una componente primaria del MODEL_v2, ma non genera uno score individuale basato sulla distanza dalla TEN-T.

DEC-0072 raffina DEC-0069 per evitare doppio conteggio tra prossimità TEN-T e conformità AFIR.

## 2. Livello del singolo candidato

La distanza dalla TEN-T non entra nello score individuale.

Il criterio site-level pertinente è invece **flussi veicolari intercettabili**:
- maggiore opportunità di intercettare traffico rilevante = maggiore punteggio;
- la formula raw e la normalizzazione restano da definire;
- va evitato il doppio conteggio con AFIR/TEN-T.

## 3. Regola dei 10 km AFIR

Per H2, la condizione “lungo TEN-T” viene verificata tramite distanza stradale dalla nearest TEN-T exit secondo AFIR.
La soglia dei 10 km:
- serve a stabilire se una localizzazione può essere conteggiata ai fini della copertura AFIR;
- non produce score;
- non è hard filter universale dell'universo candidato;
- non richiede che tutti e cinque gli Hub ricadano entro 10 km dalla TEN-T.

## 4. Livello della configurazione

La cinquina finale deve soddisfare i requisiti AFIR applicabili.

Devono essere verificati almeno, quando applicabili:
- copertura della TEN-T core;
- requisito massimo di 200 km tra le stazioni conteggiate ai fini AFIR;
- copertura dei nodi urbani TEN-T pertinenti;
- requisiti tecnici necessari affinché una stazione venga conteggiata ai fini AFIR.

Per Trieste e Udine la Chat 5.2 ha verificato al 22/09/2026 `NO_LEGAL_SPATIAL_BOUNDARY_IDENTIFIED`. Con DEC-0089 il MODEL_v2 adotta esplicitamente una proxy progettuale: Comune di Trieste = proxy operativa del nodo urbano di Trieste; Comune di Udine = proxy operativa del nodo urbano di Udine. La cinquina deve quindi includere almeno un Hub in ciascuno dei due Comuni. Questa è un'assunzione progettuale e non una dichiarazione sul perimetro legale TEN-T/AFIR. `ISS-0017` è risolta proceduralmente ma la limitazione resta documentata.

Il requisito dei 200 km è una distanza massima di copertura, non una distanza minima tra Hub.

## 5. Infrastrutture H2 esistenti/programmate

La presenza di infrastrutture H2 esistenti o programmate resta un criterio positivo separato.

La semantica approvata è:
- integrazione;
- sinergia;
- possibilità di potenziamento;
- valorizzazione di infrastrutture già presenti/programmate.
Non deve essere interpretata automaticamente come conformità AFIR.

Formula raw, normalizzazione e peso restano da definire.

## 6. Monfalcone Lisert

Con DEC-0090 Monfalcone/Lisert è trattata pienamente come area/infrastruttura H2 di riferimento per la localizzazione.

Nel MODEL_v2:
- si verifica sul candidato selezionato la compliance territoriale AFIR lato distanza stradale dalla nearest TEN-T exit secondo la regola `<=10 km`;
- il fatto che l'impianto Lisert documentato resti sotto `1 t/giorno` è mantenuto come limitation / design requirement, non come filtro localizzativo;
- il modello non dimensiona la capacità aggiuntiva necessaria;
- un Hub può essere localizzato nello stesso poligono dell'infrastruttura esistente, come integrazione/potenziamento, oppure in un poligono distinto vicino con la stessa funzione strategica;
- in entrambi i casi la verifica territoriale AFIR si applica al candidato Hub;
- il requisito tecnico `>=1 t/giorno` resta DEFER_POST_MODEL per progettazione/dimensionamento e non entra nello score o nell'universo candidati.

## 7. Distanza minima tra Hub

Con DEC-0088 la storica soglia minima di 10 km tra i cinque Hub è eliminata dal MODEL_v2.

Non costituisce né requisito AFIR, né HARD constraint, né criterio di scoring. La distribuzione territoriale della cinquina è valutata tramite il criterio `Z_COV(H)` approvato con DEC-0087.

Resta distinta e invariata la soglia AFIR di 10 km stradali dalla nearest TEN-T exit per stabilire se una stazione H2 può essere considerata «lungo TEN-T».

## 8. Effetto sulla decision queue

ACCEPTED:
- AFIR/TEN-T = vincolo HARD / quality gate della configurazione;
- nessuno score individuale basato sulla distanza TEN-T;
- flussi veicolari intercettabili = criterio site-level sostitutivo;
- infrastruttura H2 esistente/programmata = criterio positivo separato.

PENDING:
- formalizzazione computazionale del vincolo AFIR di configurazione;
- gestione operativa del requisito urban-node alla luce del gap di delimitazione ufficiale verificato da Chat 5.2;
- ruolo concreto di Monfalcone/Lisert nella copertura AFIR, senza assumerne automaticamente la conformità.
