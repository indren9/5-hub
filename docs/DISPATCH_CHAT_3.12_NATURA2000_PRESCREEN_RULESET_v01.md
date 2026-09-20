# DISPATCH — Chat 3.12 — Natura 2000: pre-screening operativo

**Fase:** 3 — Inventario e validazione dei dati
**Data:** 2026-09-20
**Stato mandato:** AUTHORIZED
**Regia:** Chat 0.2 — Chat Madre 5 HUB
**Issue principale:** ISS-0013
**Decisione vincolante:** DEC-0041

## 1. Obiettivo

Trasformare le prevalutazioni regionali Natura 2000 vigenti, le aree/criteri di interferenza funzionale e la verifica di corrispondenza in un **rule-set riproducibile** utilizzabile nelle fasi successive del progetto 5 HUB.

Il lavoro deve permettere al modello di distinguere, a scala di pianificazione macro, tra casi:
- potenzialmente coperti da prevalutazione regionale;
- che richiedono verifica di corrispondenza/condizioni;
- che richiedono screening VINCA specifico;
- per i quali le fonti disponibili non consentono una classificazione automatica affidabile.

La Chat 3.12 NON deve simulare una VINCA, NON deve dichiarare una VINCA superata e NON deve introdurre esclusioni automatiche basate sulla sola intersezione o distanza.

## 2. Baseline vincolanti

Repository:
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md`
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md`
- `docs/FASE_3_TERRITORIAL_ENVIRONMENTAL_VALIDATION_REVIEW_v01.md`
- `docs/FASE_3_TERRITORIAL_CONSTRAINT_ROLE_MATRIX_v01.csv`
- `docs/HANDOFF_CHAT_3.4_TERRITORIAL_CONSTRAINTS_v01.md`

Governance viva:
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER;
- DEC-0041;
- DEC-0059;
- ISS-0013;
- DATA_REGISTRY, in particolare `F3_SRC_FVG_NATURA_001`.

F1/F2 e DEC-0041 non devono essere riaperti.
## 3. Regola metodologica già approvata — DEC-0041

È già APPROVATO che:

1. semplice intersezione o vicinanza a ZSC/ZPS/pSIC/SIC NON produce esclusione automatica;
2. il modello esegue un pre-screening territoriale usando:
   - siti Natura 2000;
   - aree/criteri di interferenza funzionale;
   - criteri regionali vigenti;
3. prima di classificare un caso come bisognoso di VINCA specifica, il modello verifica prioritariamente l'applicabilità delle prevalutazioni regionali e la relativa verifica di corrispondenza;
4. il modello può classificare la necessità di approfondimento, ma NON dichiarare autonomamente una VINCA formalmente superata;
5. esclusione solo se disciplina/misure applicabili o valutazione competente dimostrano incompatibilità;
6. nessuna penalizzazione automatica per sola distanza;
7. eventuali indicatori ecologici/scoring sono fuori da questa chat.

La Chat 3.12 deve IMPLEMENTARE fedelmente questa logica documentale, non modificarla.

## 4. Stato di partenza già validato

Chat 3.4 ha già verificato/materializzato:
- `SITI_PROT:SIC`: 66 feature;
- `SITI_PROT:ZPS`: 35 feature;
- 72 codici sito unici;
- 29 codici condivisi fra layer tecnico SIC/ZSC e ZPS;
- nomenclatura tecnica/legacy del typename `SIC`;
- geometrie in EPSG:6708;
- pagina istituzionale Natura 2000 corrente.

Percorso già disponibile:
`5_HUB_FVG\02_external_sources\F3_CHAT_3_4\fvg_wfs\`

Non duplicare questi dataset senza motivo.

Gap reale:
- prevalutazioni regionali correnti non strutturate;
- DGR/atti e allegati applicabili non ancora tradotti in regole machine-readable;
- aree/criteri di interferenza funzionale non codificati;
- verifica di corrispondenza non formalizzata;
- eventuali differenze sito-specifiche non mappate in un crosswalk.
## 5. Attività richieste

### A. Corpus normativo/procedurale corrente

1. acquisire e verificare la DGR regionale corrente richiamata da ISS-0013 (DGR 30/2026) e tutti gli allegati pertinenti;
2. verificare eventuali aggiornamenti/atti successivi vigenti alla data della chat;
3. acquisire linee guida, modulistica, prevalutazioni, misure/criteri regionali effettivamente necessari a interpretare la procedura;
4. distinguere chiaramente:
   - prevalutazione regionale;
   - verifica di corrispondenza;
   - screening VINCA specifico;
   - misure di conservazione;
   - eventuali aree/interferenze funzionali.

### B. Struttura del rule-set

Tradurre SOLO regole esplicite/supportate dalle fonti in una tabella machine-readable.

Campi minimi raccomandati:
- `rule_id`;
- `source_id`;
- `legal_basis`;
- `effective_date`;
- `site_scope` / `site_code` se applicabile;
- `project_or_activity_scope`;
- `spatial_condition`;
- `functional_interference_condition`;
- `required_conditions`;
- `correspondence_check_required`;
- `source_outcome`;
- `model_action`;
- `limitations`;
- `evidence_reference`.

Le etichette operative devono restare descrittive e conservative. Sono ammesse, se supportate dal corpus:
- `POTENTIALLY_COVERED_BY_PREASSESSMENT`;
- `CORRESPONDENCE_CHECK_REQUIRED`;
- `SPECIFIC_VINCA_SCREENING_REQUIRED`;
- `MANUAL_REVIEW_REQUIRED`;
- `NOT_DETERMINABLE_FROM_AVAILABLE_RULES`.

Non creare una categoria equivalente a “VINCA PASSED”.

### C. Interferenza funzionale

1. individuare se esistono geometrie ufficiali pubbliche di aree di interferenza funzionale;
2. se esistono, acquisirle/materializzarle con lineage/hash;
3. se non esistono come layer unico, ricostruire la logica SOLO se le fonti ufficiali la definiscono in modo deterministico e riproducibile;
4. NON inventare buffer, distanze o soglie;
5. se la regola è sito-specifica o richiede giudizio ecologico, codificarla come `MANUAL_REVIEW_REQUIRED`.

### D. Crosswalk sito-regole

Costruire un crosswalk tra i 72 codici sito già validati e:
- designazione corrente;
- eventuale prevalutazione/regola applicabile;
- eventuali misure/condizioni rilevanti;
- presenza/assenza di informazione di interferenza funzionale;
- livello di automatizzabilità del pre-screening.

Non duplicare geometrie se basta referenziarle per codice sito e hash/path della baseline 3.4.
## 6. Verifica di corrispondenza

La Chat 3.12 deve tradurre in procedura riproducibile ciò che le fonti chiamano verifica di corrispondenza.

Deve chiarire:
- quali informazioni sul progetto/intervento servono;
- quali condizioni devono coincidere con la fattispecie prevalutata;
- quali condizioni rendono la prevalutazione non applicabile;
- quando è necessario passare a screening VINCA specifico;
- quali campi saranno necessariamente UNKNOWN nella Fase 4 perché dipendono da dettagli progettuali non ancora definiti.

Regola fondamentale:
**UNKNOWN non deve essere trasformato automaticamente in VINCA necessaria né in prevalutazione applicabile.**

Se mancano dettagli progettuali sufficienti:
`CORRESPONDENCE_CHECK_REQUIRED` o `MANUAL_REVIEW_REQUIRED`, secondo la fonte.

## 7. Test del rule-set

Eseguire test riproducibili senza costruire candidati reali della Fase 4.

Usare:
- casi espliciti presenti negli atti/allegati; oppure
- fixture sintetiche chiaramente etichettate che testino i rami logici senza introdurre nuove regole.

Testare almeno:
1. caso chiaramente coperto da prevalutazione;
2. caso che fallisce una condizione di corrispondenza;
3. caso con interferenza funzionale esterna;
4. caso con informazione progettuale insufficiente;
5. caso senza regola applicabile.

Ogni output deve essere spiegabile tramite `rule_id` e fonte.
## 8. Vincoli

NON:
- eseguire una VINCA;
- dichiarare VINCA superata;
- definire buffer arbitrari;
- usare una distanza generica come proxy di incidenza;
- escludere automaticamente un candidato perché dentro/vicino a Natura 2000;
- inventare misure di conservazione;
- inferire condizioni ecologiche non esplicite;
- produrre scoring/pesi;
- introdurre penalizzazioni;
- costruire candidati della Fase 4;
- aprire la Fase 4;
- modificare geometrie FROZEN/validate della Chat 3.4.

## 9. Principio di proporzionalità

Il 5 HUB è una pianificazione macro.

Il rule-set deve servire a classificare **il livello di approfondimento necessario**, non a sostituire la valutazione competente.

Se una regola richiede dati progettuali che non saranno disponibili nella prima costruzione candidati, il modello deve mantenere un flag di approfondimento invece di simulare una risposta.

## 10. Storage e riproducibilità

Repository:
`C:\dev\5-hub`

Storage pesante:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_12\`

Branch:
`chat-3.12-natura2000-prescreen-ruleset`

Preferire reference-by-manifest agli artifact già presenti in F3_CHAT_3_4.

Materializzare in F3_CHAT_3_12 solo:
- atti/allegati nuovi;
- prevalutazioni;
- eventuali geometrie interferenza nuove;
- evidenze necessarie al rule-set;
- manifest/QA.
## 11. Output richiesti

Repository:
- `docs/FASE_3_NATURA2000_PRESCREEN_VALIDATION_REVIEW_v01.md`
- `docs/FASE_3_NATURA2000_RULESET_v01.csv`
- `docs/FASE_3_NATURA2000_SITE_RULE_CROSSWALK_v01.csv`
- `docs/HANDOFF_CHAT_3.12_NATURA2000_v01.md`
- script leggeri di acquisizione/parsing/QA se necessari.

OneDrive:
- fonti ufficiali materializzate;
- eventuali layer ufficiali nuovi;
- `source_manifest_v01.json`;
- QA evidence.

## 12. Quality gate

PASS tecnico solo se:
- corpus regionale vigente verificato;
- prevalutazioni effettivamente applicabili identificate;
- verifica di corrispondenza formalizzata senza reinterpretazione arbitraria;
- aree/criteri di interferenza funzionale trattati con fonte e lineage;
- rule-set machine-readable completo di source/evidence;
- crosswalk sui 72 codici sito prodotto oppure gap documentato puntualmente;
- UNKNOWN gestito esplicitamente;
- nessun esito “VINCA passed” prodotto dal modello;
- nessun buffer/soglia inventato;
- fixture/test dei principali rami logici PASS;
- artifact/hash/manifest completi;
- DATA_REGISTRY aggiornato;
- ISS-0013 aggiornata ma NON chiusa autonomamente;
- `git diff --check` PASS;
- branch pulito;
- Fase 4 NON aperta.

## 13. Stato finale richiesto

Concludere con una proposta per ISS-0013:
- `KEEP_OPEN`;
- `READY_WITH_LIMITATIONS`;
- `PROPOSE_RESOLVED`;
- `PROPOSE_RESOLVED_PROCEDURALLY`.

La Chat 3.12 si ferma dopo il quality gate.

La review e l'eventuale chiusura di ISS-0013 competono alla Chat 0.2 / utente.
