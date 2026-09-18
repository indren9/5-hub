# HANDOFF â€” Chat 3.7 â€” Crosswalk TEN-T FVG e rilevanza delle uscite AFIR

**Data:** 2026-09-18
**Stato finale Chat 3.7:** PASS tecnico-operativo / REVIEW Chat Madre richiesta
**Stato FASE 3:** IN CORSO â€” NON CLOSED, NON FROZEN
**Regia:** Chat Madre 5 HUB
**Branch Git:** `chat-3.7-tent-crosswalk`

## 1. Obiettivo

Completare il crosswalk route-level corrente della rete stradale TEN-T in Friuli Venezia Giulia sui tre livelli:
- Core;
- Extended Core;
- Comprehensive;

e verificare se esista almeno un tratto TEN-T FVG senza vera uscita/rampa e con intersezioni ordinarie a raso tale da rendere materialmente necessario risolvere Q-METH-3.3-A sulla â€œnearest TEN-T exitâ€ AFIR.

Vincoli rispettati:
- FASE 1 e FASE 2 non riaperte;
- nessun candidato costruito;
- nessuna distanza candidatoâ€“TEN-T calcolata;
- nessun `TENT_EXIT_SET_v01` definitivo costruito;
- nessuna decisione metodologica o issue chiusa autonomamente;
- OSM utilizzato solo come supporto geometrico/topologico.

## 2. Baseline e governance

Letti integralmente:
- `docs/DISPATCH_CHAT_3.7_TENT_CROSSWALK_EXIT_RELEVANCE_v01.md`;
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md`;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md`;
- `docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md`;
- `docs/FASE_3_ROAD_TENT_VALIDATION_REVIEW_v01.md`;
- `docs/FASE_3_TENT_EXIT_RELEVANCE_SCREENING_v01.md`.

Verificati live su Google Drive:
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER;
- DEC-0034;
- ISS-0005.

ISS-0005 risultava e resta **OPEN**.

## 3. Lavoro svolto

### 3.1 Fonte TEN-T corrente

Ãˆ stato individuato il servizio pubblico corrente DG MOVE / TENtec:
`https://tentec.transport.ec.europa.eu/api/public/gis/TENT_Regulation_2024/MapServer`

Il servizio dichiara il Reg. (UE) 2024/1679 e contiene:
- Roads / Core = layer 8;
- Roads / Extended Core = layer 9;
- Roads / Comprehensive = layer 10.

La fonte Ã¨ stata materializzata con metadati e subset FVG in OneDrive.

### 3.2 Crosswalk route-level

Script:
`scripts/build_tent_fvg_crosswalk_chat3_7_v01.py`

Output:
`05_intermediate_outputs\F3_CHAT_3_7\TENT_FVG_ROUTE_CROSSWALK_v01.csv`

Risultato:
- 9 sezioni CORE;
- 0 sezioni EXTENDED CORE;
- 2 sezioni COMPREHENSIVE-only;
- totale 11 sezioni materialmente intersecanti FVG.

Strade reali FVG:
- A4;
- A23;
- RA13;
- RA14;
- A/SS202;
- A28.

A28 Ã¨ lâ€™unico asse comprehensive-only emerso rispetto allo screening core/corridoi della Chat 3.7 preliminare.

Il parametro <=100 m nello script Ã¨ solo QA del crosswalk geometrico, non una soglia metodologica del modello.

### 3.3 Audit morfologia accessi

Script:
`scripts/build_tent_exit_relevance_audit_chat3_7_v01.py`

Output:
`05_intermediate_outputs\F3_CHAT_3_7\TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv`

Sono stati verificati:
- A4: autostrada, accessi mediante svincoli;
- A23: autostrada, accessi mediante uscite/svincoli;
- RA13: tratto a carreggiate separate, documentazione ANAS per svincoli + supporto topologico OSM frozen;
- RA14: tratto a livelli separati/svincoli, documentazione ANAS + supporto OSM frozen;
- A/SS202: sezioni descritte da ANAS tramite svincoli; supporto OSM conferma struttura link/rampa nel caso isolato;
- A28: autostrada Portogruaroâ€“Conegliano con elenco corrente di svincoli autostradali;
- Extended Core: nessun tratto FVG corrente.

Non Ã¨ stato identificato alcun tratto TEN-T FVG corrente in cui lâ€™unico accesso pertinente sia una normale intersezione a raso priva di vera uscita/rampa.

## 4. Esito Q-METH-3.3-A

**Risultato tecnico:** il problema interpretativo della â€œnearest TEN-T exitâ€ sui tratti TEN-T non a accesso controllato **non risulta materialmente necessario nel dominio stradale TEN-T FVG corrente osservato**.

Questo risultato:
- non inventa una definizione alternativa di exit;
- non chiude Q-METH-3.3-A autonomamente;
- non chiude ISS-0005;
- deve essere verificato dalla Chat Madre.

## 5. Artifact creati

### Git â€” codice e documentazione leggera

- `scripts/build_tent_fvg_crosswalk_chat3_7_v01.py`
- `scripts/build_tent_exit_relevance_audit_chat3_7_v01.py`
- `docs/FASE_3_TENT_CROSSWALK_VALIDATION_REVIEW_v01.md`
- `docs/HANDOFF_CHAT_3.7_TENT_CROSSWALK_v01.md`

### OneDrive â€” fonti ed evidenze

Root:
`C:\Users\visen\OneDrive\UniversitÃ \UniUD\Tesi\5_HUB_FVG`

TEN-T current:
`02_external_sources\F3_CHAT_3_7\TEN_T\`

Operator evidence:
`02_external_sources\F3_CHAT_3_7\operator_evidence\`

Output:
- `05_intermediate_outputs\F3_CHAT_3_7\TENT_FVG_ROUTE_CROSSWALK_v01.csv`
- `05_intermediate_outputs\F3_CHAT_3_7\TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv`

Manifest:
- `02_external_sources\F3_CHAT_3_7\evidence_manifest_v01.json`

## 6. Hash principali

- Crosswalk: `1AAAAC6EB9E74CF0C86BD6BB31FBF2FD6390547956D5148F958477A54EADFEBF`
- Exit relevance audit: `8FDCA0E64B4A3DB24E4184412E7FC3175C650D371A0633E8B5FDC54B7D34D1A6`
- TENtec service metadata: `908E76799CCCEB2D1DE05A91CCCA2A5A236D37A349BA3F54D942B4B06A3493E4`
- TENtec Core subset: `B397912C6E3ED3D21FC4F4FBB4B7C383533DA2C947237D094DFA81CFAFF043BA`
- TENtec Extended Core subset: `C3311FCCB903EE2126AF2CF493ED98DAA5DAA7B7962F5344A25E397E46CBD3C4`
- TENtec Comprehensive subset: `1A44F76B37029B30FD14F08D89EE6079892995DD3FE4CC5ABC8C63BBFE9737DB`
- ANAS evidence: `D15EB8B9708809259B9AC4C1AB825010CAB105B8AA32B98115472755FDDE6FFC`
- Autostrade Alto Adriatico HTML: `22C6ED432B16739F3143FB325FC70BF3F3E9CFF3A609CA1EB942AD7CE9CA2B56`
- MIT evidence: `2C5BA39A7F22FEB273A25D4C43CC59C32C9CB96AEABB1195BD5E4AB39897F8C4`

## 7. Governance aggiornata

PROJECT_CONTROL_REGISTER aggiornato in-place:
- `F3_SRC_TENTEC_001`: resta REVIEW; nota aggiornata con fonte corrente e crosswalk;
- `ISS-0005`: resta OPEN; prossima azione aggiornata con esito Chat 3.7 e obbligo di review Chat Madre.

PROJECT_SOURCE_OF_TRUTH:
- non modificato;
- eventuale consolidamento compete alla Chat Madre/utente.

Nessun elemento sostanziale Ã¨ stato promosso ad ACCEPTED/FROZEN da questa chat.

## 8. Quality gate

- dispatch e baseline: PASS;
- governance viva: PASS;
- fonte corrente 3-tier: PASS;
- crosswalk route-level completo FVG: PASS;
- Core: PASS;
- Extended Core: PASS â€” assenza verificata;
- Comprehensive-only: PASS;
- mapping verso strade reali FVG: PASS;
- distinzione controlled access / intersezioni ordinarie a raso: PASS;
- rilevanza Q-METH-3.3-A dimostrata/bounded senza scelta implicita: PASS;
- OSM solo supporto: PASS;
- storico Claude / 23 exit non promosso: PASS;
- definitive exit set non costruito: PASS;
- registri aggiornati senza chiusura issue: PASS;
- artifact + hash: PASS;
- review indipendente Chat Madre prima di chiudere ISS-0005: PENDING / REQUIRED.

**Quality gate Chat 3.7: PASS tecnico-operativo.**

## 9. SESSION CLOSE â€” change-driven

**NOTEBOOK_CHANGE = NO**
Nessun notebook autorevole coinvolto.

**REGISTER_CHANGE = YES**
DATA_REGISTRY e ISSUES aggiornati con esiti tecnici; ISS-0005 resta OPEN.

**GIT_COMMIT_REQUIRED = YES**
Sono stati creati script riproducibili e documentazione tecnica.

**PROJECT_SOURCE_OF_TRUTH_CHANGE = NO**
Nessuna decisione sostanziale viene approvata autonomamente; consolidamento rimesso alla Chat Madre/utente.

Artifact check:
- nessun artifact FROZEN sovrascritto;
- fonti pesanti/output su OneDrive;
- codice/docs in Git;
- hash registrati;
- nessun `TENT_EXIT_SET_v01` prodotto;
- nessun candidato o distanza candidatoâ€“TEN-T prodotto.

## 10. Problemi / dipendenze aperte

1. ISS-0005 resta formalmente OPEN fino alla review della Chat Madre.
2. Q-METH-3.3-A puÃ² essere proposta come non materialmente rilevante nel dominio FVG corrente, ma la disposizione finale compete alla regia/utente.
3. La costruzione del futuro `TENT_EXIT_SET_v01` resta attivitÃ  successiva e non autorizzata da questo mandato.
4. ISS-0004 resta separatamente OPEN: le future distanze stradali AFIR non devono usare routing diretto non validato.
5. Eventuali revisioni future TEN-T richiederanno nuova versione del crosswalk.

## 11. Git

Commit operativo Chat 3.7: `829361b782715829b930ed6ddd94157048d74f44` — `feat(fase3): complete TEN-T FVG crosswalk and exit relevance audit`.

## 12. Stato finale e prossimo passo

**Chat 3.7: PASS tecnico-operativo / pronta per review indipendente della Chat Madre.**

Prossimo passo:
1. Chat Madre verifica script, fonti, CSV, hash e conclusione di materialitÃ ;
2. solo dopo review decide la disposizione di ISS-0005 e di Q-METH-3.3-A;
3. non costruire ancora il definitivo `TENT_EXIT_SET_v01`;
4. non avviare calcoli di distanza AFIR su routing diretto finchÃ© ISS-0004 non Ã¨ risolto.
