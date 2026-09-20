# DISPATCH — Chat 3.10 — Baseline stradali e domanda Light/Heavy

**Fase:** 3 — Inventario e validazione dei dati
**Data:** 2026-09-20
**Stato mandato:** AUTHORIZED
**Regia:** Chat 0.2 — Chat Madre 5 HUB
**Issue principale:** ISS-0004
**Decisione di riferimento:** DEC-0054

## 1. Obiettivo

Verificare e rendere riusabili nel progetto 5 HUB le baseline stradali e di domanda già sviluppate nel progetto tesi, evitando di ricostruire reti, matrici OD o flussi Heavy già disponibili.

Il lavoro è di **pianificazione macro regionale**.

La Chat 3.10 non deve sviluppare un nuovo modello di traffico. Deve stabilire se gli artifact esistenti sono sufficienti e tracciabili per alimentare le fasi successive del 5 HUB e delimitare ciò che resta da verificare sui singoli candidati/finalisti.

## 2. Principio operativo

Separare sempre tre oggetti:

1. **rete / path system** — dove possono essere rappresentati i percorsi;
2. **domanda OD / flow demand** — quanti veicoli sono associati alle relazioni;
3. **accessibilità locale del candidato** — se uno specifico sito è realmente raggiungibile dal veicolo Light/Heavy.

Non confondere una matrice OD con un grafo stradale e non interpretare un path-flow macro come verifica dell'accesso fisico a un candidato.
## 3. Baseline LIGHT da riusare

### 3.1 Grafo e path system

Repository tesi:
`C:\dev\tesi-frlm-fvg`

Artifact autorevoli/FROZEN:
- `04_FROZEN_CHECKPOINTS\OSM_5_6\grafo_operativo_osm`
- `04_FROZEN_CHECKPOINTS\OSM_5_6\accessi_comunali_osm_light`
- `04_FROZEN_CHECKPOINTS\OD_PATHS_5_7\od_paths_osm_light`

Riferimenti Artifact Register tesi:
- `F56_GAMMA_OSM_PACKAGE_V01`
- `F57_OD_PATH_SYSTEM_OSM_V01`

Stato noto:
- `G_OSM_operativo = FROZEN`
- `Gamma_OSM = FROZEN`
- `OD_PATH_SYSTEM_OSM = FROZEN`
- 215 comuni;
- 46.010 OD intercomunali ordinate;
- 3 accessi comunali per comune;
- 414.090 access-pair path;
- reachability completa nel dominio frozen.

Questi artifact NON devono essere modificati o rigenerati.

### 3.2 Domanda Light macro approvata per 5 HUB

Dataset:
`LIGHT_DIRTY_OD_v01`

Copia delivery:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\TESI_THESIS_STORAGE\07_DELIVERIES\LIGHT_OD_20260908\Matrice_OD\MATRICE_OD_VEICOLI_LEGGERI_DATI\01_LIGHT_DIRTY_OD_v01.csv`

Provenance/QA storica:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\90_ARCHIVE\LEGACY_WORKSPACES\Dirty_FRLM\05_REPORTING\light_dirty_od_v01\LIGHT_DIRTY_OD_v01_manifest.json`
Contratto della matrice:
- 46.010 OD;
- `T_dirty_ij = C_ISTAT_ij + N_dirty_ij`;
- `N_dirty_ij = 0.15 * N_v0_ij`;
- `k_dirty = 0.15`;
- `beta_dirty = 0.045953794473 1/min`;
- pendolarismo ISTAT invariato;
- nessuna nuova calibrazione ANAS richiesta nel progetto 5 HUB.

Stato originale nella tesi:
`ENGINEERING / DEMONSTRATOR / PROVISIONAL / NON-CANONICAL`.

Decisione 5 HUB:
il dataset è ammesso come **PROVISIONAL_MACRO_INPUT** per il 5 HUB. Non deve essere presentato come matrice Light scientificamente definitiva della tesi.

La Chat 3.10 deve verificare integrità, cardinalità, formula e lineage, ma NON stimare un nuovo k, beta o Q e NON riaprire la calibrazione Gravity/ANAS.

## 4. Baseline HEAVY da riusare

Pacchetto FROZEN:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\TESI_THESIS_STORAGE\04_FROZEN_CHECKPOINTS\HEAVY_6_0\HEAVY_0B_delivery_v01.zip`

Artifact Register tesi:
`H60_HEAVY_OD_SPETH_PACKAGE_V01`

Contenuti principali:
- `HEAVY_OD_VEHICLES_DAY_v01.csv`
- `HEAVY_PATH_FLOWS_v01.csv`
- `HEAVY_TRANSIT_EXCLUSIONS_v01.csv`
- `HEAVY_ARTIFACT_SUMMARY_v01.txt`
Contratto Heavy congelato:
- fonte: Speth et al. / ETISplus;
- baseline: `Traffic_flow_trucks_2019`;
- 2030 = scenario prospettico;
- i valori sono già flussi modellati di camion, non tonnellate da convertire;
- annuale -> giornaliero tramite `/365`;
- 10.875 OD_FVG;
- 70.680 transiti FVG mantenuti;
- 81.555 relazioni operative dirette complessive;
- routing su rete stradale europea Speth con path operativi validati;
- ANAS = sanity check indipendente, non calibrazione.

Limitazioni note da preservare:
- bias sistematico alto dei volumi assoluti rispetto al limitato sanity check ANAS;
- accesso/distribuzione locale Heavy relativamente grossolani;
- rappresentazione A34 / Gorizia / Sant'Andrea debole o incompleta;
- 2030 non calibrato localmente.

Stato:
`HEAVY 6.0 = CLOSED / FROZEN`
`SPETH_FOR_DELIVERY = ACCEPT_WITH_LIMITATIONS`

Gli artifact FROZEN non devono essere modificati o ricalcolati.
## 5. Domande che la Chat 3.10 deve chiudere

1. Gli artifact Light OSM FROZEN sono integri, tracciabili e sufficienti come baseline di rete/path per la pianificazione macro 5 HUB?
2. `LIGHT_DIRTY_OD_v01` è integro e coerente con il contratto k=0,15 e può essere usato nel 5 HUB come domanda Light provvisoria macro senza ricalibrazione?
3. Il pacchetto Heavy 6.0 Speth è integro e sufficiente per rappresentare domanda e corridoi Heavy a scala macro?
4. Quali funzioni sono coperte da ciascun asset: rete, OD, path flow, corridoio, accessibilità locale?
5. Per il 5 HUB è davvero necessario costruire un nuovo grafo Heavy con tutte le restrizioni legali, oppure è sufficiente rinviare la verifica dettagliata dell'accessibilità Heavy ai candidati finalisti?
6. ISS-0004 può essere proposto come `RESOLVED_PROCEDURALLY` per la pianificazione macro, mantenendo un flag di verifica locale Heavy sui finalisti?
7. Quali artifact devono essere referenziati nel DATA_REGISTRY del 5 HUB senza duplicare inutilmente file pesanti già preservati nel progetto tesi?

## 6. Vincoli

NON:
- ricostruire G_OSM;
- rigenerare Gamma_OSM;
- rigenerare OD_PATH_SYSTEM_OSM;
- stimare nuovamente k, beta o Q Light;
- calibrare nuovamente la matrice Light su ANAS;
- ricostruire ETISplus/Speth da zero;
- ricalibrare Speth su ANAS;
- costruire un nuovo modello Heavy region-wide di massa/altezza/larghezza/ordinanze salvo prova che sia indispensabile alla pianificazione macro;
- modificare artifact FROZEN della tesi;
- costruire candidati della Fase 4;
- aprire la Fase 4.
## 7. Regola sulla duplicazione dei dati

Gli artifact tesi esistenti sono già preservati in repository/OneDrive.

Preferire **reference-by-manifest + hash + path** invece di duplicare pacchetti pesanti nel namespace `5_HUB_FVG`.

Materializzare una nuova copia solo se tecnicamente necessaria alla riproducibilità del 5 HUB e motivare esplicitamente la duplicazione.

Sono ammessi nel 5 HUB:
- manifest leggeri;
- source matrix;
- crosswalk di lineage;
- piccoli estratti QA;
- report di validazione.

## 8. Output richiesti

Repository `C:\dev\5-hub`:
- `docs/FASE_3_LIGHT_HEAVY_BASELINE_VALIDATION_REVIEW_v01.md`
- `docs/FASE_3_LIGHT_HEAVY_SOURCE_MATRIX_v01.csv`
- `docs/HANDOFF_CHAT_3.10_LIGHT_HEAVY_BASELINES_v01.md`
- eventuali script leggeri esclusivamente per QA/integrità.

OneDrive 5 HUB, solo se necessario:
`5_HUB_FVG\02_external_sources\F3_CHAT_3_10\`

Branch:
`chat-3.10-light-heavy-routing-demand`
## 9. Quality gate

PASS tecnico solo se:
- gli artifact tesi richiamati esistono e la loro provenance è verificabile;
- hash/manifest principali sono coerenti dove disponibili;
- Light network/path system resta separato dalla domanda OD;
- `LIGHT_DIRTY_OD_v01` è verificata come 46.010 OD e come formula con k=0,15 senza ricalcolo;
- il suo stato provvisorio/non-canonico nella tesi resta esplicito;
- Heavy 6.0 è verificato come Speth/ETISplus in truck flows e non reinterpretato come tonnellaggio;
- i limiti Heavy noti restano espliciti;
- è chiarito se Speth copre domanda/corridoi ma non necessariamente accesso locale del candidato;
- nessuna restrizione Heavy mancante viene inventata;
- nessun artifact FROZEN viene modificato;
- viene formulata una raccomandazione esplicita su ISS-0004: `KEEP_OPEN`, `READY_WITH_LIMITATIONS` oppure `PROPOSE_RESOLVED_PROCEDURALLY`.

## 10. Criterio di successo

La Chat Madre deve poter rispondere con chiarezza:

> Per una pianificazione macro dei 5 Hub, quali artifact Light e Heavy già esistenti possiamo riusare senza ricostruzioni, per quali funzioni, con quali limiti e con quali verifiche rinviate ai finalisti?

La Chat 3.10 non può chiudere autonomamente ISS-0004. La decisione finale resta alla Chat 0.2 / utente.
