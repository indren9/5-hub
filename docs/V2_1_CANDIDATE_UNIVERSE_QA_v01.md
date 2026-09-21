# V2-1 CANDIDATE UNIVERSE — QA v01

**Chat:** 4.1 — Costruzione universo candidati V2-1
**Data:** 2026-09-21
**Stato:** REVIEW — PROPOSED TECHNICAL PASS
**Autorità metodologica:** DQ-01 / DEC-0065 ACCEPTED
**Output principale:** `CANDIDATE_UNIVERSE_v01`

## 1. Perimetro del controllo

Il QA verifica la costruzione dell'universo dei poligoni candidati senza introdurre DQ-02:
nessun indicatore, peso, normalizzazione, score o funzione obiettivo è stato calcolato.

La build applica:
- urbanistica ufficiale best-available current-first;
- classi generatrici G1–G5;
- CER/Mosaicatura PRG 2018 solo come fallback dichiarato;
- repair deterministico e split dei multipart;
- nessun dissolve/merge generalizzato;
- superficie minima HARD di 8.000 m² dopo repair e split;
- ID/versioning/geometry_hash/lineage obbligatori.

CRS operativo: **EPSG:6708**.


## 2. Copertura delle sorgenti

Presenza per Comune del tier effettivamente usato:
- S1: 4 Comuni;
- S2: 99 Comuni;
- S3: 4 Comuni;
- S4: 103 Comuni;
- S5: 5 Comuni.

I 5 Comuni S5, senza geometria poligonale utilizzabile, sono:
**Preone, Stregna, Rivignano Teor, Treppo Ligosullo, Valvasone Arzene**.

Per i 103 Comuni con vettore corrente/best-available materializzato, la selezione layer è:
- 95 `SELECTED_DETERMINISTIC_RULE`;
- 7 `SELECTED_AUDITED_OVERRIDE`;
- 1 `SELECTED_ADDITIVE_CLASS` (Ruda, layer esplicito attività produttive).

Gli override sono configurati in `config/candidate_layer_overrides_v01.csv` e conservano motivazione ed evidenza.
Per i Comuni senza layer corrente selezionabile, CER 2018 entra solo come S3/S4 e resta esplicitamente proxy/storico.


## 3. Risultato finale

Candidati finali: **3.993**.

Distribuzione G1–G5:
- G1_PRODUCTIVE: **2.550**;
- G2_COMMERCIAL_TERTIARY: **928**;
- G3_LOGISTICS_TRANSPORT: **152**;
- G4_MIXED_RELEVANT: **319**;
- G5_TECHNICAL_UTILITY_ENERGY: **44**.

Distribuzione dei candidati per source tier:
- S1: **167**;
- S2: **2.709**;
- S3: **55**;
- S4: **1.062**;
- S5: **0**.

Superficie lorda complessiva dei candidati: **251.227.636,615 m²** (251,228 km²).
Il dettaglio completo di conteggi e superfici per Comune, source tier e G1–G5 è in
`CANDIDATE_DISTRIBUTION_QA_v01.csv`. I Comuni con 0 candidati finali sono 16:
5 per assenza di geometria utilizzabile (S5) e 11 con sorgente disponibile ma senza
poligoni che superino congiuntamente mapping generatore e soglia HARD.

La revisione finale del mapping ha corretto le zone esplicitamente miste D/H
(es. D3H3, H3D3 e varianti equivalenti) verso G4 senza modificare la cardinalità dell'universo.


## 4. Exclusions e mapping

Esclusioni per superficie: **5.125** record con `MIN_AREA_8000_NOT_MET`.
Controllo indipendente: tutti hanno `observed_value < 8000`; massimo osservato **7.994,464 m²**.
Il candidato finale di area minima misura circa **8.001,732 m²**.

Ulteriori esclusioni:
- `NOT_APPROVED_GENERATOR_CLASS`: **69.852** parti geometriche;
- `GENERATOR_CLASS_UNRESOLVED`: **4.016** parti geometriche;
- `NO_POLYGON_AFTER_REPAIR`: **89** record.

Tabella mapping finale: **7.592** combinazioni semantiche aggregate:
- 1.838 `RESOLVED_INCLUDED`;
- 5.051 `RESOLVED_EXCLUDED`;
- 703 `GENERATOR_CLASS_UNRESOLVED`, corrispondenti a **3.933 feature sorgente**.

Dopo repair/split tali categorie producono **4.016 parti geometriche** escluse con
`GENERATOR_CLASS_UNRESOLVED`. Nessuno dei 3.993 candidati ha generator_class unresolved:
le categorie semanticamente insufficienti non vengono forzate verso G1–G5.


## 5. Geometria, duplicati e overlap

Nel GPKG finale:
- 3.993/3.993 geometrie sono Polygon non null e non empty;
- 3.993/3.993 geometrie risultano valide;
- 0 geometry_hash duplicati;
- 0 candidati sotto 8.000 m²;
- candidate_id univoci e non null: PASS.

Sono registrate **461** coppie con overlap areale positivo, per circa
**1.782.527,576 m²** di area pairwise complessiva. Non sono state fuse automaticamente:
DQ-01 non approva soglie universali di overlap e la sovrapposizione da sola non prova identità.

Durante la lettura di alcuni shapefile ufficiali sono comparsi warning OGR/pyogrio
su winding order, ring non chiusi o traduzione Polygon/MultiPolygon.
La pipeline usa lettura con fix, make_valid quando necessario, estrazione delle sole componenti
poligonali e split multipart; il QA finale conferma 0 geometrie invalide residue.
Le fonti originali non sono state modificate.


## 6. Determinismo e hash logici

Secondo run sugli stessi input/config: **PASS**.

Hash logici:
- universe: `648A76F925FE65567CB88CE688A1C41F158DC1C8B90E1E95BCABEA7611D38F39`;
- lineage: `C60DB10499111A4A8FD0E1F2B1A85AEF0EA28820F471799795EEE1EC7689E134`;
- exclusions: `409BB7915634D2BF855C22ED436AD8F1C8CC05395D7BA98CBF4CF91F1F085B7D`;
- mapping: `01002F2009C96FE26C515C901E80AABCF2D3ADE2CA4BD0C6C3495E3268C89C58`;
- source gaps: `0EFB6D1F9606261A752AEABB8C0BF0A66B9A38E585AC1A3C822BCE964CFB3799`.

Hash fisici principali del run finale:
- GPKG: `57B51E3B381743554E105F8E1959674AE426A3F20D379BC709EFA8E8BE78969B`;
- lineage CSV: `6C11D43EBEA8FF60FF63582393632248DB65EB07340CBDF20B3BC8B7F69AA55A`;
- exclusions CSV: `2FBD7CC5B5B733FC7679706DFBF66E833BC259AC8A01CBAF9A8FC05A9E087D24`;
- mapping CSV: `4A80A85FBF3AE839C34D91E44E74812975269C4A2B0FB7467FD83ABAEBC4E002`;
- distribution QA: `1B2F5E068FE306D9046A9DD3F277E680087B489F2A74794640F8DD538DDDB65A`;
- machine QA JSON: `F3D1958701089CBFBE6F39F5B34E1BBFB219F46268D8B8B624C1BE52C172A15E`;
- manifest: `1B36B52444D4B56C6FD23D66AB27956FB13A7B247EE2BE738B576A8BCCC02B40`.

Il manifest registra input e artifact con SHA-256; controllo di integrità: PASS.


## 7. Limiti dichiarati

1. **5 Comuni S5** non hanno geometria utilizzabile: nessun poligono è stato inventato.
2. **103 Comuni usano S4** e 1.062 candidati finali derivano da CER 2018 come proxy storico.
3. **99 Comuni usano S2**: geometria ufficiale best-available, ma currentness non integralmente chiusa.
4. Restano **703 categorie native unresolved**: sono conservate nel mapping audit e non generano candidati.
5. Gli overlap non identici restano quantificati, non canonicalizzati con soglie arbitrarie.
6. Alcune fonti presentano difetti geometrici sorgente gestiti deterministicamente.
7. Nessuna conclusione è tratta su proprietà, disponibilità commerciale, ambiente, energia, TEN-T o accessibilità.

## 8. Quality gate

QA machine-readable: **PASS** (`all_required_checks_pass=true`).
Determinismo: **PASS**.
Test automatici Chat 4.1: **5 passed**.
DQ-02 fields assenti: **PASS**.

**QUALITY GATE PROPOSTO: PASS / REVIEW CHAT 0.2.**

Questo PASS è tecnico-operativo e non rende l'artifact ACCEPTED o FROZEN:
la decisione resta alla Chat 0.2 e all'utente secondo la governance del progetto.
