# AFIR / TEN-T — ROLE IN MODEL_v2 v01

**Data:** 2026-09-21
**Stato:** ACCEPTED
**Autorità:** DEC-0069

## 1. Principio

AFIR/TEN-T è una componente **primaria** del MODEL_v2.

La relazione con la TEN-T deve concorrere in modo esplicito alla qualità individuale dei candidati, ma il requisito dei 10 km stradali non è un hard filter universale dell'intero universo candidato.

## 2. Livello del singolo candidato

Per ciascun candidato dovrà essere costruito un indicatore/insieme di indicatori che rappresenti la relazione con AFIR/TEN-T.

Il ruolo è quello di **criterio primario di localizzazione**.

Formula raw, trasformazione, normalizzazione e peso non sono ancora approvati e restano oggetto delle DQ successive.

## 3. Regola dei 10 km

Per H2, la condizione di localizzazione “lungo TEN-T” viene verificata tramite la distanza stradale dalla nearest TEN-T exit secondo la definizione AFIR applicabile.

La soglia di 10 km:
- serve a stabilire se una localizzazione può essere conteggiata come infrastruttura H2 “lungo TEN-T”;
- non elimina automaticamente un candidato oltre 10 km;
- non richiede che tutti e cinque gli Hub ricadano entro 10 km dalla TEN-T.

## 4. Livello della configurazione di cinque Hub

La cinquina finale deve essere verificata rispetto ai requisiti AFIR applicabili.

La qualità della configurazione non coincide con la sola somma dei punteggi individuali.

Devono essere verificati almeno, quando applicabili:
- copertura della TEN-T core;
- requisito massimo di 200 km tra le stazioni conteggiate ai fini AFIR;
- copertura dei nodi urbani TEN-T pertinenti;
- requisiti tecnici necessari affinché una stazione venga effettivamente conteggiata ai fini AFIR.

Il requisito dei 200 km è una **distanza massima di copertura**, non una distanza minima di separazione tra Hub.

## 5. Infrastrutture H2 esistenti/programmate

La presenza di infrastrutture H2 esistenti o programmate costituisce un **criterio positivo separato**.

La semantica è quella di:
- integrazione;
- sinergia;
- possibilità di potenziamento;
- valorizzazione di infrastrutture già presenti/programmate.

Non deve essere interpretata automaticamente come conformità AFIR.

Formula raw, trasformazione, normalizzazione e peso del criterio restano da approvare.

## 6. Monfalcone Lisert

Monfalcone Lisert è un caso esplicitamente rilevante.

L'infrastruttura APT:
- costituisce un'infrastruttura H2 di contesto verificata;
- può rendere territorialmente interessante una localizzazione nell'area per integrazione/potenziamento;
- non è automaticamente conteggiata come stazione AFIR conforme;
- non è automaticamente uno dei cinque Hub.

Un eventuale Hub localizzato nell'area può essere valutato anche come opportunità di potenziamento dell'infrastruttura H2 esistente/programmata verso i requisiti richiesti dalla configurazione.

Non si assume a priori la fattibilità tecnica del potenziamento: capacità reale di rifornimento, commissioning, accessibilità pubblica e altre condizioni necessarie devono essere validate quando richieste dal configuration contract.

## 7. Distinzione da requisito 10 km tra Hub

Il requisito di commessa proposto di distanza minima **10 km tra i cinque Hub** è distinto dalla soglia AFIR dei 10 km dalla TEN-T exit.

DEC-0069 non approva il minimo 10 km tra Hub.

## 8. Effetto sulla decision queue

DEC-0069 chiude il principio di ruolo:
- AFIR/TEN-T = criterio primario individuale;
- conformità AFIR = vincolo/quality gate della configurazione;
- infrastruttura H2 esistente/programmata = criterio positivo separato.

Restano pendenti:
- formula raw;
- unità e geometria di riferimento;
- trasformazione/normalizzazione;
- peso;
- aggregazione nello score individuale;
- formalizzazione computazionale del configuration constraint;
- trattamento quantitativo di Monfalcone e delle altre infrastrutture H2.
