# LOGISTICS / INDUSTRIAL PROXIMITY DATA REVIEW v01

**Data:** 2026-09-22
**Stato:** ACCEPTED AS MODEL_v2 OPERATIVE BASELINE — DEC-0079
**Origine:** ricognizione Chat Madre Tesi

## 1. Dataset identificato

`C:\Users\visen\Tesi_QGIS_Work\LOGISTICS_FVG\LOGISTICS_FVG_v02.gpkg`

Layer operativo da valutare:
`LOGISTICS_FVG_POINTS`

Caratteristiche:
- 26 poli;
- geometria POINT per tutti i record;
- 26 `SITE_ID` univoci;
- 26 coordinate distinte;
- CRS EPSG:32632;
- provenance incorporata nei campi `NAME`, `CATEGORY`, `MUNICIPALITY`, `SOURCE_ENTITY`, `SOURCE_FILE`, `SOURCE_TYPE`, `SOURCE_QUALITY`, `GEOMETRY_METHOD`, `POINT_METHOD`, `NOTES`.

`LOGISTICS_FVG_AREAS` esiste ma contiene 0 geometrie.

## 2. Stato

Stato tecnico Tesi:
`PASS_WITH_LIMITATION / WORKING / NOT FROZEN / non registrato nell'Artifact Register`.

`LOGISTICS_FVG_v01.gpkg` è funzionalmente superseded da v02.

`HEAVY_AFIR_LOGISTICS_MAP_V01` è CURRENT nell'Artifact Register ma è un PNG di presentazione e non deve essere usato per misure.

## 3. Copertura

Il set corrente comprende:
- 3 porti;
- 2 interporti;
- 4 autoporti / terminal logistici;
- 17 principali poli industriali selezionati nella Tesi.

Totale: 26 poli.

Il set non è un censimento completo di tutte le aree produttive FVG, ma il set dei principali poli industriali scelti nella Tesi.

## 4. Regola geometrica proposta per la base dati

Per ciascun poligono candidato del MODEL_v2 si calcolano le 26 distanze geometriche:
`d_i,01 ... d_i,26`.

Le distanze sono point-to-polygon in EPSG:32632.

In questa fase:
- nessuna soglia;
- nessun peso;
- nessun bonus;
- nessuna aggregazione in uno score unico.

Il risultato atteso è quindi una matrice completa candidato × polo.

## 5. Limiti da preservare

La semantica fisica dei punti non è perfettamente uniforme:
- SITE_ID 04 Interporto Pordenone = OFFICIAL_GATE;
- gli altri sono prevalentemente REPRESENTATIVE_INSTITUTIONAL_POINT.

SITE_ID 25 — ZIMA:
- stato `NEEDS_HUMAN_CHECK`;
- rappresenta il solo sub-ambito industriale di Manzano;
- non rappresenta definitivamente l'intero comprensorio multi-comunale.

`ex EZIT` è denominazione storica dell'attuale comprensorio COSELAG e non è un polo aggiuntivo.

## 6. Provenance

Porti/interporti/logistica e parte dei poli:
`C:\Tesi\LOGISTICS_FVG_SOURCE\`

Registro:
`C:\Tesi\LOGISTICS_FVG_SOURCE\LOGISTICS_SOURCE_REGISTER.csv`

Set 17 aree industriali:
`C:\Tesi\dati\zone_industriali_fvg\FONTI.csv`

Originali:
`C:\Tesi\dati\zone_industriali_fvg\originali\`

## 7. Stato governance 5 HUB

Con DEC-0079 `LOGISTICS_FVG_v02.gpkg / LOGISTICS_FVG_POINTS` è approvato come baseline operativa del MODEL_v2 e `F5_SRC_LOGISTICS_POINTS_001` è ACCEPTED nel DATA_REGISTRY.

Restano invariati i caveat: nella Tesi il dataset è ancora PASS_WITH_LIMITATION / WORKING / NOT FROZEN; `SITE_ID 25 — ZIMA` mantiene `NEEDS_HUMAN_CHECK`; non sono ancora approvati soglie, pesi, bonus o formula di aggregazione delle 26 distanze.
