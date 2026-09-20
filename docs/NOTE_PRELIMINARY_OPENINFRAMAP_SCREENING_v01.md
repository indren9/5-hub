# NOTE — Screening preliminare OpenInfraMap / proxy rete elettrica

**Chat:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-20
**Stato:** PROPOSED / PRELIMINARY SCREENING
**Riferimenti:** DEC-0050; `docs/DISPATCH_CHAT_3.5_ELECTRIC_GRID_ENERGY_FEASIBILITY_v02.md`

## 1. Scopo

Verificare in modo limitato e proporzionato se OpenInfraMap / OpenStreetMap possa essere una fonte operativa utile per rappresentare la prossimità all'infrastruttura elettrica nel modello 5 HUB, senza trasformare il lavoro in uno studio elettrico di dettaglio.

La decisione approvata DEC-0050 resta vincolante:
- prossimità all'infrastruttura = proxy territoriale;
- prossimità non equivale a capacità disponibile;
- capacità, punto di connessione, costo e fattibilità tecnica reale sono verifiche sui finalisti.

## 2. OpenInfraMap: che cosa è

OpenInfraMap non mantiene un proprio database elettrico: visualizza dati presenti in OpenStreetMap.

Fonte:
https://openinframap.org/about

La pagina About dichiara che tutti i dati mostrati derivano direttamente da OpenStreetMap e indica Overpass Turbo / dati OSM come modalità di accesso.

La pagina Stats avverte esplicitamente che in molti Paesi la rappresentazione della rete non è completa e va usata con cautela.

Fonte:
https://openinframap.org/stats
Conclusione:
- OpenInfraMap è utile come visualizzatore;
- la vera fonte dati sarebbe OpenStreetMap;
- per una pipeline riproducibile non va "scrapata" la mappa: vanno estratti direttamente gli oggetti OSM.

## 3. Semantica OSM rilevante

OpenStreetMap usa principalmente:
- `power=substation`;
- `substation=transmission` / `distribution` / altri tipi;
- `voltage=*`;
- `operator=*`;
- `name=*`;
- `ref=*`.

Fonte:
https://wiki.openstreetmap.org/wiki/Substation

La documentazione OSM specifica che `power=substation` rappresenta una sottostazione e non un singolo trasformatore.

La documentazione FVG di OpenStreetMap segnala che:
- le principali stazioni elettriche ad alta tensione sono state mappate;
- linee elettriche FVG sono state anche importate storicamente dalla CTRN;
- sono necessari controlli perché alcune informazioni storiche possono essere superate o incomplete.

Fonte:
https://wiki.openstreetmap.org/wiki/Friuli-Venezia_Giulia/Linee_elettriche
Questo rende OSM plausibile come geometria fisica di screening, ma non prova completezza/currentness region-wide.

## 4. Fonte ufficiale FVG già disponibile

Il GeoServer ufficiale della Regione FVG espone il layer:

`CER:AREECONVENZIONALI_CP`

Descrizione:
"Aree di influenza delle cabine primarie di distribuzione elettrica".

Endpoint:
https://serviziogc.regione.fvg.it/geoserver/ows

Schema verificato il 2026-09-20:
- `AC_CODICE`;
- `GESTORE`;
- `EXTRAFVG`;
- `GEOMETRY`;
- `ID1`.

Query WFS verificata il 2026-09-20:
- 57 feature totali;
- 51 e-distribuzione;
- 5 AcegasApsAmga;
- 1 SECAB;
- 44 con `EXTRAFVG=0`;
- 13 con `EXTRAFVG=1`.

Interpretazione:
questo layer è ufficiale e utile per area convenzionale, codice e gestore, ma NON rappresenta automaticamente la posizione fisica della cabina primaria.
## 5. Fonte GSE

Il GSE pubblica la mappa interattiva delle cabine primarie per l'autoconsumo diffuso.

Fonti:
https://www.gse.it/servizi-per-te/autoconsumo/mappa-interattiva-delle-cabine-primarie
https://www.gse.it/documenti_site/Documenti%20GSE/Servizi%20per%20te/AUTOCONSUMO/Mappa%20interattiva/Manuale%20d%20uso%20della%20mappa%20interattiva%20delle%20cabine%20primarie.pdf

Il manuale GSE dichiara che:
- la mappa geolocalizza le Aree convenzionali;
- i dati cartografici sono forniti dalle imprese distributrici;
- l'aggiornamento è biennale.

Ruolo:
fonte ufficiale per la corrispondenza territoriale delle aree convenzionali, non fonte diretta della posizione fisica della cabina.

## 6. Fonti DSO correnti

### e-distribuzione

La pagina "Aree critiche" pubblica informazioni aggiornate sulla rete e sulle sezioni AT/MT delle cabine primarie.

Fonte:
https://www.e-distribuzione.it/a-chi-ci-rivolgiamo/produttori/aree-critiche.html

Il PDF 2025 include numerose cabine primarie FVG per nome/provincia e costituisce un utile cross-check corrente dell'esistenza/denominazione delle cabine.
### AcegasApsAmga

AcegasApsAmga dichiara la propria distribuzione elettrica nei Comuni di Trieste e Gorizia e pubblica informazioni su aree critiche e piani di sviluppo.

Fonte:
https://www.acegasapsamga.it/azienda/trasparenza/comunicazioni-ai-sensi-delle-delibere-arera-energia-elettrica

La pagina indica che le informazioni sulle aree critiche vengono aggiornate periodicamente.

Ruolo:
cross-check ufficiale DSO per currentness e denominazioni, non singola geometria GIS region-wide.

### SECAB

Il layer FVG identifica almeno una area convenzionale gestita da SECAB. La relativa geometria/posizione fisica della cabina dovrà essere verificata nel controllo di copertura se OSM viene scelto come fonte operativa.

## 7. Terna / TE.R.R.A.

Terna descrive TE.R.R.A. come piattaforma integrata con dati su infrastrutture esistenti/future e richieste di connessione.

Fonte:
https://www.terna.it/it/sistema-elettrico/programmazione-territoriale-efficiente

Per DEC-0050 non è necessario usarla come fonte principale del proxy se una geometria fisica più semplice e riproducibile risulta sufficiente.

Ruolo proposto:
cross-check/supporto, non audit completo della capacità.
## 8. Test tecnici eseguiti

### WFS FVG

PASS:
- endpoint interrogabile;
- schema verificato;
- conteggio e gestori ottenuti senza elaborare geometrie pesanti.

### OpenStreetMap / Overpass

Il tentativo di interrogazione di server pubblici Overpass nella sessione ha incontrato:
- HTTP 406 sul server principale;
- timeout su un mirror.

Questo è un problema di accesso al servizio pubblico nel test, non evidenza di assenza dei dati.

### Ricerca nominale OSM

Un test tramite Nominatim su alcuni nomi di cabine e località FVG non ha restituito risultati affidabili come `substation`.

Conclusione:
la ricerca testuale nominale NON è un QA adeguato. Il controllo corretto deve essere spaziale e basato sull'estrazione diretta degli oggetti OSM `power=substation`.

## 9. Proposta tecnica — NON ANCORA ACCEPTED

### Baseline operativa proposta

**Geometria fisica per il proxy:**
OpenStreetMap, visualizzabile con OpenInfraMap, estraendo direttamente gli oggetti `power=substation`.
**Validazione/cross-check ufficiale:**
1. `CER:AREECONVENZIONALI_CP` Regione FVG / GSE;
2. elenchi e informazioni DSO correnti (e-distribuzione, AcegasApsAmga, SECAB quando reperibile);
3. Terna/TE.R.R.A. solo quando utile a risolvere casi dubbi o infrastrutture RTN.

### Perché questa combinazione

- OSM può fornire una geometria fisica semplice e uniforme;
- il layer FVG/GSE fornisce copertura territoriale ufficiale e gestore;
- i DSO danno un controllo di currentness/denominazione;
- nessuna delle fonti viene usata per dedurre MW disponibili.

## 10. Quality gate prima dell'adozione

Prima di promuovere OSM/OpenInfraMap a baseline operativa serve ancora un test leggero ma riproducibile:

1. estrarre tutte le `power=substation` FVG;
2. classificare per `voltage`, `substation`, `operator`;
3. isolare le infrastrutture plausibilmente primarie/AT;
4. confrontare la copertura spaziale con le 57 aree convenzionali ufficiali;
5. verificare un campione di cabine nominate dai DSO;
6. identificare eventuali aree/gestori senza una geometria OSM plausibile.

Non è richiesta una verifica perfetta cabina-per-cabina se il campione e la copertura mostrano che il proxy è adeguato alla pianificazione di massima.

## 11. Stato

**OpenInfraMap/OSM:** PROMISING / PROPOSED, non ancora ACCEPTED come baseline.

**Layer FVG aree convenzionali:** fonte ufficiale valida per area/gestore/codice, non per posizione fisica della cabina.

**Prossimo passo consigliato:** eseguire il solo quality gate di copertura OSM sopra descritto. Se PASS, sottoporre all'utente l'adozione formale della combinazione OSM + layer ufficiale FVG/GSE + cross-check DSO.
