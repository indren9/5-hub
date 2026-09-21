# DISPATCH — Chat 4.1 — Costruzione universo candidati V2-1

**Mandante:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Stato:** AUTHORIZED
**Branch:** `chat-4.1-candidate-universe-build`

## 1. Obiettivo

Costruire realmente l''universo dei poligoni candidati del MODEL_v2 applicando integralmente DQ-01 / DEC-0065.

Questa chat deve produrre:
- `CANDIDATE_UNIVERSE_v01`;
- `CANDIDATE_LINEAGE_v01`;
- mapping urbanistico auditabile verso G1–G5;
- QA completo e riproducibile.

NON deve definire criteri di scoring, pesi, normalizzazione o DQ-02+.

## 2. Worktree

Lavora esclusivamente in:

`C:\dev\5-hub\_worktrees\chat-4.1-candidate-universe-build`

Branch:

`chat-4.1-candidate-universe-build`

Non modificare altri worktree.

## 3. Baseline vincolanti

Leggere integralmente:
- `docs/PROJECT_MODEL_CONTRACT_REBASELINE_v01.md`;
- `docs/ROADMAP_METODOLOGICA_v2.md`;
- `docs/FASE_1_HUB_DEFINITION_REBASELINED_v03.md`;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md`;
- `docs/CANDIDATE_UNIVERSE_CONTRACT_v01.md`;
- `docs/DQ01_APPROVAL_v01.md`;
- `docs/NOTE_TECHNICAL_CONSULTANCY_MIN_AREA_8000_v01.md`;
- `docs/REBASELINE_APPROVAL_AND_PHASE3_CLOSE_v01.md`.

Verificare inoltre:
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER;
- DEC-0065;
- DATA_REGISTRY;
- ISSUES.

## 4. Regole DQ-01 già approvate

### Fonti
Urbanistica ufficiale best-available, current-first.

Gerarchia:
- S1 = vettore corrente verificato;
- S2 = vettore ufficiale best-available con currentness non chiusa;
- S3 = piano corrente verificato ma geometria proxy;
- S4 = CER/Mosaicatura PRG 2018 solo ultima risorsa storica;
- S5 = nessuna geometria utilizzabile → gap QA, nessuna geometria inventata.

### Classi generatrici
- `G1_PRODUCTIVE`;
- `G2_COMMERCIAL_TERTIARY`;
- `G3_LOGISTICS_TRANSPORT`;
- `G4_MIXED_RELEVANT`;
- `G5_TECHNICAL_UTILITY_ENERGY`.

Servizi pubblici generici/sociali/sanitari/scolastici senza componente pertinente NON generano candidati.

### Geometria
- solo poligoni;
- repair deterministico quando necessario;
- multipart disconnessi splittati;
- nessun dissolve generalizzato;
- merge solo per identità logica documentata;
- nessuna soglia geometrica universale arbitraria.

### Superficie minima HARD
Calcolare `area_m2` dopo repair + split, in CRS metrico documentato.

- `area_m2 >= 8000` → può entrare;
- `area_m2 < 8000` → esclusione HARD con `MIN_AREA_8000_NOT_MET`.

Gli 8.000 m² sono area lorda del poligono.

### HARD ammessi
Solo:
- geometria poligonale valida/riparabile;
- area >= 8.000 m²;
- FVG;
- classe generatrice approvata;
- deduplicazione della stessa alternativa fisica.

NON usare come HARD:
- proprietà/catasto;
- disponibilità commerciale;
- currentness non verificata;
- ambiente;
- energia;
- TEN-T;
- accessibilità;
- PAI/PGRA/PPR/Natura 2000;
- score o ranking.

## 5. Attività A — Inventario sorgenti effettivamente utilizzabili

Partire dal materiale Fase 3 già validato.

Per ogni Comune:
- identificare fonte geometrica effettivamente disponibile;
- assegnare source tier S1–S5;
- registrare dataset_id;
- path/URL;
- stato currentness;
- eventuale proxy;
- feature ID nativo disponibile.

NON assumere che coverage 215/215 significhi automaticamente 215/215 geometrie materializzate.

Se un Comune non ha geometria utilizzabile:
- NON digitalizzare manualmente;
- marcare `NO_USABLE_POLYGON_SOURCE`;
- quantificare il gap.

## 6. Attività B — Mapping urbanistico G1–G5

Costruire una tabella auditabile:

`docs/CANDIDATE_GENERATOR_CLASS_MAPPING_v01.csv`

Campi minimi:
- source_dataset_id;
- municipality_code;
- source_layer;
- native_zone_code;
- native_zone_description;
- generator_class;
- mapping_rule;
- mapping_status;
- evidence;
- notes.

Regole:
- nessuna classificazione opaca basata solo su keyword non documentate;
- conservare sempre codice e descrizione nativa;
- categorie ambigue → `GENERATOR_CLASS_UNRESOLVED`;
- nessun candidato può entrare nella baseline finale con mapping unresolved.

Se serve una regola automatica, deve essere esplicita, verificabile e accompagnata da QA.

## 7. Attività C — Costruzione geometrica

Pipeline minima:
1. ingestione sorgente;
2. controllo CRS;
3. reproiezione nel CRS metrico operativo documentato;
4. controllo geometry type;
5. make_valid / repair deterministico;
6. estrazione componenti poligonali;
7. split dei multipart disconnessi;
8. calcolo area_m2;
9. filtro HARD 8.000 m²;
10. canonicalizzazione duplicati;
11. assegnazione ID/versioning/hash;
12. esportazione baseline.

Ogni trasformazione deve essere registrata nel lineage.

## 8. Identità e versioning

Produrre almeno:
- `candidate_id`;
- `candidate_version`;
- `universe_version`;
- `geometry_hash`;
- `canonical_identity_key`;
- `supersedes_candidate_id` quando applicabile.

Usare ID logico stabile, non un progressivo fragile e non il geometry hash come ID.

## 9. Output pesanti

Storage:

`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\04_geodatabases\V2_1_CANDIDATE_UNIVERSE`

Produrre almeno:
- `CANDIDATE_UNIVERSE_v01.gpkg`;
- `CANDIDATE_LINEAGE_v01.csv`;
- `CANDIDATE_EXCLUSIONS_v01.csv`;
- `CANDIDATE_SOURCE_GAPS_v01.csv`;
- manifest con SHA256;
- QA summary machine-readable.

Se tecnicamente utile, aggiungere Parquet/GeoParquet, ma il GPKG resta artifact GIS principale.

## 10. Output repository

Produrre almeno:
- `docs/CANDIDATE_GENERATOR_CLASS_MAPPING_v01.csv`;
- `docs/V2_1_CANDIDATE_UNIVERSE_QA_v01.md`;
- `docs/V2_1_CANDIDATE_UNIVERSE_SUMMARY_v01.csv`;
- `docs/HANDOFF_CHAT_4.1_CANDIDATE_UNIVERSE_BUILD_v01.md`;
- script/config/test necessari in `scripts/`, `config/`, `tests/`.

## 11. QA obbligatorio

Verificare almeno:
- 100% candidate_id univoci e non null;
- 100% candidate_version/universe_version valorizzati;
- 100% geometry_hash valorizzati;
- 0 geometrie null/empty/non poligonali;
- 0 geometrie invalide non gestite;
- 100% candidati con `area_m2 >= 8000`;
- tutte le esclusioni <8000 registrate;
- 100% generator_class risolto per i candidati inclusi;
- 100% currentness/proxy status valorizzato;
- source-gap report per 215/215 Comuni;
- duplicati/canonicalizzazione documentati;
- overlap non risolti quantificati;
- conteggi e superficie per Comune, source tier e G1–G5;
- determinismo del rerun con stessi input/config;
- manifest e hash completi;
- nessun indicatore DQ-02 applicato.

## 12. Benchmark storico

Le 1.377 aree Claude/QGIS possono essere confrontate solo come benchmark descrittivo.

NON:
- forzare il numero di candidati verso 1.377;
- usare la vecchia soglia ~5.000 m²;
- usare i poligoni Claude come baseline autorevole.

## 13. Decisioni emergenti

Se durante l''implementazione emerge una scelta sostanziale NON coperta da DQ-01, non scegliere implicitamente.

Esempi:
- nuova famiglia territoriale;
- nuova classe generatrice;
- tolleranza metrica con impatto materiale;
- regola di merge non basata su identità;
- esclusione sostanziale aggiuntiva.

Registrare il punto e fermare solo il ramo interessato; completare tutto ciò che è possibile senza quella decisione.

## 14. Quality gate finale

La Chat 4.1 può proporre PASS solo se:
- universo realmente costruito;
- lineage completo;
- filtro 8.000 m² applicato correttamente;
- mapping G1–G5 auditabile;
- gap sorgente espliciti;
- QA numerico completo;
- rerun deterministico;
- artifact pesanti salvati in OneDrive;
- registri proposti per aggiornamento;
- git diff --check PASS;
- test PASS;
- branch pulito e pushato.

## 15. Stato finale

Concludere con:
- numero candidati finali;
- numero esclusi per <8.000 m²;
- distribuzione G1–G5;
- distribuzione S1–S5;
- Comuni senza geometria utilizzabile;
- principali gap/limiti;
- hash principali;
- commit;
- proposta PASS/FAIL.

Poi fermarsi per review Chat 0.2.

NON aprire DQ-02.
