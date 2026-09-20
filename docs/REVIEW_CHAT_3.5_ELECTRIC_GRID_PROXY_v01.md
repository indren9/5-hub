# REVIEW — Chat 3.5 — Proxy territoriale di prossimità alla rete elettrica

**Reviewer:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-20
**Mandato review:** verifica indipendente del quality gate minimo OSM/OpenInfraMap
**Artifact specialistico:** `docs/FASE_3_ELECTRIC_GRID_PROXY_VALIDATION_REVIEW_v01.md`
**Handoff:** `docs/HANDOFF_CHAT_3.5_ELECTRIC_GRID_PROXY_v01.md`

## 1. Esito della review indipendente

**TECHNICAL_QUALITY_GATE: ACCEPTED_WITH_LIMITATIONS**

Il giudizio specialistico `READY_WITH_LIMITATIONS` è confermato sul piano tecnico.

Questa review NON approva ancora la combinazione di fonti come baseline metodologica definitiva del futuro indicatore energetico. Tale scelta resta soggetta ad approvazione esplicita dell'utente.

## 2. Controlli indipendenti eseguiti

La Chat Madre non ha assunto come veri i conteggi dell'handoff.

Sono stati verificati direttamente:
- esistenza e appartenenza dei commit `ff5edc3` e `df8d8cb` al branch `chat-3.5-electric-grid-energy`;
- branch pulito prima della review;
- contenuto dei quattro artifact repository;
- script di acquisizione/QA;
- manifest OneDrive e relativi SHA-256;
- conteggi dei raw OSM, subset CP-proxy, aree ufficiali e coverage;
- due gap interni;
- cross-check DSO;
- semantica di Overpass `out center`;
- coerenza con DEC-0050.
## 3. Conteggi riprodotti

Ricalcolo indipendente sui file materializzati:
- elementi OSM `power=substation` deduplicati: **8.206**;
- subset QA CP-proxy: **92**;
- classi: 89 `A_DSO_HV_PLAUSIBLE`, 3 `B_DISTRIBUTION_HV_OPERATOR_MISSING`;
- operatori: 81 e-distribuzione, 7 AcegasApsAmga, 1 SECAB, 3 mancanti;
- aree convenzionali ufficiali: **57**;
- aree con posizione CP-proxy interna: **48/57**;
- aree interne FVG `EXTRAFVG=0`: **44**;
- aree interne coperte: **42/44**;
- aree interne con match gestore: **42/44**;
- gap interni: `AC001E00999`, `AC001E00994`.

I conteggi coincidono con l'handoff.

## 4. Integrità e riproducibilità

Il manifest `source_manifest_v01.json` contiene 20 record.

Verifica indipendente:
- file mancanti: 0;
- mismatch byte: 0;
- mismatch SHA-256: 0.

Lo script `scripts/acquire_validate_electric_grid_proxy_chat3_5_v01.py` supera il controllo sintattico Python.

La logica di deduplicazione OSM usa la chiave `(osm_type, osm_id)`, coerente con l'estrazione tiled.
## 5. Regola QA >= 60 kV

La soglia >=60 kV è accettabile esclusivamente come regola di QA del quality gate.

Motivazione documentata:
- evita di perdere Barcis, confermata dalla fonte ufficiale e-distribuzione e mappata OSM a 60 kV;
- non è presentata come soglia normativa;
- non è presentata come requisito di connessione;
- non è presentata come soglia di capacità;
- non viene congelata come regola del futuro modello.

Conclusione review:
**PASS_WITH_LIMITATIONS**.

La soglia non deve essere riutilizzata automaticamente nelle fasi successive senza nuova decisione metodologica.

## 6. Rilievo della Chat Madre — Overpass out center

Lo script specialistico usa:

`out center tags qt;`

Per way e relation, Overpass restituisce il centro del bounding box dell'oggetto, non la geometria completa. La documentazione Overpass precisa inoltre che tale centro non è garantito all'interno del poligono OSM.

Riferimento:
https://wiki.openstreetmap.org/wiki/OverpassQL

Conseguenza:
- il quality gate 42/44 dimostra una forte coerenza territoriale delle **posizioni rappresentative OSM** rispetto alle aree convenzionali;
- non dimostra ancora che il dataset derivato contenga il footprint fisico completo di ogni sottostazione;
- questo limite non invalida il quality gate di copertura, perché le aree convenzionali sono territorialmente molto più estese dei singoli impianti;
- il limite deve però restare esplicito e la futura metrica di prossimità dovrà decidere se usare un punto rappresentativo o la geometria OSM completa.
## 7. Cross-check DSO indipendente

Il file `dso_official_crosscheck_v01.csv` contiene 17 casi:
- 10 `MATCH_NAME_ROLE` e-distribuzione;
- 5 `MATCH_NAME_VOLTAGE_ROLE` AcegasApsAmga;
- 1 `PARTIAL_PHYSICAL_COMPLEX_ONLY` Redipuglia;
- 1 `PARTIAL_OPERATOR_VOLTAGE_SEMANTIC_CONFLICT` SECAB.

Spot-check indipendente delle fonti:
- e-distribuzione `Inversioni_di_flusso_2025.pdf` contiene, tra gli altri, Cormons, Redipuglia, Barcis, Giais, Pordenone e Prata;
- il Piano AcegasApsAmga 2025-2029 Rev.1 identifica le CP AT/MT di Trieste/Gorizia e conferma Sant'Andrea 132 kV;
- SECAB conferma la cabina primaria di Paluzza 132/20 kV.

Riferimenti:
- https://www.e-distribuzione.it/content/dam/e-distribuzione/documenti/aree_critiche/Inversioni_di_flusso_2025.pdf
- https://www.acegasapsamga.it/documents/d/acegasapsamga/piano-di-sviluppo-aaa-2025-29-definitivo-pdf
- https://www.secab.it/it/servizi/distribuzione

Il cross-check supporta la plausibilità territoriale ma non trasforma OSM in censimento ufficiale.
## 8. Gap e limiti da preservare

Restano espliciti:
- `AC001E00999` — Redipuglia: CP e-distribuzione confermata ufficialmente ma non isolata come distinta posizione CP-proxy DSO in OSM;
- `AC001E00994` — posizione OSM plausibile non interna all'area ufficiale;
- 7 aree `EXTRAFVG=1` senza posizione CP-proxy interna;
- tagging OSM non uniforme;
- possibile sovra-inclusione di infrastrutture plausibili ma non equivalenti a CP ufficiali;
- nessun dato di capacità disponibile;
- nessuna connessione garantita;
- nessun costo di connessione.

Nessuno di questi gap è stato riempito con una tolleranza o stima arbitraria.

## 9. Correzioni richieste dalla review

Prima del merge la Chat Madre ha corretto:
1. trailing whitespace nei Markdown specialistici;
2. formulazioni che chiamavano genericamente "geometrie" i punti `out center`;
3. Source Matrix, aggiungendo esplicitamente che il QA usa `out center` per way/relation.

Le correzioni non cambiano conteggi, risultati o giudizio tecnico.

## 10. Giudizio finale della Chat Madre

**Chat 3.5: TECHNICAL_QUALITY_GATE = PASS / ACCEPTED_WITH_LIMITATIONS.**

È tecnicamente difendibile proporre come base dati per il futuro proxy:
- oggetti OSM `power=substation` / loro localizzazioni rappresentative;
- aree convenzionali ufficiali FVG/GSE come controllo territoriale e gestore;
- fonti DSO ufficiali come cross-check di currentness, ruolo e tensione.

Restano NON approvati anche dopo DEC-0053:
- OSM come censimento ufficiale delle cabine primarie;
- una soglia elettrica del modello;
- la geometria target finale del futuro indicatore;
- la metrica o soglia di distanza;
- qualsiasi conversione distanza → MW/capacità/costo;
- apertura della Fase 4.

La sola modifica successiva alla review tecnica è la risoluzione **procedurale** di `ISS-0007` tramite DEC-0053: non è stato acquisito un dataset di capacità disponibile, ma quel dato non è più richiesto a scala regionale.

## 11. Decisione metodologica finale

**DEC-0053 — ACCEPTED.**

L'utente approva la combinazione **OSM substation objects / representative locations + aree convenzionali ufficiali FVG/GSE + cross-check DSO** come baseline dati del futuro proxy territoriale di prossimità alla rete elettrica.

La scelta è esplicitamente coerente con una **pianificazione macro**: non si richiede una precisione da studio di connessione elettrica nella fase regionale.

Restano invariati i limiti già documentati:
- OSM non è un censimento ufficiale delle cabine primarie;
- prossimità non equivale a capacità disponibile;
- i gap `AC001E00999` e `AC001E00994` restano espliciti;
- la regola >=60 kV resta QA-only;
- punto rappresentativo vs geometria completa, metrica e soglie di distanza saranno definiti nelle fasi indicatori;
- capacità reale, punto di connessione, costi e fattibilità tecnica restano verifiche puntuali sui candidati finalisti.

`ISS-0007` è quindi **RESOLVED proceduralmente**: l'assenza di un dataset region-wide di capacità resta un limite reale, ma non è più un blocker della Fase 3 perché la metodologia approvata non richiede tale dato a scala regionale.
