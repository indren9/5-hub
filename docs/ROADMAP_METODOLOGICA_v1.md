ROADMAP METODOLOGICA v1

STATO OPERATIVO — 2026-09-19

- FASE 0 — INIZIALIZZAZIONE DEL PROGETTO: PASS / CLOSED.
- FASE 1 — DEFINIZIONE DELL’OGGETTO “HUB ENERGETICO GREEN”: PASS / CLOSED / FROZEN.
- FASE 2 — DEFINIZIONE DELL’UNITÀ ELEMENTARE DI ANALISI: PASS / CLOSED / FROZEN.
- FASE 3 — INVENTARIO E VALIDAZIONE DEI DATI: IN CORSO — Chat 3.1, Chat 3.2, Chat 3.3, Chat 3.4 e Chat 3.7 PASS tecnico-operativo / review Chat Madre completata. Chat 3.7 ha validato il crosswalk stradale TEN-T FVG corrente; Chat 3.4 ha validato il blocco territoriale/ambientale, con ISS-0008 PPR RESOLVED, ISS-0011 biotopi RESOLVED proceduralmente e ISS-0006 PGRA ancora OPEN. Tutte le questioni metodologiche territoriali Q-METH-3.4-A…E sono ACCEPTED: PGRA DEC-0039; frane DEC-0040; Natura 2000 DEC-0041; parchi/riserve/biotopi/prati stabili DEC-0042; PPR DEC-0043. Chat 3.8 — Acquisizione e validazione urbanistica corrente FVG — AUTHORIZED con DEC-0044.
- FASI 4–15: NON AVVIATE.
- Attività corrente: Chat 3.8 esegue l'acquisizione/validazione urbanistica current-first Comune per Comune per ridurre ISS-0010 e produrre PHASE_4_READINESS; restano inoltre routing Light/Heavy, energia, dati di domanda e gap tecnici/dati già tracciati.

Nota: questo aggiornamento modifica esclusivamente lo stato di avanzamento. La metodologia della ROADMAP METODOLOGICA v1 resta invariata.

Scopo

Costruire in house un modello serio, riproducibile e verificabile per individuare 5 Hub Energetici Green in Friuli Venezia Giulia.

Il progetto Claude viene usato come baseline e fonte di materiale utile, non come metodologia da correggere alla cieca.

La logica deve essere:

definire cosa stiamo localizzando
→ definire l’unità di analisi
→ costruire i candidati
→ escludere ciò che non è ammissibile
→ valutare ciò che resta
→ scegliere la migliore configurazione di 5 siti
→ verificare quanto il risultato è robusto
→ approfondire i 5 siti scelti.

FASE 0 — INIZIALIZZAZIONE DEL PROGETTO

Obiettivo:
mettere in piedi l’ambiente di lavoro e le fonti autorevoli.

Attività:
- creare cartella dev;
- creare struttura OneDrive;
- creare repository Git;
- creare eventualmente repository GitHub;
- creare PROJECT_SOURCE_OF_TRUTH;
- creare PROJECT_CONTROL_REGISTER con DECISIONS, DATA_REGISTRY, ISSUES;
- caricare baseline Claude;
- verificare disponibilità della procedura SESSION CLOSE;
- definire naming e versionamento.

Output:
progetto operativo e tracciabile.

Gate:
PASS solo se è chiaro dove vive ogni componente del progetto.

FASE 1 — DEFINIZIONE DELL’OGGETTO “HUB ENERGETICO GREEN”

Obiettivo:
capire esattamente cosa stiamo cercando di localizzare.

Da definire:
- quali componenti sono obbligatorie;
- quali componenti sono opzionali;
- presenza obbligatoria o meno di idrogeno;
- ricarica elettrica;
- accumulo;
- produzione rinnovabile;
- eventuale elettrolisi;
- eventuali altri servizi;
- superficie minima necessaria;
- requisiti di accesso;
- requisiti energetici minimi;
- eventuali requisiti normativi.

Output:
definizione operativa dell’Hub.

Decisione da congelare:
configurazione minima dell’Hub da usare nel modello.

Gate:
non si procede se non sappiamo cosa deve fisicamente contenere il sito.

FASE 2 — DEFINIZIONE DELL’UNITÀ ELEMENTARE DI ANALISI

Obiettivo:
eliminare l’ambiguità tra area, punto, comune e impianto.

Da definire:
- cos’è un candidato;
- geometria del candidato;
- origine dei poligoni;
- quando si usa il poligono intero;
- quando si usa un punto rappresentativo;
- come viene scelto il punto rappresentativo;
- come vengono calcolate le distanze;
- come viene gestito l’accesso stradale;
- come vengono gestiti candidati contigui o sovrapposti.

Impostazione attesa:
l’unità elementare è un’area candidata fisicamente localizzabile.

Il punto rappresentativo è solo uno strumento di calcolo e non coincide automaticamente con la posizione futura dell’impianto.

Output:
specifica formale dell’unità di analisi.

Gate:
ogni indicatore deve avere una geometria di riferimento esplicita.

FASE 3 — INVENTARIO E VALIDAZIONE DEI DATI

Obiettivo:
capire cosa abbiamo realmente e cosa manca.

Per ogni dataset:
- fonte;
- data;
- versione;
- copertura territoriale;
- sistema di riferimento;
- qualità;
- scala;
- completezza;
- licenza;
- percorso;
- uso previsto;
- limiti.

Categorie minime:
- rete stradale;
- rete europea dei trasporti;
- nodi urbani;
- aree produttive e commerciali;
- porti;
- interporti;
- terminali logistici;
- rete ferroviaria se rilevante;
- popolazione;
- pendolarismo;
- turismo;
- aree interne;
- vincoli ambientali;
- frane;
- rischio idraulico;
- vincoli urbanistici;
- rete elettrica;
- cabine;
- linee;
- eventuale capacità disponibile;
- superfici disponibili.

Output:
DATA_REGISTRY verificato.

Gate:
nessun indicatore entra nel modello se non sappiamo da quale dato deriva.

FASE 4 — COSTRUZIONE DELL’UNIVERSO DEI CANDIDATI

Obiettivo:
costruire tutte le aree realisticamente candidabili.

Attività:
- definire le categorie urbanistiche ammissibili;
- costruire i poligoni;
- gestire contiguità e dissoluzione;
- applicare eventuali filtri territoriali preliminari;
- definire la superficie minima sulla base dell’Hub reale;
- evitare soglie arbitrarie non motivate;
- assegnare identificativo univoco a ogni candidato;
- salvare geometrie e attributi di base.

Output:
CANDIDATES_RAW_v01.

Importante:
questa fase non deve ancora attribuire punteggi.

Gate:
ogni candidato deve essere tracciabile fino ai dati sorgente.

FASE 5 — AMMISSIBILITÀ DEI SINGOLI SITI

Obiettivo:
eliminare ciò che non può essere scelto indipendentemente dal punteggio.

Possibili criteri:
- superficie insufficiente;
- incompatibilità urbanistica;
- distanza non conforme ai requisiti minimi di accessibilità;
- rischio da frana incompatibile;
- rischio idraulico incompatibile;
- vincoli ambientali realmente ostativi;
- impossibilità di accesso;
- altre condizioni tecniche indispensabili.

Regola:
un criterio di esclusione deve essere:
- esplicito;
- motivato;
- verificabile;
- applicato prima del ranking.

Output:
CANDIDATES_ADMISSIBLE_v01.

Per ogni esclusione:
- motivo;
- regola applicata;
- valore osservato;
- fonte.

Gate:
l’insieme delle alternative ammesse viene congelato prima della valutazione multicriteriale.

FASE 6 — DEFINIZIONE DEGLI INDICATORI

Obiettivo:
misurare la qualità dei candidati rimasti.

Ogni indicatore deve avere:
- significato;
- fonte;
- unità di misura;
- geometria di riferimento;
- formula;
- direzione preferenziale;
- eventuali soglie;
- trattamento dei valori mancanti;
- metodo di normalizzazione.

Macroaree indicative:
- accessibilità;
- domanda logistica;
- domanda industriale;
- domanda di mobilità;
- popolazione servita;
- turismo;
- aree interne;
- superficie disponibile;
- compatibilità territoriale;
- ambiente;
- rischio;
- fattibilità energetica;
- costo o complessità di connessione.

Regola:
non usare un indicatore solo perché il dato esiste.

Ogni indicatore deve rispondere a una domanda concreta.

Gate:
nessun indicatore con valore costante o quasi costante deve essere mantenuto come se fosse discriminante.

FASE 7 — FATTIBILITÀ ENERGETICA

Obiettivo:
evitare di chiamare Hub Energetici Green siti scelti senza vera valutazione energetica.

Da verificare, nei limiti dei dati disponibili:
- prossimità alla rete elettrica;
- tipo di infrastruttura;
- livello di tensione;
- possibili punti di connessione;
- capacità disponibile se ottenibile;
- difficoltà di connessione;
- eventuale costo proxy;
- spazio per infrastrutture elettriche;
- possibilità di integrare fotovoltaico o altre fonti;
- possibilità di accumulo;
- possibilità di elettrolisi.

Se alcuni dati non sono disponibili:
registrare chiaramente il limite.

Non sostituire capacità elettrica reale con proxy deboli senza dichiararlo.

Output:
set di indicatori energetici realmente utilizzabili.

Gate:
il criterio energetico deve discriminare oppure deve essere dichiarato non utilizzabile.

FASE 8 — NORMALIZZAZIONE E PESI

Obiettivo:
rendere confrontabili gli indicatori senza alterare arbitrariamente il risultato.

Priorità:
preferire scale assolute o soglie interpretabili quando possibile.

Evitare:
normalizzazioni dipendenti dal campione senza motivazione.

Se viene usato min-max:
- specificare su quale insieme;
- usare solo alternative ammissibili salvo motivo forte contrario;
- verificare l’effetto degli estremi.

Pesi:
- devono essere espliciti;
- motivati;
- modificabili da configurazione;
- mai nascosti nel codice.

Output:
configurazione ufficiale degli indicatori e dei pesi.

Gate:
formula del punteggio completamente ricostruibile.

FASE 9 — RANKING DEI SINGOLI SITI

Obiettivo:
ottenere la qualità individuale dei candidati.

Output minimo:
per ogni candidato:
- valori grezzi;
- valori normalizzati;
- peso;
- contributo di ogni indicatore;
- punteggio finale;
- posizione.

Importante:
questa graduatoria non coincide automaticamente con la scelta finale dei 5 siti.

Output:
RANKING_SITES_v01.

Gate:
ranking verificato numericamente su campione manuale.

FASE 10 — MODELLO DI SELEZIONE DEI 5 HUB

Obiettivo:
scegliere la migliore configurazione di rete, non semplicemente i primi cinque siti.

Da definire:
- numero di siti = 5;
- eventuale copertura obbligatoria dei nodi urbani;
- requisiti lungo la rete europea;
- distanza minima tra siti;
- distanza massima tra stazioni se normativa;
- eventuali obiettivi di copertura territoriale;
- eventuale copertura minima della domanda;
- eventuale equilibrio territoriale.

Metodo:
usare un modello di ottimizzazione esplicito.

Evitare di chiamare “ottima” una soluzione ottenuta soltanto scorrendo la graduatoria.

Funzione obiettivo possibile:
massimizzare la qualità complessiva dei 5 siti, eventualmente combinata con copertura e domanda servita.

Output:
SHORTLIST_5_v01.

Gate:
deve essere chiaro perché quei 5 siti sono stati scelti e perché alternative vicine sono state scartate.

FASE 11 — ANALISI DI ROBUSTEZZA

Obiettivo:
capire se la cinquina dipende troppo dalle assunzioni.

Test minimi:
- variazione dei pesi;
- variazione delle soglie;
- variazione della superficie minima;
- rimozione di singoli indicatori;
- scenari energetici;
- scenari ambientali;
- eventuali alternative nella funzione obiettivo.

Output:
ROBUSTNESS_REPORT_v01.

Da riportare:
- frequenza con cui ogni sito resta nella cinquina;
- alternative ricorrenti;
- criteri che cambiano maggiormente il risultato;
- eventuali siti strutturalmente fragili.

Gate:
nessuna cinquina viene definita robusta senza numeri.

FASE 12 — VERIFICA PUNTUALE DEI 5 SITI

Obiettivo:
controllare i cinque candidati selezionati a livello più concreto.

Verifiche:
- geometria;
- accesso reale;
- urbanistica;
- rischio idraulico;
- frane;
- vincoli ambientali;
- superficie;
- eventuale proprietà e disponibilità;
- connessione energetica;
- contesto territoriale;
- ortofoto;
- eventuali criticità locali.

Output:
scheda tecnica per ciascun sito.

Gate:
eventuali criticità bloccanti riportano il progetto alla fase precedente.

FASE 13 — CONFRONTO CON BASELINE CLAUDE

Obiettivo:
capire cosa cambia rispetto al progetto precedente.

Confrontare:
- universo candidati;
- esclusioni;
- indicatori;
- pesi;
- ranking;
- cinque siti finali;
- motivazioni delle differenze.

Output:
BASELINE_COMPARISON_v01.

Non usare questo confronto per forzare il nuovo modello verso il risultato Claude.

FASE 14 — FREEZE DEL MODELLO

Condizioni:
- dati registrati;
- metodologia documentata;
- codice pulito;
- configurazioni salvate;
- test passati;
- ranking verificato;
- shortlist verificata;
- robustezza analizzata;
- handoff completato;
- commit eseguito.

Output:
MODEL_v1_FROZEN.

FASE 15 — DELIVERABLE

Solo dopo il freeze:
- relazione metodologica;
- relazione generale;
- schede dei siti;
- tabelle;
- mappe;
- tavole;
- eventuale dashboard;
- allegati tecnici.

Regola:
i documenti finali devono essere generati dai risultati congelati, non ricostruiti manualmente da numeri copiati.

PRINCIPI NON NEGOZIABILI

1. Prima i dati, poi il modello.
2. Prima l’ammissibilità, poi il punteggio.
3. Prima il ranking individuale, poi la selezione della rete.
4. Un proxy deve essere dichiarato come proxy.
5. Un dato mancante non va inventato.
6. Un vincolo normativo non va confuso con una scelta progettuale.
7. Un sito non è un punto se l’unità di analisi è un’area.
8. Nessun risultato importante deve esistere solo in chat.
9. Ogni fase deve lasciare file, controlli, commit e handoff.
10. Se un risultato non è riproducibile, non è chiuso.