# INPUT PER PIPELINE CLAUDE — MODEL_v2 LOCALIZZAZIONE 5 HUB ENERGETICI GREEN FVG

Assumere che la pipeline Claude esista già. Non è richiesto progettare una nuova architettura, proporre una nuova metodologia o riaprire le scelte descritte in questo input. Lo scopo è eseguire il MODEL_v2 sui dati forniti, in modo riproducibile, tracciabile e verificabile.

Il modello deve selezionare esattamente 5 poligoni candidati nel Friuli Venezia Giulia. L'unità di localizzazione è il poligono candidato, non un punto rappresentativo. I punti eventualmente creati servono solo a elaborazione o visualizzazione e non sostituiscono la geometria del candidato.

Usare il file `PACKAGE_MANIFEST_MODEL_v2_v01.csv` come indice fisico dei file nel package. I ruoli logici descritti qui sotto devono essere risolti tramite il manifest. Non sostituire un input mancante con un dataset diverso senza documentarlo esplicitamente.

## FILE FORNITI

### 1. Universo candidati — ruolo CANDIDATE_UNIVERSE
GeoPackage con un solo universo candidato definitivo per il run. Il layer contiene poligoni con identificativo `candidate_id`, versione, Comune di origine, classe generatrice G1–G5, source tier, lineage essenziale, flag di currentness/proxy e `area_m2`.

Usare la geometria del poligono per tutte le distanze site-level. Non usare il centroide del candidato al posto della geometria. Ogni candidato del file ha già superato la regola di costruzione dell'universo e la superficie minima lorda di 8.000 m²; non applicare un nuovo filtro di ammissibilità site-level.

Il package deve contenere anche il lineage e il QA associati all'universo candidato. Se il manifest non marca l'universo candidato come READY/ACCEPTED per questo run, non produrre una selezione finale: eseguire solo i controlli e le elaborazioni indipendenti possibili e restituire `PRECHECK_BLOCKED_CANDIDATE_UNIVERSE`.

### 2. Confine FVG — ruolo FVG_BOUNDARY
Il ruolo `FVG_BOUNDARY` è soddisfatto dal layer `fvg_boundary` del medesimo GeoPackage fornito per `HEAVY_EDGE_GEOMETRY`, in EPSG:32632. Non duplicare fisicamente il file nel package. Il layer contiene una geometria regionale e serve esclusivamente per costruire la griglia di copertura territoriale e pesare correttamente le celle di confine.

### 3. Traffico LIGHT — ruoli LIGHT_EDGE_FLOWS e OSM_ROAD_GRAPH
`LIGHT_EDGE_FLOWS` contiene flussi direzionali LIGHT in veicoli/giorno. Usare il campo `dirty_flow_veh_day`. La geometria stradale è nel ruolo `OSM_ROAD_GRAPH`, layer `G_OSM_operativo_segments_v01`, e si associa tramite `segment_uid`.

La rete OSM è in EPSG:32632 e contiene, tra gli altri, `segment_uid`, `way_id`, `length_m`, `highway`, `ref`, `oneway_raw`, `direction_status`, `direction_code` e attributi di accesso. Può essere riutilizzata per routing tecnico quando necessario, mantenendo esplicite le sue limitazioni.

Il flusso LIGHT è una baseline operativa del MODEL_v2 ma deriva da una matrice Dirty FRLM dimostrativa/non canonica rispetto alla tesi. Non presentarlo come domanda LIGHT scientifica definitiva o calibrata.

### 4. Traffico HEAVY — ruoli HEAVY_PATH_FLOWS e HEAVY_EDGE_GEOMETRY
`HEAVY_PATH_FLOWS` contiene i path-flow Heavy. La baseline di score è `heavy_vehicles_day_2030`. Il campo `rerouted_edge_path` contiene la sequenza di `Network_Edge_ID` attraversati da ciascun path.

Ricostruire deterministicamente il flusso per edge 2030 sommando `heavy_vehicles_day_2030` su ogni `Network_Edge_ID` presente nei path. Associare le geometrie dal ruolo `HEAVY_EDGE_GEOMETRY`, layer `speth_geometry_edges`, campo chiave `Network_Edge_ID`, EPSG:32632.

`heavy_vehicles_day_2019` resta solo benchmark/sensitivity. Lo scenario Heavy 2030 è una scelta di coerenza temporale del modello, non un dato localmente calibrato; mantenere espliciti i limiti di bias e granularità della rete Heavy.

### 5. Proxy rete elettrica — ruolo GRID_CP_PROXY
Layer puntuale delle posizioni OSM plausibili per cabine primarie / infrastrutture AT-MT, con 92 record e attributi di operatore, tensione e classe QA. Il CRS sorgente è EPSG:4326; trasformare in CRS metrico per le distanze.

Questi punti sono un proxy territoriale validato con controlli contro aree convenzionali e fonti DSO. Non rappresentano capacità disponibile, hosting capacity, punto di connessione garantito, costo reale o fattibilità tecnica di connessione.

### 6. Poli logistici/industriali — ruolo LOGISTICS_POINTS
GeoPackage `LOGISTICS_FVG_v02.gpkg`, layer `LOGISTICS_FVG_POINTS`, 26 punti in EPSG:32632. Campi principali: `SITE_ID`, `NAME`, `CATEGORY`, `MUNICIPALITY`, provenienza e note.

Usare esclusivamente il layer puntuale. Il record `SITE_ID=25` relativo a ZIMA conserva un caveat di verifica umana e rappresenta il sub-ambito di Manzano, non automaticamente l'intero comprensorio multi-comunale.

### 7. Pericolosità alluvioni PGRA — ruolo PGRA_HAZARD
Snapshot vettoriale della pericolosità alluvioni, layer `Pericolo_direttiva_alluvioni`, EPSG:3035, con campi `OBJECTID` e `PDESCRIPT`. Le classi operative osservate includono `P1`, `P1_ST`, `P1_SM`, `P2`, `P3A`, `P3B`, oltre a `AA` e `F`.

Usare il layer di pericolosità per lo score PGRA. `AA` e `F` restano flag informativi separati e non ricevono uno score di classe P1–P3B.

### 8. Infrastrutture H2 — ruolo H2_INVENTORY
CSV con inventario current-first delle infrastrutture H2 FVG. Campi principali: `H2_SITE_ID`, `NAME`, `COMUNE`, `LOCATION_TEXT`, `LATITUDE`, `LONGITUDE`, `LOCATION_PRECISION`, `LOCATION_CONFIDENCE`, `SCOPE_CLASS`, `STATUS`, capacità separate, fonti e limitazioni.

Per lo score usare esclusivamente i quattro target spaziali:
- `FVG_H2_001` — Hydrogen Hub Trieste;
- `FVG_H2_002` — APT EcoMove Monfalcone / Lisert;
- `FVG_H2_003` — Q8 Porpetto PNRR H2;
- `FVG_H2_005` — ABS Pozzuolo / Cargnacco.

`FVG_H2_004` SOLHX resta nell'inventario fattuale ma è escluso dalle distanze finché la localizzazione resta solo comunale. Testbed e record `ANNOUNCED_UNVERIFIED` non entrano nello score core.

Per i quattro target ammessi, quando non sono presenti coordinate numeriche, materializzare un punto con procedura di georeferenziazione deterministica e auditabile a partire da `LOCATION_TEXT` e dalla precisione dichiarata. Non inventare coordinate. Se non è possibile localizzare in modo affidabile uno dei quattro target, dichiarare il criterio H2 non pienamente valutabile e non sostituire silenziosamente il target.

Al 22 settembre 2026 nessuno dei core site è documentato come `OPERATIONAL`. Lo status è descrittivo e non modifica lo score.

### 9. TEN-T / AFIR — ruoli TENT_CORE, TENT_ROUTE_CROSSWALK e TENT_EXIT_AUDIT
`TENT_CORE` contiene la geometria ufficiale TEN-T Core rilevante per il FVG. `TENT_ROUTE_CROSSWALK` collega le sezioni TENtec agli assi reali FVG. `TENT_EXIT_AUDIT` documenta che, nel dominio FVG verificato, l'accesso rilevante è tramite vere uscite/rampe e non tramite normali intersezioni a raso.

Usare questi file insieme alla rete stradale per le verifiche territoriali AFIR. Se la pipeline dispone già di dati TEN-T o di routing più affidabili, può usarli solo se ne documenta fonte, versione e coerenza con il package.

## CRS E REGOLE GEOMETRICHE GENERALI

Portare ogni confronto spaziale in un CRS metrico coerente. Conservare i CRS sorgente e documentare ogni trasformazione.

Le distanze dei criteri LIGHT, HEAVY, GRID, LOG e H2 sono distanze geometriche minime dalla geometria del poligono candidato all'oggetto target. Non sostituire il poligono con il suo centroide.

La distanza AFIR dalla TEN-T è invece una distanza di guida stradale alla vera uscita/rampa TEN-T pertinente.

## IMPORTANZA CRITERI — DA COMPILARE MANUALMENTE

LIGHT = ____
HEAVY = ____
GRID = ____
LOG = ____
PGRA = ____
H2 = ____
COVERAGE = ____

I valori, una volta compilati manualmente, devono essere interi nella scala 1–5. Non inferire, suggerire o sostituire valori mancanti. Se anche una sola importanza resta `____`, non calcolare lo score finale ponderato e non dichiarare una cinquina selezionata; produrre comunque tutti gli output precomputabili e restituire `WEIGHTS_REQUIRED`.

## ARCHITETTURA DEL MODELLO

Selezionare esattamente 5 `candidate_id` distinti.

Non imporre macro-aree, un Hub per macro-area o una preselezione top-k nella metodologia ordinaria. Questi strumenti sono ammessi solo come fallback computazionale dopo aver documentato una reale intrattabilità del problema e aver quantificato, con sensitivity o benchmark adeguato, il rischio di perdere la migliore configurazione.

Non applicare un vincolo generale di distanza minima di 10 km tra Hub.

Non introdurre criteri aggiuntivi per accessibilità/classe della strada, distanza TEN-T, PAI/frane, BESS, elettrolizzatore o altri fattori non elencati qui. Accesso locale reale, capacità di rete elettrica, proprietà/disponibilità, autorizzazioni e dimensionamento tecnico sono verifiche post-model, non nuovi score.

## CRITERIO LIGHT — FLUSSO VEICOLARE INTERCETTABILE

Per ogni candidato `i`, considerare gli edge LIGHT con geometria entro 5 km dal poligono.

Per ogni edge `e`:
`d_ie` = distanza geometrica minima in km fra poligono candidato ed edge, con `0 <= d_ie <= 5`.

`f(d_ie) = 1 - d_ie / 5`

Calcolare `q_max_LIGHT` come massimo `dirty_flow_veh_day` sull'intera rete di riferimento LIGHT, non sui soli edge vicini al singolo candidato.

`q_norm_e = q_e / q_max_LIGHT`

`S_ie = q_norm_e * f(d_ie)`

`z_i_LIGHT = max_e(S_ie)`

Se non esistono edge utili entro 5 km, `z_i_LIGHT = 0`. Il risultato è già in [0,1]: non applicare una seconda normalizzazione.

## CRITERIO HEAVY — FLUSSO VEICOLARE INTERCETTABILE

Ricostruire prima `q_e^H2030` per `Network_Edge_ID` sommando `heavy_vehicles_day_2030` su tutti i path che attraversano l'edge.

Per ogni candidato applicare la stessa finestra di 5 km e lo stesso decadimento lineare:

`f(d_ie) = 1 - d_ie / 5`

`q_max_HEAVY = max_e(q_e^H2030)` sull'intera rete Heavy di riferimento.

`q_norm_e = q_e^H2030 / q_max_HEAVY`

`S_ie = q_norm_e * f(d_ie)`

`z_i_HEAVY = max_e(S_ie)`

Se non esistono edge utili entro 5 km, `z_i_HEAVY = 0`. Nessuna seconda normalizzazione.

Calcolare separatamente, solo come sensitivity/benchmark, l'analogo risultato 2019 senza sostituirlo alla baseline 2030.

## CRITERIO GRID — PROSSIMITÀ AL PROXY DI CABINA PRIMARIA

Per ogni candidato:
`d_i_GRID = min_j d(poligono_i, CP_proxy_j)`

Sull'intero universo:
`d_max_GRID = max_i(d_i_GRID)`

Score:
`z_i_GRID = 1 - d_i_GRID / d_max_GRID`

Non introdurre soglie artificiali. Il criterio misura solo prossimità territoriale al proxy elettrico.

## CRITERIO LOG — PROSSIMITÀ LOGISTICO-INDUSTRIALE

Per ogni candidato calcolare la distanza geometrica da tutti i 26 poli. Ordinare le distanze e prendere le due minori `d_i(1)` e `d_i(2)`.

`D_i_LOG = [d_i(1) + d_i(2)] / 2`

`D_max_LOG = max_i(D_i_LOG)` sull'intero universo.

`z_i_LOG = 1 - D_i_LOG / D_max_LOG`

Nessuna soglia, bonus o peso per tipologia di polo.

## CRITERIO PGRA — PERICOLOSITÀ ALLUVIONI

Applicare la seguente scala:
- fuori dalle classi P1–P3B = 1,00;
- P1 / P1_ST / P1_SM = 0,75;
- P2 = 0,50;
- P3A = 0,25;
- P3B = 0,00.

Per ogni candidato calcolare `z_i_PGRA` come media degli score di classe pesata per la superficie del candidato ricadente in ciascuna classe. La porzione non ricadente in P1–P3B vale 1,00.

In caso di sovrapposizione spaziale tra classi, assegnare alla porzione sovrapposta la classe peggiore e contarne l'area una sola volta.

Mantenere separati come flag `AA` e `F`; non trasformarli in classi numeriche aggiuntive.

## CRITERIO H2 — PROSSIMITÀ A INFRASTRUTTURA CORE

Per ogni candidato, sui soli quattro target ammessi:
`d_i_H2 = min_j d(poligono_i, H2_core_j)`

Sull'intero universo:
`d_max_H2 = max_i(d_i_H2)`

`z_i_H2 = 1 - d_i_H2 / d_max_H2`

Nessuna soglia, nessun bonus per numero di siti, nessun peso per status.

Il criterio misura prossimità/sinergia con infrastrutture H2 core verificate esistenti, in costruzione o committed; non prova commissioning, accesso pubblico, capacità disponibile o conformità AFIR.

## CRITERIO DI COPERTURA TERRITORIALE DELLA CINQUINA

Costruire una griglia regolare sul territorio FVG. La dimensione della cella è un parametro tecnico: scegliere una risoluzione praticabile, verificare convergenza/sensitivity su almeno una risoluzione più fine o più grossolana e documentare l'effetto sui risultati.

Per ogni cella `g`, usare il centro `c_g`. Per una cinquina `H`:

`d_g(H) = min_{h in H} d(c_g, h)`

dove `d` è la distanza geometrica euclidea in CRS metrico dal centro cella al poligono Hub più vicino.

Per le celle di confine usare come peso `a_g` la sola area della cella ricadente nel FVG.

`D_COV(H) = sum_g[a_g * d_g(H)] / sum_g[a_g]`

Calcolare il benchmark geografico sulla totalità dell'universo candidato:

`D_COV* = min_{|H|=5} D_COV(H)`

Poi:

`Z_COV(H) = D_COV* / D_COV(H)`

La copertura misura distribuzione geografica pura. Non ponderare la griglia per popolazione, traffico, domanda o accessibilità stradale.

Il 95° percentile delle distanze può essere riportato come diagnostica QA, ma non diventa un secondo criterio.

## VINCOLI E QUALITY GATE AFIR / TEN-T

AFIR/TEN-T non produce uno score individuale e non deve essere sommato ai criteri sopra. Opera separatamente come vincolo/quality gate della configurazione.

### Proxy progettuali dei nodi urbani
Usare esplicitamente queste due assunzioni progettuali:
- Comune di Trieste = proxy operativa del nodo urbano TEN-T di Trieste;
- Comune di Udine = proxy operativa del nodo urbano TEN-T di Udine.

La cinquina deve includere almeno un Hub associato al Comune di Trieste e almeno un Hub associato al Comune di Udine. Usare gli attributi comunali dell'universo candidato; se emergono geometrie ambigue rispetto al confine, documentare il trattamento.

Queste sono proxy operative di progetto e non dichiarazioni dei perimetri legali AFIR/TEN-T.

### Regola “lungo TEN-T” per H2
Per stabilire se un Hub può essere conteggiato territorialmente ai fini AFIR, calcolare la distanza stradale alla vera uscita/rampa della TEN-T Core più vicina.

Condizione territoriale:
`road_distance_to_nearest_TENT_exit <= 10 km`

La soglia non è uno score e non è un filtro universale dei candidati. Un Hub oltre 10 km può restare nel modello ma non va contato come stazione “lungo TEN-T” ai fini della copertura AFIR.

Derivare o identificare le uscite in modo riproducibile usando rete stradale, geometrie TEN-T, crosswalk e audit forniti. Non trattare come uscita una normale intersezione a raso non validata.

### Requisito massimo di 200 km
Entro il perimetro normativo effettivamente valutabile con i dati disponibili, verificare la copertura della TEN-T Core rispetto alla distanza massima di 200 km tra le stazioni H2 conteggiate ai fini AFIR.

I 200 km sono una distanza massima di copertura lungo la rete TEN-T Core, non una distanza minima tra Hub e non una distanza euclidea generica.

Non considerare automaticamente le infrastrutture H2 dell'inventario come AFIR-compliant. Per gli Hub selezionati, distinguere almeno:
- conformità territoriale “lungo TEN-T”;
- requisiti tecnici/post-model necessari affinché la futura stazione possa essere conteggiata ai fini AFIR.

Se il package FVG non consente di verificare i tratti esterni alla regione o le stazioni confinanti necessarie per una verifica normativa completa, calcolare la parte verificabile, quantificare il perimetro controllato e dichiarare il resto come `NOT_EVALUABLE_WITH_PACKAGE`. Non inventare stazioni esterne.

### Monfalcone / Lisert
Monfalcone/Lisert è pienamente utilizzabile nel modello localizzativo e nel criterio H2.

Per il candidato Hub pertinente:
- verificare la distanza stradale alla nearest TEN-T exit con la regola <=10 km;
- mantenere esplicito che l'impianto Lisert documentato è sotto 1 t H2/giorno;
- non dimensionare nel MODEL_v2 la capacità aggiuntiva;
- non penalizzare né escludere la localizzazione per questo deficit;
- trattare il requisito di capacità come requisito progettuale post-model.

Il candidato può coincidere con il poligono dell'infrastruttura esistente, come integrazione/potenziamento, oppure essere un poligono distinto vicino con la stessa funzione strategica.

## AGGREGAZIONE DEI CRITERI E FUNZIONE OBIETTIVO

Per ciascun criterio site-level `j in {LIGHT, HEAVY, GRID, LOG, PGRA, H2}` e per una cinquina `H`:

`Z_j(H) = (1/5) * sum_{i in H} z_ij`

La copertura `Z_COV(H)` è calcolata direttamente sulla cinquina e non deriva dalla media di score site-level.

Dopo la compilazione manuale delle sette importanze:

`Q(H) = [sum_j r_j * Z_j(H) + r_COV * Z_COV(H)] / [sum_j r_j + r_COV]`

Ogni criterio entra una sola volta nella ponderazione finale. Non calcolare prima uno score candidato ponderato da ripesare poi sulla cinquina.

Il MODEL_v2 è single-objective. Con importanze compilate, selezionare la cinquina con massimo `Q(H)` tra le configurazioni che soddisfano i vincoli di configurazione verificabili.

Se il gate AFIR è solo parzialmente valutabile, non dichiarare “AFIR compliant” la soluzione: identificare la migliore configurazione sotto i vincoli effettivamente verificati e marcarla `CONDITIONAL_AFIR_VERIFICATION`.

## MARGINE DI MANOVRA COMPUTAZIONALE

La pipeline può scegliere:
- strutture dati, indici spaziali e formati intermedi;
- algoritmo di ottimizzazione esatto o euristico;
- strategie di pruning che non eliminino a priori configurazioni potenzialmente ottime senza controllo;
- dimensione pratica della griglia con sensitivity/convergenza;
- modalità tecnica di materializzazione delle uscite TEN-T e dei quattro punti H2;
- parallelizzazione e caching;
- ulteriori output diagnostici.

Ogni euristica o riduzione dello spazio di ricerca deve essere documentata e accompagnata da controlli sufficienti a stimare il rischio di perdita dell'ottimo. Preferire metodi deterministici o fissare e registrare eventuali seed.

La pipeline non può cambiare le formule, inventare criteri, assegnare importanze, trasformare proxy in fatti, modificare l'universo candidato o sostituire dati mancanti con valori inventati.

## OUTPUT RICHIESTI

Produrre almeno:

1. `candidate_scores.csv` o equivalente machine-readable, una riga per candidato, con identificativi, valori raw, distanze/quantità intermedie rilevanti e score `z_i_LIGHT`, `z_i_HEAVY`, `z_i_GRID`, `z_i_LOG`, `z_i_PGRA`, `z_i_H2`.
2. Un layer GIS dei candidati con gli stessi score e `candidate_id` invariato.
3. `configuration_results.csv` o equivalente con le configurazioni confrontate o la shortlist rilevante, i sei `Z_j(H)`, `D_COV(H)`, `Z_COV(H)`, stato dei gate AFIR e `Q(H)` quando le importanze sono compilate.
4. Identificazione univoca della cinquina selezionata, con i cinque `candidate_id`, solo quando pesi e gate necessari consentono una selezione.
5. Layer GIS dei 5 Hub selezionati.
6. Output derivato delle uscite TEN-T usate e delle distanze stradali candidato–uscita per i cinque Hub selezionati o per le configurazioni finaliste.
7. Output dei quattro punti H2 effettivamente usati, con metodo/qualità della georeferenziazione.
8. Report sintetico di assunzioni, limitazioni, dati non valutabili e caveat.
9. Report QA con controlli numerici e spaziali.
10. Sensitivity/robustness almeno su risoluzione della griglia; includere anche confronto Heavy 2030 vs 2019 come benchmark. Ulteriori sensitivity devono restare coerenti con i parametri realmente disponibili.

## CONTROLLI MINIMI DI COERENZA

Prima del calcolo:
- verificare presenza, hash e stato dei file indicati nel manifest;
- verificare unicità di `candidate_id`, geometrie valide e area >= 8.000 m² per il 100% dei candidati;
- verificare che nessun candidato sia aggiunto, dissolto, eliminato o riclassificato dalla pipeline;
- verificare CRS e trasformazioni;
- verificare che i campi di flusso siano numerici e non negativi;
- verificare il join LIGHT `segment_uid` e il join HEAVY `Network_Edge_ID`;
- verificare che i quattro e soli quattro target H2 ammessi siano quelli usati nello score;
- verificare che `q_max_LIGHT`, `q_max_HEAVY`, `d_max_GRID`, `D_max_LOG` e `d_max_H2` siano calcolati sull'intero universo/rete di riferimento prevista e non su subset opportunistici.

Dopo il calcolo:
- tutti gli score normalizzati devono ricadere in [0,1], salvo tolleranza numerica documentata;
- per PGRA, le aree usate nella media devono ricostruire l'area del candidato senza doppio conteggio;
- per ogni cinquina devono esserci esattamente 5 `candidate_id` distinti;
- verificare separatamente la presenza di almeno un Hub a Trieste e uno a Udine;
- verificare e riportare la regola <=10 km stradali per ogni Hub che si intende conteggiare ai fini AFIR;
- verificare il requisito dei 200 km sul perimetro TEN-T Core effettivamente valutabile;
- verificare coerenza tra tabella finale e layer GIS;
- registrare tempi, versione del codice, configurazione, seed eventualmente usato e hash degli output principali.

## LIMITAZIONI DA NON NASCONDERE

Il MODEL_v2 è un modello strategico di localizzazione, non una due diligence progettuale. Non dimostra proprietà/disponibilità dei terreni, autorizzabilità, accesso locale definitivo, capacità elettrica residua, costo di connessione, commissioning H2 o conformità tecnica finale AFIR.

Il criterio LIGHT usa una baseline Dirty FRLM operativa ma non canonica rispetto alla tesi. Il criterio HEAVY 2030 usa una rete sovralocale e uno scenario con limiti di calibrazione locale. Il criterio GRID è un proxy di prossimità, non una misura di capacità. Il dataset logistico contiene il caveat ZIMA. La localizzazione H2 deve rispettare la precisione documentata. Le proxy comunali di Trieste e Udine non sono perimetri legali dei nodi urbani.

PAI/frane non entra nello scoring corrente. L'assenza del criterio non equivale ad assenza di rischio e deve restare una verifica post-model.

## OBIETTIVO FINALE

Usare i file del package e le regole sopra per calcolare in modo riproducibile i sei criteri site-level, la copertura territoriale della cinquina, i gate AFIR/TEN-T e, solo dopo compilazione manuale delle sette importanze, la funzione obiettivo unica del MODEL_v2.

Restituire la migliore cinquina identificata dal modello insieme a tutti i valori che ne permettono la ricostruzione, distinguendo sempre dato osservato, proxy, assunzione progettuale, requisito normativo, limitazione e requisito post-model.
