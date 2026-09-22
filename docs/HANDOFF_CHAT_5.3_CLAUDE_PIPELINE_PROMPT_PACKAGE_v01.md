# HANDOFF — CHAT 5.3 — PROMPT E PACKAGE PIPELINE CLAUDE MODEL_v2 v01

**Chat:** 5.3 — Prompt e package pipeline Claude MODEL_v2
**Data:** 2026-09-22
**Regia:** Chat 0.2 — Chat Madre 5 HUB
**Branch:** `chat-5.3-claude-pipeline-package`
**Core commit:** `5e98caa`
**Stato proposto:** REVIEW / BLOCKED_FOR_FINAL_ZIP

## 1. Obiettivo

Preparare:
1. prompt/input finale autosufficiente per la pipeline Claude esistente;
2. manifest minimale e tracciabile del package MODEL_v2;
3. procedura fail-closed di preflight/assembly;
4. ZIP finale solo dopo verifica di tutti gli input.

Non ridisegnare la metodologia approvata e non assegnare valori alle importanze dei criteri.

## 2. Lavoro svolto

- letto integralmente il dispatch Chat 5.3;
- usato il DOCX LIGHT fornito dall'utente come riferimento di struttura operativa;
- letti gli artifact metodologici MODEL_v2 richiesti dal dispatch;
- verificato lo stato vivo di PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER;
- inventariati e ispezionati gli artifact tecnici realmente disponibili;
- verificati layer, campi, CRS, cardinalità e hash degli input principali;
- costruito il prompt operativo finale in forma version-agnostic rispetto all'universo candidato;
- costruito un manifest di 14 righe dati, evitando duplicati e materiale storico/non operativo;
- implementato uno script fail-closed per hash, preflight, estrazione selettiva da ZIP e assembly;
- costruiti test automatici dedicati;
- eseguito il quality gate tecnico.

## 3. Prompt finale

Artifact:
`docs/INPUT_PIPELINE_CLAUDE_MODEL_v2_FVG_v01.md`

Il prompt traduce direttamente la metodologia consolidata in:
- file/input e loro semantica;
- formule dei sei criteri site-level;
- copertura territoriale della cinquina;
- funzione obiettivo unica;
- AFIR/TEN-T come gate separato dallo scoring;
- proxy progettuali Trieste/Udine;
- regola <=10 km stradali dalla nearest TEN-T exit;
- requisito massimo 200 km sulla TEN-T Core valutabile;
- trattamento Monfalcone/Lisert;
- output e QA;
- caveat e margine di manovra computazionale.

Non contiene riferimenti operativi a DEC, DQ, Chat o fasi interne.

Le importanze restano esattamente:
~~~text
LIGHT = ____
HEAVY = ____
GRID = ____
LOG = ____
PGRA = ____
H2 = ____
COVERAGE = ____
~~~

Nessun valore, esempio o default è stato assegnato.

## 4. Manifest package

Artifact:
`docs/CLAUDE_MODEL_v2_PACKAGE_MANIFEST_v01.csv`

Contiene 14 righe dati:
- 3 artifact candidati obbligatori ancora `BLOCKING_PENDING`;
- 11 artifact/ruoli già bindati a sorgenti reali e sottoposti a verifica di presenza/hash.

Scelte di minimalità:
- esclusa baseline Claude storica;
- escluse chat/governance completa;
- esclusi documenti superseded;
- esclusi raw/cache non necessari;
- esclusi output cartografici di sola presentazione non necessari;
- escluso il grande GeoPackage territoriale LIGHT come duplicato: il ruolo FVG_BOUNDARY usa il layer `fvg_boundary` già presente nel GeoPackage Heavy;
- dal package Heavy frozen viene estratto solo `HEAVY_PATH_FLOWS_v01.csv`, non l'intero ZIP.

## 5. Blocker candidato

ISS-0015 resta materialmente rilevante.

La build candidata v01:
- ha technical build PASS;
- contiene 3.993 candidati;
- resta REVIEW;
- non è accettabile come universo definitivo finché non viene chiusa la semantica urbanistica unresolved materialmente incidente.

La Chat 4.2 sta costruendo la nuova versione, ma al controllo Chat 5.3 non risultavano ancora materializzati:
- `CANDIDATE_UNIVERSE_v02.gpkg`;
- `CANDIDATE_LINEAGE_v02.csv`;
- machine QA v02.

Per questo il manifest non sostituisce v01 implicitamente e il package finale non è stato creato.

## 6. Script di package

Artifact:
`scripts/build_claude_model_v2_package_v01.py`

Funzioni principali:
- parsing del manifest;
- fail su qualsiasi row `BLOCKING_*`;
- verifica presenza;
- SHA-256;
- verifica hash del singolo membro quando la sorgente è uno ZIP;
- estrazione selettiva del solo membro richiesto;
- staging con i package path dichiarati;
- copia prompt + manifest risolto;
- creazione ZIP solo con flag `--build` e solo dopo preflight PASS.

Output finale previsto:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\07_deliverables\CLAUDE_MODEL_v2_PACKAGE_v01.zip`

## 7. Controlli eseguiti

Test:
`tests/test_claude_model_v2_prompt_package_v01.py`

Esito:
- pytest: **5 passed**;
- py_compile builder: **PASS**;
- `git diff --cached --check`: **PASS** prima del core commit;
- importanze vuote: **PASS**;
- assenza codici governance nel prompt: **PASS**;
- formule/vincoli core presenti: **PASS**;
- manifest = 14 righe dati, package path univoci: **PASS**.

Preflight package:
`PACKAGE_PREFLIGHT=FAIL` — **FAIL ATTESO / CORRETTO**.

Dopo le correzioni QA del manifest, le sole cause residue sono:
- CANDIDATE_UNIVERSE = BLOCKING_PENDING / source missing;
- CANDIDATE_LINEAGE = BLOCKING_PENDING / source missing;
- CANDIDATE_QA = BLOCKING_PENDING / source missing.

Non risultano altri errori sugli input già bindati.

## 8. File creati

Repository/worktree:
- `docs/INPUT_PIPELINE_CLAUDE_MODEL_v2_FVG_v01.md`;
- `docs/CLAUDE_MODEL_v2_PACKAGE_MANIFEST_v01.csv`;
- `docs/CLAUDE_MODEL_v2_PACKAGE_READINESS_v01.md`;
- `scripts/build_claude_model_v2_package_v01.py`;
- `tests/test_claude_model_v2_prompt_package_v01.py`;
- questo handoff.

Core commit:
`5e98caa — feat(chat-5.3): prepare Claude MODEL_v2 prompt package`

## 9. Stato del quality gate

- prompt autosufficiente: PASS;
- descrizione operativa degli input: PASS;
- importanze 1–5 non valorizzate: PASS;
- formule e vincoli consolidati trascritti: PASS;
- assunzioni progettuali separate dai requisiti normativi: PASS;
- requisito AFIR 200 km esplicito: PASS;
- manifest minimale e motivato: PASS;
- coerenza prompt/manifest: PASS;
- controlli e limitazioni espliciti: PASS;
- ZIP finale verificabile: **NOT EXECUTED — BLOCKED BY DEFINITIVE CANDIDATE UNIVERSE**.

**Esito Chat 5.3 corrente: REVIEW / BLOCKED_FOR_FINAL_ZIP.**

Il blocco è di readiness dell'input candidato, non un conflitto metodologico del MODEL_v2.

## 10. Prossimo passo

Dopo chiusura/review della Chat 4.2 e accettazione esplicita dell'universo candidati definitivo:
1. verificare path/nome effettivo di GPKG, lineage e machine QA;
2. sostituire nel manifest i tre binding placeholder;
3. inserire bytes, SHA-256 e stato effettivi;
4. rieseguire pytest e preflight;
5. se PASS, eseguire il builder con `--build`;
6. verificare contenuto ZIP, hash dello ZIP e corrispondenza col manifest;
7. riportare il package finale alla Chat 0.2 per review.

Non usare la v01 REVIEW come scorciatoia per sbloccare il package.
