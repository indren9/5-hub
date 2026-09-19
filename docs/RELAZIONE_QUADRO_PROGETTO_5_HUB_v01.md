# RELAZIONE QUADRO E SCHELETRO METODOLOGICO — PROGETTO 5 HUB ENERGETICI GREEN FVG

**Versione:** v01
**Data aggiornamento:** 19 settembre 2026
**Stato:** DRAFT — documento esplicativo e di lavoro
**Destinatari:** tecnici, analisti e collaboratori che devono entrare nel progetto senza conoscere la nomenclatura interna o la storia delle chat.

## Avvertenza sul ruolo del documento

Questa relazione è una sintesi leggibile e progressivamente completabile del progetto. Non sostituisce la governance ufficiale.

In caso di conflitto prevalgono, nell’ordine:
1. PROJECT_SOURCE_OF_TRUTH;
2. decisioni registrate nel PROJECT_CONTROL_REGISTER;
3. baseline metodologiche FROZEN;
4. codice, configurazioni e artifact tecnici versionati;
5. documentazione di review e handoff.

Nel documento si distinguono quattro stati:
- **FROZEN:** scelta approvata e congelata; si modifica solo con nuova versione e nuova approvazione;
- **ACCEPTED:** scelta approvata e operativa, ma non ancora congelata come baseline definitiva;
- **IN VALIDAZIONE / OPEN:** dato, fonte o metodo ancora da verificare;
- **HISTORICAL / SUPPORT ONLY:** materiale utile come riferimento o benchmark, ma non autorevole per il modello corrente.

---

# 1. Scopo del progetto

Il progetto sviluppa in house, in modo riproducibile e verificabile, un modello per individuare la localizzazione di **5 Hub Energetici Green in Friuli Venezia Giulia**.

La domanda centrale è: **quali cinque aree del territorio regionale sono le più adatte a ospitare gli Hub, tenendo insieme requisiti normativi, accessibilità, domanda, vincoli territoriali, fattibilità energetica e robustezza della soluzione?**

Il progetto non sviluppa il layout esecutivo dell’impianto e non progetta nel dettaglio serbatoi, elettrolizzatori, colonnine o opere civili. Gli aspetti impiantistici entrano nel modello soltanto quando producono un requisito territoriale o infrastrutturale rilevante per la localizzazione.

## 1.1 Principi di lavoro

Il modello viene costruito secondo alcuni principi non negoziabili:
- prima si definiscono concetti e requisiti, poi si implementa;
- prima si validano i dati, poi si usano;
- un dato mancante non viene inventato;
- un proxy viene sempre dichiarato come proxy;
- un requisito normativo non viene confuso con una scelta progettuale;
- prima si verifica l’ammissibilità dei siti, poi si attribuiscono punteggi;
- il ranking dei singoli siti non coincide automaticamente con la scelta finale dei cinque Hub;
- ogni risultato importante deve essere riproducibile da dati, codice e configurazioni;
- nessun risultato importante deve esistere soltanto in una conversazione.

## 1.2 Stato generale al 18 settembre 2026

- Fase 0 — inizializzazione del progetto: **PASS / CLOSED**.
- Fase 1 — definizione di cosa sia un Hub: **PASS / CLOSED / FROZEN**.
- Fase 2 — definizione dell’unità elementare di analisi: **PASS / CLOSED / FROZEN**.
- Fase 3 — inventario e validazione dei dati: **IN CORSO**.
- Fasi 4–15: **NON AVVIATE**.

La Fase 4, nella quale verrà costruito l’universo reale dei candidati, non può iniziare finché la Fase 3 non viene formalmente chiusa.

---

# 2. Organizzazione del progetto e fonti autorevoli

Il progetto separa codice, dati pesanti e governance.

- Repository locale di sviluppo: C:\dev\5-hub
- Versionamento: Git
- Repository remoto ufficiale: GitHub privato indren9/5-hub
- Storage tecnico per dati pesanti e output: C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG
- Governance viva: Google Drive, tramite PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER

La precedente cartella C:\Tesi\dev è deprecata e non deve essere usata.

La baseline prodotta nel precedente progetto Claude è conservata integralmente, ma è classificata **HISTORICAL / NON_AUTHORITATIVE**. Può servire per recuperare fonti, idee, layer, benchmark e confronti, ma nessuna metodologia, soglia, graduatoria o conclusione viene ereditata automaticamente.

---

# 3. Logica complessiva del modello

La catena metodologica prevista è:

1. definire cosa deve contenere un Hub;
2. definire che cosa rappresenta un singolo candidato;
3. validare le fonti dati;
4. costruire tutte le aree candidabili;
5. eliminare le aree non ammissibili;
6. definire gli indicatori di qualità;
7. valutare la fattibilità energetica;
8. definire normalizzazione e pesi;
9. calcolare il ranking dei singoli siti;
10. selezionare con un modello esplicito la migliore configurazione di 5 Hub;
11. testare la robustezza della soluzione;
12. verificare in dettaglio i 5 siti selezionati;
13. confrontare il risultato con la baseline Claude;
14. congelare il modello;
15. produrre i deliverable finali.

Questa sequenza è fondamentale: **non si parte dai cinque siti finali e non si cerca di giustificarli a posteriori**.

---

# 4. Che cosa si intende per Hub Energetico Green

Questa parte è già consolidata e costituisce una baseline **FROZEN**.

## 4.1 Nucleo minimo obbligatorio

Tutti e cinque gli Hub devono integrare:
- una stazione di rifornimento di **idrogeno accessibile al pubblico**;
- un modulo di **ricarica elettrica in corrente continua accessibile al pubblico**;
- le infrastrutture di supporto necessarie alla loro operatività e accessibilità.

Il modulo elettrico deve poter servire sia **veicoli leggeri** sia **veicoli pesanti**.

## 4.2 Relazione con AFIR e TEN-T

**AFIR** è il Regolamento europeo sulle infrastrutture per combustibili alternativi.
**TEN-T** è la rete transeuropea dei trasporti.

Le specifiche AFIR per l’idrogeno, tra cui **700 bar** e **1 tonnellata/giorno**, sono vincolanti solo per gli Hub che devono svolgere una funzione di copertura AFIR/TEN-T. Non sono automaticamente imposte a tutti i cinque Hub.

Ai fini localizzativi, quando un Hub deve concorrere alla copertura AFIR/TEN-T:
- per l’idrogeno la collocazione può essere sulla rete TEN-T o entro **10 km di percorrenza stradale dall’uscita TEN-T più vicina**;
- per la ricarica elettrica la distanza corrispondente è **3 km di percorrenza stradale**.

La definizione operativa delle uscite TEN-T sarà costruita solo dopo il completamento della validazione della rete TEN-T FVG.

## 4.3 Energia rinnovabile e architettura dell’idrogeno

La produzione da fonti rinnovabili fisicamente all’interno del sito non è obbligatoria.

Fotovoltaico o altre fonti rinnovabili possono essere presenti, ma non costituiscono un requisito universale. Il sito deve però essere compatibile con l’uso diretto di energia rinnovabile quando tecnicamente e progettualmente opportuno.

L’idrogeno rinnovabile o certificato non è un requisito obbligatorio della configurazione minima.

Il modello non predefinisce l’architettura di approvvigionamento dell’idrogeno. Tube trailer, pipeline, elettrolisi in sito o altre soluzioni vengono considerate solo se producono esigenze territoriali, infrastrutturali, di sicurezza o di accessibilità che influenzano la localizzazione.

Biocarburanti e altri vettori energetici sono opzionali e non fanno parte del nucleo minimo obbligatorio.

## 4.4 Requisiti di accesso stradale regionale

La Legge Regionale FVG 19/2012 include l’idrogeno tra i carburanti e, dove applicabile, introduce requisiti tecnici di accesso agli impianti stradali di distribuzione.

Tra i requisiti localizzativi già individuati:
- fronte strada minimo generalmente pari a 40 m;
- 25 m nei casi territoriali specificamente previsti dalla legge;
- 100 m lungo strade a quattro o più corsie;
- accessi distinti di entrata e uscita;
- separazione del piazzale dalla sede stradale;
- divieto di accessi su due o più strade pubbliche.

Questi elementi saranno trattati come vincoli di fattibilità dove effettivamente applicabili, non come punteggi di merito.

## 4.5 Elementi volutamente non ancora fissati

Non sono ancora definiti:
- layout dell’Hub;
- superficie minima universale;
- potenza elettrica universale per tutti gli Hub;
- numero universale di punti di ricarica;
- tecnologia H₂ obbligatoria;
- presenza obbligatoria di fotovoltaico, accumulo o elettrolisi.

Questi elementi potranno essere definiti solo quando serviranno per tradurre esigenze reali in requisiti localizzativi.

---

# 5. Che cosa rappresenta un candidato

Anche questa parte è **FROZEN**.

## 5.1 Il candidato è un’area, non un punto

L’unità elementare del modello è una **area/poligono fisicamente localizzabile**.

Un candidato non coincide con:
- un Comune;
- un semplice punto;
- un impianto esistente;
- il centroide di una zona urbanistica.

Il poligono rappresenta una superficie sulla quale l’Hub potrebbe essere localizzato.

## 5.2 Geometrie disconnesse

Se una geometria contiene più parti fisicamente separate, tali parti vengono considerate candidati distinti.

Possono essere mantenute insieme solo se esiste una continuità operativa reale e documentabile.

## 5.3 Punto rappresentativo

Per visualizzazioni o calcoli che richiedono un singolo punto viene utilizzato, di default, un punto interno garantito alla superficie del poligono.

Non si usa automaticamente il centroide geometrico, perché potrebbe cadere fuori dal poligono o avere poco significato operativo.

Il punto rappresentativo **non è l’accesso stradale** e non è l’origine automatica del routing.

## 5.4 Accessi alla rete stradale

Un candidato può avere più accessi stradali potenziali o validati.

La catena corretta è:

**poligono candidato → punto di accesso → punto di aggancio alla rete stradale → rete di routing**

Le distanze stradali non devono quindi essere calcolate automaticamente dal centroide o dal punto rappresentativo.

## 5.5 Duplicati e sovrapposizioni

Lo stesso sito fisico non deve essere contato più volte solo perché compare in più dataset.

Nella futura costruzione dei candidati dovrà esistere una procedura riproducibile per distinguere:
- duplicati dello stesso sito;
- sovrapposizioni parziali;
- alternative realmente distinte.

La provenienza delle geometrie sorgente deve essere sempre conservata.

## 5.6 Identità e versionamento

Ogni candidato dovrà avere:
- un identificativo logico stabile;
- una versione;
- un hash della geometria;
- il riferimento alle feature sorgente;
- metadati di creazione e stato.

Una correzione geometrica non crea automaticamente un nuovo candidato se il sito fisico rimane lo stesso.

## 5.7 Confini comunali

Un’area non viene spezzata automaticamente perché attraversa il confine tra due Comuni.

Uno split è giustificato solo se il confine coincide con differenze urbanistiche, normative o di fattibilità che rendono le due porzioni realmente diverse.

## 5.8 Tolleranze geometriche

Non sono state ancora fissate soglie numeriche per snap, merge, micro-gap o overlap.

Le tolleranze saranno definite sulla base della qualità reale dei dataset e non tramite valori arbitrari scelti in anticipo.

---

# 6. Costruzione della base urbanistica

Questa parte è **APPROVATA come metodo**, ma non ancora completata sul piano dei dati.

## 6.1 Perché non si usa direttamente la vecchia mosaicatura regionale

I layer regionali delle zone industriali/artigianali e delle zone commerciali sono servizi ufficiali e tecnicamente accessibili, ma derivano dalla **Mosaicatura PRG 2018**.

Le verifiche svolte hanno mostrato date non oltre il 2018, codici comunali storici e casi concreti in cui i piani comunali oggi vigenti sono successivi.

Di conseguenza questi layer sono classificati:

**HISTORICAL ONLY / SUPPORT ONLY**

Possono essere usati per ricostruire la storia, confrontare geometrie o accelerare le verifiche, ma **non rappresentano automaticamente l’urbanistica vigente nel 2026**.

## 6.2 Procedura urbanistica approvata: current-first / ibrida

Per ogni Comune del Friuli Venezia Giulia si deve prima stabilire quale sia il **PRGC realmente vigente**.

**PRGC** significa Piano Regolatore Generale Comunale.

La procedura approvata è:
1. identificare il PRGC e le varianti effettivamente vigenti;
2. verificare l’atto e la data di efficacia;
3. usare EagleFVG o una geometria regionale solo quando si dimostra che corrisponde alla variante vigente;
4. se questo non è dimostrabile, tornare alla fonte ufficiale comunale;
5. registrare fonte, URL, data, variante, stato, geometria e lineage;
6. marcare esplicitamente i casi ancora non verificabili.

L’obiettivo futuro è costruire una mosaicatura tecnica controllata dei PRGC vigenti, non aggiornare alla cieca il layer 2018.

## 6.3 Stato corrente

La procedura metodologica è **ACCEPTED**.

Resta aperto il lavoro di acquisizione e validazione effettiva Comune per Comune. L’accesso a EagleFVG è stato verificato per una parte significativa dei Comuni, ma l’esistenza di una configurazione digitale non dimostra da sola che il contenuto sia aggiornato alla variante vigente.

---

# 7. Proprietà, occupazione e disponibilità delle aree

La metodologia è **ACCEPTED**, mentre il dato region-wide resta incompleto.

È fondamentale distinguere almeno tre concetti:
1. **disponibilità fisica:** esiste realmente spazio utilizzabile?;
2. **proprietà:** chi possiede il terreno?;
3. **disponibilità proprietaria/commerciale:** il terreno è realmente acquisibile, assegnabile o disponibile?

La regola approvata è:
- raccogliere queste informazioni appena diventano disponibili;
- non interpretare un dato mancante come indisponibilità;
- la sola disponibilità proprietaria/commerciale sconosciuta **non esclude** un candidato;
- condizioni fisiche oggettive e verificate possono incidere prima sulla fattibilità;
- la verifica proprietaria e commerciale approfondita viene effettuata sui siti finalisti.

Stato concettuale minimo consigliato:
- VERIFIED_AVAILABLE;
- VERIFIED_UNAVAILABLE;
- UNKNOWN.

Esistono fonti parziali utili, come il patrimonio disponibile della Regione e le informazioni dei Consorzi di sviluppo economico locale, ma non esiste ancora un dataset completo e validato per l’intero territorio regionale.

---

# 8. Rete stradale e routing

## 8.1 Grafo stradale regionale

La Regione FVG pubblica un grafo stradale ufficiale con circa 75.500 segmenti.

La fonte è autorevole come base geometrica regionale, ma **non è ancora validata per routing di produzione**.

Le verifiche hanno mostrato:
- buona connettività geometrica generale;
- presenza di intersezioni che richiedono distinzione tra incroci reali e separazioni di quota;
- campo di direzione non interpretabile direttamente come semplice flag di senso unico;
- copertura insufficiente delle restrizioni necessarie per il traffico pesante.

Conseguenza:
- utilizzabile per screening e analisi geometriche;
- non ancora utilizzabile come rete definitiva per distanze direzionali Light;
- non sufficiente da sola per routing Heavy.

**Light** indica qui i veicoli leggeri. **Heavy** indica i veicoli pesanti.

## 8.2 Baseline OSM storica della tesi

Esiste anche un grafo OSM congelato proveniente dal precedente lavoro di rete stradale della tesi.

**OSM** significa OpenStreetMap.

Questo grafo è molto ricco per topologia, sensi di marcia, rampe e restrizioni. Nel progetto 5 HUB può essere utilizzato come strumento tecnico di supporto e confronto, ma la sua eventuale promozione a rete operativa del nuovo modello deve essere formalmente verificata e documentata.

## 8.3 Stato da definire

Prima dell’uso modellistico occorre ancora:
- scegliere e validare la rete di routing definitiva;
- definire la semantica dei sensi di marcia;
- gestire le restrizioni Heavy;
- definire il processo di creazione e validazione degli accessi reali dei candidati.

---

# 9. Rete TEN-T e uscite rilevanti per AFIR

La rete TEN-T vigente è disciplinata dal Regolamento (UE) 2024/1679 e utilizza tre livelli: core, extended core e comprehensive.
I vecchi servizi TENtec a due livelli non possono essere usati come rappresentazione completa della rete vigente.

## 9.1 Crosswalk TEN-T

Per **crosswalk** si intende una tabella di corrispondenza tra:
- le geometrie ufficiali TEN-T;
- le strade reali del Friuli Venezia Giulia, come A4, A23, A28, RA13, SS202 ecc.;
- il livello TEN-T corretto di ciascun tratto.

Esempio concettuale:

**geometria TEN-T ufficiale → tratto reale A4 → livello core → estensione e fonte documentate**

Il crosswalk completo copre la rete stradale TEN-T FVG corrente nei tre livelli. La Chat 3.7 ha validato **11 sezioni TENtec ufficiali aggregate in 6 assi stradali FVG**: A4, A23, RA13, RA14, A/SS202 e A28. La ripartizione corrente è 9 sezioni CORE, 0 EXTENDED CORE e 2 COMPREHENSIVE-only.

## 9.2 Problema della nearest exit

Le FAQ tecniche AFIR della Commissione chiariscono che, quando si misura dalla più vicina uscita TEN-T, la distanza parte dal punto in cui la rampa si separa dalla strada TEN-T.

Il progetto ha verificato l’intera rete stradale TEN-T FVG corrente prima di introdurre qualsiasi regola speciale per strade con intersezioni a raso.

L’audit completo non ha individuato alcun tratto TEN-T FVG rilevante privo di una vera uscita/rampa. La questione metodologica è quindi **ACCEPTED / RESOLVED** con DEC-0036 come **non materialmente applicabile al dominio FVG corrente**. Non viene introdotta alcuna regola artificiale che assimili rotatorie o normali intersezioni a raso a una TEN-T exit. La questione dovrà essere riaperta solo se una futura versione della rete TEN-T o della rete stradale introduce un caso reale diverso.
---

# 10. Vincoli territoriali, ambientali e paesaggistici

Questa sezione ha superato la **validazione tecnica di Fase 3**, ma le regole metodologiche con cui i singoli vincoli entreranno nell’ammissibilità restano da approvare.

Le principali famiglie di dati già individuate sono:
- PGRA — Piano di Gestione del Rischio di Alluvioni;
- frane e pericolosità geologica;
- Natura 2000;
- parchi, riserve, biotopi e altre aree protette;
- PPR — Piano Paesaggistico Regionale;
- altri vincoli territoriali eventualmente rilevanti.

## 10.1 Rischio idraulico

La fonte di riferimento è l’Autorità di Bacino Distrettuale delle Alpi Orientali, tramite SIGMA/PGRA.

Il quadro aggiornato adottato con Delibera n. 12 del 18 dicembre 2025 è vigente dal 22 gennaio 2026. Il set corrente SIGMA `PGRA2027` e i servizi WFS live sono stati verificati. Resta però aperto `ISS-0006`: il servizio WFS non espone un binding di versione esplicito che colleghi in modo machine-readable le geometrie live alla Delibera 12/2025, quindi tali vettori non sono ancora promossi a baseline normativa corrente.

## 10.2 Paesaggio

Il PPR vigente con Variante 2/2025 è stato verificato sul riferimento ufficiale regionale. Il servizio WFS corrente incorpora la Variante 2 e il subset pertinente è stato materializzato con una procedura GIS riproducibile e hash verificati. `ISS-0008` è quindi RESOLVED sul piano dei dati. Resta separata la decisione metodologica su quali componenti del PPR costituiscano esclusione, verifica di ammissibilità o semplice contesto.
## 10.3 Regola metodologica ancora da definire

Per ogni tematismo territoriale è stata predisposta una matrice tecnica dei possibili ruoli, ma resta necessario approvare se e come ciascuna categoria agisca come:
- vincolo normativo di esclusione;
- criterio di ammissibilità;
- indicatore di merito;
- semplice informazione di contesto.

`Q-METH-3.4-A` — trattamento PGRA — è **ACCEPTED** con DEC-0039. La presenza di pericolosità o allagabilità PGRA non costituisce di per sé un criterio automatico di esclusione. Un candidato viene escluso quando la disciplina vigente rende l’intervento incompatibile/non ammissibile oppure quando emerge una incompatibilità tecnica non ragionevolmente mitigabile. Negli altri casi pericolosità e allagabilità restano fattori negativi di futura valutazione, preferibili alla sola carta del rischio; scoring, pesi e funzioni di valutazione sono rinviati alle fasi dedicate. Le classi PGRA devono essere ricondotte alle Norme di Attuazione/PAI applicabili prima di produrre effetti operativi. Per la geometria si cerca prioritariamente un binding esplicito alla versione vigente; se non reperibile dopo ricerca documentata, il WFS ufficiale live può essere utilizzato operativamente con caveat e lineage espliciti. `Q-METH-3.4-B` — frane — è **ACCEPTED** con DEC-0040. Per la pericolosità da frana e le eventuali incompatibilità normative il riferimento operativo principale è il **PAI vigente completo**, incluse le classi di pericolosità e le eventuali aree/zone di attenzione pertinenti. Il Catasto Frane e i perimetri inventariali restano fonti conoscitive di supporto e non producono automaticamente esclusioni o punteggi. Le classi PAI devono essere ricondotte alle Norme di Attuazione applicabili prima di produrre effetti operativi. Prima dell'implementazione va acquisita e validata la cartografia PAI franosa corrente completa; il gap è tracciato da `ISS-0012`. `Q-METH-3.4-C` — Natura 2000 — è **ACCEPTED** con DEC-0041. Il modello non applica esclusioni automatiche per la sola intersezione o distanza da siti Natura 2000: esegue invece un pre-screening territoriale automatico usando ZSC/ZPS, aree di interferenza funzionale e criteri regionali vigenti. Prima di classificare un candidato come bisognoso di VINCA specifica, deve sfruttare prioritariamente le prevalutazioni regionali correnti e la relativa verifica di corrispondenza. Il modello può classificare la necessità di approfondimento, ma non dichiarare autonomamente una VINCA superata. Il gap di implementazione è tracciato da `ISS-0013`. Restano aperte `Q-METH-3.4-D…E`.

---

# 11. Fattibilità energetica

Questa è una delle aree ancora più critiche del progetto.

Le fonti individuate includono Terna e il portale TE.R.R.A., distributori locali, aree convenzionali delle cabine primarie e dati di rete.

## 11.1 Principio metodologico

La distanza da una linea o da una cabina **non equivale alla capacità elettrica disponibile**.

Le aree convenzionali delle cabine primarie non rappresentano né la posizione reale della cabina né la capacità disponibile del nodo.

Qualsiasi proxy futuro dovrà essere dichiarato esplicitamente come proxy.

## 11.2 Gap principale

Non esiste ancora nel progetto un dataset validato che fornisca, per ogni futuro candidato, capacità disponibile, punto di connessione e costo o difficoltà reale di connessione.
La futura Fase 7 dovrà stabilire quali dati siano realmente ottenibili e, se la capacità reale non fosse disponibile, quali proxy possano essere utilizzati senza confonderli con il dato reale.

---

# 12. Dati di domanda e contesto territoriale

Sono già state identificate fonti ufficiali per:
- popolazione residente — ISTAT;
- griglia di popolazione 1 km — ISTAT;
- pendolarismo per lavoro 2021 — ISTAT;
- distanze e tempi tra Comuni — ISTAT;
- turismo — Regione FVG / WebTur / ISTAT;
- aree interne — Strategia Nazionale Aree Interne;
- porti, interporti e terminali logistici;
- aree industriali e poli produttivi.

La presenza di una fonte non implica automaticamente che il relativo dato diventerà un indicatore.

Ogni indicatore dovrà avere significato, unità di misura, geometria di riferimento, formula, direzione preferenziale, trattamento dei valori mancanti e normalizzazione dichiarata.

---

# 13. Fase 4 — costruzione dell’universo dei candidati

**STATO: DA DEFINIRE / NON AVVIATA**

Questa fase dovrà costruire CANDIDATES_RAW_v01, cioè l’insieme completo e tracciabile delle aree realisticamente candidabili.
Da definire:
- categorie urbanistiche ammissibili;
- procedura di estrazione dei poligoni;
- gestione di contiguità, merge e split;
- canonicalizzazione dei duplicati;
- tolleranze geometriche;
- eventuali filtri territoriali preliminari;
- superficie minima motivata dall’Hub reale;
- CRS operativo;
- identificativi e versionamento.

Regola già consolidata: la soglia storica di circa 5.000 m² osservata nel progetto Claude **non viene ereditata automaticamente**.

---

# 14. Fase 5 — ammissibilità dei singoli siti

**STATO: DA DEFINIRE / NON AVVIATA**

L’obiettivo sarà eliminare i siti che non possono essere scelti indipendentemente dal punteggio.

Possibili famiglie di criteri: superficie insufficiente, incompatibilità urbanistica, impossibilità di accesso, non conformità AFIR/TEN-T applicabile, rischio idraulico o da frana incompatibile, vincoli ambientali o paesaggistici realmente ostativi.

Ogni esclusione dovrà riportare regola applicata, valore osservato, fonte e motivazione.

L’insieme dei candidati ammissibili dovrà essere congelato prima del ranking.
---

# 15. Fase 6 — indicatori

**STATO: DA DEFINIRE / NON AVVIATA**

Possibili macro-famiglie:
- accessibilità;
- domanda logistica e industriale;
- mobilità;
- popolazione servita;
- turismo;
- aree interne;
- caratteristiche dimensionali;
- compatibilità territoriale;
- ambiente e rischio;
- fattibilità energetica;
- costo o complessità di connessione.

Nessun indicatore viene mantenuto solo perché il dato è disponibile. Indicatori costanti o quasi costanti non devono essere presentati come discriminanti.

---

# 16. Fase 7 — fattibilità energetica

**STATO: DA DEFINIRE / NON AVVIATA**

Dovranno essere valutati, nei limiti dei dati disponibili, prossimità alla rete, livello di tensione, possibili punti di connessione, capacità disponibile, difficoltà/costo di connessione e compatibilità con fotovoltaico, accumulo ed eventuale elettrolisi.

Se il dato reale non esiste, il limite deve essere esplicitato.
---

# 17. Fase 8 — normalizzazione e pesi

**STATO: DA DEFINIRE / NON AVVIATA**

Le scale di normalizzazione e i pesi dovranno essere:
- espliciti;
- motivati;
- configurabili;
- documentati;
- sottoposti a verifica di sensibilità.

La normalizzazione min-max, se utilizzata, dovrà dichiarare l’insieme sul quale viene calcolata e l’effetto degli estremi.

---

# 18. Fase 9 — ranking dei siti

**STATO: DA DEFINIRE / NON AVVIATA**

Per ogni candidato ammissibile dovranno essere disponibili valori grezzi, valori normalizzati, peso, contributo di ogni indicatore, punteggio complessivo e posizione in graduatoria.

Il ranking misura la qualità individuale del sito, ma non seleziona automaticamente i cinque Hub finali.
---

# 19. Fase 10 — selezione della configurazione di 5 Hub

**STATO: DA DEFINIRE / NON AVVIATA**

La scelta finale deve essere formulata come problema di selezione/ottimizzazione esplicito.

Non sarà sufficiente prendere i primi cinque siti della graduatoria.

Dovranno essere definite e approvate, se applicabili:
- copertura territoriale;
- copertura di nodi urbani;
- obblighi o funzioni TEN-T;
- distanza minima tra Hub;
- eventuale distanza massima richiesta da normativa;
- copertura della domanda;
- equilibrio territoriale;
- funzione obiettivo.

Output previsto: SHORTLIST_5_v01.

---

# 20. Fase 11 — robustezza

**STATO: DA DEFINIRE / NON AVVIATA**

La soluzione dovrà essere stressata variando pesi, soglie, superficie minima, indicatori, assunzioni energetiche, assunzioni ambientali e funzione obiettivo.

La robustezza dovrà essere espressa con numeri, non con giudizi qualitativi.
---

# 21. Fase 12 — verifica puntuale dei 5 siti

**STATO: DA DEFINIRE / NON AVVIATA**

Per ciascun finalista dovranno essere verificati in dettaglio:
- geometria;
- accesso reale;
- urbanistica;
- rischio idraulico;
- frane;
- vincoli ambientali e paesaggistici;
- superficie effettivamente utilizzabile;
- proprietà e disponibilità;
- connessione energetica;
- ortofoto e criticità locali.

Una criticità bloccante può riportare il progetto alla fase precedente.

---

# 22. Fasi 13–15 — confronto, freeze e deliverable

## 22.1 Confronto con il progetto Claude

Il nuovo modello sarà confrontato con la baseline Claude per capire differenze in universo candidati, esclusioni, indicatori, pesi, ranking e cinque siti finali.

Il confronto non serve a forzare il nuovo modello verso il risultato storico.
## 22.2 Freeze del modello

Il modello potrà essere congelato solo quando dati e fonti sono registrati, metodologia è documentata, codice e configurazioni sono salvati, test e quality gate sono superati, ranking e shortlist sono verificati, robustezza è stata analizzata e handoff/commit sono completi.

## 22.3 Deliverable finali

Solo dopo il freeze saranno prodotti:
- relazione metodologica;
- relazione generale;
- schede sito;
- tabelle;
- mappe;
- tavole;
- eventuali dashboard;
- allegati tecnici.

I numeri finali dovranno essere generati dagli artifact congelati, non ricopiati manualmente.

---

# 23. Fonti e dataset: quadro sintetico

È importante non confondere il congelamento della metodologia con la validazione dei dati. Al momento le baseline metodologiche delle Fasi 1 e 2 sono FROZEN; molte fonti dati della Fase 3 sono invece SOURCE VERIFIED, REVIEW o IN VALIDAZIONE e potranno diventare baseline operative solo dopo i rispettivi quality gate.

| Tema | Fonte principale | Stato attuale | Uso consentito / limite |
|---|---|---|---|
| Baseline precedente | Progetto Claude + QGIS Beltrame | HISTORICAL / NON_AUTHORITATIVE | benchmark, source discovery, confronto finale |
| Urbanistica D/H | Regione FVG / WFS CER | HISTORICAL ONLY / SUPPORT ONLY | non rappresenta automaticamente PRGC 2026 |
| PRGC vigenti | Comuni FVG + EagleFVG/Regione | IN VALIDAZIONE | base current-first, Comune per Comune |
| Patrimonio regionale | Regione FVG | REVIEW | fonte parziale per proprietà pubblica |
| Lotti Consorzi | Consorzi di sviluppo economico locale | REVIEW | disponibilità parziale e dinamica |
| Grafo stradale FVG | Regione FVG / IRDAT | REVIEW | screening geometrico; routing di produzione non ancora validato |
| OSM congelato tesi | OpenStreetMap, baseline tecnica storica | SUPPORT / TO VERIFY | supporto topologico e confronto |
| TEN-T | Reg. UE 2024/1679 + DG MOVE / TENtec | SOURCE_VERIFIED / CROSSWALK_VALIDATED | 11 sezioni ufficiali aggregate in 6 assi FVG; classificazione corrente validata |
| PGRA | Autorità di Bacino / SIGMA | SOURCE VERIFIED, CURRENT VECTOR TO ACQUIRE | rischio idraulico corrente ancora da materializzare |
| PPR | Regione FVG / WebGIS PPR | SOURCE VERIFIED, EXTRACTION TO VALIDATE | riferimento paesaggistico vigente |
| Frane | Regione FVG / IRDAT | ENDPOINT VERIFIED / TO VALIDATE | semantica e ruolo normativo da definire |
| Natura 2000 e aree protette | Regione FVG / fonti ufficiali | ENDPOINT VERIFIED / TO VALIDATE | classificazione normativa da verificare |
| Rete elettrica | Terna / TE.R.R.A. | SOURCE VERIFIED / DATA ACCESS TO VALIDATE | non equivale a capacità disponibile |
| Capacità DSO | distributori locali | GAP CRITICO | capacità puntuale non disponibile in dataset validato |
| Popolazione | ISTAT | SOURCE VERIFIED | uso come indicatore ancora da decidere |
| Pendolarismo | ISTAT 2021 | SOURCE VERIFIED | stima 2021, non conteggio traffico |
| Turismo | Regione FVG / WebTur / ISTAT | TO VALIDATE RAW DATA | estratto riproducibile ancora da fissare |
| Aree interne | Presidenza del Consiglio / SNAI | SOURCE VERIFIED | uso come indicatore ancora da decidere |

---

# 24. Questioni aperte prioritarie

1. **Urbanistica:** completare la verifica dei PRGC vigenti e delle relative geometrie.
2. **Routing:** validare la rete definitiva per Light e Heavy, compresi sensi di marcia e restrizioni.
3. **TEN-T:** crosswalk route-level completato e validato; Q-METH-3.3-A risolta come non materialmente applicabile al dominio FVG corrente.
4. **Rischio idraulico:** acquisire e versionare i layer PGRA correnti.
5. **Paesaggio:** definire l’estrazione GIS riproducibile del PPR vigente.
6. **Energia:** chiarire quali dati reali di capacità e connessione siano ottenibili da Terna e distributori.
7. **Proprietà e disponibilità:** il metodo è definito, ma manca un dataset region-wide completo.
8. **Superficie minima:** dovrà derivare da requisiti reali dell’Hub, non dalla soglia storica di 5.000 m².
9. **Categorie urbanistiche ammissibili:** da definire dopo la costruzione della base urbanistica corrente.
10. **Indicatori, pesi e ottimizzazione:** volutamente rinviati alle fasi successive e soggetti ad approvazione esplicita.

---

# 25. Glossario essenziale

**AFIR** — Alternative Fuels Infrastructure Regulation, regolamento europeo sulle infrastrutture per combustibili alternativi.

**TEN-T** — Trans-European Transport Network, rete transeuropea dei trasporti.

**Core / Extended Core / Comprehensive** — i tre livelli della rete TEN-T vigente.

**PRGC** — Piano Regolatore Generale Comunale.

**PPR** — Piano Paesaggistico Regionale.

**PGRA** — Piano di Gestione del Rischio di Alluvioni.

**GIS** — sistema informativo geografico.

**WFS** — Web Feature Service, servizio web che espone geometrie e attributi vettoriali.

**OSM** — OpenStreetMap.

**Routing** — calcolo di un percorso lungo una rete stradale con regole di percorrenza.

**Road anchor** — punto della rete stradale al quale viene collegato un accesso del candidato.

**Lineage / provenance** — tracciabilità della provenienza e delle trasformazioni di un dato.

**Proxy** — variabile usata come approssimazione di un fenomeno non direttamente misurabile.

**RTN** — Rete di Trasmissione Nazionale.

**DSO** — gestore della rete di distribuzione elettrica.

**FROZEN** — elemento approvato e congelato; non modificabile senza nuova versione e approvazione.

**ACCEPTED** — scelta approvata e operativa ma non ancora necessariamente congelata come baseline finale.

---

# 26. Tracciabilità delle principali decisioni interne

Questa sezione serve solo a collegare il testo leggibile ai registri interni.

## Definizione dell’Hub — FROZEN

- F1-D1: tutti e 5 gli Hub = H₂ pubblico + ricarica DC pubblica.
- F1-D2: requisiti AFIR H₂ specifici solo per Hub con funzione AFIR/TEN-T.
- F1-D3: ricarica per Light + Heavy.
- F1-D4: produzione rinnovabile in sito non obbligatoria.
- F1-D5: H₂ rinnovabile/certificato non obbligatorio nella configurazione minima.
- F1-D6: architettura H₂ non predefinita.
- F1-D7: altri vettori opzionali.

Baseline: docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md.

## Unità di analisi — FROZEN

- F2-D1: candidato = area/poligono.
- F2-D2: multipart disconnessi separati salvo continuità reale.
- F2-D3: punto rappresentativo interno, non centroide/accesso.
- F2-D4: accessi multipli e road anchor distinti.
- F2-D5: canonicalizzazione di duplicati/sovrapposizioni.
- F2-D6: identificativo logico separato da versione geometrica.
- F2-D7: confine comunale non implica split automatico.
- F2-D8: tolleranze geometriche numeriche rinviate alla qualità dei dati.

Baseline: docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md.

## Decisioni Fase 3 già approvate

- DEC-0031: layer D/H della Mosaicatura PRG 2018 non sono urbanistica corrente 2026.
- DEC-0032: procedura urbanistica current-first/ibrida approvata.
- DEC-0033: disponibilità fisica e disponibilità proprietaria/commerciale trattate separatamente; UNKNOWN non equivale a indisponibile.
- DEC-0034: autorizzata Chat 3.7 per crosswalk TEN-T FVG e verifica della rilevanza delle uscite AFIR.
- DEC-0035: accettato il PASS tecnico-operativo della Chat 3.7; ISS-0005 risolta sul piano tecnico.
- DEC-0036: Q-METH-3.3-A risolta come non materialmente applicabile al dominio FVG corrente; nessuna regola artificiale per rotatorie/intersezioni a raso.
- DEC-0037: autorizzata Chat 3.4 per validazione dei vincoli territoriali, ambientali e paesaggistici.
- DEC-0038: accettato il PASS tecnico-operativo della Chat 3.4; ISS-0008 PPR RESOLVED; ISS-0006 PGRA e ISS-0011 biotopi restano OPEN.
- DEC-0039: approvato il trattamento PGRA senza hard filter generale; esclusione solo quando imposta dalla disciplina vigente o da incompatibilità tecnica non ragionevolmente mitigabile; negli altri casi pericolosità/allagabilità resta un fattore negativo di futura valutazione.
- DEC-0040: approvato il trattamento delle frane con PAI vigente completo come riferimento operativo/normativo principale; Catasto Frane e perimetri inventariali restano supporto conoscitivo; ISS-0012 aperta per acquisizione/validazione della cartografia PAI corrente completa.
- DEC-0041: approvato il pre-screening Natura 2000 automatico con uso prioritario delle prevalutazioni regionali e delle aree di interferenza; VINCA formale fuori dal modello; ISS-0013 aperta per la codifica riproducibile delle regole regionali.

---

# 27. Riferimenti normativi e istituzionali principali già presenti nel progetto

- Regolamento (UE) 2023/1804 — AFIR.
- Regolamento (UE) 2024/1679 — TEN-T.
- Legge Regionale FVG 11 ottobre 2012, n. 19.
- Regione FVG / IRDAT / GeoServer regionale.
- EagleFVG e fonti comunali ufficiali per PRGC.
- Autorità di Bacino Distrettuale delle Alpi Orientali / SIGMA per PGRA.
- Regione FVG / WebGIS PPR.
- Terna / TE.R.R.A.
- distributori di rete elettrica competenti.
- ISTAT per popolazione, pendolarismo e dati statistici.
- Presidenza del Consiglio / politiche di coesione per Aree Interne.
- Regione FVG / WebTur / ISTAT per turismo.

Per ogni dataset effettivamente utilizzato nel modello dovranno essere conservati: fonte, versione/data, percorso, licenza se rilevante, hash della materializzazione, uso previsto e stato di validazione.

---

# 28. Come completare questa relazione nelle fasi successive

Questa relazione è volutamente uno **scheletro vivo**.

Quando una fase viene chiusa:
1. sostituire il testo DA DEFINIRE con la metodologia approvata;
2. riportare la fonte dati effettivamente utilizzata;
3. indicare versione e artifact ufficiali;
4. spiegare la scelta in linguaggio leggibile, non solo tramite codici interni;
5. mantenere in appendice la tracciabilità verso decisioni, issue e commit;
6. non anticipare come definitivi risultati ancora in REVIEW.

La versione finale della relazione dovrà poter essere letta da una persona esterna al progetto senza dover consultare le chat per capire che cosa è stato deciso, perché e con quali dati.

