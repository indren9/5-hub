# DISPATCH — Chat 3.11 — Baseline idrogeologica corrente PGRA + PAI

**Fase:** 3 — Inventario e validazione dei dati  
**Data:** 2026-09-20  
**Stato mandato:** AUTHORIZED  
**Regia:** Chat 0.2 — Chat Madre 5 HUB  
**Issue principali:** ISS-0006, ISS-0012  
**Decisioni vincolanti:** DEC-0039, DEC-0040

## 1. Obiettivo

Chiudere, per quanto ragionevolmente necessario alla pianificazione macro dei 5 HUB, i due gap residui relativi a:

1. **PGRA corrente** — pericolosità/rischio idraulico e relativo lineage/versionamento;
2. **PAI corrente** — pericolosità da frana e altre eventuali aree/zone di attenzione rilevanti per l'applicazione della disciplina vigente.

Il lavoro è di **baseline dati e disciplina corrente**, non di scoring e non di progettazione geotecnica/idraulica.

La Chat 3.11 deve stabilire quali fonti GIS e normative correnti sono sufficientemente affidabili, riproducibili e tracciabili per alimentare in seguito lo screening dei candidati.

## 2. Baseline vincolanti da leggere

Repository 5 HUB:
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md`
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md`
- `docs/FASE_3_TERRITORIAL_ENVIRONMENTAL_VALIDATION_REVIEW_v01.md`
- `docs/FASE_3_TERRITORIAL_CONSTRAINT_ROLE_MATRIX_v01.csv`
- `docs/HANDOFF_CHAT_3.4_TERRITORIAL_CONSTRAINTS_v01.md`

Governance viva:
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER;
- DEC-0039;
- DEC-0040;
- ISS-0006;
- ISS-0012;
- DATA_REGISTRY, in particolare `F3_SRC_PGRA_001` e `F3_SRC_FVG_LANDSLIDE_001`.

F1/F2 e le decisioni metodologiche già ACCEPTED non devono essere riaperte.
## 3. Regole metodologiche già approvate

### 3.1 PGRA — DEC-0039

La presenza di pericolosità/allagabilità:
- NON produce automaticamente esclusione;
- produce esclusione solo quando la disciplina vigente rende l'intervento incompatibile/non ammissibile oppure emerge incompatibilità tecnica non ragionevolmente mitigabile;
- negli altri casi resta fattore negativo da trattare nelle fasi successive.

Per la geometria:
1. cercare prima un binding forte tra servizio GIS e versione/atto vigente;
2. se tale binding non è reperibile dopo ricerca documentata adeguata, è ammesso usare il **WFS ufficiale live** come geometria operativa con caveat e lineage espliciti.

La Chat 3.11 NON deve inventare una nuova regola PGRA.

### 3.2 Frane / PAI — DEC-0040

Il riferimento principale è il **PAI vigente completo** e la relativa disciplina.

Catasto Frane e perimetri inventariali:
- sono supporto conoscitivo;
- NON equivalgono automaticamente al PAI;
- NON producono automaticamente esclusioni o punteggi.

La Chat 3.11 deve quindi verificare quale cartografia PAI vigente sia applicabile al territorio FVG e come materializzarla in modo riproducibile.
## 4. Stato di partenza PGRA

La Chat 3.4 ha già verificato:
- Autorità di Bacino Distrettuale delle Alpi Orientali / SIGMA;
- Delibera n. 12 del 18-12-2025;
- efficacia del quadro aggiornato dal 22-01-2026;
- catalogo SIGMA corrente: set id 40, codice `PGRA2027`, in salvaguardia;
- precedente `PGRA2021` marcato superato;
- WFS live ufficiale:
  `https://sigma.distrettoalpiorientali.it/sigma/geo/sigma/wfs`;
- layer:
  - `sigma:Pericolo_direttiva_alluvioni`;
  - `sigma:Rischio`;
- CRS nativo dichiarato: EPSG:3035.

Gap:
il WFS live non esponeva un identificatore machine-readable che collegasse direttamente le feature alla Delibera 12/2025 / set PGRA2027.

La Chat 3.11 NON deve ripetere indiscriminatamente il lavoro già svolto. Deve cercare in modo mirato:
- metadati ufficiali;
- capabilities/configurazioni;
- cataloghi;
- documentazione SIGMA;
- atti e allegati;
- eventuali download/versioni GIS ufficiali;
- eventuale evidenza indiretta ma robusta di currentness.

Se il binding forte non esiste o non è pubblicamente verificabile, applicare il fallback già previsto da DEC-0039 e documentare precisamente perché.
## 5. Stato di partenza frane / PAI

La Chat 3.4 ha già verificato il layer regionale:

`IRDAT:CATFRANE_PERICOLOSITA`

con:
- 830 geometrie;
- CRS EPSG:3004;
- classi osservate P1-P4.

Ha inoltre distinto:
- pericolosità;
- `CATFRANE_PERIMFRANE`;
- Catasto Frane complessivo.

Questi dati NON sono stati dimostrati equivalenti al **PAI vigente completo**.

ISS-0012 richiede:
- identificare il corpus PAI corrente applicabile al FVG;
- acquisire/validare la cartografia vigente utile alle frane;
- includere, se previste e pertinenti, aree/zone di attenzione o categorie assimilabili;
- acquisire le Norme di Attuazione o disciplina ufficiale necessaria a interpretare correttamente i layer;
- documentare relazione e differenze rispetto ai layer regionali CATFRANE.

Non assumere a priori che un singolo layer regionale sia equivalente al PAI.
## 6. Attività richieste

### A. PGRA
1. verificare nuovamente lo stato corrente delle fonti ufficiali al 2026-09-20;
2. cercare un binding documentabile tra geometria GIS e quadro PGRA corrente;
3. se trovato, documentarlo e materializzare la baseline corrente;
4. se non trovato dopo ricerca adeguata:
   - documentare le evidenze negative;
   - applicare DEC-0039;
   - proporre il WFS ufficiale live come `CURRENT_OFFICIAL_LIVE_GEOMETRY_WITH_VERSION_CAVEAT`;
5. materializzare solo ciò che serve alla riproducibilità del 5 HUB;
6. registrare schema, CRS, conteggi, timestamp, query/procedura e SHA-256.

### B. PAI / frane
1. identificare fonte e versione/atto vigente;
2. verificare l'ambito territoriale pertinente al FVG;
3. acquisire la cartografia ufficiale corrente;
4. distinguere chiaramente:
   - pericolosità PAI;
   - rischio, se pertinente;
   - aree/zone di attenzione;
   - inventario/catasto;
5. acquisire e citare la disciplina ufficiale pertinente;
6. materializzare la baseline GIS corrente con lineage e hash;
7. confrontare il PAI con `CATFRANE_PERICOLOSITA` solo per capire relazione/copertura, non per sostituire il PAI.

### C. Governance
Per ciascuna issue concludere con una proposta:
- `KEEP_OPEN`;
- `READY_WITH_LIMITATIONS`;
- `PROPOSE_RESOLVED`;
- `PROPOSE_RESOLVED_PROCEDURALLY`.
## 7. Vincoli

NON:
- modificare DEC-0039 o DEC-0040;
- introdurre punteggi;
- definire pesi;
- stabilire soglie quantitative nuove;
- applicare esclusioni automatiche alle sole classi P1-P4 o PGRA;
- dichiarare edificabilità/non edificabilità senza supporto della disciplina applicabile;
- fare modellazione idraulica;
- fare analisi geotecnica;
- produrre nuove mappe di pericolosità;
- usare il Catasto Frane come sostituto implicito del PAI;
- nascondere un gap di versione con un'assunzione;
- aprire la Fase 4.

## 8. Principio di proporzionalità

Il 5 HUB è una pianificazione macro.

La Chat 3.11 deve cercare un livello di evidenza sufficiente per:
- screening regionale;
- identificazione di casi che richiedono approfondimento;
- futura verifica puntuale dei finalisti.

Non serve trasformare la Fase 3 in uno studio idraulico o geologico di dettaglio.

Se una lacuna non è materialmente risolvibile con fonti pubbliche correnti, documentarla e valutare il fallback già approvato invece di continuare indefinitamente la ricerca.
## 9. Storage e riproducibilità

Repository locale:
`C:\dev\5-hub`

Storage pesante:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_11\`

Branch:
`chat-3.11-pgra-pai-current-baseline`

Usare Git solo per:
- script;
- configurazioni;
- manifest leggeri;
- report;
- tabelle di controllo.

Dati GIS pesanti e documenti sorgente voluminosi vanno su OneDrive.

Ogni file sorgente materializzato deve avere:
- URL/fonte;
- data/ora acquisizione;
- ruolo;
- versione/atto quando disponibile;
- SHA-256;
- eventuale licenza/condizioni note.

## 10. Output richiesti

Repository:
- `docs/FASE_3_PGRA_PAI_CURRENT_BASELINE_VALIDATION_REVIEW_v01.md`
- `docs/FASE_3_PGRA_PAI_SOURCE_MATRIX_v01.csv`
- `docs/HANDOFF_CHAT_3.11_PGRA_PAI_v01.md`
- script leggeri di acquisizione/QA se necessari.

OneDrive:
- raw/download ufficiali;
- eventuali GeoJSON/GPKG materializzati;
- Norme/atti ufficiali;
- `source_manifest_v01.json`;
- QA evidence.

## 11. Quality gate

PASS tecnico solo se:

### PGRA
- stato corrente verificato;
- fonte ufficiale identificata;
- ricerca del binding versione documentata;
- baseline geometrica operativa scelta secondo DEC-0039;
- caveat esplicito se si usa WFS live senza binding forte;
- procedura riproducibile;
- conteggi/schema/CRS/hash verificati.

### PAI
- corpus vigente applicabile identificato;
- disciplina ufficiale acquisita;
- geometria corrente verificata/materializzata oppure gap residuo dimostrato;
- rapporto PAI ↔ CATFRANE documentato;
- nessuna equivalenza inventata;
- procedura riproducibile;
- conteggi/schema/CRS/hash verificati.

### Generale
- DATA_REGISTRY aggiornato;
- ISS-0006 e ISS-0012 aggiornate ma NON chiuse autonomamente;
- artifact completi;
- `git diff --check` PASS;
- branch pulito;
- handoff completo.

## 12. Criterio di successo

La Chat Madre deve poter rispondere in modo semplice a due domande:

> Qual è la migliore geometria ufficiale corrente da usare per lo screening PGRA regionale, con quale livello di certezza sul versionamento?

> Qual è la baseline PAI vigente da usare per lo screening delle frane, e quale ruolo resta ai layer CATFRANE regionali?

La Chat 3.11 si ferma dopo il quality gate. La review e l'eventuale chiusura di ISS-0006 / ISS-0012 competono alla Chat 0.2 / utente.
