# TRAFFIC DATA INPUT REVIEW v01

**Data:** 2026-09-22
**Stato:** REVIEW
**Origine:** ricognizione Chat Madre Tesi + DEC-0075

## 1. Scopo

Identificare gli artifact da riusare nel criterio site-level "flussi veicolari intercettabili" definito da DEC-0072/0073/0074 e fissare l'orizzonte HEAVY secondo DEC-0075.

## 2. LIGHT

Artifact operativo identificato:
`DIRTY_EDGE_FLOWS_v01.csv`

Percorso:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\90_ARCHIVE\LEGACY_WORKSPACES\Dirty_FRLM\04_OUTPUT\path_flows_v01\DIRTY_EDGE_FLOWS_v01.csv`

Campo flusso:
`dirty_flow_veh_day`

Unità:
veicoli/giorno.

Identificativi:
`edge_id`, `edge_uid`, `segment_uid`, `way_id`, `seq`, `u`, `v`, `way_direction`.

Join geometrico preferito:
`segment_uid`.

Geometria:
`G_OSM_operativo_segments_v01` nel GeoPackage
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\90_ARCHIVE\LEGACY_WORKSPACES\Dirty_FRLM\01_INPUT_SNAPSHOT\network\G_OSM_operativo_v01.gpkg`.

CRS: EPSG:32632.

QA riportata dalla Tesi:
- 46.010 OD;
- 414.090 access-pair path;
- 284.913 directed edges con flusso positivo;
- 0 unreachable;
- mass balance PASS;
- determinismo byte-identical.

Stato scientifico:
DEMONSTRATOR / NON CANONICAL nella Tesi.

Limitazione:
non presentare il dataset come domanda LIGHT finale/calibrata della Tesi.

Con DEC-0076 il LIGHT Dirty FRLM è promosso a baseline operativa ACCEPTED del criterio 5 HUB. Resta obbligatorio dichiararne la natura DEMONSTRATOR / NON CANONICAL rispetto alla Tesi.

## 3. HEAVY

Package scientifico:
`H60_HEAVY_OD_SPETH_PACKAGE_V01`

Percorso:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\TESI_THESIS_STORAGE\04_FROZEN_CHECKPOINTS\HEAVY_6_0\HEAVY_0B_delivery_v01.zip`

Stato sorgente:
FROZEN / VERIFIED.

File:
`HEAVY_PATH_FLOWS_v01.csv`.

Campi:
- `heavy_vehicles_day_2019`;
- `heavy_vehicles_day_2030`.

Unità:
camion/giorno medio annuo.

Il campo `rerouted_edge_path` contiene la sequenza ordinata dei `Network_Edge_ID`.

L'edge flow viene ricostruito deterministicamente sommando, per ciascun `Network_Edge_ID`, il valore dei path che attraversano l'arco.

Procedura già validata nella baseline Tesi:
`audit_speth_flow_concentration.py`.

Geometria:
layer `speth_geometry_edges` nel GeoPackage
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\TESI_THESIS_STORAGE\03_CANONICAL_DATA\QGIS_PRESENTATION\HEAVY_SPETH_v02\HEAVY_SPETH_PRESENTATION_v02.gpkg`.

CRS: EPSG:32632.

### Orizzonte approvato — DEC-0075

Per il MODEL_v2:
- `heavy_vehicles_day_2030` = **baseline HEAVY dello score**;
- `heavy_vehicles_day_2019` = benchmark / sensitivity.

Motivazione:
allineamento temporale dell'analisi con l'orizzonte 2030 dei principali target H2 AFIR. Questa è una scelta metodologica del progetto, non un obbligo AFIR di usare una previsione di traffico 2030.

Limitazioni HEAVY da mantenere esplicite:
- systematic high bias rispetto alle sezioni ANAS confrontabili;
- coarseness locale a Trieste;
- rappresentazione debole su A34 / Gorizia / Sant'Andrea-Vrtojba / H4;
- rete ETISplus/Speth adatta soprattutto ai corridoi sovralocali;
- scenario 2030 non calibrato localmente su ANAS FVG.

## 4. Separazione delle reti

Gli identificativi LIGHT e HEAVY non sono compatibili.

LIGHT usa rete OSM / `segment_uid`.
HEAVY usa rete ETISplus/Speth / `Network_Edge_ID`.

I due layer restano distinti e vengono associati ai candidati spazialmente.

## 5. Applicazione della formula DEC-0074

Per ogni candidato:
- LIGHT: calcolare `F_i^L` sugli archi OSM entro 5 km, se/quanto la fonte LIGHT sarà approvata;
- HEAVY: calcolare `F_i^H` sugli edge flows 2030 ricostruiti per `Network_Edge_ID`;
- usare `f(d)=1-d/5`;
- contributo `V=q*f(d)`;
- valore raw = massimo contributo entro 5 km;
- 0 se non esistono archi utili nella finestra.

## 6. Stato governance

HEAVY 2030 come orizzonte baseline è ACCEPTED con DEC-0075.

La sorgente LIGHT Dirty FRLM è ACCEPTED come baseline operativa del MODEL_v2 con DEC-0076, mantenendo obbligatoriamente il caveat DEMONSTRATOR / NON CANONICAL rispetto alla Tesi.

Il full edge-flow HEAVY deve essere materializzato e sottoposto a QA prima di essere registrato come artifact operativo definitivo del 5 HUB.
