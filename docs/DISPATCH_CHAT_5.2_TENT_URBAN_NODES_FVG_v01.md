# DISPATCH CHAT 5.2 — DELIMITAZIONE NODI URBANI TEN-T FVG

**Chat:** 5.2 — Delimitazione nodi urbani TEN-T FVG
**Regia:** Chat 0.2 — Chat Madre 5 HUB
**Data apertura:** 2026-09-22
**Stato:** DISPATCHED

## Obiettivo

Determinare in modo verificabile e riproducibile quale sia la **copertura geografica / delimitazione territoriale ufficiale** dei nodi urbani TEN-T di **Trieste** e **Udine**, ai fini della futura formalizzazione del configuration constraint AFIR H2 del MODEL_v2.

## Domanda principale

Per l'obbligo AFIR di almeno una stazione H2 accessibile al pubblico in ciascun nodo urbano pertinente:
1. esiste un perimetro territoriale ufficiale del nodo urbano?
2. se sì, quale fonte lo definisce?
3. è già disponibile al 22/09/2026 per Trieste e Udine?
4. è espresso come LAU/comuni, poligono GIS, TENtec layer o altra delimitazione?
5. tale delimitazione è giuridicamente applicabile al requisito AFIR H2 oppure riguarda solo reporting/SUMP/data collection?

## Fonti prioritarie

Ordine di preferenza:
1. EUR-Lex — Reg. (UE) 2024/1679 TEN-T e atti successivi;
2. atti UE 2026 sulla geographical coverage degli urban nodes / LAU;
3. Commissione europea / DG MOVE / TENtec;
4. Ministero italiano competente / MIT;
5. Regione FVG solo come supporto o recepimento.

Non usare fonti secondarie come base autorevole se esiste fonte primaria.

## Baseline vincolante

Leggere:
- `docs/AFIR_TENT_MODEL_ROLE_v02.md`
- `docs/FASE_1_HUB_DEFINITION_REBASELINED_v03.md`
- `docs/CLAUDE_PIPELINE_REQUIREMENTS_INPUT_v01.md`
- `docs/RELATION_PENDING_DECISIONS_RESOLUTION_v01.md`

Decisioni da NON riaprire:
- AFIR/TEN-T non genera score individuale di distanza;
- il requisito H2 “lungo TEN-T” usa 10 km stradali dalla nearest exit;
- il vincolo AFIR opera a livello di configurazione;
- Trieste e Udine sono i nodi urbani TEN-T pertinenti già identificati nel progetto, salvo verifica formale della fonte.

## Output richiesto

Produrre:
1. `docs/REVIEW_CHAT_5.2_TENT_URBAN_NODES_FVG_v01.md`
2. eventuale tabella/source register leggero se utile;
3. handoff finale.

La review deve concludere con una delle seguenti classi:
- `OFFICIAL_BOUNDARY_AVAILABLE`
- `OFFICIAL_LAU_COMPOSITION_AVAILABLE`
- `OFFICIAL_BOUNDARY_PENDING`
- `NO_LEGAL_SPATIAL_BOUNDARY_IDENTIFIED`
- `NOT_DETERMINABLE`

## Regole metodologiche

- Non inventare buffer.
- Non assumere automaticamente che nodo urbano = Comune capoluogo.
- Non usare centroidi o aree metropolitane come proxy senza mandato.
- Distinguere chiaramente:
  - definizione giuridica del nodo urbano;
  - delimitazione per reporting/data collection;
  - geometria tecnica TENtec;
  - eventuale proxy operativo.
- Se la delimitazione ufficiale non è ancora disponibile, dichiararlo esplicitamente e non colmare il gap con una scelta implicita.

## Quality gate

PASS solo se:
- fonti primarie verificate;
- Trieste e Udine trattate separatamente;
- data/currentness esplicite;
- distinzione legale/tecnica chiara;
- conclusione riproducibile;
- nessun proxy inventato.

La Chat 5.2 non deve definire da sola il configuration constraint finale AFIR: deve riportare evidenze e opzioni alla Chat 0.2.
