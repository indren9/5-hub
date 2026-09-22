# CLAUDE PIPELINE REQUIREMENTS INPUT v01 — REVIEWED

**Chat di origine:** 90.5 — Audit stralci relazione e integrazione MODEL_v2
**Data:** 2026-09-21
**Stato:** REVIEWED / ACCEPTED AS PROMPT-BUILD INPUT — non approva le scelte metodologiche pendenti
**Uso previsto:** input ripulito per una successiva costruzione del prompt/pipeline Claude
**Importante:** questo file **NON è il prompt Claude finale** e non approva nuove scelte metodologiche.

## BASELINE_ACCEPTED

### A. Scopo e significato del MODEL_v2

- Il progetto sviluppa un modello GIS multicriterio riproducibile di pianificazione strategica territoriale per selezionare una configurazione di **cinque** Hub Energetici Green in Friuli Venezia Giulia.
- L'unità di analisi è il **poligono** come alternativa localizzativa territoriale.
- I cinque poligoni finali non equivalgono a terreni già verificati per proprietà, disponibilità commerciale, autorizzabilità, accesso locale definitivo, capacità elettrica reale o cantierabilità.
- Il ranking/score individuale, se adottato, è distinto dalla qualità della configurazione di cinque Hub.
- La cinquina deve derivare da una procedura dichiarata e riproducibile; non può essere ottenuta semplicemente prendendo i primi cinque del ranking individuale.
- Robustezza/sensitivity quantitativa è richiesta prima del freeze finale.

### B. Definizione funzionale dell'Hub

- Tutti e cinque gli Hub integrano **H2 accessibile al pubblico + ricarica elettrica DC accessibile al pubblico** come nucleo minimo comune.
- Il modulo EV deve poter servire **veicoli Light e Heavy**.
- FER fisica in sito non è obbligatoria.
- H2 rinnovabile/certificato non è requisito universale del nucleo minimo.
- **Elettrolizzatore in sito obbligatorio in tutti e cinque gli Hub** (DEC-0068), ma senza effetto su generazione candidati, ammissibilità, scoring o configurazione territoriale; eventuali approvvigionamenti H2 aggiuntivi (tube trailer, pipeline o altre soluzioni) restano aperti.
- Biocarburanti e altri vettori non fanno parte del nucleo minimo comune.
- **BESS opzionale**: non fa parte del nucleo minimo obbligatorio e non condiziona generazione candidati, ammissibilità, scoring o configurazione del MODEL_v2, salvo futura decisione esplicita (DEC-0067).

### C. DQ-01 — universo candidati già APPROVATO

- Famiglia generatrice principale: urbanistica/pianificazione ufficiale **best-available current-first**.
- CER/Mosaicatura PRG 2018: solo ultima risorsa storica/proxy dichiarata.
- Classi generatrici approvate:
  - `G1_PRODUCTIVE`;
  - `G2_COMMERCIAL_TERTIARY`;
  - `G3_LOGISTICS_TRANSPORT`;
  - `G4_MIXED_RELEVANT`;
  - `G5_TECHNICAL_UTILITY_ENERGY`.
- Multipart disconnessi: split di default.
- Nessun dissolve/merge generalizzato; merge solo per identità logica/frammentazione tecnica documentata.
- Canonicalizzazione guidata da identità e lineage, non da soglie arbitrarie di overlap.
- Superficie minima HARD: **area lorda del poligono >= 8.000 m²**, misurata dopo repair deterministico e split.
- `candidate_id` logico stabile + `candidate_version` + `universe_version` + `geometry_hash` + lineage e QA deterministico.
- DQ-01 non applica hard filter di idoneità su energia, accesso locale, TEN-T, PGRA, PAI, PPR, Natura 2000, parchi/riserve, biotopi o prati stabili.

### D. Routing / domanda / TEN-T già acquisiti come baseline tecnica

- Light: riuso macro di `G_OSM_operativo`, `Gamma_OSM` e `OD_PATH_SYSTEM_OSM` FROZEN secondo DEC-0054/DEC-0055.
- Heavy: riuso della baseline Heavy 6.0 / Speth-ETISplus secondo DEC-0055.
- Il grafo stradale regionale FVG non è sufficiente da solo per routing di produzione, ma non è più un blocker.
- Accesso locale definitivo e restrizioni esecutive del singolo sito sono post-model salvo futura regola GIS esplicitamente approvata.
- Crosswalk TEN-T FVG validato: 11 sezioni ufficiali aggregate in 6 assi; 9 CORE, 0 EXTENDED CORE, 2 COMPREHENSIVE-only.
- Nearest exit: punto di divergenza della rampa dalla carreggiata TEN-T; non introdurre pseudo-uscite a raso nel dominio corrente.

### E. Energia e ambiente — principi già accettati

- Prossimità all'infrastruttura elettrica = **proxy**; non equivale a MW disponibili, punto di connessione o fattibilità garantita.
- Capacità, punto e costo reale di connessione sono post-model.
- Nessun tematismo ambientale diventa hard filter o penalizzazione per semplice intersezione/presenza.
- PGRA: pericolosità/allagabilità non implica esclusione automatica.
- PAI vigente: riferimento normativo principale per frane; Catasto Frane/IFFI = supporto.
- Natura 2000: pre-screening/flag; niente hard/penalty automatici per sola distanza/intersezione; nessun `VINCA_PASSED` automatico.
- Parchi/riserve: nessuna esclusione automatica per sola intersezione.
- Prati stabili: `DEROGA_REQUIRED` resta flag; nessuna penalizzazione è pre-approvata.
- PPR: `PPR_CHECK_REQUIRED` nei casi prescrittivi; nessun punteggio PPR generico.

### F. AFIR — fatti normativi verificati

Fonte primaria verificata: Regolamento (UE) 2023/1804, versione consolidata EUR-Lex corrente al 08/01/2026:
https://eur-lex.europa.eu/eli/reg/2023/1804/2026-01-08

- «Lungo la rete stradale TEN-T»: EV sulla TEN-T o entro **3 km di distanza stradale** dall'uscita più vicina; H2 sulla TEN-T o entro **10 km di distanza stradale**.
- Entro **31/12/2030**, lungo la **TEN-T core**, stazioni H2 accessibili al pubblico a distanza massima **200 km** tra loro.
- Target art. 6: capacità cumulativa minima **1 t/giorno** e almeno un dispenser **700 bar**.
- Il requisito 200 km dell'art. 6 è sulla **core**; non va esteso automaticamente alla comprehensive.
- Secondo F1-D2/DEC-0007, queste specifiche H2 sono obbligatorie solo per gli Hub cui venga assegnata una funzione AFIR/TEN-T pertinente; non sono automaticamente requisiti universali dei cinque Hub.

## USER_REQUIREMENT_PENDING_INTEGRATION

### UR-01 — distanza minima tra Hub

- Lo stralcio utente dichiara come requisito di commessa una **distanza minima di 10 km tra i cinque Hub**.
- Questo requisito è distinto dai 10 km AFIR che definiscono la posizione H2 «lungo TEN-T».
- Stato: **PENDING USER APPROVAL / DQ-07-DQ-08**. Non applicare finché non è formalmente integrato nel configuration contract.

### UR-02 — pipeline Claude

- In una fase successiva dovrà essere riusata una pipeline Claude esistente e il materiale fornito dall'utente.
- La pipeline dovrà distinguere chiaramente baseline approvata, fatti verificati, assunzioni/proxy, requisiti pendenti e contenuti superseded.
- Gli output futuri dovranno riportare assunzioni, limitazioni e requisiti non valutabili.
- Stato: requisito operativo per la fase successiva; **non** autorizza la Chat 90.5 a scrivere ora il prompt Claude finale.

## VERIFIED_NEW_FACT

### VF-01 — impianto H2 APT Monfalcone Lisert

Fonti:
- APT EcoMove: https://www.aptgorizia.it/gli-impianti-apt-ecomove/
- APT 2026, lavori avanzati: https://www.aptgorizia.it/apt-news/assemblea-dei-soci-crescita-transizione-ecologica/
- NAHV Testbed Catalogue May 2025: https://www.nahv.eu/wp-content/uploads/2025/05/NAHV-testbeds-catalogue-may-2025.pdf
- Prefettura di Gorizia 13/11/2025: https://prefettura.interno.gov.it/it/prefetture/gorizia/notizie/vigilanza-e-tutela-legalita-e-trasparenza-nei-lavori-pubblici
- FVG Energia 2026: https://prod-energia.regione.fvg.it/notizie/article/Mobilita-sostenibile-incontro-con-Apt-Goriziabr--sullo-sviluppo-delle-stazioni-multienergia/

Fatti verificati:
- soggetto: **APT Gorizia**;
- area: zona industriale **Monfalcone Lisert**, nuova sede/area operativa con accesso da via Consiglio d'Europa;
- impianto integrato produzione/distribuzione H2 con elettrolizzatore e fotovoltaico;
- capacità pubblicate **source-dependent**: NAHV (maggio 2025) indica **400 kg H2/giorno di produzione**; la pagina ufficiale APT corrente indica **453 kg H2/giorno di produzione massima** e circa **300 kg H2/giorno di capacità media di rifornimento**; IIT Hydrogen riporta **400 kg/giorno di capacità** per il progetto in realizzazione;
- dispenser: **2 × 350 bar** per bus + **1 × 700 bar** per veicoli;
- stato documentato nel 2026: lavori/realizzazione in fase avanzata; **operatività/commissioning non verificata al 21/09/2026**.

Caveat AFIR:
- il 700 bar è documentato;
- i valori di capacità pubblicati non sono univoci e non costituiscono, senza validazione tecnica aggiornata, prova della capacità cumulativa di rifornimento richiesta dall'art. 6;
- non sono qui dimostrati commissioning, accessibilità pubblica e conformità/collocazione completa rispetto alla TEN-T core;
- quindi Monfalcone **non deve essere conteggiata automaticamente come copertura AFIR**.

Stato di integrazione: `VERIFIED_NEW_FACT / CONTEXT`; il ruolo modellistico resta una decisione successiva.

## USER_DECISIONS_INTEGRATED

### UDI-01 — BESS opzionale

Con DEC-0067 l'utente ha deciso che il BESS resta **opzionale** perché irrilevante ai fini della pianificazione territoriale del MODEL_v2.

Effetto operativo:
- non è requisito del nucleo minimo;
- non genera hard filter;
- non genera score;
- non condiziona la configurazione dei cinque Hub;
- può essere previsto successivamente nella progettazione dei singoli Hub.

### UDI-02 — elettrolizzatore obbligatorio, territorialmente neutro

Con DEC-0068 l'utente ha deciso che ogni Hub deve integrare un **elettrolizzatore in sito**.

Effetto operativo nel MODEL_v2:
- è requisito funzionale del nucleo minimo;
- non genera hard filter territoriali;
- non genera score;
- non modifica DQ-01 o l'universo candidato;
- non condiziona la configurazione dei cinque Hub;
- potenza, layout, sicurezza e connessione elettrica necessaria restano post-model/progettuali.

### UDI-03 — AFIR/TEN-T come vincolo della configurazione

DEC-0069, raffinata da DEC-0072, stabilisce che:
- la distanza dalla TEN-T non entra nello score individuale;
- la soglia H2 di 10 km stradali dalla TEN-T exit serve solo a stabilire se una localizzazione può essere conteggiata ai fini della copertura AFIR;
- la conformità AFIR opera come vincolo della cinquina complessiva, inclusa copertura TEN-T core e altri requisiti applicabili;
- il criterio site-level sostitutivo è **flussi veicolari intercettabili**;
- la presenza di infrastrutture H2 esistenti/programmate resta un criterio positivo separato;
- Monfalcone Lisert resta un'opportunità di integrazione/potenziamento, senza assumerne automaticamente conformità AFIR o appartenenza alla cinquina.

Formula raw e normalizzazione del criterio flussi sono chiuse con DEC-0074 e DEC-0077; LIGHT/HEAVY restano separati secondo le decisioni successive.

### UDI-04 — architettura single-objective della cinquina

DEC-0070 è raffinata da DEC-0086.

Architettura ACCEPTED:
- nessuna seconda fase ordinaria di eliminazione site-level dopo la costruzione dell'universo candidato;
- importanza di ogni criterio su scala intera **1–5**, con valori concreti attualmente sospesi;
- per ogni criterio site-level `j`, valore di cinquina `Z_j(H)=(1/5)Σ_{i∈H} z_ij`;
- la copertura territoriale è un criterio configuration-level distinto `Z_COV(H)`;
- tutti i criteri entrano una sola volta nella ponderazione finale;
- funzione obiettivo unica: `Q(H)=[Σ_j r_j Z_j(H)+r_COV Z_COV(H)]/[Σ_j r_j+r_COV]`;
- nessun secondo obiettivo autonomo e nessun fronte di Pareto;
- confronto delle cinquine solo dopo verifica dei vincoli di configurazione applicabili.

Restano pendenti la formula raw/normalizzazione della copertura territoriale e i valori concreti di importanza 1–5.

## METHODOLOGY_PENDING_DECISION

### MPD-04 — dettagli ancora aperti dello scoring

DEC-0070, raffinata da DEC-0086, definisce l'architettura generale dello scoring.

Per i criteri numerici site-level attualmente ammessi, formule raw e normalizzazioni sono state chiuse dalle decisioni successive. Restano da definire:
- formula raw del criterio di copertura territoriale della cinquina;
- normalizzazione di `Z_COV(H)`;
- valori concreti di importanza 1–5, attualmente sospesi;
- eventuali regole generali di gestione missing/outlier se emergeranno casi non già disciplinati dai singoli criteri.

Non è imposto automaticamente il min-max per tutti gli indicatori.

### MPD-05 — indicatori specifici

Indicatori ancora da formalizzare in DQ-02/DQ-03:
- **domanda/prossimità logistica-industriale** — baseline dati ACCEPTED con DEC-0079: `LOGISTICS_FVG_v02.gpkg / LOGISTICS_FVG_POINTS`, 26 `SITE_ID` POINT EPSG:32632. Con DEC-0080, per ogni candidato si prendono le due distanze minori `d(1)` e `d(2)`, si calcola `D=(d(1)+d(2))/2`, poi `D_max=max(D)` sull'intero universo candidati e `S_LOG=1-D/D_max`; nessuna soglia, bonus o peso per tipologia di polo; `SITE_ID 25 — ZIMA` mantiene `NEEDS_HUMAN_CHECK`;
- **flussi veicolari intercettabili** — semantica ACCEPTED con DEC-0072, raggio baseline **5 km dal bordo del poligono** con DEC-0073 e formula raw chiusa con DEC-0074: `f(d)=1-d/5`, `V=q*f(d)`, valore candidato = massimo contributo tra gli archi entro 5 km, separatamente Light/Heavy; se non esistono archi utili entro 5 km il valore raw è 0. DEC-0075 fissa `heavy_vehicles_day_2030` come baseline HEAVY dello score e il 2019 come benchmark/sensitivity; DEC-0076 approva `DIRTY_EDGE_FLOWS_v01.csv` come baseline operativa LIGHT del MODEL_v2, con caveat DEMONSTRATOR / NON CANONICAL rispetto alla Tesi; DEC-0077 normalizza il flusso di ciascun edge come `q/q_max` sulla rispettiva rete completa LIGHT o HEAVY 2030 e applica poi il decadimento `1-d/5`, producendo direttamente uno score candidato in [0,1] senza seconda normalizzazione;
- **PGRA / alluvioni** — ACCEPTED con DEC-0082 + DEC-0084 come criterio numerico separato. Scala: fuori P1–P3B = 1,00; P1/P1_ST/P1_SM = 0,75; P2 = 0,50; P3A = 0,25; P3B = 0,00. Score candidato = media pesata per superficie delle classi intersecate; sulle sovrapposizioni prevale la classe peggiore per evitare doppio conteggio. `AA` (Zona di Attenzione) e `F` (Area fluviale) restano informazioni/flag separati e non entrano nella graduatoria;
- **PAI / frane** — SUSPENDED con DEC-0083: non entra per ora nello scoring del MODEL_v2 per assenza di baseline vettoriale unica, completa e corrente con lineage normativo sufficiente; CATFRANE/UTIL_TER/IFFI restano SUPPORT_ONLY / CONTEXT e non sostituiscono il PAI;
- **prossimità alla cabina primaria** — ACCEPTED con DEC-0078: `d_i` = distanza geometrica minima tra poligono candidato e cabina primaria più vicina nella baseline elettrica approvata DEC-0053; `d_max = max_i(d_i)` sull'intero universo candidati; `S_i_GRID = 1 - d_i/d_max`; nessuna soglia artificiale; prossimità = proxy di costo/complessità potenziale, non capacità disponibile o fattibilità reale;
- **prossimità a infrastrutture H2 core verificate** — ACCEPTED con DEC-0085. Baseline fattuale: `H2_FVG_INFRASTRUCTURE_INVENTORY_v01.csv`. Target spaziali iniziali: Trieste, Monfalcone/Lisert, Porpetto e ABS. Per ogni candidato `d_H2 = min(distanza ai target point-ready)`; `d_max_H2 = max(d_H2)` sull'universo candidati; `S_H2 = 1 - d_H2/d_max_H2`. Nessuna soglia, nessun peso per status, nessun bonus per numero di siti. SOLHX resta nella baseline ma fuori dalle distanze finché non è localizzato puntualmente; testbed e `ANNOUNCED_UNVERIFIED` restano fuori dallo score core.

Ogni indicatore dovrà specificare domanda decisionale, fonte, geometria, unità, formula raw, direzione, missing, ruolo HARD/SOFT/FLAG e limiti.

### UDI-05 — macro-aree e top-k solo come fallback computazionale

Con DEC-0071 l'utente ha stabilito che la metodologia ordinaria **non** usa:
- cinque macro-aree;
- vincolo di un Hub per macro-area;
- preselezione top-10/top-5.

Questi strumenti possono essere introdotti soltanto come **fallback computazionale** se la selezione delle cinquine sull'universo completo risultasse eccessivamente onerosa.

In tal caso devono essere:
- esplicitamente motivati;
- attivati solo dopo evidenza del problema computazionale;
- sottoposti a confronto/sensitivity per valutare il rischio di perdere la soluzione migliore.

I conteggi 10^5 = 100.000 e 5^5 = 3.125 restano esempi condizionati a tale fallback e non requisiti del MODEL_v2.

### MPD-08 — quantificazione del ruolo di Monfalcone Lisert

DEC-0069 ha stabilito la semantica: Monfalcone Lisert è un'opportunità di integrazione/potenziamento e la presenza di infrastruttura H2 è un criterio positivo separato.

Restano da decidere:
- formula raw del criterio;
- normalizzazione e peso;
- trattamento della capacità disponibile/programmata;
- modalità con cui un eventuale potenziamento può contribuire alla conformità AFIR della configurazione;
- verifiche tecniche necessarie prima di conteggiare Monfalcone ai fini AFIR.

## DO_NOT_USE_SUPERSEDED

- `ROADMAP_METODOLOGICA_v1` come roadmap operativa: è DEPRECATED/HISTORICAL_BASELINE.
- Formulazione secondo cui l'uso operativo di OSM/Gamma/OD Light deve ancora essere validato ex novo: superseded da DEC-0054/DEC-0055.
- Formulazione secondo cui il crosswalk TEN-T deve ancora essere completato/validato: superseded da DEC-0035/DEC-0036.
- Obbligo di verificare integralmente la vigenza urbanistica di tutti i Comuni prima della generazione candidati: superseded da best-available current-first con source tier/currentness flag.
- Soglia storica di circa 5.000 m²: solo benchmark storico; non usare operativamente.
- Formula generica 'superficie minima ancora da definire': superseded da HARD 8.000 m² DQ-01.
- Due diligence di proprietà/disponibilità commerciale come gate del core: DEFER_POST_MODEL.
- Verifica urbanistica definitiva del finalista come gate del core: DEFER_POST_MODEL.
- Accesso locale definitivo, sagome/manovre/restrizioni Heavy del singolo sito come gate del core: DEFER_POST_MODEL.
- MW disponibili, punto/costo reale di connessione come gate del core: DEFER_POST_MODEL.
- PAI pointwise / autorizzazioni/VINCA/PPR puntuali come condizioni necessarie per chiudere MODEL_v2: DEFER_POST_MODEL salvo futura regola hard esplicitamente approvata.
- Penalizzazione dei prati stabili come già decisa: non è pre-approvata dopo la re-baseline.

## VINCOLI DI USO DEL PACCHETTO

1. Non trasformare `METHODOLOGY_PENDING_DECISION` in default impliciti.
2. Non elevare `VERIFIED_NEW_FACT` a criterio o vincolo senza la DQ pertinente.
3. Non usare contenuti `DO_NOT_USE_SUPERSEDED` come istruzioni operative.
4. Se una fonte esterna può essere cambiata nel tempo, re-verificarla al momento dell'implementazione.
5. In caso di conflitto prevalgono PROJECT_SOURCE_OF_TRUTH, PROJECT_CONTROL_REGISTER e baseline FROZEN/ACCEPTED correnti.
6. Questo file può essere usato per costruire un prompt Claude solo **dopo review della Chat 0.2**.
