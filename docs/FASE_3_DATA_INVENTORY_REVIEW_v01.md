# FASE 3 — DATA INVENTORY REVIEW v01

**Chat:** 3.1 — Inventario master e gap analysis dei dati  
**Data:** 2026-09-18  
**Stato documento:** REVIEW  
**Stato Fase 3:** IN CORSO — questo documento non chiude né congela la Fase 3  
**Baseline vincolanti:** `FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` e `FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md` — FROZEN  
**Mandato:** `DISPATCH_CHAT_3.1_DATA_INVENTORY_GAP_ANALYSIS_v01.md`

## 1. Scopo e confini

Questo documento costruisce l'inventario master verificabile delle fonti dati disponibili o candidate per la Fase 3 del progetto 5 HUB.

Distingue esplicitamente:
- dato materialmente disponibile;
- fonte primaria o candidata;
- verifica effettivamente eseguita;
- dato già verificato per un futuro uso modellistico;
- limite noto;
- gap residuo e attività necessaria.

Non costruisce `CANDIDATES_RAW`, non fissa una superficie minima, non introduce indicatori, pesi o ranking, non modifica artifact FROZEN e non promuove automaticamente a dato validato materiale proveniente dalla baseline Claude/QGIS.

La priorità operativa è:
1. P1 — fonti per generare in futuro i poligoni candidati;
2. P2 — rete stradale, accessi e TEN-T;
3. P3 — vincoli territoriali e fattibilità, inclusa la rete elettrica.

## 2. Stato di governance verificato

Alla data del 2026-09-18 è stato letto lo stato vivo su Google Drive.

### 2.1 PROJECT_SOURCE_OF_TRUTH

Stato rilevato:
- progetto ACTIVE;
- FASE 1 = PASS / CLOSED / FROZEN;
- FASE 2 = PASS / CLOSED / FROZEN;
- FASE 3 = IN CORSO;
- FASE 4 non apribile prima del PASS/CLOSED formale della Fase 3;
- Chat 3.1 autorizzata con dispatch già versionato al commit `79fc4f1`.

### 2.2 PROJECT_CONTROL_REGISTER

`DATA_REGISTRY` conteneva, prima di questa attività, solo:
- `BL_CLAUDE_001`;
- `BL_CLAUDE_QGIS_001`.

Entrambi sono baseline storiche/non autorevoli e restano tali.

`ISSUES` conteneva inoltre `ISS-0002`, OPEN: l'universo storico di 1.377 candidati non è ricostruibile dal solo QGZ/GPKG e mostra evidenza di un pre-filtro attorno a 5.000 m². Questo impedisce il riuso diretto dell'universo candidato storico.

Nessuna decisione FROZEN è stata riaperta.

## 3. Regole di stato usate nell'inventario

| Stato | Significato |
|---|---|
| **AVAILABLE_LOCAL** | esiste una materializzazione locale/OneDrive verificata fisicamente |
| **SOURCE_VERIFIED** | ente/fonte primaria, URL o endpoint e identità della fonte sono stati verificati |
| **ENDPOINT_VERIFIED** | il servizio risponde ed espone il layer dichiarato; non implica validità metodologica |
| **METADATA_VERIFIED** | metadati ufficiali o RNDT letti e coerenti con l'identità del dataset |
| **DATA_VALIDATED** | contenuto, semantica, aggiornamento e qualità sono sufficientemente verificati per l'uso dichiarato |
| **TO_VALIDATE** | fonte plausibile o ufficiale ma validazione specialistica ancora necessaria |
| **HISTORICAL_ONLY** | utile come pista, benchmark o lineage storico; non utilizzabile automaticamente |
| **GAP** | dato necessario o potenzialmente necessario non ancora disponibile in forma adeguata |

Regola applicata in tutto il documento:

> **ENDPOINT_VERIFIED ≠ DATA_VALIDATED.**

Un servizio può essere vivo nel 2026 e contenere geometrie o contenuti derivati da fonti urbanistiche del 2018 o precedenti.

## 4. Evidenze tecniche prodotte dalla Chat 3.1

### 4.1 WFS Regione FVG

Endpoint testato:
`https://serviziogc.regione.fvg.it/geoserver/wfs`

`GetCapabilities` ha risposto HTTP 200 il 2026-09-18.

`GetFeature&resultType=hits` ha restituito:
- `CER:ZONE_INDUSTRIALI_ARTIG_D`: 4.155 feature;
- `CER:ZONE_COMMERCIALI_H`: 1.466 feature;
- `RETI_TRASP:GRAFO_STRADALE_FVG`: 75.546 feature;
- `CER:INTERPORTI_FVG`: 5 feature;
- `CER:AREECONVENZIONALI_CP`: 57 feature;
- `IRDAT:CATFRANE_PERICOLOSITA`: 830 feature;
- `SITI_PROT:SIC`: 66 feature;
- `SITI_PROT:ZPS`: 35 feature;
- `SITI_PROT:BIOTOPI`: 40 feature;
- `SITI_PROT:RISERVE_NATURALI_REG`: 13 feature;
- `SITI_PROT:PARCHI_COMUNALI_RAFVG`: 18 feature;
- `SITI_PROT:PRATISTABILI`: 10.486 feature;
- `CAR_GEO:V_AREA_INONDATA`: 1.050 feature.

Queste cardinalità sono evidenze di accessibilità del servizio, non certificazioni di aggiornamento o idoneità.

### 4.2 Struttura attributi P1

`DescribeFeatureType` dei layer produttivi/commerciali espone, fra gli altri:
- codici provincia/comune e nome comune;
- parametri urbanistici;
- `ZONA_OMOGE`, `ZONA_DESC`, `SOTTOZONA`, `DEST_PREV`;
- `ART_NTA`;
- `VARIANTE`;
- `DATA_VAL`;
- `SUPERFICIE`;
- identificativi `FID`, `GID`, `ID1`;
- geometria.

La presenza di questi campi è positiva per lineage e ricostruibilità, ma non dimostra che il layer rappresenti il PRGC oggi vigente.

La lettura degli attributi `DATA_VAL` sulle 4.155 feature industriali e sulle 1.466 commerciali mostra frequenze dominanti fra 2014 e 2018; esempi molto frequenti sono 2017-07-13, 2017-05-25, 2017-12-14, 2018-02-15 e 2018-04-12.

La documentazione regionale 2023 delle mappe CER identifica esplicitamente questi strati come estratti della **Mosaicatura PRG 2018**.

Conclusione tecnica: i layer sono una fonte ufficialmente pubblicata e molto utile per ricostruire geometrie e semantica storica, ma **non sono ancora DATA_VALIDATED come rappresentazione dell'urbanistica comunale vigente nel 2026**.

### 4.3 Grafo stradale FVG

Metadato RNDT: **Grafo stradale Regione FVG**.

Elementi verificati:
- proprietario: Regione Autonoma Friuli Venezia Giulia;
- finalità dichiarata: grafo della viabilità regionale per analisi CRMSS;
- modello dati dichiarato: Linear Reference System (LRS);
- creazione: 2014-07-03;
- revisione metadato/dataset riportata: 2024-01-16;
- WFS regionale attivo nel 2026.

`DescribeFeatureType` espone campi utili quali:
- direzione `DIR`;
- classe stradale `CLASSE`;
- ente gestore;
- allowance/uso;
- stato/tipo tratto;
- nome elemento;
- lane count;
- validità temporale;
- geometria.

Conclusione tecnica: è il candidato ufficiale prioritario per la rete regionale, ma **non è ancora validato come grafo routabile Light/Heavy**. Servono test di topologia, direzioni, connettività e restrizioni veicolari.

### 4.4 TEN-T / TENtec

Fonti primarie verificate:
- Regolamento (UE) 2024/1679;
- pagina TEN-T della Commissione europea;
- TENtec Information System;
- servizi ArcGIS REST pubblici TENtec.

Il Reg. (UE) 2024/1679 struttura la TEN-T in:
- core network;
- extended core network;
- comprehensive network.

Il servizio REST pubblico storico `tentec_public_services_ext`, interrogato il 2026-09-18, espone invece gruppi **Core Network** e **Comprehensive Network** con strati Roads, Railways, Urban Nodes, Ports e Rail-Road Terminals, ma non un gruppo Extended Core.

Questa discordanza conferma un gap già intravisto nella baseline storica: la materializzazione TEN-T a due livelli non può essere assunta come rappresentazione completa della classificazione vigente 2024/1679.

La geometria TEN-T 2026, la classificazione a tre livelli e l'identificazione delle uscite pertinenti devono quindi essere validate in una attività specialistica P2.

### 4.5 Provenienza dei layer storici QGIS/CER

La baseline QGIS Beltrame contiene 14 istanze WFS collegate al GeoServer regionale, tra cui:
- zone industriali/artigianali;
- zone commerciali;
- grafo stradale;
- interporti;
- aree convenzionali cabine primarie;
- frane;
- Natura 2000 / siti protetti;
- CORINE;
- confini amministrativi.

La documentazione regionale Protos Energy, revisione 31/08/2023, consente di ricostruire limiti importanti:
- zone industriali/commerciali: estratti da Mosaicatura PRG 2018;
- interporti: fonte istituzionale per l'elenco, ma posizionamento 2023 recuperato tramite Google Maps;
- aree convenzionali CP: fonti miste; per 51 aree e-distribuzione furono georeferenziate schermate e digitalizzati manualmente i confini, con buffer di incertezza indicativo ±200 m;
- linee elettriche storicamente ricognite da OpenInfraMap: espressamente considerate a scarsa affidabilità;
- ferrovie regionali: dataset DBPrior acquisito da EAGLE.

Questi elementi rendono la baseline utile per source discovery, non per validazione automatica.

## 5. INVENTARIO MASTER — P1 geometrie dei futuri candidati

| ID | Dataset / fonte | Dato disponibile | Fonte primaria/candidata | Verifica eseguita | Dato verificato per uso futuro? | Limite noto | Gap / azione |
|---|---|---|---|---|---|---|---|
| F3-P1-01 | Zone industriali e artigianali `CER:ZONE_INDUSTRIALI_ARTIG_D` | WFS live; storico nel QGIS | Regione FVG / IRDAT | endpoint, 4.155 feature, schema attributi, origine Mosaicatura PRG 2018 | **NO — TO_VALIDATE** | base urbanistica storica; vigenza 2026 non provata | ricostruire rapporto con PRGC vigenti e varianti |
| F3-P1-02 | Zone commerciali `CER:ZONE_COMMERCIALI_H` | WFS live; storico nel QGIS | Regione FVG / IRDAT | endpoint, 1.466 feature, schema, origine Mosaicatura PRG 2018 | **NO — TO_VALIDATE** | stesso limite di P1-01 | stessa attività specialistica |
| F3-P1-03 | PRGC comunali vigenti | disponibili in modo frammentato per Comune / sistemi regionali | Comuni FVG; Regione come infrastruttura di pubblicazione | esistenza istituzionale verificata, inventario regionale unico non verificato | **NO** | 215 contesti comunali; varianti e conformazioni PPR | trovare fonte/versione region-wide o procedura riproducibile |
| F3-P1-04 | Catasto cartografico | servizio WMS pubblico nazionale | Agenzia delle Entrate | servizio istituzionale individuato | **NO — supporto** | WMS di consultazione; non prova proprietà o disponibilità | definire se serve in F4/F12 e modalità di integrazione |
| F3-P1-05 | Proprietà/disponibilità aree pubbliche | nessun dataset region-wide validato | Regione, Comuni, consorzi/gestori | ricognizione storica 2023 mostra dati catastali puntuali non correnti | **NO — GAP** | disponibilità non deducibile dalla zonizzazione | fonte da richiedere/ricostruire separatamente |
| F3-P1-06 | Poligoni/planimetrie poli logistici-industriali | materiale locale `C:\Tesi\LOGISTICS_FVG_SOURCE` | Autorità portuale, Regione, gestori, Comuni, consorzi | 9 famiglie di fonti materializzate e registro locale letto | **PARZIALE** | eterogeneità; Vallenoncello parziale; alcune planimetrie non in scala | riconciliare con fonte primaria e versioni correnti |

**Valutazione P1:** la fonte regionale WFS è tecnicamente accessibile e ricca di lineage, ma la **vigenza urbanistica è il principale blocker di Fase 3 verso Fase 4**.

## 6. INVENTARIO MASTER — P2 rete stradale, accessi e TEN-T

| ID | Dataset / fonte | Dato disponibile | Fonte primaria/candidata | Verifica eseguita | Dato verificato per uso futuro? | Limite noto | Gap / azione |
|---|---|---|---|---|---|---|---|
| F3-P2-01 | `RETI_TRASP:GRAFO_STRADALE_FVG` | WFS live | Regione FVG / IRDAT / CRMSS | endpoint 75.546 feature; RNDT; revisione 2024-01-16; schema | **NO — TO_VALIDATE routing** | LRS non equivale automaticamente a network routabile | test topologia, direzioni, connettività, one-way e restrictions |
| F3-P2-02 | TEN-T roads | layer storico materializzato + servizi TENtec live | Commissione europea / DG MOVE / TENtec | regolamento e servizi verificati | **NO — TO_VALIDATE** | servizio REST storico espone 2 livelli, regolamento vigente ne ha 3 | ottenere geometria/classificazione coerente con 2024/1679 |
| F3-P2-03 | Urban nodes / ports / rail-road terminals TEN-T | layer storico + TENtec | Commissione europea / DG MOVE | categorie presenti nel servizio ufficiale | **NO — TO_VALIDATE** | perimetri/semantica dei nodi da verificare; non ridurre nodo a punto senza base | acquisire layer current e metadati |
| F3-P2-04 | Uscite TEN-T | storico: 23 uscite core nel GPKG | derivazione storica non ricostruita | presenza storica verificata | **NO — HISTORICAL_ONLY** | non esiste lineage sufficiente e può riflettere vecchia tassonomia | definire fonte/regola riproducibile per exit set |
| F3-P2-05 | Accessi dei candidati | non esiste ancora: correttamente deferred da F2 | da derivare da poligoni + rete + fonti locali | nessuna derivazione anticipata | **NO — GAP** | non basta nearest-road; servono access point, road anchor, connector | specifica e procedura dopo validazione P1/P2 |
| F3-P2-06 | Restrizioni Heavy | solo attributi parziali nel grafo | Regione/gestori stradali/ANAS/autostrade | non validato | **NO — GAP** | sagome, pesi, divieti, accessibilità reale non garantiti | inventario restrizioni e validazione campionaria Heavy |
| F3-P2-07 | Tratta ferroviaria DBPrior | fonte regionale individuata | Regione FVG / IRDAT | metadato RNDT: edizione 2006 | **NO — supporto storico** | dataset vecchio per una rete operativa | confrontare con fonte RFI/aggiornamenti solo se rilevante |
| F3-P2-08 | Porti/interporti/terminali logistici | documenti locali + 5 punti WFS interporti + TENtec nodes | enti gestori/Regione/Commissione | sorgenti istituzionali storiche identificate | **PARZIALE** | geometrie e precisione eterogenee | specialistica su footprint/accesso se usati territorialmente |

**Valutazione P2:** esiste una base ufficiale forte, ma non è ancora dimostrata la catena completa **accesso candidato → rete Light/Heavy → uscita TEN-T vigente** richiesta dalle baseline FROZEN.

## 7. INVENTARIO MASTER — P3 vincoli territoriali e fattibilità

| ID | Dataset / fonte | Dato disponibile | Fonte primaria/candidata | Verifica eseguita | Dato verificato per uso futuro? | Limite noto | Gap / azione |
|---|---|---|---|---|---|---|---|
| F3-P3-01 | PGRA — allagabilità/pericolosità/rischio | storico GPKG + portale SIGMA | Autorità di Bacino Distrettuale Alpi Orientali | fonte e adozione aggiornamento 2025/2026 verificate | **NO — CURRENT DATA TO ACQUIRE** | vecchio GPKG può essere superato | acquisire layer vettoriali corrispondenti alle mappe 2026 in salvaguardia |
| F3-P3-02 | Aree inondate geologiche `CAR_GEO:V_AREA_INONDATA` | WFS live, 1.050 feature | Regione FVG | endpoint verificato | **NO — complementare** | non sostituisce PGRA normativo | chiarire semantica e uso eventuale |
| F3-P3-03 | Frane / pericolosità `IRDAT:CATFRANE_PERICOLOSITA` | WFS live, 830 feature | Regione FVG | endpoint + pagina Catasto Frane verificati | **NO — TO_VALIDATE** | Catasto Frane complessivo dichiara ~6.500 fenomeni: layer hazard non coincide col catasto completo | mappare layer, classi, aggiornamento e rilevanza normativa |
| F3-P3-04 | Natura 2000 SIC/ZSC/ZPS | WFS live | Regione FVG / fonti Natura | endpoint SIC=66, ZPS=35 | **NO — TO_VALIDATE semantics** | nomenclatura SIC/ZSC e stato legale devono essere allineati al registro vigente | validare layer e date di designazione |
| F3-P3-05 | Parchi/riserve/biotopi/prati stabili | WFS live per più tematismi | Regione FVG | cardinalità endpoint parzialmente verificate | **NO — TO_VALIDATE** | non tutti i type name storici sono ancora validi | catalogare layer correnti e regime di tutela |
| F3-P3-06 | PPR e beni paesaggistici | WebGIS ufficiale | Regione FVG | PPR vigente + Variante 2 efficace 18/12/2025 verificati | **NO — TO_ACQUIRE** | IRDAT/Eagle può non essere allineato; Regione indica WebGIS PPR come riferimento ufficiale | definire estrazione/API riproducibile dal WebGIS vigente |
| F3-P3-07 | Aree convenzionali cabine primarie `CER:AREECONVENZIONALI_CP` | WFS live, 57 feature | Regione/DSO | endpoint e lineage 2023 verificati | **NO — solo screening territoriale** | per e-distribuzione, 51 aree storicamente digitalizzate da screenshot con ±200 m; non sono siti CP né capacità | reacquisire fonte corrente DSO/GSE e non usarla come capacità |
| F3-P3-08 | RTN e richieste connessione | portale TE.R.R.A. attivo | Terna | fonte ufficiale e funzioni report/mappa verificate | **NO — TO_VALIDATE ACCESS** | accesso/export GIS e granularità per FVG da verificare | specialistica energia |
| F3-P3-09 | Hosting capacity / capacità DSO | informazioni aggregate e piani investimenti | e-distribuzione e altri DSO | fonti pubbliche generali verificate | **NO — GAP CRITICO** | nessuna capacità disponibile puntuale per sito verificata | interlocuzione DSO / preventivi / dati ufficiali |
| F3-P3-10 | Linee elettriche AT/MT | storico OpenInfraMap non acquisito | Terna/DSO da preferire | storica bassa affidabilità documentata | **NO — GAP** | geometria ufficiale/aggiornata non ancora materializzata | recuperare fonte primaria o dichiarare indisponibilità |

**Valutazione P3:** ambiente e rischio hanno fonti istituzionali forti; l'energia resta il gap di fattibilità più rilevante.

## 8. INVENTARIO MASTER — dati di supporto e domanda

| ID | Dataset / fonte | Dato disponibile / fonte | Verifica 3.1 | Stato | Limite / prossimo passo |
|---|---|---|---|---|---|
| F3-SUP-01 | Confini amministrativi | ISTAT, confini al 01/01/2026 | fonte ufficiale verificata | SOURCE_VERIFIED | scala non certificabile uniformemente; usare fini coerenti |
| F3-SUP-02 | Popolazione residente | ISTAT DEMO/Censimento permanente | dati al 31/12/2024 e DEMO 01/01/2026 individuati | SOURCE_VERIFIED | fissare annualità solo quando serve al metodo |
| F3-SUP-03 | Popolazione griglia 1 km | ISTAT, Censimento 2021 | fonte ufficiale verificata | SOURCE_VERIFIED | anno 2021; uso eventuale da motivare |
| F3-SUP-04 | Pendolarismo lavoro | ISTAT matrice 2021, pubblicata 02/10/2025 | fonte e nota metodologica individuate | SOURCE_VERIFIED | è stima 2021; non equivale a conteggio traffico osservato |
| F3-SUP-05 | Matrici distanze/tempi comuni | ISTAT, geografia 2021 / grafo commerciale 2020 | fonte ufficiale individuata | SOURCE_VERIFIED | utile a controlli, non sostituisce rete candidato-accesso |
| F3-SUP-06 | Turismo | WebTur/Regione FVG + rilevazione ISTAT | report 2023/2024 e dati 2024/2025 individuati | TO_VALIDATE RAW DATA | serve estratto riproducibile alla granularità scelta |
| F3-SUP-07 | Aree interne | Presidenza Consiglio / Politiche di coesione, Mappa Aree Interne 2020 / ciclo 2021-2027 | fonte ufficiale e file elenco individuati | SOURCE_VERIFIED | distinguere classificazione comunale da aree-progetto SNAI |
| F3-SUP-08 | Uso del suolo CORINE | WFS regionale storico | fonte ufficiale di supporto | TO_VALIDATE | non sostituisce zonizzazione urbanistica vigente |

Questi dati non vengono trasformati in indicatori in Chat 3.1.

## 9. Gap analysis consolidata

| Gap ID | Priorità | Gap | Impatto | Stato / sblocco |
|---|---|---|---|---|
| GAP-3.1-01 | **BLOCKER P1** | manca una rappresentazione region-wide dimostrata come coerente con i PRGC vigenti 2026 | non si può generare un universo candidato difendibile | validazione urbanistica specialistica |
| GAP-3.1-02 | ALTO P1 | disponibilità/proprietà effettiva delle superfici non disponibile region-wide | fattibilità e verifiche puntuali | fonti patrimonio/consorzi/comuni; non dedurre dalla zonizzazione |
| GAP-3.1-03 | **BLOCKER P2** | grafo FVG non ancora validato per routing Light/Heavy | distanze AFIR/accesso non ricostruibili con sufficiente garanzia | test topologia/direzioni/restrizioni |
| GAP-3.1-04 | **BLOCKER P2** | geometria TEN-T vigente 2024/1679 e classificazione a tre livelli non materializzata/validata | rischio di usare tassonomia superata | TENtec current + allegati regolamento + verifica FVG |
| GAP-3.1-05 | ALTO P2 | dataset/procedura per uscite TEN-T e accessi candidati non definita | impedisce 10 km H2 / 3 km EV stradali | definire lineage di exit/access dopo P1/P2 |
| GAP-3.1-06 | ALTO P2 | restrizioni Heavy incomplete | possibile falsa accessibilità camion | fonti gestori + test campione |
| GAP-3.1-07 | **BLOCKER P3** | layer vettoriali PGRA 2026 in salvaguardia non ancora acquisiti | rischio idraulico non aggiornato | acquisizione da Autorità di Bacino/SIGMA |
| GAP-3.1-08 | ALTO P3 | estrazione riproducibile PPR vigente Variante 2/2025 non definita | vincoli paesaggistici incompleti | WebGIS PPR ufficiale / servizi sottostanti |
| GAP-3.1-09 | **CRITICO ENERGIA** | capacità reale di connessione elettrica per sito non pubblicamente verificata | fattibilità energetica non discriminabile | Terna/DSO; richieste ufficiali; dichiarare limite se non ottenibile |
| GAP-3.1-10 | ALTO ENERGIA | geometria ufficiale e livelli di tensione RTN/DSO non ancora materializzati | proxy di distanza debole | TE.R.R.A./gestori e metadati |
| GAP-3.1-11 | MEDIO | dataset turistico raw riproducibile da fissare | futura domanda turistica | acquisizione ufficiale con annualità/granularità documentata |
| GAP-3.1-12 | MEDIO | footprint precisi di poli logistici/industriali eterogenei | analisi nodi/logistica | riconciliare materiale locale con fonti primarie correnti |

## 10. Fonti primarie e URL di riferimento

### Regione FVG / IRDAT
- Catalogo IRDAT: https://irdat.regione.fvg.it/
- WFS: https://serviziogc.regione.fvg.it/geoserver/wfs
- regola generale licenza: IODL 2.0 salvo diversa indicazione nel metadato;
- metadato RNDT Grafo stradale Regione FVG: identificatore `r_friuve:m10400-cc-i9983`.
- documentazione 2023 dei layer CER: https://prod-energia.regione.fvg.it/export/sites/energia/documents/CER/LINEE-GUIDA-LAYER-MAPPATURA-FVG.PDF

### TEN-T
- TEN-T policy: https://transport.ec.europa.eu/transport-themes/infrastructure-and-investment/trans-european-transport-network-ten-t_en
- TENtec: https://transport.ec.europa.eu/transport-themes/infrastructure-and-investment/trans-european-transport-network-ten-t/tentec-information-system-and-ten-t-map-library_en
- REST storico interrogato: https://webgate.ec.europa.eu/getis/rest/services/TENTec/tentec_public_services_ext/MapServer
- atto vigente: Regolamento (UE) 2024/1679.

### Rischio / paesaggio
- PGRA/SIGMA: https://sigma.distrettoalpiorientali.it/portal/
- cartografie PGRA: https://sigma.distrettoalpiorientali.it/portal/index.php/direttiva-alluvioni/pgra-2021-2027/cartografie-pgra/
- PPR FVG: pagina istituzionale Regione e WebGIS PPR vigente.

### Energia
- Terna — Programmazione territoriale / TE.R.R.A.: https://www.terna.it/it/sistema-elettrico/programmazione-territoriale-efficiente
- MyTerna / report TE.R.R.A.: https://my.terna.it/
- e-distribuzione — aree convenzionali CER e piani smart grid: sito istituzionale e-distribuzione.

### Statistica / domanda
- ISTAT confini amministrativi: https://www.istat.it/notizia/confini-delle-unita-amministrative-a-fini-statistici-al-1-gennaio-2018-2/
- ISTAT pendolarismo 2021: https://www.istat.it/notizia/matrice-di-pendolarismo-per-lavoro/
- ISTAT popolazione: https://demo.istat.it/
- Aree interne/SNAI: https://politichecoesione.governo.it/it/politica-di-coesione/strategie-tematiche-e-territoriali/strategie-territoriali/strategia-nazionale-aree-interne-snai/le-aree-interne-2021-2027/
- turismo: Regione FVG / WebTur / rilevazione ISTAT Movimento dei clienti negli esercizi ricettivi.

Gli URL sono riferimenti di fonte; ogni futura acquisizione deve registrare URL effettivo, data di download, versione e hash quando materializzata.

## 11. Materiale storico disponibile e uso consentito

### 11.1 Baseline Claude
Package:
`5_HUB_FVG\00_baseline\21624001 FVG Energia Spa – Studio mobilità sostenibile.zip`

Contiene deliverable, relazioni, fogli di calcolo e tavole. È stato usato unicamente per:
- individuare fonti già percorse;
- ricostruire nomi di layer;
- identificare limiti già emersi;
- confrontare la copertura dell'inventario.

Non è fonte di verità per metodologia, candidati, soglie, indicatori o risultati.

### 11.2 QGIS Beltrame
Package:
`5_HUB_FVG\00_baseline\claude_qgis\QGZ_Beltrame_20260918\QGZ_Beltrame.zip`

È utile per ricostruire WFS/typeName e materializzazioni storiche. I 1.377 candidati e gli strati derivati restano HISTORICAL_ONLY.

### 11.3 LOGISTICS_FVG_SOURCE
Percorso read-only consultato:
`C:\Tesi\LOGISTICS_FVG_SOURCE`

Il registro locale censisce nove famiglie di fonti relative a porti, interporti/autoporti e zone industriali. Devono essere riconciliate con le fonti primarie correnti prima dell'uso ufficiale.

## 12. Proposta di suddivisione delle attività specialistiche successive

La seguente è una **PROPOSTA alla Chat Madre**, non una decisione approvata.

### Chat 3.2 — Urbanistica, poligoni sorgente e disponibilità
Mandato:
- risolvere GAP-3.1-01 e GAP-3.1-02;
- verificare PRGC vigenti, eventuale mosaicatura regionale corrente e semantica D/H;
- valutare identificativi, versioni, CRS, precisione, lineage e licenza;
- censire fonti di proprietà/disponibilità senza costruire `CANDIDATES_RAW`.

Quality gate: fonte/i P1 dichiarate utilizzabili oppure gap formalmente documentato con procedura sostitutiva approvabile.

### Chat 3.3 — Rete stradale, accessi e TEN-T
Mandato:
- validare `GRAFO_STRADALE_FVG` per routing;
- distinguere Light/Heavy;
- acquisire/validare TEN-T coerente con Reg. 2024/1679;
- definire fonte e lineage delle uscite TEN-T;
- definire requisiti dati per access point/road anchor/connector senza calcolare ancora candidati.

### Chat 3.4 — Vincoli idraulici, geologici, ambientali e paesaggistici
Mandato:
- acquisire PGRA 2026 vigente/in salvaguardia;
- validare frane, Natura 2000, aree protette e altri layer ostativi/rilevanti;
- acquisire il PPR vigente Variante 2/2025 dal riferimento ufficiale;
- classificare ciascun tematismo come requisito normativo, fonte informativa o semplice contesto, senza ancora fissare regole di esclusione non approvate.

### Chat 3.5 — Rete elettrica e fattibilità energetica
Mandato:
- distinguere RTN, DSO, cabine primarie, aree convenzionali e capacità disponibile;
- verificare TE.R.R.A. e fonti dei DSO;
- determinare quali dati geografici e di capacità siano realmente ottenibili;
- vietare l'uso delle aree convenzionali CP come proxy non dichiarato di capacità o posizione della cabina.

### Chat 3.6 — Domanda e dati territoriali di supporto
Mandato:
- materializzare/versionare ISTAT popolazione, pendolarismo 2021, SNAI e turismo;
- documentare geografie, annualità, granularità e join keys;
- nessun indicatore o peso in questa fase.

Ordine raccomandato per dipendenze tecniche: **3.2 e 3.3 prima; 3.4 e 3.5 in parallelo; 3.6 non bloccante per la generazione geometrica dei candidati.**

## 13. Questioni metodologiche da riportare alla Chat Madre

La Chat 3.1 non assume autonomamente le seguenti scelte.

### Q-METH-3.1-A — Fonte urbanistica ufficiale operativa
Va deciso, dopo la Chat 3.2, se:
- utilizzare una eventuale base regionale aggiornata;
- ricostruire una mosaicatura dai PRGC comunali vigenti;
- adottare una strategia ibrida con controllo comunale puntuale.

Il layer 2018 non viene implicitamente accettato.

### Q-METH-3.1-B — Tassonomia TEN-T operativa
Va definito come rappresentare core / extended core / comprehensive nel modello e quale versione cartografica diventa baseline.

Il servizio pubblico storico a due livelli non viene implicitamente accettato.

### Q-METH-3.1-C — Trattamento della disponibilità fondiaria
Va deciso in quale fase la disponibilità/proprietà diventa:
- requisito di generazione;
- criterio di ammissibilità;
- verifica puntuale di Fase 12.

La Chat 3.1 registra il gap ma non sceglie.

### Q-METH-3.1-D — Dato energetico minimo accettabile
Se capacità reale di connessione non sarà accessibile, la Chat Madre dovrà decidere quali proxy siano ammissibili, come dichiararli e se siano sufficienti a superare la Fase 7. La Chat 3.1 non sostituisce capacità reale con distanza o area convenzionale.

## 14. Aggiornamenti eseguiti nel PROJECT_CONTROL_REGISTER

Gli aggiornamenti seguenti sono stati scritti e riletti nel registro vivo Google Sheets il 2026-09-18. La registrazione documenta fonti e gap; non equivale ad accettazione metodologica né a validazione dei dataset.

### DATA_REGISTRY — fonti registrate
- `F3_SRC_FVG_ZONING_IND_001` — `CER:ZONE_INDUSTRIALI_ARTIG_D` — ENDPOINT_VERIFIED / DATA_TO_VALIDATE.
- `F3_SRC_FVG_ZONING_COM_001` — `CER:ZONE_COMMERCIALI_H` — ENDPOINT_VERIFIED / DATA_TO_VALIDATE.
- `F3_SRC_FVG_ROADGRAPH_001` — Grafo stradale FVG — SOURCE+METADATA+ENDPOINT_VERIFIED / ROUTING_TO_VALIDATE.
- `F3_SRC_TENTEC_001` — TENtec / Reg. 2024/1679 — SOURCE_VERIFIED / CURRENT_GEOMETRY_TO_VALIDATE.
- `F3_SRC_PGRA_001` — PGRA aggiornamento 2026 — SOURCE_VERIFIED / CURRENT_VECTOR_TO_ACQUIRE.
- `F3_SRC_PPR_001` — PPR FVG vigente Variante 2/2025 — SOURCE_VERIFIED / EXTRACTION_TO_VALIDATE.
- `F3_SRC_FVG_LANDSLIDE_001` — Catasto/pericolosità frane — ENDPOINT_VERIFIED / SEMANTICS_TO_VALIDATE.
- `F3_SRC_FVG_NATURA_001` — Natura 2000 e aree protette — ENDPOINT_VERIFIED / SEMANTICS_TO_VALIDATE.
- `F3_SRC_FVG_CP_001` — aree convenzionali cabine primarie — ENDPOINT_VERIFIED / SCREENING_ONLY.
- `F3_SRC_TERNA_TERRA_001` — TE.R.R.A. — SOURCE_VERIFIED / DATA_ACCESS_TO_VALIDATE.
- `F3_SRC_ISTAT_COMMUTE_001` — Pendolarismo lavoro 2021 — SOURCE_VERIFIED.
- `F3_SRC_ISTAT_POP_001` — Popolazione — SOURCE_VERIFIED.
- `F3_SRC_SNAI_001` — Aree interne 2021-2027 / Mappa 2020 — SOURCE_VERIFIED.
- `F3_SRC_FVG_TOURISM_001` — WebTur/ISTAT turismo — SOURCE_VERIFIED / RAW_EXTRACT_TO_VALIDATE.

### ISSUES — nuove issue dati registrate OPEN
- `ISS-0003`: vigenza 2026 della Mosaicatura PRG 2018 non dimostrata; priorità P1.
- `ISS-0004`: routing Light/Heavy del grafo FVG non validato; priorità P2.
- `ISS-0005`: TEN-T current a tre livelli non materializzata/validata; priorità P2.
- `ISS-0006`: layer vettoriali PGRA aggiornati 2026 non ancora acquisiti; priorità P3.
- `ISS-0007`: capacità elettrica puntuale e connessione DSO/RTN non disponibile in dataset validato; gap critico.
- `ISS-0008`: PPR vigente 2025 richiede procedura di estrazione riproducibile dal riferimento ufficiale.
- `ISS-0009`: proprietà/disponibilità aree non coperta da dataset region-wide validato.

## 15. Quality gate della Chat 3.1

| Controllo | Esito | Evidenza |
|---|---|---|
| categorie minime Fase 3 censite o marcate GAP | **PASS** | sezioni 5–8 |
| ogni dataset ha fonte identificata oppure stato non verificato esplicito | **PASS** | inventario master |
| P1 e P2 hanno fonti prioritarie identificate e limiti espliciti | **PASS** | P1: WFS/PRGC; P2: grafo FVG/TENtec |
| Claude/QGIS separati dalle fonti autorevoli | **PASS** | sezione 11 |
| nessuna assunzione trasformata in dato validato | **PASS** | regola ENDPOINT ≠ DATA_VALIDATED |
| nessuna scelta metodologica sostanziale approvata implicitamente | **PASS** | sezione 13 |
| FROZEN F1/F2 non modificati | **PASS** | nessun file F1/F2 alterato |
| gap P1/P2/P3 esplicitati e assegnabili | **PASS** | sezioni 9 e 12 |

### 15.1 Esito operativo

**CHAT 3.1 = PASS TECNICO-OPERATIVO / REVIEW PER CHAT MADRE.**

Significato:
- l'inventario master v01 è stato costruito;
- i principali gap sono identificati e tracciabili;
- è disponibile una proposta concreta di decomposizione della Fase 3;
- **la FASE 3 complessiva resta IN CORSO**;
- non viene autorizzata la costruzione di `CANDIDATES_RAW`;
- nessun dataset marcato TO_VALIDATE viene promosso a baseline ufficiale con questo documento.

## 16. Prossimo passo raccomandato alla Chat Madre

1. ricevere e verificare questo handoff;
2. registrare/accettare gli aggiornamenti DATA_REGISTRY e ISSUES appropriati;
3. aprire prioritariamente Chat 3.2 e Chat 3.3;
4. aprire in parallelo Chat 3.4 e Chat 3.5;
5. mantenere Fase 4 bloccata finché i gap P1/P2 necessari alla costruzione e all'accessibilità dei candidati non sono risolti o formalmente accettati come limite.

Il passaggio dalla fonte candidata al dato ufficiale del modello deve avvenire solo dopo la validazione specialistica e l'eventuale approvazione metodologica richiesta.

## 17. Handoff alla Chat Madre

**Chat:** 3.1 — Inventario master e gap analysis dei dati  
**Obiettivo:** costruire inventario verificabile, identificare fonti primarie/limiti/gap e proporre specializzazione Fase 3.  
**Lavoro svolto:** letti dispatch e baseline FROZEN; verificata governance live; ispezionati baseline QGIS/Claude e `LOGISTICS_FVG_SOURCE`; verificati WFS regionali, metadati stradali, TENtec, PGRA/PPR, principali fonti energia e statistiche; costruita gap analysis.  
**Decisioni approvate:** nessuna nuova decisione metodologica.  
**Proposte:** Q-METH-3.1-A/B/C/D e suddivisione Chat 3.2–3.6.  
**Artifact creato:** `C:\dev\5-hub\docs\FASE_3_DATA_INVENTORY_REVIEW_v01.md`.  
**Artifact FROZEN modificati:** nessuno.  
**Controlli:** quality gate sezione 15 = PASS tecnico-operativo.  
**Problemi aperti principali:** urbanistica vigente; routing Light/Heavy; TEN-T 2024/1679; PGRA 2026 vettoriale; PPR extraction; disponibilità fondiaria; capacità rete elettrica.  
**Stato finale:** Chat 3.1 pronta per REVIEW; Fase 3 ancora IN CORSO.  
**Prossimo passo:** dispatch specialistici 3.2–3.6 secondo priorità/dipendenze sopra riportate.

### SESSION CLOSE
- `NOTEBOOK_CHANGE = NO` — il progetto 5 HUB non usa il notebook storico come Source of Truth; nessuna memoria scientifica FROZEN è stata modificata.
- `REGISTER_CHANGE = YES` — eseguito: DATA_REGISTRY aggiornato con 14 fonti Fase 3 e ISSUES aggiornato con `ISS-0003`…`ISS-0009`; rilettura post-write PASS.
- `GIT_COMMIT_REQUIRED = YES` — il nuovo artifact di review è versionabile.
- build notebook: N/A.
- preservation FROZEN: N/A; nessun artifact FROZEN creato o modificato.
