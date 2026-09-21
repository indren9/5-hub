# DISPATCH — Chat 90.5 — Audit stralci relazione e integrazione MODEL_v2

**Mandante:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Stato:** AUTHORIZED — AUDIT ONLY
**Branch:** `chat-90.5-relation-audit`

## 1. Scopo

Analizzare gli stralci di relazione e i requisiti aggiuntivi forniti dall'utente per stabilire, elemento per elemento, cosa:
- è già coerente con il MODEL_v2;
- deve essere adattato;
- è stato superato;
- confligge con decisioni correnti;
- costituisce informazione nuova da verificare/approvare;
- è solo contenuto editoriale.

Questa chat NON deve modificare autonomamente metodologia, Source of Truth, DEC, FROZEN, DQ o roadmap.

## 2. Input primario

Leggere integralmente:

`docs/INPUT_RELATION_EXCERPTS_USER_20260921_v01.md`

Stato dell'input:
**SOURCE INPUT / NON AUTHORITATIVE / DA AUDITARE**.

Il materiale fornito dall'utente può contenere contemporaneamente fatti utili, formulazioni storiche, assunzioni, requisiti di commessa e decisioni metodologiche non ancora approvate.

## 3. Baseline autorevoli da confrontare

Verificare almeno:
- PROJECT_SOURCE_OF_TRUTH vivo;
- PROJECT_CONTROL_REGISTER vivo;
- `docs/PROJECT_MODEL_CONTRACT_REBASELINE_v01.md`;
- `docs/ROADMAP_METODOLOGICA_v2.md`;
- `docs/FASE_1_HUB_DEFINITION_REBASELINED_v03.md`;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md`;
- `docs/CANDIDATE_UNIVERSE_CONTRACT_v01.md`;
- `docs/DQ01_APPROVAL_v01.md`;
- `docs/REBASELINE_APPROVAL_AND_PHASE3_CLOSE_v01.md`;
- DEC-0061…DEC-0066 e decisioni precedenti materialmente pertinenti;
- DATA_REGISTRY e ISSUES pertinenti.

Se durante il lavoro V2-1/Chat 4.2 è ancora in corso, non assumerne gli output REVIEW come baseline approvata.

## 4. Unità di analisi

NON classificare automaticamente un intero paragrafo con una sola etichetta.

Spezzare il materiale in **claim/requisiti atomici**, ciascuno comprensibile da solo.

Esempio:
un paragrafo può contenere una parte KEEP e una parte SUPERSEDED.

## 5. Tassonomia obbligatoria

Per ogni claim assegnare uno dei seguenti stati:

- `KEEP` — coerente e già supportato dalla governance corrente;
- `ADAPT` — concetto utile ma formulazione/ruolo/fase deve essere riallineata;
- `SUPERSEDED` — sostituito da decisione o baseline successiva;
- `CONFLICT` — incompatibile con una decisione corrente e richiede decisione utente se si vuole reintrodurlo;
- `NEW_INFORMATION` — informazione nuova potenzialmente utile, da verificare e poi eventualmente integrare;
- `EDITORIAL_ONLY` — utile alla relazione ma senza effetto metodologico/operativo;
- `DUPLICATE` — contenuto già pienamente rappresentato altrove senza valore aggiunto.

Aggiungere `VERIFY_EXTERNAL` come flag separato quando la verità fattuale dipende da normativa, infrastruttura, progetto o fonte esterna corrente.

## 6. Distinzioni obbligatorie

Per ogni claim indicare anche la natura:
- FACT_OBSERVED;
- USER_REQUIREMENT / REQUIREMENT_OF_COMMISSION;
- REGULATORY_REQUIREMENT;
- DESIGN_CHOICE;
- METHODOLOGICAL_CHOICE;
- ASSUMPTION;
- PROXY;
- EDITORIAL_DESCRIPTION.

Non trasformare una frase della relazione in un fatto solo perché è scritta in forma assertiva.

## 7. Temi da auditare esplicitamente

### Identità funzionale Hub
Verificare in particolare:
- H2 pubblico;
- DC EV Light/Heavy;
- BESS;
- elettrolizzatore;
- FER;
- architettura approvvigionamento H2.

### Universo candidati
Confrontare con DQ-01 già ACCEPTED:
- categorie urbanistiche;
- split/merge;
- soglia 8.000 m²;
- CRS;
- ID/versioning;
- hard prefilter.

### Ammissibilità
Auditare:
- incompatibilità urbanistica;
- accesso stradale adeguato;
- AFIR/TEN-T come eventuale HARD;
- momento della verifica puntuale.

### Scoring
Auditare senza approvare:
- pesi interi 1–5;
- min-max obbligatorio;
- somma pesata;
- criteri proposti;
- ruolo della fattibilità energetica;
- infrastrutture H2 preesistenti.

Confrontare con DQ-02…DQ-06 ancora non approvate.

### Configurazione dei 5 Hub
Auditare senza approvare:
- 5 macro-aree;
- criterio di bilanciamento per lunghezza TEN-T;
- criterio di bilanciamento per addetti manifatturieri;
- un Hub per macro-area implicito;
- top 10 o top 5 per macro-area;
- enumerazione 10^5 / 5^5;
- distanza minima 10 km;
- copertura AFIR;
- funzione obiettivo.

Confrontare con DQ-07…DQ-09 ancora non approvate.

### AFIR
Verificare su fonte normativa corrente:
- definizione di infrastruttura “lungo TEN-T”;
- 10 km H2;
- 3 km EV se richiamato;
- 200 km H2;
- rete core vs comprehensive;
- 1 t/giorno;
- 700 bar;
- scadenza 31/12/2030;
- corretta applicabilità al modello e alla configurazione.

Separare sempre normativa AFIR da requisito di commessa dei 10 km tra Hub.

### Monfalcone Lisert
Verificare esternamente:
- esistenza/stato del progetto;
- localizzazione;
- soggetto;
- capacità 400 kg H2/giorno;
- 2×350 bar;
- 1×700 bar;
- stato programmato/in costruzione/operativo;
- se può ragionevolmente concorrere a copertura AFIR o solo essere infrastruttura di contesto.

NON decidere autonomamente se conta come uno dei cinque Hub o come copertura della configurazione.

### Routing e TEN-T
Individuare formulazioni storiche ormai superate da:
- switch OSM;
- Gamma_OSM / OD path frozen;
- validazione TEN-T già eseguita.

### Ambiente/territorio
Confrontare PGRA, PAI, Natura 2000, PPR, parchi/riserve/biotopi/prati stabili con le decisioni già assunte e il rebaseline MODEL_v2.

### Verifiche finalisti
Confrontare accesso, proprietà, urbanistica puntuale, connessione energetica, ecc. con il passaggio a DEFER_POST_MODEL.

## 8. Ricerca esterna

Usare fonti web aggiornate quando serve verificare:
- AFIR;
- stato Monfalcone Lisert;
- eventuali dati normativi/progettuali contemporanei.

Preferire fonti primarie o istituzionali.

Non usare la ricerca web per sostituire le baseline private del progetto.

## 9. Output obbligatori

Produrre:

1. `docs/RELATION_CLAIM_AUDIT_MATRIX_v01.csv`

Campi minimi:
- claim_id;
- source_section;
- source_excerpt_short;
- claim_summary;
- claim_nature;
- audit_status;
- current_project_reference;
- conflict_or_change;
- external_verification_required;
- external_source;
- recommendation;
- user_decision_required;
- downstream_effect;
- notes.

2. `docs/RELATION_INTEGRATION_RECOMMENDATIONS_v01.md`

Deve spiegare in forma semplice:
- cosa integrare subito;
- cosa integrare riscrivendo;
- cosa non usare;
- quali elementi richiedono nuova decisione utente;
- quali elementi vanno verificati esternamente.

3. `docs/RELATION_NEW_INFORMATION_QUEUE_v01.csv`

Solo elementi realmente nuovi, con stato di verifica.

4. `docs/CLAUDE_PIPELINE_REQUIREMENTS_INPUT_v01_PROPOSED.md`

Questo NON è il prompt finale Claude.
È il pacchetto ripulito delle sole informazioni che, dopo audit, potrebbero alimentare il futuro prompt.

Separare:
- BASELINE_ACCEPTED;
- USER_REQUIREMENT_PENDING_INTEGRATION;
- VERIFIED_NEW_FACT;
- METHODOLOGY_PENDING_DECISION;
- DO_NOT_USE_SUPERSEDED.

5. `docs/HANDOFF_CHAT_90.5_RELATION_AUDIT_v01.md`

## 10. Divieti

Non:
- aggiornare Source of Truth;
- creare nuove DEC;
- cambiare stati ACCEPTED/FROZEN;
- modificare DQ-01;
- approvare DQ-02…DQ-10;
- scrivere il prompt Claude definitivo;
- modificare la relazione finale;
- importare in blocco gli stralci come metodologia corrente.

## 11. Quality gate

PASS se:
- tutti i claim sostanziali sono classificati;
- conflitti e superseded hanno riferimento esplicito alla baseline corrente;
- informazioni nuove sono separate dalle decisioni metodologiche;
- AFIR e Monfalcone sono verificati con fonti adeguate quando possibile;
- nessuna scelta pendente viene spacciata per approvata;
- il pacchetto per Claude contiene solo informazioni ripulite e marcate per stato;
- git diff --check PASS;
- branch pulito e pushato.

Poi STOP per review Chat 0.2 e decisioni utente.
