# DISPATCH — Chat 3.7 — Crosswalk TEN-T FVG e rilevanza delle uscite AFIR

**Fase:** 3 — Inventario e validazione dei dati
**Data:** 2026-09-18
**Stato mandato:** AUTHORIZED
**Regia:** Chat Madre 5 HUB

## 1. Obiettivo

Costruire un crosswalk route-level corrente e tracciabile tra la rete stradale TEN-T vigente in Friuli Venezia Giulia e le strade reali FVG, distinguendo esplicitamente i tre livelli **core / extended core / comprehensive**.

Usare poi tale crosswalk per verificare se esista realmente, nel dominio FVG rilevante al modello 5 HUB, almeno un tratto TEN-T privo di vere rampe/svincoli e caratterizzato da accessi/intersezioni ordinarie a raso.

La chat NON deve decidere autonomamente come interpretare “nearest TEN-T exit” nei casi a raso. Deve prima dimostrare se il caso esiste davvero e, solo se esiste, riportarlo alla Chat Madre.

## 2. Baseline vincolanti e input READ ONLY

- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md` — FROZEN;
- `docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md`;
- `docs/FASE_3_ROAD_TENT_VALIDATION_REVIEW_v01.md`;
- `docs/FASE_3_TENT_EXIT_RELEVANCE_SCREENING_v01.md` — screening preliminare Chat Madre, non decisione metodologica;
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER, soprattutto `ISS-0005`.

Baseline OSM FROZEN utilizzabile esclusivamente come supporto geometrico/topologico:
`TESI_THESIS_STORAGE\04_FROZEN_CHECKPOINTS\RECOVERED_BASELINE\OSM_5_6\grafo_operativo_osm\G_OSM_operativo_v01.gpkg`

Il progetto Claude, i 23 exit storici e i layer TENtec legacy possono essere usati solo come piste/benchmark, mai come fonte autorevole corrente.

## 3. Fonti autorevoli

Per appartenenza alla TEN-T e livello di rete usare prioritariamente:
- Regolamento (UE) 2024/1679;
- cartografia e allegati ufficiali DG MOVE / TENtec 2024;
- eventuali servizi TENtec correnti coerenti con la tassonomia a tre livelli.

Per denominazione, gestione e natura fisica della strada usare, quando necessario:
- ANAS;
- concessionari/autostrade;
- Regione FVG;
- altri gestori ufficiali.

OSM serve a leggere topologia, rampe, `motorway_link`, `trunk_link`, sensi di marcia e morfologia dell’accesso. OSM NON determina se una strada appartiene alla TEN-T né il suo livello normativo.

## 4. Crosswalk obbligatorio

Produrre un artifact tabellare versionato, indicativamente:
`TENT_FVG_ROUTE_CROSSWALK_v01.csv`

Ogni record deve essere tracciabile e contenere almeno:
- identificativo stabile del record;
- livello TEN-T: core / extended core / comprehensive;
- fonte ufficiale TEN-T e relativo feature/object ID quando disponibile;
- strada reale FVG: ref/nome;
- tratto o estensione spaziale;
- gestore se disponibile;
- metodo di associazione geometrica;
- distanza/qualità del match dove applicabile;
- stato di validazione;
- evidenza e note;
- versione/data della fonte.

Il crosswalk deve coprire l’intera rete stradale TEN-T FVG corrente, non soltanto i corridoi core già validati da Chat 3.3.

Non sono ammessi:
- inferenza del livello TEN-T per semplice prossimità;
- riuso della tassonomia legacy core/comprehensive come se fosse vigente;
- assunzione che l’assenza di extended core in un servizio legacy implichi assenza reale;
- assegnazioni route-level senza evidenza verificabile.

## 5. Audit della rilevanza “nearest exit”

Per ogni tratto TEN-T del crosswalk classificare la morfologia di accesso almeno come:
- `GRADE_SEPARATED / CONTROLLED_ACCESS`;
- `AT_GRADE`;
- `MIXED`;
- `UNKNOWN / TO_VERIFY`.

Per i tratti non chiaramente grade-separated:
1. usare OSM come screening;
2. verificare online con fonte del gestore o cartografia ufficiale;
3. documentare gli specifici nodi/intersezioni che rendono il caso rilevante.

Output indicativo:
`TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv`.

Domanda finale obbligatoria, a cui rispondere con evidenza:

> Esiste almeno un tratto stradale TEN-T corrente in FVG, rilevante al modello 5 HUB, nel quale l’applicazione AFIR del concetto di “nearest exit” richieda davvero una decisione interpretativa perché non esiste una vera uscita/rampa univoca?

Se NO:
- dimostrarlo rispetto alla copertura completa del crosswalk;
- proporre alla Chat Madre di considerare Q-METH-3.3-A non materialmente rilevante nel dominio FVG.

Se SÌ:
- elencare esattamente i tratti e le intersezioni coinvolte;
- NON inventare una regola;
- formulare una questione decisionale puntuale per la Chat Madre/utente.

## 6. Divieti

NON:
- costruire candidati Hub;
- calcolare distanze candidato→TEN-T;
- creare il definitivo `TENT_EXIT_SET_v01`;
- riusare automaticamente le 23 uscite storiche;
- trasformare rotatorie/intersezioni a raso in “exit” per convenzione;
- modificare baseline FROZEN;
- chiudere autonomamente Q-METH-3.3-A o `ISS-0005`;
- assumere una classe TEN-T mancante.

## 7. Output attesi

Minimo:
- `docs/FASE_3_TENT_CROSSWALK_VALIDATION_REVIEW_v01.md`;
- `TENT_FVG_ROUTE_CROSSWALK_v01.csv`;
- `TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv`;
- eventuale script riproducibile del crosswalk/audit;
- evidence package con fonti materializzate, metadati e hash;
- `docs/HANDOFF_CHAT_3.7_TENT_CROSSWALK_v01.md`.

Percorsi pesanti/intermedi in OneDrive secondo architettura ufficiale; codice e documentazione leggera in `C:\dev\5-hub`.

La chat deve lavorare su branch dedicato:
`chat-3.7-tent-crosswalk`.

## 8. Quality gate

PASS tecnico-operativo solo se:
- la rete stradale TEN-T FVG corrente è coperta route-level nei tre livelli o ogni gap residuo è esplicito e localizzato;
- ogni associazione TEN-T↔strada reale è tracciabile;
- legacy e OSM restano chiaramente supporti, non fonti normative;
- l’audit distingue veri svincoli/rampe da intersezioni a raso;
- la rilevanza reale di Q-METH-3.3-A è dimostrata oppure il residuo è esplicitamente delimitato;
- nessuna decisione metodologica sostanziale è stata presa autonomamente;
- registri, hash, Git e SESSION CLOSE/handoff sono completi.

La Chat Madre effettua review indipendente prima di accettare il PASS e prima di qualsiasi chiusura di issue o decisione metodologica.