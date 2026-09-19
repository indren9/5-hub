# DISPATCH — Chat 3.8 — Acquisizione e validazione urbanistica corrente FVG

**Fase:** 3 — Inventario e validazione dei dati  
**Data:** 2026-09-19  
**Stato mandato:** AUTHORIZED  
**Regia:** Chat Madre 5 HUB

## 1. Obiettivo

Eseguire operativamente la procedura urbanistica current-first / ibrida già approvata con DEC-0032, Comune per Comune, per costruire una base di fonti PRGC correnti, tracciabili e sufficienti alla futura Fase 4.

La chat deve ridurre e, se possibile, chiudere ISS-0010: la vigenza dei PRGC comunali e la disponibilità di geometrie correnti non sono ancora verificate in modo uniforme sul territorio regionale.

La chat NON deve costruire candidati Hub, scegliere categorie urbanistiche ammissibili o introdurre soglie geometriche.

## 2. Baseline vincolanti — READ ONLY

- docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md — FROZEN;
- docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md — FROZEN;
- docs/FASE_3_DATA_INVENTORY_REVIEW_v01.md;
- docs/FASE_3_URBAN_PLANNING_VALIDATION_REVIEW_v01.md;
- docs/FASE_3_URBAN_PLANNING_MUNICIPAL_COVERAGE_v01.csv;
- docs/FASE_3_URBAN_PLANNING_CURRENT_SAMPLE_v01.csv;
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER, in particolare DEC-0032 e ISS-0010.

Decisione metodologica vincolante:

**DEC-0032 — procedura P1 current-first / ibrida.**

Per ogni Comune la vigenza urbanistica deve derivare dal PRGC effettivamente vigente. EagleFVG/Regione può fornire la geometria solo quando l'allineamento alla versione vigente è verificato; altrimenti si usa la fonte ufficiale comunale con lineage esplicito. I casi non verificabili restano TO_VERIFY.

I WFS CER D/H basati sulla Mosaicatura PRG 2018 sono HISTORICAL / SUPPORT ONLY e non possono sostituire la fonte corrente.

## 3. Domanda operativa da risolvere

Per ciascun Comune FVG:

1. qual è il PRGC effettivamente vigente;
2. qual è l'ultima variante efficace/esecutiva pertinente;
3. quale fonte ufficiale dimostra la vigenza;
4. esiste una geometria vettoriale ufficiale allineata a quella versione;
5. se esiste, può essere acquisita e versionata in modo riproducibile;
6. se non esiste, qual è esattamente il gap residuo.

La chat deve distinguere sempre:
- accesso tecnico a un WebGIS;
- documento/atto vigente;
- geometria corrente verificata.

Nessuna delle tre condizioni implica automaticamente le altre.

## 4. Procedura obbligatoria

Partire dalla tabella dei 215 Comuni già prodotta dalla Chat 3.2 e aggiornarla, senza ricominciare da zero.

Gerarchia di ricerca:
1. fonte/atto ufficiale comunale che dimostra PRGC e variante vigente;
2. servizio vettoriale ufficiale comunale o EagleFVG/Regione;
3. elaborati urbanistici ufficiali comunali;
4. altre fonti istituzionali solo come supporto.

Per ogni Comune registrare almeno:
- codice ISTAT e denominazione;
- PRGC/piano vigente;
- numero o identificativo della variante corrente, se applicabile;
- stato procedurale: adottata / approvata / efficace-esecutiva;
- atto e data;
- eventuale pubblicazione BUR;
- URL istituzionale;
- data di accesso;
- fonte della geometria;
- formato e CRS;
- identificativo del layer/servizio;
- stato di allineamento geometria ↔ piano vigente;
- currentness_status;
- evidenza utilizzata;
- note e gap residui.

Quando possibile, automatizzare ricerca, download, checksum e QA; i passaggi manuali devono restare tracciati.

## 5. Regole per le geometrie

Se esiste una geometria vettoriale ufficiale e l'allineamento al PRGC vigente è verificato:
- acquisirla;
- conservarne il formato originale quando pratico;
- registrare hash, CRS, data e fonte;
- preservare codici e descrizioni urbanistiche native.

Se la geometria è accessibile ma non è dimostrato che corrisponda al piano vigente:
- NON promuoverla a corrente;
- classificarla come VECTOR_AVAILABLE_CURRENTNESS_NOT_VERIFIED o equivalente.

Se esistono solo PDF/tavole ufficiali:
- documentare la fonte corrente;
- classificare il gap geometrico;
- NON digitalizzare automaticamente come unica fonte autorevole.

Non creare in questa chat una mosaicatura definitiva, non dissolvere zone e non filtrare categorie per produrre candidati.

## 6. Stati minimi richiesti

Ogni Comune deve terminare in uno stato esplicito, ad esempio:
- CURRENT_VECTOR_VERIFIED;
- CURRENT_PLAN_VERIFIED_NO_VECTOR;
- CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE;
- TO_VERIFY.

La nomenclatura finale può essere raffinata tecnicamente, ma non deve nascondere i casi incompleti.

## 7. Output obbligatori

Documentazione leggera in C:\dev\5-hub:
- docs/FASE_3_CURRENT_URBAN_PLANNING_VALIDATION_REVIEW_v01.md;
- docs/FASE_3_CURRENT_URBAN_PLANNING_COVERAGE_v01.csv;
- docs/FASE_3_CURRENT_URBAN_PLANNING_EVIDENCE_v01.json;
- docs/HANDOFF_CHAT_3.8_CURRENT_URBAN_PLANNING_v01.md;
- script o moduli riproducibili necessari all'acquisizione/QA.

Storage tecnico pesante:
5_HUB_FVG\02_external_sources\F3_CHAT_3_8\

Gli artifact pesanti devono includere manifest con fonte, URL, data, byte e SHA-256 quando applicabile.

Branch dedicato:
chat-3.8-current-urban-planning.

## 8. Divieti

NON:
- costruire CANDIDATES_RAW;
- assegnare candidate_id;
- scegliere quali zone urbanistiche siano ammissibili;
- fissare una superficie minima;
- applicare merge/split/canonicalizzazione da Fase 4;
- sostituire dati mancanti con CER 2018 senza dichiararlo storico;
- assumere che PUBLIC_CONFIG_DETECTED significhi PRGC vigente verificato;
- modificare Fase 1 o Fase 2 FROZEN;
- chiudere autonomamente ISS-0010.

## 9. Quality gate

Il PASS tecnico-operativo richiede almeno:

- tutti i Comuni FVG presenti nella coverage table;
- per ogni Comune uno stato finale esplicito e un lineage verificabile;
- nessun uso silenzioso della Mosaicatura PRG 2018 come fonte corrente;
- le geometrie dichiarate correnti collegate a evidenza di vigenza;
- i casi senza geometria corrente identificati puntualmente;
- controlli di integrità e CRS sulle geometrie acquisite;
- manifest/hash degli artifact materializzati;
- nessuna categoria urbanistica trasformata in criterio di ammissibilità;
- F1/F2 FROZEN invariati;
- DATA_REGISTRY / ISSUES aggiornati con stati prudenti;
- Git e SESSION CLOSE / handoff completi.

La chat deve produrre anche un giudizio separato di PHASE_4_READINESS:
- READY solo se i gap residui non impediscono una costruzione region-wide autorevole dei poligoni sorgente;
- NOT_READY se uno o più Comuni restano senza una base sufficiente e il gap può alterare l'universo candidati.

ISS-0010 può essere soltanto proposta come RESOLVED. La decisione finale spetta alla Chat Madre dopo review indipendente.

## 10. Criterio di successo

Il risultato deve permettere alla Chat Madre di rispondere senza ambiguità:

> Abbiamo, per l'intero FVG, fonti urbanistiche correnti e sufficientemente tracciate da poter iniziare la Fase 4 senza usare geometrie storiche come se fossero vigenti?

Se la risposta è no, la Chat 3.8 deve dire esattamente quali Comuni, quali fonti e quale tipo di dato mancano, senza colmare il gap con assunzioni.
