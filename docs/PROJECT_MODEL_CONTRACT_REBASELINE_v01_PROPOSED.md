# PROJECT MODEL CONTRACT — REBASELINE v01 — PROPOSED

**Chat:** 0.3 — Re-baseline strategica e semplificazione metodologica
**Data:** 2026-09-21
**Stato:** PROPOSED — richiede review Chat 0.2 e approvazione esplicita dell'utente
**Autorità:** DEC-0061 ACCEPTED

Questo documento non apre la Fase 4 e non approva indicatori, formule, normalizzazioni, pesi, scoring, funzione obiettivo, vincoli di configurazione o algoritmo.

## 1. Obiettivo

Sviluppare e dimostrare un modello GIS multicriterio riproducibile per individuare una configurazione di cinque Hub Energetici Green in Friuli Venezia Giulia, massimizzandone l'idoneità territoriale complessiva secondo criteri di mobilità, accessibilità, infrastruttura energetica, territorio e ambiente.

Il modello è uno strumento di pianificazione strategica territoriale. Non è una due diligence immobiliare, catastale, autorizzativa, elettrica o progettuale.

## 2. Output finale

L'output finale è una configurazione di cinque poligoni selezionata da un universo di alternative tracciabili mediante una procedura dichiarata, riproducibile e sottoposta ad analisi di sensibilità/robustezza.

Per ciascun poligono devono essere ricostruibili origine e lineage della geometria, valori degli indicatori approvati, trasformazioni, contributi allo score individuale se adottato, hard constraint applicati e flag informativi.

Per la cinquina devono essere ricostruibili funzione di qualità/obiettivo approvata, eventuali vincoli, procedura di selezione, alternative rilevanti e risultati di sensibilità/robustezza.

## 3. Significato dei cinque poligoni

La cinquina finale significa: secondo il modello multicriterio approvato, questi cinque poligoni costituiscono una configurazione territorialmente preferibile tra le alternative considerate, sulla base dei criteri, delle trasformazioni, dei pesi e dei vincoli dichiarati.

La cinquina non significa che i cinque terreni siano acquistabili, in vendita, catastalmente verificati, liberi da edifici, autorizzabili senza approfondimenti, dotati di capacità elettrica sufficiente, con punto di connessione garantito, cantierabili o già verificati a livello progettuale.

## 4. Scala di analisi

La scala è regionale e strategica.

Sono coerenti con questa scala domanda e flussi Light, domanda e flussi Heavy, corridoi e TEN-T, accessibilità territoriale, prossimità a infrastrutture energetiche come proxy, struttura territoriale/urbanistica per generazione e classificazione, rischi/tutele al livello consentito dalle fonti e confronto fra alternative territoriali.

Non sono richieste nel core analisi che presuppongono un progetto definitivo, un titolo di disponibilità del bene o una pratica autorizzativa sito-specifica.

## 5. Cosa valuta il modello

Il modello valuta, previa futura approvazione degli indicatori:
- domanda e mobilità Light;
- domanda e mobilità Heavy;
- accessibilità e relazione con rete stradale/TEN-T;
- infrastruttura energetica mediante proxy coerenti con scala macro;
- caratteristiche territoriali rilevanti;
- ambiente, rischio e principali tutele;
- ulteriori variabili territoriali solo se discriminanti, supportate da dati adeguati e motivate rispetto all'obiettivo.

La presenza di un dataset non implica che esso diventi automaticamente un indicatore.

## 6. Cosa non valuta il modello core

Sono fuori dal core e, se utili, diventano DEFER_POST_MODEL, materiale storico o limite dichiarato:
- proprietà catastale e titolarità;
- disponibilità alla vendita o commerciale;
- prezzo e acquisizione del terreno;
- due diligence puntuale su edifici/manufatti;
- verifica autorizzativa completa;
- layout e progettazione impiantistica;
- progetto stradale di dettaglio;
- capacità elettrica effettivamente disponibile;
- punto e costo reale di connessione;
- cantierabilità definitiva;
- negoziazione con proprietari, gestori o enti.

Questi aspetti possono essere raccomandati come approfondimenti successivi alla selezione strategica, ma non sono condizioni per dichiarare concluso il modello.

## 7. Unità di analisi

L'unità di analisi resta il poligono, coerentemente con F2-D1 e DEC-0061.

Il poligono rappresenta una alternativa localizzativa del modello. Non è automaticamente una particella catastale, un lotto immobiliare unitario, una superficie già disponibile o il footprint del futuro impianto.

Le geometrie ausiliarie definite in Fase 2 restano utilizzabili quando servono a una misura specifica. Non devono generare, da sole, l'obbligo di svolgere progettazione locale di dettaglio.

## 8. Score individuale e qualità della configurazione

Il progetto distingue:
1. qualità individuale del poligono, cioè quanto una singola alternativa è territorialmente idonea rispetto ai criteri approvati;
2. qualità della configurazione di cinque Hub, cioè la bontà congiunta della cinquina, eventualmente dipendente anche da relazioni tra siti, coperture, ridondanze o vincoli di configurazione.

Il ranking individuale, se adottato, non seleziona automaticamente i cinque Hub finali.

Non sono approvati in questo documento formula dello score individuale, aggregazione della cinquina, premi/penalità di diversificazione, vincoli provinciali, funzione obiettivo o metodo di ottimizzazione.

## 9. Hard constraint, soft criterion e flag

### Hard constraint

Regola binaria che rende una alternativa non selezionabile indipendentemente dal punteggio.

Può entrare nel modello solo se è realmente necessaria allo scopo strategico, deriva da una regola esplicita e documentata o da una condizione tecnica indispensabile già approvata, è applicabile in modo coerente e riproducibile e non richiede una due diligence che il modello non può svolgere.

Nessun tematismo ambientale, urbanistico o tecnico diventa hard constraint per semplice presenza/intersezione senza una futura decisione operativa esplicita coerente con le DEC già approvate.

### Soft criterion

Variabile quantitativa o ordinale che contribuisce alla comparazione tra alternative senza produrre esclusione automatica. Formula, direzione, trasformazione, normalizzazione e peso richiedono approvazione separata.

### Flag informativo

Attributo che segnala incertezza, currentness non dimostrata, approfondimento successivo, possibile requisito autorizzativo, limite del dato o condizione non risolvibile alla scala macro.

Un flag non esclude e non modifica il punteggio salvo successiva decisione esplicita.

## 10. Dati mancanti e proxy

- Un dato mancante non viene trasformato in zero, esclusione o penalizzazione senza regola approvata.
- Un proxy resta dichiarato come proxy.
- Prossimità alla rete elettrica non equivale a capacità disponibile.
- Domanda/corridoi Light e Heavy non equivalgono a accessibilità locale del lotto.
- Urbanistica best-available non equivale a attestazione giuridica definitiva di vigenza del singolo sito.
- Pre-screening ambientale non equivale a autorizzazione o valutazione competente.

## 11. Limiti dichiarati

Il risultato dipende dall'universo dei poligoni, dalla qualità/currentness dei dati, dalle future scelte su criteri/trasformazioni/pesi, dalla definizione della qualità della cinquina, dai proxy e dalla granularità regionale.

La robustezza deve essere valutata quantitativamente prima del freeze finale.

## 12. Implicazioni sulle baseline FROZEN

### Fase 1

F1-D1…F1-D7 restano validi. La baseline FASE_1_HUB_DEFINITION_CONSOLIDATED_v02 contiene però requisiti localizzativi puntuali che possono essere letti come gate di fattibilità del singolo lotto.

Proposta: non modificare v02. Dopo approvazione utente creare FASE_1_HUB_DEFINITION_CONSOLIDATED_v03_PROPOSED che:
- mantenga integralmente F1-D1…F1-D7;
- mantenga AFIR/TEN-T solo quando materialmente rilevante alla funzione strategica;
- riclassifichi progettazione dell'accesso, sicurezza sito-specifica, capacità/connessione elettrica reale e verifiche esecutive come post-model;
- distingua requisiti funzionali dell'Hub da due diligence del terreno.

### Fase 2

FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01 resta coerente con DEC-0061 e non richiede sostituzione.

Le geometrie ausiliarie e le regole di accesso si applicano quando richieste da uno specifico indicatore approvato; non costituiscono obbligo di progettazione locale generalizzata.

## 13. Stato proposto

PROJECT_MODEL_CONTRACT_REBASELINE_v01 = PROPOSED.

Diventa baseline operativa solo dopo approvazione esplicita dell'utente e registrazione nella governance viva.
