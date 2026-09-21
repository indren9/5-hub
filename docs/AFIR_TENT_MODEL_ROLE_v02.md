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

Monfalcone Lisert resta un caso rilevante:
- infrastruttura H2 di contesto verificata;
- possibile opportunità di integrazione/potenziamento;
- non automaticamente AFIR-compliant;
- non automaticamente uno dei cinque Hub.

## 7. Distinzione da requisito 10 km tra Hub

Il requisito proposto di distanza minima 10 km tra i cinque Hub resta distinto dai 10 km AFIR dalla TEN-T exit.

DEC-0072 non approva il minimo 10 km tra Hub.

## 8. Effetto sulla decision queue

ACCEPTED:
- AFIR/TEN-T = vincolo HARD / quality gate della configurazione;
- nessuno score individuale basato sulla distanza TEN-T;
- flussi veicolari intercettabili = criterio site-level sostitutivo;
- infrastruttura H2 esistente/programmata = criterio positivo separato.

PENDING:
- formula raw del criterio flussi;
- segmento/rete di riferimento;
- eventuale combinazione tra flusso e prossimità/accessibilità;
- normalizzazione;
- peso;
- formalizzazione computazionale del vincolo AFIR di configurazione.
