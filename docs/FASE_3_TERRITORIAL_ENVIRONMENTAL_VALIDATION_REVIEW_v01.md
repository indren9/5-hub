# FASE 3 — VALIDAZIONE VINCOLI TERRITORIALI, AMBIENTALI E PAESAGGISTICI

**Chat:** 3.4 — Vincoli territoriali, ambientali e paesaggistici
**Data:** 2026-09-19
**Branch:** `chat-3.4-territorial-constraints`
**Stato documento:** REVIEW — TECHNICAL_PASS_PROPOSED
**Regia metodologica:** Chat Madre 5 HUB
**FASE 1 / FASE 2:** PASS / CLOSED / FROZEN — non modificate

## 1. Scopo e limiti

La Chat 3.4 ha validato e, quando tecnicamente sostenibile, materializzato le fonti correnti necessarie per descrivere:

- PGRA — pericolosità/rischio idraulico;
- frane e pericolosità geologica;
- Natura 2000;
- parchi, riserve, biotopi, parchi comunali e prati stabili pertinenti;
- Piano Paesaggistico Regionale vigente.

Il lavoro è di **validazione dati e fonti**, non di definizione dell’ammissibilità finale.

Non sono stati:
- costruiti candidati;
- applicati overlay ai candidati;
- introdotti buffer o soglie;
- assegnati pesi o punteggi;
- approvate esclusioni automatiche;
- modificate baseline FROZEN.

Le categorie `ADMISSIBILITY_CHECK`, `POTENTIAL_EXCLUSION`, `POTENTIAL_INDICATOR`, `CONTEXT_ONLY`, `TO_DECIDE` sono esclusivamente **proposte di ruolo futuro**.

## 2. Gerarchia delle fonti applicata

Per ciascun tematismo è stata seguita la gerarchia:

1. atto normativo / provvedimento vigente;
2. ente proprietario o gestore della fonte;
3. servizio GIS ufficiale;
4. metadata/capabilities;
5. materiale secondario o storico.

La baseline Claude/QGIS non è stata usata come fonte autorevole.

## 3. Pipeline riproducibile e storage

Script versionabile:

`scripts/acquire_validate_territorial_constraints_chat3_4_v01.py`

Comando:

```powershell
python scripts\acquire_validate_territorial_constraints_chat3_4_v01.py
```

Storage tecnico:

- raw/source: `5_HUB_FVG\02_external_sources\F3_CHAT_3_4\`
- QA: `5_HUB_FVG\05_intermediate_outputs\F3_CHAT_3_4\`

Manifest corrente:

`5_HUB_FVG\02_external_sources\F3_CHAT_3_4\source_manifest_v01.json`

SHA-256 manifest:

`B3FA6C361B8B8EC269C03B6A8304EF6C9F23785C45387BFF5ACBC9474DA3FB5B`

QA corrente:

`5_HUB_FVG\05_intermediate_outputs\F3_CHAT_3_4\TERRITORIAL_CONSTRAINTS_QA_v01.json`

SHA-256 QA:

`705C1D7EEE62241041220965169711EA13F4F901AD7FE7C75F75628EBA0C4A8D`

Il manifest registra URL, percorso, data di acquisizione, byte e SHA-256 degli artifact materializzati.

## 4. Esito sintetico

| Tema | Fonte corrente verificata | Esito tecnico | Ruolo futuro proposto | Gap residuo |
|---|---|---|---|---|
| PGRA | Autorità di Bacino Distrettuale Alpi Orientali / SIGMA | status giuridico corrente e set `PGRA2027` verificati; WFS live verificato | `ADMISSIBILITY_CHECK / TO_DECIDE` | binding esplicito WFS ↔ Delibera 12/2025 non esposto |
| Frane | Regione FVG / IRDAT | semantica layer pericolosità separata dal catasto/perimetri | `ADMISSIBILITY_CHECK` per pericolosità; `CONTEXT_ONLY / TO_DECIDE` per perimetri | classe/regola da decidere; riferimento cogente PAI da applicare caso per caso |
| Natura 2000 | Regione FVG / IRDAT + pagine/misure correnti | nomenclatura e geometrie WFS validate; typename `SIC` riconosciuto come tecnico/legacy | `ADMISSIBILITY_CHECK` | nessuna esclusione automatica approvata |
| Parchi/riserve | Regione FVG / IRDAT | conteggi correnti coerenti per le categorie principali | `ADMISSIBILITY_CHECK / TO_DECIDE` | disciplina specifica per categoria/sito da applicare |
| Biotopi | Regione FVG / atti istitutivi + WFS | corpus legale e tabella istituzionale = 42; WFS e testo riepilogativo regionale ancora = 40 | `ADMISSIBILITY_CHECK / TO_DECIDE` | disallineamento della pubblicazione regionale e due biotopi 2026 non ancora nel WFS — ISS-0011 |
| Prati stabili | Regione FVG / IRDAT | 10.486 geometrie; attributo `PRATO_TUTELATO` presente | `ADMISSIBILITY_CHECK` sul sottoinsieme tutelato | regola operativa da approvare |
| PPR | Regione FVG / PPR WebGIS-WFS | Variante 2/2025 verificata nel servizio live; subset pertinente materializzato | `ADMISSIBILITY_CHECK / TO_DECIDE` per singolo strato/regime | nessuna regola unica di esclusione definita |

## 5. PGRA — rischio/pericolosità idraulica

### 5.1 Fonte istituzionale e vigenza

Fonte proprietaria:

- Autorità di Bacino Distrettuale delle Alpi Orientali;
- portale SIGMA.

Evidenza normativa/corrente:

- Delibera n. 12 del 18 dicembre 2025;
- mappe revisionate adottate in salvaguardia;
- avviso pubblicato in G.U. n. 16 del 21 gennaio 2026;
- efficacia del quadro aggiornato dal **22 gennaio 2026**.

Il catalogo live SIGMA espone:

- set id = `40`;
- codice = `PGRA2027`;
- nome = `Piano di Gestione del rischio di alluvioni 2027-33 IN SALVAGUARDIA`;
- precedente set `PGRA2021` marcato come `SUPERATO`.

L’indice corrente contiene 5.448 mappe:
- 1.069 Carta della Pericolosità Idraulica;
- 1.069 Carta del Rischio Idraulico;
- 1.069 mappe altezze idriche TR30;
- 1.069 mappe altezze idriche TR100;
- 1.172 mappe altezze idriche TR300.

### 5.2 Geometria / CRS / copertura

Servizio GIS ufficiale verificato:

`https://sigma.distrettoalpiorientali.it/sigma/geo/sigma/wfs`

Layer live rilevanti:
- `sigma:Pericolo_direttiva_alluvioni`;
- `sigma:Rischio`.

CRS nativo dichiarato dal WFS:
- EPSG:3035.

Per il controllo tecnico è stato usato un envelope geografico FVG:
`BBOX(the_geom,12.20,45.50,14.00,46.75,'EPSG:4326')`.

Questo envelope è **solo un filtro tecnico** e non costituisce un ritaglio amministrativo FVG.

Conteggi live nell’envelope:
- pericolosità: 187.230 feature;
- rischio: 132.840 feature.

Sono stati preservati schema, conteggi/hits e campioni semantici; non viene promossa automaticamente la geometria bulk WFS come vettore normativo corrente.

### 5.3 Semantica e limite principale

Il layer di pericolosità espone almeno:
- `PDESCRIPT`;
- classi osservate nei campioni come `P1`, `P2`, `AA`.

Il layer rischio espone:
- `RISKCLASS`;
- `RCDESCRIPT`.

**Limite bloccante per la promozione a baseline operativa:** le capabilities/schema WFS non espongono un identificatore di versione che colleghi in modo machine-readable le feature live alla Delibera 12/2025 / set PGRA2027.

Di conseguenza:

- lo status giuridico/cartografico corrente è verificato;
- il servizio vettoriale live è verificato tecnicamente;
- l’equivalenza formale del vettore WFS alle mappe adottate in salvaguardia **non viene assunta**.

`ISS-0006` resta **OPEN**.

### 5.4 Licenza

Negli endpoint/materiali acquisiti non è stata identificata una licenza di riuso esplicita sufficiente per autorizzare redistribuzione del pacchetto vettoriale.

Stato: `TO_VERIFY`.

### 5.5 Ruolo futuro proposto

`ADMISSIBILITY_CHECK / TO_DECIDE`.

Non è approvata alcuna esclusione per classi PGRA.

## 6. Frane e pericolosità geologica

### 6.1 Fonte

Regione Autonoma Friuli Venezia Giulia / IRDAT.

Endpoint:

`https://serviziogc.regione.fvg.it/geoserver/wfs`

Snapshot: 2026-09-19.

Licenza: IODL 2.0 è lo standard regionale IRDAT, salvo eventuali condizioni specifiche del singolo metadato.

### 6.2 Layer di pericolosità

`IRDAT:CATFRANE_PERICOLOSITA`

- feature: **830**;
- CRS: EPSG:3004;
- geometrie osservate: 816 Polygon + 14 GeometryCollection;
- classi:
  - P1 = 2;
  - P2 = 39;
  - P3 = 349;
  - P4 = 440.

La semantica del servizio descrive classi di pericolosità collegate a magnitudo/probabilità. Dove vigono strumenti PAI cogenti, l’effetto urbanistico deve essere ricondotto alla disciplina applicabile e non ricavato dal solo codice P1–P4.

### 6.3 Distinzione dal Catasto Frane

Il layer sopra **non rappresenta l’intero Catasto Frane**.

Confronti:
- `CATFRANE_PERICOLOSITA`: 830 geometrie;
- `IRDAT:CATFRANE_PERIMFRANE`: 4.989 geometrie;
- la pagina regionale descrive il Catasto complessivo come circa 6.500 fenomeni franosi, oltre alle segnalazioni storiche.

Pertanto:
- perimetro frana;
- fenomeno censito;
- classe di pericolosità

sono oggetti distinti.

### 6.4 Ruolo futuro proposto

- `CATFRANE_PERICOLOSITA`: `ADMISSIBILITY_CHECK`;
- `CATFRANE_PERIMFRANE`: `CONTEXT_ONLY / TO_DECIDE`.

Nessuna classe P1/P2/P3/P4 è stata approvata come esclusione.

## 7. Natura 2000

### 7.1 Fonte e nomenclatura

Fonte istituzionale:
- Regione FVG — Rete Natura 2000;
- WFS regionale `SITI_PROT`.

La pagina corrente regionale distingue esplicitamente:
- pSIC;
- SIC;
- ZSC;
- ZPS.

Il typename WFS `SITI_PROT:SIC` è quindi un **nome tecnico legacy**, non una prova che tutte le feature siano oggi SIC.

### 7.2 Geometrie e CRS

`SITI_PROT:SIC`:
- 66 feature;
- EPSG:6708;
- 66 MultiPolygon.

Attributo `TIPO_SITO`:
- 29 `ZSC e ZPS coincidenti`;
- 20 `ZSC senza relazioni con altro sito NATURA 2000`;
- 10 `ZSC incluso in una ZPS`;
- ulteriori record ZSC, SIC e pSIC.

`SITI_PROT:ZPS`:
- 35 feature;
- EPSG:6708;
- 35 MultiPolygon.

Unione dei codici sito WFS:
- 72 codici unici;
- 29 codici presenti sia nel layer tecnico SIC/ZSC sia nel layer ZPS.

### 7.3 Valore normativo e procedura

I siti Natura 2000 hanno misure di conservazione e/o strumenti di gestione propri.

La disciplina VINCA regionale dimostra che la sola intersezione spaziale non equivale automaticamente a una esclusione modellistica generale:
- lo screening valuta la possibilità di incidenza significativa;
- esistono anche criteri di interferenza funzionale esterna;
- le prevalutazioni 2026 si applicano nel rispetto delle misure di conservazione.

### 7.4 Ruolo futuro proposto

`ADMISSIBILITY_CHECK`.

Nessuna esclusione automatica di tutto ciò che interseca un sito Natura 2000 è approvata.

## 8. Parchi, riserve, biotopi e altre aree protette

### 8.1 Parchi e riserve

Layer WFS correnti materializzati:

- `SITI_PROT:PARCHI_NATURALI_REG`: 2;
- `SITI_PROT:RISERVE_NATURALI_REG`: 13;
- `SITI_PROT:RIS_NATURALI_STATALI`: 3;
- `SITI_PROT:PARCHI_COMUNALI_RAFVG`: 18.

CRS:
- EPSG:6708.

La pagina regionale corrente conferma:
- 2 parchi naturali regionali;
- 3 aree naturali protette statali;
- 13 riserve naturali regionali;
- 18 parchi comunali/intercomunali;
- 3 zone Ramsar.

Le riserve regionali WFS espongono inoltre:
- `STATO_PERIMETRO`: 6 definitivo, 7 provvisorio;
- riferimenti istitutivi, PCS e regolamenti quando presenti.

Ruolo proposto:
`ADMISSIBILITY_CHECK / TO_DECIDE`, con verifica della disciplina specifica del singolo sito.

### 8.2 Biotopi — gap corrente

Il WFS `SITI_PROT:BIOTOPI` espone:
- 40 geometrie;
- EPSG:6708;
- 35 Polygon + 5 MultiPolygon.

La pubblicazione regionale corrente è **internamente disallineata**: il testo riepilogativo della pagina continua a dichiarare 40 biotopi, mentre la tabella della stessa pagina elenca anche:
- n. 41 — Monte Joanaz;
- n. 42 — Prati di Spignon/Varh e Monte Craguenza/Kraguojnca.

I relativi DPReg 065/2026 e 066/2026 li hanno istituiti formalmente. Il corpus legale corrente comprende quindi 42 biotopi, mentre il WFS verificato e il testo riepilogativo della pagina regionale sono ancora fermi a 40.

Gli atti istitutivi sono:
- DPReg 065/2026 del 09-06-2026 — Monte Joanaz;
- DPReg 066/2026 del 09-06-2026 — Prati di Spignon/Varh e Monte Craguenza/Kraguojnca.

Sono stati materializzati testo integrale e Allegato 2 cartografico:

- `DPReg_065_2026_TESTO_INTEGRALE_20260919.pdf`
  SHA-256 `54A3DDFA49DA70777027D6568D53C76E32551101B6FB712BCAA9FF7FF8607A20`
- `DPReg_065_2026_ALLEGATO2_20260919.pdf`
  SHA-256 `A86461F447A7755DCFADBBC21E4B6165EB94A3F90C4CB6AEA54CE4BFC947DE2A`
- `DPReg_066_2026_TESTO_INTEGRALE_20260919.pdf`
  SHA-256 `437DA2F428A71516BF24B26DAC05EDD268B44E39A8CBE56F33DDC7368E353E13`
- `DPReg_066_2026_ALLEGATO2_20260919.pdf`
  SHA-256 `FF537359DCE518BF7778BB0699F9BA6F16CD597361B48395365DE8FAE1FED141`

Le quattro firme magic sono `%PDF`.

Non è stata eseguita digitizzazione manuale.

`ISS-0011` è stato aperto per tracciare il gap GIS.

### 8.3 Prati stabili

`SITI_PROT:PRATISTABILI`:
- 10.486 geometrie;
- EPSG:6708;
- 10.091 Polygon;
- 395 MultiPolygon;
- aggiornamento attributo `DATA_AGG` osservato fino al 2025-07-29;
- `PRATO_TUTELATO = Sì`: 8.097;
- `PRATO_TUTELATO = No`: 2.389.

La pagina regionale indica il divieto di trasformazione dei prati inclusi nell’inventario tutelato.

Ruolo proposto:
`ADMISSIBILITY_CHECK` sul sottoinsieme giuridicamente tutelato, con regola operativa da approvare.

## 9. Piano Paesaggistico Regionale — PPR

### 9.1 Vigenza

Fonte istituzionale:
Regione Autonoma FVG — PPR.

Status:
- PPR originario efficace dal 10-05-2018;
- Variante 1 efficace dal 06-04-2023;
- **Variante 2 approvata con D.P.Reg. 0133/Pres del 12-12-2025, efficace dal 18-12-2025**.

Endpoint WFS:

`https://serviziogc.regione.fvg.it/geoserver/PPR/wfs`

CRS:
- EPSG:6708.

### 9.2 Prova di allineamento del servizio live

`PPR:v_aggiornamenti_ppr`:
- 67 feature;
- 53 feature con `numero_variante = 2/2025`;
- 12 con `1/2023`;
- 2 senza numero variante.

I record Variante 2 riportano il riferimento:
`D.P.Reg. 0133/Pres S.O n 30 al B.U.R. n.51 del 17/12/2025`.

Questo dimostra che il servizio live incorpora aggiornamenti della Variante 2/2025.

### 9.3 Layer pertinenti materializzati

Per ogni layer sono stati conservati:
- schema WFS;
- `resultType=hits`;
- geometria in `shape-zip` oppure GeoJSON per il layer di aggiornamenti;
- SHA-256.

| Layer | Feature |
|---|---:|
| `v_aggiornamenti_ppr` | 67 |
| `v_paesaggi_delimitazione_art_136` | 50 |
| `v_corsi_acqua_aree_tutelate` | 974 |
| `v_laghi_aree_tutelate` | 151 |
| `v_fascia_rispetto_battigia_marittima` | 1 |
| `v_fascia_rispetto_battigia_lagunare` | 1 |
| `v_ghiacciai` | 28 |
| `v_montagne_oltre_1600_m` | 316 |
| `v_territori_coperti_da_foreste_e_boschi` | 18.602 |
| `v_parchi_e_riserve_naturali_nazionali_o_regionali` | 18 |
| `v_aree_umide` | 3 |
| `v_usi_civici` | 13.477 |
| `v_zone_interesse_archeologico` | 1.534 |
| `v_ulteriori_contesti_archeologici` | 3.578 |
| `v_uc_immobili_int_storico_artistico_architettonico` | 3.311 |
| `v_ulteriori_contesti_immobili_decretati` | 73 |

Gli ZIP materializzati sono stati verificati con `zipfile.is_zipfile` e `testzip()`: tutti PASS.

Esempi di hash:
- boschi: `35AF30006A32C395C3380509CC66B0913516782FB2A1A02EEF47BA06A2E0204C`;
- usi civici: `E03B4C4B81ADFD0DFBB5A0D3D2159E07DCC0765109B6620425AEBA97799809AA`;
- art. 136: `70EAD10BFD6B5DF9F1865DE66CF54B9CD9691B762825EAB59DDE9C37621200F2`.

Gli hash completi sono nel manifest.

### 9.4 Valore normativo

La presenza di una feature PPR non viene trasformata in una regola uniforme di esclusione.

Occorre distinguere:
- beni ex art. 136;
- categorie ex art. 142;
- ulteriori contesti;
- elementi informativi/ricognitivi;
- prescrizioni specifiche, atti/decreti e discipline di piano.

Quando il servizio stesso rinvia al provvedimento istitutivo o a perimetri legalmente approvati, prevale l’atto vigente.

### 9.5 Ruolo futuro proposto

`ADMISSIBILITY_CHECK / TO_DECIDE` per singolo strato/regime.

Non è approvata una regola “intersezione PPR = esclusione”.

## 10. Licenze

### Regione FVG / IRDAT / PPR

Il catalogo IRDAT dichiara **IODL 2.0** come licenza standard regionale per i dati aperti.

Per prudenza:
- questa indicazione è registrata come standard di riferimento;
- eventuali eccezioni o condizioni specifiche del singolo metadato prevalgono.

### SIGMA / PGRA

Licenza di riuso/redistribuzione:
`TO_VERIFY`.

## 11. Questioni metodologiche da riportare alla Chat Madre

### Q-METH-3.4-A — PGRA: geometria operativa e classi

Decidere:
1. se il futuro modello usa pericolosità, rischio, aree allagabili o combinazioni distinte;
2. quali classi abbiano solo funzione di verifica e quali, se supportate dalla disciplina vigente, possano diventare esclusioni;
3. se il WFS SIGMA live sia accettabile come geometria operativa corrente in assenza di un binding di versione esplicito oppure se servano vettori ufficiali versionati.

### Q-METH-3.4-B — Frane: oggetto giuridicamente rilevante

Decidere:
1. se il riferimento futuro debba essere il layer di pericolosità, il PAI vigente applicabile, il perimetro di frana o una combinazione gerarchica;
2. quali classi P1–P4, se del caso, producano esclusione o sola verifica;
3. come trattare fenomeni censiti senza poligono di pericolosità.

### Q-METH-3.4-C — Natura 2000

Decidere se l’intersezione con ZSC/ZPS/pSIC/SIC:
- comporti una esclusione modellistica;
- oppure una verifica di ammissibilità/VINCA sito-specifica.

Evidenza normativa disponibile favorisce una gestione tramite verifica di incidenza e misure di conservazione, ma la scelta modellistica resta da approvare.

### Q-METH-3.4-D — Parchi, riserve, biotopi, prati stabili

Decidere per ciascuna categoria:
- eventuale esclusione;
- verifica di ammissibilità;
- trattamento dei perimetri provvisori;
- trattamento dei prati `PRATO_TUTELATO`;
- gestione dei due biotopi 2026 finché manca un vettore regionale aggiornato.

### Q-METH-3.4-E — PPR

Definire una matrice prescrizione → ruolo modellistico che distingua:
- art. 136;
- art. 142 per categoria;
- ulteriori contesti;
- componenti ricognitive/informative;
- casi in cui serve consultare l’atto/decreto specifico.

Nessuna di queste categorie è automaticamente esclusione finché l’utente non approva la regola.

## 12. Governance aggiornata

### DATA_REGISTRY

Aggiornati a `REVIEW`:
- `F3_SRC_PGRA_001`;
- `F3_SRC_PPR_001`;
- `F3_SRC_FVG_LANDSLIDE_001`;
- `F3_SRC_FVG_NATURA_001`.

### ISSUES

- `ISS-0006`: **OPEN** — status PGRA corrente verificato, ma binding vettoriale corrente ancora non chiuso;
- `ISS-0008`: **REVIEW** — procedura PPR corrente e materializzazione completate, in attesa di review Chat Madre;
- `ISS-0011`: **OPEN** — WFS biotopi 40 vs quadro legale/istituzionale 42.

Readback del registro eseguito dopo l’aggiornamento: PASS.

### DECISIONS

Nessuna nuova decisione metodologica registrata.

### PROJECT_SOURCE_OF_TRUTH

Non modificato. Il consolidamento autorevole compete alla Chat Madre/utente dopo review.

## 13. Quality gate Chat 3.4

| Controllo | Esito | Nota |
|---|---|---|
| Dispatch e baseline F1/F2/F3 letti | PASS | F1/F2 non riaperte |
| Governance viva verificata | PASS | SOT + register |
| Branch dedicato | PASS | `chat-3.4-territorial-constraints` |
| PGRA corrente: status/atto/set | PASS | Delibera 12/2025, vigenza 22-01-2026, PGRA2027 |
| PGRA vettore corrente normativamente versionato | GAP DOCUMENTATO | ISS-0006 OPEN |
| Frane: fonte/semantica/copertura | PASS | hazard ≠ perimetri ≠ catasto |
| Natura 2000: nomenclatura/geometrie | PASS | typename SIC legacy gestito |
| Parchi/riserve principali | PASS | conteggi correnti coerenti |
| Biotopi: copertura vettoriale corrente | GAP DOCUMENTATO | 40 WFS vs 42 legali; ISS-0011 |
| PPR vigente post Variante 2 | PASS | 53 record Variante 2 nel layer aggiornamenti |
| PPR: estrazione riproducibile | PASS | selected layers materializzati e hashati |
| Hash / lineage | PASS | manifest + QA |
| Role matrix | PASS | file separato |
| Nessuna esclusione approvata implicitamente | PASS | solo proposte/TO_DECIDE |
| Registro aggiornato e readback | PASS | DATA_REGISTRY + ISSUES |
| Source of Truth non alterato | PASS | review richiesta |
| Baseline FROZEN non modificata | PASS | controllo Git finale richiesto |
| QA automatico | PASS | `technical_checks_pass=true` |

## 14. Stato proposto

**TECHNICAL_PASS_PROPOSED / REVIEW**

Il PASS è esclusivamente tecnico-operativo.

Non chiude:
- FASE 3;
- ISS-0006;
- ISS-0011;
- questioni metodologiche Q-METH-3.4-A…E.

`ISS-0008` è proposto per review indipendente della Chat Madre e potrà essere risolto solo dopo tale review.

## 15. Fonti istituzionali principali

- PGRA / SIGMA: `https://sigma.distrettoalpiorientali.it/portal/`
- PGRA WFS: `https://sigma.distrettoalpiorientali.it/sigma/geo/sigma/wfs`
- PPR FVG: `https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/pianificazione-gestione-territorio/FOGLIA21`
- PPR WFS: `https://serviziogc.regione.fvg.it/geoserver/PPR/wfs`
- IRDAT: `https://irdat.regione.fvg.it/`
- WFS regionale: `https://serviziogc.regione.fvg.it/geoserver/wfs`
- Frane FVG: `https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/geologia/FOGLIA20/`
- Natura 2000 FVG: `https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/tutela-ambiente-gestione-risorse-naturali/FOGLIA203/`
- Aree protette FVG: `https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/tutela-ambiente-gestione-risorse-naturali/FOGLIA41/`
- Decreti regionali: `https://decreti.regione.fvg.it/`
