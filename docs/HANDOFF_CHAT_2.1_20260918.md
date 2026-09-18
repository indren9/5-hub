# HANDOFF — Chat 2.1 — Definizione dell’unità elementare di analisi

**Data:** 2026-09-18
**Stato finale Chat 2.1:** PASS tecnico-operativo
**Stato FASE 2:** REVIEW / IN CORSO — NON FROZEN, NON CLOSED
**Regia:** Chat Madre 5 HUB

## 1. Obiettivo

Definire una proposta metodologicamente solida e riproducibile dell’unità elementare con cui il modello rappresenterà una singola alternativa candidata alla localizzazione di un Hub Energetico Green.

La Chat 2.1 non aveva autorità per congelare decisioni metodologiche sostanziali.

## 2. Baseline rispettata

- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN, non modificata;
- `docs/ROADMAP_METODOLOGICA_v1.md`;
- `docs/DISPATCH_CHAT_2.1_UNIT_ANALYSIS_v01.md`;
- governance viva verificata su PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER.

Non è stata ereditata automaticamente alcuna scelta della baseline Claude.

## 3. Lavoro svolto

È stato creato e verificato:

`C:\dev\5-hub\docs\FASE_2_UNIT_ANALYSIS_REVIEW_v01.md`

Il review contiene:

1. confronto tra punto, comune, impianto esistente, area e modello ibrido;
2. proposta formale dell’unità elementare;
3. regole per poligono, multipart, contiguità e overlap;
4. distinzione tra punto rappresentativo e accesso stradale;
5. struttura concettuale access point / road anchor / connector;
6. tassonomia esplicita delle distanze;
7. contratto geometrico minimo per futuri indicatori e vincoli;
8. requisiti di scala e precisione;
9. schema di identificativo/versionamento;
10. implicazioni per Fase 3 e Fase 4;
11. decisioni F2-D1…F2-D8 da sottoporre all’utente.

## 4. Proposta metodologica

La proposta principale è un modello **ibrido area + geometrie ausiliarie**:

- il candidato è un’**area/poligono fisicamente localizzabile**;
- il punto rappresentativo è solo un supporto descrittivo/operativo;
- gli accessi stradali sono entità separate e possono essere multipli;
- le distanze stradali partono dagli accessi, non dal centroide;
- la geometria del candidato non coincide con il layout futuro dell’Hub.

Formalmente il review propone:

`C_i^v = (P_i^v, R_i^v, A_i^v, L_i^v, M_i^v)`

con poligono candidato, punto rappresentativo, accessi, lineage e metadati/versione.

## 5. Alternative analizzate

- **Punto candidato:** scartato come unità principale perché non rappresenta superficie, forma e accessi.
- **Comune/unità amministrativa:** scartato come candidato perché non identifica una localizzazione fisica.
- **Impianto esistente:** mantenibile come fonte/categoria ma non come unità universale, perché escluderebbe siti greenfield.
- **Area/poligono:** adeguata come unità principale.
- **Area + punti ausiliari:** proposta preferita perché conserva la realtà areale e supporta routing/calcoli puntuali senza confondere i ruoli.

## 6. Decisioni richieste all’utente

Le seguenti decisioni restano **PROPOSED**:

- **F2-D1:** unità elementare = area/poligono fisicamente localizzabile con punti ausiliari separati;
- **F2-D2:** multipart disconnessi separati di default, salvo continuità operativa documentata;
- **F2-D3:** punto rappresentativo interno per usi descrittivi; centroide non default e mai accesso implicito;
- **F2-D4:** accessi multipli mantenuti; routing da accesso;
- **F2-D5:** canonicalizzazione obbligatoria di overlap/duplicati con lineage;
- **F2-D6:** ID logico stabile separato da versione e geometry hash;
- **F2-D7:** nessuno split automatico per confine comunale;
- **F2-D8:** nessuna tolleranza geometrica numerica fissata in Fase 2; derivazione dalla qualità dei dati in Fase 3–4.

Non sono state registrate come ACCEPTED/FROZEN nel PROJECT_CONTROL_REGISTER.

## 7. Elementi deliberatamente rinviati

Restano fuori dalla decisione Fase 2:

- dataset definitivo dei poligoni;
- EPSG operativo definitivo;
- tolleranze quantitative di snap/merge/overlap;
- soglia minima di superficie;
- categorie urbanistiche ammissibili;
- algoritmo definitivo di generazione accessi;
- rete stradale definitiva;
- indicatori, pesi, normalizzazione e ranking.

## 8. Controlli effettuati

- lettura integrale dispatch: PASS;
- lettura integrale baseline Fase 1 FROZEN: PASS;
- lettura integrale roadmap locale: PASS;
- verifica PROJECT_SOURCE_OF_TRUTH: PASS;
- verifica PROJECT_CONTROL_REGISTER: PASS — nessuna decisione F2 preesistente;
- verifica SESSION CLOSE PROCEDURE V1: PASS;
- coerenza con perimetro del dispatch: PASS;
- assenza di soglie arbitrarie introdotte: PASS;
- separazione area / punto rappresentativo / accesso: PASS;
- Fase 1 non modificata: PASS;
- `git diff --cached --check` sul review: PASS.

## 9. Git

Commit del review:

`168d7128669228ec8c87ac633129c56066e97faf` — `docs: propose Phase 2 unit of analysis`

Staging eseguito in modo esplicito sul solo artifact previsto.

Al momento della preparazione dell’handoff il branch `main` risultava avanti di 1 commit rispetto a `origin/main`.

## 10. SESSION CLOSE — change-driven

`NOTEBOOK_CHANGE = NO`

Motivo: il notebook legacy non è fonte autorevole del nuovo progetto 5 HUB e nessun aggiornamento è richiesto dalla nuova architettura.

`REGISTER_CHANGE = NO`

Motivo: non è stata approvata alcuna nuova decisione metodologica; PROJECT_CONTROL_REGISTER e PROJECT_SOURCE_OF_TRUTH devono essere aggiornati dalla regia solo dopo decisione dell’utente.

`GIT_COMMIT_REQUIRED = YES`

Motivo: sono stati creati documenti metodologici versionabili nel repository ufficiale.

Artifact interessato:

- `docs/FASE_2_UNIT_ANALYSIS_REVIEW_v01.md` — stato REVIEW / NON FROZEN;
- `docs/HANDOFF_CHAT_2.1_20260918.md` — handoff operativo.

Hash/preservation aggiuntivi: N/A per documentazione leggera versionata in Git.

## 11. Problemi aperti

Nessun problema tecnico bloccante.

Il blocco metodologico residuo è intenzionale: F2-D1…F2-D8 richiedono approvazione esplicita dell’utente prima di una baseline consolidata Fase 2.

## 12. Stato finale e prossimo passo

**Chat 2.1: PASS tecnico-operativo.**

Questo PASS attesta il completamento del mandato della chat, non l’approvazione delle proposte.

**FASE 2 resta REVIEW / IN CORSO.**

Prossimo passo suggerito alla Chat Madre:

1. sottoporre F2-D1…F2-D8 all’utente;
2. registrare le decisioni approvate nel PROJECT_CONTROL_REGISTER;
3. produrre un consolidato Fase 2 solo dopo approvazione;
4. non aprire Fase 3 finché Fase 2 non viene formalmente PASS / CLOSED dalla Chat Madre.
