# HANDOFF — Chat 90.5 — Audit stralci relazione e integrazione MODEL_v2

**Data:** 2026-09-21
**Chat:** 90.5 — Audit stralci relazione e integrazione MODEL_v2
**Regia:** Chat 0.2 — Chat Madre 5 HUB
**Worktree:** `C:\dev\5-hub\_worktrees\chat-90.5-relation-audit`
**Branch:** `chat-90.5-relation-audit`
**Stato finale della chat:** `REVIEW — STOP FOR CHAT 0.2`

## 1. Obiettivo

Auditare gli stralci di relazione forniti dall'utente senza assumerli come autorevoli, scomponendoli in claim atomici e confrontandoli con MODEL_v2, governance viva e fonti esterne aggiornate per AFIR e Monfalcone Lisert.

Il mandato vietava di:
- modificare governance;
- approvare nuove scelte metodologiche;
- scrivere il prompt Claude finale.

## 2. Input letti

Letti integralmente:
- `docs/DISPATCH_CHAT_90.5_RELATION_AUDIT_v01.md`;
- `docs/INPUT_RELATION_EXCERPTS_USER_20260921_v01.md`.

Baseline locali consultate:
- `docs/PROJECT_MODEL_CONTRACT_REBASELINE_v01.md`;
- `docs/ROADMAP_METODOLOGICA_v2.md`;
- `docs/FASE_1_HUB_DEFINITION_REBASELINED_v03.md`;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md`;
- `docs/CANDIDATE_UNIVERSE_CONTRACT_v01.md`;
- `docs/DQ01_APPROVAL_v01.md`;
- `docs/REBASELINE_APPROVAL_AND_PHASE3_CLOSE_v01.md`.

Governance viva verificata su Google Drive:
- `PROJECT_SOURCE_OF_TRUTH` — MODEL_v2 operativo;
- `PROJECT_CONTROL_REGISTER / DECISIONS` — verificato fino a DEC-0066;
- nessuna DEC-0067/0068 presente al momento della verifica;
- DQ-02 e successive non risultano approvate.

## 3. Lavoro svolto

### 3.1 Atomizzazione e classificazione

Sono stati classificati **114 claim** con la tassonomia richiesta:
- `KEEP`: 55;
- `ADAPT`: 18;
- `SUPERSEDED`: 16;
- `CONFLICT`: 2;
- `NEW_INFORMATION`: 19;
- `EDITORIAL_ONLY`: 1;
- `DUPLICATE`: 3.

Ogni claim contiene almeno:
- fonte/sezione;
- natura del claim;
- status audit;
- riferimento corrente di progetto;
- conflitto/cambiamento;
- necessità di verifica esterna;
- raccomandazione;
- necessità di decisione utente;
- effetto downstream.

### 3.2 Coda delle novità

Sono stati separati **20 elementi realmente nuovi** in `RELATION_NEW_INFORMATION_QUEUE_v01.csv`, distinguendo:
- requisiti confliggenti con baseline FROZEN;
- requisiti utente/commessa da integrare;
- proposte metodologiche non approvate;
- fatti esterni verificati;
- gap di verifica esterna;
- requisiti della futura pipeline Claude.

## 4. Findings principali

### 4.1 BESS ed elettrolizzatore

- **BESS obbligatorio in ogni Hub = CONFLICT**: non fa parte del nucleo minimo Fase 1 FROZEN.
- **Elettrolizzatore obbligatorio in ogni Hub = CONFLICT**: contrasta con F1-D6/DEC-0011, che non predefinisce l'architettura H2.
- Nessuno dei due è stato promosso a requisito corrente.

### 4.2 Scoring

Le seguenti proposte sono state mantenute esclusivamente come `METHODOLOGY_PENDING_DECISION`:
- pesi interi 1–5;
- min-max [0,1];
- somma pesata;
- specifici indicatori di accessibilità, domanda, flussi, energia e infrastrutture H2.

Riferimento decisionale:
- DQ-04 normalizzazione;
- DQ-05 pesi;
- DQ-06 aggregazione score;
- DQ-02/DQ-03 definizione indicatori e ruoli.

### 4.3 Configurazione dei cinque Hub

Restano non approvati:
- cinque macro-aree;
- bilanciamento per lunghezza TEN-T;
- bilanciamento per quota addetti manifatturieri;
- un Hub per macro-area;
- preselezione top-10/top-5;
- enumerazione condizionata 100.000 / 3.125 combinazioni;
- distanza minima 10 km tra Hub.

La distanza 10 km tra Hub è stata classificata come **requisito utente/commessa nuovo**, separato dai 10 km AFIR dalla TEN-T exit, e richiede decisione DQ-07/DQ-08.

### 4.4 Routing / OSM

È stata classificata `SUPERSEDED` la formulazione storica secondo cui OSM sarebbe solo supporto/comparazione e dovrebbe ancora essere validato per uso operativo.

Baseline corrente:
- Light: `G_OSM_operativo` + `Gamma_OSM` + `OD_PATH_SYSTEM_OSM` FROZEN riusati a scala macro secondo DEC-0054/DEC-0055;
- Heavy: baseline Heavy 6.0 / Speth-ETISplus;
- accesso locale definitivo e restrizioni esecutive = post-model salvo futura regola GIS approvata.

### 4.5 Ambiente e finalisti

Sono stati mantenuti i principi già accettati: nessun hard/score automatico per semplice intersezione, PGRA non hard per sola pericolosità, PAI come riferimento, Natura 2000 pre-screen/flag, PPR check, prati stabili `DEROGA_REQUIRED`.

È stata rimossa l'idea che la penalizzazione dei prati stabili sia già approvata.

Le verifiche finali di proprietà, disponibilità commerciale, urbanistica definitiva, accesso locale definitivo, MW/punto/costo di connessione e due diligence autorizzativa sono state classificate `SUPERSEDED` come gate del core e riportate a `DEFER_POST_MODEL`.

## 5. Verifica AFIR

Fonte primaria usata:
`https://eur-lex.europa.eu/eli/reg/2023/1804/2026-01-08`

Verificato sul Regolamento (UE) 2023/1804, versione consolidata corrente al 08/01/2026:
- EV «lungo TEN-T»: rete o entro 3 km di distanza stradale dall'uscita più vicina;
- H2 «lungo TEN-T»: rete o entro 10 km di distanza stradale dall'uscita più vicina;
- entro 31/12/2030, sulla TEN-T **core**, stazioni H2 pubbliche a distanza massima 200 km;
- capacità cumulativa minima 1 t/giorno;
- almeno un dispenser 700 bar;
- il target dell'art. 6 non va esteso automaticamente alla comprehensive.

Applicazione MODEL_v2:
- F1-D2/DEC-0007 resta il filtro metodologico: le specifiche AFIR H2 non sono universali per tutti i cinque Hub, ma valgono per gli Hub cui venga assegnata la relativa funzione;
- ruolo HARD/SOFT/configuration constraint resta pendente.

## 6. Verifica Monfalcone Lisert

Fonti principali:
- APT EcoMove: `https://www.aptgorizia.it/gli-impianti-apt-ecomove/`;
- APT 2026: `https://www.aptgorizia.it/apt-news/assemblea-dei-soci-crescita-transizione-ecologica/`;
- NAHV Testbed Catalogue May 2025: `https://www.nahv.eu/wp-content/uploads/2025/05/NAHV-testbeds-catalogue-may-2025.pdf`;
- Prefettura Gorizia 13/11/2025: `https://prefettura.interno.gov.it/it/prefetture/gorizia/notizie/vigilanza-e-tutela-legalita-e-trasparenza-nei-lavori-pubblici`;
- FVG Energia 2026: `https://prod-energia.regione.fvg.it/notizie/article/Mobilita-sostenibile-incontro-con-Apt-Goriziabr--sullo-sviluppo-delle-stazioni-multienergia/`.

Fatti verificati:
- APT Gorizia;
- nuova sede/area operativa in zona industriale Monfalcone Lisert, accesso da via Consiglio d'Europa;
- elettrolizzatore + produzione/distribuzione H2 + fotovoltaico;
- produzione pubblicata: **400 kg H2/giorno**;
- dispenser: **2 × 350 bar + 1 × 700 bar**;
- stato 2026: lavori in fase avanzata/realizzazione; **operatività/commissioning non verificata al 21/09/2026**.

Conclusione audit:
- Monfalcone può entrare come `VERIFIED_NEW_FACT / CONTEXT`;
- non può essere conteggiata automaticamente come copertura AFIR;
- 400 kg/giorno è produzione, non prova della capacità cumulativa di rifornimento AFIR;
- accessibilità pubblica, commissioning e relazione con TEN-T core restano da verificare se il configuration contract le richiede;
- non è stata presa alcuna decisione sul fatto che Monfalcone conti come uno dei cinque Hub.

## 7. Artifact creati

1. `docs/RELATION_CLAIM_AUDIT_MATRIX_v01.csv`
2. `docs/RELATION_INTEGRATION_RECOMMENDATIONS_v01.md`
3. `docs/RELATION_NEW_INFORMATION_QUEUE_v01.csv`
4. `docs/CLAUDE_PIPELINE_REQUIREMENTS_INPUT_v01_PROPOSED.md`
5. `docs/HANDOFF_CHAT_90.5_RELATION_AUDIT_v01.md`

Il quarto file è il pacchetto ripulito richiesto per la futura costruzione del prompt Claude e contiene esattamente le sezioni logiche:
- `BASELINE_ACCEPTED`;
- `USER_REQUIREMENT_PENDING_INTEGRATION`;
- `VERIFIED_NEW_FACT`;
- `METHODOLOGY_PENDING_DECISION`;
- `DO_NOT_USE_SUPERSEDED`.

## 8. Controlli eseguiti

- CSV matrix parse via PowerShell `Import-Csv`: PASS, 114 record.
- CSV queue parse via PowerShell `Import-Csv`: PASS, 20 record.
- Claim ID univoci: PASS, 0 duplicati.
- Campi obbligatori della matrice: PASS, 0 null/blank nei campi verificati.
- Status audit ammessi: PASS, 0 status fuori tassonomia.
- `git diff --cached --check` sugli artifact principali: PASS dopo correzione trailing whitespace.
- Nessuna governance modificata: PASS.
- Nessuna nuova DQ approvata dalla Chat 90.5: PASS.
- Nessun prompt Claude finale scritto: PASS.

## 9. Git

Commit artifact principali:
`c005406bac8969357deb0442c1cf6e60b48c9c22` — `docs: audit relation excerpts for MODEL_v2`

Il presente handoff viene committato separatamente nella chiusura della chat; il relativo hash non è auto-riferito nel file e viene riportato nel messaggio finale della Chat 90.5.

## 10. Questioni aperte da sottoporre a Chat 0.2 / utente

1. BESS obbligatorio sì/no.
2. Elettrolizzatore obbligatorio sì/no, con eventuale successor decision F1-D6.
3. Ruolo operativo AFIR/TEN-T.
4. Scoring: pesi 1–5, min-max, somma pesata.
5. Indicatori specifici DQ-02/DQ-03.
6. Cinque macro-aree e criteri di bilanciamento.
7. Vincolo uno-per-macro-area.
8. Top-10/top-5 come pre-screen.
9. Minimo 10 km tra Hub come configuration constraint.
10. Ruolo di Monfalcone Lisert nella copertura/configurazione.

## 11. Stato finale e prossimo passo

**Chat 90.5 = REVIEW / CLOSED OPERATIVELY.**

Prossimo passo: **review della Chat 0.2** sui cinque artifact. Nessuna delle scelte pendenti deve essere trattata come ACCEPTED prima della decisione esplicita dell'utente.

Dopo la review, il solo pacchetto `CLAUDE_PIPELINE_REQUIREMENTS_INPUT_v01_PROPOSED.md` potrà essere usato come base per una chat separata che costruisca il prompt Claude finale.

**STOP.**
