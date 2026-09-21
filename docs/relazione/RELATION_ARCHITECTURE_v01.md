# RELAZIONE ESTERNA 5 HUB — ARCHITETTURA EDITORIALE E SCHELETRO v01

**Chat:** 90.0 — Relazione Builder
**Data:** 2026-09-21
**Stato:** PROPOSED — da sottoporre a review della Chat 0.2
**Perimetro:** architettura editoriale della relazione esterna; nessuna nuova decisione metodologica.

## 1. Scopo dell'architettura

La relazione finale è destinata a un lettore terzo che non conosce chat, codici decisionali, branch o procedure interne.
Deve spiegare in modo autosufficiente: cosa si localizza, perché, con quali dati, con quale metodo, quali risultati si ottengono e quali limiti restano.

La struttura proposta non replica la sequenza cronologica delle fasi interne.
La roadmap resta la struttura di sviluppo del modello; la relazione adotta invece una narrazione tecnica orientata al problema decisionale.

## 2. Base autorevole consultata

La ricostruzione dello stato al 2026-09-21 usa, in ordine di priorità:
- istruzioni persistenti del progetto;
- PROJECT_SOURCE_OF_TRUTH, stato ACTIVE con Fase 3 in corso;
- PROJECT_CONTROL_REGISTER, letto fino a DEC-0059 e allo stato corrente di DATA_REGISTRY e ISSUES;
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md` — FROZEN;
- review e baseline Fase 3 accettate dalla Chat 0.2;
- `docs/ROADMAP_METODOLOGICA_v1.md`;
- `docs/RELAZIONE_QUADRO_PROGETTO_5_HUB_v01.md` soltanto come precedente bozza editoriale DRAFT.

Gli output non ancora revisionati della Chat 3.12 sono esclusi dal contenuto consolidato.
Possono essere citati soltanto come lavoro in corso, mai come baseline accettata.

## 3. Definizione degli stati editoriali

**READY**: il capitolo può essere scritto in forma sostanzialmente stabile usando decisioni FROZEN/ACCEPTED e fonti già validate; potranno restare normali rifiniture editoriali o bibliografiche.

**PARTIAL**: esiste una base consistente e già approvata, ma il capitolo dipende anche da attività o decisioni ancora aperte. Si può redigere solo la parte consolidata, marcando chiaramente ciò che resta provvisorio.

**NOT_READY**: il contenuto sostanziale dipende da fasi non ancora avviate o da risultati non ancora disponibili. È ammesso solo lo scheletro, non una narrazione che anticipi risultati o scelte.

## 4. Indice ragionato proposto

### Front matter
- Titolo, committente/progetto, versione, data.
- Nota sul perimetro del documento.
- Elenco acronimi essenziali.
- Eventuale elenco figure e tabelle.

### Executive summary
Sintesi del problema, approccio, dati principali, metodo, risultati, principali limiti e implicazioni operative.
**Stato: PARTIAL.** Obiettivo e impostazione sono disponibili, ma risultati e conclusioni non esistono ancora.

### 1. Contesto, obiettivi e problema di localizzazione
Inquadra la finalità dei 5 Hub Energetici Green in Friuli Venezia Giulia e delimita ciò che il modello fa e non fa.
Evita di raccontare l'organizzazione interna del progetto.
**Stato: READY.**

### 2. Quadro normativo e strategico
Raccoglie solo le norme e gli atti che generano requisiti localizzativi o di verifica: AFIR, TEN-T, disciplina regionale degli impianti stradali, pianificazione e tutele territoriali pertinenti.
Distingue obblighi normativi, condizioni di applicabilità e scelte progettuali.
**Stato: PARTIAL.** Il nucleo normativo è già solido, ma il corpus Natura 2000/prevalutazioni è ancora in formalizzazione.

### 3. Definizione funzionale degli Hub Energetici Green
Spiega il nucleo minimo comune H2 pubblico + ricarica DC pubblica, la copertura Light/Heavy e gli elementi volutamente non predefiniti.
Chiarisce il rapporto condizionato con i requisiti AFIR/TEN-T e il fatto che il modello è localizzativo, non di progettazione impiantistica.
**Stato: READY.**

### 4. Perimetro territoriale e unità di analisi
Definisce il candidato come area/poligono fisicamente localizzabile.
Spiega geometrie ausiliarie, point-on-surface, accessi, road anchor, multipart, duplicati, confini comunali, identity/versioning e regola generale sulle distanze.
**Stato: READY.**

### 5. Dati, fonti informative e qualità
Presenta le famiglie di dati utilizzate, la loro provenienza, currentness, copertura, licenza, ruolo e limiti.
Introduce una tassonomia leggibile tra dato osservato, fonte ufficiale, proxy, baseline interna riutilizzata e gap.
**Stato: PARTIAL.** La Fase 3 è ancora in corso.

### 6. Architettura complessiva del metodo di localizzazione
Descrive il flusso logico: costruzione candidati, ammissibilità, valutazione, ranking individuale, selezione della configurazione di 5 siti, robustezza e verifica finale.
Questa sezione deve spiegare il metodo senza usare la numerazione delle fasi come struttura narrativa principale.
**Stato: PARTIAL.** La pipeline è definita, ma molte operazionalizzazioni future non sono ancora approvate.

### 7. Costruzione dell'universo dei candidati
Descriverà le categorie territoriali effettivamente utilizzate, la generazione dei poligoni, canonicalizzazione, split/merge, superficie, lineage, proxy urbanistici e QA.
Dovrà quantificare l'universo risultante e spiegare come si passa dalle fonti ai candidati.
**Stato: NOT_READY.** La Fase 4 non è ancora aperta.

### 8. Ammissibilità e controlli di esclusione
Distinguerà hard constraints, verifiche normative, condizioni di incompatibilità e flag che richiedono approfondimento.
Dovrà documentare per ogni esclusione regola, valore osservato e fonte.
**Stato: PARTIAL.** Esistono regole accettate per diverse tutele, ma non esiste ancora il set operativo completo applicato ai candidati.

### 9. Accessibilità, rete TEN-T e domanda di mobilità
Riunisce in un'unica narrazione: TEN-T corrente, uscite rilevanti, domanda Light, domanda Heavy, corridoi/path-flow e verifica locale degli accessi.
Mantiene separati domanda macro, rete/path e accessibilità fisica-legale del singolo candidato.
**Stato: PARTIAL.** Le baseline macro sono accettate; mancano ancora accessi candidati e metriche finali.

### 10. Fattibilità energetica e prossimità alla rete elettrica
Spiega il ruolo del proxy territoriale di prossimità all'infrastruttura elettrica.
Distingue esplicitamente prossimità da capacità disponibile, punto di connessione, costo e fattibilità tecnica.
**Stato: PARTIAL.** Baseline dati accettata; geometria target, metrica e soglie del futuro indicatore non sono ancora definite.

### 11. Vincoli territoriali, ambientali e paesaggistici
Organizza PGRA, PAI/frane, Natura 2000, parchi/riserve/biotopi/prati stabili e PPR per funzione modellistica.
Per ogni tema separa pre-screening, verifica normativa, possibile incompatibilità e futuro eventuale contributo valutativo.
**Stato: PARTIAL.** Molte regole sono ACCEPTED; il rule-set Natura 2000 è ancora in corso.

### 12. Sistema degli indicatori
Definirà per ogni indicatore significato, fonte, unità, geometria, formula, direzione preferenziale, missing values e capacità discriminante.
La sezione dovrà mostrare perché ogni indicatore esiste e quale domanda decisionale risponde.
**Stato: NOT_READY.**

### 13. Normalizzazione, pesi e ranking dei singoli siti
Documenterà trasformazioni, scale, pesi, configurazioni, contributi elementari, punteggio finale e controlli numerici.
Dovrà distinguere il ranking individuale dalla scelta della rete di cinque Hub.
**Stato: NOT_READY.**

### 14. Selezione della configurazione di 5 Hub
Descriverà il modello esplicito di selezione/ottimizzazione, funzione obiettivo, vincoli di rete/copertura e motivazione della cinquina.
Dovrà mostrare perché i cinque siti sono selezionati rispetto ad alternative prossime.
**Stato: NOT_READY.**

### 15. Analisi di robustezza e sensibilità
Documenterà variazioni di pesi, soglie, indicatori e scenari, frequenza di permanenza dei siti e alternative ricorrenti.
Nessuna affermazione di robustezza sarà ammessa senza risultati quantitativi.
**Stato: NOT_READY.**

### 16. Risultati e interpretazione territoriale
Presenterà universo iniziale, esclusioni, shortlist, ranking, configurazione finale, mappe e lettura territoriale dei risultati.
Dovrà distinguere risultati del modello da interpretazioni e da verifiche successive.
**Stato: NOT_READY.**

### 17. Verifica puntuale dei siti selezionati
Per ogni finalista: geometria, accessi reali, urbanistica corrente, PAI/PGRA, tutele, superficie, proprietà/disponibilità, energia, ortofoto e criticità locali.
Includerà i flag di verifica obbligatoria già emersi nel progetto.
**Stato: NOT_READY.**

### 18. Limiti, incertezza e uso corretto dei risultati
Raccoglie limiti di dati, proxy, currentness, scala macro, assenza di capacità elettrica region-wide, disponibilità fondiaria incompleta e differenza tra screening e autorizzazione/progettazione.
Distingue limiti risolti proceduralmente da informazioni realmente acquisite.
**Stato: PARTIAL.**

### 19. Conclusioni e indicazioni per le fasi successive
Sintetizzerà i risultati, le condizioni di utilizzo della cinquina e gli approfondimenti necessari prima di progettazione o investimento.
**Stato: NOT_READY.**

### Fonti normative, dati e bibliografia esterna
Sezione separata dalle fonti interne del progetto.
La struttura proposta è definita al § 7.

### Appendice A — Tracciabilità metodologica e documentale interna
Mappa sezioni della relazione a decisioni, baseline, DATA_REGISTRY, review, artifact e commit.
Non sostituisce la bibliografia esterna e non deve appesantire il corpo principale.

### Appendici tecniche ulteriori
Da attivare solo quando esiste contenuto reale: dizionario indicatori, tabelle di esclusione, parametri, QA, schede sito, dettagli di robustezza.
**Stato: NOT_READY / evolutivo.**

## 5. Skeleton operativo per capitolo

| Sezione | Obiettivo | Materiali interni principali | Fonti esterne principali richieste | Readiness |
|---|---|---|---|---|
| Executive summary | Dare una visione completa in 2–4 pagine | Tutta la baseline finale e risultati | Solo fonti citate nel testo principale | PARTIAL |
| 1. Contesto e obiettivi | Definire problema e perimetro | SOT, Fase 1, roadmap | Documenti strategici di progetto solo se pubblici/rilevanti | READY |
| 2. Quadro normativo | Tradurre norme in requisiti localizzativi | Fase 1; DEC territoriali accettate | AFIR; Reg. TEN-T 2024/1679; LR FVG 19/2012; atti PGRA/PAI/PPR/Natura 2000 | PARTIAL |
| 3. Definizione Hub | Spiegare cosa viene localizzato | FASE_1_HUB_DEFINITION_CONSOLIDATED_v02 | AFIR e LR FVG per i soli requisiti normativi richiamati | READY |
| 4. Unità di analisi | Spiegare che cosa è un candidato | FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01 | Eventuale letteratura GIS/metodologica solo se utile | READY |
| 5. Dati e qualità | Rendere trasparenti fonti, versioni e limiti | DATA_REGISTRY; review Fase 3 | IRDAT/FVG; TENtec; ISTAT; Distretto; OSM; DSO/GSE/Terna; fonti comunali | PARTIAL |
| 6. Metodo complessivo | Spiegare la catena decisionale | Roadmap; SOT; decisioni ACCEPTED | Letteratura di localizzazione/MCDM/ottimizzazione da selezionare in seguito | PARTIAL |
| 7. Universo candidati | Ricostruire fonte→poligono candidato | DEC-0032/0048; futura Fase 4 | PRGC/IRDAT/Comuni e relative fonti vigenti | NOT_READY |
| 8. Ammissibilità | Esplicitare regole di esclusione/verifica | DEC-0039…0043; future regole F5 | NTA PGRA/PAI; PPR; Natura 2000; urbanistica; sicurezza/accesso applicabile | PARTIAL |
| 9. Mobilità/TEN-T | Misurare domanda e accessibilità | DEC-0035/0036/0054/0055; baseline Light/Heavy | TENtec; OSM; ISTAT; provenance Speth/ETISplus; eventuali gestori stradali | PARTIAL |
| 10. Energia | Valutare prossimità e limiti del proxy | DEC-0050/0052/0053; review 3.5 | OSM/Overpass; aree convenzionali FVG/GSE; DSO; Terna | PARTIAL |
| 11. Territorio/ambiente | Gestire rischi e tutele | DEC-0039…0043; DEC-0057/0058; Chat 3.12 dopo review | Distretto Alpi Orientali; Regione FVG; PPR; Natura 2000 e atti regionali | PARTIAL |
| 12. Indicatori | Definire misure discriminanti | Futuri artifact F6/F7 | Fonti dati già validate + letteratura metodologica | NOT_READY |
| 13. Normalizzazione/ranking | Rendere ricostruibile il punteggio | Futuri artifact F8/F9 | Letteratura metodologica solo per giustificare tecniche adottate | NOT_READY |
| 14. Selezione 5 Hub | Selezionare una configurazione, non i primi cinque | Futuri artifact F10 | Letteratura di ottimizzazione/localizzazione se adottata | NOT_READY |
| 15. Robustezza | Misurare dipendenza dalle assunzioni | Futuro report F11 | Letteratura sensitivity/robustness se utile | NOT_READY |
| 16. Risultati | Comunicare output e mappe | Ranking, shortlist, GIS finali | Nessuna nuova fonte salvo contesto territoriale | NOT_READY |
| 17. Verifica finalisti | Verificare i siti sul terreno/documenti correnti | Future schede F12 | PRGC correnti, PAI/PGRA, PPR, DSO, catasto/proprietà, ortofoto, gestori stradali | NOT_READY |
| 18. Limiti | Rendere esplicita l'incertezza | ISSUES; review; caveat DATA_REGISTRY | Fonti esterne necessarie a qualificare singoli limiti | PARTIAL |
| 19. Conclusioni | Sintetizzare risultato e uso corretto | Tutti gli output finali | Nessuna nuova fonte salvo richiami | NOT_READY |

## 6. Regole editoriali di separazione delle evidenze

Nel corpo principale ogni affermazione importante deve essere riconoscibile come una delle seguenti categorie:
- fatto o dato osservato;
- requisito normativo;
- risultato del modello;
- assunzione;
- proxy;
- scelta progettuale/metodologica;
- limite o incertezza;
- elemento ancora da verificare.

Le decisioni interne non devono essere presentate al lettore come fonti scientifiche.
I codici DEC/ISS e i nomi delle chat restano nell'Appendice A o nelle note tecniche di tracciabilità.

Un contenuto DRAFT/PROPOSED/REVIEW non deve essere riscritto in forma assertiva come se fosse consolidato.
Quando una scelta futura è indispensabile a completare un capitolo, lo skeleton resta vuoto o marcato `[DA COMPLETARE DOPO APPROVAZIONE]`.

## 7. Struttura delle fonti esterne e della bibliografia

Si propone un unico registro esterno strutturato, da cui generare la sezione finale della relazione.

### 7.1 Categorie
1. Normativa e regolamenti UE/nazionali/regionali.
2. Piani, delibere, norme tecniche e atti di pianificazione/tutela.
3. Dataset, cartografie e servizi geospaziali ufficiali.
4. Statistiche e fonti di domanda.
5. Documentazione tecnica di enti gestori e operatori.
6. Letteratura scientifica e metodologica.
7. Dati/open data di comunità utilizzati come proxy, con attribuzione e licenza.

### 7.2 Campi minimi del registro
- `citation_key`;
- categoria;
- titolo;
- ente/autore;
- numero dell'atto o identificatore;
- versione/data;
- URL o identificatore persistente;
- data di accesso;
- copertura territoriale/temporale;
- uso nella relazione;
- licenza/condizioni di riuso quando rilevanti;
- stato di verifica;
- eventuale percorso di evidenza preservata.

### 7.3 Convenzione proposta per le chiavi
Formato editoriale: `EXT-[TIPO]-[ENTE]-[ANNO]-NN`.
Esempi di tipo: `REG`, `PLAN`, `DATA`, `STAT`, `TECH`, `LIT`.
La chiave serve al source register; nel testo si privilegia una citazione leggibile per ente/atto.

### 7.4 Nucleo esterno già chiaramente richiesto
- Regolamento (UE) 2023/1804 — AFIR, versione applicabile;
- Regolamento (UE) 2024/1679 — TEN-T;
- LR FVG 11 ottobre 2012, n. 19, per i requisiti pertinenti;
- fonti ufficiali TENtec/DG MOVE;
- PRGC, IRDAT e fonti comunali utilizzate;
- PGRA e PAI dell'Autorità di Bacino Distrettuale delle Alpi Orientali;
- PPR e fonti regionali FVG per aree protette/Natura 2000;
- ISTAT per popolazione/pendolarismo e altri dati effettivamente usati;
- OSM/Overpass con corretta attribuzione ODbL quando utilizzato;
- GSE/DSO/Terna per i riferimenti elettrici effettivamente utilizzati;
- fonti originarie/metodologiche Speth/ETISplus se i dati Heavy compaiono nella relazione.

## 8. Appendice A — struttura della tracciabilità interna

La matrice di tracciabilità deve essere separata dalla bibliografia esterna.

Campi minimi proposti:
- capitolo/sezione relazione;
- tema/claim;
- readiness;
- stato interno dell'evidenza;
- decisioni DEC rilevanti;
- documenti FROZEN/ACCEPTED;
- DATA_REGISTRY ID;
- review/handoff;
- artifact tecnico;
- commit Git rilevante;
- issue/gap associati;
- note di aggiornamento.

Regola: la matrice deve permettere di risalire dal testo esterno all'origine interna senza costringere il lettore principale a conoscere la governance del progetto.

Una prima matrice è salvata in `RELATION_TRACEABILITY_MATRIX_v01.csv`.

## 9. Capitoli oggi non scrivibili in forma definitiva

Non sono oggi scrivibili in modo sostanziale e definitivo:
- Cap. 7 — universo candidati;
- Cap. 12 — indicatori;
- Cap. 13 — normalizzazione, pesi e ranking;
- Cap. 14 — selezione dei 5 Hub;
- Cap. 15 — robustezza;
- Cap. 16 — risultati;
- Cap. 17 — verifica puntuale finalisti;
- Cap. 19 — conclusioni finali.

Il Cap. 8 può essere scritto solo nella parte concettuale già approvata.
I Cap. 5, 9, 10 e 11 possono essere sviluppati in modo consistente ma devono conservare i limiti e le parti ancora aperte della Fase 3.

## 10. Gap editoriali/metodologici da non nascondere

- Fase 3 non ancora PASS/CLOSED.
- ISS-0013 Natura 2000 è OPEN e la Chat 3.12 è in corso; i suoi output non sono ancora baseline accettata.
- ISS-0009 resta OPEN come gap region-wide di proprietà/disponibilità, pur con trattamento metodologico già deciso.
- ISS-0002 resta OPEN sulla ricostruibilità dell'universo storico Claude/QGIS e non autorizza il suo riuso come universo candidati.
- La base urbanistica per screening è ACCEPTED con limitazioni e proxy di currentness espliciti; la verifica corrente puntuale resta obbligatoria sui finalisti.
- Il proxy elettrico non fornisce capacità disponibile o connessione garantita.
- Le baseline Light/Heavy sono valide per pianificazione macro, non per dimostrare accessibilità locale del sito.
- Il PAI macro usa un fallback procedurale: il gap di vettore pubblico completo non è scomparso.
- Categorie candidate, superficie minima, tolleranze geometriche, indicatori, metriche, soglie, pesi e ottimizzazione non devono essere anticipati.

## 11. Chat 90.x consigliate dopo review della Chat 0.2

**Chat 90.1 — Fonti esterne e bibliografia.**
Mandato: costruire il registro delle fonti esterne, verificare versioni/date/licenze/citazioni e preparare la bibliografia senza modificare metodologia.

**Chat 90.2 — Matrice di tracciabilità interna.**
Mandato: completare la mappa sezione→DEC/baseline/DATA_REGISTRY/review/artifact/commit e mantenerla aggiornata.

**Chat 90.3 — Redazione capitoli consolidati F1/F2.**
Mandato: trasformare in prosa esterna i soli capitoli READY 1, 3 e 4, senza anticipare Fase 4+.

**Chat 90.4 — Figure, tabelle e registro visuale.**
Da aprire più avanti, quando esistono candidati e risultati sufficienti; non è prioritaria ora.

## 12. Quality gate editoriale del presente skeleton

- Indice orientato al lettore esterno: PASS.
- Non replica meccanicamente la roadmap interna: PASS.
- Collocazione dei principali blocchi metodologici: PASS.
- Separazione fonti esterne / tracciabilità interna: PASS.
- Readiness esplicita per ogni capitolo: PASS.
- Gap e dipendenze aperte espliciti: PASS.
- Nessuna nuova soglia, peso, indicatore o regola metodologica introdotta: PASS.
- Persistenza nel repository su branch dedicato Chat 90.0: PASS dopo commit.
- Review finale richiesta alla Chat 0.2 prima di procedere alla redazione massiva.
