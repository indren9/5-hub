# FASE 3 — URBAN PLANNING VALIDATION REVIEW v01

**Chat:** 3.2 — Urbanistica, poligoni sorgente e disponibilità
**Fase:** 3 — Inventario e validazione dei dati
**Data:** 2026-09-18
**Stato:** REVIEW — PASS tecnico-operativo proposto alla Chat Madre
**Mandato:** `docs/DISPATCH_CHAT_3.2_URBAN_PLANNING_POLYGONS_v01.md`

## 1. Scopo e limiti

Obiettivo della Chat 3.2 è validare le fonti urbanistiche utili alla futura costruzione dei poligoni candidati e delimitare il problema della disponibilità/proprietà, senza costruire `CANDIDATES_RAW`.

Sono rimaste READ ONLY:
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md` — FROZEN;
- `docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md` — baseline Chat 3.1;
- PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER come governance viva.

Questa chat non decide categorie urbanistiche ammissibili, superficie minima, criteri di esclusione o collocazione metodologica della proprietà/disponibilità.

## 2. Esito sintetico

1. **Non è stata individuata e verificata una singola mosaicatura regionale 2026 dei PRGC con vigenza documentata region-wide** utilizzabile direttamente come fonte definitiva dei poligoni.
2. I WFS `CER:ZONE_INDUSTRIALI_ARTIG_D` e `CER:ZONE_COMMERCIALI_H` sono servizi live, ma il contenuto deriva dalla **Mosaicatura PRG 2018** e non rappresenta automaticamente l'urbanistica vigente 2026.
3. Il confronto con fonti comunali correnti dimostra mismatch temporali multipli; Polcenigo documenta anche modifiche di zonizzazione/perimetro successive allo snapshot CER.
4. EagleFVG è un'infrastruttura utile per la consultazione/pubblicazione dei PRGC comunali, ma la presenza di una configurazione pubblica non prova da sola la vigenza o l'allineamento legale della geometria.
5. Il probe riproducibile ha rilevato configurazioni PRG pubbliche standard per **147 dei 215 Comuni FVG**; i 68 casi non rilevati non sono classificati come assenza del PRGC, ma come necessità di ricerca tramite fonte comunale/regionale alternativa.
6. La Regione stessa, in documentazione tecnica 2024, prevede che un primo strato di zoning messo a disposizione a supporto dei Comuni debba essere verificato dagli uffici tecnici comunali per il grado di aggiornamento.
7. Per `ISS-0003` esiste evidenza sufficiente a classificare la Mosaicatura PRG 2018 come **HISTORICAL / NON_CURRENT_FOR_2026**. Si propone alla Chat Madre la risoluzione dell'issue nel suo significato stretto, senza confondere ciò con l'approvazione della futura fonte P1.
8. Per `ISS-0009` sono state identificate fonti ufficiali parziali e dinamiche, ma **non un dataset region-wide validato di disponibilità effettiva**. L'issue resta OPEN ma meglio delimitata.

## 3. Fonti e procedura di verifica

### 3.1 Fonti principali
- Regione FVG — GeoServer/WFS: `https://serviziogc.regione.fvg.it/geoserver/wfs`
- Regione FVG — Linee guida layer mappatura CER 2023:
  `https://prod-energia.regione.fvg.it/export/sites/energia/documents/CER/LINEE-GUIDA-LAYER-MAPPATURA-FVG.PDF`
- Regione FVG — Allegato tecnico DGR 1174/2024:
  `https://www.regione.fvg.it/rafvg/export/sites/default/RAFVG/ambiente-territorio/pianificazione-gestione-territorio/FOGLIA43/allegati/29112024_Allegato_tecnico_alla_Circolare.pdf`
- EagleFVG: `https://eaglefvg.regione.fvg.it/eagle/`
- ISTAT — elenco Comuni italiani:
  `https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv`
- siti istituzionali dei Comuni campione;
- Regione FVG — patrimonio immobiliare e Consorzi di sviluppo economico locale.
### 3.2 Controlli riproducibili eseguiti

Script:
`scripts/validate_urban_planning_sources.py`

Il controllo:
- importa l'elenco ISTAT e verifica che i Comuni FVG correnti siano 215;
- interroga integralmente i layer CER D e H;
- aggrega per Comune cardinalità, `DATA_VAL` e `VARIANTE`;
- interroga il GetCapabilities WFS regionale;
- prova le configurazioni pubbliche EagleFVG secondo naming standard, senza interpretare un mancato match come assenza del PRGC;
- integra un campione comunale verificato con fonti istituzionali correnti;
- produce una tabella region-wide e un JSON di evidenza.

Comando di riproduzione:

`python .\scripts\validate_urban_planning_sources.py --istat-csv .\tmp\Elenco-comuni-italiani.csv --sample-evidence .\docs\FASE_3_URBAN_PLANNING_CURRENT_SAMPLE_v01.csv --output-dir .\docs --delay 0.02`

Output:
- `docs/FASE_3_URBAN_PLANNING_MUNICIPAL_COVERAGE_v01.csv`;
- `docs/FASE_3_URBAN_PLANNING_VALIDATION_EVIDENCE_v01.json`;
- `docs/FASE_3_URBAN_PLANNING_CURRENT_SAMPLE_v01.csv`.

## 4. Verifica della Mosaicatura PRG 2018
Le Linee guida regionali 2023 per la mappatura CER documentano esplicitamente che:
- le zone commerciali H derivano da estratti della **Mosaicatura PRG 2018**;
- le zone industriali/artigianali D derivano dalla stessa Mosaicatura PRG 2018;
- l'acquisizione per il lavoro CER risale al 20/04/2023, ma questo non modifica la data urbanistica della mosaicatura sorgente.

### 4.1 Evidenza quantitativa WFS

Al run del 2026-09-18:
- `CER:ZONE_INDUSTRIALI_ARTIG_D`: 4.155 feature;
- `CER:ZONE_COMMERCIALI_H`: 1.466 feature;
- tra i 215 Comuni correnti, nessun `DATA_VAL` osservato nei due layer è successivo al 2018;
- D: `DATA_VAL` osservati tra 2001-04-12 e 2018-05-03;
- H: `DATA_VAL` osservati tra 2010-08-12 e 2018-04-12.

### 4.2 Evidenza amministrativa strutturale

Il layer D contiene ancora codici comunali non correnti:
- 030038 Fiumicello;
- 030050 Ligosullo;
- 030096 Rivignano;
- 030119 Teor;
- 030125 Treppo Carnico;
- 030134 Villa Vicentina;
- 093003 Arzene;
- 093048 Valvasone.
Il layer H contiene ancora, tra gli altri, Fiumicello, Rivignano, Villa Vicentina, Arzene e Valvasone.

Questa evidenza è incompatibile con l'uso del CER come rappresentazione amministrativamente corrente dei 215 Comuni FVG.

### 4.3 Classificazione tecnica

Stato proposto dei due WFS CER:
**ENDPOINT_CURRENT / CONTENT_HISTORICAL / NON_CURRENT_FOR_2026 / SUPPORT_ONLY**.

Uso consentito proposto:
- benchmark storico;
- screening iniziale;
- confronto;
- pista per recuperare zone e metadati;
- mai prova automatica della zonizzazione vigente di un Comune nel 2026.

## 5. Esistenza di una fonte regionale corrente region-wide

Il GetCapabilities WFS regionale corrente contiene diversi layer urbanistici e alcuni layer comunali/territoriali, ma nel controllo eseguito non emerge un singolo feature type che possa essere dimostrato come mosaicatura completa e vigente dei PRGC dei 215 Comuni.

Sono visibili, tra gli altri:
- layer ASTER_MF per specifici Comuni;
- `CMC_SIMFVG:v_zoneomogenee_carnia`;
- `PRG_CCC:v_zooning_ravascletto`;
- i due layer CER storici.

La documentazione regionale 2024 fornisce un'indicazione decisiva sullo stato del problema: quando la Regione mette a disposizione un primo strato informativo di zoning comunale, questo **deve essere verificato dagli uffici tecnici comunali per il grado di aggiornamento**.
Conclusione operativa:
**nessuna fonte region-wide corrente è stata verificata come sufficiente a sostituire la validazione comunale della vigenza**.

Questa conclusione è prudente: non afferma l'inesistenza assoluta di qualunque banca dati regionale interna o non pubblica; afferma che non è stata trovata una fonte pubblica e documentata che superi il quality gate del mandato.

## 6. EagleFVG: copertura e ruolo

Il probe standard ha rilevato:
- Comuni FVG correnti ISTAT: 215;
- configurazioni PRG pubbliche standard EagleFVG rilevate: 147;
- configurazioni standard non rilevate: 68.

Interpretazione obbligatoria:
- `PUBLIC_CONFIG_DETECTED` = accesso tecnico rilevato;
- non equivale a `CURRENT_PRGC_VERIFIED`;
- `NOT_DETECTED_BY_STANDARD_PROBE` non equivale ad assenza di PRGC o di servizio Eagle.

EagleFVG è quindi una componente utile della procedura P1, non una garanzia autonoma di vigenza per tutti i Comuni.

## 7. Campione corrente e confronto CER

| Comune | Prov. | CER | Evidenza corrente | Esito |
|---|---|---:|---|---|
| Tavagnacco | UD | var. 9, 2015-01-29 | var. 22 approvata 30/01/2024, pubblicata EagleFVG 19/11/2025 | mismatch temporale |
| Gorizia | GO | var. 40, 2017-04-14 | varianti 60/61 esecutive nel 2025; fonte comunale corrente | mismatch temporale |
| Monfalcone | GO | var. 54, 2017-05-22 | elaborati di zonizzazione 64+71; var. 71 approvata 31/01/2025 | mismatch temporale |
| San Canzian d'Isonzo | GO | var. 17, 2016-08-04 | var. 29 approvata 10/07/2025 | mismatch temporale |
| Polcenigo | PN | var. 26, 2015-12-24 | var. 30 approvata 14/12/2023 / BUR 03/01/2024 | mismatch temporale e geometrico |
| Zoppola | PN | var. 46, 2017-05-25 | servizio comunale PRGC vigente con accesso EagleFVG; variante corrente da ricostruire | accesso corrente, lineage da completare |
| Trieste | TS | var. 1, 2017-05-11 | pagina comunale PRGC vigente e consultazione interattiva; ultima variante effettiva da ricostruire | fonte corrente, lineage da completare |

La tabella completa e la distinzione tra fonte corrente verificata e sola accessibilità sono in:
`docs/FASE_3_URBAN_PLANNING_CURRENT_SAMPLE_v01.csv`.

### 7.1 Caso Polcenigo

La documentazione della variante 30 descrive modifiche di zonizzazione e correzioni di perimetri cartografici. Questo dimostra che la divergenza rispetto al CER non è soltanto un numero di variante più recente: può cambiare la geometria e la classificazione delle aree.

Conseguenza:
una geometria CER non deve essere aggiornata solo sostituendo un attributo `VARIANTE`; il perimetro corrente va acquisito dalla fonte urbanistica vigente.

## 8. Semantica D/H e uso come fonte geometrica

I layer CER estraggono:
- zone H per la componente commerciale;
- zone D1/D2/D3 e miste per la componente industriale/artigianale.

Questa tassonomia può essere utilizzata come indizio semantico e chiave di riconciliazione, ma non costituisce una regola di ammissibilità.

Non viene approvato in Chat 3.2 alcun assunto del tipo:
`zona D/H = candidato ammissibile`.

La futura Fase 4 dovrà operare su geometrie correnti con il codice/descrizione nativi del PRGC, conservando la relazione alla categoria omogenea senza perdere la semantica locale.
## 9. Procedura P1 proposta alla Chat Madre

### P1-A — Ricostruzione current-first con lineage comunale

Procedura tecnica proposta, NON APPROVATA:

1. partire dall'elenco ISTAT corrente dei 215 Comuni;
2. per ogni Comune individuare la fonte ufficiale del PRGC vigente e delle varianti efficaci;
3. distinguere chiaramente `adottata`, `approvata`, `esecutiva/efficace`;
4. usare geometrie vettoriali EagleFVG/Regione quando il Comune ne conferma l'allineamento alla versione vigente;
5. quando la geometria vettoriale non è disponibile o la vigenza non è dimostrabile, acquisire gli elaborati ufficiali comunali e registrare il gap geometrico;
6. non digitalizzare automaticamente PDF come unica fonte autorevole senza controllo;
7. versionare ogni acquisizione con URL, data, atto/variante, hash e stato di vigenza;
8. produrre solo successivamente una mosaicatura tecnica controllata, senza eliminare il lineage comunale;
9. mantenere il CER 2018 come livello storico di confronto, non come base corrente.

### P1-B — Strategia ibrida di efficienza

La procedura può usare EagleFVG e servizi regionali come acceleratore:
- dove la configurazione pubblica è presente e la versione è verificata, si acquisisce il vettore;
- dove manca o non è dimostrato l'aggiornamento, si passa al sito/atto comunale;
- i casi irrisolti restano esplicitamente `TO_VERIFY`.

Questa strategia riduce il lavoro manuale senza trasformare la copertura tecnica di Eagle in una falsa copertura normativa.

### Alternative non proposte come baseline corrente

- usare direttamente il CER 2018: non supera il gate temporale;
- usare un generico layer regionale non accompagnato da prova di aggiornamento comunale: non supera il gate di vigenza;
- usare solo PDF/ortofoto senza lineage urbanistico: insufficiente come fonte primaria dei perimetri.
## 10. Schema minimo di lineage per Fase 4

Per ogni geometria urbanistica sorgente futura dovranno essere conservati almeno:

- `source_id`;
- codice ISTAT corrente del Comune;
- denominazione Comune;
- identificativo/titolo del PRGC;
- numero variante;
- stato procedurale: adottata / approvata / efficace-esecutiva;
- atto di approvazione e data;
- data di efficacia/pubblicazione BUR quando applicabile;
- URL istituzionale;
- data di accesso/acquisizione;
- formato sorgente;
- layer/feature identifier nativo;
- codice zona/sottozona nativo;
- descrizione/destinazione urbanistica nativa;
- eventuale categoria omogenea;
- CRS/EPSG sorgente;
- scala/accuratezza dichiarata o nota di assenza;
- hash del file/materializzazione quando applicabile;
- `currentness_status`;
- evidenza usata per validare la vigenza;
- trasformazioni applicate alla geometria;
- producer/script e versione;
- geometry hash/version nelle fasi in cui verrà creato il candidato.

Questo schema supporta le decisioni F2-D5/F2-D6 senza creare ancora identità candidate.

## 11. Proprietà e disponibilità — `ISS-0009`

### 11.1 Distinzioni necessarie
Sono concetti diversi:
- **destinazione urbanistica**: cosa il PRGC consente/regola;
- **proprietà**: titolarità del bene;
- **patrimonio pubblico disponibile**: classificazione patrimoniale del bene pubblico;
- **disponibilità commerciale/operativa**: lotto o immobile effettivamente offerto/assegnabile in una certa data;
- **disponibilità fisica**: superficie effettivamente utilizzabile, libera o trasformabile;
- **fattibilità per Hub**: risultato di ulteriori vincoli urbanistici, infrastrutturali, ambientali e tecnici.

Nessuna di queste dimensioni può essere dedotta automaticamente da un'altra.

### 11.2 Fonti ufficiali verificate

**Regione FVG — patrimonio immobiliare.**
La pagina Amministrazione Trasparente dichiara dati aggiornati al 30/06/2026 e pubblica:
- patrimonio immobiliare disponibile;
- identificativi catastali del patrimonio disponibile;
- patrimonio indisponibile;
- demanio storico/artistico/culturale.

Copertura: beni della Regione, non l'intero territorio FVG.
Uso possibile: fonte puntuale di proprietà/classificazione patrimoniale pubblica; non prova automatica di idoneità fisica o disponibilità per un Hub.

**Consorzi di sviluppo economico locale.**
La Regione elenca sei Consorzi attivi. Le loro funzioni includono acquisto, vendita e locazione di aree e fabbricati negli agglomerati di competenza.

Sono state verificate fonti operative che pubblicano lotti/immobili disponibili o avvisi di assegnazione/locazione, tra cui NIP, COSEVEG/COSEF e Carnia Industrial Park.
Copertura: agglomerati/beni di competenza dei singoli Consorzi.
Limite: informazione frammentata e dinamica; non costituisce un dataset region-wide uniforme.

**Comuni / patrimoni pubblici locali.**
Piani di alienazione, inventari patrimoniali e bandi possono fornire evidenza puntuale, ma la copertura e la struttura sono comunali e devono essere censite caso per caso.

### 11.3 Esito su `ISS-0009`

Non è stato verificato un dataset unico che rappresenti contemporaneamente, per tutte le superfici FVG:
- proprietà;
- disponibilità effettiva;
- disponibilità fisica;
- disponibilità commerciale/operativa.

Stato proposto:
**OPEN / DELIMITED**.

La scelta se usare disponibilità/proprietà in generazione, ammissibilità o verifica puntuale resta `Q-METH-3.1-C` e non viene assunta da Chat 3.2.

## 12. Evidenza materializzata in OneDrive

Directory:
`5_HUB_FVG\02_external_sources\urban_planning_validation_20260918\`

Materializzati:
- elenco Comuni ISTAT;
- Linee guida CER 2023;
- Allegato tecnico regionale 2024;
- GetCapabilities WFS regionale;
- snapshot codici Comune dei layer CER D/H;
- patrimonio disponibile regionale 30/06/2026;
- identificativi catastali del patrimonio disponibile;
- `source_manifest_v01.json`.

Il manifest conserva URL, byte e SHA-256 dei file materializzati.

## 13. Stato delle issue

### `ISS-0003`
**Stato proposto: REVIEW / PROPOSED_RESOLVED nel significato stretto.**

Evidenza:
- lineage ufficiale alla Mosaicatura PRG 2018;
- nessun `DATA_VAL` post-2018 nei layer osservati;
- presenza di codici comunali storici;
- mismatch con varianti comunali correnti;
- caso Polcenigo con modifiche geometriche/di zonizzazione.

Interpretazione: è risolto il dubbio se il CER possa essere assunto come urbanistica vigente 2026: **no**.

Resta distinta e ancora da approvare la scelta della fonte/procedura P1 per la futura Fase 4.

### `ISS-0009`
**Stato proposto: OPEN / DELIMITED.**

Evidenza: esistono fonti ufficiali parziali di patrimonio e disponibilità, ma non una copertura region-wide uniforme di disponibilità effettiva.

## 14. Nuova issue proposta

### `ISS-0010` — Lineage comunale della vigenza PRGC non uniformemente automatizzabile

La pubblicazione/consultazione digitale è eterogenea; EagleFVG ha ampia ma non completa rilevazione standard e, anche quando accessibile, richiede verifica di versione/atto corrente.

Impatto: la futura mosaicatura P1 necessita di una pipeline comunale con stato di validazione esplicito e gestione dei casi manuali.

Stato proposto: **OPEN — P1 / urbanistica**.
## 15. Quality gate Chat 3.2

| Controllo | Esito | Evidenza |
|---|---|---|
| fonte region-wide vigente verificata direttamente | **PASS** | nessuna fonte pubblica verificata supera il gate; necessità di validazione comunale documentata |
| procedura sostitutiva realistica/riproducibile | **PASS** | §9 + script + coverage table |
| vigenza/data non inferite | **PASS** | stati ACCESS e CURRENTNESS separati |
| CER 2018 classificato correttamente | **PASS** | §§4–7 |
| copertura comunale costruita | **PASS** | 215 righe ISTAT; 147 configurazioni standard Eagle rilevate |
| nessuna categoria urbanistica ammissibile introdotta | **PASS** | §8 |
| nessuna soglia di superficie introdotta | **PASS** | nessuna |
| nessun `CANDIDATES_RAW` costruito | **PASS** | nessun artifact candidato |
| proprietà, disponibilità e urbanistica distinte | **PASS** | §11 |
| gap residui espliciti | **PASS** | §§13–14 |
| evidenze materializzate con hash | **PASS** | §12 + manifest |
| registri aggiornati e riletti | **PASS** | DATA_REGISTRY + ISSUES riletti dopo scrittura |
| Git commit tracciabile | **PASS** | commit tecnico `e46ed56` |

### Esito tecnico

**CHAT 3.2 = PASS TECNICO-OPERATIVO PROPOSTO / REVIEW PER CHAT MADRE.**

La FASE 3 complessiva resta IN CORSO.
La FASE 4 non viene aperta da questa chat.

## 16. Elementi da sottoporre alla Chat Madre

1. accettare o modificare la procedura P1 current-first/ibrida descritta al §9;
2. verificare e, se appropriato, accettare la proposta di risoluzione di `ISS-0003`;
3. mantenere `ISS-0009` aperta e decidere `Q-METH-3.1-C`;
4. decidere se l'acquisizione completa dei 215 PRGC vigenti debba avvenire ancora in Fase 3 oppure come input controllato della Fase 4;
5. definire quale livello minimo di vigenza/lineage è necessario per autorizzare un Comune alla generazione dei poligoni;
6. mantenere CER 2018 come storico/supporto e non promuoverlo a baseline corrente.
## 17. Fonti web principali

- Regione FVG, Linee guida layer mappatura FVG/CER 2023:
  https://prod-energia.regione.fvg.it/export/sites/energia/documents/CER/LINEE-GUIDA-LAYER-MAPPATURA-FVG.PDF
- Regione FVG, Allegato tecnico DGR 1174/2024:
  https://www.regione.fvg.it/rafvg/export/sites/default/RAFVG/ambiente-territorio/pianificazione-gestione-territorio/FOGLIA43/allegati/29112024_Allegato_tecnico_alla_Circolare.pdf
- Regione FVG, patrimonio immobiliare:
  https://www.regione.fvg.it/rafvg/cms/RAFVG/GEN/amministrazione-trasparente/FOGLIA14/FOGLIA1/
- Regione FVG, Consorzi di sviluppo economico locale:
  https://www.regione.fvg.it/rafvg/cms/RAFVG/economia-imprese/industria/FOGLIA5/
- Tavagnacco, Variante 22:
  https://www.comune.tavagnacco.ud.it/Novita/Notizie/Pubblicata-online-la-Variante-n.-22-al-PRGC
- Gorizia, varianti PRGC:
  https://comune.gorizia.it/it/amministrazione-trasparente-5819/pianificazione-e-governo-del-territorio-272820/varianti-al-prgc-272822
- Monfalcone, PRGC:
  https://www.comune.monfalcone.go.it/it/amministrazione-trasparente-5724/pianificazione-e-governo-del-territorio-5794/pianificazione-territoriale-30539/piano-regolatore-generale-comunale-prgc-249162
- San Canzian d'Isonzo, varianti:
  https://www.comune.sancanziandisonzo.go.it/it/amministrazione-trasparente-10292/pianificazione-e-governo-del-territorio-16324/pianificazione-territoriale-16437/delibere-16439
- Polcenigo, Variante 30:
  https://www.comune.polcenigo.pn.it/it/amministrazione-trasparente-54903/pianificazione-e-governo-del-territorio-54976/variante-n30-al-prgc-247428
- Zoppola, PRGC vigente:
  https://www.comune.zoppola.pn.it/it/servizi-206518/piano-regolatore-generale-comunale-prgc-217182
- Trieste, PRGC:
  https://www.comune.trieste.it/it/guide-223180/territorio-iu-223181/nta-norme-tecniche-di-attuazione-e-pianificazione-generale-223182
