# RELATION PENDING DECISIONS — RESOLUTION LOG v01

**Data apertura:** 2026-09-21
**Stato:** ACTIVE

Questo file registra le decisioni utente emerse dalla review degli stralci della relazione preesistente.

## DEC-0067 — BESS

**Stato:** ACCEPTED

Decisione:
il BESS resta opzionale e non entra nel nucleo minimo obbligatorio dei cinque Hub.

Motivazione:
ai fini del MODEL_v2 di pianificazione territoriale, la presenza di un BESS non è considerata discriminante per localizzazione, ammissibilità o configurazione dei siti.

Effetti:
- nessun hard filter;
- nessun indicatore o score dedicato;
- nessun effetto sulla selezione della cinquina;
- possibile integrazione progettuale successiva senza modificare la baseline territoriale.

## DEC-0068 — Elettrolizzatore

**Stato:** ACCEPTED

Decisione:
ogni Hub deve integrare un elettrolizzatore in sito.

Trattamento nel MODEL_v2:
il requisito è funzionale ma territorialmente neutro. Non genera hard filter, score, modifica dell'universo candidato o vincoli aggiuntivi della cinquina.

Restano post-model/progettuali:
- potenza e dimensionamento;
- layout e sicurezza;
- connessione elettrica reale;
- configurazione esecutiva dell'approvvigionamento H2.

DEC-0068 supersede F1-D6 / DEC-0011 limitatamente alla non obbligatorietà dell'elettrolizzatore.

## DEC-0069 — Ruolo AFIR/TEN-T e infrastrutture H2

**Stato:** ACCEPTED

Decisione:
- AFIR/TEN-T è criterio primario della qualità del singolo candidato;
- la soglia H2 di 10 km stradali dalla TEN-T exit stabilisce se una localizzazione può concorrere alla copertura AFIR, ma non è hard filter universale;
- la cinquina finale deve soddisfare i vincoli AFIR applicabili;
- il requisito massimo di 200 km opera a livello di copertura/configurazione e non come distanza minima tra Hub;
- la presenza di infrastrutture H2 esistenti/programmate è un criterio positivo separato;
- Monfalcone Lisert può essere valorizzata come opportunità di integrazione/potenziamento, senza essere automaticamente AFIR-compliant né automaticamente uno dei cinque Hub.

Restano pendenti formula raw, normalizzazione, peso, aggregazione e formalizzazione computazionale dei vincoli di configurazione.

## DEC-0070 — Architettura di scoring

**Stato:** ACCEPTED / REFINED BY DEC-0086

Decisione originaria preservata:
- una volta definito l'universo candidato non è prevista una seconda fase ordinaria di eliminazione site-level;
- ogni criterio riceve importanza intera 1–5;
- i valori di importanza vengono convertiti in pesi percentuali normalizzati;
- gli indicatori vengono normalizzati prima dell'aggregazione;
- la cinquina deve comunque rispettare i vincoli di configurazione approvati.

La formulazione originaria `S_i = Σ_j(w_j z_ij)` seguita da `Q=(1/5)Σ_iS_i` è stata raffinata da DEC-0086 perché il MODEL_v2 include anche un criterio configuration-level di copertura territoriale. La formulazione operativa corrente è quindi quella definita in DEC-0086 / `SCORING_ARCHITECTURE_MODEL_v2_v02.md`.

## DEC-0071 — Macro-aree e top-k solo come fallback computazionale

**Stato:** ACCEPTED

Decisione:
la metodologia ordinaria di selezione delle cinquine non usa macro-aree, vincolo uno-per-area o preselezione top-k.

Tali strumenti possono essere introdotti solo come ultima risorsa se la selezione sull'universo completo risulta eccessivamente onerosa dal punto di vista computazionale.

Condizioni per l'eventuale fallback:
- problema computazionale dimostrato;
- semplificazione esplicitamente documentata;
- confronto/sensitivity rispetto alla ricerca non ridotta o a benchmark adeguati;
- quantificazione del rischio di perdere la soluzione migliore.

Le ipotesi top-10/top-5 e i conteggi 100.000/3.125 combinazioni restano esempi di fallback e non metodologia corrente.

## DEC-0072 — AFIR senza score di distanza; criterio flussi veicolari

**Stato:** ACCEPTED

Decisione:
- nessun punteggio individuale basato sulla distanza dalla TEN-T;
- AFIR/TEN-T resta vincolo della cinquina;
- il criterio site-level sostitutivo è il flusso veicolare intercettabile;
- maggiore traffico rilevante intercettabile = maggiore punteggio;
- formula raw, segmento/rete di riferimento, ruolo della prossimità/accessibilità e normalizzazione restano da definire.

Motivazione:
evitare doppio conteggio tra prossimità normativa alla TEN-T e conformità AFIR della configurazione.

## DEC-0073 — Raggio di ricerca flussi = 5 km

**Stato:** ACCEPTED

Decisione:
- per ogni candidato si cercano gli archi con dati di flusso entro **5 km dal bordo del poligono**;
- i 5 km costituiscono una finestra di ricerca, non uno score;
- la distanza dovrà incidere tramite una funzione di penalizzazione ancora da definire;
- è ammessa una sensitivity sul raggio per verificare la robustezza della scelta;
- il raggio baseline resta 5 km salvo futura successor decision;
- Light e Heavy restano distinti.

Restano aperti la funzione di distanza, l'aggregazione tra più archi e la gestione dei candidati senza archi utili entro 5 km.

## DEC-0074 — Formula raw dei flussi veicolari intercettabili

**Stato:** ACCEPTED

Decisione:
- per ogni arco entro 5 km dal candidato: `f(d)=1-d/5`, con d in km;
- contributo arco: `V=q*f(d)`;
- valore raw candidato: massimo `V` tra gli archi nella finestra;
- se non esistono archi utili entro 5 km, valore raw = 0;
- calcolo separato per Light e Heavy;
- distanza geometrica misurata tra poligono e arco.

La sensitivity sul raggio resta ammessa. Restano da verificare gli artifact canonici dei flussi e da definire normalizzazione finale e valori di importanza/peso.

## DEC-0075 — HEAVY 2030 baseline dello score

**Stato:** ACCEPTED

Decisione:
- `heavy_vehicles_day_2030` è la baseline HEAVY del criterio traffico;
- `heavy_vehicles_day_2019` resta benchmark / sensitivity;
- la ricostruzione edge-flow resta deterministica per `Network_Edge_ID` da `HEAVY_PATH_FLOWS_v01.csv`;
- le limitazioni note dello scenario 2030, inclusa la mancata calibrazione locale su ANAS FVG, devono restare esplicite.

Motivazione:
allineamento temporale con l'orizzonte 2030 dei principali target H2 AFIR. Questa è una scelta metodologica del MODEL_v2, non un obbligo AFIR di usare traffico 2030.

## DEC-0076 — LIGHT Dirty FRLM baseline operativa

**Stato:** ACCEPTED

Decisione:
- `DIRTY_EDGE_FLOWS_v01.csv` è la baseline operativa LIGHT del criterio traffico nel MODEL_v2;
- campo flusso: `dirty_flow_veh_day`;
- join geometrico: `segment_uid` verso `G_OSM_operativo_segments_v01.segment_uid`;
- unità: veicoli/giorno;
- resta obbligatorio dichiarare che la sorgente è DEMONSTRATOR / NON CANONICAL rispetto alla Tesi e non rappresenta la matrice LIGHT finale/calibrata.

La decisione non modifica raggio, formula raw o separazione Light/Heavy già approvati.

## DEC-0077 — normalizzazione flussi rispetto al massimo della rete

**Stato:** ACCEPTED

Decisione:
- per ogni rete il flusso edge viene normalizzato come `q_e / q_max`;
- `q_max` è il massimo flusso osservato sull'intera rete di riferimento LIGHT o HEAVY 2030, non nella sola finestra locale del candidato;
- lo score edge è `(q_e/q_max) * (1-d/5)`;
- lo score candidato è il massimo score edge tra gli archi entro 5 km;
- LIGHT e HEAVY 2030 restano separati;
- lo score ottenuto è già in [0,1] e non viene applicata una seconda normalizzazione.

La decisione completa la scala del criterio traffico senza modificare raggio, decadimento lineare o regola del massimo locale già approvati.

## DEC-0078 — criterio elettrico di prossimità alla cabina primaria

**Stato:** ACCEPTED

Decisione:
- `d_i` = distanza geometrica minima tra il poligono candidato e la cabina primaria più vicina;
- distanza misurata dalla geometria del poligono, non dal centroide;
- `d_max = max_i(d_i)` sull'intero universo candidati;
- score: `S_i_GRID = 1 - d_i/d_max`;
- nessuna soglia di distanza artificiale;
- la distanza è solo proxy di costo/complessità potenziale della connessione.

Restano fuori dal MODEL_v2: capacità disponibile, capacità residua, punto di connessione, opere necessarie, costo effettivo e fattibilità reale, da verificare post-model con il gestore.

## DEC-0079 — baseline logistica/industriale operativa

**Stato:** ACCEPTED

Decisione:
- `LOGISTICS_FVG_v02.gpkg / LOGISTICS_FVG_POINTS` è la baseline operativa del MODEL_v2 per il criterio logistico-industriale;
- 26 `SITE_ID` univoci, geometrie POINT, EPSG:32632;
- per ciascun candidato si costruisce la matrice completa delle distanze verso tutti i 26 poli;
- in questa fase non sono approvati soglie, pesi, bonus o aggregazione in score;
- `SITE_ID 25 — ZIMA` mantiene `NEEDS_HUMAN_CHECK`;
- lo stato Tesi resta PASS_WITH_LIMITATION / WORKING / NOT FROZEN.

## DEC-0080 — score logistico-industriale sui 2 poli più vicini

**Stato:** ACCEPTED

Decisione:
- per ogni candidato si ordinano le 26 distanze verso i poli della baseline DEC-0079;
- si prendono le due minori `d_i(1)` e `d_i(2)`;
- `D_i = (d_i(1)+d_i(2))/2`;
- `D_max = max_i(D_i)` sull'intero universo candidati;
- score: `S_i_LOG = 1 - D_i/D_max`;
- nessuna soglia, bonus o peso per tipologia di polo.

Il criterio premia i candidati ben posizionati rispetto ad almeno due poli mantenendo una formulazione semplice e data-driven.

## DEC-0081 — accessibilità stradale fuori dal MODEL_v2

**Stato:** ACCEPTED

Decisione:
- nessun criterio dedicato di accessibilità/classe della strada servente;
- nessuno score e nessun flag dedicato nel MODEL_v2;
- accesso locale effettivo, geometria di accesso, svincoli e verifiche progettuali restano post-model sui finalisti;
- nessuna metrica sostitutiva viene introdotta.

## DEC-0082 — PGRA/alluvioni come criterio numerico

**Stato:** ACCEPTED IN PRINCIPLE

Decisione:
- PGRA/alluvioni resta un criterio numerico separato;
- per ogni candidato si considera la quota di superficie ricadente nelle classi PGRA;
- le classi saranno ordinate dalla meno critica alla più critica e normalizzate in [0,1];
- lo score sarà la media pesata per superficie delle classi intersecate;
- la mappatura concreta classe→score resta da chiudere dopo verifica delle classi effettivamente disponibili.

## DEC-0084 — scala PGRA/alluvioni

**Stato:** ACCEPTED

Decisione:
- fuori P1–P3B = `1,00`;
- P1 / P1_ST / P1_SM = `0,75`;
- P2 = `0,50`;
- P3A = `0,25`;
- P3B = `0,00`;
- score candidato = media pesata per superficie delle classi intersecate;
- sulle sovrapposizioni prevale la classe peggiore;
- `AA` (Zona di Attenzione) e `F` (Area fluviale) restano informazioni/flag separati e non entrano nella graduatoria.

`P1_ST` e `P1_SM` sono sottotipi della P1 moderata secondo lo stile ufficiale SIGMA corrente.

## DEC-0083 — PAI/frane sospeso

**Stato:** ACCEPTED / SUSPENDED

Decisione:
- PAI/frane non entra per ora nello scoring del MODEL_v2;
- motivo: manca una baseline vettoriale unica, completa e corrente con lineage normativo sufficiente;
- i layer CATFRANE / UTIL_TER / IFFI restano SUPPORT_ONLY / CONTEXT e non sostituiscono il PAI vigente;
- nessuna penalità o proxy sostitutiva viene introdotta;
- il criterio potrà essere riaperto solo con una baseline vettoriale ufficiale o equivalente sufficientemente completa e versionata.

## DEC-0085 — baseline e score H2 core

**Stato:** ACCEPTED

Decisione:
- `H2_FVG_INFRASTRUCTURE_INVENTORY_v01.csv` è baseline fattuale H2 del MODEL_v2;
- target spaziali iniziali dello score: Trieste, Monfalcone/Lisert, Porpetto, ABS;
- `d_i^H2 = min_j(d_ij)` sui target point-ready;
- `d_max^H2 = max_i(d_i^H2)` sull'universo candidati;
- `S_i^H2 = 1 - d_i^H2/d_max^H2`;
- nessuna soglia, nessun peso per status e nessun bonus per numero di siti;
- SOLHX resta nella baseline ma fuori dai calcoli di distanza finché non viene localizzato puntualmente;
- testbed e `ANNOUNCED_UNVERIFIED` non entrano nello score core;
- al 2026-09-22 nessun core site è `OPERATIONAL`.

## DEC-0086 — architettura della funzione obiettivo della cinquina

**Stato:** ACCEPTED

Decisione:
- il MODEL_v2 resta single-objective;
- per ogni criterio site-level `j` si calcola sulla cinquina `Z_j(H)=(1/5)Σ_{i∈H} z_ij`;
- la copertura territoriale è un criterio distinto calcolato direttamente sulla configurazione e rappresentato da `Z_COV(H)`;
- tutti i criteri entrano una sola volta nella ponderazione finale;
- funzione obiettivo: `Q(H)=[Σ_j r_j Z_j(H)+r_COV Z_COV(H)]/[Σ_j r_j+r_COV]`, equivalente a pesi normalizzati;
- nessun secondo obiettivo autonomo e nessun fronte di Pareto;
- i valori concreti di importanza 1–5 restano sospesi;
- formula raw e normalizzazione di `Z_COV(H)` restano da definire separatamente.

## DEC-0087 — copertura territoriale della cinquina

**Stato:** ACCEPTED

Decisione:
- il FVG viene rappresentato tramite griglia regolare;
- per ogni cella `g`, con centro `c_g`, si calcola `d_g(H)=min_{h∈H} d(c_g,h)`, con distanza euclidea minima in CRS metrico dal centro cella al poligono Hub;
- le celle di confine sono pesate per la sola area `a_g` ricadente nel FVG;
- `D_COV(H)=Σ_g a_g d_g(H)/Σ_g a_g`;
- `D_COV*=min_{|H|=5}D_COV(H)` sull'universo candidati;
- `Z_COV(H)=D_COV*/D_COV(H)`;
- la metrica misura distribuzione geografica pura, non accessibilità, domanda o popolazione;
- la dimensione operativa della griglia resta parametro tecnico da definire con verifica di convergenza/sensitivity.

## Decisioni ancora pendenti

La review dei nuovi appunti è sostanzialmente chiusa sul piano dei criteri site-level e della copertura territoriale della cinquina.

## DEC-0088 — eliminazione della distanza minima Hub–Hub

**Stato:** ACCEPTED

Decisione:
- non si applica alcun vincolo generale `d(h_i,h_j) ≥ 10 km` tra gli Hub selezionati;
- la soglia storica di 10 km non deriva da AFIR e non entra né come HARD constraint né come score;
- la distribuzione geografica della cinquina è valutata tramite `Z_COV(H)` secondo DEC-0087;
- resta soltanto il requisito logico che la cinquina contenga cinque candidati/localizzazioni distinti, senza trasformarlo in una soglia chilometrica.

## DEC-0089 — proxy progettuale dei nodi urbani

**Stato:** ACCEPTED

A seguito della Chat 5.2, il MODEL_v2 usa il confine amministrativo del Comune di Trieste come proxy operativa del nodo urbano di Trieste e il Comune di Udine come proxy operativa del nodo urbano di Udine. La cinquina deve contenere almeno un Hub in ciascuno dei due Comuni. La scelta è una assunzione progettuale esplicita e non una dichiarazione sul perimetro legale AFIR/TEN-T. `ISS-0017` è RESOLVED PROCEDURALLY; la limitazione resta documentata e va riaperta se emerge una delimitazione ufficiale applicabile.

## DEC-0090 — ruolo Monfalcone/Lisert

**Stato:** ACCEPTED

Per Monfalcone/Lisert il MODEL_v2 verifica la compliance territoriale AFIR lato distanza stradale alla nearest TEN-T exit (`<=10 km`). L'impianto Lisert documentato resta sotto `1 t/giorno`, ma il deficit di capacità è un requisito di progettazione/dimensionamento post-model e non un filtro localizzativo. Un Hub può essere nello stesso poligono dell'infrastruttura esistente, come integrazione/potenziamento, oppure in un poligono distinto vicino con la stessa funzione strategica. In entrambi i casi la verifica territorialmente rilevante nel modello si applica al candidato selezionato.

Restano da discutere separatamente:
- valori concreti di importanza 1–5 dei criteri, esplicitamente sospesi;
- formalizzazione computazionale della copertura TEN-T core / requisito massimo 200 km a livello di configurazione.
