# HANDOFF — Chat 3.4 — Vincoli territoriali, ambientali e paesaggistici

**Data:** 2026-09-19
**Stato finale proposto:** TECHNICAL_PASS_PROPOSED / REVIEW
**Stato FASE 3:** IN CORSO — NON CLOSED, NON FROZEN
**Regia metodologica:** Chat Madre 5 HUB
**Branch Git:** chat-3.4-territorial-constraints

## 1. Obiettivo

Validare e, quando tecnicamente sostenibile, materializzare le fonti correnti relative a:
- PGRA / rischio e pericolosità idraulica;
- frane e pericolosità geologica;
- Natura 2000;
- parchi, riserve, biotopi, prati stabili e altre tutele pertinenti;
- Piano Paesaggistico Regionale vigente.

Il mandato non autorizzava costruzione di candidati, overlay, buffer, soglie arbitrarie,
pesi, punteggi o regole autonome di esclusione.

## 2. Baseline e governance rispettate

Letti e applicati:
- docs/DISPATCH_CHAT_3.4_TERRITORIAL_ENVIRONMENTAL_CONSTRAINTS_v01.md;
- docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md — FROZEN;
- docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md — FROZEN;
- docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md;
- docs/ROADMAP_METODOLOGICA_v1.md;
- PROJECT_SOURCE_OF_TRUTH vivo;
- PROJECT_CONTROL_REGISTER vivo.
Nessuna baseline FROZEN è stata modificata.
La baseline Claude/QGIS non è stata usata come fonte autorevole corrente.

## 3. Esiti principali

### 3.1 PGRA
- fonte: Autorità di Bacino Distrettuale delle Alpi Orientali / SIGMA;
- aggiornamento adottato con Delibera n. 12 del 18-12-2025;
- quadro aggiornato efficace dal 22-01-2026;
- catalogo SIGMA corrente: set id 40, codice PGRA2027, in salvaguardia;
- WFS live di pericolosità e rischio verificato, CRS nativo EPSG:3035;
- schema, hits e campioni materializzati;
- geometria bulk WFS non promossa a baseline corrente perché il servizio non espone
  un binding machine-readable esplicito alla Delibera 12/2025 / set PGRA2027.

**ISS-0006 resta OPEN.**

### 3.2 Frane
- IRDAT:CATFRANE_PERICOLOSITA: 830 geometrie, EPSG:3004;
- classi: P1=2, P2=39, P3=349, P4=440;
- IRDAT:CATFRANE_PERIMFRANE: 4.989 geometrie;
- Catasto complessivo regionale descritto dall'ente come circa 6.500 fenomeni;
- pericolosità, perimetro inventariale e fenomeno censito sono oggetti distinti.

Nessuna classe P1–P4 è stata trasformata in esclusione.
### 3.3 Natura 2000 e aree protette
- SITI_PROT:SIC: 66 feature; typename tecnico/legacy, attributi ZSC/SIC/pSIC;
- SITI_PROT:ZPS: 35 feature;
- 72 codici sito unici; 29 codici condivisi fra i due layer;
- parchi regionali=2; riserve regionali=13; aree protette statali=3;
- parchi comunali/intercomunali=18;
- prati stabili=10.486, di cui 8.097 con PRATO_TUTELATO=Sì.

Biotopi:
- WFS = 40 geometrie;
- il testo riepilogativo regionale continua a dichiarare 40;
- la tabella della stessa pagina e gli atti vigenti includono anche n. 41 e n. 42;
- DPReg 065/2026 e 066/2026, con Allegato 2 cartografico, sono stati preservati;
- corpus legale corrente = 42 biotopi;
- nessuna digitizzazione manuale è stata eseguita.

**ISS-0011 resta OPEN** per il disallineamento e la mancanza dei due vettori aggiornati.

### 3.4 PPR
- PPR originario efficace dal 10-05-2018;
- Variante 1 efficace dal 06-04-2023;
- Variante 2: D.P.Reg. 0133/Pres del 12-12-2025, efficace dal 18-12-2025;
- WFS PPR corrente verificato, CRS EPSG:6708;
- v_aggiornamenti_ppr: 67 feature, di cui 53 con numero_variante=2/2025;
- subset pertinente materializzato con schema, count, geometria e SHA-256.

**ISS-0008 = REVIEW**: procedura riproducibile completata, risoluzione demandata alla Chat Madre.
## 4. Materializzazioni e lineage

Script riproducibile:
scripts/acquire_validate_territorial_constraints_chat3_4_v01.py

Comando:
python scripts\acquire_validate_territorial_constraints_chat3_4_v01.py

Raw/source:
C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_4\

QA:
C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\05_intermediate_outputs\F3_CHAT_3_4\

Manifest:
source_manifest_v01.json
SHA-256:
B3FA6C361B8B8EC269C03B6A8304EF6C9F23785C45387BFF5ACBC9474DA3FB5B

QA:
TERRITORIAL_CONSTRAINTS_QA_v01.json
SHA-256:
705C1D7EEE62241041220965169711EA13F4F901AD7FE7C75F75628EBA0C4A8D

Audit indipendente finale:
- artifact nel manifest: 78;
- mismatch SHA-256: 0;
- ZIP PPR verificati: 15, errori: 0;
- PDF legali biotopi verificati: 4, magic %PDF errate: 0;
- QA automatico: technical_checks_pass=true.
## 5. Artifact Git

Commit implementazione/review:
f32f640159198870d408d332d5a92cc8f73dc0d5
— feat(fase3): validate territorial environmental constraints

Contenuto:
- docs/FASE_3_TERRITORIAL_ENVIRONMENTAL_VALIDATION_REVIEW_v01.md;
- docs/FASE_3_TERRITORIAL_CONSTRAINT_ROLE_MATRIX_v01.csv;
- docs/FASE_3_TERRITORIAL_VALIDATION_EVIDENCE_v01.json;
- scripts/acquire_validate_territorial_constraints_chat3_4_v01.py.

Questo handoff viene aggiunto con commit di chiusura separato.

## 6. Governance aggiornata

PROJECT_CONTROL_REGISTER — DATA_REGISTRY:
- F3_SRC_PGRA_001 = REVIEW;
- F3_SRC_PPR_001 = REVIEW;
- F3_SRC_FVG_LANDSLIDE_001 = REVIEW;
- F3_SRC_FVG_NATURA_001 = REVIEW.

PROJECT_CONTROL_REGISTER — ISSUES:
- ISS-0006 = OPEN;
- ISS-0008 = REVIEW;
- ISS-0011 = OPEN.

Readback post-write: PASS.
PROJECT_SOURCE_OF_TRUTH: non modificato.
DECISIONS: nessuna nuova decisione metodologica registrata.
## 7. Questioni metodologiche da sottoporre alla Chat Madre / utente

- **Q-METH-3.4-A — PGRA:** geometria operativa, pericolosità/rischio/aree allagabili,
  classi e accettabilità del WFS live senza binding versione esplicito.
- **Q-METH-3.4-B — Frane:** gerarchia fra pericolosità, PAI vigente, perimetri e fenomeni;
  eventuale ruolo delle classi P1–P4.
- **Q-METH-3.4-C — Natura 2000:** esclusione modellistica oppure verifica di
  ammissibilità/VINCA sito-specifica.
- **Q-METH-3.4-D — Parchi/riserve/biotopi/prati:** disciplina per categoria,
  perimetri provvisori, prati tutelati e gestione biotopi 41–42.
- **Q-METH-3.4-E — PPR:** matrice prescrizione → ruolo modellistico per art. 136,
  art. 142, ulteriori contesti, componenti informative e atti specifici.

Tutte restano PROPOSED / TO_DECIDE. Nessuna esclusione automatica è stata approvata.

## 8. Quality gate

PASS:
- fonte/stato corrente PGRA verificati;
- impossibilità di promuovere il vettore PGRA documentata riproducibilmente;
- frane: semantica/copertura chiarite;
- Natura 2000: nomenclatura e geometrie validate;
- parchi/riserve principali validate;
- PPR post Variante 2 e procedura GIS riproducibile validate;
- hash e lineage completi;
- role matrix prodotta;
- registri aggiornati e riletti;
- F1/F2 FROZEN non modificate;
- Git contiene solo codice/documentazione leggera pertinente.
GAP DOCUMENTATI, non mascherati:
- binding normativo/versione dei vettori PGRA;
- copertura vettoriale dei biotopi 41–42.

## 9. SESSION CLOSE — change-driven

**NOTEBOOK_CHANGE = NO**
Il notebook legacy non è Source of Truth del progetto 5 HUB.

**REGISTER_CHANGE = YES**
Aggiornati DATA_REGISTRY e ISSUES con soli esiti tecnici; nessuna decisione metodologica
è stata promossa ad ACCEPTED/FROZEN.

**PROJECT_SOURCE_OF_TRUTH_CHANGE = NO**
Il consolidamento autorevole compete alla Chat Madre/utente dopo review.

**GIT_COMMIT_REQUIRED = YES**
Review, matrice, evidence JSON, script e handoff sono artifact leggeri versionabili.

Artifact preservation:
- raw e output pesanti restano su OneDrive;
- manifest/hash verificati;
- nessun artifact FROZEN modificato;
- nessun candidato o overlay prodotto.

Build notebook: N/A.

## 10. Stato finale e prossimo passo

**Chat 3.4 = TECHNICAL_PASS_PROPOSED / REVIEW.**

La Chat Madre deve:
1. eseguire review indipendente degli artifact e del commit operativo;
2. decidere se ISS-0008 può diventare RESOLVED;
3. mantenere ISS-0006 e ISS-0011 aperti finché i gap indicati non sono risolti
   o formalmente accettati;
4. sottoporre Q-METH-3.4-A…E all'utente prima di trasformare le tutele in regole operative;
5. non aprire implicitamente Fase 4 sulla base di questo PASS tecnico.
