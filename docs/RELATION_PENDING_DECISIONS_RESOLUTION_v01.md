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

## Decisioni ancora pendenti

Restano da discutere separatamente:
- criteri e formule raw;
- normalizzazioni criterio-specifiche;
- valori concreti di importanza 1–5;
- cinque macro-aree;
- uno-per-macro-area;
- top-k;
- distanza minima 10 km tra Hub;
- quantificazione del ruolo di Monfalcone Lisert.
