# REVIEW — Chat 3.10 — Baseline stradali e domanda Light/Heavy

**Reviewer:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-20
**Mandato:** review indipendente degli artifact Chat 3.10 e disposizione di ISS-0004
**Decisioni di riferimento:** DEC-0054
**Artifact specialistico:** `docs/FASE_3_LIGHT_HEAVY_BASELINE_VALIDATION_REVIEW_v01.md`
**Handoff:** `docs/HANDOFF_CHAT_3.10_LIGHT_HEAVY_BASELINES_v01.md`

## 1. Esito

**TECHNICAL_QUALITY_GATE = ACCEPTED_WITH_LIMITATIONS**

La raccomandazione della Chat 3.10 è confermata.

Per la pianificazione macro dei 5 HUB non è necessario costruire un nuovo sistema regionale Light/Heavy da zero:
- Light può riusare G_OSM + Gamma_OSM + OD_PATH_SYSTEM_OSM;
- LIGHT_DIRTY_OD_v01 è ammessa come domanda macro provvisoria con k=0,15 secondo DEC-0054;
- Heavy può riusare Heavy 6.0 Speth/ETISplus per domanda, path-flow e corridoi;
- l'accessibilità fisica e legale del singolo candidato resta un controllo locale separato.

## 2. Verifiche indipendenti Chat 0.2

La Chat Madre non ha assunto come veri i risultati dell'handoff.

Sono stati verificati:
- branch `chat-3.10-light-heavy-routing-demand` e commit finale `05fa09d`;
- `git diff --check main...branch` senza errori;
- contenuto dei tre artifact specialistici;
- hash della matrice Light delivery;
- hash del package Heavy 6.0;
- hash di tre copie di `G_OSM_operativo_v01.gpkg`;
- cardinalità Light/Heavy tramite ricalcolo indipendente.

Risultati indipendenti:
- `LIGHT_DIRTY_OD_v01`: 46.010 righe;
- `HEAVY_OD_VEHICLES_DAY_v01.csv`: 81.555 righe / 81.555 `od_id` unici;
- `HEAVY_PATH_FLOWS_v01.csv`: 81.555 righe / 81.555 `od_id` unici;
- path Heavy vuoti: 0;
- distanze Heavy non positive: 0;
- hash Light: `c114d71cc8fbfd47167709899dc93e6dba823424fe9f1d25499795c6cbdd7769`;
- hash Heavy ZIP: `24bab0bde58e6f8fc83833ff177464b2e4ded4ae1a6b91894d3542506f9350bb`.

## 3. Funzione delle baseline

### Light
`G_OSM_operativo` e `OD_PATH_SYSTEM_OSM` forniscono rete e path macro.

`Gamma_OSM` rappresenta accessi comunali, non accessi dei candidati Hub.

`LIGHT_DIRTY_OD_v01` fornisce la domanda Light macro provvisoria. Il suo stato originario di tesi resta `PROVISIONAL / NON-CANONICAL`; l'uso nel 5 HUB è autorizzato esclusivamente da DEC-0054 e non la trasforma in baseline scientifica definitiva della tesi.

### Heavy
Heavy 6.0 Speth/ETISplus fornisce domanda, path-flow e corridoi macro.

Non fornisce prova completa della percorribilità locale Heavy fino al singolo sito, né sostituisce la verifica di restrizioni locali, accessi, geometrie e ordinanze pertinenti al candidato.
## 4. ISS-0004

Il fatto originario resta vero: il layer regionale `F3_SRC_FVG_ROADGRAPH_001` da solo non è una rete Light/Heavy di produzione validata.

Tuttavia DEC-0054 ha eliminato la necessità metodologica di dipendere da quel layer come backbone operativo del 5 HUB.

Le baseline tesi già validate coprono ciò che serve alla scala macro:
- Light: rete/path + domanda provvisoria;
- Heavy: domanda + path-flow + corridoi.

La verifica locale resta obbligatoria quando un candidato deve essere confermato come realmente accessibile.

**DISPOSIZIONE CHAT 0.2: ISS-0004 = RESOLVED PROCEDURALLY.**

La risoluzione:
- non dichiara idoneo il vecchio grafo regionale;
- non dichiara Speth rete legale completa per mezzi pesanti;
- non elimina la verifica locale;
- rimuove il blocker region-wide perché non è più richiesto dalla metodologia approvata.

Flag operativo futuro:
`LOCAL_ROAD_ACCESS_CHECK_REQUIRED`, con verifica specifica Light/Heavy quando pertinente prima della conferma finale del sito.

## 5. ISS-0014 — preservation

La review indipendente conferma:
- copia difforme `TESI_BASELINE_SAFE\...\G_OSM_operativo_v01.gpkg`:
  `eb2953dfb05ee71d11688a38d6eeed67412a939f95040dd874fb2b9d192cab37`;
- hash FROZEN atteso:
  `f1d87245d1bc28f3ecab16e126514f8a3ab718b73ce7bd244db2f12628697ef3`;
- due copie indipendenti preservate coincidono con l'hash FROZEN atteso.

Le tre copie hanno la stessa dimensione file, ma una sola è byte-difforme.

**ISS-0014 resta OPEN**, separata da ISS-0004.

Regola:
- non usare la copia difforme;
- non sovrascriverla in place;
- usare manifest FROZEN + copia hash-corretta;
- gestire successivamente la preservation copy con procedura versionata.

ISS-0014 non blocca la Fase 3 metodologica perché l'artifact FROZEN hash-corretto è disponibile in due copie indipendenti.

## 6. Data Registry

Le sei fonti Chat 3.10 possono passare da REVIEW ad ACCEPTED per il perimetro 5 HUB autorizzato:
- `F3_SRC_LIGHT_OSM_GRAPH_001`;
- `F3_SRC_LIGHT_GAMMA_001`;
- `F3_SRC_LIGHT_OD_PATH_001`;
- `F3_SRC_LIGHT_DEMAND_001`;
- `F3_SRC_HEAVY_OD_001`;
- `F3_SRC_HEAVY_PATH_001`.

L'accettazione non modifica lo stato FROZEN/provvisorio degli artifact nel progetto tesi: definisce soltanto il loro ruolo approvato nel 5 HUB.

## 7. Stato finale

**Chat 3.10 = REVIEWED / ACCEPTED_WITH_LIMITATIONS.**

**ISS-0004 = RESOLVED PROCEDURALLY.**

**ISS-0014 = OPEN / NON-BLOCKING PRESERVATION ISSUE.**

Fase 4 non viene aperta da questa review.
