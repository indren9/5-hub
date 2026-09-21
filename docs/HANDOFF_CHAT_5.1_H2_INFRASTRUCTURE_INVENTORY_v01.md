# HANDOFF — Chat 5.1 — Inventario infrastrutture H2 FVG

**Chat:** 5.1 — Inventario infrastrutture H2 FVG  
**Regia:** Chat 0.2 — Chat Madre 5 HUB  
**Data:** 2026-09-22  
**Stato operativo:** PASS tecnico / REVIEW metodologica  
**Artifact commit:** `d648b85` — `data(h2): build verified FVG hydrogen infrastructure inventory`

## 1. Obiettivo

Costruire un inventario current-first, verificato, georiferibile e tracciabile delle infrastrutture H2 esistenti o concretamente programmate in Friuli Venezia Giulia, verificando esplicitamente Monfalcone/Lisert, Trieste, Porpetto, testbed NAHV e interventi PNRR/MASE/MIMIT/Regione FVG.

Nessuna formula di score, peso, soglia di distanza o normalizzazione è stata definita.

## 2. Fonti consultate

Fonti prioritarie utilizzate:
- Regione Autonoma Friuli Venezia Giulia: Strategia regionale idrogeno, BUR/autorizzazioni, decreti Progetti Bandiera, comunicati;
- Sistema CUP / OpenCUP per Porpetto;
- NAHV e CORDIS per testbed e stato progetti;
- operatori/promotori: APT Gorizia, Q8, Autoporto Pontebba;
- Area Science Park per H2SmartCampus;
- fonti secondarie soltanto come cross-check dove la fonte primaria non localizza il Comune/asset con precisione sufficiente.

Registro completo: `docs/H2_FVG_SOURCE_REGISTER_v01.csv`.

## 3. Inventario finale

Record totali: **10**.

Per stato:
- UNDER_CONSTRUCTION: **3**
- FUNDED_COMMITTED: **5**
- ANNOUNCED_UNVERIFIED: **2**
- OPERATIONAL: **0**
- PLANNED_AUTHORIZED: **0**
- UNKNOWN: **0**

Per scope:
- CORE_H2_INFRA: **5**
- H2_TESTBED_CONTEXT: **4**
- ANNOUNCED_CONTEXT: **1**

Per tipologia:
- INTEGRATED_H2_SITE: 4
- REFUELING_STATION: 2
- ELECTROLYZER_PRODUCTION: 1
- INDUSTRIAL_H2_TESTBED: 1
- H2_COMPONENT_TESTBED: 1
- H2_RESEARCH_INFRASTRUCTURE: 1

## 4. Risultati chiave

1. **Monfalcone/Lisert:** UNDER_CONSTRUCTION. Fonti current-first 2026 descrivono ancora lavori/realizzazione; nessun commissioning H2 primario trovato. Non OPERATIONAL e nessuna conformità AFIR inferita.
2. **Trieste Hydrogen Hub:** UNDER_CONSTRUCTION. NAHV 16/06/2026 lo descrive in fase avanzata di costruzione; AU regionale per 5 MW H2 + 4,85 MWp PV. Nessun commissioning primario trovato.
3. **Porpetto Q8:** FUNDED_COMMITTED. CUP H2 attivo, ma la stazione Q8 aperta elenca attualmente altri vettori e non H2. L'apertura della stazione base non prova l'operatività H2.
4. **SOLHX Manzano:** FUNDED_COMMITTED. Concessione regionale certa; sito recuperato solo a livello comunale, quindi non pronto per distanze puntuali.
5. **ABS Pozzuolo/Cargnacco:** FUNDED_COMMITTED. Concessione regionale certa e sito industriale georiferibile; NAHV Testbed II deduplicato nello stesso record.
6. **Pontebba:** ANNOUNCED_UNVERIFIED. La fonte corrente dell'operatore non elenca H2; un vecchio annuncio non è stato trasformato in asset operativo.
7. **CTS:** ANNOUNCED_UNVERIFIED come sito, perché il testbed NAHV è reale ma il sito finale HRS non risulta fissato.

## 5. Deduplicazione NAHV

- Testbed VIII Acegas + Testbed III Snam/Cubogas -> FVG_H2_001 Trieste Hub.
- Testbed II ABS -> FVG_H2_005.
- Testbed XV componente APT -> FVG_H2_002 Monfalcone.
- Testbed XV componente Trieste Trasporti: non creato record autonomo perché manca un sito finale sufficientemente documentato.
- Testbed IX rete gas FVG: non trasformato artificialmente in punto.
- Ferriere Nord, Faber e H2SmartCampus restano record di contesto/testbed distinti.

## 6. File creati/modificati

- `data/interim/H2_FVG_INFRASTRUCTURE_INVENTORY_v01.csv`
- `docs/H2_FVG_SOURCE_REGISTER_v01.csv`
- `docs/H2_FVG_INFRASTRUCTURE_INVENTORY_REVIEW_v01.md`
- `scripts/qa_h2_inventory.py`
- log locale rigenerabile: `logs/H2_FVG_INFRASTRUCTURE_INVENTORY_QA_v01.txt` (gitignored)

Nessun dataset pesante materializzato; OneDrive non modificato.

## 7. Quality gate

Primo run QA: **FAIL** per shift di colonne nel CSV originale.  
Azione correttiva: schema CSV rigenerato con campi di capacità per natura separati e serializzazione deterministica.  
Run finale: **PASS**.

Controlli finali:
- 10 ID univoci e validi;
- enum stato valido;
- fonti primarie risolte nel source register;
- localizzazioni tracciate;
- coordinate, quando presenti, complete e in range;
- nessun duplicate NAME+COMUNE;
- produzione/potenza/rifornimento/stoccaggio/altre capacità separati;
- announced/unverified non classificati come CORE_H2_INFRA;
- warning: NONE;
- error: NONE.

## 8. Problemi aperti / gap

- **H2-GAP-01 — SOLHX:** recuperare indirizzo, lotto o coordinate primarie del sito di Manzano prima di qualsiasi distanza puntuale.
- **H2-GAP-02 — Porpetto:** cercare evidenza primaria successiva che documenti avvio lavori o commissioning della specifica componente H2.
- **H2-GAP-03 — Monfalcone:** non avanzare a OPERATIONAL senza commissioning/esercizio primario.
- **H2-GAP-04 — Trieste:** non avanzare a OPERATIONAL senza commissioning/esercizio primario.
- **H2-GAP-05 — CTS / Trieste Trasporti:** mantenere fuori dai target spaziali finché il sito finale non è documentato.
- **H2-GAP-06 — AFIR:** nessuna conformità AFIR è stata determinata da questa chat.

Gli ID H2-GAP-* sono locali all'handoff; l'eventuale creazione di ISS ufficiali spetta alla Chat Madre.

## 9. Raccomandazione alla Chat Madre

Per una futura baseline fattuale del criterio H2, senza ancora deciderne formula o regole:
- **sufficientemente solidi e spazialmente utilizzabili a scala regionale:** FVG_H2_001 Trieste, FVG_H2_002 Monfalcone, FVG_H2_003 Porpetto, FVG_H2_005 ABS;
- **status/funding solido ma localizzazione da raffinare prima delle distanze:** FVG_H2_004 SOLHX;
- **solo contesto/testbed, non assimilare automaticamente a core infrastructure:** FVG_H2_006, 007, 008;
- **non usare come asset concretamente disponibile:** FVG_H2_009 Pontebba e FVG_H2_010 CTS finché restano ANNOUNCED_UNVERIFIED.

La Chat Madre deve decidere se accettare questa baseline e, separatamente, come trattare status, tipologie e distanza nel futuro criterio H2.

## 10. Governance

Nessuna decisione ACCEPTED/FROZEN è stata modificata.  
PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER sono stati letti come baseline viva.  
Non sono stati scritti aggiornamenti nei registri ufficiali: la Chat Madre può registrare il dataset/issue dopo review e acceptance.

