# HANDOFF — CHAT 3.8 CURRENT URBAN PLANNING v01

**Chat:** 3.8 — Acquisizione e validazione urbanistica corrente FVG
**Data chiusura:** 2026-09-19
**Stato attività:** COMPLETED / TECHNICAL PASS
**PHASE_4_READINESS:** NOT_READY
**ISS-0010:** OPEN
**Branch:** `chat-3.8-current-urban-planning`
**Commit implementazione:** `558e0233615f052966fe830ed28ff97474c71b3f`

## 1. Obiettivo

Eseguire il mandato `DISPATCH_CHAT_3.8_CURRENT_URBAN_PLANNING_ACQUISITION_v01.md`
secondo DEC-0032 e DEC-0044, costruendo una coverage urbanistica current-first
per tutti i Comuni FVG senza costruire candidati Hub né modificare baseline FROZEN.

## 2. Lavoro svolto

- lette integralmente baseline Fase 1/Fase 2 e artifact Fase 3 indicati nel dispatch;
- verificati live PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER;
- verificati DEC-0032, DEC-0044 e ISS-0010;
- censito il catalogo ufficiale IRDAT per i PRGC comunali;
- riconciliati 151 record PRGC IRDAT con il perimetro dei 215 Comuni correnti;
- confrontati i record con il campione comunale frozen della precedente validazione;
- acquisite quattro geometrie vettoriali con allineamento alla variante corrente verificato;
- raccolte 24 fonti comunali supplementari per casi senza record IRDAT;
- materializzate con hash 21 delle 24 fonti supplementari;
- mantenuti espliciti i casi non chiusi senza usare CER 2018 come sostituto corrente;
- eseguito QA strutturale dei vettori e verifica completa del manifest;
- aggiornati DATA_REGISTRY e ISS-0010 nel PROJECT_CONTROL_REGISTER.

## 3. Risultato quantitativo

Coverage finale: **215/215 Comuni**, 215 codici ISTAT univoci.

| Stato | N |
|---|---:|
| CURRENT_VECTOR_VERIFIED | 4 |
| CURRENT_PLAN_VERIFIED_NO_VECTOR | 1 |
| CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE | 167 |
| TO_VERIFY | 43 |
| Totale | 215 |

Nessun Comune ha stato vuoto.
Nessun layer CER 2018 è stato promosso a geometria corrente.

## 4. Vettori correnti verificati

- Tavagnacco — Variante 22 — IRDAT 12217.
- Gorizia — Variante 61 — IRDAT 12238.
- Monfalcone — Variante 71 — IRDAT 12239.
- San Canzian d'Isonzo — Variante 29 — IRDAT 12194.

QA: 4/4 ZIP integri; ogni SHP possiede DBF e SHX.
Tavagnacco e San Canzian d'Isonzo includono PRJ.
Gorizia e Monfalcone non includono PRJ: CRS `RDN2008-TM33NE`
derivato dai metadata IRDAT e limite registrato esplicitamente.

## 5. Decisioni / proposte emerse

Nessuna nuova decisione metodologica è stata assunta autonomamente.

Conferme operative, non nuove decisioni:

- IRDAT/Eagle può fornire accesso e distribuzione, ma non dimostra da solo la vigenza;
- CER D/H 2018 resta storico/supporto;
- un caso privo di currentness verificata resta incompleto o `TO_VERIFY`;
- non è legittimo costruire una mosaicatura region-wide "best effort" usando fallback storici.

**Proposta alla Chat Madre:** mantenere ISS-0010 OPEN e non avviare Fase 4
finché i gap residui possono alterare l'universo poligonale.

## 6. File creati — repository locale

### Documentazione / dati leggeri

- `docs/FASE_3_CURRENT_URBAN_PLANNING_VALIDATION_REVIEW_v01.md`
- `docs/FASE_3_CURRENT_URBAN_PLANNING_COVERAGE_v01.csv`
- `docs/FASE_3_CURRENT_URBAN_PLANNING_EVIDENCE_v01.json`
- `docs/FASE_3_CURRENT_URBAN_PLANNING_SOURCE_SUPPLEMENT_v01.csv`
- `docs/FASE_3_CURRENT_URBAN_PLANNING_VECTOR_QA_v01.csv`
- `docs/HANDOFF_CHAT_3.8_CURRENT_URBAN_PLANNING_v01.md`

### Codice

- `scripts/acquire_validate_current_urban_planning_chat3_8_v01.py`
- `scripts/run_current_urban_planning_chat3_8_v01.py`
- `scripts/apply_current_urban_planning_source_supplement_v01.py`
- `scripts/qa_current_urban_planning_vectors_v01.py`

## 7. Output pesanti / evidenze raw

Root OneDrive:

`5_HUB_FVG\02_external_sources\F3_CHAT_3_8\`

Contenuti principali:

- `irdat_catalog\` — 19 blocchi raw del catalogo IRDAT;
- `municipalities\` — detail IRDAT e quattro pacchetti vettoriali verificati;
- `supplement_sources\` — fonti comunali materializzate;
- `source_manifest_v01.json`.

Manifest:
- artifact registrati: 51;
- SHA-256 manifest: `3F8422B29F85B1C5FE9B9D2DCEB1FC7A05119A5FAD88B574FC09655479378482`;
- size: 25.007 byte;
- preservation check: **PASS**;
- file mancanti: 0;
- mismatch SHA-256: 0.

## 8. Controlli ed esito

- coverage 215/215: PASS;
- unicità codice ISTAT: PASS;
- stato esplicito 215/215: PASS;
- CER non promosso a corrente: PASS;
- QA ZIP / SHP+DBF+SHX: PASS 4/4;
- CRS: PASS con limitazione documentata per 2 pacchetti senza PRJ;
- manifest/hash/preservation: PASS;
- `py_compile` dei quattro script: PASS;
- `git diff --check`: PASS;
- Fase 1 e Fase 2 FROZEN non modificate: PASS;
- nessun output CANDIDATES/ADMISSIBLE: PASS;
- PROJECT_CONTROL_REGISTER aggiornato: PASS.

**TECHNICAL_QUALITY_GATE = PASS.**

## 9. PHASE_4_READINESS

**NOT_READY.**

Motivo: 43 Comuni restano `TO_VERIFY`, 167 hanno lineage incompleto,
e Grado ha piano corrente verificato ma nessun vettore corrente acquisito.
Questi gap possono alterare l'universo poligonale della futura Fase 4.

La Chat 3.8 non autorizza né costruisce alcun universo candidati.

## 10. Governance aggiornata

PROJECT_CONTROL_REGISTER:

- DATA_REGISTRY: aggiunto `F3_SRC_FVG_PRGC_CURRENT_001`, stato `REVIEW`;
- ISSUES: aggiornata la prossima azione di `ISS-0010`;
- `ISS-0010` mantenuta `OPEN`.

PROJECT_SOURCE_OF_TRUTH:
- nessuna modifica;
- nessuna nuova decisione metodologica sostanziale introdotta.

## 11. SESSION CLOSE

Procedura applicata da `TESI_RECORDKEEPING_PROTOCOL_V1.md`,
adattando il registro al sistema di governance ufficiale del progetto 5 HUB.

- `NOTEBOOK_CHANGE = NO`
- `REGISTER_CHANGE = YES`
- `GIT_COMMIT_REQUIRED = YES`
- Artifact check: PASS
- Preservation verification: PASS
- Notebook/build: N/A — nessun notebook autorevole del progetto 5 HUB modificato
- FROZEN overwrite: NO
- Commit implementazione: `558e0233615f052966fe830ed28ff97474c71b3f`

## 12. Problemi aperti

1. Chiudere i 43 casi `TO_VERIFY` con fonte comunale/BUR corrente.
2. Per i 167 lineage incompleti verificare l'ultima variante efficace
   e l'allineamento della geometria distribuita.
3. Acquisire geometria vettoriale ufficiale corrente per Grado oppure
   documentare formalmente un percorso alternativo approvato.
4. Conservare il warning CRS sui due ZIP senza PRJ.
5. Verificare condizioni di riuso delle singole fonti comunali se saranno redistribuite.

## 13. Prossimo passo raccomandato

La Chat Madre deve:

1. revieware `FASE_3_CURRENT_URBAN_PLANNING_VALIDATION_REVIEW_v01.md`;
2. prendere atto di `PHASE_4_READINESS = NOT_READY`;
3. mantenere o ridefinire ISS-0010;
4. aprire un mandato mirato per la chiusura dei gap residui
   prima di autorizzare la costruzione dell'universo poligonale di Fase 4.

**Stato finale Chat 3.8: CLOSED OPERATIVAMENTE / PASS TECNICO / PHASE 4 NOT READY.**
