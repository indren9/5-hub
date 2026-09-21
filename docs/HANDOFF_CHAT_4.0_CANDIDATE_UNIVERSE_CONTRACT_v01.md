# HANDOFF — CHAT 4.0 — CANDIDATE UNIVERSE CONTRACT v01

**Chat:** 4.0 — Contratto dell'universo dei poligoni candidati
**Fase:** MODEL_v2 / V2-1 / DQ-01
**Data:** 2026-09-21
**Stato finale:** COMPLETED / TECHNICAL PASS — DQ-01 resta PROPOSED
**Regia:** Chat 0.2 — Chat Madre 5 HUB

## 1. Obiettivo

Definire il contratto metodologico dell'universo dei poligoni candidati senza costruire l'universo definitivo.

Perimetro rispettato:
- fonti/categorie generatrici;
- unione di famiglie;
- split/merge/canonicalizzazione;
- multipart/geometrie invalide;
- superficie minima;
- soli prefiltri HARD indispensabili;
- currentness/proxy;
- lineage;
- candidate_id/versioning;
- QA minimo.

Fuori perimetro e non definiti:
- indicatori;
- normalizzazioni;
- pesi;
- score;
- funzione obiettivo;
- ottimizzazione;
- costruzione di CANDIDATE_UNIVERSE_v01.

## 2. Baseline lette e verificate

Locali:
- DISPATCH_CHAT_4.0_CANDIDATE_UNIVERSE_CONTRACT_v01.md;
- PROJECT_MODEL_CONTRACT_REBASELINE_v01.md;
- ROADMAP_METODOLOGICA_v2.md;
- FASE_1_HUB_DEFINITION_REBASELINED_v03.md;
- FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md;
- REBASELINE_APPROVAL_AND_PHASE3_CLOSE_v01.md;
- BASELINE_QGIS_BELTRAME_REVIEW_v01.md;
- review Fase 3 urbanistica/data inventory pertinenti.

Governance viva Google Drive:
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER / DECISIONS;
- DEC-0061, DEC-0062, DEC-0063, DEC-0064;
- DATA_REGISTRY;
- ISSUES.Nota governance: l'intestazione iniziale del PROJECT_SOURCE_OF_TRUTH riporta ancora Fase 3 “IN CORSO”, ma la sezione 13 recepisce DEC-0062/0063/0064, dichiara MODEL_v2 operativo e Fase 3 chiusa e specifica che tali decisioni prevalgono sulle formulazioni precedenti. La Chat 4.0 non ha modificato la governance viva; si raccomanda alla Chat 0.2 di riallineare l'intestazione in una futura manutenzione editoriale.

## 3. Evidenze principali usate

- MODEL_v2 = pianificazione strategica territoriale, non due diligence immobiliare/catastale/autorizzativa.
- Fase 2 = poligono come unità; multipart disconnessi splittati di default; no split automatico ai confini comunali; canonicalizzazione duplicati obbligatoria; candidate_id distinto dalla versione geometrica.
- F3_SRC_FVG_PRGC_CURRENT_001 = ACCEPTED come baseline urbanistica best-available per generazione/classificazione.
- Coverage urbanistica = 215/215 Comuni.
- Stato coverage v02 = 4 CURRENT_VECTOR_VERIFIED, 4 CURRENT_PLAN_VERIFIED_NO_VECTOR, 207 CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE.
- CER D/H = Mosaicatura PRG 2018, HISTORICAL_ONLY / SUPPORT_ONLY.
- Baseline Claude/QGIS = 1.377 candidati historical support; minimo osservato 5.016,2 m²; procedura di generazione non ricostruibile dal package.
- Proprietà/disponibilità commerciale = fuori core con DEC-0062/0063.

## 4. Proposta DQ-01 consegnata

Bundle raccomandato, tutto PROPOSED:
1. famiglia generatrice principale = urbanistica ufficiale best-available current-first;
2. gerarchia S1–S4 con proxy/currentness espliciti e CER 2018 solo ultima risorsa;
3. classi generatrici G1 produttivo, G2 commerciale/servizi, G3 logistica/trasporti, G4 misto rilevante;
4. nessuna union autonoma con catasto/lotti/proprietà;
5. split multipart disconnessi; no dissolve generalizzato;
6. merge/canonicalizzazione guidati da identità e lineage, non da soglie arbitrarie;
7. nessuna superficie minima in V2-1;
8. soli gate tecnici/di scope come hard prefilter;
9. proxy/currentness mai tradotti automaticamente in esclusione;
10. candidate_id logico stabile + candidate_version + universe_version + geometry_hash;
11. QA strutturale, lineage, source-gap e determinismo.

## 5. Artifact creati

- docs/CANDIDATE_UNIVERSE_CONTRACT_v01_PROPOSED.md
- docs/CANDIDATE_SOURCE_OPTIONS_v01.csv
- docs/DQ01_DECISION_PACKET_v01.md
- docs/HANDOFF_CHAT_4.0_CANDIDATE_UNIVERSE_CONTRACT_v01.md

Nessuno script di generazione candidati è stato creato.

## 6. Git

Branch:
`chat-4.0-candidate-universe-contract`

Commit principale degli artifact decisionali:
`0492bd079a4306a85d1232d2124183a63ca8e2c1`
— `docs(v2-1): propose candidate universe contract`

Il presente handoff viene versionato con commit di chiusura separato; il relativo hash è riportato nella risposta finale della Chat 4.0.## 7. Quality gate

| Controllo | Esito |
|---|---|
| Nessun candidato definitivo costruito | PASS |
| Opzioni confrontate con razionale/vantaggi/svantaggi/bias/completezza | PASS |
| Nessuna soglia storica 5.000 m² ereditata | PASS |
| Proprietà/catasto fuori core | PASS |
| Hard prefilter ridotti a gate tecnici/di scope | PASS |
| Fase 2 rispettata | PASS |
| DQ-01 resta PROPOSED | PASS |
| CSV source options parsabile | PASS |
| Nessun CANDIDATE_UNIVERSE_v01 creato | PASS |
| git diff --check sugli artifact decisionali dopo correzione whitespace | PASS |
| Artifact persistenti obbligatori | PASS |
| Handoff completo | PASS |

La verifica finale `git diff main...HEAD --check` e `git status --porcelain` viene eseguita dopo il commit del presente handoff.

## 8. Decisioni non assunte

Non sono stati approvati:
- DQ-01;
- mapping definitivo dei codici PRGC locali;
- CRS operativo numerico;
- tolleranze metriche non nulle;
- soglia minima di superficie;
- qualunque hard constraint ambientale/energetico/accessibilità;
- indicatori o formule DQ-02+.

Questi elementi non devono essere dedotti implicitamente dal contratto.

## 9. Problemi/limiti aperti

1. La materializzazione effettiva delle geometrie urbanistiche per V2-1 resta attività successiva all'approvazione DQ-01.
2. Il mapping dei codici/descrizioni PRGC locali verso G1–G4 richiede una tabella auditabile prima della generazione.
3. Nei Comuni con geometria proxy/storica l'universo avrà qualità/currentness disomogenea: il QA deve quantificarla.
4. Perimetri logistici/portuali/consortili non sono stati promossi a seconda famiglia generatrice: eventuale integrazione richiede successor contract.
5. L'intestazione del PROJECT_SOURCE_OF_TRUTH è editorialmente arretrata rispetto alla sezione 13/DEC-0062…0064; nessun conflitto operativo perché il documento dichiara la prevalenza delle decisioni più recenti.

## 10. Stato finale

**Chat 4.0 = COMPLETED / TECHNICAL PASS.**

**DQ-01 = PROPOSED.**

Non è autorizzata da questa chat la costruzione dell'universo candidato definitivo.

## 11. Prossimo passo

Review della Chat 0.2 e decisione esplicita dell'utente sul pacchetto DQ-01.

Solo dopo approvazione:
- DQ-01 potrà diventare ACCEPTED;
- la Chat Madre potrà autorizzare la costruzione V2-1;
- potranno essere prodotti CANDIDATE_UNIVERSE_v01, CANDIDATE_LINEAGE_v01 e QA associato.

STOP per review.
