# DISPATCH — Chat 0.3 — Re-baseline strategica e semplificazione metodologica

**Mandante:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Stato:** AUTHORIZED / DEC-0061 ACCEPTED
**Branch:** `chat-0.3-strategic-rebaseline`

## 1. Contesto

L''utente ha approvato una riformulazione sostanziale dello scopo del progetto.

Nuovo obiettivo vincolante:

> Sviluppare e dimostrare un modello GIS multicriterio riproducibile per individuare una configurazione di cinque Hub Energetici Green in Friuli Venezia Giulia, massimizzandone l''idoneità territoriale complessiva secondo criteri di mobilità, accessibilità, infrastruttura energetica, territorio e ambiente. Il modello opera a scala di pianificazione strategica e non costituisce verifica di fattibilità catastale, proprietaria, autorizzativa o progettuale dei siti selezionati.

Questa decisione è registrata come `DEC-0061 = ACCEPTED`.

Il progetto è quindi un modello dimostrativo di pianificazione territoriale multicriterio, non una due diligence di investimento né una verifica completa di cantierabilità dei cinque siti.

## 2. Autorità e limiti

La Chat 0.3 è una chat operativa di architettura metodologica, subordinata alla Chat 0.2.

Può:
- analizzare l''intero progetto esistente;
- proporre una nuova baseline di scopo e una roadmap semplificata;
- proporre quali elementi esistenti mantenere, semplificare, rinviare o superare;
- proporre una nuova struttura di fasi coerente con DEC-0061;
- identificare le decisioni sostanziali residue da sottoporre all''utente.

Non può autonomamente:
- modificare o cancellare baseline FROZEN;
- cambiare lo stato di decisioni sostanziali già ACCEPTED senza nuova decisione esplicita;
- approvare pesi, normalizzazioni, formule di scoring o funzione obiettivo;
- aprire la Fase 4;
- cancellare artifact o storia Git;
- trasformare un elemento storico in inesistente.

Qualsiasi superamento di un elemento FROZEN deve avvenire tramite nuova versione e approvazione esplicita.

## 3. Principi vincolanti della re-baseline

### 3.1 Natura del risultato

Il risultato del modello è una **configurazione pianificatoria di 5 poligoni**, non cinque terreni pronti all''investimento.

I cinque poligoni rappresentano alternative localizzative territorialmente preferibili secondo il modello.

La relazione finale deve poter affermare che la configurazione è preferibile secondo criteri e pesi dichiarati, ma NON che:
- i terreni sono acquistabili;
- sono liberi da edifici;
- sono catastalmente disponibili;
- hanno già capacità elettrica sufficiente;
- sono autorizzabili senza approfondimenti;
- sono immediatamente cantierabili.

### 3.2 Unità di analisi

Resta confermato:

**unità di analisi = poligono.**

Il poligono è una alternativa localizzativa del modello, non necessariamente una particella catastale o un lotto immobiliare verificato.

### 3.3 Fuori dallo scope core

Devono essere rimossi dal core metodologico, salvo eventuale uso puramente descrittivo o come limite dichiarato:
- proprietà catastale;
- disponibilità alla vendita;
- disponibilità commerciale;
- prezzo/acquisizione del terreno;
- titolarità;
- presenza puntuale di edifici o manufatti come due diligence;
- trattative o disponibilità del proprietario;
- verifica autorizzativa completa;
- progettazione impiantistica;
- progetto stradale di dettaglio;
- verifica puntuale definitiva della capacità elettrica;
- fattibilità tecnica definitiva di connessione;
- costi di connessione;
- verifiche da due diligence finale di investimento.

Non eliminare automaticamente dati o artifact già prodotti: classificarli e conservarli come storico/supporto quando appropriato.

### 3.4 Centro del modello

Il progetto deve concentrarsi sulla qualità della pianificazione multicriterio.

Domini centrali attesi:
- mobilità e domanda Light;
- mobilità e domanda Heavy;
- accessibilità/rete TEN-T e rete stradale;
- infrastruttura energetica tramite proxy compatibili con scala macro;
- territorio;
- ambiente e principali tutele;
- eventuali ulteriori criteri territoriali realmente discriminanti e supportati dai dati.

La selezione finale deve essere trattata come problema di configurazione di cinque Hub, non come semplice presa dei primi cinque poligoni di una classifica, salvo futura decisione metodologica esplicita.

## 4. Stato delle formule di scoring

DEC-0061 NON approva ancora:
- indicatori definitivi;
- normalizzazione;
- pesi;
- metodo di elicitation dei pesi;
- formula di scoring del singolo poligono;
- aggregazione dei cinque punteggi;
- media semplice vs media pesata della configurazione;
- premi/penalità di diversificazione geografica;
- vincoli provinciali;
- funzione obiettivo finale;
- metodo di ottimizzazione.

Questi elementi devono essere identificati come decisioni future e organizzati in un ordine logico semplice.

Non introdurli implicitamente durante la re-baseline.

## 5. Materiale da leggere

Leggi integralmente e confronta almeno:

- istruzioni persistenti del progetto;
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER;
- `docs/ROADMAP_METODOLOGICA_v1.md`;
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md`;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md`;
- review e handoff delle Chat 3.1–3.12 pertinenti;
- DATA_REGISTRY;
- ISSUES;
- DECISIONS;
- `docs/relazione/RELATION_ARCHITECTURE_v01.md`;
- `docs/relazione/REVIEW_CHAT_90.0_RELATION_BUILDER_v01.md`.

Considera anche il branch:
`chat-3.12-natura2000-prescreen-ruleset`

La review indipendente della Chat 3.12 ha dato PASS WITH LIMITATIONS, ma la relativa chiusura di ISS-0013 e il merge non sono stati ancora eseguiti.

Claude/QGIS resta baseline storica NON autorevole.

## 6. Attività A — Definizione del nuovo model contract

Produci una proposta chiara e breve che definisca:

1. obiettivo del modello;
2. output finale;
3. interpretazione corretta dei 5 poligoni;
4. scala di analisi;
5. cosa il modello valuta;
6. cosa il modello NON valuta;
7. unità di analisi;
8. rapporto fra punteggio del singolo poligono e qualità della configurazione di 5;
9. ruolo di hard constraint, soft criterion e flag informativo;
10. limiti dichiarati.

Il model contract deve essere comprensibile anche a un lettore esterno.

## 7. Attività B — Audit completo del progetto esistente

Costruisci una matrice di impatto che mappi almeno:

- fasi;
- decisioni;
- issue;
- dataset;
- principali artifact;
- verifiche puntuali richieste;
- quality gate;
- attività future della roadmap.

Per ogni elemento assegna una proposta fra:

- `KEEP` — pienamente coerente e utile;
- `SIMPLIFY` — concetto utile ma implementazione attuale troppo dettagliata;
- `DEFER_POST_MODEL` — utile solo in una futura fattibilità/due diligence;
- `HISTORICAL_SUPPORT` — conservare come supporto/storia, non nel core;
- `SUPERSEDE_PROPOSED` — incompatibile con il nuovo scopo e da sostituire mediante nuova versione/decisione.

Per ogni classificazione indica:
- motivazione;
- impatto sulla roadmap;
- eventuale decisione utente necessaria.

Nessun elemento deve semplicemente scomparire.

## 8. Attività C — Revisione specifica delle aree sovradimensionate

Esamina con attenzione almeno:

### Proprietà e disponibilità
Valuta la rimozione dal modello core di proprietà, disponibilità commerciale e catastale.
In particolare rivaluta `DEC-0033` e `ISS-0009` alla luce di DEC-0061.

### Urbanistica
Distingui:
- uso dell''urbanistica come fonte per generare/descrivere poligoni e destinazioni territoriali;
- due diligence urbanistica puntuale di un sito.

La seconda non deve essere automaticamente richiesta dal nuovo scopo.

### Ambiente e tutele
Rivaluta il livello di dettaglio necessario per:
- PGRA;
- PAI;
- PPR;
- Natura 2000;
- parchi/riserve/biotopi/prati stabili.

Non cancellare il lavoro già fatto.
Proponi come trasformarlo in criteri, hard constraint realmente necessari o flag, coerentemente con una pianificazione macro.
Non introdurre nuove regole normative durante questa chat.

### Energia
Conferma o riformula il ruolo del proxy di prossimità alla rete elettrica come indicatore strategico.
Capacità MW, connessione reale e costi non devono diventare requisiti della selezione macro.

### Mobilità
Preserva quanto utile delle baseline Light/Heavy.
Distingui domanda/corridoi/accessibilità territoriale dalla progettazione puntuale dell''accesso al lotto.

## 9. Attività D — Nuova roadmap

Proponi una `ROADMAP_METODOLOGICA_v2` molto più snella.

La nuova roadmap deve privilegiare una sequenza del tipo:

1. scopo e unità di analisi;
2. universo dei poligoni candidati;
3. criteri e indicatori;
4. trasformazione/normalizzazione;
5. pesi;
6. score del singolo poligono;
7. definizione della qualità della configurazione di 5;
8. vincoli di configurazione;
9. selezione/ottimizzazione;
10. sensibilità/robustezza;
11. risultati e interpretazione;
12. relazione.

Questa sequenza è orientativa, non un ordine già approvato.

Riduci fasi che esistono solo perché il progetto precedente trattava i siti come oggetti quasi pronti alla realizzazione.

La roadmap deve essere abbastanza dettagliata da essere riproducibile, ma non burocratica.

## 10. Attività E — Decision queue minima

Costruisci una lista corta e ordinata delle sole decisioni metodologiche che servono davvero per arrivare ai risultati.

Esempi attesi:
- come costruire l''universo dei poligoni;
- quali criteri usare;
- quali variabili sono hard constraint;
- come normalizzare;
- come assegnare i pesi;
- come calcolare lo score individuale;
- come valutare la cinquina;
- quali vincoli territoriali imporre alla configurazione;
- come fare sensitivity/robustness.

Non chiedere all''utente di decidere dettagli che non influenzano materialmente il risultato.

## 11. Attività F — Impatto sulla relazione

Produci una nota per la Chat 90.0 che specifichi:
- quali capitoli dell''architettura editoriale restano validi;
- quali devono essere semplificati;
- quali riferimenti a fattibilità puntuale vanno rimossi o ricollocati nei limiti;
- come descrivere correttamente il significato dei 5 Hub risultanti.

Non modificare autonomamente gli artifact della Chat 90.0.

## 12. Deliverable richiesti

Crea almeno:

- `docs/PROJECT_MODEL_CONTRACT_REBASELINE_v01_PROPOSED.md`
- `docs/ROADMAP_METODOLOGICA_v2_PROPOSED.md`
- `docs/REBASELINE_IMPACT_MATRIX_v01.csv`
- `docs/REBASELINE_ISSUE_DISPOSITION_v01.csv`
- `docs/REBASELINE_DECISION_QUEUE_v01.md`
- `docs/REBASELINE_EDITORIAL_IMPACT_CHAT90_v01.md`
- `docs/HANDOFF_CHAT_0.3_STRATEGIC_REBASELINE_v01.md`

Se emerge la necessità di nuovi successori delle baseline F1/F2, NON modificare i file FROZEN.
Proponi invece i nomi/versioni dei successori e specifica esattamente cosa cambierebbe.

## 13. Quality gate

Il lavoro può essere proposto come PASS solo se:

- DEC-0061 è rispettata;
- l''intero progetto esistente è mappato senza cancellazioni implicite;
- le attività fuori scope sono esplicitamente separate dal core;
- FROZEN/ACCEPTED non sono modificati silenziosamente;
- la nuova roadmap è sostanzialmente più snella;
- ogni fase futura ha un output verificabile;
- la decision queue contiene solo scelte materialmente necessarie;
- scoring/pesi/F.O. non sono approvati implicitamente;
- il ruolo del poligono resta coerente con DEC-0061;
- la relazione esterna viene riallineata concettualmente;
- Fase 4 non è aperta;
- `git diff --check` PASS;
- branch pulito;
- handoff completo.

## 14. Stato finale

Concludi con:

- proposta di stato della roadmap v1;
- proposta di stato per Fasi 1–3;
- lista delle DEC/ISS che richiedono nuova disposizione;
- lista delle decisioni che richiedono esplicita approvazione utente;
- prossimo passo minimo consigliato.

Poi fermati.

La Chat 0.3 NON deve implementare il nuovo scoring né costruire candidati.
La review finale della re-baseline compete alla Chat 0.2 e all''utente.
