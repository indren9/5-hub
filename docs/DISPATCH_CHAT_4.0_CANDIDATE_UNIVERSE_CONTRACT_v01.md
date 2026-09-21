# DISPATCH — Chat 4.0 — Contratto dell'universo dei poligoni candidati

**Mandante:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Stato:** AUTHORIZED
**Stadio:** V2-1 / DQ-01
**Vincolo:** NON costruire ancora l'universo candidato

## 1. Obiettivo

Definire il CANDIDATE_UNIVERSE_CONTRACT del MODEL_v2.

La chat deve stabilire quali fonti e categorie generano i poligoni candidati, quali sole regole geometriche sono necessarie, se serve una superficie minima e quali eventuali prefiltri HARD sono davvero indispensabili.

Il contratto deve essere sottoposto all'utente prima di qualsiasi generazione massiva dei candidati.

## 2. Baseline vincolanti

Leggere integralmente:
- docs/PROJECT_MODEL_CONTRACT_REBASELINE_v01.md;
- docs/ROADMAP_METODOLOGICA_v2.md;
- docs/FASE_1_HUB_DEFINITION_REBASELINED_v03.md;
- docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md;
- docs/REBASELINE_APPROVAL_AND_PHASE3_CLOSE_v01.md;
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER.
## 3. Principi da non riaprire

- unità di analisi = poligono;
- il poligono è alternativa localizzativa strategica, non lotto catastale verificato;
- proprietà/disponibilità commerciale fuori core;
- nessuna due diligence autorizzativa o progettuale;
- nessun indicatore, peso, score o ottimizzazione in questa chat;
- baseline Claude/QGIS da 1.377 candidati = HISTORICAL SUPPORT, non universo autorevole;
- nessuna soglia storica di 5.000 m² viene ereditata implicitamente.

## 4. Domande DQ-01 da risolvere

Preparare una proposta esplicita su:
1. quali dataset/categorie territoriali generano i candidati;
2. se l'universo nasce da una sola famiglia di aree o da unione di più famiglie;
3. regole di split/merge coerenti con Fase 2;
4. trattamento dei multipart e delle geometrie invalide;
5. eventuale superficie minima e sua giustificazione;
6. eventuali prefiltri hard indispensabili prima dello scoring;
7. cosa NON deve essere usato come prefiltro hard;
8. gestione di currentness/proxy e lineage;
9. ID/versioning dei candidati;
10. QA minimo prima di passare a V2-2.

## 5. Metodo di decisione

Non scegliere per comodità tecnica.

Per ogni opzione sostanziale:
- descrivere il razionale;
- indicare vantaggi/svantaggi metodologici;
- indicare effetto possibile su completezza e bias dell'universo;
- distinguere requisito necessario da scelta progettuale;
- proporre una raccomandazione, ma lasciarla PROPOSED.
## 6. Materiale da riusare

Usare le fonti territoriali/urbanistiche già validate in Fase 3.

La baseline Claude/QGIS può essere consultata solo per:
- capire categorie storicamente usate;
- confrontare ordine di grandezza e copertura;
- recuperare piste/fonti.

Non deve determinare automaticamente:
- categorie;
- soglie;
- geometrie;
- numero atteso di candidati.

## 7. Output obbligatori

- docs/CANDIDATE_UNIVERSE_CONTRACT_v01_PROPOSED.md
- docs/CANDIDATE_SOURCE_OPTIONS_v01.csv
- docs/DQ01_DECISION_PACKET_v01.md
- docs/HANDOFF_CHAT_4.0_CANDIDATE_UNIVERSE_CONTRACT_v01.md

Eventuali script possono essere usati solo per audit/quantificazione delle opzioni, non per produrre l'universo definitivo.

## 8. Quality gate

PASS solo se:
- nessun candidato definitivo è costruito;
- le opzioni sono confrontate con evidenze;
- nessuna soglia storica è ereditata senza giustificazione;
- proprietà/catasto non rientrano nel core;
- hard prefilter ridotti al minimo indispensabile;
- Fase 2 è rispettata;
- DQ-01 resta PROPOSED;
- git diff --check PASS;
- handoff completo.

Poi fermarsi per decisione utente.
