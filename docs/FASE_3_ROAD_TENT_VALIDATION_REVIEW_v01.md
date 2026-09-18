# FASE 3 — Rete stradale, accessi e TEN-T — Review Chat 3.3

**Chat:** 3.3 — Rete stradale, accessi e TEN-T
**Data:** 2026-09-18
**Stato documento:** REVIEW
**Esito Chat 3.3:** PASS tecnico-operativo con gap esplicitamente delimitati
**FASE 3:** IN CORSO — non CLOSED, non FROZEN
**Regia metodologica:** Chat Madre 5 HUB

## 1. Scopo e confini

Il mandato è verificare e delimitare con evidenza ISS-0004 e ISS-0005 prima della costruzione dei candidati.

La chat non costruisce candidati, accessi reali, road anchor reali, connettori candidato–rete, exit set TEN-T operativo, indicatori, punteggi o ranking.

Le baseline FROZEN di Fase 1 e Fase 2 non sono modificate.

La catena futura resta:

candidate polygon -> access point -> road anchor -> road network -> TEN-T exit/node

Il punto rappresentativo del candidato non è un accesso e non è origine implicita del routing.

## 2. Fonti e baseline verificate

Baseline locali:
- docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md — FROZEN;
- docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md — FROZEN;
- docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md;
- docs/DISPATCH_CHAT_3.3_ROAD_TENT_VALIDATION_v01.md.

Governance viva:
- PROJECT_SOURCE_OF_TRUTH verificato su Google Drive;
- PROJECT_CONTROL_REGISTER verificato, in particolare DATA_REGISTRY e ISSUES;
- ISS-0004 e ISS-0005 risultavano OPEN all’avvio.

Fonti esterne principali:
- Regione Autonoma FVG / IRDAT / GeoServer, RETI_TRASP:GRAFO_STRADALE_FVG;
- Commissione europea / DG MOVE, Reg. (UE) 2024/1679 e cartografia TEN-T 2024;
- TENtec public REST services e European Transport Corridors;
- fonti ufficiali dei gestori per evidenza dell’esistenza di restrizioni Heavy dinamiche.

## 3. Grafo stradale FVG — snapshot e schema

Snapshot materializzato dal WFS regionale il 2026-09-18:

5_HUB_FVG\01_raw_data\F3_CHAT_3_3\GRAFO_STRADALE_FVG_WFS_20260918.geojson

Caratteristiche:
- feature: 75.546;
- geometrie: 75.546 LineString;
- CRS dichiarato dal WFS: EPSG:6708;
- geometrie invalide: 0;
- geometrie vuote: 0;
- lunghezza zero: 0;
- lunghezza geometrica complessiva: 13.524,087 km;
- SHA-256: 81BFD7E97300F12230324440C40A7944DAB7075EC2EA2CC5FCB9AE6201C72B8E.

Lo schema include, tra gli altri: CLASSE, ENTE_GESTORE, DIR, ENTEXT, TRIM_USAGE_ALLOWANCE, TRIM_LANES, GEOMETRY_REVERSED, FONTE_INT e campi di validità.

La lineage interna non è omogenea. FONTE_INT include CTRN, Catasto Strade, TeleAtlas, Autovie Venete, OSM e altre fonti. Il grafo va quindi trattato come integrazione regionale e non come rilievo monolitico con qualità uniforme.

## 4. Audit topologico

È stato costruito un grafo diagnostico non orientato sugli endpoint delle feature, arrotondati a 1 mm. Questa scelta serve solo a misurare la connettività dichiarata dalle feature, non a imporre nuovi nodi agli incroci geometrici.

Risultati:
- nodi endpoint: 59.945;
- archi: 75.546;
- componenti connesse: 21;
- componente gigante: 75.502 archi, pari al 99,9418% degli archi;
- quota lunghezza nella componente gigante: 99,8767%;
- nodi di grado 1: 2.935;
- archi isolati: 9;
- dangling con altro nodo distinto entro 0,1 m: 136;
- entro 1 m: 137;
- entro 5 m: 150.

I dangling non sono automaticamente errori: comprendono cul-de-sac e limiti reali. I valori entro pochi metri sono soltanto candidati a micro-gap da ispezionare.

L’audit delle intersezioni geometriche ha contato:
- 126.373 intersezioni endpoint–endpoint;
- 42 endpoint–interior;
- 1.022 interior–interior;
- 1 coppia con overlap lineare;
- 1.064 punti potenzialmente non nodati in un grafo basato sui soli endpoint.

Molti esempi coinvolgono autostrade/raccordi e viabilità locale e possono essere correttamente separati in quota. Pertanto non è ammissibile spezzare automaticamente tutte le intersezioni geometriche. Eventuali correzioni topologiche future devono distinguere incroci a raso, cavalcavia/sottopassi e duplicazioni.

## 5. Test di connettività Light — solo sanity check

È stato eseguito un test di raggiungibilità sul grafo non orientato, con peso pari alla lunghezza geometrica, usando sette probe territoriali: Pordenone, Udine, Gorizia, Trieste, Tolmezzo, Tarvisio e Lignano Sabbiadoro.

Tutte le coppie risultano raggiungibili nella componente operativa.

Esempi di distanza diagnostica:
- Pordenone–Udine: 49,86 km;
- Udine–Gorizia: 36,84 km;
- Gorizia–Trieste: 43,63 km;
- Udine–Tarvisio: 87,78 km;
- Tolmezzo–Tarvisio: 60,20 km.

Questi numeri non sono output del modello: ignorano sensi unici, divieti, restrizioni veicolari e accessi reali e servono soltanto a verificare che la geometria regionale non sia frammentata macroscopicamente.

## 6. Direzionalità — esito critico

### 6.1 DIR

DIR non è un flag di senso unico.

Distribuzione principale:
- nd: 65.629 feature;
- i restanti valori sono in larga parte destinazioni o denominazioni direzionali, ad esempio Palmanova, Tarvisio, Trieste, Venezia, Sistiana.

Sulle principali autostrade il campo descrive chiaramente la direzione nominale:
- A4: Venezia / Trieste;
- A23: Palmanova / Tarvisio;
- A28: Conegliano / Portogruaro;
- A34: Villesse / Gorizia.

DIR può contribuire alla lettura semantica della carreggiata, ma non può essere trasformato in un booleano one-way senza una regola documentata.

### 6.2 TRIM_USAGE_ALLOWANCE

Valori osservati sul dataset:
- 0: 60.217;
- 1: 12.338;
- 2: 2.462;
- NULL: 529.

Nel materiale pubblico ispezionato non è stata trovata una definizione affidabile dei codici 0/1/2 sufficiente per usarli come regola di percorrenza.

Inoltre la copertura è incompatibile con un uso ingenuo come flag direzionale:
- A4: 162/162 NULL;
- A28: 109/109 NULL;
- A34: 45/47 NULL;
- A23: prevalentemente 1, ma 49 NULL;
- RA13 e RA14: prevalentemente 1.

GEOMETRY_REVERSED distingue il verso geometrico di alcune feature, ma non prova da solo la legalità della percorrenza.

### 6.3 Conseguenza

Il grafo regionale è idoneo come base geometrica e per screening di connettività non orientata, ma NON è ancora validato come rete di routing Light diretta/legalmente percorribile.

Non viene introdotta alcuna correzione o inferenza implicita dei sensi di marcia.

## 7. Heavy routing

Lo schema ispezionato non contiene un set sufficiente e documentato di restrizioni Heavy, per esempio massa totale, massa per asse, altezza, larghezza, lunghezza, sagoma, divieti locali ai mezzi pesanti e restrizioni temporanee o stagionali.

Fonti ufficiali regionali mostrano che sulla rete reale esistono limitazioni variabili per massa, dimensioni, direzione e periodo. Queste informazioni non sono ricostruibili dal solo snapshot statico del grafo.

Conclusione: F3_SRC_FVG_ROADGRAPH_001 da solo non è idoneo a routing Heavy di produzione.

Per una rete Heavy futura sarà necessario sovrapporre almeno:
1. restrizioni strutturali permanenti;
2. ordinanze/restrizioni dei gestori;
3. eventuali limitazioni temporanee con data di validità;
4. compatibilità del singolo accesso e connector con il veicolo Heavy.

Non è stata inventata alcuna restrizione mancante.

## 8. TEN-T corrente — gerarchia autorevole

La rete TEN-T vigente è trattata secondo il Reg. (UE) 2024/1679 e la cartografia DG MOVE 2024 a tre livelli:
- core;
- extended core;
- comprehensive.

Le mappe ufficiali 2024 e gli allegati normativi sono stati materializzati in OneDrive.

Annex1_listing8_HRITMTSI_2024.pdf
- SHA-256 6C0CD7607C071B15968D8C75213067176F0D78457E80927078469716DC233556.

TEN-T-guidelines-2024-annex-2.pdf
- SHA-256 CC33C50BC6D2A96A3CEDB5E47DAB582B8564760DE8479867BBB788BC8DBC7E65.

L’Annex I usa esplicitamente la legenda Roads Core / Roads Extended Core / Roads Comprehensive. L’Annex II identifica i nodi TEN-T.

Nel FVG l’Annex II include, tra gli elementi rilevanti:
- Monfalcone: porto marittimo comprehensive e porto interno comprehensive;
- Pordenone: terminale ferroviario-stradale comprehensive;
- Porto Nogaro: porto interno comprehensive;
- Trieste: nodo urbano; aeroporto comprehensive; porto marittimo core; porto interno core; RRT core (Fernetti);
- Udine: nodo urbano.

Questi nodi sono inventario normativo/territoriale; non sono candidati Hub.

## 9. TENtec REST: corrente vs legacy

Il servizio pubblico storico tentec_public_services_ext espone ancora gruppi Comprehensive Network e Core Network, senza un gruppo Extended Core Network.

Per questo motivo non viene usato come fonte autorevole della tassonomia 2024 a tre livelli. È conservato come evidenza/benchmark legacy.

Metadato materializzato:
tentec_public_services_ext_metadata_20260918.json
- SHA-256 4F7B61F372FE186C5E3A52BE45127A05AD8176C151DC5011DEDBFA06DD854F59.

Sono state estratte anche le geometrie FVG dei layer stradali legacy core e comprehensive, ma restano HISTORICAL/LEGACY SUPPORT ONLY.

Il servizio tentec_public_corridors_ext è invece coerente con i European Transport Corridors 2024. I layer stradali dei corridoi Baltic Sea–Adriatic Sea e Mediterranean interrogati sul FVG restituiscono feature con CORE_NETWORK=1.

Il crosswalk tecnico campionato con il grafo FVG associa in modo netto tali tratti, tra gli altri, ad A4, A23, RA13 e all’asse di collegamento di Trieste/Fernetti.

Questo crosswalk è corroborativo, non sostituisce una classificazione route-level completa dei tre livelli.

## 10. Limite residuo della classificazione stradale TEN-T

La cartografia ufficiale 2024 dimostra la tassonomia corrente a tre livelli. Il servizio corrente dei corridoi consente di corroborare tratti core.

Non è stato però individuato, nel mandato corrente, un layer pubblico REST unico che fornisca in modo direttamente interrogabile e documentato la completa classificazione core / extended core / comprehensive di ogni tratto stradale FVG.

Pertanto:
- non viene riciclata la tassonomia legacy a due livelli;
- non viene inferita la classe mancante per semplice prossimità;
- non viene dichiarato “nessun extended core in FVG” per assenza nel subset dei corridoi;
- il crosswalk route-level completo rimane attività successiva.

## 11. Uscite TEN-T — lineage futura

Le 23 uscite del progetto storico non vengono riutilizzate come insieme autorevole: la loro lineage non è sufficiente.

La futura materializzazione deve creare un artifact versionato, indicativamente TENT_EXIT_SET_v01, derivato da una baseline TEN-T corrente e da fonti di svincoli/intersezioni verificabili.

Campi minimi proposti:
- tent_exit_id;
- tent_snapshot_id e versione;
- network_level;
- route_id / gestore;
- junction_or_exit_source_id;
- nome e, se disponibile, progressiva/km ufficiale;
- geometria;
- road_anchor_id;
- fonte, data, hash/evidence;
- validation_status;
- valid_from / valid_to se necessario;
- classe interpretativa dell’elemento.

Per autostrade e strade a accesso controllato l’uscita deve derivare da uno svincolo reale verificabile, non da ogni incrocio geometrico.

Per i tratti TEN-T ordinari a raso resta una questione metodologica sostanziale: come tradurre operativamente il concetto AFIR di “nearest exit” quando non esiste uno svincolo autostradale univoco.

Q-METH-3.3-A — PROPOSED / da sottoporre alla Chat Madre e all’utente:
definizione operativa di nearest TEN-T road exit sui tratti non a accesso controllato, senza alterare i limiti AFIR già FROZEN in Fase 1.

## 12. Data contract futuro per accessi e rete

Nessun record reale è stato creato. Si definisce solo il contratto minimo coerente con F2-D4.

### 12.1 access_point

Campi minimi:
- access_id;
- candidate_id, candidate_version;
- geometria;
- relazione con bordo/perimetro;
- ruolo ingresso/uscita/bidirezionale;
- light_status, heavy_status;
- validation_status;
- fonte/evidence, data e versione;
- note su legalità/fattibilità fisica.

Sono ammessi più accessi per candidato. L’assenza di accessi validabili deve essere esplicita e non tradotta in eliminazione silenziosa.

### 12.2 road_anchor

Campi minimi:
- anchor_id, access_id;
- snapshot della rete e feature sorgente;
- geometria e posizione lungo la feature;
- classe e gestore;
- node/edge id della topologia;
- relazione lato/verso solo se validata;
- metodo di snap, distanza effettiva e stato;
- evidence/versione.

Una distanza di ricerca futura è un parametro da motivare e approvare; non viene fissata in questa chat.

### 12.3 connector

Campi minimi:
- connector_id, access_id, anchor_id;
- geometria LineString;
- lunghezza;
- percorribilità Light/Heavy;
- natura pubblica/privata se disponibile;
- barrier/crossing flags;
- fonte/evidence;
- validation_status.

Il nearest road può al massimo proporre un anchor da verificare. Non prova l’esistenza di un accesso fisico o legale.

## 13. Disposizione di ISS-0004

**Stato proposto: OPEN — delimitato con evidenza.**

Accertato:
- geometria valida e copertura regionale consistente;
- componente gigante >99,9% degli archi;
- reachability non orientata su probe territoriali: PASS;
- DIR non è un flag one-way;
- semantica operativa di TRIM_USAGE_ALLOWANCE non validata;
- allowance fortemente incompleto su A4/A28/A34;
- 1.064 intersezioni geometriche candidate non possono essere nodate alla cieca;
- restrizioni Heavy insufficienti.

Conclusione operativa:
- Light non orientato / screening: utilizzabile;
- Light diretto di produzione: NON VALIDATO;
- Heavy di produzione: NON IDONEO con il solo grafo regionale.

Prossimo passo necessario: definire una sorgente/regola di direzionalità documentata e un layer di restrizioni Heavy prima dell’uso per distanze AFIR definitive.

## 14. Disposizione di ISS-0005

**Stato proposto: OPEN — delimitato con evidenza.**

Accertato:
- fonte normativa/cartografica corrente 2024 materializzata e hashata;
- tassonomia a tre livelli verificata;
- nodi FVG dell’Annex II identificati;
- legacy public REST a due livelli identificato come non sufficiente;
- corridoi 2024 e tratti core FVG corroborati;
- storico set di 23 uscite escluso dall’uso autorevole;
- lineage minima del futuro exit set definita.

Residuo:
- crosswalk stradale FVG completo e machine-readable dei tre livelli;
- definizione operativa dell’exit sui tratti a raso;
- costruzione futura e validazione di TENT_EXIT_SET_v01.

## 15. Quality gate Chat 3.3

- [x] Dispatch e baseline FROZEN letti e rispettati.
- [x] PROJECT_SOURCE_OF_TRUTH e registri vivi verificati.
- [x] Snapshot WFS materializzato e hashato.
- [x] Geometria, validità e connettività quantificate.
- [x] Dangling, componenti, micro-gap e crossing candidate quantificati.
- [x] Direzionalità non inferita da campi non documentati.
- [x] Light delimitato: screening non orientato utilizzabile; routing diretto non validato.
- [x] Heavy delimitato: grafo statico insufficiente.
- [x] TEN-T corrente trattata a tre livelli.
- [x] Legacy TENtec a due livelli separato dalla baseline corrente.
- [x] Nodi TEN-T FVG documentati.
- [x] Historical 23 exits non riutilizzati.
- [x] Lineage del futuro exit set definita.
- [x] Data contract futuro access / anchor / connector definito senza record reali.
- [x] Nessuna soglia di snap inventata.
- [x] Nessun candidato, accesso o ranking costruito.
- [x] Nessuna baseline FROZEN modificata.

**Esito:** PASS tecnico-operativo della Chat 3.3.

Il PASS significa che i due issue sono stati sufficientemente verificati e delimitati per la regia. Non significa che ISS-0004 o ISS-0005 siano risolti, né che la Fase 3 possa essere chiusa o congelata.

## 16. Artifact e riproducibilità

Script versionabili:
- scripts/audit_roadgraph_chat3_3_v01.py;
- scripts/audit_roadgraph_intersections_chat3_3_v01.py;
- scripts/audit_roadgraph_reachability_chat3_3_v01.py;
- scripts/crosswalk_tentec_corridor_fvg_chat3_3_v01.py.

Output OneDrive:
- ROADGRAPH_AUDIT_METRICS_v01.json — SHA-256 324DBD888F4122425D6A2A449D7C67C8A90E712979EE04C25700099A481F01C0;
- ROADGRAPH_INTERSECTION_AUDIT_v01.json — 6E9E341818D9088D04BA78E438BFC04DF23B56F5C88408935B2B0D936EA71E5A;
- ROADGRAPH_NONNODED_INTERSECTION_EXAMPLES_v01.csv — 8D00DFB6DE92E6D89E63651D1ED92BA44B24F13758F4664CF5290577812DB2A1;
- ROADGRAPH_REACHABILITY_TEST_v01.json — F808B3F4B1021E63DA7F89A1C35AC76DB3D7E2358E0C3479C08F46335CC2B517;
- TENTEC_CORRIDOR_TO_FVG_ROAD_CROSSWALK_v01.csv — D85E45FBDDA39D76D2513546E395EEA5688AE8056EFB25FDCB33104A9DE4392B.

I file pesanti restano in OneDrive e non vengono aggiunti a Git.

## 17. Decisioni non assunte dalla Chat 3.3

La chat non approva:
- un algoritmo definitivo di routing;
- una semantica non documentata per TRIM_USAGE_ALLOWANCE;
- una correzione automatica della topologia;
- un layer definitivo di restrizioni Heavy;
- una baseline completa route-level TEN-T 3-tier;
- la definizione AFIR di exit per tratti a raso;
- tolleranze di snap;
- procedure di generazione degli accessi.

Questi elementi restano REVIEW/PROPOSED o OPEN e richiedono regia/approvazione quando metodologicamente sostanziali.
