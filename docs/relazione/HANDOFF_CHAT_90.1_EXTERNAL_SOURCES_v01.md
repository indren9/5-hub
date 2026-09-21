# HANDOFF_CHAT_90.1_EXTERNAL_SOURCES_v01

## Identità

- Chat: **90.1 — Fonti esterne e bibliografia**
- Chat madre editoriale: **90.0 — Relazione Builder**
- Regia metodologica: **0.2 — Chat Madre 5 HUB**
- Data chiusura: **2026-09-21**
- Branch: `chat-90.1-external-sources`
- Stato finale proposto: **REVIEW**
- Technical quality gate: **PASS_WITH_DOCUMENTED_GAPS**

## Obiettivo

Costruire e normalizzare il registro delle fonti esterne effettivamente utilizzabili nella relazione, rendendo ogni riferimento identificabile e verificabile da un lettore esterno, senza confondere bibliografia esterna e tracciabilità interna e senza introdurre nuove scelte metodologiche.

## Lavoro svolto

1. Letto integralmente il dispatch 90.1 e gli artifact editoriali vincolanti della 90.0.
2. Verificato lo stato vivo di PROJECT_SOURCE_OF_TRUTH, PROJECT_CONTROL_REGISTER, DATA_REGISTRY, decisioni ACCEPTED e review pertinenti.
3. Ricostruita la lineage delle fonti a partire dai dataset/atti realmente usati nelle baseline accettate, senza trasformare DEC/ISS/review/artifact in bibliografia.
4. Verificate fonti originali e metadati correnti ove accessibili; dove il sito originale è risultato intermittente sono state usate esclusivamente evidenze originali già preservate e hashate.
5. Sostituiti i record-ombrello del seed con record specifici a livello di atto, dataset, typename, ID IRDAT, versione o DOI.
6. Documentati separatamente currentness, ruolo nella relazione, licenze/condizioni di riuso note, limiti e percorso dell'evidenza preservata.
7. Consultata la baseline Claude/QGIS solo come archivio storico intelligente; nessun claim corrente è sostenuto direttamente da Claude.
8. Non sono stati scritti capitoli della relazione.

## Fonti verificate e famiglie

Il registro finale contiene **52 record** esterni, distribuiti in:
- **REG: 5**
- **DATA: 25**
- **PLAN: 15**
- **TECH: 5**
- **STAT: 1**
- **LIT: 1**

Le famiglie coperte sono:
- AFIR e normativa TEN-T;
- LR FVG 19/2012;
- TENtec / rete TEN-T corrente;
- urbanistica FVG e PRGC correnti verificati;
- PGRA e PAI;
- PPR;
- Natura 2000 e aree protette;
- proxy energetico OSM / aree convenzionali / GSE / DSO / Terna;
- ISTAT pendolarismo 2021 per Light;
- Speth/ETISplus per Heavy.

## Fonti nuove / specificizzazioni principali

Rispetto al seed iniziale di 12 righe, il registro passa a 52 record (**+40 netto**). Il delta non equivale a 40 fonti completamente nuove: include soprattutto lo split di record generici in fonti puntuali.

Principali normalizzazioni:
- TENtec separato dal Reg. (UE) 2024/1679 e identificato con MapServer/layer 2024;
- IRDAT mantenuto solo come catalogo/licenza e separato dai singoli dataset;
- urbanistica separata tra Mosaicatura PRG 2018 storico-supporto e 8 casi comunali con currentness chiusa;
- PGRA separato tra atto/currentness e WFS pericolosità/rischio;
- PAI articolato per corpus e discipline di bacino;
- PPR separato tra piano vigente e subset WFS effettivamente materializzato;
- Natura 2000 / parchi / riserve / biotopi / prati stabili separati per typename;
- energia separata tra OSM, aree convenzionali, GSE, E-Distribuzione, AcegasApsAmga, SECAB e Terna;
- ISTAT pendolarismo identificato come dataset 2021;
- Heavy ricondotto a Speth et al. (2022) e Mendeley Data V1 DOI `10.17632/py2zkrb65h.1`.

## Fonti rimaste incomplete / gap espliciti

1. **Light / ISTAT:** non ancora dimostrato il binding byte-to-byte tra `ISTAT_commuting_LIGHT_v0.xlsx` e lo specifico download ufficiale ISTAT.
2. **Light / OSM stradale:** non ricostruito con sufficiente certezza bibliografica il timestamp/estratto OSM esatto che generò `G_OSM_operativo_v01`; nessun record fittiziamente preciso creato.
3. **PRGC:** currentness chiusa a livello citabile per 8/215 Comuni; i restanti casi mantengono la limitazione best-available già approvata.
4. **Natura 2000:** dataset di base verificati, ma ruleset finale dipendente dalla chiusura della Chat 3.12 / ISS-0013.
5. **PGRA WFS:** resta il limite già accettato di assenza di binding machine-readable WFS ↔ Delibera 12/2025.
6. **PAI:** sito del Distretto intermittente al re-check; originali già acquisiti e hashati dalla Chat 3.11 preservati.
7. **Licenze/riuso:** alcune pagine istituzionali e documenti DSO non espongono condizioni di riuso sufficientemente chiare; nessuna licenza è stata inventata.
8. **Letteratura metodologica futura:** volutamente non popolata per MCDM/ranking/normalizzazione/pesi/ottimizzazione.

## Piste Claude/QGIS e loro esito

La baseline storica Claude/QGIS è stata consultata soltanto per recuperare possibili piste. Esito:
- **0 fonti correnti promosse sulla sola base di Claude/QGIS**;
- nessuna pista Claude unica è risultata necessaria per colmare i gap residui;
- tutte le fonti entrate nel registro corrente sono state ricondotte a originali verificati o a originali già preservati nel nuovo progetto.

## Problemi di versioning/currentness rilevanti

- AFIR: usare la versione consolidata applicabile al claim; verificata quella al 08-01-2026.
- PPR: Variante 2 efficace dal 18-12-2025.
- PGRA: quadro vigente dal 22-01-2026; WFS operativo con caveat di version binding.
- Biotopi: quadro legale 42, WFS verificato 40.
- Heavy: la baseline frozen usa **Mendeley V1 (2021)**; non sostituire implicitamente con V2 (2025).
- Urbanistica: distinguere piano corrente verificato, vettore corrente verificato e proxy best-available.

## Questioni da riportare alla Chat 90.0

- mantenere aperti in tracciabilità editoriale i gap Light/ISTAT e Light/OSM finché non viene ricostruita la lineage esterna precisa;
- aggiornare la famiglia Natura 2000 dopo review/accettazione della Chat 3.12;
- estendere i record PRGC solo quando una fonte comunale entra effettivamente nella relazione o nella verifica dei candidati/finalisti;
- non presentare TE.R.R.A. come fonte di capacità disponibile del singolo sito;
- non introdurre bibliografia metodologica finché le tecniche non sono approvate.

## File creati/modificati

Modificati:
- `docs/relazione/EXTERNAL_SOURCE_REGISTER_v01.csv`
- `docs/relazione/EXTERNAL_SOURCE_NOTES_v01.md`

Creato:
- `docs/relazione/HANDOFF_CHAT_90.1_EXTERNAL_SOURCES_v01.md`

Nessun PROJECT_SOURCE_OF_TRUTH, PROJECT_CONTROL_REGISTER, baseline FROZEN o artifact scientifico è stato modificato.

## Controlli eseguiti

- CSV parsing Python standard library: **PASS**
- colonne header: **14**
- record dati: **52**
- righe con numero colonne errato: **0**
- citation key duplicate: **0**
- citation key vuote: **0**
- titoli vuoti: **0**
- URL vuoti: **0**
- pattern citation key `EXT-...`: **PASS**
- replacement character UTF-8 nei due artifact principali: **0**
- percorsi di evidenza preservata dichiarati: **43**
- percorsi di evidenza mancanti: **0**
- separazione fonti esterne / governance interna: **PASS**
- record dataset-specifici al posto di record-ombrello: **PASS**
- nessun contenuto Claude a sostegno diretto di claim corrente: **PASS**
- versioni/currentness esplicite quando reperibili: **PASS**
- gap espliciti: **PASS**
- `git diff --check`: **PASS**
- nessuna modifica metodologica o a baseline FROZEN: **PASS**

## Git

Commit contenuti principali:
- `6a2e3bb57c61bbb0db7fec8b2ddd12a46247625e` — `docs: normalize external source register`

Il presente handoff viene committato separatamente sullo stesso branch; il relativo hash è quello del commit che contiene questo file.

## Stato finale

**REVIEW / TECHNICAL QUALITY GATE = PASS_WITH_DOCUMENTED_GAPS**

Il mandato operativo 90.1 è completato per lo stato corrente del progetto. Non viene dichiarato ACCEPTED o FROZEN: la review spetta alla Chat 90.0 e, per gli aspetti di governance, alla Chat 0.2/utente.

## Prossimo passo consigliato

1. Chat 90.0: review del registro, delle note e dei gap.
2. Integrare/accettare il branch solo dopo la review editoriale.
3. Riattivare 90.1 quando Chat 3.12 o future fasi ACCEPTED/FROZEN introducono nuove fonti effettivamente usate, mantenendo il registro incrementale.
4. Non iniziare da questo handoff la redazione dei capitoli: il registro è infrastruttura bibliografica, non autorizzazione a superare lo stato scientifico corrente.
