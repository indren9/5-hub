# DISPATCH — Chat 3.3 — Rete stradale, accessi e TEN-T

**Fase:** 3 — Inventario e validazione dei dati
**Data:** 2026-09-18
**Stato mandato:** AUTHORIZED
**Regia:** Chat Madre 5 HUB

## 1. Obiettivo

Validare le fonti P2 necessarie alla futura catena **poligono candidato → access point → road anchor → rete stradale → uscita/nodo TEN-T**, senza costruire ancora accessi dei candidati né calcolare distanze per `CANDIDATES_RAW`.

La chat deve stabilire se il Grafo stradale FVG è tecnicamente idoneo al routing Light/Heavy e quale rappresentazione TEN-T corrente e tracciabile usare come fonte.
## 2. Baseline vincolanti e input

READ ONLY:
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md` — FROZEN;
- `docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md` — REVIEW/PASS tecnico Chat 3.1;
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER.

Issue prioritarie:
- `ISS-0004` — Grafo FVG non validato per routing Light/Heavy;
- `ISS-0005` — TEN-T corrente a tre livelli non materializzata/validata.

L'OD/routing storico della tesi e le baseline Claude/QGIS possono essere usati solo come benchmark tecnico, non come fonte autorevole del nuovo progetto.
## 3. Rete stradale — verifiche obbligatorie

Sul `RETI_TRASP:GRAFO_STRADALE_FVG`:
- acquisire/metadocumentare versione corrente, CRS, schema e licenza;
- verificare topologia: nodi/intersezioni, segmentazione, dangling, sovrapposizioni e disconnessioni rilevanti;
- interpretare e testare `DIR` e ogni attributo di transitabilità/allowance;
- verificare coerenza one-way su un campione controllabile con fonti ufficiali/gestori quando disponibili;
- verificare connettività e raggiungibilità su casi rappresentativi FVG;
- distinguere ciò che consente routing Light da ciò che richiede dati Heavy ulteriori;
- censire restrizioni Heavy ottenibili: classi, sagoma, peso, divieti, gestori, limitazioni locali;
- quantificare errori/anomalie osservate e documentare procedure di correzione ammissibili senza applicarle alla futura baseline senza approvazione.

Nessun nearest-road cieco è ammesso come surrogato dell'accesso candidato.
## 4. TEN-T — verifiche obbligatorie

- usare come riferimento normativo corrente il Reg. (UE) 2024/1679 e fonti DG MOVE/TENtec;
- materializzare o identificare una geometria corrente per FVG coerente con **core / extended core / comprehensive**;
- documentare data/versione, layer, CRS, licenza e lineage;
- verificare quali strade FVG ricadono nei tre livelli e come sono rappresentati nodi urbani, porti e rail-road terminals;
- spiegare eventuali differenze fra servizi TENtec legacy a due livelli e tassonomia vigente;
- definire una procedura riproducibile per ottenere l'insieme delle **uscite/svincoli TEN-T rilevanti** senza riusare automaticamente le 23 uscite storiche;
- non decidere qui quali livelli TEN-T debbano concorrere a specifici criteri del modello oltre quanto già imposto da Fase 1/normativa: eventuali scelte interpretative sostanziali vanno riportate alla Chat Madre come `Q-METH`.
## 5. Requisiti dati per accessi

Senza generare accessi reali dei candidati, definire il contratto dati minimo futuro per:
- `access_point` sul/per il perimetro candidato;
- `road_anchor` sulla rete;
- connector access_point→road_anchor;
- stato validazione accesso;
- classe Light/Heavy;
- fonte/evidenza;
- eventuali accessi multipli per candidato;
- gestione di accessi impossibili/non validabili.

La specifica deve restare coerente con F2-D4 FROZEN.
## 6. Divieti

NON:
- costruire `CANDIDATES_RAW`;
- generare accessi per candidati non ancora esistenti;
- calcolare ranking o indicatori;
- fissare soglie geometriche arbitrarie;
- assumere che `DIR` o allowance siano corretti senza test;
- riusare automaticamente il set storico di 23 uscite TEN-T;
- ridurre TEN-T alla vecchia tassonomia core/comprehensive;
- dichiarare Heavy routabile se le restrizioni necessarie non sono coperte.

## 7. Output atteso

`docs/FASE_3_ROAD_TENT_VALIDATION_REVIEW_v01.md`

Deve contenere:
- audit tecnico del grafo FVG;
- test e metriche di topologia/connettività/direzioni;
- matrice di copertura Light/Heavy;
- fonte TEN-T corrente e mapping FVG a tre livelli;
- procedura proposta per exit set;
- contratto dati access/anchor/connector;
- stato `ISS-0004` / `ISS-0005` e nuovi gap;
- questioni sostanziali da sottoporre alla Chat Madre.
## 8. Quality gate

PASS tecnico-operativo solo se:
- routing Light sul grafo è supportato da evidenza o dichiarato non idoneo con motivazione;
- per Heavy è chiaro quali restrizioni sono coperte e quali no;
- classificazione TEN-T corrente a tre livelli per FVG è tracciabile a fonte ufficiale;
- il futuro exit set ha una procedura riproducibile e lineage chiara;
- nessun accesso candidato è stato inventato;
- nessuna soglia o scelta metodologica sostanziale è stata congelata;
- dataset/materializzazioni sono registrati con metadati e hash dove appropriato;
- SESSION CLOSE e handoff sono completi.

La chat può proporre `ISS-0004`/`ISS-0005` RESOLVED solo con evidenza sufficiente; la Chat Madre verifica prima dell'accettazione.
