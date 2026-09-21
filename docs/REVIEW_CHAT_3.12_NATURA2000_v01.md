# REVIEW — Chat 3.12 — Natura 2000: pre-screening operativo

**Reviewer:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Perimetro:** review indipendente tecnica; nessuna decisione di governance applicata
**Stato:** REVIEW_PASSED_WITH_LIMITATIONS — proposta specialistica supportata, in attesa di decisione utente/Chat 0.2

## 1. Esito sintetico

La review indipendente supporta il quality gate tecnico della Chat 3.12.

Il rule-set rispetta i guardrail di DEC-0041:
- nessuna esclusione o penalizzazione automatica per sola distanza/intersezione;
- nessun esito equivalente a VINCA_PASSED;
- il verde resta subordinato a verifica di corrispondenza;
- il rosso richiede screening specifico;
- gli UNKNOWN restano non determinati;
- le soglie di interferenza codificate sono source-defined e non inventate dal modello;
- Fase 4 non è stata aperta.

La proposta specialistica PROPOSE_RESOLVED_PROCEDURALLY per ISS-0013 è tecnicamente supportata, ma non viene applicata in questa review.

## 2. Verifica indipendente degli artifact

Verificati:
- docs/FASE_3_NATURA2000_PRESCREEN_VALIDATION_REVIEW_v01.md
- docs/FASE_3_NATURA2000_RULESET_v01.csv
- docs/FASE_3_NATURA2000_SITE_RULE_CROSSWALK_v01.csv
- docs/HANDOFF_CHAT_3.12_NATURA2000_v01.md
- scripts/build_natura2000_prescreen_ruleset_chat3_12_v01.py
- tests/test_natura2000_prescreen_ruleset_chat3_12_v01.py
- OneDrive F3_CHAT_3_12/source_manifest_v01.json
- evidence QA in F3_CHAT_3_12/qa/

Conteggi verificati indipendentemente:
- 3.634 regole totali;
- 3.600 righe SITE_ACTIVITY_PREASSESSMENT;
- 72 righe nel crosswalk e 72 site_code unici;
- 0 duplicati rule_id;
- 0 duplicati site_code;
- source outcomes SITE_ACTIVITY: 2.512 PREASSESSED_NO_SIGNIFICANT_INCIDENCE, 1.043 NOT_APPLICABLE, 40 SCREENING_REQUIRED, 5 UNKNOWN.

Le cinque righe UNKNOWN sono:
- IT3330009 / attività 3.06;
- IT3330010 / attività 3.06;
- IT3340006 / attività 3.06;
- IT3340007 / attività 3.06;
- IT3341002 / attività 3.06.

Sono mantenute come NOT_DETERMINABLE_FROM_AVAILABLE_RULES.

## 3. Test e ambiente

Durante la review, la .venv non conteneva inizialmente pytest né pandas.

Su richiesta dell'utente sono stati installati:
- pytest 9.1.1;
- pandas 3.0.6.

Il file tests/test_natura2000_prescreen_ruleset_chat3_12_v01.py è un runner standalone e non una suite pytest-discoverable:
- pytest: no tests ran;
- esecuzione diretta del file: 19 PASS / 0 FAIL.

Sono stati inoltre verificati:
- py_compile: PASS;
- git diff --check: PASS;
- branch specialistico pulito prima della presente review.

La dicitura corretta è quindi “runner automatico 19/19 PASS”, non “pytest 19/19 PASS”.

## 4. Manifest e hash

source_manifest_v01.json contiene 19 entry di fonte:
- 13 riferimenti con file locale;
- 6 pagine web ufficiali registrate come riferimenti web-only.

Controllo indipendente:
- 13/13 file locali presenti;
- 0 hash locali discordanti;
- 8/8 artifact generati presenti;
- 0 hash degli artifact generati discordanti.

Le 6 pagine web-only non sono file mancanti: sono riferimenti correnti non materializzati.

## 5. Verifica delle fonti ufficiali correnti

La verifica web indipendente del 2026-09-21 conferma:
- DGR 30 del 16 gennaio 2026 quale aggiornamento corrente delle prevalutazioni;
- sostituzione delle prevalutazioni approvate con DGR 119/2023;
- applicazione delle prevalutazioni nel rispetto delle misure di conservazione;
- permanenza della verifica di corrispondenza;
- uso di DGR 30/2026 per le aree di interferenza funzionale;
- disciplina sito-specifica della Laguna di Marano e Grado IT3320037 tramite DPReg 65/2025;
- misure di conservazione correnti DGR 1148/2024 e 1149/2024 per ZSC, DGR 594/2025 per ZPS e aggiornamento DGR 1760/2025 per IT3341002.

## 6. Cautela interpretativa sul giallo

La fonte ufficiale descrive il giallo come NOT_APPLICABLE / non pertinente: il P/I/A non è realizzabile per ragioni giuridiche o fisiche e, in tale fattispecie, non necessita di ulteriori valutazioni VINCA.

Il rule-set 3.12 mappa invece il giallo a MANUAL_REVIEW_REQUIRED.

La scelta è più conservativa della fonte ed è compatibile con il guardrail progettuale che vieta di trasformare automaticamente Natura 2000 in un hard filter senza verificare la disciplina concreta.

Deve però essere mantenuta semanticamente distinta:
- NOT_APPLICABLE è l'esito della fonte;
- MANUAL_REVIEW_REQUIRED è l'azione prudenziale del modello 5 HUB;
- non va presentata come obbligo normativo regionale di ulteriore review VINCA.

Questa cautela non costituisce blocker tecnico.

## 7. Limiti della review

La review indipendente non ha ripetuto una ispezione visuale manuale delle cinque celle bianche dell'Allegato A.3, già documentata dalla Chat 3.12. Il mantenimento conservativo a UNKNOWN rende comunque il caso fail-safe: nessuna classificazione favorevole o obbligo VINCA è inferito dal parser.

Non è stato eseguito alcun test su candidati reali, coerentemente con il mandato e con Fase 4 non aperta.

## 8. Conclusione

Esito review tecnica Chat 0.2:

**PASS WITH LIMITATIONS**

La proposta della Chat 3.12 di:
**PROPOSE_RESOLVED_PROCEDURALLY**

è supportata tecnicamente.

Nessuna delle seguenti azioni viene eseguita in questa review:
- chiusura di ISS-0013;
- nuova decisione DEC;
- promozione del DATA_REGISTRY da REVIEW;
- merge su main;
- apertura della Fase 4.

Tali azioni restano sospese in attesa delle successive indicazioni dell'utente.
