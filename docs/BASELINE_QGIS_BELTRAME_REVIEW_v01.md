# BASELINE QGIS BELTRAME — REVIEW v01

**Data review:** 2026-09-18
**Stato:** HISTORICAL / NON_AUTHORITATIVE
**Pacchetto:** `QGZ_Beltrame.zip`
**SHA256:** `AB2591E6DED67D7B165E0702400DF7270EB8EF1966EF80B68C966F0F4459E614`
**Archivio ufficiale:** `5_HUB_FVG\00_baseline\claude_qgis\QGZ_Beltrame_20260918\QGZ_Beltrame.zip`

## 1. Scopo della review

Valutare il contenuto del pacchetto QGIS storico per capire quali elementi possano essere utili al nuovo progetto 5 HUB senza ereditare automaticamente metodologia, filtri, ranking o risultati della baseline precedente.

## 2. Struttura del pacchetto

Il ZIP contiene esattamente due file:
- `fvge.gpkg` — GeoPackage, 249.470.976 byte;
- `fvge.qgz` — progetto QGIS, 783.165 byte.

Il progetto QGIS usa EPSG:6708. È stato creato il 2026-07-29; metadata autore `Augusto Pellis`; ultimo salvataggio 2026-09-08 con QGIS 3.44.14-Solothurn da `Enrico Beltrame`.
## 3. Struttura QGIS

Il progetto contiene 147 istanze di layer:
- 131 OGR;
- 14 WFS;
- 2 memory layer.

Le 131 istanze OGR corrispondono a 12 layer GeoPackage unici più 119 viste comunali filtrate della stessa tabella `aree_candidate_amministrativo`.

I 14 WFS puntano al GeoServer ufficiale della Regione FVG e richiamano:
- aree cabine primarie;
- aree inondate della Carta Geologica;
- confini comunali, provinciali e regionali;
- grafo stradale FVG;
- interporti;
- limiti amministrativi INSPIRE;
- Natura 2000 ZPS;
- pericolosità frane;
- siti protetti;
- uso del suolo CORINE;
- zone commerciali;
- zone industriali e artigianali.

Questi riferimenti sono **fonti candidate da validare**, non dataset già approvati nel nuovo progetto.
## 4. Contenuto del GeoPackage

Il GeoPackage contiene 14 layer vettoriali:
- `aree_candidate` — 1.377 poligoni;
- `aree_candidate_amministrativo` — 1.377 poligoni;
- `esiti_esclusioni` — 1.377 poligoni;
- `esito_mca` — 1.114 poligoni;
- `localizzazioni_proposte` — 5 poligoni;
- `pgra_pericolosita_idraulica` — 127.639 multipoligoni;
- `pgra_rischio_idraulico` — 87.001 multipoligoni;
- layer TEN-T core/comprehensive stradali, nodi urbani, porti e terminal ferro-strada;
- `uscite_tent_core` — 23 punti;
- `area_servizio_10km` — 23 geometrie multilineari di rete.

Tutte le 1.377 geometrie candidate sono poligoni validi, non vuoti, con `area_id` univoco; non risultano sovrapposizioni positive >1 m². Sono presenti solo 8 coppie di poligoni che si toccano.
## 5. Catena storica candidato → esclusione → MCA → cinquina

La geometria dei layer derivati coincide esattamente con quella del candidato avente lo stesso `area_id`:
- `aree_candidate_amministrativo`: 1.377/1.377;
- `esiti_esclusioni`: 1.377/1.377;
- `esito_mca`: 1.114/1.114;
- `localizzazioni_proposte`: 5/5.

Esiti storici:
- 1.114 candidate ammesse;
- 263 escluse;
- 245 escluse per `fuori_dalla_rete_tent_afir`;
- 13 per `vincolo_assoluto`;
- 3 per `vulnerabilita_ambientale_elevata`;
- 2 con motivazioni multiple.

La MCA divide gli ammessi in quartili quasi perfetti: A=279, B=278, C=278, D=279. La tavola QGIS dichiara infatti: `Classi ai quartili della distribuzione dei punteggi degli ambiti ammessi`.
## 6. Cinquina storica

La baseline contiene 5 localizzazioni proposte:
1. `FVGE-929` — Remanzacco 2 — posizione MCA 1;
2. `FVGE-1309` — Muggia 2 — posizione 21;
3. `FVGE-992` — Cervignano Del Friuli 11 — posizione 50;
4. `FVGE-600` — Cassacco 3 — posizione 123;
5. `FVGE-876` — Pavia Di Udine 7 — posizione 125.

La TAV_05 le descrive esplicitamente come:
`Migliore cinquina conforme ai vincoli d'insieme AFIR — applicazione dimostrativa, valori da confermare`.

Questa dicitura è coerente con il trattamento del pacchetto come baseline storica e non come risultato validato.

## 7. Evidenza critica sulla soglia di superficie

`aree_candidate` contiene il campo `superficie_disponibile_mq` e la superficie geometrica coincide con il valore attributo.

La superficie minima osservata è **5.016,2 m²**; nessun candidato scende sotto 5.000 m². Questo è fortemente coerente con un pre-filtro storico a 5.000 m².
Nel nuovo progetto una soglia universale di 5.000 m² non è stata approvata. La Fase 1 FROZEN stabilisce che non deve essere introdotta una superficie minima arbitraria.

**Conseguenza:** le 1.377 aree non possono essere adottate direttamente come universo candidati del nuovo modello senza ricostruire e verificare la procedura che le ha generate.

## 8. Provenienza e riproducibilità

Il progetto dichiara come fonti generali TENtec, IRDAT FVG, Carta geologica regionale e grafo stradale regionale e si presenta come elaborazione riproducibile tramite `fvge.qgz` + `fvge.gpkg`.

Tuttavia nel pacchetto non è presente una lineage completa delle trasformazioni che hanno prodotto `aree_candidate`, i criteri di esclusione, il punteggio MCA o la cinquina. `projectModels` è vuoto e non risultano join che ricostruiscano la pipeline.

Di conseguenza la riproducibilità del **file QGIS** è buona, mentre la riproducibilità della **metodologia di generazione dei risultati** non è dimostrata dal solo pacchetto.

## 9. Uso consentito nel nuovo progetto

### Fase 2
Usare il pacchetto come caso storico per studiare la distinzione tra:
- area candidata;
- punto/uscita TEN-T;
- accessibilità di rete;
- distanza stradale di servizio.

Non assumere queste scelte come già approvate.
### Fase 3
Usare i 14 WFS e i layer TEN-T/PGRA come inventario di **fonti da verificare**. Ogni fonte va ricontrollata per versione, copertura, licenza, data e adeguatezza.

### Fase 4
Usare `aree_candidate` come benchmark storico e come supporto alla ricostruzione della possibile origine geometrica. Non usarlo come `CANDIDATES_RAW` autorevole finché la generazione non è ricostruita e validata.

### Fasi 5–10
`esiti_esclusioni`, `esito_mca` e `localizzazioni_proposte` sono esclusivamente benchmark storici. Non trasferire automaticamente motivi di esclusione, soglie, pesi, punteggi o cinquina nel nuovo modello.

## 10. Valutazione finale

**DA CONSERVARE:** sì.

**DA RIUSARE DIRETTAMENTE COME INPUT AUTOREVOLE:** no, allo stato attuale.

**VALORE PRINCIPALE:**
1. geometrie storiche candidate tecnicamente pulite;
2. inventario di fonti GIS regionali utili;
3. layer TEN-T/PGRA già organizzati;
4. struttura QGIS e tavole utili come benchmark;
5. evidenza concreta delle scelte e dei risultati del modello storico per il futuro confronto di Fase 13.

## 11. Regola di riuso

Se un singolo layer del pacchetto verrà riutilizzato nel nuovo modello, dovrà essere estratto/copiato in una posizione tecnica appropriata, registrato autonomamente nel DATA_REGISTRY e validato rispetto alla fonte originaria. Il ZIP storico resta immutato in `00_baseline`.
