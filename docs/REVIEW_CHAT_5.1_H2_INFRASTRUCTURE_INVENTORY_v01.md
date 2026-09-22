# REVIEW CHAT 5.1 — H2 INFRASTRUCTURE INVENTORY v01

**Data review:** 2026-09-22
**Reviewer:** Chat 0.2 — Chat Madre 5 HUB
**Stato:** ACCEPTED AS MODEL_v2 FACTUAL BASELINE — DEC-0085
**Input:** Chat 5.1 — Inventario infrastrutture H2 FVG

## 1. Esito review indipendente

La Chat Madre ha verificato:
- handoff Chat 5.1;
- inventory CSV;
- source register;
- review metodologica;
- script QA;
- stato Git.

Il QA è stato rieseguito dalla Chat Madre il 2026-09-22 con esito:
- record: 10;
- source records: 22;
- warning: 0;
- errori: 0;
- risultato: PASS.

Git:
- `d648b85 data(h2): build verified FVG hydrogen infrastructure inventory`;
- `5ef4f79 docs(h2): close chat 5.1 inventory handoff`.

I commit risultano ora presenti su `origin/main` a seguito dei successivi push della Chat Madre.

## 2. Risultato fattuale verificato

Inventario totale:
- 3 UNDER_CONSTRUCTION;
- 5 FUNDED_COMMITTED;
- 2 ANNOUNCED_UNVERIFIED;
- 0 OPERATIONAL.

Core infrastructure:
- FVG_H2_001 Trieste — UNDER_CONSTRUCTION — spatial readiness HIGH;
- FVG_H2_002 Monfalcone/Lisert — UNDER_CONSTRUCTION — HIGH;
- FVG_H2_003 Porpetto — FUNDED_COMMITTED — MEDIUM_HIGH;
- FVG_H2_004 SOLHX Manzano — FUNDED_COMMITTED — MEDIUM, municipality only;
- FVG_H2_005 ABS Pozzuolo/Cargnacco — FUNDED_COMMITTED — HIGH.

## 3. Interpretazione metodologica

Il dataset non supporta un criterio denominato semplicemente “infrastrutture H2 già presenti”, perché nessun core site dispone di prova primaria corrente di stato OPERATIONAL.

La semantica corretta, se approvata, è:
**prossimità a infrastrutture H2 core verificate esistenti/in costruzione/committed**, con status preservato e senza trasformare lo status in prova di disponibilità attuale.

## 4. Readiness spaziale proposta

Per calcoli point-to-polygon immediati risultano sufficientemente solidi:
- FVG_H2_001 Trieste;
- FVG_H2_002 Monfalcone/Lisert;
- FVG_H2_003 Porpetto;
- FVG_H2_005 ABS.

FVG_H2_004 SOLHX è fattualmente valido come progetto FUNDED_COMMITTED, ma non è point-ready: la localizzazione disponibile è solo comunale. Non deve ricevere coordinate inventate né entrare in distanze puntuali finché non viene recuperata una localizzazione primaria più precisa.

I record H2_TESTBED_CONTEXT e ANNOUNCED_CONTEXT non sono automaticamente assimilabili a infrastrutture core di produzione/rifornimento.

## 5. Gap da mantenere aperto

Gap principale:
**SOLHX spatial localization** — recuperare indirizzo/lotto/coordinate primarie prima dell'inclusione in calcoli puntuali.

Ulteriori aggiornamenti di stato per Trieste, Monfalcone e Porpetto sono monitoraggi currentness, non blocker della baseline fattuale.

## 6. Decisione utente — DEC-0085

ACCEPTED:
1. l'inventario Chat 5.1 è baseline fattuale H2 del MODEL_v2;
2. i target spaziali iniziali dello score sono i quattro core site point-ready: Trieste, Monfalcone/Lisert, Porpetto e ABS;
3. SOLHX resta nella baseline fattuale ma fuori dai calcoli di distanza fino a localizzazione primaria più precisa;
4. testbed e announced/unverified restano contesto e non target dello score core;
5. lo status viene sempre preservato; nessun record è OPERATIONAL al 2026-09-22;
6. il criterio usa la distanza dal core site point-ready più vicino, normalizzata con `S_H2 = 1 - d_H2/d_max_H2` sull'intero universo candidati;
7. nessuna soglia, nessun peso per status e nessun bonus per numero di siti.

Il peso/importanza del criterio sarà assegnato successivamente dall'utente insieme agli altri criteri.
