# DISPATCH — Chat 3.5 — Proxy territoriale di prossimità alla rete elettrica

**Fase:** 3 — Inventario e validazione dei dati
**Data:** 2026-09-20
**Stato mandato:** AUTHORIZED
**Regia:** Chat Madre 5 HUB
**Decisioni di riferimento:** DEC-0049, DEC-0050
**Sostituisce operativamente:** `DISPATCH_CHAT_3.5_ELECTRIC_GRID_ENERGY_FEASIBILITY_v01.md`

## 1. Obiettivo

Costruire una base dati semplice, difendibile e riproducibile per rappresentare, nel modello regionale 5 HUB, la **prossimità dei candidati all'infrastruttura elettrica rilevante**.

Il lavoro è di **pianificazione territoriale di massima**. Non deve trasformarsi in uno studio di connessione elettrica di dettaglio.

La Chat 3.5 deve individuare e validare la migliore fonte ragionevolmente disponibile per localizzare:
- cabine primarie e/o stazioni elettriche rilevanti;
- se utile, linee o altra infrastruttura elettrica principale.

## 2. Principio metodologico APPROVATO — DEC-0050

Per lo screening regionale:

- la prossimità all'infrastruttura elettrica può essere usata come **proxy della facilità potenziale di connessione**;
- cabina vicina o linea vicina **NON equivale** a capacità disponibile;
- non è richiesto stimare MW disponibili region-wide per tutti i candidati;
- capacità disponibile, punto di connessione, costi e fattibilità tecnica reale sono verifiche puntuali sui candidati finalisti;
- nessun proxy deve essere presentato come connessione garantita.

## 3. Domande operative

La Chat 3.5 deve rispondere soltanto a queste domande:

1. Qual è la migliore fonte ragionevolmente disponibile per localizzare in FVG le cabine primarie/stazioni o altra infrastruttura utile al proxy?
2. OpenInfraMap è utilizzabile per questo scopo? Da quali dati deriva, con quale copertura, completezza e currentness?
3. Esistono fonti ufficiali Terna, DSO o Regione FVG altrettanto semplici o migliori per lo stesso scopo?
4. Quale geometria deve essere usata nel modello: punto/stazione reale, linea, area servita o combinazione?
5. Quale metrica di prossimità è tecnicamente riproducibile e coerente con l'unità di analisi della Fase 2?
6. Quali limiti devono accompagnare obbligatoriamente il proxy?
7. Quali verifiche elettriche reali devono essere rinviate ai finalisti?

## 4. Fuori scope

NON svolgere un audit energetico specialistico region-wide.

In particolare, salvo che serva strettamente a interpretare la fonte scelta, non è richiesto:

- stimare hosting capacity;
- stimare MW disponibili;
- ricostruire code o richieste di connessione;
- modellare flussi elettrici;
- valutare costi reali di connessione;
- progettare nuove cabine o trasformazioni;
- censire in dettaglio tutti i piani di sviluppo Terna/DSO;
- costruire scenari di fabbisogno elettrico dell'Hub;
- valutare BESS, fotovoltaico o elettrolisi come progettazione impiantistica.

Questi aspetti possono essere annotati come limite o verifica futura, ma non devono espandere il mandato.

## 5. Fonti da confrontare

Confrontare in modo proporzionato almeno:

1. eventuale fonte ufficiale direttamente utilizzabile per cabine/stazioni;
2. Terna/TE.R.R.A. solo per quanto utile a localizzazione e lineage;
3. distributori di rete competenti, se rendono disponibile una geometria pertinente;
4. `F3_SRC_FVG_CP_001` — aree convenzionali cabine primarie, ricordando che un'area servita non è necessariamente la posizione fisica della cabina;
5. OpenInfraMap/OpenStreetMap come possibile fonte operativa, da verificare e non assumere automaticamente autorevole.

La scelta della fonte finale non è già decisa.

## 6. Classificazione minima dei dati

Ogni fonte esaminata deve essere classificata almeno come:

- `PHYSICAL_INFRASTRUCTURE_GEOMETRY` — geometria fisica di cabina/stazione/linea;
- `SERVICE_AREA` — area territoriale associata a una cabina o servizio;
- `PROXY_ONLY` — dato utile allo screening ma non equivalente a capacità reale;
- `NOT_SUITABLE` — fonte non adeguata allo scopo.

## 7. Output richiesti

Repository locale:

- `docs/FASE_3_ELECTRIC_GRID_PROXY_VALIDATION_REVIEW_v01.md`;
- `docs/FASE_3_ELECTRIC_GRID_PROXY_SOURCE_MATRIX_v01.csv`;
- `docs/HANDOFF_CHAT_3.5_ELECTRIC_GRID_PROXY_v01.md`;
- eventuali script leggeri necessari a acquisizione e QA.

Dataset pesanti o geospaziali:
`5_HUB_FVG\02_external_sources\F3_CHAT_3_5\`

Per ogni fonte materializzata registrare almeno:
- fonte e URL;
- data di accesso;
- versione/data quando disponibile;
- formato;
- CRS;
- byte e SHA-256;
- ruolo nel modello;
- limiti.

Branch:
`chat-3.5-electric-grid-energy`

## 8. Governance

La Chat 3.5 può aggiornare con stati prudenti:
- DATA_REGISTRY;
- ISS-0007;
- documentazione tecnica del proprio mandato.

Non può:
- chiudere autonomamente ISS-0007;
- trasformare prossimità in capacità;
- approvare autonomamente soglie, pesi o scoring;
- modificare Fase 1 o Fase 2 FROZEN;
- aprire Fase 4.

Se emerge una scelta metodologica sostanziale non già coperta da DEC-0050, deve restituirla alla Chat Madre come proposta.

## 9. Quality gate

PASS tecnico solo se:

- almeno una fonte operativa è stata verificata con lineage sufficiente;
- OpenInfraMap, se considerata, è stata verificata e non assunta per nome;
- posizione fisica, area servita e capacità disponibile restano concetti distinti;
- coverage FVG e limiti sono documentati;
- la geometria scelta è acquisibile o ricostruibile in modo riproducibile;
- nessun valore di capacità elettrica è inventato;
- la futura metrica di prossimità è implementabile senza assunzioni nascoste;
- artifact, hash, Git e handoff sono completi.

## 10. Criterio di successo

La Chat Madre deve poter rispondere chiaramente:

> Quale infrastruttura elettrica possiamo rappresentare in modo affidabile a scala regionale, con quale fonte, e come possiamo usarne la prossimità come proxy senza confonderla con la capacità reale?

Il risultato deve essere proporzionato a una **pianificazione di massima dei 5 Hub**.
