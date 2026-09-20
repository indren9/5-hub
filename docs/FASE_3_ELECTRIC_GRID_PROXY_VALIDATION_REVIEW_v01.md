# FASE 3 — Electric grid proxy validation review v01

**Chat:** Chat 3.5 — Proxy territoriale di prossimità alla rete elettrica
**Data gate:** 2026-09-20
**Stato documento:** REVIEW
**Giudizio tecnico della Chat 3.5:** **READY_WITH_LIMITATIONS**
**Autorità metodologica:** Chat 0.2 / utente. Questo documento non approva OSM/OpenInfraMap come baseline definitiva.

## 1. Mandato e perimetro

Il gate verifica esclusivamente se OpenStreetMap, visualizzato anche tramite OpenInfraMap, è sufficientemente tracciabile e territorialmente coerente da poter essere proposto come sorgente fisica per un futuro **proxy di prossimità alla rete elettrica** conforme a DEC-0050.

Non vengono stimati MW disponibili, hosting capacity, costi di connessione, fattibilità tecnica reale o punti di connessione garantiti. Le 57 aree `CER:AREECONVENZIONALI_CP` sono usate come **SERVICE_AREA** e non come geometria fisica della cabina primaria.

Baseline rispettate:
- FASE 1 PASS / CLOSED / FROZEN;
- FASE 2 PASS / CLOSED / FROZEN;
- DEC-0050 ACCEPTED;
- ISS-0007 resta OPEN;
- FASE 4 non viene aperta.

## 2. Fonti e classificazione

La matrice completa è in `docs/FASE_3_ELECTRIC_GRID_PROXY_SOURCE_MATRIX_v01.csv`.

Classificazione operativa:
- **OSM via Overpass:** `PHYSICAL_INFRASTRUCTURE_GEOMETRY`, utilizzabile solo come proxy fisico e con limiti;
- **OpenInfraMap:** `NOT_SUITABLE` come fonte autonoma; è un visualizzatore dei dati OSM;
- **FVG CER:AREECONVENZIONALI_CP:** `SERVICE_AREA`, screening territoriale;
- **documenti DSO e-distribuzione / AcegasApsAmga / SECAB:** `PROXY_ONLY` per cross-check ufficiale di nomi, ruolo e tensione;
- **Terna / TE.R.R.A.:** riferimento trasmissione disponibile, non usato come baseline CP nel gate minimo.

## 3. Estrazione OSM riproducibile

Script:
`scripts/acquire_validate_electric_grid_proxy_chat3_5_v01.py`

Ambiente usato:
- Python 3.13.15;
- shapely 2.1.2;
- pyproj 3.8.0;
- certifi 2026.07.22.

Query elementare per ciascuna tile:
```overpass
[out:json][timeout:120];
nwr["power"="substation"](S,W,N,E);
out center tags qt;
```

Envelope di estrazione: lat 45.55–46.75, lon 12.15–14.05. È volutamente più ampio del solo FVG per intercettare anche infrastrutture prossime alle 13 aree ufficiali marcate `EXTRAFVG=1`.

La griglia è 3 x 3 = 9 tile. Le risposte raw conservano query, endpoint e timestamp OSM. Timestamp OSM delle 9 tile: 2026-09-20 tra 08:53:34Z e 08:59:35Z.

Risultato deduplicato: **8.206** elementi `power=substation`.

Attributi conservati almeno:
`osm_type`, `osm_id`, coordinate, `name`, `ref`, `voltage`, `max_voltage_v`, `substation`, `operator`, `operator_norm`, `location`, `frequency`, classi QA e `tags_json` completo.

## 4. Regola QA per isolare infrastrutture plausibili AT/MT

La regola è esclusivamente di **quality assurance**, non una soglia di modello né una regola di connessione.

Classe A — `A_DSO_HV_PLAUSIBLE`:
- operatore normalizzato in {e-distribuzione, AcegasApsAmga, SECAB};
- tensione massima OSM >= 60 kV;
- esclusione esplicita dei ruoli `traction` e `generation`.

Classe B — `B_DISTRIBUTION_HV_OPERATOR_MISSING`:
- `substation=distribution`;
- tensione massima OSM >= 60 kV;
- operatore mancante.

Il limite inferiore a 60 kV è una regola di screening scelta per non perdere la CP di Barcis, presente nel riferimento ufficiale e-distribuzione e mappata in OSM a 60 kV. Non è un confine normativo e non deve essere riutilizzato automaticamente nel modello.

Esito:
- **92** posizioni rappresentative OSM plausibili per il proxy CP/AT-MT;
- 89 classe A;
- 3 classe B;
- operatori: 81 e-distribuzione, 7 AcegasApsAmga, 1 SECAB, 3 mancanti.

Queste 92 posizioni rappresentative non equivalgono a 92 cabine primarie certe. Esempio importante: il Piano AcegasApsAmga identifica 5 CP AT/MT nei territori di Trieste e Gorizia, mentre il filtro OSM restituisce 7 geometrie Acegas a 132 kV. Il filtro va quindi interpretato come insieme **plausibile**, non come inventario ufficiale di CP.

## 5. Confronto con le 57 aree convenzionali ufficiali

Dataset ufficiale:
`CER:AREECONVENZIONALI_CP` via WFS Regione FVG.

Consistenza verificata:
- 57 aree totali;
- 51 e-distribuzione;
- 5 AcegasApsAmga;
- 1 SECAB;
- 44 aree `EXTRAFVG=0`;
- 13 aree `EXTRAFVG=1`.

Analisi spaziale:
- CRS sorgenti: EPSG:4326;
- CRS metrico QA: EPSG:32633;
- test principale: presenza della posizione rappresentativa CP-proxy **dentro** il poligono convenzionale;
- per way/relation la posizione usata dal gate è il `center` restituito da Overpass (`out center`), cioè il centro del bounding box dell'oggetto OSM; non è la geometria completa della sottostazione e non è garantito che cada dentro il relativo poligono OSM;
- questa semplificazione è accettabile esclusivamente per il presente quality gate di copertura territoriale e non definisce ancora la geometria target della futura metrica di prossimità;
- nessuna tolleranza metrica è stata introdotta per trasformare un punto esterno in “coperto”;
- viene riportata separatamente la distanza dalla più vicina geometria CP-proxy.

Risultato complessivo:
- 48/57 aree con almeno una geometria CP-proxy all'interno;
- 9/57 senza geometria CP-proxy all'interno.

Risultato per le 44 aree interne FVG:
- **42/44 (95,5%)** con geometria plausibile all'interno;
- **42/44 (95,5%)** anche con operatore OSM coerente col gestore dell'area;
- **2/44 (4,5%)** senza geometria CP-proxy all'interno.

Le 13 aree `EXTRAFVG=1` hanno 6 casi coperti e 7 senza geometria plausibile interna. Questi 7 casi non sono considerati un blocco del proxy FVG perché la marcatura ufficiale segnala già una relazione extraregionale e la CP fisica può trovarsi fuori dal territorio regionale o fuori dall'envelope utile.

### 5.1 Gap interni da mantenere espliciti

| area ufficiale | gestore | evidenza QA | interpretazione |
|---|---|---|---|
| `AC001E00999` | e-distribuzione | 0 CP-proxy dentro il poligono; nelle vicinanze OSM contiene infrastrutture HV, inclusa la stazione Terna “Redipuglia” 380 kV | **gap OSM di geometria/semantica DSO**: il riferimento ufficiale e-distribuzione conferma una CP “REDIPUGLIA”, ma non è stata isolata una geometria OSM distinta come CP e-distribuzione |
| `AC001E00994` | e-distribuzione | 0 CP-proxy dentro il poligono; CP-proxy OSM “Opicina”, e-distribuzione, 132 kV, a circa 1,80 km dal poligono | **gap di copertura/posizionamento**: non si introduce una tolleranza ad hoc; il caso resta da trattare come missing nel proxy finché non viene definita una regola metodologica |

### 5.2 Gap extraregionali

Aree `EXTRAFVG=1` senza CP-proxy interno:
`AC001E01603`, `AC001E01601`, `AC001E01602`, `AC001E01597`, `AC001E01596`, `AC001E00874`, `AC001E00853`.

Le distanze alla geometria CP-proxy più vicina sono rispettivamente circa 4,10 km; 9,48 km; 8,92 km; 3,51 km; 8,31 km; 4,94 km; 7,65 km. Non vengono interpretate come soglie di accettazione.

## 6. Cross-check mirato con DSO ufficiali

Artifact:
`derived_qa/dso_official_crosscheck_v01.csv`.

### e-distribuzione

Il documento ufficiale “Inversioni di flusso 2025”, datato 28 febbraio 2026, elenca per il Friuli Venezia Giulia numerose cabine primarie/sezioni AT-MT. Il campione verificato include Cormons, Barcis, Giais, Pordenone, Prata, Ampezzo, Cividale, Ovaro, Reana, Udine Nord Est e Redipuglia.

Esito campione:
- 10 nomi su 11 hanno una geometria OSM coerente per nome/ruolo DSO;
- “REDIPUGLIA” è confermata dalla fonte ufficiale ma OSM mostra nel sito una stazione Terna 380 kV senza una geometria separata isolata come CP e-distribuzione;
- Barcis dimostra che una CP ufficialmente rilevante può comparire in OSM con high-side a 60 kV, motivando il mantenimento della regola QA >=60 kV.

Il documento e-distribuzione non è un inventario esaustivo di tutte le CP: elenca le sezioni che soddisfano i criteri di inversione del flusso del documento. È quindi usato solo come campione ufficiale.

### AcegasApsAmga

Il Piano di Sviluppo 2025-2029 Rev.1 identifica:
- Trieste: Broletto, Altipiano, Rozzol, Valmartinaga, tutte a 132 kV lato AT;
- Gorizia: Sant'Andrea, 132 kV lato AT.

Tutte e 5 sono state ritrovate in OSM con operatore Acegas e tensione 132 kV. Il caso è un controllo forte della corrispondenza fisica OSM nel territorio Acegas.

Il filtro OSM produce però 7 geometrie Acegas plausibili complessive: questo conferma che “DSO + tensione alta + distribution” non deve essere equiparato automaticamente a “cabina primaria ufficiale”.

### SECAB

SECAB conferma sul proprio sito la **cabina primaria di Paluzza 132/20 kV** collegata alla RTN Terna.

In OSM è presente una geometria a 132 kV con operatore SECAB, ma:
- nome: “Secab”;
- `substation=industrial`.

Il riscontro fisico/operatore/tensione è plausibile, ma la semantica OSM è incoerente con la classificazione ufficiale di cabina primaria. Il caso resta marcato `PARTIAL_OPERATOR_VOLTAGE_SEMANTIC_CONFLICT`.

## 7. OpenInfraMap e OSM

OpenInfraMap è trattata correttamente come **viewer**, non come fonte dati autonoma. La documentazione di OpenInfraMap dichiara che i dati mostrati provengono direttamente da OpenStreetMap; le sue statistiche avvertono inoltre che in molti Paesi la rete rappresentata può essere incompleta.

Per il gate:
- sorgente dati = OpenStreetMap;
- canale di estrazione = Overpass API;
- OpenInfraMap = supporto visuale;
- nessuna informazione vista su OpenInfraMap viene considerata indipendente da OSM.

## 8. Reproducibilità e artifact pesanti

Storage tecnico:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_5\`

Artifact principali:
- `fvg_wfs/CER_AREECONVENZIONALI_CP_20260920.geojson`;
- `osm_overpass/osm_power_substation_tile_01_v01.json` … `tile_09_v01.json`;
- `derived_qa/osm_substations_all_v01.csv`;
- `derived_qa/osm_substations_relevant_qc_v01.csv`;
- `derived_qa/osm_substations_cp_proxy_qc_v01.csv`;
- `derived_qa/osm_substations_cp_proxy_qc_v01.geojson`;
- `derived_qa/cer_cp_osm_coverage_v01.csv`;
- `derived_qa/coverage_summary_v01.json`;
- `derived_qa/dso_official_crosscheck_v01.csv`;
- `dso_official/e_distribuzione_inversioni_flusso_2025.pdf`;
- `dso_official/acegas_piano_sviluppo_2025_2029_rev1.pdf`;
- `dso_official/secab_distribuzione_20260920.html`;
- `source_manifest_v01.json`.

Hash principali:
- FVG WFS GeoJSON: `dea1b982b2f7c5a2029e4e901df797e9f4302a3d0d0756292c13d1cfd2a1a822`;
- OSM CP-proxy CSV: `23ffb98b8716c5423ff58882c0625076308ec908b53b184f46c68d7bb43d1351`;
- OSM CP-proxy GeoJSON: `9360ecc0675814b8a3d58b59690c5153862405206a99ebba1f909b8b7e42c967`;
- coverage CSV: `fb22971c80d0c5b15e0d2483d165691faac20e6aea394b3ec41eba6c0dc97a2f`;
- coverage summary JSON: `0fda21b5af140a0f1513f4f2fa906b83e599c862efb2ee185805e2e3ba049992`;
- cross-check DSO CSV: `6049f5ccfd8a944e94ae56c35e658ad85a23737df0a4626431f76e559cbafe50`.

Il manifest conserva bytes e SHA-256 anche per le 9 risposte raw Overpass e per i tre riferimenti DSO materializzati.

## 9. Implementabilità del futuro proxy

Il gate dimostra che una misura futura di prossimità è tecnicamente implementabile senza assumere capacità elettrica.

Una formulazione coerente con la FASE 2 potrebbe essere, **solo come proposta da sottoporre alla Chat 0.2/utente**:
- origine: geometria del poligono candidato;
- target: insieme di geometrie OSM CP-proxy validate;
- metrica: minima distanza planare in CRS metrico coerente;
- valori mancanti/gap: espliciti, senza sostituzione automatica con la distanza a una stazione Terna o a una cabina secondaria;
- nessun passaggio da distanza a MW, hosting capacity, costo o fattibilità reale.

Questa formulazione **non è implementata né approvata** in questa chat perché l'universo dei candidati appartiene alle fasi successive e la scelta della metrica finale è metodologica.

## 10. Quality gate minimo

| controllo | esito |
|---|---|
| estrazione OSM riproducibile e raw conservati | PASS |
| attributi `voltage`, `substation`, `operator` e tag completi | PASS |
| isolamento infrastrutture plausibili CP / AT-MT | PASS_WITH_LIMITATIONS |
| confronto spaziale con 57 aree ufficiali | PASS |
| controllo mirato su e-distribuzione, AcegasApsAmga, SECAB | PASS_WITH_LIMITATIONS |
| identificazione gap territoriali/semantici | PASS |
| separazione physical geometry / service area / capacity | PASS |
| nessuna stima di MW/hosting capacity/costi | PASS |
| tracciabilità, hash e riproducibilità | PASS |
| approvazione OSM come baseline definitiva | NON ESEGUITA — fuori mandato |
| chiusura ISS-0007 | NON ESEGUITA — resta OPEN |
| apertura FASE 4 | NON ESEGUITA |

## 11. Giudizio tecnico

# READY_WITH_LIMITATIONS

Motivazione:

1. OSM fornisce una base fisica sufficientemente ricca e riproducibile per **proporre** un proxy territoriale di prossimità: 42/44 aree interne FVG hanno una geometria plausibile con gestore coerente all'interno.
2. I controlli ufficiali sui tre DSO confermano numerose corrispondenze reali, incluse tutte le 5 CP AT/MT dichiarate da AcegasApsAmga nel Piano 2025-2029.
3. Restano due gap interni, sette gap extraregionali, tag OSM non uniformi e casi di sovra-inclusione/semantica ambigua.
4. OSM non contiene, e questo gate non tenta di ricavare, capacità disponibile o fattibilità di connessione.
5. OpenInfraMap non viene elevata a fonte autonoma.
6. La decisione se accettare questa sorgente come baseline del futuro indicatore resta alla Chat 0.2 e all'utente.

## 12. Prossimo passo consentito

La Chat 0.2 può eseguire review indipendente di:
- regola QA >=60 kV;
- trattamento dei due gap interni;
- distinzione tra “CP ufficiale” e “geometria OSM plausibile”;
- eventuale accettazione della combinazione **OSM physical geometry + official service areas + official DSO cross-check** come base del futuro proxy.

Nessuna implementazione sull'universo candidati deve partire da questo documento senza la successiva decisione metodologica.
