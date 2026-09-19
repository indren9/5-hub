# FASE 3 — CURRENT URBAN PLANNING VALIDATION REVIEW v01

**Chat:** 3.8 — Acquisizione e validazione urbanistica corrente FVG
**Data:** 2026-09-19
**Stato:** REVIEW
**TECHNICAL_QUALITY_GATE:** PASS
**PHASE_4_READINESS:** NOT_READY
**Issue principale:** ISS-0010 = OPEN, decisione finale riservata alla Chat Madre

## 1. Mandato

Questa attività esegue DEC-0032 secondo il dispatch
`DISPATCH_CHAT_3.8_CURRENT_URBAN_PLANNING_ACQUISITION_v01.md`.

Obiettivo: costruire una base urbanistica current-first tracciabile per tutti i 215 Comuni FVG,
senza costruire candidati Hub, senza scegliere categorie urbanistiche ammissibili,
senza applicare soglie geometriche e senza modificare le baseline FROZEN di Fase 1 e Fase 2.

## 2. Baseline e governance rispettate

- FASE 1: PASS / CLOSED / FROZEN — non modificata.
- FASE 2: PASS / CLOSED / FROZEN — non modificata.
- DEC-0032: ACCEPTED — currentness basata sul PRGC effettivamente vigente.
- DEC-0044: ACCEPTED — autorizza il mandato Chat 3.8 e separa gate tecnico da readiness Fase 4.
- ISS-0010: OPEN — non risolta autonomamente da questa chat.
- CER D/H 2018: mantenuti esclusivamente come HISTORICAL / SUPPORT.
- Accesso EagleFVG: non trattato come prova sufficiente di variante vigente.

## 3. Strategia di acquisizione

La procedura usa una gerarchia prudente:

1. censimento ufficiale IRDAT dei dataset PRGC comunali;
2. confronto con evidenza comunale indipendente già verificata nel campione Chat 3.2;
3. ricerca supplementare su pagine, atti e documenti dei Comuni per i casi non coperti da IRDAT;
4. promozione a `CURRENT_VECTOR_VERIFIED` solo quando variante corrente e vettore risultano allineati;
5. mantenimento esplicito dei casi non chiusi come lineage incompleto o `TO_VERIFY`.

IRDAT è quindi usato come fonte ufficiale di discovery e distribuzione,
non come attestazione automatica che il contenuto vettoriale rappresenti l'ultima variante efficace.

## 4. Copertura ottenuta

La coverage finale contiene **215/215 Comuni FVG**, con 215 codici ISTAT univoci e nessuno stato vuoto.

| Stato finale | Comuni |
|---|---:|
| CURRENT_VECTOR_VERIFIED | 4 |
| CURRENT_PLAN_VERIFIED_NO_VECTOR | 1 |
| CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE | 167 |
| TO_VERIFY | 43 |
| **Totale** | **215** |

Il censimento IRDAT ha individuato **151 record PRGC comunali esatti**.
Per 24 casi senza record IRDAT è stato preparato un supplemento di fonti comunali ufficiali:
21 sorgenti sono state anche materializzate localmente con successo, 3 hanno restituito errore tecnico di fetch
e sono rimaste prudentemente `TO_VERIFY`.

## 5. Vettori correnti verificati e materializzati

| Comune | Variante verificata | Dataset | QA archivio | CRS | Nota CRS |
|---|---|---|---|---|---|
| Tavagnacco | 22 | IRDAT 12217 | PASS | RDN2008-TM33NE | .prj presente |
| Gorizia | 61 | IRDAT 12238 | PASS | RDN2008-TM33NE | .prj assente; CRS da metadata IRDAT |
| Monfalcone | 71 | IRDAT 12239 | PASS | RDN2008-TM33NE | .prj assente; CRS da metadata IRDAT |
| San Canzian d'Isonzo | 29 | IRDAT 12194 | PASS | RDN2008-TM33NE | .prj presente |

Tutti i quattro ZIP hanno superato `ZipFile.testzip()`.
Per ogni layer `.shp` è stata verificata la presenza del corrispondente `.dbf` e `.shx`.
Il controllo strutturale dettagliato è in
`docs/FASE_3_CURRENT_URBAN_PLANNING_VECTOR_QA_v01.csv`.

L'assenza di `.prj` per Gorizia e Monfalcone non è nascosta:
il CRS è dichiarato dai metadata ufficiali IRDAT, ma i pacchetti non sono autonomamente auto-descrittivi sul CRS.

## 6. Evidenza che IRDAT non può essere promosso automaticamente a "corrente"

Il confronto con fonti comunali conferma che il catalogo/distribuzione IRDAT può essere disallineato
rispetto all'ultima variante efficace.

Caso esplicito: **Polcenigo**.
Il record IRDAT disponibile riporta Variante 26, mentre la fonte comunale già validata documenta
la Variante 30 approvata con DCC 62 del 14/12/2023 e pubblicata sul BUR il 03/01/2024.

Di conseguenza la regola DEC-0032 è confermata operativamente:
la disponibilità del vettore regionale non sostituisce la verifica di vigenza.

## 7. Casi senza vettore corrente verificato

**Grado** è classificato `CURRENT_PLAN_VERIFIED_NO_VECTOR`:
la pagina comunale ufficiale identifica esplicitamente il PRGC vigente,
ma in questa attività non è stato acquisito un vettore ufficiale allineato.

I **167** casi `CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE` hanno una fonte istituzionale
o un record PRGC ufficiale utile, ma manca almeno uno degli elementi necessari per promuovere il vettore:
ultima variante efficace, prova di assenza di varianti successive, allineamento del download,
oppure geometria corrente utilizzabile.

I **43** casi `TO_VERIFY` restano esplicitamente aperti.
L'elenco completo e la motivazione per Comune sono nella coverage CSV;
nessuno di essi è stato sostituito silenziosamente con CER 2018.

## 8. Artifact e tracciabilità

Output leggeri versionabili:

- `docs/FASE_3_CURRENT_URBAN_PLANNING_COVERAGE_v01.csv`
- `docs/FASE_3_CURRENT_URBAN_PLANNING_EVIDENCE_v01.json`
- `docs/FASE_3_CURRENT_URBAN_PLANNING_SOURCE_SUPPLEMENT_v01.csv`
- `docs/FASE_3_CURRENT_URBAN_PLANNING_VECTOR_QA_v01.csv`
- questo review document;
- script in `scripts/` dedicati alla pipeline Chat 3.8.

Output pesanti/evidenze raw:

`5_HUB_FVG\02_external_sources\F3_CHAT_3_8\`

Il manifest contiene **51 artifact** tra pagine IRDAT, detail record, fonti comunali e pacchetti vettoriali.
`source_manifest_v01.json`:
SHA-256 `3F8422B29F85B1C5FE9B9D2DCEB1FC7A05119A5FAD88B574FC09655479378482`,
25.007 byte alla chiusura del run.

Controllo preservation alla SESSION CLOSE: **PASS** — 51/51 artifact presenti,
0 file mancanti, 0 mismatch SHA-256.

## 9. Quality gate tecnico

| Controllo | Esito | Evidenza |
|---|---|---|
| Coverage 215/215 Comuni | PASS | 215 righe, 215 codici ISTAT univoci |
| Stato finale esplicito per Comune | PASS | nessun `currentness_status` vuoto |
| CER 2018 non promosso a corrente | PASS | 0 righe con CER come `geometry_source` corrente |
| Vettori promossi solo con verifica indipendente | PASS | 4 casi; confronto con campione comunale frozen |
| Integrità ZIP e componenti Shapefile | PASS | 4/4; DBF+SHX presenti per ogni SHP |
| CRS controllato | PASS con nota | 4/4 metadata CRS; 2/4 senza PRJ interno |
| Evidenze raw + SHA-256 | PASS | manifest OneDrive e hash |
| Gap senza vettore corrente espliciti | PASS | 1 no-vector, 167 lineage incomplete, 43 TO_VERIFY |
| Nessuna costruzione candidati / ammissibilità | PASS | nessun output CANDIDATES, merge, dissolve o soglia minima |
| Fase 1 e Fase 2 FROZEN non modificate | PASS | `git diff --exit-code` = 0 sui due file |
| PROJECT_CONTROL_REGISTER aggiornato prudentemente | PASS | DATA_REGISTRY + ISS-0010, stato issue mantenuto OPEN |

**TECHNICAL_QUALITY_GATE = PASS.**

Questo PASS certifica la corretta esecuzione e tracciabilità dell'acquisizione,
non la sufficienza della base dati per costruire l'universo dei candidati.

## 10. PHASE_4_READINESS

**PHASE_4_READINESS = NOT_READY.**

Motivazione: la base corrente non consente ancora di costruire un universo poligonale autorevole region-wide.
Restano 43 Comuni `TO_VERIFY`, 167 casi con lineage incompleto e un Comune con piano corrente verificato
ma senza vettore corrente acquisito. Tali gap possono modificare direttamente l'universo delle aree
che la futura Fase 4 dovrà costruire.

Non viene quindi autorizzata implicitamente alcuna mosaicatura "best effort".

## 11. Stato ISS-0010

**ISS-0010 resta OPEN.**

La Chat 3.8 ha ridotto e reso misurabile il problema,
ma non esistono le condizioni per proporre `RESOLVED`.
La decisione di review e l'eventuale ridefinizione del prossimo mandato spettano alla Chat Madre.

## 12. Aggiornamento governance viva

Nel `PROJECT_CONTROL_REGISTER` è stato:

- aggiunto `F3_SRC_FVG_PRGC_CURRENT_001` in DATA_REGISTRY con stato `REVIEW`;
- aggiornata la prossima azione di ISS-0010;
- mantenuto ISS-0010 nello stato `OPEN`.

Il PROJECT_SOURCE_OF_TRUTH non è stato modificato:
non è stata introdotta né approvata alcuna nuova decisione metodologica sostanziale.

## 13. Riproducibilità

Script principali:

- `scripts/acquire_validate_current_urban_planning_chat3_8_v01.py`
- `scripts/run_current_urban_planning_chat3_8_v01.py`
- `scripts/apply_current_urban_planning_source_supplement_v01.py`
- `scripts/qa_current_urban_planning_vectors_v01.py`

La pipeline parte dalle coverage/sample frozen già presenti in `docs/`,
scrive gli output leggeri in `docs/` e conserva le evidenze raw pesanti su OneDrive.

## 14. Limiti residui

1. La verifica "ultima variante efficace" non è chiusa per la maggioranza dei 215 Comuni.
2. I 151 record IRDAT non sono equivalenti a 151 PRGC correnti verificati.
3. Le pubblicazioni comunali hanno struttura eterogenea e richiedono controlli mirati.
4. Due dei quattro ZIP correnti verificati non contengono file `.prj`.
5. La disponibilità di un piano corrente in PDF/WebGIS non implica disponibilità di una geometria vettoriale riusabile.
6. La licenza/riuso delle singole fonti comunali non è stata generalizzata.

## 15. Conclusione operativa

La Chat 3.8 chiude il proprio mandato acquisitivo con **PASS tecnico**,
ma consegna alla Chat Madre una condizione di **NOT_READY per la Fase 4**.

Nessun candidato Hub è stato costruito e nessun elemento FROZEN è stato modificato.
