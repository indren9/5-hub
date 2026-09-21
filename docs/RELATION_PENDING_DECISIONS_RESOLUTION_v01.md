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

**Stato:** ACCEPTED

Decisione:
- una volta definito l'universo candidato non è prevista una seconda fase ordinaria di eliminazione site-level;
- ogni criterio riceve importanza intera 1–5;
- i valori di importanza vengono convertiti in pesi percentuali normalizzati;
- gli indicatori vengono normalizzati prima dell'aggregazione;
- score candidato = media pesata dei criteri normalizzati;
- score cinquina = media aritmetica degli score dei cinque candidati;
- la cinquina deve comunque rispettare i vincoli di configurazione approvati.

Formule:
- `w_j = r_j / Σ r_j`;
- `S_i = Σ_j (w_j × z_ij)`;
- `Q = (1/5) × Σ_i S_i`.

Restano pendenti valori concreti 1–5, formule raw e normalizzazioni criterio-specifiche.

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

## Decisioni ancora pendenti

Restano da discutere separatamente:
- criteri e formule raw;
- normalizzazioni criterio-specifiche;
- valori concreti di importanza 1–5;
- distanza minima 10 km tra Hub;
- quantificazione del ruolo di Monfalcone Lisert.
