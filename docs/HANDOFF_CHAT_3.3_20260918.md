# HANDOFF — Chat 3.3 — Rete stradale, accessi e TEN-T

**Data:** 2026-09-18
**Stato finale Chat 3.3:** PASS tecnico-operativo
**Stato FASE 3:** IN CORSO — NON CLOSED, NON FROZEN
**Regia:** Chat Madre 5 HUB
**Branch Git dedicato:** chat-3.3-road-tent

## 1. Obiettivo

Validare o delimitare con evidenza ISS-0004 e ISS-0005:
- idoneità del Grafo stradale FVG al routing Light/Heavy;
- TEN-T corrente a tre livelli;
- futura lineage degli accessi, road anchor, connector e uscite TEN-T;
- senza costruire candidati o accessi reali.

## 2. Baseline e governance rispettate

Letti integralmente e applicati:
- docs/DISPATCH_CHAT_3.3_ROAD_TENT_VALIDATION_v01.md;
- docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md — FROZEN;
- docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md — FROZEN;
- docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md;
- PROJECT_SOURCE_OF_TRUTH vivo su Google Drive;
- PROJECT_CONTROL_REGISTER vivo, con verifica di DATA_REGISTRY e ISSUES.

La baseline Claude/QGIS è stata usata solo come riferimento storico. Le 23 uscite TEN-T storiche non sono state riutilizzate come fonte autorevole.

## 3. Lavoro svolto

### 3.1 Grafo stradale

È stato materializzato e auditato l’intero WFS regionale:
- 75.546 feature;
- 75.546 LineString valide;
- nessuna geometria vuota o a lunghezza zero;
- snapshot SHA-256 81BFD7E97300F12230324440C40A7944DAB7075EC2EA2CC5FCB9AE6201C72B8E.

Audit topologico:
- 59.945 nodi endpoint;
- 21 componenti;
- componente gigante con 99,9418% degli archi;
- 2.935 dangling;
- 9 archi isolati;
- 1.064 intersezioni geometriche candidate non nodate, da non correggere automaticamente perché una parte può essere separata in quota.

Sanity check non orientato:
- sette probe territoriali;
- tutte le coppie raggiungibili;
- risultati usati esclusivamente come controllo di connettività, non come output del modello.

### 3.2 Direzionalità Light

Risultato critico:
- DIR non è un flag one-way; è prevalentemente nd o una direzione/destinazione nominale;
- TRIM_USAGE_ALLOWANCE assume 0/1/2/NULL ma la semantica non è stata trovata in forma pubblica affidabile;
- A4 e A28 hanno allowance NULL su tutte le feature esaminate; A34 quasi completamente NULL;
- GEOMETRY_REVERSED non è prova autonoma della legalità di percorrenza.

Conclusione:
- grafo idoneo come base geometrica e screening non orientato;
- routing Light diretto/legalmente percorribile NON VALIDATO.

### 3.3 Heavy

Il grafo statico non contiene un set sufficiente di restrizioni Heavy.

Sono state verificate evidenze ufficiali di limitazioni reali variabili per massa/dimensione/periodo su strade FVG, non ricostruibili dal solo grafo.

Conclusione:
- routing Heavy di produzione NON IDONEO con il solo F3_SRC_FVG_ROADGRAPH_001;
- serve una futura sovrapposizione di restrizioni strutturali e ordinanze dei gestori.

### 3.4 TEN-T

Sono state materializzate e verificate fonti correnti DG MOVE 2024:
- Annex I con roads core / extended core / comprehensive;
- Annex II con nodi TEN-T;
- European Transport Corridors 2024.

Il servizio tentec_public_services_ext è stato confermato come legacy a due livelli core/comprehensive e non viene promosso a baseline corrente.

Il servizio dei corridoi 2024 corrobora tratti core FVG, con crosswalk tecnico verso il grafo regionale, ma non chiude il crosswalk completo route-level a tre livelli.

Sono stati identificati nell’Annex II gli elementi FVG rilevanti, inclusi Monfalcone, Pordenone, Porto Nogaro, Trieste e Udine.

### 3.5 Uscite e accessi futuri

Non sono stati costruiti accessi reali né un nuovo exit set.

È stata definita la lineage minima futura per:
- access_point;
- road_anchor;
- connector;
- TENT_EXIT_SET_v01.

È stata proposta alla regia:
Q-METH-3.3-A — definizione operativa di nearest TEN-T road exit sui tratti TEN-T non a accesso controllato / con intersezioni a raso.

Nessuna soglia di snap è stata fissata.

## 4. Disposizione degli issue

### ISS-0004

**Resta OPEN.**

È però delimitato con evidenza:
- Light non orientato: tecnicamente utilizzabile per screening;
- Light diretto: NON VALIDATO;
- Heavy: NON IDONEO con il solo grafo.

Prossima azione registrata:
validare una semantica one-way documentata, integrare restrizioni Heavy e non applicare noding cieco agli incroci geometrici.

### ISS-0005

**Resta OPEN.**

È però delimitato con evidenza:
- tassonomia corrente a tre livelli verificata;
- Annex I/II materializzati e hashati;
- legacy REST a due livelli separato;
- tratti core dei corridoi corroborati;
- 23 uscite storiche escluse;
- lineage futura exit set definita.

Residuo:
- crosswalk route-level completo a tre livelli;
- Q-METH-3.3-A;
- futura costruzione TENT_EXIT_SET_v01.

## 5. File creati / modificati

### Git — documentazione e codice leggero

- docs/FASE_3_ROAD_TENT_VALIDATION_REVIEW_v01.md
- scripts/audit_roadgraph_chat3_3_v01.py
- scripts/audit_roadgraph_intersections_chat3_3_v01.py
- scripts/audit_roadgraph_reachability_chat3_3_v01.py
- scripts/crosswalk_tentec_corridor_fvg_chat3_3_v01.py
- docs/HANDOFF_CHAT_3.3_20260918.md

### OneDrive — dati pesanti / evidenze

Root principale:
C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG

Raw:
- 01_raw_data\F3_CHAT_3_3\GRAFO_STRADALE_FVG_WFS_20260918.geojson

Output:
- 05_intermediate_outputs\F3_CHAT_3_3\ROADGRAPH_AUDIT_METRICS_v01.json
- 05_intermediate_outputs\F3_CHAT_3_3\ROADGRAPH_INTERSECTION_AUDIT_v01.json
- 05_intermediate_outputs\F3_CHAT_3_3\ROADGRAPH_NONNODED_INTERSECTION_EXAMPLES_v01.csv
- 05_intermediate_outputs\F3_CHAT_3_3\ROADGRAPH_REACHABILITY_TEST_v01.json
- 05_intermediate_outputs\F3_CHAT_3_3\TENTEC_CORRIDOR_TO_FVG_ROAD_CROSSWALK_v01.csv

TEN-T external sources:
- 02_external_sources\F3_CHAT_3_3\TEN_T\Annex1_listing8_HRITMTSI_2024.pdf
- 02_external_sources\F3_CHAT_3_3\TEN_T\TEN-T-guidelines-2024-annex-2.pdf
- metadata REST e subset stradali corridoi/legacy nella stessa cartella.

## 6. Hash principali

- raw road graph: 81BFD7E97300F12230324440C40A7944DAB7075EC2EA2CC5FCB9AE6201C72B8E
- ROADGRAPH_AUDIT_METRICS_v01.json: 324DBD888F4122425D6A2A449D7C67C8A90E712979EE04C25700099A481F01C0
- ROADGRAPH_INTERSECTION_AUDIT_v01.json: 6E9E341818D9088D04BA78E438BFC04DF23B56F5C88408935B2B0D936EA71E5A
- ROADGRAPH_NONNODED_INTERSECTION_EXAMPLES_v01.csv: 8D00DFB6DE92E6D89E63651D1ED92BA44B24F13758F4664CF5290577812DB2A1
- ROADGRAPH_REACHABILITY_TEST_v01.json: F808B3F4B1021E63DA7F89A1C35AC76DB3D7E2358E0C3479C08F46335CC2B517
- TENTEC_CORRIDOR_TO_FVG_ROAD_CROSSWALK_v01.csv: D85E45FBDDA39D76D2513546E395EEA5688AE8056EFB25FDCB33104A9DE4392B
- Annex I TEN-T 2024: 6C0CD7607C071B15968D8C75213067176F0D78457E80927078469716DC233556
- Annex II TEN-T 2024: CC33C50BC6D2A96A3CEDB5E47DAB582B8564760DE8479867BBB788BC8DBC7E65

## 7. Governance aggiornata

PROJECT_CONTROL_REGISTER è stato aggiornato in-place su Google Sheets.

DATA_REGISTRY:
- F3_SRC_FVG_ROADGRAPH_001 -> REVIEW, con esito Light/Heavy e hash snapshot;
- F3_SRC_TENTEC_001 -> REVIEW, con materializzazione corrente, mismatch legacy e gap residuo.

ISSUES:
- ISS-0004 resta OPEN, prossima azione aggiornata;
- ISS-0005 resta OPEN, prossima azione aggiornata.

PROJECT_SOURCE_OF_TRUTH:
- non modificato dalla Chat 3.3;
- eventuale consolidamento autorevole compete alla Chat Madre dopo review.

Nessuna decisione sostanziale è stata registrata come ACCEPTED o FROZEN.

## 8. Controlli

- lettura integrale dispatch: PASS;
- lettura baseline F1/F2 FROZEN: PASS;
- verifica review Chat 3.1: PASS;
- verifica governance viva: PASS;
- materializzazione WFS completa: PASS;
- hash raw/output: PASS;
- validità geometrica: PASS;
- audit topologico: PASS;
- intersection audit: PASS;
- sanity reachability: PASS;
- semantica one-way sufficiente per routing diretto: FAIL / gap esplicito;
- copertura Heavy: FAIL / gap esplicito;
- TEN-T 3-tier corrente documentata: PASS;
- REST legacy separato dalla baseline corrente: PASS;
- exit lineage definita senza generazione di exit reali: PASS;
- py_compile dei quattro script: PASS;
- git diff --cached --check sul commit operativo: PASS;
- nessun artifact FROZEN sovrascritto: PASS.

## 9. Git e concorrenza

Durante il lavoro il working tree C:\dev\5-hub è stato occupato dalla branch parallela chat-3.2-urban-planning con file della Chat 3.2 già presenti/staged.

Per evitare contaminazione:
- non sono stati toccati né committati file Chat 3.2;
- è stato creato il worktree separato C:\dev\5-hub-chat3.3;
- branch dedicata: chat-3.3-road-tent;
- base: main = bb29552e4a80ec6da78cdba0bb61bbcd15b70f28.

Commit operativo Chat 3.3:
66f9c7dd87333832d9a41a8dae5b0e4103b2e807
feat(fase3): audit road routing and TEN-T lineage

L’integrazione su main compete alla regia dopo verifica degli handoff paralleli.

## 10. SESSION CLOSE — change-driven

NOTEBOOK_CHANGE = NO

Motivo: il notebook legacy non è fonte autorevole del progetto 5 HUB.

REGISTER_CHANGE = YES

Motivo: DATA_REGISTRY e ISSUES hanno ricevuto aggiornamenti tecnici non decisionali coerenti con il mandato. Gli issue restano OPEN e le fonti restano REVIEW.

GIT_COMMIT_REQUIRED = YES

Motivo: review metodologico-tecnico e script riproducibili sono artifact leggeri versionabili.

PROJECT_SOURCE_OF_TRUTH_CHANGE = NO

Motivo: la Chat 3.3 non approva autonomamente decisioni sostanziali; il consolidamento spetta alla Chat Madre/utente.

Artifact check:
- nessun artifact FROZEN modificato;
- raw/output pesanti conservati in OneDrive;
- hash principali calcolati e riportati;
- script e documentazione conservati in Git;
- preservation fisica verificata sui percorsi OneDrive sincronizzati disponibili nella sessione.

Build notebook: N/A.

## 11. Problemi aperti

1. Semantica di direzionalità del grafo insufficiente per routing Light diretto.
2. Restrizioni Heavy non coperte dal grafo statico.
3. Crosswalk completo route-level TEN-T 3-tier non ancora chiuso.
4. Q-METH-3.3-A da sottoporre all’utente.
5. TENT_EXIT_SET_v01 non ancora costruito, intenzionalmente.
6. Accessi reali non ancora costruiti, intenzionalmente.

## 12. Stato finale e prossimo passo

**Chat 3.3: PASS tecnico-operativo.**

Questo PASS attesta il completamento del mandato di validazione/delimitazione, non la risoluzione di ISS-0004/ISS-0005 e non il freeze della Fase 3.

Prossimo passo per la Chat Madre:
1. ricevere e verificare il presente handoff;
2. integrare con gli esiti delle altre chat Fase 3;
3. decidere se aprire un follow-up tecnico sulla direzionalità/Heavy;
4. sottoporre Q-METH-3.3-A all’utente prima di costruire l’exit set;
5. non avviare candidati/accessi sulla base di una rete diretta o TEN-T exit set non ancora validati.
