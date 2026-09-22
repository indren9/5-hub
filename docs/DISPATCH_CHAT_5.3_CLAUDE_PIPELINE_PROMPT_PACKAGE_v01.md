# DISPATCH CHAT 5.3 — PROMPT E PACKAGE PIPELINE CLAUDE MODEL_v2

**Chat:** 5.3 — Prompt e package pipeline Claude MODEL_v2
**Regia:** Chat 0.2 — Chat Madre 5 HUB
**Data apertura:** 2026-09-22
**Stato:** DISPATCHED

## 1. Obiettivo

Preparare il materiale necessario per affidare a una pipeline Claude già esistente l'implementazione del MODEL_v2 per la localizzazione dei 5 Hub Energetici Green in Friuli Venezia Giulia.

La chat deve produrre:
1. il prompt/input finale destinato alla pipeline Claude;
2. il manifest dei file da includere nello ZIP di input;
3. solo dopo verifica del manifest, il package ZIP finale con i materiali realmente utili;
4. un handoff finale alla Chat 0.2.

Non deve riprogettare la metodologia del MODEL_v2.

## 2. Riferimento obbligatorio

Usare come riferimento stilistico e funzionale il file fornito dall'utente:

`INPUT_PIPELINE_CLAUDE_LIGHT_FVG.docx`

Il riferimento serve a capire scope, granularità, chiarezza, autonomia concessa alla pipeline, descrizione dei file, controlli, output e gestione delle limitazioni.

Non copiare meccanicamente contenuti LIGHT non pertinenti al MODEL_v2.

## 3. Principio di scrittura del prompt

Il prompt deve essere operativo e autosufficiente.

Non deve richiedere alla pipeline di conoscere la governance interna del progetto.

Evitare riferimenti non necessari a:
- codici DEC-*;
- numeri di chat;
- DQ-*;
- numerazione interna delle fasi;
- ragionamenti storici;
- alternative metodologiche superseded;
- discussioni interne della Chat Madre.

Tradurre invece ogni decisione approvata in regola operativa diretta.

Esempio:
- NON: `secondo DEC-0087...`
- SÌ: `la copertura territoriale della cinquina è calcolata come ...`

## 4. Materiale metodologico autorevole da leggere

Leggere almeno:
- `docs/SCORING_ARCHITECTURE_MODEL_v2_v02.md`
- `docs/CONFIGURATION_OBJECTIVE_ARCHITECTURE_v01.md`
- `docs/TRAFFIC_INTERCEPTABILITY_CRITERION_v01.md`
- `docs/GRID_PROXIMITY_CRITERION_v01.md`
- `docs/LOGISTICS_INDUSTRIAL_PROXIMITY_CRITERION_v01.md`
- `docs/PGRA_FLOOD_HAZARD_CRITERION_v01.md`
- `docs/H2_CORE_PROXIMITY_CRITERION_v01.md`
- `docs/AFIR_TENT_MODEL_ROLE_v02.md`
- `docs/CANDIDATE_UNIVERSE_CONTRACT_v01.md`
- `docs/RELATION_PENDING_DECISIONS_RESOLUTION_v01.md`
- `docs/REVIEW_CHAT_5.2_MOTHER_v01.md`

Verificare inoltre lo stato vivo di PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER.

## 5. Architettura da rappresentare nel prompt

Il MODEL_v2 deve:
- selezionare esattamente 5 poligoni candidati;
- usare i criteri site-level approvati;
- aggregare ogni criterio site-level sulla cinquina tramite media dei 5 Hub;
- calcolare la copertura territoriale direttamente sulla cinquina;
- usare una sola funzione obiettivo finale;
- applicare separatamente i vincoli / quality gate AFIR-TEN-T;
- non usare un vincolo generale minimo Hub-Hub di 10 km.

## 6. IMPORTANZE / PESI — REGOLA VINCOLANTE

NON assegnare valori ai criteri.

Il prompt finale deve contenere una sezione esplicita con i valori di importanza lasciati VUOTI per compilazione manuale dell'utente.

Formato consigliato:

```text
IMPORTANZA CRITERI — DA COMPILARE MANUALMENTE

LIGHT = ____
HEAVY = ____
GRID = ____
LOG = ____
PGRA = ____
H2 = ____
COVERAGE = ____
```

Non sostituire gli spazi vuoti con esempi numerici, default o valori suggeriti.

Specificare che i valori, una volta compilati, appartengono alla scala intera 1–5 e vengono normalizzati nella funzione obiettivo.

## 7. Copertura territoriale

Rappresentare direttamente la formula approvata:

`d_g(H) = min_{h∈H} d(c_g,h)`

`D_COV(H) = Σ_g a_g d_g(H) / Σ_g a_g`

`D_COV* = min_{|H|=5} D_COV(H)`

`Z_COV(H) = D_COV* / D_COV(H)`

Usare distanza geometrica euclidea in CRS metrico dal centro cella al poligono Hub più vicino.

Le celle di confine sono pesate per la sola area effettivamente ricadente nel FVG.

La dimensione pratica della griglia può essere definita tecnicamente dalla pipeline, ma deve essere verificata con sensitivity/convergenza e documentata.

## 8. Nodi urbani AFIR

Usare come ASSUNZIONE PROGETTUALE esplicita:
- Comune di Trieste = proxy operativa del nodo urbano TEN-T di Trieste;
- Comune di Udine = proxy operativa del nodo urbano TEN-T di Udine.

La configurazione deve quindi includere almeno un Hub nel Comune di Trieste e almeno un Hub nel Comune di Udine.

Specificare chiaramente che si tratta di proxy progettuali, non di perimetri legali AFIR/TEN-T.

## 9. Monfalcone/Lisert

Monfalcone/Lisert deve essere pienamente utilizzabile nel modello localizzativo.

Per il candidato Hub pertinente:
- verificare la compliance territoriale AFIR lato distanza stradale alla nearest TEN-T exit secondo la regola `<=10 km`;
- mantenere come informazione che l'impianto Lisert documentato è sotto il requisito di capacità `1 t/giorno`;
- NON dimensionare nel MODEL_v2 la capacità aggiuntiva;
- NON penalizzare o escludere la localizzazione per tale deficit;
- trattare il requisito di capacità come design requirement post-model.

Un Hub può coincidere con il poligono dell'infrastruttura esistente oppure essere localizzato in un poligono distinto vicino con la stessa funzione strategica.

## 10. Requisito AFIR 200 km

Il prompt deve impartire alla pipeline il requisito:

entro il perimetro normativo applicabile, verificare la copertura della TEN-T core rispetto alla distanza massima di 200 km tra le stazioni H2 conteggiate ai fini AFIR.

Non è richiesto alla Chat 5.3 progettare ora un nuovo algoritmo metodologico dedicato.

La pipeline deve usare i dati TEN-T disponibili nel package o altre fonti affidabili già disponibili al suo ambiente; se il requisito non è completamente valutabile, deve riportare chiaramente limitazioni, dati mancanti e quota di verifica effettivamente eseguita, senza bloccare il resto del modello.

## 11. Funzione obiettivo

Per ogni criterio site-level `j`:

`Z_j(H) = (1/5) * Σ_{i∈H} z_ij`

La funzione obiettivo finale, dopo compilazione manuale delle importanze, è:

`Q(H) = [Σ_j r_j Z_j(H) + r_COV Z_COV(H)] / [Σ_j r_j + r_COV]`

Ogni criterio entra una sola volta nella ponderazione finale.

Il MODEL_v2 resta single-objective.

## 12. Package ZIP

Non creare subito uno ZIP indiscriminato.

Prima produrre un manifest ragionato dei file realmente utili alla pipeline.

Includere solo materiale che serve per:
- universo candidati;
- geometrie e attributi necessari;
- criteri site-level;
- copertura territoriale;
- TEN-T / AFIR;
- proxy comunali Trieste/Udine;
- infrastrutture H2;
- QA / metadata necessari a interpretare i dati;
- eventuali script validati realmente utili.

Escludere salvo necessità motivata:
- chat;
- log completi di governance;
- documenti superseded;
- baseline Claude storica non necessaria;
- duplicati;
- output di presentazione;
- file che non influenzano direttamente esecuzione, controllo o interpretazione.

Ogni file proposto nel manifest deve avere:
- nome/path sorgente;
- ruolo nella pipeline;
- contenuto rilevante;
- CRS/unità se applicabili;
- layer/campi da usare se applicabili;
- stato/caveat essenziali;
- motivazione dell'inclusione.

## 13. Margine di manovra della pipeline

La pipeline può decidere autonomamente dettagli implementativi e computazionali che non alterano la metodologia approvata.

Può ad esempio:
- scegliere strutture dati;
- ottimizzare il calcolo;
- definire formati intermedi;
- scegliere la dimensione pratica della griglia previa sensitivity;
- implementare solver/euristiche efficienti;
- documentare assunzioni tecniche necessarie.

Non può:
- cambiare formule approvate;
- inventare nuovi criteri;
- assegnare pesi mancanti;
- riaprire scelte metodologiche approvate;
- trasformare limitazioni in fatti;
- sostituire dati mancanti con valori inventati.

## 14. Output della pipeline da specificare nel prompt

Il prompt finale deve richiedere almeno:
- tabella completa dei candidati con valori raw e score normalizzati per criterio;
- valori di cinquina per ciascun criterio;
- `D_COV` e `Z_COV`; 
- stato dei vincoli AFIR/TEN-T;
- score finale `Q(H)` per le configurazioni confrontate o per la shortlist rilevante;
- identificazione della cinquina selezionata;
- layer GIS dei 5 Hub selezionati;
- output tabellare machine-readable;
- report sintetico di assunzioni, limitazioni e controlli;
- sensitivity/robustness compatibile con i dati e parametri disponibili.

## 15. Quality gate Chat 5.3

PASS solo se:
- il prompt finale è leggibile senza conoscere la governance interna;
- tutti i dati/file citati sono descritti in modo operativo;
- nessun peso/importanza è inventato;
- gli spazi per i valori 1–5 sono chiaramente lasciati vuoti;
- formule e vincoli approvati sono trascritti senza alterazioni;
- le assunzioni progettuali sono distinte dai requisiti normativi;
- il requisito AFIR 200 km è impartito chiaramente;
- il manifest ZIP è minimale e motivato;
- il package finale, se creato, contiene solo materiale utile e tracciabile;
- prompt e package sono coerenti tra loro;
- controlli e limitazioni sono espliciti.

## 16. Procedura

Prima fase: studiare il prompt LIGHT e le baseline MODEL_v2.

Seconda fase: proporre struttura del prompt e manifest ZIP.

Terza fase: verificare coerenza con la governance corrente.

Quarta fase: produrre prompt finale e package soltanto quando la struttura è consolidata.

La Chat 5.3 non deve modificare decisioni metodologiche ACCEPTED/FROZEN. Eventuali conflitti reali devono essere riportati alla Chat 0.2.
