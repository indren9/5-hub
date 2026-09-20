# FASE 3 â€” Baseline stradali e domanda Light/Heavy â€” Review Chat 3.10

**Chat:** 3.10 â€” Baseline stradali e domanda Light/Heavy
**Data:** 2026-09-20
**Stato documento:** REVIEW
**Esito tecnico:** PASS WITH LIMITATIONS
**Regia metodologica:** Chat 0.2 â€” Chat Madre 5 HUB
**Decisione di riferimento:** DEC-0054 â€” ACCEPTED
**Issue principale:** ISS-0004 â€” OPEN all'avvio

## 1. Scopo e confini

Il mandato verifica la riusabilitÃ  nel progetto 5 HUB di baseline stradali e di domanda giÃ  FROZEN o materializzate nella tesi, senza ricostruire reti, matrici OD o flussi Heavy.

La scala di riferimento Ã¨ la pianificazione macro regionale. Restano separati: rete/path system; domanda OD/flow demand; path flow/corridoi; accessibilitÃ  locale del singolo candidato.

Non sono stati costruiti candidati, accessi, road anchor, connettori, nuove reti o nuove matrici. Non sono stati ricalibrati k, beta, Q, ANAS o Speth. Nessun artifact FROZEN Ã¨ stato modificato.

## 2. Baseline e governance verificate

Sono stati letti integralmente il dispatch Chat 3.10, le baseline FROZEN di Fase 1 e Fase 2, la review Chat 3.3 e il relativo handoff.

Il PROJECT_SOURCE_OF_TRUTH vivo conferma: Fasi 1â€“2 FROZEN, Fase 3 IN CORSO, Fase 4 NON AVVIATA.
Il PROJECT_CONTROL_REGISTER conferma DEC-0054 = ACCEPTED; ISS-0004 = OPEN con owner Chat 3.10; il DATA_REGISTRY non conteneva ancora le baseline tesi Light/Heavy come fonti del 5 HUB.

DEC-0054 autorizza il riuso macro delle baseline tesi esistenti e vieta la ricostruzione non necessaria del sistema traffico.

## 3. LIGHT â€” G_OSM_operativo

G_OSM_operativo_v01 Ã¨ una rete OSM Light diretta FROZEN, con modello B5 turn-aware e separazione tra CORE e local restricted.

Il final gate FROZEN riporta 944.219 segmenti fisici, 1.698.857 archi diretti, giant SCC di 889.440 nodi, F1 PASS, F2 PASS, F3 PASS_NO_SYSTEMIC_SIGNAL, zero issue systemic e zero blocking.

Il manifest corrente ha SHA-256 c4ea80c9c660f6a513b20400d0c3edb2f9e6ec10c3364f0a4b0beed91af55da3, coerente con il gate FROZEN.

### 3.1 Anomalia di preservation copy

La copia TESI_BASELINE_SAFE\04_FROZEN_CHECKPOINTS\OSM_5_6\grafo_operativo_osm\G_OSM_operativo_v01.gpkg ha oggi SHA-256 eb2953dfb05ee71d11688a38d6eeed67412a939f95040dd874fb2b9d192cab37 e NON coincide con l'hash FROZEN atteso f1d87245d1bc28f3ecab16e126514f8a3ab718b73ce7bd244db2f12628697ef3.

L'artifact hash-corretto non Ã¨ perso: due copie indipendenti preservate coincidono con l'hash FROZEN atteso:
- 90_ARCHIVE\LEGACY_WORKSPACES\Dirty_FRLM\01_INPUT_SNAPSHOT\network\G_OSM_operativo_v01.gpkg;
- TESI_THESIS_STORAGE\04_FROZEN_CHECKPOINTS\RECOVERED_BASELINE\OSM_5_6\grafo_operativo_osm\G_OSM_operativo_v01.gpkg.

Non Ã¨ stata eseguita alcuna riparazione o sovrascrittura in place. Il 5 HUB deve referenziare il manifest FROZEN e una copia hash-corretta finchÃ© la preservation copy difforme non viene gestita separatamente.

**Giudizio funzionale:** G_OSM Ã¨ idoneo come baseline Light di rete/path a scala macro. Non prova l'accesso fisico o legale di un futuro candidato.

## 4. LIGHT â€” Gamma_OSM

Gamma_OSM Ã¨ FROZEN e rappresenta il sistema di accesso comunale usato dalla tesi, non gli accessi dei futuri candidati Hub.

Contratto verificato: 215 Comuni, K=3 accessi comunali per Comune, 645 accessi, 414.090 coppie intercomunali di accesso, unreachable=0, bad triplets=0, pesi EXP_REL_300 FROZEN.

Il manifest corrente ha SHA-256 31ee2d78cd06c75cdf07014a8cecac4af2c58adeb26ec7285362ab4c02b11416. Sono stati ri-hashati in questa chat anche Gamma_OSM_L_comuni_fvg_v01.gpkg e Gamma_OSM_L_comuni_fvg_v01.csv, entrambi MATCH con il manifest.

**Giudizio funzionale:** riusabile per rappresentare accessi/impedenze comunali del sistema Light esistente. Non Ã¨ accessibilitÃ  locale del candidato e non sostituisce access_point -> road_anchor -> network.

## 5. LIGHT â€” OD_PATH_SYSTEM_OSM

OD_PATH_SYSTEM_OSM Ã¨ FROZEN / PASS: 215 Comuni, 46.010 OD intercomunali ordinate, 3 accessi per Comune, 414.090 access-pair path, tutti finiti, unreachable=0.

Il manifest corrente ha SHA-256 9c3279c604685dbb8ebf52d18910658efc5fb7fe0ab1069d36d313476abb8fff, coerente con l'Artifact Register tesi. L'Artifact Register registra F57_OD_PATH_SYSTEM_OSM_V01 come FROZEN / VERIFIED e dichiara tutti i membri canonici verificati il 2026-09-17. In questa chat non sono stati nuovamente ri-hashati tutti i membri multi-GB.

**Giudizio funzionale:** sufficiente come path baseline Light macro. Ãˆ un path system, non una domanda OD e non un path-flow di traffico finchÃ© non gli viene associata domanda.

## 6. LIGHT â€” LIGHT_DIRTY_OD_v01

Il CSV delivery corrente ha SHA-256 c114d71cc8fbfd47167709899dc93e6dba823424fe9f1d25499795c6cbdd7769, 46.010 righe e 46.010 chiavi OD uniche.

Controllo numerico indipendente Chat 3.10:
- N_dirty_ij = 0,15 * N_v0_ij: max errore serializzato circa 1,0e-11;
- T_dirty_ij = C_ISTAT_ij + N_dirty_ij: max errore circa 5,0e-12;
- sum(T_dirty) circa 437.968,4592 veh/day.

Parametri di provenance: k_dirty=0,15; beta_dirty=0,045953794473 1/min; status tesi = ENGINEERING / DEMONSTRATOR / PROVISIONAL / NON-CANONICAL.

La provenance punta a OSM_OD_municipal_summary_v01.csv con SHA-256 dfa2db5e3b18c9c1c7f05e2c7b7445848904971f35c916390bfc4d1b34571441, identico al membro FROZEN del path system F57.

**Giudizio funzionale:** sufficiente come PROVISIONAL_MACRO_INPUT di domanda Light nel 5 HUB ai sensi di DEC-0054. Non deve essere presentato come matrice Light scientificamente definitiva e non giustifica nuova calibrazione.

## 7. HEAVY â€” Heavy 6.0 Speth/ETISplus

Il package FROZEN HEAVY_0B_delivery_v01.zip ha SHA-256 corrente 24bab0bde58e6f8fc83833ff177464b2e4ded4ae1a6b91894d3542506f9350bb, MATCH con Artifact Register tesi.

I tre artifact principali interni sono stati ri-hashati e coincidono con il summary FROZEN:
- HEAVY_OD_VEHICLES_DAY_v01.csv = 3b3b053b48429dce8bd51790c788690ed9e75f8aea26ed37fb2807e6e2d050d8;
- HEAVY_PATH_FLOWS_v01.csv = fb20e5c7ef2e7fa45600ad9f9d75709017e0d8173d6ef69fd3ca806ebd539e6f;
- HEAVY_TRANSIT_EXCLUSIONS_v01.csv = 6590a2b4a88b7725b6b436c198c33431e54e0a4e800f0c07de06c0ddc4518011.

Controllo indipendente: 81.555 OD operative uniche; 10.875 OD_FVG; 70.680 TRANSIT_FVG; 81.555 righe path; set OD=set path; path vuoti=0; distanze non positive=0; conversione annuale/giornaliero coerente con /365 entro precisione di serializzazione.

Tutti i path usano il metodo SPETH_EXACT_ENDPOINT_DIJKSTRA_NO_MANUAL_MACRO_EDGES. Il baseline year Ã¨ 2019. Il 2030 Ã¨ scenario prospettico, non calibrato localmente. ANAS Ã¨ solo sanity check.

Limitazioni da mantenere: bias alto dei volumi assoluti rispetto al sanity check ANAS disponibile; accesso/distribuzione locale Heavy grossolani, soprattutto attorno a Trieste; rappresentazione A34 / Gorizia / Sant'Andrea debole o incompleta; nessuna copertura completa delle restrizioni legali locali Heavy.

**Giudizio funzionale:** Speth 6.0 Ã¨ sufficiente per domanda, path-flow e corridoi Heavy a scala macro. Non Ã¨ prova di accessibilitÃ  fisica/legale del singolo candidato.

## 8. Matrice funzionale sintetica

| Asset | Rete/path system | Domanda | Path flow | Corridoio | AccessibilitÃ  locale candidato |
|---|---|---|---|---|---|
| G_OSM_operativo | SÃŒ â€” Light | NO | NO | supporta | NO |
| Gamma_OSM | supporto accessi comunali | NO | NO | NO | NO |
| OD_PATH_SYSTEM_OSM | SÃŒ â€” path Light | NO | NO | SÃŒ, geometrico | NO |
| LIGHT_DIRTY_OD_v01 | NO | SÃŒ â€” provvisoria macro | NO | NO da sola | NO |
| HEAVY_OD_VEHICLES_DAY_v01 | NO | SÃŒ â€” Heavy | NO | NO da solo | NO |
| HEAVY_PATH_FLOWS_v01 | path incorporati | domanda riportata | SÃŒ | SÃŒ | NO |

## 9. NecessitÃ  di un nuovo grafo Heavy region-wide

Non emerge una necessitÃ  metodologica di costruire ora un nuovo grafo Heavy regionale completo di massa, altezza, larghezza e ordinanze.

Per la pianificazione macro, domanda e corridoi Heavy sono giÃ  coperti da Speth 6.0. Una nuova rete Heavy region-wide aggiungerebbe complessitÃ  senza chiudere automaticamente l'accesso al singolo sito.

La verifica dettagliata Heavy puÃ² quindi essere rinviata ai candidati finalisti, con flag obbligatorio proposto HEAVY_LOCAL_ACCESS_CHECK_REQUIRED. Per le verifiche candidate-specifiche future non serve ricostruire G_OSM o Speth: sarÃ  sufficiente collegare gli accessi reali/validati alla baseline appropriata e verificare localmente la percorribilitÃ  richiesta.

## 10. Implicazione per ISS-0004

Il fatto originario della Chat 3.3 resta corretto: il solo F3_SRC_FVG_ROADGRAPH_001 regionale non Ã¨ una rete Light/Heavy di produzione validata.

Tuttavia DEC-0054 modifica la necessitÃ  operativa: il 5 HUB non deve dipendere da quel grafo per costruire da zero il sistema traffico.

Le baseline alternative giÃ  esistenti coprono Light come rete/path macro + domanda provvisoria macro; Heavy come domanda + path-flow + corridoi macro; l'accessibilitÃ  locale resta una verifica separata sui candidati/finalisti.

**Raccomandazione Chat 3.10 per ISS-0004: PROPOSE_RESOLVED_PROCEDURALLY.**

La proposta non dichiara il grafo regionale idoneo e non elimina la verifica locale. Rimuove invece il blocker region-wide perchÃ© la metodologia approvata non richiede piÃ¹ una nuova rete regionale Light/Heavy. La decisione finale compete alla Chat 0.2 / utente.

## 11. DATA_REGISTRY e duplicazione

Si propone di registrare per riferimento, senza duplicare dati pesanti: G_OSM/Gamma_OSM; OD_PATH_SYSTEM_OSM; LIGHT_DIRTY_OD_v01; Heavy 6.0 Speth/ETISplus.

Metodo: reference-by-manifest + SHA-256 + path, con stato 5 HUB REVIEW fino alla review della Chat 0.2. Nessuna nuova copia pesante Ã¨ necessaria in 5_HUB_FVG\02_external_sources\F3_CHAT_3_10.

## 12. Quality gate

- provenance e status tesi verificabili: PASS;
- separazione rete / domanda / path-flow / locale: PASS;
- Light 46.010 OD e k=0,15: PASS;
- stato provvisorio Light preservato: PASS;
- Heavy truck flows e /365: PASS;
- limiti Heavy preservati: PASS;
- nessuna nuova calibrazione: PASS;
- nessun artifact FROZEN modificato: PASS;
- nessuna Fase 4 aperta: PASS;
- integrity: PASS WITH LIMITATION per mismatch della sola preservation copy G_OSM in TESI_BASELINE_SAFE; due copie hash-corrette disponibili.

**Esito tecnico Chat 3.10: PASS WITH LIMITATIONS.**

**Preservation issue correlata:** ISS-0014 = OPEN.
