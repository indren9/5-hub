# FASE 1 — Definizione Hub Energetico Green — REBASELINED v03 — FROZEN

**Chat:** 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Stato:** FROZEN — approvato esplicitamente dall'utente il 2026-09-21
**Predecessore preservato:** FASE_1_HUB_DEFINITION_REBASELINED_v03.md — FROZEN / HISTORICAL PREDECESSOR
**Autorità:** DEC-0061, DEC-0062 e DEC-0068 ACCEPTED

## 1. Perché serve un successore

La v02 definisce correttamente l'identità funzionale dell'Hub, ma alcune formulazioni dei requisiti localizzativi possono essere lette come obbligo di dimostrare fattibilità puntuale del terreno prima della chiusura del modello.

DEC-0061 ha ristretto il risultato richiesto a una pianificazione strategica territoriale: i cinque poligoni finali sono alternative territorialmente preferibili, non terreni già verificati sotto il profilo catastale, autorizzativo, progettuale o di connessione.

Questa v04 aggiorna esclusivamente il requisito funzionale relativo all'elettrolizzatore, senza modificare retroattivamente le versioni precedenti.

## 2. Elementi che restano invariati

Restano validi i principi funzionali precedenti con una successor decision su F1-D6:
- tutti i cinque Hub integrano H₂ pubblico e ricarica elettrica DC pubblica;
- le specifiche AFIR H₂ sono obbligatorie solo quando l'Hub svolge la relativa funzione AFIR/TEN-T;
- il modulo EV deve servire Light e Heavy;
- FER fisica in sito non è obbligatoria;
- H₂ rinnovabile/certificato non è requisito universale del nucleo minimo;
- **ogni Hub integra un elettrolizzatore in sito** (DEC-0068);
- l'eventuale approvvigionamento H₂ aggiuntivo tramite tube trailer, pipeline o altre soluzioni resta aperto;
- altri vettori energetici restano opzionali.

DEC-0068 supersede F1-D6 / DEC-0011 **solo** nella parte in cui l'elettrolizzatore in sito non era obbligatorio.

Restano inoltre fuori scope layout, progettazione esecutiva e scelta tecnologica definitiva.

## 3. Nuova interpretazione localizzativa

Il modello deve verificare la coerenza territoriale con le funzioni dell'Hub alla scala strategica.

Un requisito funzionale entra nel core solo quando può essere rappresentato in modo territoriale, riproducibile e proporzionato alla scala regionale.

Le verifiche che richiedono il progetto concreto, sopralluoghi, interlocuzione con gestori/enti, dati proprietari o istruttoria autorizzativa sono post-model due diligence.

## 4. AFIR e TEN-T

Resta valido il principio della v02: requisiti e distanze AFIR si applicano solo agli Hub cui venga assegnata una funzione AFIR/TEN-T pertinente.

La decisione se e come questa funzione generi hard constraint, soft criterion o vincolo della configurazione non è assunta qui e resta nella futura decision queue.

## 5. Accessibilità Light/Heavy

Nel core:
- domanda, flussi/path-flow e corridoi Light/Heavy;
- relazione territoriale con la rete stradale e TEN-T;
- eventuali indicatori macro di accessibilità approvati in seguito.

Fuori dal core obbligatorio:
- progettazione degli accessi;
- verifica legale/esecutiva della singola entrata/uscita;
- verifica definitiva di sagome, manovre e restrizioni locali Heavy.

Le condizioni della LR FVG 19/2012 e altre prescrizioni applicabili restano riferimenti reali, ma il loro accertamento sito-specifico diventa post-model salvo futura operazionalizzazione GIS di un hard constraint esplicitamente approvato.

## 6. Energia e approvvigionamento

Nel core l'infrastruttura elettrica è rappresentata mediante il proxy territoriale approvato e futuri indicatori coerenti con la scala macro.

L'elettrolizzatore è **obbligatorio come componente funzionale** di tutti e cinque gli Hub, ma DEC-0068 stabilisce che la sua presenza non produce effetti localizzativi nel MODEL_v2. In particolare non genera:
- hard filter territoriali;
- score o premialità;
- requisiti aggiuntivi sull'universo candidato;
- vincoli della configurazione dei cinque Hub.

Restano post-model/progettuali:
- potenza e dimensionamento dell'elettrolizzatore;
- layout e distanze di sicurezza;
- MW realmente disponibili;
- punto di connessione;
- preventivo/costo;
- studio tecnico di connessione;
- configurazione esecutiva complessiva dell'approvvigionamento H₂.

## 7. Sicurezza, spazio e fattibilità progettuale

Il modello non certifica il rispetto esecutivo delle distanze di sicurezza o delle prescrizioni antincendio e non costruisce il layout dell'Hub.

L'eventuale superficie minima o altra regola geometrica dell'universo candidato deve essere motivata e approvata nella fase dedicata; non viene ereditata implicitamente da stime storiche.

Le interferenze territoriali osservabili possono entrare come hard constraint, soft criterion o flag solo dopo decisione esplicita.

## 8. Significato della compatibilità

Dire che un poligono è idoneo nel modello significa che è una buona alternativa territoriale secondo i criteri approvati.

Non significa che:
- il terreno sia disponibile o acquistabile;
- il PRGC puntuale sia definitivamente verificato;
- gli accessi siano già autorizzabili;
- la connessione elettrica sia disponibile;
- la sicurezza impiantistica sia già dimostrata;
- l'Hub sia immediatamente cantierabile.

## 9. Decisioni precedenti: trattamento

- DEC-0006…DEC-0012 / F1-D1…F1-D7: **KEEP**, salvo F1-D6 / DEC-0011 parzialmente superseded da DEC-0068 per l'obbligatorietà dell'elettrolizzatore.
- DEC-0013: resta la decisione storica di freeze della v02; **non viene modificata**.
- DEC-0061: mantiene la separazione fra requisiti funzionali e due diligence.
- DEC-0068: rende obbligatorio l'elettrolizzatore in tutti e cinque gli Hub senza introdurre effetti localizzativi nel MODEL_v2.
- Le DEC successive che impongono verifiche puntuali sui finalisti richiedono specifiche successor decisions dove la re-baseline propone di rinviarle post-model.

## 10. Stato

Questa v04 è **FROZEN** ed è la baseline funzionale corrente di Fase 1.

Con l'approvazione esplicita dell'utente:
1. la v04 succede alla v03;
2. v03 e v02 restano preservate come baseline FROZEN storiche;
3. DEC-0068 è la successor decision di F1-D6 / DEC-0011 limitatamente all'obbligatorietà dell'elettrolizzatore;
4. l'obbligo funzionale non riapre DQ-01 e non modifica l'universo candidato.

Nessuna nuova fase viene aperta da questo documento.
