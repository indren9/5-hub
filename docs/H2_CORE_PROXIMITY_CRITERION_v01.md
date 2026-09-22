# H2 CORE PROXIMITY CRITERION v01

**Data:** 2026-09-22
**Stato:** ACCEPTED
**Autorità:** DEC-0085

## 1. Baseline fattuale

Baseline:
`data/interim/H2_FVG_INFRASTRUCTURE_INVENTORY_v01.csv`

Inventario verificato:
- 10 record totali;
- 5 `CORE_H2_INFRA`;
- 0 `OPERATIONAL` al 2026-09-22.

## 2. Target spaziali iniziali dello score

Entrano inizialmente nel criterio solo i core site sufficientemente localizzati:
- `FVG_H2_001` — Hydrogen Hub Trieste;
- `FVG_H2_002` — APT EcoMove Monfalcone / Lisert;
- `FVG_H2_003` — Q8 Porpetto PNRR hydrogen refueling project;
- `FVG_H2_005` — ABS Pozzuolo / Cargnacco.

`FVG_H2_004` — SOLHX Manzano resta nella baseline fattuale ma non entra nei calcoli di distanza finché la localizzazione non viene raffinata oltre il solo Comune.

Testbed context e `ANNOUNCED_UNVERIFIED` non entrano nello score core.

## 3. Distanza

Per ogni candidato i:
`d_i^H2 = min_j(d_ij)`

dove j varia sui core site point-ready approvati.

## 4. Normalizzazione

Sull'intero universo candidati:
`d_max^H2 = max_i(d_i^H2)`

Score:
`S_i^H2 = 1 - d_i^H2 / d_max^H2`

Proprietà:
- score in [0,1];
- candidato più vicino a un core site ottiene score maggiore;
- candidato più svantaggiato rispetto al proprio core site più vicino = 0;
- nessuna soglia artificiale;
- nessun bonus per numero di siti;
- nessun peso per stato del progetto.

## 5. Status

Lo status (`UNDER_CONSTRUCTION`, `FUNDED_COMMITTED`, ecc.) resta attributo descrittivo e non modifica lo score.

Al 2026-09-22 nessun core site è `OPERATIONAL`.

## 6. Limiti

Il criterio misura prossimità a infrastrutture H2 core verificate esistenti/in costruzione/committed, non disponibilità operativa attuale.

Non prova:
- commissioning;
- accesso pubblico;
- capacità disponibile;
- conformità AFIR;
- compatibilità tecnica del candidato con il sito H2.

## 7. Currentness

Se SOLHX viene localizzato puntualmente, potrà essere incluso nei target spaziali dopo verifica dati.

Eventuali aggiornamenti futuri di status/localizzazione richiedono nuova verifica della baseline ma non modificano automaticamente la formula.
