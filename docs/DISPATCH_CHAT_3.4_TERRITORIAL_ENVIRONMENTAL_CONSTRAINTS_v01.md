# DISPATCH — Chat 3.4 — Vincoli territoriali, ambientali e paesaggistici

**Fase:** 3 — Inventario e validazione dei dati  
**Data:** 2026-09-19  
**Stato mandato:** AUTHORIZED  
**Regia metodologica:** Chat Madre 5 HUB

## 1. Obiettivo

Validare e materializzare le fonti correnti necessarie a descrivere i principali vincoli e fattori territoriali, idraulici, geologici, ambientali e paesaggistici rilevanti per il futuro modello di localizzazione dei 5 Hub Energetici Green in Friuli Venezia Giulia.

La Chat 3.4 deve stabilire, per ciascun tematismo:
- quale sia la fonte istituzionale corrente;
- quale dataset/geometria sia realmente disponibile;
- data, versione, copertura, CRS, scala/accuratezza e licenza quando disponibile;
- semantica delle classi;
- eventuale valore normativo o prescrittivo documentabile;
- limiti d’uso;
- modalità riproducibile di acquisizione;
- stato di validazione.

La chat NON deve decidere autonomamente quali classi comportino esclusione di un futuro candidato.

## 2. Baseline vincolanti e governance

Prima di operare leggere integralmente:
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md` — FROZEN;
- `docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md`;
- `docs/ROADMAP_METODOLOGICA_v1.md`;
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER, con particolare attenzione a DATA_REGISTRY e a `ISS-0006`, `ISS-0008`.

Non riaprire Fase 1 o Fase 2.

Il materiale Claude/QGIS può essere utilizzato solo come baseline storica, pista per recuperare fonti o benchmark. Non costituisce fonte autorevole corrente.

## 3. Tematismi obbligatori

### 3.1 Rischio e pericolosità idraulica — PGRA

Priorità massima.

Verificare l’aggiornamento del Piano di Gestione del Rischio di Alluvioni del Distretto delle Alpi Orientali coerente con:
- aggiornamento mappe adottato con Delibera n. 12 del 18 dicembre 2025;
- regime di salvaguardia efficace dal 22 gennaio 2026, come già registrato in Fase 3.

Obiettivi:
- individuare la fonte ufficiale corrente Autorità di Bacino / SIGMA;
- acquisire, se tecnicamente disponibile, i layer vettoriali correnti relativi a pericolosità e/o rischio pertinenti al FVG;
- identificare legenda, classi, geometrie, data, versione, CRS e metadati;
- conservare package sorgente, hash e procedura di acquisizione;
- confrontare soltanto a fini diagnostici eventuali copie storiche già presenti;
- determinare se `ISS-0006` può essere proposta come RESOLVED.

Non sostituire il PGRA vigente con layer regionali storici o con `CAR_GEO:V_AREA_INONDATA`.

### 3.2 Frane e pericolosità geologica

Validare il layer regionale `IRDAT:CATFRANE_PERICOLOSITA` e le fonti ufficiali correlate.

Chiarire:
- cosa rappresentano realmente le circa 830 feature osservate in Chat 3.1;
- rapporto fra layer di pericolosità e Catasto Frane complessivo;
- classi e semantica;
- aggiornamento;
- copertura;
- ruolo normativo/informativo documentato.

Non assumere che “presenza di frana” equivalga automaticamente a esclusione.

### 3.3 Natura 2000 e aree protette

Validare almeno:
- ZSC/SIC, verificando la nomenclatura corrente;
- ZPS;
- biotopi;
- riserve naturali;
- parchi;
- eventuali altri tematismi regionali di tutela realmente pertinenti.

Per ogni famiglia:
- identificare fonte ufficiale corrente;
- verificare che layer e denominazioni siano allineati allo stato legale vigente;
- documentare data/versione;
- materializzare le geometrie quando appropriato;
- distinguere tutela normativa da semplice informazione territoriale.

### 3.4 Piano Paesaggistico Regionale — PPR

Priorità massima.

Riferimento di base già verificato:
- PPR FVG approvato nel 2018;
- Variante 2 approvata il 12 dicembre 2025;
- efficacia dal 18 dicembre 2025.

Obiettivi:
- individuare il riferimento ufficiale aggiornato del WebGIS PPR;
- identificare servizi/download/API utilizzabili;
- costruire una procedura GIS riproducibile di estrazione;
- identificare i layer prescrittivi o comunque rilevanti alla futura localizzazione;
- documentare versione, data, CRS, attributi, metadati e hash;
- non assumere copie EagleFVG, IRDAT legacy o baseline Claude come equivalenti alla cartografia PPR vigente senza prova;
- determinare se `ISS-0008` può essere proposta come RESOLVED.

## 4. Tematismi complementari

Valutare, senza espandere inutilmente il perimetro:
- `CAR_GEO:V_AREA_INONDATA` come eventuale informazione complementare al PGRA;
- prati stabili e altri tematismi ambientali regionali già emersi nell’inventario;
- altri vincoli territoriali soltanto se una fonte ufficiale dimostra rilevanza concreta per la localizzazione di impianti comparabili agli Hub.

Ogni nuovo tematismo deve essere motivato. Non creare un catalogo enciclopedico di layer solo perché disponibili.

## 5. Classificazione metodologica da PROPORRE, non approvare

Per ogni tematismo costruire una matrice che proponga una delle seguenti funzioni future:
- `POTENTIAL_EXCLUSION` — possibile vincolo ostativo da sottoporre a decisione metodologica;
- `ADMISSIBILITY_CHECK` — elemento da verificare prima del ranking;
- `POTENTIAL_INDICATOR` — eventuale fattore di merito/penalità da valutare in Fase 6;
- `CONTEXT_ONLY` — informazione di contesto;
- `TO_DECIDE` — ruolo non determinabile senza decisione della Chat Madre/utente.

Per ogni proposta citare il fondamento normativo o tecnico.

La Chat 3.4 NON può trasformare autonomamente una classe PGRA, PPR, frana, Natura 2000 o altra tutela in regola di esclusione.

Qualsiasi scelta sostanziale va formulata come questione metodologica chiara, ad esempio:
`Q-METH-3.4-A — trattamento operativo delle classi PGRA`.

## 6. Regole sulle fonti

Ordine di preferenza:
1. norma e atto ufficiale vigente;
2. ente titolare del piano/dataset;
3. servizio GIS/download ufficiale corrente;
4. metadato istituzionale;
5. fonti secondarie solo come supporto.

Per ogni dataset materializzato registrare almeno:
- nome;
- ente;
- URL/endpoint;
- data di acquisizione;
- versione/data del dato;
- formato;
- CRS;
- feature count quando pertinente;
- licenza/condizioni d’uso se disponibili;
- SHA-256;
- percorso OneDrive;
- uso previsto;
- limite noto.

## 7. Architettura di salvataggio

Codice, review, configurazioni e file leggeri:
`C:\dev\5-hub`

Dati sorgente/materializzazioni:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_4\`

Output intermedi:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\05_intermediate_outputs\F3_CHAT_3_4\`

Lavorare sul branch:
`chat-3.4-territorial-constraints`

Non versionare in Git dataset pesanti.

## 8. Output attesi

Minimo:
- `docs/FASE_3_TERRITORIAL_ENVIRONMENTAL_VALIDATION_REVIEW_v01.md`;
- `docs/FASE_3_TERRITORIAL_CONSTRAINT_ROLE_MATRIX_v01.csv`;
- manifest/evidence package versionato e hashato;
- eventuali script riproducibili di download, estrazione e QA;
- aggiornamenti proposti a DATA_REGISTRY e ISSUES;
- eventuali questioni metodologiche numerate e motivate;
- `docs/HANDOFF_CHAT_3.4_TERRITORIAL_CONSTRAINTS_v01.md`.

Se l’acquisizione di un layer ufficiale non è tecnicamente possibile:
- non improvvisare una sostituzione;
- documentare fonte, tentativi, limite e alternativa candidata;
- lasciare il dataset in stato GAP / TO_VALIDATE.

## 9. Divieti

NON:
- costruire `CANDIDATES_RAW`;
- applicare overlay ai futuri candidati inesistenti;
- fissare buffer o soglie numeriche arbitrarie;
- decidere autonomamente classi di esclusione;
- assegnare punteggi;
- definire pesi;
- confondere “fonte ufficiale” con “dato validato per il modello”;
- usare una copia storica come corrente solo perché più facile da scaricare;
- modificare baseline FROZEN.

## 10. Quality gate

La Chat 3.4 può dichiarare PASS tecnico-operativo solo se:

- PGRA corrente: fonte e stato normativo verificati; dataset corrente materializzato oppure impossibilità documentata in modo riproducibile;
- frane/pericolosità: semantica, fonte, aggiornamento e copertura chiariti;
- Natura 2000/aree protette: nomenclatura e stato legale corrente verificati per i layer proposti;
- PPR vigente: riferimento ufficiale e procedura di estrazione GIS riproducibile validati, oppure gap tecnico precisamente documentato;
- ogni dataset materializzato ha hash e lineage;
- la matrice dei ruoli distingue fonte/dato da decisione metodologica;
- eventuali questioni sostanziali sono riportate alla Chat Madre e non auto-approvate;
- DATA_REGISTRY / ISSUES sono aggiornati tecnicamente e riletti;
- nessun artifact FROZEN è stato modificato;
- Git contiene solo codice/documentazione leggera pertinente;
- SESSION CLOSE e handoff sono completi.

Il PASS della Chat 3.4 è tecnico-operativo e richiede review indipendente della Chat Madre.

## 11. Criterio di completamento

Il risultato finale della Chat 3.4 deve permettere alla Chat Madre di rispondere, per ciascun tematismo:

> Qual è il dato corrente che possiamo realmente usare, da dove proviene, che cosa significa, con quale affidabilità, e quale decisione metodologica resta eventualmente da prendere prima di usarlo per escludere o valutare un candidato?

La Fase 3 resta IN CORSO e la Fase 4 non viene aperta da questa chat.
