# HANDOFF COMPLESSIVO — Chat 90.0 — Relazione Builder

**Data:** 2026-09-21
**Destinatario:** Chat 0.2 — Chat Madre 5 HUB
**Perimetro:** recepimento congiunto del mandato iniziale della Chat 90.0 e della successiva istruzione sull'uso della baseline storica Claude
**Stato:** RECEIVED / IMPLEMENTED EDITORIALLY / REVIEW BY CHAT 0.2

## 1. Ruolo della Chat 90.0

La Chat 90.0 è la regia editoriale e documentale della relazione esterna del progetto 5 HUB.

La sua responsabilità è costruire e mantenere una relazione destinata a un lettore terzo che non conosce:
- chat operative;
- codici DEC/ISS;
- branch;
- workflow interni;
- nomenclature tecniche non spiegate.

La relazione deve essere autosufficiente, leggibile, tecnicamente rigorosa, tracciabile e organizzata secondo una narrazione professionale simile a un paper tecnico, senza replicare meccanicamente la cronologia interna del progetto.

## 2. Autorità e limiti

La Chat 90.0 ha autorità editoriale, non metodologica.

Può:
- progettare indice e struttura;
- riorganizzare materiale approvato;
- sintetizzare e riscrivere contenuti tecnici;
- uniformare stile e terminologia;
- costruire tabelle, figure, schemi e apparati di riferimento;
- gestire fonti esterne e bibliografia;
- mantenere una matrice di tracciabilità;
- creare e coordinare chat figlie nel namespace Chat 90.x.

Non può:
- modificare metodologia;
- cambiare criteri, vincoli, indicatori, pesi o assunzioni;
- modificare definizioni FROZEN;
- promuovere DRAFT/PROPOSED/REVIEW a fatti consolidati;
- correggere implicitamente contraddizioni metodologiche;
- modificare artifact scientifici FROZEN.

Quando emerge un problema metodologico, la Chat 90.0 lo documenta e lo riporta alla Chat 0.2.

## 3. Gerarchia delle fonti interne

La relazione usa prioritariamente:
1. istruzioni persistenti del progetto;
2. PROJECT_SOURCE_OF_TRUTH;
3. PROJECT_CONTROL_REGISTER;
4. baseline FROZEN;
5. decisioni ACCEPTED;
6. review accettate;
7. DATA_REGISTRY;
8. artifact tecnici e handoff;
9. repository Git e storage tecnico;
10. materiale storico Claude/QGIS come supporto secondario.

Nel corpo principale si privilegiano contenuti FROZEN, ACCEPTED o tecnicamente validati e successivamente accettati.

## 4. Separazione dei riferimenti

La relazione deve mantenere due sistemi distinti.

### 4.1 Fonti esterne

Normativa, regolamenti, delibere, dataset, portali istituzionali, paper, report, cartografie, documentazione tecnica e fonti statistiche.

Queste fonti entrano nella bibliografia/sitografia/fonti della relazione.

### 4.2 Tracciabilità interna

Decisioni DEC, issue, baseline FROZEN, review, DATA_REGISTRY, artifact, handoff e commit Git.

Questi riferimenti confluiscono in una appendice dedicata di tracciabilità interna e non devono essere confusi con la bibliografia scientifica o normativa.

## 5. Architettura editoriale già prodotta

È stato creato uno skeleton esterno con:
- Executive summary;
- 19 capitoli tematici;
- sezione fonti esterne;
- appendice di tracciabilità interna.

La struttura evita di usare la numerazione delle fasi come principale narrazione.

Readiness attuale:
- READY: capitoli 1, 3, 4;
- PARTIAL: Executive summary; capitoli 2, 5, 6, 8, 9, 10, 11, 18;
- NOT_READY: capitoli 7, 12, 13, 14, 15, 16, 17, 19.

La classificazione è editoriale e non modifica lo stato metodologico del progetto.

## 6. Uso autorizzato della baseline storica Claude

La Relazione Builder è autorizzata a consultare il precedente progetto Claude come archivio storico intelligente.

Il materiale Claude può essere usato come:
- baseline storica;
- fonte di idee editoriali;
- pista per recuperare fonti originali;
- riferimento per vecchie elaborazioni, tabelle, figure o risultati;
- termine di confronto con il nuovo progetto.

Può essere utile per recuperare:
- strutture narrative;
- testi tecnici da verificare;
- riferimenti bibliografici o normativi;
- dataset e portali già individuati;
- figure, mappe o tabelle ricostruibili;
- risultati storici da confrontare con il nuovo modello.

## 7. Limiti tassativi sull'uso di Claude

Claude NON è Source of Truth.

Nessun dato, metodologia, assunzione, risultato, graduatoria o conclusione proveniente da Claude può essere presentato come corrente senza verifica.

Quando si recupera un elemento Claude:
1. identificare, quando possibile, la fonte originale;
2. verificare fonte o contenuto contro lo stato corrente del progetto;
3. usare la versione validata del nuovo progetto quando disponibile;
4. se non verificabile, mantenere il contenuto come HISTORICAL / NON_VALIDATED;
5. non usare Claude per modificare o reinterpretare elementi ACCEPTED o FROZEN.

In caso di conflitto prevalgono sempre governance e baseline correnti del progetto.

## 8. Implicazioni editoriali concrete

Nel corpo della relazione:
- Claude può suggerire struttura o formulazioni, ma il claim fattuale deve essere riancorato a una fonte corrente o a governance valida;
- vecchi risultati Claude possono apparire solo come confronto storico esplicito;
- figure/tabelle Claude possono essere ricostruite solo dopo verifica di fonte, significato e dati;
- riferimenti bibliografici recuperati da Claude devono essere verificati sulla fonte originale prima di entrare nel registro esterno.

Nella tracciabilità interna:
- Claude può essere registrato come origine storica o pista di recupero;
- la fonte autorevole finale resta separata;
- un elemento non validato non può sostenere da solo un claim corrente.

## 9. Artifact persistenti creati

Cartella editoriale:
docs/relazione/

File:
- RELATION_ARCHITECTURE_v01.md
- RELATION_TRACEABILITY_MATRIX_v01.csv
- EXTERNAL_SOURCE_REGISTER_TEMPLATE_v01.csv
- EDITORIAL_GAPS_v01.md
- README.md
- HANDOFF_CHAT_90.0_RELATION_ARCHITECTURE_v01.md
- CLAUDE_BASELINE_EDITORIAL_USE_v01.md
- HANDOFF_CHAT_90.0_MANDATE_AND_CLAUDE_BASELINE_v01.md

Il file CLAUDE_BASELINE_EDITORIAL_USE_v01.md formalizza la nuova regola di consultazione Claude senza modificarne lo stato HISTORICAL / NON_AUTHORITATIVE nel DATA_REGISTRY.

## 10. Stato Git e isolamento operativo

Il lavoro editoriale vive sul branch:
chat-90.0-relation-architecture

Worktree:
C:\dev\5-hub-chat90

Questa scelta evita interferenze con il branch scientifico Chat 3.12 attualmente in lavorazione nel repository principale.

Commit precedenti:
- 37b567c0ec1263941113d5c9c646dd57014c4ec8 — architettura editoriale;
- eaad0213d23e1b2166d7ad56b6f2269d8971b635 — handoff architettura.

La nuova regola Claude e questo handoff devono essere committati sullo stesso branch.

## 11. Gap da preservare

Restano aperti, tra gli altri:
- Fase 3 non ancora chiusa;
- ISS-0013 Natura 2000 ancora in corso;
- ISS-0009 proprietà/disponibilità region-wide;
- ISS-0002 sull'universo storico Claude/QGIS;
- universo candidati non costruito;
- indicatori, metriche, soglie, pesi e normalizzazione non definiti;
- modello di selezione dei 5 Hub non ancora definito;
- robustezza, risultati e verifiche finali ancora assenti.

L'autorizzazione a consultare Claude non chiude nessuno di questi gap.

## 12. Chat 90.x consigliate dopo review

- Chat 90.1 — Fonti esterne e bibliografia.
- Chat 90.2 — Matrice di tracciabilità interna.
- Chat 90.3 — Redazione capitoli consolidati F1/F2.
- Chat 90.4 — Figure e tabelle, da attivare più avanti.

Le chat 90.x restano editoriali e non hanno autorità metodologica.

## 13. Quality gate del recepimento

- Mandato editoriale Chat 90.0 recepito: PASS.
- Autorità/limiti separati correttamente: PASS.
- Fonti esterne e tracciabilità interna separate: PASS.
- Uso Claude formalizzato come storico/supporto e non autorevole: PASS.
- Nessuna modifica a FROZEN/ACCEPTED: PASS.
- Nessuna nuova decisione metodologica introdotta: PASS.
- Persistenza su repository editoriale: PASS dopo commit.
- Review Chat 0.2 richiesta prima della redazione massiva: confermata.

## 14. Prossimo passo

La Chat 90.0 resta ferma sulla redazione massiva fino alla review della Chat 0.2.

Dopo review positiva, il primo blocco consigliato è:
1. Chat 90.1 — costruzione registro fonti esterne;
2. Chat 90.2 — consolidamento tracciabilità interna;
3. Chat 90.3 — redazione dei capitoli READY basati su Fase 1 e Fase 2.
