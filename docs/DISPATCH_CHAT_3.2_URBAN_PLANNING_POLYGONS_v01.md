# DISPATCH — Chat 3.2 — Urbanistica, poligoni sorgente e disponibilità

**Fase:** 3 — Inventario e validazione dei dati
**Data:** 2026-09-18
**Stato mandato:** AUTHORIZED
**Regia:** Chat Madre 5 HUB

## 1. Obiettivo

Risolvere il blocco P1 emerso dalla Chat 3.1: identificare e validare una base urbanistica utilizzabile e riproducibile per la futura costruzione dei poligoni candidati, senza costruire ancora `CANDIDATES_RAW`.

La chat deve chiarire quali geometrie urbanistiche rappresentano realmente la situazione vigente e con quale livello di copertura, aggiornamento, precisione e lineage.
## 2. Baseline vincolanti e input

READ ONLY:
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md` — FROZEN;
- `docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md` — REVIEW/PASS tecnico Chat 3.1;
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER.

Issue prioritarie:
- `ISS-0003` — Mosaicatura PRG 2018 non dimostrata come urbanistica vigente 2026;
- `ISS-0009` — proprietà/disponibilità non coperta region-wide.

Fonti storiche Claude/QGIS restano HISTORICAL / NON_AUTHORITATIVE.
## 3. Domande da risolvere

1. Esiste una fonte regionale aggiornata e region-wide dei PRGC/zonizzazioni comunali vigenti?
2. Se non esiste, è possibile costruire una procedura riproducibile per recuperare e versionare i PRGC vigenti dei Comuni FVG?
3. Quali layer/zone possono essere usati come **fonti geometriche** senza confondere la fonte con una futura regola di ammissibilità?
4. Quali identificativi, date di validità, varianti, CRS, scale/accuratezze e attributi consentono lineage e aggiornamento?
5. Quali differenze reali esistono fra WFS CER basati sulla Mosaicatura PRG 2018 e urbanistica vigente?
6. Quali fonti ufficiali esistono per proprietà/disponibilità delle aree, e con quale copertura?

La chat non decide autonomamente se proprietà/disponibilità debba essere requisito di generazione, ammissibilità o verifica puntuale: questa resta `Q-METH-3.1-C`.
## 4. Attività obbligatorie

- verificare fonti Regione FVG, IRDAT, strumenti regionali di consultazione PRGC e sistemi comunali ufficiali;
- determinare se esiste una mosaicatura più recente del 2018 e documentarne identità/versione;
- costruire una tabella di copertura dei Comuni FVG: fonte disponibile, data/variante, formato, accesso, qualità, stato;
- effettuare controlli campionari su più Comuni e Province, includendo casi con varianti recenti;
- confrontare in modo documentato il WFS CER 2018 con fonti urbanistiche correnti su un campione sufficiente a valutarne l'affidabilità temporale;
- verificare semantica e continuità delle zone produttive/commerciali, senza fissare ancora le categorie ammissibili;
- censire fonti di proprietà/disponibilità (Regione, Comuni, consorzi, patrimoni pubblici), distinguendo disponibilità fisica, proprietà e destinazione urbanistica;
- registrare dataset/fonti e gap nel DATA_REGISTRY/ISSUES con stati prudenti;
- materializzare solo dati realmente utili alla validazione, in OneDrive `5_HUB_FVG`, con metadati e hash quando appropriato.
## 5. Divieti

NON:
- costruire o numerare candidati;
- dissolvere/splittare aree per produrre l'universo candidato;
- fissare superficie minima;
- decidere categorie urbanistiche definitive ammissibili;
- assumere che zona D/H = sito ammissibile;
- usare catastale/proprietà come prova automatica di disponibilità;
- modificare F1/F2 FROZEN;
- accettare la Mosaicatura 2018 solo perché pubblicata su WFS corrente.

## 6. Output atteso

`docs/FASE_3_URBAN_PLANNING_VALIDATION_REVIEW_v01.md`

Deve contenere:
- fonti regionali/comunali verificate;
- copertura territoriale e temporale;
- confronto Mosaicatura 2018 vs urbanistica vigente;
- proposta tecnica di fonte/procedura P1 con alternative e limiti;
- schema minimo di lineage necessario alla futura Fase 4;
- stato di `ISS-0003` e `ISS-0009`;
- eventuali nuove issue;
- elementi da sottoporre alla Chat Madre, senza approvarli.
## 7. Quality gate

PASS tecnico-operativo solo se:
- è dimostrato se esiste o non esiste una fonte region-wide vigente utilizzabile;
- se non esiste, è definita una procedura realistica e riproducibile di acquisizione/ricostruzione;
- la vigenza e la data delle fonti sono documentate, non inferite;
- il WFS CER 2018 è classificato correttamente rispetto alla fonte vigente;
- non è stata introdotta alcuna categoria ammissibile o soglia di Fase 4;
- i gap residui sono espliciti e assegnabili;
- registri, file e commit sono tracciabili;
- SESSION CLOSE e handoff sono completi.

La chat può proporre `ISS-0003` RESOLVED solo se esiste evidenza sufficiente; la Chat Madre verifica prima di accettarlo.
