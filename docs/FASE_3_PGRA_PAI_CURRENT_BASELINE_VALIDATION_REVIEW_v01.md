# FASE 3 — Validazione baseline idrogeologica corrente PGRA + PAI

**Chat:** 3.11 — Baseline idrogeologica corrente PGRA + PAI
**Data:** 2026-09-20
**Branch:** `chat-3.11-pgra-pai-current-baseline`
**Stato documento:** REVIEW — TECHNICAL_QUALITY_GATE_PASS_PROPOSED
**Regia metodologica:** Chat 0.2 — Chat Madre 5 HUB
**Decisioni vincolanti:** DEC-0039, DEC-0040, DEC-0056
**Issue:** ISS-0006, ISS-0012

## 1. Scopo e limiti

Questa attività chiude il quality gate dati corrente PGRA + PAI per lo screening macro-regionale dei 5 HUB.
Non ridefinisce la metodologia e non apre la Fase 4.

Non sono stati introdotti:
- scoring, pesi o soglie;
- modellazione idraulica o geotecnica;
- nuove mappe di pericolosità;
- esclusioni automatiche basate sulle sole classi PGRA o PAI.

La sola presenza in una classe di pericolosità non viene trasformata in esclusione.
## 2. Baseline e governance applicate

Sono state lette integralmente le baseline F1/F2 FROZEN, la review Chat 3.4, la role matrix e l'handoff 3.4.
Sono stati verificati sul Google Drive vivo PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER.

Regole applicate:
- DEC-0039: per PGRA si cerca prima un binding forte geometria↔versione vigente; in assenza di binding pubblico verificabile è autorizzato il WFS ufficiale live con caveat/version lineage;
- DEC-0040: per frane il riferimento principale è il PAI vigente completo; Catasto Frane e perimetri inventariali sono supporto conoscitivo;
- DEC-0056: autorizza questa validazione senza riaprire le regole metodologiche.

## 3. Pipeline riproducibile

Script:
`scripts/acquire_validate_pgra_pai_chat3_11_v01.py`

Storage:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_11\`

Output tecnici:
- `source_manifest_v01.json` — SHA-256 `24E9FD460EA1D72A020C624C15A2A2DAC819B1D7B7E22B111BFA6E4177C0F67C`;
- `qa_validation_v01.json` — SHA-256 `FC6F7EA395DA7F68745095479F879706FB2B95827BE35215C254D40C009DB945`.
## 4. PGRA — stato corrente

Fonte proprietaria: Autorità di Bacino Distrettuale delle Alpi Orientali / SIGMA.

Il quadro corrente verificato è quello derivante dalla Delibera n. 12 del 18-12-2025:
- mappe revisionate adottate in salvaguardia;
- avviso in G.U. n. 16 del 21-01-2026;
- efficacia dal 22-01-2026;
- successiva fase di osservazioni avviata nel 2026.

Sono stati preservati anche gli HTML ufficiali di lineage corrente in `pgra\`.

Servizio WFS ufficiale:
`https://sigma.distrettoalpiorientali.it/sigma/geo/sigma/wfs`

Layer:
- `sigma:Pericolo_direttiva_alluvioni`;
- `sigma:Rischio`.

CRS nativo verificato dai file materializzati: EPSG:3035 — ETRS89 / LAEA Europe.
## 5. PGRA — ricerca del binding e fallback DEC-0039

La ricerca mirata ha incluso:
- stato/atti correnti del Distretto;
- pagine SIGMA 2026;
- WFS GetCapabilities;
- DescribeFeatureType dei due layer;
- contenuti machine-readable disponibili nelle capabilities/schema.

Nel WFS/schema materializzato non compaiono marcatori espliciti quali:
`PGRA2027`, `Delibera 12`, `18.12.2025`, `18/12/2025`, `2027-33`.

Esito: **binding forte machine-readable WFS ↔ Delibera 12/2025 / quadro PGRA corrente NON DIMOSTRATO**.

Si applica quindi esattamente il fallback già autorizzato da DEC-0039:
**CURRENT_OFFICIAL_LIVE_GEOMETRY_WITH_VERSION_CAVEAT**.

Questo non dichiara equivalenza normativa non dimostrata; separa:
1. currentness giuridico/cartografica verificata sulle fonti ufficiali;
2. geometria operativa corrente prelevata dal WFS live ufficiale.
## 6. PGRA — baseline geometrica materializzata

Per riproducibilità è stato usato il filtro tecnico:
`BBOX(the_geom,12.20,45.50,14.00,46.75,'EPSG:4326')`.

È un envelope tecnico che contiene il FVG, non un ritaglio amministrativo della Regione.

| Layer | Conteggio WFS | Record DBF | Geometria | SHA-256 ZIP |
|---|---:|---:|---|---|
| Pericolosità | 187.230 | 187.230 | MultiSurface / ShapeZIP, EPSG:3035 | `F05C36817726A0B7F06C8E82E617DBFC2F817D7AF7ACD4A846BFCC274D9D54E2` |
| Rischio | 132.840 | 132.840 | MultiSurface / ShapeZIP, EPSG:3035 | `00F103637A541522DADA659EF84B4A560DCAA2F47FA465293DA6FCD4BB370B05` |

Schema pericolosità:
- `OBJECTID`;
- `PDESCRIPT`.

Schema rischio:
- `RISKCLASS`;
- `RCDESCRIPT`.

Tutti gli ZIP: `zipfile.is_zipfile = true`, `testzip() = null`.
## 7. PAI — corpus vigente applicabile al FVG

Le fonti correnti del Distretto confermano che, dopo il primo aggiornamento PGRA, il PAI continua a esprimere conoscenze, cartografie e disposizioni per pericolosità geologica e da valanga; la componente idraulica è ricondotta al PGRA.

Per il territorio FVG il corpus pertinente, nelle porzioni territorialmente applicabili, comprende:
- bacino Isonzo — UOM ITN004;
- bacino Livenza — UOM ITN006;
- bacino Piave — UOM ITN007;
- bacino Tagliamento — UOM ITN009;
- sottobacino Fella;
- bacini dei fiumi della Regione Friuli Venezia Giulia — UOM ITR061.

Il PAI non è quindi un singolo layer regionale statico, ma un corpus di piani/bacini con cartografie, Norme di Attuazione e aggiornamenti mediante decreti segretariali/procedure previste dalle NTA.
## 8. PAI — cartografia e disciplina ufficiale

Sono state materializzate le pagine ufficiali delle tavole di pericolosità e rischio geologico per i sei corpus sopra indicati.
L'inventario automatico delle pagine contiene **627 URL PDF** complessivi.

Il numero 627 è il conteggio dei collegamenti cartografici presenti nelle pagine di bacino acquisite:
non rappresenta il numero di tavole ricadenti esclusivamente nel FVG e non viene usato come indicatore.

Sono state inoltre preservate le discipline principali:
- `PAI4_NORME_ATTUAZIONE.pdf` — SHA-256 `CB8F485D77F05B4AAB456F12C00990857545E8AFA1367A0BA19386038F428034`;
- `PAI_FELLA_NORME_ATTUAZIONE.pdf` — `2F72CE6730004D05535CDA1736CCE37C6DB12BE4B5EA23413ED70E524F435FEE`;
- `PAI_LIVENZA_PRIMA_VARIANTE_RELAZIONE_NORME.pdf` — `612E670E535581F8FA27A48B0C499907EE8E3F587334C255300856CA93416D4B`;
- `PAIR_FVG_RELAZIONE_NORME.pdf` — `E1518C82D9C1DB26D2E79F91C1FB57F5516C79B414BACE082ECDDD8F8140095A`.

La cartografia pubblicata include anche aggiornamenti successivi alla base storica; il corpus va quindi letto insieme agli aggiornamenti ufficiali vigenti.
## 9. PAI — gap vettoriale pubblico corrente

La pagina/FAQ ufficiale Regione FVG rinvia al Distretto per perimetrazioni e norme e specifica che i **file vettoriali della cartografia ufficiale possono essere richiesti all'Autorità di bacino distrettuale**.

Nella ricerca pubblica svolta non è stato identificato un download vettoriale unico, completo e versionato del PAI corrente FVG che:
- copra tutti i corpus pertinenti;
- includa in modo dimostrabile tutti gli aggiornamenti vigenti;
- distingua correttamente classi PAI e zone di attenzione;
- sia legato a una versione/atto corrente con lineage completo.

Il gap è quindi **dimostrato, non mascherato**.

La cartografia ufficiale corrente è verificabile nelle tavole del Distretto; per ottenere una baseline vettoriale PAI normativamente forte resta necessario acquisire i vettori ufficiali dal Distretto oppure ottenere un binding pubblico equivalente.
## 10. Distinzioni semantiche obbligatorie

**PAI:** strumento normativo/tecnico-operativo vigente per pericolosità geologica e da valanga, articolato per bacini.

**Pericolosità PAI:** aree classificate secondo la disciplina applicabile. La classe non viene convertita automaticamente in esclusione.

**Rischio:** concetto distinto dalla sola pericolosità, legato anche agli elementi esposti/vulnerabilità; non sostituisce la carta della pericolosità.

**Zone di attenzione geologica:** la FAQ FVG le descrive come informazione complementare; un punto IFFI può rappresentare un fenomeno non delimitato nel PAI e non ancora classificato. Se il punto ricade già in un perimetro PAI, non costituisce automaticamente una zona di attenzione.

**Catasto Frane:** banca dati conoscitiva e dinamica di fenomeni, perimetri, pericolosità, elementi a rischio, opere e dati geomorfologici. Non è automaticamente equivalente al PAI vigente completo.
## 11. Rapporto con CATFRANE e viste regionali correnti

Il GeoServer regionale corrente espone popolazioni diverse:

| Layer | Feature | CRS | Ruolo |
|---|---:|---|---|
| `UTIL_TER:VW_DATA_FRANE_PERICOLOSITA` | 2.904 | EPSG:6708 | supporto regionale per pericolosità |
| `UTIL_TER:VW_DATA_FRANE_PERIMETRO` | 6.919 | EPSG:6708 | perimetri inventariali / supporto |
| `IRDAT:VW_FR_IFFI` | 6.568 | EPSG:6708 | punti IFFI / supporto |
| `IRDAT:CATFRANE_PERICOLOSITA` | 830 | EPSG:3004 | layer legacy già usato in Chat 3.4 |
| `IRDAT:CATFRANE_PERIMFRANE` | 4.989 | EPSG:3004 | layer legacy già usato in Chat 3.4 |

La distribuzione RNDT ufficiale per il dataset regionale “Pericolosità” rimanda alla vista `UTIL_TER:VW_DATA_FRANE_PERICOLOSITA`.
La differenza di conteggio dimostra che i layer `CATFRANE_*` e le viste correnti `UTIL_TER/VW_*` non sono popolazioni equivalenti.

Nessuno di questi layer viene però promosso a sostituto del PAI corrente completo senza prova di equivalenza/version lineage.
## 12. Snapshot regionali materializzati

Sono stati preservati:
- `vw_data_frane_pericolosita_20260920.zip` — 2.904 record — SHA-256 `6A51C9CE8FB03F1E601FC07367001D56A95D2C189FF154ECEF499D16A4A9FCC1`;
- `vw_data_frane_perimetro_20260920.zip` — 6.919 record — `1A152D3DFC8C810C43B379B267CE3F64DB038E874E5FC578A474C8F66C677D53`;
- `vw_fr_iffi_20260920.zip` — 6.568 record — `03F64550311480430E39C606871961E015E3E338405B752FCC5B0B4AFD47985A`.

Tutti gli ZIP hanno integrità PASS e conteggio DBF coerente con il WFS live.

Sono stati inoltre conservati schema/hits dei due layer `CATFRANE_*` per confronto riproducibile.

Ruolo autorizzato: **SUPPORT_ONLY / CONTEXT**, coerentemente con DEC-0040.
## 13. Quality gate

| Controllo | Esito | Nota |
|---|---|---|
| Governance e baseline lette | PASS | F1/F2 non riaperte |
| PGRA currentness giuridica | PASS | Delibera 12/2025, efficacia 22-01-2026 |
| Binding forte WFS↔versione | NOT FOUND | ricerca documentata |
| Fallback DEC-0039 applicato | PASS | WFS ufficiale live + caveat |
| PGRA schema/CRS/count/hash | PASS | 187.230 / 132.840 |
| Corpus PAI FVG identificato | PASS | sei corpus pertinenti |
| Disciplina PAI acquisita | PASS | NTA/relazioni principali |
| Cartografia ufficiale corrente verificata | PASS | pagine/tavole Distretto + lineage aggiornamenti |
| Vettore PAI completo pubblico | GAP DOCUMENTATO | vettori ufficiali su richiesta al Distretto |
| PAI ↔ CATFRANE distinto | PASS | nessuna equivalenza inventata |
| Snapshot supporto regionale | PASS | 2.904 / 6.919 / 6.568 |
| Nessun hard filter/scoring nuovo | PASS | coerente DEC-0039/0040 |
| Fase 4 aperta | NO | vincolo rispettato |

**Quality gate tecnico Chat 3.11: PASS WITH LIMITATIONS / REVIEW.**
## 14. Stati proposti delle issue

### ISS-0006 — PGRA
**PROPOSE_RESOLVED_PROCEDURALLY**

Motivo:
- quadro vigente verificato;
- binding forte non reperito dopo ricerca mirata;
- la condizione di fallback prevista da DEC-0039 è soddisfatta;
- WFS ufficiale live materializzato con caveat, schema, CRS, conteggi e hash.

La chiusura effettiva resta a Chat 0.2 / utente.

### ISS-0012 — PAI / frane
**READY_WITH_LIMITATIONS**

Motivo:
- corpus corrente e disciplina identificati;
- cartografia ufficiale corrente verificata e indicizzata;
- supporto GIS regionale corrente materializzato;
- resta non dimostrata la disponibilità pubblica di un vettore PAI unico/completo/current-versioned; la Regione indica la richiesta al Distretto come canale per i vettori ufficiali.

La limitazione è compatibile con la chiusura del quality gate dati macro, ma non va trasformata in equivalenza PAI↔Catasto.
## 15. Implicazioni operative

Per un futuro screening macro, subordinatamente alla review della Chat Madre:
- PGRA: usare i due snapshot WFS live come geometria operativa corrente con flag di version caveat;
- PAI: usare le fonti ufficiali del Distretto come riferimento normativo/cartografico;
- viste regionali frane: usare solo come supporto conoscitivo e per pre-screening, mantenendo il flag di non-equivalenza al PAI;
- casi finalisti: verificare sempre disciplina e cartografia PAI/PGRA corrente puntuale.

Questa review **non autorizza**:
- apertura Fase 4;
- esclusioni automatiche per classe;
- scoring o pesi;
- promozione dei layer regionali a PAI ufficiale completo.

## 16. Artifact

Repository:
- `docs/FASE_3_PGRA_PAI_CURRENT_BASELINE_VALIDATION_REVIEW_v01.md`;
- `docs/FASE_3_PGRA_PAI_SOURCE_MATRIX_v01.csv`;
- `docs/HANDOFF_CHAT_3.11_PGRA_PAI_v01.md`;
- `scripts/acquire_validate_pgra_pai_chat3_11_v01.py`.

OneDrive:
`5_HUB_FVG\02_external_sources\F3_CHAT_3_11\`

Il manifest è la fonte tecnica puntuale per URL, timestamp, byte e SHA-256.
