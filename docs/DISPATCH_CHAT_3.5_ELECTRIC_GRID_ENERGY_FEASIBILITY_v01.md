# DISPATCH — Chat 3.5 — Rete elettrica e fattibilità energetica

**Fase:** 3 — Inventario e validazione dei dati  
**Data:** 2026-09-20  
**Stato mandato:** AUTHORIZED  
**Regia:** Chat Madre 5 HUB

## 1. Obiettivo

Validare le migliori fonti disponibili per rappresentare, nel modello 5 HUB, la fattibilità elettrica dei siti senza confondere:
- presenza/prossimità della rete;
- livello di tensione;
- presenza di stazioni/cabine;
- richieste di connessione;
- capacità di connessione realmente disponibile.

La chat deve ridurre e, se possibile, chiudere `ISS-0007`: non esiste ancora nel progetto un dataset validato di capacità elettrica disponibile o di punto di connessione utilizzabile per i siti candidati.

La chat NON deve inventare una capacità disponibile a partire dalla sola distanza da linee, cabine, aree convenzionali o richieste di connessione.

## 2. Baseline vincolanti — READ ONLY

- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md` — FROZEN;
- `docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md`;
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER, in particolare:
  - `ISS-0007` — capacità elettrica / punto di connessione;
  - `F3_SRC_FVG_CP_001` — aree convenzionali cabine primarie;
  - `F3_SRC_TERNA_TERRA_001` — TE.R.R.A. Terna.

Principi FROZEN rilevanti:
- tutti i 5 Hub integrano ricarica elettrica DC pubblica;
- il modello deve considerare Light e Heavy;
- la disponibilità/adeguatezza dell'infrastruttura elettrica è fattore di fattibilità;
- non esiste una potenza elettrica universale già approvata per tutti gli Hub;
- compatibilità con uso diretto di energia rinnovabile richiesta, ma non implica produzione FER obbligatoria in sito.

## 3. Domande operative da risolvere

La Chat 3.5 deve rispondere con evidenza verificabile a queste domande:

1. Quali operatori di rete rilevanti coprono il Friuli Venezia Giulia e a quali livelli di tensione?
2. Quali dati ufficiali e correnti sono pubblicamente accessibili per:
   - rete di trasmissione;
   - rete di distribuzione;
   - stazioni/cabine primarie e, se utile, secondarie;
   - livelli di tensione;
   - aree servite;
   - richieste di connessione;
   - hosting capacity / capacità disponibile;
   - piani di sviluppo o potenziamento?
3. Esiste un dato pubblico region-wide che possa essere interpretato come capacità di connessione disponibile per un nuovo Hub?
4. Se non esiste, quali informazioni possono essere usate solo come proxy territoriale, con quale significato e con quali limiti?
5. Quali verifiche puntuali dovranno essere rinviate ai candidati finalisti o a richieste formali ai gestori?
6. Quali dati sono abbastanza affidabili da entrare nelle Fasi 4–6 e con quale ruolo: ammissibilità, attributo descrittivo, indicatore candidato o semplice supporto?

## 4. Gerarchia delle fonti

Priorità:
1. Terna e relativi portali/dataset ufficiali;
2. distributori di rete competenti (DSO) e relativi dataset/portali ufficiali;
3. ARERA / GSE / Regione FVG solo per informazioni di competenza effettivamente pertinenti;
4. altri dataset istituzionali come supporto;
5. fonti non istituzionali solo per cross-check, mai come unica base di capacità.

TE.R.R.A. deve essere verificato per:
- contenuto;
- granularità;
- data/versione;
- possibilità di export o acquisizione riproducibile;
- significato delle richieste di connessione;
- eventuale utilità GIS in FVG.

Il layer regionale `CER:AREECONVENZIONALI_CP` è già classificato come SCREENING_ONLY:
- non rappresenta necessariamente la posizione esatta della cabina primaria;
- non rappresenta capacità disponibile;
- non può essere promosso automaticamente a fonte energetica principale.

## 5. Separazione concettuale obbligatoria

Ogni dato deve essere classificato almeno in una delle seguenti categorie:

### A. INFRASTRUCTURE_GEOMETRY
Geometria fisica o territoriale di linee, stazioni, cabine, aree servite.

### B. NETWORK_ATTRIBUTE
Livello di tensione, tipologia impianto, gestore, stato, altri attributi tecnici osservati.

### C. CONNECTION_DEMAND
Richieste di connessione, code, progetti o domande pubblicate.

### D. CONNECTION_CAPACITY
Capacità realmente disponibile o tecnicamente allocabile per nuova connessione.

### E. PLANNED_REINFORCEMENT
Piani di sviluppo/potenziamento futuri.

### F. PROXY_ONLY
Dato utile allo screening ma non equivalente a capacità reale.

La chat deve impedire esplicitamente equivalenze del tipo:
- vicino a linea AT = capacità disponibile;
- dentro area convenzionale CP = capacità disponibile;
- presenza di cabina = connessione disponibile;
- poche richieste = capacità residua;
- piano di sviluppo = capacità già disponibile.

## 6. Capacità reale: regola prudenziale

Se non viene trovato un dataset pubblico, corrente e tecnicamente interpretabile di capacità disponibile:

- dichiarare `CONNECTION_CAPACITY_PUBLIC_DATA_NOT_AVAILABLE` o stato equivalente;
- NON stimare MW disponibili con formule arbitrarie;
- proporre, se utile, proxy separati e chiaramente denominati;
- indicare quali verifiche finali richiedano interlocuzione DSO/Terna, preventivo di connessione o altra procedura ufficiale.

Qualunque proposta di proxy che possa influenzare ranking, esclusione o pesi è solo PROPOSED e deve essere sottoposta alla Chat Madre.

## 7. Compatibilità con il modello Hub

La chat deve mantenere separati:
- fabbisogno elettrico dell'Hub;
- capacità della rete;
- distanza dalla rete;
- necessità di nuova cabina/trasformazione;
- possibilità di integrazione FER/BESS;
- eventuale elettrolisi H2, che in Fase 1 non è obbligatoria.

Non deve fissare una potenza universale in MW per i 5 Hub.

Può però costruire scenari tecnici o range di fabbisogno SOLO se:
- derivano dalle baseline approvate o da norme/fonti esplicite;
- sono marcati come scenari, non requisiti FROZEN;
- servono esclusivamente a capire quali dati di rete siano necessari.

## 8. Output obbligatori

Repository locale:
- `docs/FASE_3_ELECTRIC_GRID_ENERGY_VALIDATION_REVIEW_v01.md`;
- `docs/FASE_3_ELECTRIC_GRID_SOURCE_MATRIX_v01.csv`;
- `docs/FASE_3_ELECTRIC_GRID_VALIDATION_EVIDENCE_v01.json`;
- `docs/HANDOFF_CHAT_3.5_ELECTRIC_GRID_ENERGY_v01.md`;
- script/moduli leggeri necessari a discovery, acquisizione, QA e riproducibilità.

Storage tecnico pesante:
`5_HUB_FVG\02_external_sources\F3_CHAT_3_5\`

Per ogni artifact materializzato registrare almeno:
- fonte;
- URL;
- data di accesso;
- versione/data del dato se disponibile;
- byte;
- SHA-256;
- formato;
- CRS se geografico.

Branch dedicato:
`chat-3.5-electric-grid-energy`.

## 9. Aggiornamenti governance richiesti

La chat può aggiornare, con stati prudenti:
- DATA_REGISTRY per le fonti energetiche validate;
- ISS-0007 con evidenze e gap residuo.

Non può:
- chiudere autonomamente ISS-0007;
- approvare proxy energetici che influenzino scoring o ammissibilità;
- modificare Fase 1 o Fase 2 FROZEN;
- aprire Fase 4;
- fissare pesi o soglie di ranking.

Eventuali questioni metodologiche sostanziali devono essere formulate come `Q-METH-3.5-*` e restituite alla Chat Madre.

## 10. Quality gate

Il TECHNICAL_QUALITY_GATE può essere PASS solo se:

- operatori e fonti rilevanti per FVG sono inventariati con sufficiente copertura;
- le fonti ufficiali sono separate da fonti di supporto;
- currentness/versione e accessibilità sono documentate;
- dati geografici acquisiti hanno QA minimo di integrità, geometria e CRS;
- capacità reale e proxy sono chiaramente distinti;
- nessun proxy è presentato come MW disponibili;
- limiti di TE.R.R.A. e delle aree convenzionali CP sono espliciti;
- eventuali gap DSO sono attribuiti al gestore/territorio corretto;
- manifest/hash degli artifact materializzati sono verificati;
- F1/F2 FROZEN risultano invariati;
- Git e SESSION CLOSE / handoff sono completi.

## 11. ENERGY_READINESS

La chat deve restituire un giudizio separato:

### READY
Esiste una base dati sufficientemente affidabile e riproducibile per applicare il ruolo energetico previsto senza assunzioni sostanziali non approvate.

### READY_WITH_LIMITATIONS
La capacità reale non è disponibile region-wide, ma esiste una combinazione di dati ufficiali/proxy tecnici utilizzabile nello screening purché le limitazioni siano esplicite e la verifica puntuale sia obbligatoria sui finalisti. Questo stato richiede comunque approvazione metodologica della Chat Madre sui proxy.

### NOT_READY
Mancano dati o regole sufficienti anche per uno screening energetico difendibile.

ENERGY_READINESS non equivale all'apertura della Fase 4.

## 12. Criterio di successo

La Chat Madre deve poter rispondere senza ambiguità:

> “Che cosa sappiamo realmente della rete elettrica FVG, che cosa NON sappiamo sulla capacità disponibile e quale parte può essere automatizzata senza trasformare un proxy in un fatto?”

Il risultato deve rendere possibile una successiva decisione metodologica consapevole sulla fattibilità energetica, non produrre artificialmente una mappa di capacità che i dati non supportano.
