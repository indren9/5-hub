# HANDOFF — Chat 90.0 — Relazione Builder

**Data:** 2026-09-21  
**Destinatario:** Chat 0.2 — Chat Madre 5 HUB  
**Attività:** primo incarico — architettura della relazione esterna  
**Stato proposto:** TECHNICAL/EDITORIAL PASS — REVIEW REQUIRED

## 1. Obiettivo svolto

È stata progettata l'architettura della relazione esterna senza redigere massicciamente i capitoli.
La struttura è orientata a un lettore terzo e non replica la sequenza cronologica delle chat o delle fasi interne.

Sono stati ricostruiti lo stato autorevole del progetto, i contenuti FROZEN/ACCEPTED disponibili e i blocchi non ancora scrivibili.

## 2. Stato progetto usato come baseline editoriale

- Fase 1: PASS / CLOSED / FROZEN.
- Fase 2: PASS / CLOSED / FROZEN.
- Fase 3: IN CORSO.
- Fase 4 e successive: non aperte.
- PROJECT_CONTROL_REGISTER verificato fino a DEC-0059.
- ISS-0013: OPEN, con Chat 3.12 in corso.
- ISS-0009: OPEN come gap dati region-wide di proprietà/disponibilità.
- ISS-0002: OPEN sulla ricostruibilità dell'universo storico Claude/QGIS.
- Output non revisionati della Chat 3.12 esclusi dal contenuto consolidato.

## 3. Struttura proposta

La relazione è organizzata in 19 capitoli principali più Executive summary, fonti esterne e appendice di tracciabilità interna.

Blocchi principali:
1. contesto e obiettivi;
2. quadro normativo;
3. definizione degli Hub;
4. unità di analisi;
5. dati e qualità;
6. architettura del metodo;
7. universo candidati;
8. ammissibilità;
9. accessibilità/TEN-T/domanda;
10. fattibilità energetica;
11. vincoli territoriali e ambientali;
12. indicatori;
13. normalizzazione/pesi/ranking;
14. selezione della configurazione di 5 Hub;
15. robustezza;
16. risultati;
17. verifica puntuale dei finalisti;
18. limiti e incertezza;
19. conclusioni.

Fonti esterne e tracciabilità interna sono separate esplicitamente.

## 4. Readiness sintetica

**READY:** Cap. 1, 3, 4.

**PARTIAL:** Executive summary; Cap. 2, 5, 6, 8, 9, 10, 11, 18.

**NOT_READY:** Cap. 7, 12, 13, 14, 15, 16, 17, 19.

La classificazione non modifica lo stato metodologico del progetto; serve solo a governare la redazione.

## 5. File creati

Target logico nel repository:
docs/relazione/

Artifact:
- RELATION_ARCHITECTURE_v01.md
- RELATION_TRACEABILITY_MATRIX_v01.csv
- EXTERNAL_SOURCE_REGISTER_TEMPLATE_v01.csv
- EDITORIAL_GAPS_v01.md
- README.md
- HANDOFF_CHAT_90.0_RELATION_ARCHITECTURE_v01.md

Artifact principali già commitati:
37b567c0ec1263941113d5c9c646dd57014c4ec8
— docs(relazione): define external report architecture

## 6. Gestione Git e isolamento

Il repository principale era sul branch chat-3.12-natura2000-prescreen-ruleset con file non committati della Chat 3.12.

Per non contaminare il lavoro scientifico in corso è stato creato un worktree separato:
C:\dev\5-hub-chat90

Branch:
chat-90.0-relation-architecture

Nessun file della Chat 3.12 è stato modificato, committato o incluso nel branch editoriale.

Dopo approvazione/review, il branch Chat 90.0 potrà essere integrato in main; a quel punto il percorso operativo ordinario sarà C:\dev\5-hub\docs\relazione\.

## 7. Quality checks

- git diff --check: PASS.
- Parsing RELATION_TRACEABILITY_MATRIX_v01.csv: PASS, 21 righe dati.
- Parsing EXTERNAL_SOURCE_REGISTER_TEMPLATE_v01.csv: PASS, 12 righe dati.
- UTF-8 RELATION_ARCHITECTURE_v01.md: PASS.
- Modifiche fuori docs/relazione: nessuna nel worktree Chat 90.0.
- Nessuna soglia, peso, indicatore o regola metodologica nuova introdotta.

## 8. Gap editoriali principali

- Fase 3 non chiusa.
- Natura 2000 rule-set ancora in corso.
- Universo candidati non costruito.
- Categorie operative, superficie minima e tolleranze non definite.
- Indicatori, metriche, soglie, pesi, normalizzazione e ranking non definiti.
- Modello di selezione dei 5 Hub non definito.
- Robustezza e risultati assenti.
- Verifiche puntuali finalisti non eseguite.
- Registro bibliografico esterno non ancora normalizzato.
- La precedente RELAZIONE_QUADRO_PROGETTO_5_HUB_v01.md è DRAFT e in parte superata dalle decisioni del 20 settembre; va usata solo come materiale editoriale da riesaminare.

## 9. Questioni metodologiche emerse

Nessuna nuova questione metodologica che richieda decisione è stata creata da questa attività.

Sono stati soltanto preservati come aperti i limiti già esistenti:
- urbanistica best-available con currentness non sempre verificata;
- proprietà/disponibilità region-wide incompleta;
- proxy elettrico senza capacità disponibile;
- Light/Heavy validi a scala macro ma non come prova di accessibilità locale;
- fallback PAI macro;
- Natura 2000 ancora da formalizzare operativamente.

## 10. Chat 90.x consigliate

Nessuna chat figlia è stata aperta in questa attività.

Dopo review positiva si consigliano:
- Chat 90.1 — Fonti esterne e bibliografia;
- Chat 90.2 — Matrice di tracciabilità interna;
- Chat 90.3 — Redazione capitoli consolidati F1/F2;
- Chat 90.4 — Figure, tabelle e registro visuale, da rinviare finché non esistono candidati/risultati.

## 11. Prossimo passo consigliato

Chat 0.2 revisiona:
1. indice;
2. readiness dei capitoli;
3. separazione fonti esterne / tracciabilità interna;
4. priorità delle prime chat 90.x.

Fino alla review non avviare la redazione massiva della relazione.

