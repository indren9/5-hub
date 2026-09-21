# REVIEW — Chat 4.0 — Candidate Universe Contract v01

**Reviewer:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Stato:** TECHNICAL PASS / ONE METHODOLOGICAL AMENDMENT PROPOSED / USER DECISION REQUIRED
**Decisione:** DQ-01 resta PROPOSED

## 1. Esito

La review indipendente conferma il quality gate tecnico della Chat 4.0.

Sono supportate senza modifica sostanziale:
- A2 — urbanistica ufficiale best-available current-first;
- B4 — gerarchia current-first con CER 2018 solo ultima risorsa storica dichiarata;
- D2 — conservazione delle feature sorgente, split multipart disconnessi e merge solo per identità logica documentata;
- E3 — nessuna superficie minima in V2-1;
- F2 — soli gate tecnici/di scope come prefiltri HARD;
- G3 — candidate_id logico stabile separato da candidate_version e geometry_hash;
- H2 — QA strutturale, lineage, source-gap e determinismo senza target numerico sulla baseline Claude.

Nessun universo candidato definitivo è stato costruito.

## 2. Controlli indipendenti

Verificati:
- CANDIDATE_UNIVERSE_CONTRACT_v01_PROPOSED.md;
- CANDIDATE_SOURCE_OPTIONS_v01.csv;
- DQ01_DECISION_PACKET_v01.md;
- HANDOFF_CHAT_4.0_CANDIDATE_UNIVERSE_CONTRACT_v01.md;
- coerenza con Fase 1 v03 FROZEN, Fase 2 FROZEN e MODEL_v2;
- CSV parsabile: 7 opzioni;
- assenza di CANDIDATE_UNIVERSE_v01;
- git diff main...HEAD --check: PASS;
- working tree specialistico pulito prima delle correzioni formali di review.

Sono stati corretti esclusivamente difetti Markdown/line break nei tre artifact testuali. Nessuna proposta metodologica della Chat 4.0 è stata modificata in place.

## 3. Punto metodologico da emendare

La proposta C3 è corretta come principio — limitare l'universo a destinazioni non-residenziali territorialmente pertinenti — ma la tassonomia G1–G4 è parzialmente ambigua.

Problema 1:
G2_COMMERCIAL_SERVICE include la parola "servizi", che può essere interpretata troppo ampiamente e includere scuole, ospedali, attrezzature civiche o altre zone di servizio pubblico non coerenti con la funzione degli Hub.

Problema 2:
non esiste una classe esplicita per aree tecniche/tecnologiche/utility/energia, che possono essere territorialmente pertinenti per un Hub Energetico Green quando la destinazione urbanistica nativa le identifica come aree areali per impianti o infrastrutture tecniche.

## 4. Emendamento proposto C3+

La review propone di approvare C3 con la seguente tassonomia armonizzata:

- G1_PRODUCTIVE — industriale, artigianale, produttivo/manifatturiero, deposito/magazzino esplicito;
- G2_COMMERCIAL_TERTIARY — commerciale, direzionale, terziario e servizi economici non-residenziali; esclusi servizi pubblici generici/sociali/sanitari/scolastici privi di componente economico-produttiva pertinente;
- G3_LOGISTICS_TRANSPORT — logistica, porto, interporto, autoporto, terminal, trasporto e aree di servizio trasportistiche areali;
- G4_MIXED_RELEVANT — zone miste con almeno una componente esplicita G1/G2/G3/G5;
- G5_TECHNICAL_UTILITY_ENERGY — aree areali esplicitamente destinate a impianti tecnologici, utility, servizi tecnici, infrastrutture energetiche o funzioni equivalenti.

Le categorie native restano sempre conservate; il mapping verso G1–G5 deve essere auditabile e le categorie ambigue restano GENERATOR_CLASS_UNRESOLVED fino a risoluzione.

Questo emendamento non introduce un punteggio né un hard constraint DQ-02: definisce soltanto quali destinazioni urbanistiche possono generare alternative in DQ-01.

## 5. Motivazione

La scelta delle categorie generatrici è sostanziale perché ciò che non entra nell'universo non potrà essere recuperato successivamente dallo scoring.

Per questo:
- non è opportuno usare "tutte le zone non residenziali";
- non è opportuno usare "servizi" senza distinguere il significato urbanistico;
- è opportuno includere esplicitamente le aree tecniche/utility/energia;
- residenziale puro, agricolo puro, verde/tutela puro, acqua/alveo e servizi pubblici generici restano fuori dalla generazione iniziale salvo futura revisione del contratto.

## 6. Currentness e fallback

La review supporta A2+B4 con una cautela interpretativa:

l'uso di una geometria proxy o CER 2018 consente di mantenere completezza territoriale, ma non rende vera la destinazione urbanistica corrente.

Pertanto ogni candidato derivato da S2–S4 deve mantenere source_tier/currentness/proxy machine-readable e il QA deve quantificare la quota dell'universo derivata da fonti non current-verified.

Questa incertezza non produce automaticamente esclusione o penalizzazione in DQ-01.

## 7. Superficie minima

La review supporta E3.

Non esiste nella baseline FROZEN un footprint minimo universale approvato. Ereditare 5.000 m² dalla baseline Claude sarebbe metodologicamente scorretto.

area_m2 deve essere calcolata e diagnosticata; micro-poligoni/sliver devono essere visibili nel QA. Una eventuale soglia futura richiede nuova decisione e analisi di sensibilità.

## 8. HARD prefilter

La review supporta F2.

DQ-01 deve applicare soltanto gate tecnici/di scope necessari a costruire una popolazione di alternative coerente:
- geometria poligonale;
- valida/riparabile;
- area positiva;
- perimetro FVG;
- categoria generatrice approvata;
- deduplicazione della stessa alternativa fisica.

Ambiente, rischio, energia, TEN-T, accesso locale, proprietà e currentness non diventano hard filter in DQ-01.

## 9. Decisione utente richiesta

Pacchetto raccomandato dalla Chat 0.2:

- A2 — APPROVE;
- B4 — APPROVE;
- C3 — APPROVE WITH AMENDMENT C3+ (G1–G5);
- D2 — APPROVE;
- E3 — APPROVE;
- F2 — APPROVE;
- G3 — APPROVE;
- H2 — APPROVE.

Se approvato, DQ-01 potrà diventare ACCEPTED e il contratto definitivo dovrà recepire C3+ prima della costruzione di CANDIDATE_UNIVERSE_v01.

## 10. Governance editoriale

È stata confermata l'incoerenza segnalata dalla Chat 4.0 nell'intestazione del PROJECT_SOURCE_OF_TRUTH.

La Chat 0.2 ha riallineato l'intestazione allo stato corrente:
MODEL_v2 OPERATIVE; FASE 3 PASS / CLOSED WITH DECLARED LIMITATIONS; FASE 1 v03 e FASE 2 FROZEN.

## 11. Stato finale review

Chat 4.0 = TECHNICAL PASS.

DQ-01 = PROPOSED.

Unica modifica sostanziale proposta dalla review: C3+.

Nessuna costruzione dell'universo è autorizzata prima della decisione esplicita dell'utente.
