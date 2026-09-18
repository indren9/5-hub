# DISPATCH — Chat 3.1 — Inventario master e gap analysis dei dati

**Fase:** 3 — Inventario e validazione dei dati
**Data:** 2026-09-18
**Stato mandato:** AUTHORIZED
**Regia:** Chat Madre 5 HUB

## 1. Obiettivo

Costruire il primo inventario completo e verificabile dei dati disponibili o candidati per il modello dei 5 Hub Energetici Green FVG e identificare con precisione ciò che manca.

La Chat 3.1 deve rispondere a quattro domande:
1. quali dataset esistono realmente;
2. dove sono e da chi provengono;
3. quali caratteristiche/limiti sono già verificabili;
4. quali dataset richiedono validazione specialistica o nuova acquisizione.

La Chat 3.1 **non approva automaticamente dataset per il modello** e non costruisce ancora l’universo dei candidati.
## 2. Baseline vincolante

Sono READ ONLY e non devono essere riaperte:
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md` — FROZEN.

Dalla Fase 2 discendono in particolare:
- candidato = poligono fisicamente localizzabile;
- punti/accessi/road anchor = geometrie ausiliarie;
- lineage obbligatoria;
- nessuna tolleranza geometrica arbitraria;
- fonti dei poligoni, rete stradale, CRS e tolleranze quantitative sono ancora da validare.

## 3. Perimetro della Chat 3.1

La chat deve inventariare almeno le categorie previste dalla roadmap:
- rete stradale;
- TEN-T / rete europea dei trasporti;
- nodi urbani;
- aree produttive, industriali, artigianali e commerciali;
- porti, interporti e terminali logistici;
- rete ferroviaria se rilevante;
- popolazione;
- pendolarismo;
- turismo;
- aree interne;
- vincoli ambientali;
- frane;
- rischio idraulico;
- vincoli urbanistici;
- rete elettrica, cabine, linee ed eventuale capacità disponibile;
- superfici disponibili e altre fonti utili alla futura costruzione dei poligoni.
## 4. Fonti da considerare

Ordine di priorità:
1. fonti ufficiali e primarie aggiornate;
2. dataset pubblici istituzionali con metadati verificabili;
3. dati già presenti nel progetto, da riconciliare con la fonte originaria;
4. baseline storiche Claude/QGIS solo come pista, benchmark o indice di fonti.

Materiale storico utile ma NON AUTHORITATIVE:
- `5_HUB_FVG\00_baseline\21624001 FVG Energia Spa – Studio mobilità sostenibile.zip`;
- `5_HUB_FVG\00_baseline\claude_qgis\QGZ_Beltrame_20260918\QGZ_Beltrame.zip`;
- `docs/BASELINE_QGIS_BELTRAME_REVIEW_v01.md`.

La Chat 3.1 può leggere in sola lettura il materiale preesistente locale utile alla ricognizione, incluso `C:\Tesi\LOGISTICS_FVG_SOURCE`, ma non deve spostarlo, rinominarlo o dichiararlo autorevole senza verifica.
## 5. Scheda minima per ogni dataset

Per ogni dataset o fonte candidata raccogliere, quando disponibile:
- nome canonico;
- ente/fonte primaria;
- URL o endpoint ufficiale;
- versione/data di aggiornamento;
- licenza/condizioni d’uso;
- copertura territoriale;
- geometria/tipo dato;
- CRS e unità;
- scala, risoluzione o accuratezza nota;
- completezza;
- identificativi sorgente disponibili;
- formato e modalità di accesso/download;
- percorso locale/OneDrive se già acquisito;
- uso previsto nel modello;
- limiti noti;
- stato della verifica;
- evidenza che supporta la verifica.

Non inventare valori mancanti: usare esplicitamente `n.d.` / `da verificare` quando necessario.
## 6. Priorità analitica

Pur inventariando tutte le categorie, dare priorità a ciò che condiziona direttamente le Fasi 4–5:

**P1 — geometrie candidate**
- aree industriali/artigianali;
- aree commerciali;
- strumenti urbanistici o altre superfici territorialmente utilizzabili;
- eventuali dati catastali o di disponibilità, se accessibili e metodologicamente pertinenti.

**P2 — accesso e funzione TEN-T**
- rete stradale routabile;
- TEN-T;
- uscite/svincoli pertinenti;
- dati utili agli accessi light/heavy.

**P3 — vincoli territoriali/fattibilità**
- rischio idraulico e frane;
- vincoli ambientali;
- urbanistica;
- infrastruttura elettrica;
- altri vincoli territoriali derivati dalle baseline FROZEN.

Le priorità servono solo a organizzare il lavoro, non sono pesi del modello.
## 7. Compiti specifici

La Chat 3.1 deve:
1. leggere il DATA_REGISTRY vivo prima di lavorare;
2. evitare duplicazioni di fonti già registrate;
3. ricostruire l’origine ufficiale dei layer interessanti emersi dal QGIS Beltrame, inclusi i WFS regionali;
4. verificare se endpoint, download e metadati sono ancora attuali;
5. distinguere dataset già materializzati da semplici fonti candidate;
6. produrre una gap analysis per ogni categoria minima;
7. proporre quali categorie richiedono chat operative specialistiche successive;
8. segnalare alla Chat Madre qualsiasi scelta metodologica che ecceda l’inventario/validazione dei dati.

Se la verifica di una fonte richiede ricerca web, usare fonti ufficiali/primarie e riportare evidenza e data di accesso.
## 8. Divieti

La Chat 3.1 NON deve:
- costruire `CANDIDATES_RAW_v01`;
- scegliere categorie urbanistiche definitive;
- fissare superficie minima;
- creare ranking o indicatori;
- fissare pesi o normalizzazioni;
- applicare criteri di esclusione ai candidati;
- riaprire Fase 1 o Fase 2;
- copiare automaticamente dati storici Claude/QGIS nel nuovo modello;
- dichiarare un dataset VALIDATO senza evidenza sufficiente;
- modificare artifact FROZEN.

## 9. Output attesi

Artifact di review principale:
`docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md`

Deve contenere almeno:
- inventario per categoria;
- fonti primarie e alternative;
- stato di verifica;
- gap;
- rischi/limiti;
- priorità di acquisizione/validazione;
- proposta di suddivisione delle successive chat 3.x;
- questioni da sottoporre alla Chat Madre/utente.
Il `PROJECT_CONTROL_REGISTER` resta la governance viva. La Chat 3.1 può proporre aggiornamenti al DATA_REGISTRY, ma non deve trasformare questioni metodologiche sostanziali in decisioni implicite.

Eventuali file pesanti scaricati o acquisiti devono essere collocati in `5_HUB_FVG` nella categoria tecnica appropriata, non nel repository Git.

## 10. Quality gate Chat 3.1

PASS operativo solo se:
- tutte le categorie minime della roadmap sono coperte dall’inventario o marcate esplicitamente come gap;
- ogni dataset citato ha una fonte identificabile o è marcato come non verificato;
- per i dati prioritari P1/P2 è chiaro se esiste una fonte ufficiale utilizzabile;
- baseline Claude/QGIS resta separata dalle fonti validate;
- nessuna assunzione viene trasformata in dato;
- nessuna scelta metodologica sostanziale viene congelata;
- artifact e registri necessari sono aggiornati in modo tracciabile;
- Git usa staging esplicito e working tree finale pulito;
- viene prodotto SESSION CLOSE / handoff.

La Chat 3.1 può dichiarare il proprio PASS tecnico-operativo, ma **non può dichiarare FASE 3 CLOSED/FROZEN**.

## 11. Handoff obbligatorio

L’handoff deve riportare:
- numero e nome chat;
- obiettivo;
- lavoro svolto;
- fonti/dataset verificati;
- file creati/modificati e percorsi;
- aggiornamenti DATA_REGISTRY proposti/eseguiti;
- controlli e relativo esito;
- commit Git;
- gap e problemi aperti;
- stato finale;
- proposta del prossimo passo.
