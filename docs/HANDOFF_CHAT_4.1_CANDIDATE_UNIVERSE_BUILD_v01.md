# HANDOFF — CHAT 4.1 — CANDIDATE UNIVERSE BUILD v01

**Chat:** 4.1 — Costruzione universo candidati V2-1
**Data chiusura:** 2026-09-21
**Stato proposto:** TECHNICAL PASS / REVIEW CHAT 0.2
**Branch:** `chat-4.1-candidate-universe-build`
**Commit implementazione:** `7b9e806`

## 1. Obiettivo

Costruire realmente `CANDIDATE_UNIVERSE_v01` e `CANDIDATE_LINEAGE_v01`
applicando DQ-01 / DEC-0065, senza introdurre DQ-02 o criteri di scoring.

Sono stati mantenuti come vincoli:
- urbanistica ufficiale best-available current-first;
- G1–G5;
- CER 2018 solo fallback storico;
- split multipart, no dissolve/merge generalizzato;
- HARD area lorda >= 8.000 m² dopo repair/split;
- lineage, ID/versioning e geometry_hash obbligatori.


## 2. Lavoro svolto

1. Verificati dispatch, contratto DQ-01 e baseline FROZEN/ACCEPTED.
2. Verificata la governance viva con PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER.
3. Materializzati/inventariati i vettori PRGC ufficiali disponibili.
4. Inventariati 1.847 layer interni; selezionati i layer urbanistici effettivi con regola auditabile.
5. Materializzato CER D/H 2018 esclusivamente come fallback.
6. Costruito mapping nativo -> G1–G5 con codice, descrizione, regola, stato ed evidenza.
7. Applicati repair, estrazione poligonale, split multipart e area in EPSG:6708.
8. Applicato HARD `MIN_AREA_8000_NOT_MET`.
9. Assegnati candidate_id stabili UUIDv5, versioni, geometry_hash e canonical_identity_key.
10. Costruiti lineage, exclusions, source gaps, overlap QA, manifest e hash.
11. Eseguito doppio run con confronto dei logical hash.
12. Eseguiti test automatici e controlli Git.

Nessun indicatore, peso, score, normalizzazione, TEN-T/accessibilità,
filtro ambientale o filtro energetico è stato applicato.


## 3. Risultato quantitativo

Candidati finali: **3.993**.

Distribuzione G1–G5:
- G1_PRODUCTIVE: 2.550;
- G2_COMMERCIAL_TERTIARY: 928;
- G3_LOGISTICS_TRANSPORT: 152;
- G4_MIXED_RELEVANT: 319;
- G5_TECHNICAL_UTILITY_ENERGY: 44.

Esclusi per `MIN_AREA_8000_NOT_MET`: **5.125**.

Distribuzione candidati per tier:
- S1: 167;
- S2: 2.709;
- S3: 55;
- S4: 1.062;
- S5: 0.

Presenza tier per Comune: S1=4, S2=99, S3=4, S4=103, S5=5.

Superficie lorda complessiva dei candidati: **251.227.636,615 m²**.
Il dettaglio di conteggi e superfici per Comune, tier e G1–G5 è persistito in
`CANDIDATE_DISTRIBUTION_QA_v01.csv`.

I 5 Comuni senza geometria utilizzabile sono:
**Preone, Stregna, Rivignano Teor, Treppo Ligosullo, Valvasone Arzene**.
Sono registrati come `NO_USABLE_POLYGON_SOURCE`; nessun poligono è stato digitalizzato o inventato.

Mapping finale:
- 1.838 combinazioni `RESOLVED_INCLUDED`;
- 5.051 `RESOLVED_EXCLUDED`;
- 703 `GENERATOR_CLASS_UNRESOLVED`.

Le categorie unresolved non entrano nell'universo. Le relative geometrie producono
4.016 esclusioni `GENERATOR_CLASS_UNRESOLVED` dopo repair/split.

## 4. Correzione emersa durante il QA

È stata corretta l'operazionalizzazione delle zone esplicitamente miste D/H
(es. D3H3, H3D3, D2_H2): devono essere G4_MIXED_RELEVANT e non G1/G2.
La correzione applica direttamente CU-03/DQ-01 e non introduce una nuova classe o scelta metodologica.

Effetto: cardinalità invariata a 3.993; 85 candidati riclassificati verso G4.


## 5. Artifact pesanti — OneDrive

Root:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\04_geodatabases\V2_1_CANDIDATE_UNIVERSE`

Artifact principali:
- `CANDIDATE_UNIVERSE_v01.gpkg`;
- `CANDIDATE_LINEAGE_v01.csv`;
- `CANDIDATE_EXCLUSIONS_v01.csv`;
- `CANDIDATE_SOURCE_GAPS_v01.csv`;
- `CANDIDATE_SOURCE_LAYER_SELECTION_v01.csv`;
- `CANDIDATE_OVERLAP_QA_v01.csv`;
- `CANDIDATE_DISTRIBUTION_QA_v01.csv`;
- `V2_1_CANDIDATE_UNIVERSE_QA_v01.json`;
- `CANDIDATE_UNIVERSE_MANIFEST_v01.json`;
- inventari e cache sorgente necessari alla ricostruzione.

Il GPKG contiene il layer `candidate_universe_v01` in EPSG:6708.


## 6. Artifact repository

Creati/versionati:
- `config/candidate_universe_v01.json`;
- `config/candidate_layer_overrides_v01.csv`;
- `scripts/materialize_candidate_source_vectors_v01.py`;
- `scripts/inventory_candidate_zoning_layers_v01.py`;
- `scripts/materialize_cer2018_fallback_v01.py`;
- `scripts/candidate_universe_rules_v01.py`;
- `scripts/build_candidate_universe_v01.py`;
- `tests/test_candidate_universe_v01.py`;
- `docs/CANDIDATE_GENERATOR_CLASS_MAPPING_v01.csv`;
- `docs/V2_1_CANDIDATE_UNIVERSE_SUMMARY_v01.csv`;
- `docs/V2_1_CANDIDATE_UNIVERSE_QA_v01.md`;
- `docs/PROJECT_CONTROL_REGISTER_UPDATE_PROPOSAL_CHAT_4.1_v01.md`;
- questo handoff.

Il mapping conserva categoria nativa, evidenza semantica, regola applicata,
stato resolved/unresolved e conteggio delle feature sorgente.


## 7. QA ed esito

- candidate_id univoci/non null: PASS;
- candidate_version/universe_version completi: PASS;
- geometry_hash completi: PASS;
- geometrie finali Polygon, non empty e valide: PASS;
- area >= 8.000 m² per 100% candidati: PASS;
- 5.125 esclusioni sotto soglia registrate: PASS;
- generator_class risolto per 100% candidati inclusi: PASS;
- currentness/proxy status valorizzato: PASS;
- source-gap report 215/215: PASS;
- duplicati geometry_hash finali: 0;
- overlap non identici quantificati: 461 coppie;
- determinismo rerun: PASS;
- manifest/hash: PASS;
- campi DQ-02 assenti: PASS;
- py_compile: PASS;
- pytest: 5 passed;
- git diff --cached --check pre-commit: PASS.

Machine QA: `all_required_checks_pass=true`.


## 8. Hash principali

Hash fisici:
- GPKG: `57B51E3B381743554E105F8E1959674AE426A3F20D379BC709EFA8E8BE78969B`;
- lineage: `6C11D43EBEA8FF60FF63582393632248DB65EB07340CBDF20B3BC8B7F69AA55A`;
- exclusions: `2FBD7CC5B5B733FC7679706DFBF66E833BC259AC8A01CBAF9A8FC05A9E087D24`;
- mapping: `4A80A85FBF3AE839C34D91E44E74812975269C4A2B0FB7467FD83ABAEBC4E002`.

Hash logici:
- universe: `648A76F925FE65567CB88CE688A1C41F158DC1C8B90E1E95BCABEA7611D38F39`;
- lineage: `C60DB10499111A4A8FD0E1F2B1A85AEF0EA28820F471799795EEE1EC7689E134`;
- exclusions: `409BB7915634D2BF855C22ED436AD8F1C8CC05395D7BA98CBF4CF91F1F085B7D`;
- mapping: `01002F2009C96FE26C515C901E80AABCF2D3ADE2CA4BD0C6C3495E3268C89C58`;
- source gaps: `0EFB6D1F9606261A752AEABB8C0BF0A66B9A38E585AC1A3C822BCE964CFB3799`.


## 9. Limiti e problemi aperti

1. Cinque Comuni restano S5.
2. 103 Comuni ricadono su S4 e 1.062 candidati usano geometria CER 2018 storica.
3. I 99 Comuni S2 mantengono currentness non integralmente verificata.
4. Restano 703 categorie native semanticamente insufficienti: non sono state forzate.
5. Restano 461 overlap non identici; DQ-01 non autorizza fusione per sola sovrapposizione.
6. Alcuni shapefile sorgente presentano warning geometrici OGR/pyogrio,
   ma l'output finale ha 0 geometrie invalide.
7. Proprietà, disponibilità commerciale, ambiente, energia, TEN-T e accessibilità
   non sono stati usati come filtri in questa fase.

Nessuno di questi punti è stato trasformato implicitamente in una nuova decisione metodologica.

## 10. Governance proposta

Preparato `PROJECT_CONTROL_REGISTER_UPDATE_PROPOSAL_CHAT_4.1_v01.md`.
La proposta registra l'universo come dataset derivato REVIEW e porta alla Chat 0.2
i gap S5/S4, gli unresolved e gli overlap. Nessun nuovo codice DEC/ISS è stato assegnato.


## 11. Git e stato finale

Commit principali:
- `7b9e806 — feat(v2-1): build candidate universe with DQ-01 QA`;
- `614b3e3 — docs(v2-1): close chat 4.1 candidate universe build`;
- `ebc4222 — qa(v2-1): add candidate distribution audit`.

Il presente handoff viene riallineato in un commit finale di chiusura dopo il refinement QA;
il relativo hash è riportato nel messaggio finale della Chat 4.1.

**QUALITY GATE CHAT 4.1: PROPOSED PASS.**

Stato dell'artifact: **REVIEW**, non ACCEPTED/FROZEN.

## 12. Prossimo passo

Chat 0.2 deve revieware:
- universo e lineage;
- mapping e unresolved;
- source gaps S1–S5;
- overlap QA;
- proposta di aggiornamento registri;
- hash e commit.

Dopo la review, la Chat 0.2/utente potrà accettare o respingere il gate V2-1.
La Chat 4.1 si ferma qui e **non apre DQ-02**.
