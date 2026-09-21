# FASE 3 — NATURA 2000 PRESCREEN VALIDATION REVIEW v01

**Chat:** 3.12 — Natura 2000: pre-screening operativo  
**Data di verifica:** 2026-09-21  
**Stato:** REVIEW — proposta di PASS tecnico con limitazioni, soggetta a review Chat 0.2 / utente.

## 1. Scopo e autorità metodologica

Questo artifact implementa il mandato `DISPATCH_CHAT_3.12_NATURA2000_PRESCREEN_RULESET_v01.md`.
Non riapre Fase 1, Fase 2 né `DEC-0041`.
La regola vincolante resta: nessuna esclusione o penalizzazione automatica deriva dalla sola intersezione o distanza da Natura 2000; il modello classifica il livello di approfondimento e non dichiara una VINCA formalmente superata.
`DEC-0059` autorizza esclusivamente la formalizzazione riproducibile del corpus regionale, delle prevalutazioni, della verifica di corrispondenza e dell'interferenza funzionale.
La Fase 4 resta NON AVVIATA.

## 2. Baseline geometriche riusate

Le geometrie Natura 2000 non sono state ricostruite.
Sono referenziati gli snapshot WFS validati dalla Chat 3.4:
- `SITI_PROT__SIC_20260919.geojson`, SHA-256 `772dabc52d720eaedfc5bd8de6649d2be915c01a88d2686d553137e3ebaa2e06`;
- `SITI_PROT__ZPS_20260919.geojson`, SHA-256 `949724e039aac197490c80e0ebbdfb6fbb46bf2a12f3b457e3989af0bc032660`.
L'unione validata contiene 72 codici sito; il typename tecnico `SIC` mantiene la nomenclatura legacy della fonte e non ridefinisce la designazione giuridica corrente.
## 3. Corpus regionale verificato

Corpus operativo materializzato in `02_external_sources/F3_CHAT_3_12/official_sources`:
- DGR 1183/2022 con allegati e tabella Allegato A;
- DGR 30/2026, testo integrale;
- DGR 30/2026 Allegato A.1 — criteri e verifica di corrispondenza;
- DGR 30/2026 Allegati A.2 e A.3 — prevalutazioni per regione biogeografica alpina e continentale;
- DGR 30/2026 Allegato B — osservazioni/provenance, non tradotto in regole eseguibili;
- DGR 30/2026 Allegato C — criteri per le aree di interferenza funzionale;
- DPReg 065/2025, Allegato 14 — aree di interferenza esterne del sito IT3320037 Laguna di Marano e Grado;
- Decreto 72016/GRFVG del 30/12/2025 e Allegato 1 — condizioni d'obbligo per lo screening, conservate come corpus procedurale downstream.

Le pagine regionali correnti di VINCA, prevalutazioni, interferenza funzionale, modulistica, condizioni d'obbligo e Natura 2000 sono state ricontrollate il 2026-09-21.
La ricerca mirata sulle fonti ufficiali non ha individuato un atto successivo che sostituisca DGR 30/2026 quale riferimento corrente per le prevalutazioni regionali.
Le misure di conservazione correnti restano fonte separata e obbligatoria nel controllo di corrispondenza: DGR 1148/2024 e 1149/2024 per le ZSC secondo regione biogeografica, DGR 594/2025 per le ZPS, DGR 1760/2025 per l'aggiornamento della ZPS IT3341002 e il piano vigente per IT3320037.
Il lineage puntuale, gli URL, le dimensioni e gli hash dei file materializzati sono registrati in `source_manifest_v01.json`.

## 4. Concetti mantenuti distinti

**Prevalutazione regionale:** giudizio preventivo espresso nelle matrici sito × tipologia P/I/A della DGR 30/2026.  
**Verifica di corrispondenza:** verifica che il caso concreto coincida con la fattispecie prevalutata e ne rispetti condizioni e misure vigenti.  
**Screening VINCA specifico:** procedura di livello I necessaria quando la prevalutazione non copre il caso o quando la fonte lo richiede.  
**Misure di conservazione:** disciplina sito/specie/habitat da verificare separatamente; non è sostituita dalla matrice di prevalutazione.  
**Interferenza funzionale:** relazione esterna al perimetro del sito definita da criteri regionali o sito-specifici; non coincide con una generica distanza ecologica.
## 5. Traduzione machine-readable delle prevalutazioni

Gli Allegati A.2 e A.3 sono stati letti per sito e tipologia di attività.
La matrice attesa è completa: `72 siti × 50 attività = 3.600` righe `SITE_ACTIVITY_PREASSESSMENT`.
La codifica conserva l'esito della fonte e applica un'azione di modello più conservativa:
- **verde fonte** → `PREASSESSED_NO_SIGNIFICANT_INCIDENCE`, ma il modello restituisce `CORRESPONDENCE_CHECK_REQUIRED` e usa `POTENTIALLY_COVERED_BY_PREASSESSMENT` solo dopo corrispondenza dimostrata;
- **rosso fonte** → `SPECIFIC_VINCA_SCREENING_REQUIRED`;
- **giallo fonte / non pertinente** → `MANUAL_REVIEW_REQUIRED`, mai esclusione automatica;
- **cella non determinabile dalla fonte** → `NOT_DETERMINABLE_FROM_AVAILABLE_RULES`.

Nessun record produce `VINCA_PASSED` o equivalente.
Le attività di ordine dimensionale o tipologico inferiore sono trattate come possibile corrispondenza solo se tale relazione è dimostrabile con dati progettuali espliciti; il modello non usa similarità semantica libera.

## 6. Verifica di corrispondenza

La procedura è codificata per i regimi amministrativi esplicitamente previsti dalla fonte: permesso di costruire, SCIA/CILA, edilizia libera, conferenza di servizi, procedimenti forestali, altra autorizzazione pubblica e assenza di procedimento autorizzativo.
Per applicare una prevalutazione verde devono essere disponibili almeno:
- tipologia concreta del P/I/A e attributi dimensionali/tecnologici necessari;
- localizzazione e sito interessato;
- condizioni specifiche riportate nella fattispecie prevalutata;
- verifica delle misure di conservazione vigenti e degli eventuali riferimenti `REP...`;
- eventuale relazione con area di interferenza funzionale;
- regime autorizzativo necessario a identificare il soggetto che effettua/attesta la corrispondenza.
Quando questi dati non esistono ancora alla scala macro, l'esito resta `CORRESPONDENCE_CHECK_REQUIRED` o `MANUAL_REVIEW_REQUIRED`.
`UNKNOWN` non viene convertito né in prevalutazione applicabile né in obbligo automatico di VINCA.
## 7. Interferenza funzionale

Non è stato individuato un unico layer ufficiale pubblico e machine-readable che rappresenti tutte le aree di interferenza funzionale regionali.
La DGR 30/2026 Allegato C definisce invece regole deterministiche differenziate per categoria di progetto, designazione del sito e contesto.
Nel rule-set sono state codificate esclusivamente soglie e relazioni esplicite della fonte: distanze definite dall'atto, relazioni idrologiche lungo i corsi d'acqua, lista esplicita di 15 siti per le derivazioni sotterranee, contesti Carso/Sappada, componenti PPR/RER e categorie marine/costiere.
Le regole distinguono dove la fonte limita il trigger a ZPS rispetto a ZSC/ZPS; per esempio elettrodotti aerei maggiori e impianti eolici usano il perimetro ZPS secondo la sintesi ufficiale dell'Allegato C.
La regola RER richiede la componente ufficiale di connettività e la relazione con almeno due ZSC; non viene sostituita da un buffer generico.
La riduzione condizionale delle distanze prevista dall'Allegato C è codificata come `MANUAL_REVIEW_REQUIRED` e non si applica con dati mancanti.

Per `IT3320037` prevale il criterio sito-specifico del Piano di gestione / DPReg 065/2025, Allegato 14, che definisce fasce 300 m, 1 km, 3 km, 10 km e 20 km per fattispecie specifiche, corridoi fluviali, sistemi sabbiosi e casi di livello II.
Tali distanze sono **valori normativi/source-defined**, non buffer inventati dal modello.
Una regola di interferenza esterna non scavalca una prevalutazione verde applicabile alla stessa fattispecie: prima si verifica la corrispondenza della prevalutazione, come richiesto da `DEC-0041`.

## 8. Crosswalk sito–regole

`FASE_3_NATURA2000_SITE_RULE_CROSSWALK_v01.csv` contiene 72 righe univoche, una per codice sito.
Per ciascun sito registra designazione corrente ricostruita dalla baseline validata, presenza nei layer tecnici SIC/ZPS, allegato DGR 30/2026 applicabile, conteggi degli esiti, base corrente delle misure di conservazione, fonte dell'interferenza funzionale, eventuale override sito-specifico e lineage geometrico per hash.
## 9. Anomalia sorgente preservata come UNKNOWN

Cinque celle dell'Allegato A.3, tutte relative all'attività `3.06`, non presentano una banda di esito classificabile nella sorgente PDF: `IT3330009`, `IT3330010`, `IT3340006`, `IT3340007`, `IT3341002`.
È stato effettuato un controllo mirato delle pagine e delle primitive grafiche del PDF.
La banda corrispondente è effettivamente bianca/non classificata, mentre le attività circostanti presentano bande verdi o gialle riconoscibili.
Non si tratta quindi di un semplice fallimento del parser da colmare per inferenza.
Le cinque celle restano `UNKNOWN` con azione `NOT_DETERMINABLE_FROM_AVAILABLE_RULES`.

## 10. Ordine operativo del pre-screening

1. Applicare i guardrail di `DEC-0041`: nessuna esclusione/penalizzazione per sola distanza o intersezione.
2. Determinare la relazione con il sito e gli eventuali trigger ufficiali di interferenza funzionale.
3. Recuperare la riga esatta sito × attività della prevalutazione.
4. Se verde, verificare corrispondenza e misure vigenti prima di qualsiasi escalation.
5. Se rosso o non coperto, applicare il livello di approfondimento richiesto dalla fonte.
6. Se giallo, UNKNOWN o dipendente da dati non disponibili, mantenere review/flag esplicito.
7. Non trasformare mai l'esito del pre-screening in una dichiarazione formale di superamento VINCA.

## 11. QA riproducibile

Script di build: `scripts/build_natura2000_prescreen_ruleset_chat3_12_v01.py`.  
Test: `tests/test_natura2000_prescreen_ruleset_chat3_12_v01.py`.  
Evidence machine-readable: `F3_CHAT_3_12/qa/natura2000_prescreen_qa_v01.json` e `natura2000_prescreen_test_results_v01.json`.
I test includono cinque fixture sintetiche dichiarate come tali: prevalutazione chiaramente coperta, mancata corrispondenza, interferenza funzionale esterna con prevalutazione applicabile, informazione progettuale insufficiente e nessuna regola applicabile.
## 12. Limiti residui

Il rule-set è un pre-screening procedurale per pianificazione macro e non sostituisce una valutazione competente.
Alcuni trigger richiedono input cartografici ufficiali esterni al presente artifact: PPR/RER, relazioni idrologiche, habitat/fauna, zonizzazione urbanistica o cartografia del Piano Laguna.
La prima costruzione dei candidati potrà non disporre di attributi progettuali sufficienti per la corrispondenza: questi casi restano esplicitamente non conclusivi.
Le cinque celle sorgente `UNKNOWN` devono essere sottoposte a review puntuale se materialmente rilevanti.
Le condizioni d'obbligo 2025 sono corpus downstream dello screening e non vengono usate per dichiarare preventivamente una prevalutazione applicabile.

## 13. Valutazione del quality gate

Esito proposto: **PASS TECNICO CON LIMITAZIONI**, subordinato all'esito finale dei test, al controllo `git diff --check`, all'aggiornamento dei registri e al commit pulito.
Non sono state create nuove geometrie Natura 2000, soglie ecologiche arbitrarie, penalizzazioni o categorie equivalenti a `VINCA_PASSED`.

Per `ISS-0013` si propone **`PROPOSE_RESOLVED_PROCEDURALLY`**:
il gap di codifica riproducibile è risolto, mentre le limitazioni applicative sono conservate come rami `UNKNOWN`/review e come requisiti di input futuri.
La proposta non chiude autonomamente l'issue: review e decisione competono a Chat 0.2 / utente.

**FASE 4 NON APERTA.**
