# FASE 3 — Screening di rilevanza del problema “nearest TEN-T exit”

**Data:** 2026-09-18

**Stato:** REVIEW / evidenza diagnostica, non decisione metodologica

**Contesto:** Q-METH-3.3-A — definizione operativa di “nearest TEN-T road exit” sui tratti non a accesso controllato.

## 1. Domanda

Verificare prima di introdurre una regola metodologica se, nel Friuli Venezia Giulia, esistano davvero tratti stradali TEN-T rilevanti per il modello 5 HUB privi di vere rampe/svincoli e caratterizzati da intersezioni ordinarie a raso.

Principio: la cartografia TEN-T ufficiale stabilisce **quali** tratti appartengono alla TEN-T; OSM viene usato solo come supporto geometrico/topologico per capire **come** sono fatti gli accessi.

## 2. Evidenza TEN-T corrente già disponibile

La review Chat 3.3 e i layer corridoio TENtec correnti materializzati il 2026-09-18 associano i principali tratti core/corridoio FVG a:
- A4;
- A23;
- RA13;
- RA14;
- asse SS202 / Grande Viabilità Triestina e relativi segmenti NSA nel nodo triestino.

Nel servizio corridoi TENtec tali geometrie sono classificate come `Motorways` oppure `Rural road with separate directions`.

## 3. Screening sul grafo OSM congelato

Baseline read-only:
`TESI_THESIS_STORAGE\04_FROZEN_CHECKPOINTS\RECOVERED_BASELINE\OSM_5_6\grafo_operativo_osm\G_OSM_operativo_v01.gpkg`

Layer: `G_OSM_operativo_segments_v01` — 944.219 segmenti, EPSG:32632.

Classificazione OSM osservata:
- A4: prevalentemente `motorway`, con `motorway_link` e pochi segmenti `trunk`;
- A23: `motorway` + `motorway_link`;
- RA13: `motorway` + `motorway_link`;
- RA14: `motorway` + `motorway_link`;
- SS202: `trunk` + `trunk_link` / `primary_link`.

Audit dei nodi della carreggiata principale:
- A23: nessuna connessione diretta sospetta con viabilità ordinaria;
- RA13: nessuna;
- RA14: nessuna;
- A4: un solo nodo sospetto, relativo alla `Bretella di Latisana` (`trunk`, ref A4), connessa a SP75 e link; non è evidenza di intersezione a raso sulla carreggiata principale A4;
- SS202: un solo nodo sospetto, sulla `Nuova Sopraelevata`, connesso a `Via della Rampa`; la topologia OSM mostra struttura di rampa/link a senso unico, non una normale intersezione a raso.

Conclusione dello screening OSM: sui tratti core/corridoio verificati non emerge il caso problematico “TEN-T ordinaria con rotatoria/incrocio a raso usato come pseudo-exit”.

## 4. Controllo di supporto sul TENtec legacy

È stato prodotto, esclusivamente come supporto storico, il crosswalk:
`5_HUB_FVG\05_intermediate_outputs\F3_CHAT_3_3\TENTEC_LEGACY_ROADS_TO_FVG_ROAD_CROSSWALK_SUPPORT_v01.csv`

SHA-256: `62CF8F3ABE7D45BF5A77773B9637FDAC98123B940A377EECEDAD0D0DBC25163D`.

Il layer legacy non-core individua in FVG soprattutto A28 nei campioni associabili alla rete regionale. A28 è autostrada; quindi anche questo controllo non introduce evidenza di un tratto ordinario a raso.

Limite: il servizio legacy non rappresenta la tassonomia corrente 2024 a tre livelli e non può essere promosso a baseline autorevole.

## 5. Fonti ufficiali di controllo

- Commissione europea / TENtec: mappe 2024 core / extended core / comprehensive e sistema TENtec.
- Regione FVG, progetto 5G-SITACOR: tratte corridoio transfrontaliere Udine Nord–Palmanova, Latisana–Fernetti, Fernetti–Sežana, Fernetti–Koper via Trieste, Villesse–Gorizia–Nova Gorica.
- ANAS: RA13 e RA14 classificati come raccordi autostradali; SS202/Grande Viabilità Triestina descritta con svincoli e rampe nei documenti tecnici consultati.

## 6. Esito e limite residuo

**Esito tecnico:** per i tratti TEN-T core/corridoio FVG oggi verificati, Q-METH-3.3-A non produce un problema operativo osservato.

**Non conclusione:** non è ancora dimostrato che il problema sia assente sull’intera rete TEN-T FVG, perché manca il crosswalk route-level corrente completo dei tre livelli `core / extended core / comprehensive`.

Pertanto:
- non introdurre ora una regola artificiale per equiparare rotatorie/incroci a raso a “exit”;
- mantenere Q-METH-3.3-A aperta ma confinata;
- riesaminarla solo se il crosswalk TEN-T corrente completo identifica effettivamente un tratto rilevante senza vera uscita/rampa.

Questo documento non modifica alcuna baseline FROZEN e non crea `TENT_EXIT_SET_v01`.