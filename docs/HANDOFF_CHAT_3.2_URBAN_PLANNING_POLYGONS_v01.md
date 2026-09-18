# HANDOFF — CHAT 3.2 — URBANISTICA, POLIGONI SORGENTE E DISPONIBILITÀ

**Chat:** 3.2 — Urbanistica, poligoni sorgente e disponibilità
**Fase:** 3 — Inventario e validazione dei dati
**Data chiusura:** 2026-09-18
**Stato finale proposto:** PASS TECNICO-OPERATIVO / REVIEW CHAT MADRE
**Mandato:** `docs/DISPATCH_CHAT_3.2_URBAN_PLANNING_POLYGONS_v01.md`

## 1. Obiettivo

Risolvere o delimitare con evidenza:
- `ISS-0003`: affidabilità della Mosaicatura PRG 2018 come rappresentazione urbanistica corrente;
- `ISS-0009`: esistenza e copertura di dati di proprietà/disponibilità.

Vincoli rispettati:
- nessun `CANDIDATES_RAW`;
- nessuna categoria urbanistica ammissibile decisa;
- nessuna soglia di superficie introdotta;
- nessuna modifica alle baseline FROZEN Fase 1 e Fase 2;
- nessuna decisione metodologica sostanziale approvata autonomamente.

## 2. Lavoro svolto

1. letti dispatch 3.2, baseline F1/F2 e review 3.1;
2. verificati PROJECT_SOURCE_OF_TRUTH, DATA_REGISTRY e ISSUES vivi;
3. verificato lineage ufficiale dei WFS CER D/H;
4. costruito audit riproducibile sui 215 Comuni ISTAT FVG;
5. verificata presenza tecnica di configurazioni EagleFVG PRG;
6. analizzato GetCapabilities WFS regionale;
7. confrontato CER con un campione di PRGC/varianti comunali correnti;
8. censite fonti ufficiali per patrimonio/disponibilità;
9. materializzate evidenze esterne in OneDrive con manifest e SHA-256;
10. aggiornati DATA_REGISTRY e ISSUES;
11. eseguiti test e commit Git esplicito.
## 3. Risultati principali

### Urbanistica / ISS-0003

- `CER:ZONE_INDUSTRIALI_ARTIG_D`: 4.155 feature.
- `CER:ZONE_COMMERCIALI_H`: 1.466 feature.
- Origine documentata: Mosaicatura PRG 2018.
- Nessun `DATA_VAL` osservato nei 215 Comuni correnti è post-2018.
- Il CER contiene codici di Comuni oggi soppressi/aggregati.
- Il campione corrente dimostra mismatch temporali multipli.
- Polcenigo fornisce anche evidenza di modifica di zonizzazione/perimetro successiva allo snapshot CER.

Classificazione tecnica proposta:
`ENDPOINT_CURRENT / CONTENT_HISTORICAL / NON_CURRENT_FOR_2026 / SUPPORT_ONLY`.

`ISS-0003` è stato portato da OPEN a **REVIEW**, con proposta alla Chat Madre di considerare risolto il dubbio stretto sulla currentness del CER.

### Fonte P1 corrente

Non è stata verificata una singola mosaicatura regionale pubblica 2026 con vigenza documentata per tutti i 215 Comuni.

Il probe ha rilevato configurazioni EagleFVG PRG standard per **147/215** Comuni.

Il mancato rilevamento standard non è stato trasformato in assenza del PRGC o di Eagle.

Proposta tecnica, non approvata:
procedura **current-first / ibrida**, con vigenza verificata da fonte ufficiale comunale e geometria EagleFVG/Regione utilizzata quando il relativo allineamento è documentato.

### Disponibilità / ISS-0009

Fonti ufficiali parziali identificate:
- patrimonio immobiliare disponibile Regione FVG, dati aggiornati al 30/06/2026;
- dati catastali del patrimonio regionale disponibile;
- fonti dei sei Consorzi di sviluppo economico locale;
- fonti comunali/patrimoniali puntuali.

Non è stato verificato un dataset unico region-wide di disponibilità effettiva/fisica/commerciale.

`ISS-0009` resta **OPEN**, ma è ora DELIMITED.

### Nuova issue

Registrata `ISS-0010`: la vigenza dei PRGC comunali non è uniformemente automatizzabile; accessibilità digitale ed effettiva vigenza devono restare stati separati.
## 4. File creati / modificati

### Git — file 3.2

- `scripts/validate_urban_planning_sources.py`
- `docs/FASE_3_URBAN_PLANNING_CURRENT_SAMPLE_v01.csv`
- `docs/FASE_3_URBAN_PLANNING_MUNICIPAL_COVERAGE_v01.csv`
- `docs/FASE_3_URBAN_PLANNING_VALIDATION_EVIDENCE_v01.json`
- `docs/FASE_3_URBAN_PLANNING_VALIDATION_REVIEW_v01.md`
- `docs/HANDOFF_CHAT_3.2_URBAN_PLANNING_POLYGONS_v01.md` — da includere nel commit di chiusura.

### OneDrive — evidenze esterne

Directory:
`5_HUB_FVG\02_external_sources\urban_planning_validation_20260918\`

Contiene:
- `Elenco-comuni-italiani.csv`;
- `CER_LINEE_GUIDA_LAYER_MAPPATURA_FVG_2023.pdf`;
- `DGR1174_2024_Allegato_tecnico_PRGC_PGRA.pdf`;
- `FVG_GeoServer_WFS_GetCapabilities_20260918.xml`;
- `CER_ZONE_D_codes_20260918.csv`;
- `CER_ZONE_H_codes_20260918.csv`;
- `Patrimonio_disponibile_Regione_2026-06.pdf`;
- `Patrimonio_disponibile_catasto_2026-06.pdf`;
- `source_manifest_v01.json`.

SHA-256 del manifest:
`207E2656C28FF5829A764F4ACD4139FEC5388E63A3EE283AABC90E52F0F29F55`.

Verifica manifest:
**PASS — 8/8 file presenti con SHA-256 coerente**.

## 5. Registri vivi aggiornati

### DATA_REGISTRY

Aggiornati:
- `F3_SRC_FVG_ZONING_IND_001` → REVIEW; storico/supporto, non fonte corrente definitiva;
- `F3_SRC_FVG_ZONING_COM_001` → REVIEW; stesso trattamento.

Aggiunti:
- `F3_SRC_ISTAT_MUNI_001`;
- `F3_SRC_FVG_EAGLE_PRGC_001`;
- `F3_SRC_FVG_PATRIMONY_001`;
- `F3_SRC_FVG_CONSORTIA_AVAIL_001`.

Le celle sono state rilette dopo la scrittura; validazione e formattazione risultano preservate.

### ISSUES

- `ISS-0003`: OPEN → REVIEW.
- `ISS-0009`: resta OPEN; prossima azione aggiornata con la delimitazione.
- `ISS-0010`: nuova issue OPEN.

Nessun elemento sostanziale è stato marcato ACCEPTED/FROZEN.
## 6. Controlli ed esito

- Python `py_compile`: **PASS**.
- coverage table: **215/215** righe e codici ISTAT univoci.
- campione corrente: **7** Comuni.
- cardinalità CER: **4.155 D / 1.466 H**.
- Eagle probe: **147/215** configurazioni standard rilevate.
- JSON evidence parse/assertions: **PASS**.
- OneDrive manifest: **PASS 8/8**.
- `git diff --cached --check`: **PASS** prima del commit tecnico.
- nessun file Chat 3.3 incluso nello staging/commit 3.2.

## 7. Git

Branch:
`chat-3.2-urban-planning`

Commit tecnico:
`e46ed56` — `feat(fase3): validate urban planning sources and availability`

Nota concorrenza:
nel working tree sono presenti file non tracciati della Chat 3.3. Sono stati lasciati intatti e deliberatamente esclusi dallo staging 3.2.

Il presente handoff e l'aggiornamento finale del quality gate vengono versionati con un commit di chiusura separato.

## 8. Decisioni / proposte emerse

Nessuna decisione metodologica sostanziale è stata approvata autonomamente.

Da sottoporre alla Chat Madre:
1. accettare/modificare la procedura P1 current-first/ibrida;
2. verificare la proposta di risoluzione di `ISS-0003`;
3. mantenere `ISS-0009` aperta e decidere `Q-METH-3.1-C`;
4. stabilire se la raccolta completa dei 215 PRGC correnti debba essere completata in Fase 3 oppure diventare input controllato della Fase 4;
5. fissare il livello minimo di currentness/lineage necessario prima di generare poligoni;
6. mantenere CER 2018 come storico/supporto e non promuoverlo a baseline urbanistica corrente.

## 9. Problemi aperti

- `ISS-0009`: disponibilità/proprietà region-wide non risolta.
- `ISS-0010`: currentness PRGC non completamente automatizzabile.
- per 68 Comuni il probe standard Eagle non ha rilevato una configurazione; serve fallback ufficiale, non interpretazione negativa.
- per molti Comuni il numero/data della variante effettivamente vigente deve ancora essere ricostruito.
- licenze/condizioni di riuso delle geometrie comunali/Eagle vanno registrate durante l'acquisizione completa.
- la procedura P1 è PROPOSED, non ACCEPTED.
## 10. Stato finale e prossimo passo

**Chat 3.2: PASS TECNICO-OPERATIVO / REVIEW CHAT MADRE.**

La Fase 3 complessiva resta IN CORSO.
La Fase 4 non è autorizzata da questa chat.

Prossimo passo raccomandato:
review della Chat Madre sulle proposte P1 e sugli stati `ISS-0003`, `ISS-0009`, `ISS-0010`, coordinandole con l'handoff della Chat 3.3 prima di dichiarare il gate Fase 3.

## 11. SESSION CLOSE V1

`NOTEBOOK_CHANGE = NO`
Motivo: il progetto 5 HUB usa PROJECT_SOURCE_OF_TRUTH/PROJECT_CONTROL_REGISTER come governance autorevole; F1/F2 non sono stati modificati.

`REGISTER_CHANGE = YES`
Eseguito e verificato su DATA_REGISTRY e ISSUES.

`GIT_COMMIT_REQUIRED = YES`
Soddisfatto: commit tecnico eseguito e handoff/aggiornamento finale review inclusi nel commit di chiusura della sessione; hash finale riportato nella risposta di chiusura.

Artifact check:
- nessun FROZEN sovrascritto;
- artifact Git nuovi in stato REVIEW/working result;
- evidenze esterne preservate in OneDrive con manifest e hash;
- nessun output candidato costruito.

Build notebook:
N/A.

Preservation verification:
**PASS** per il package di evidenze esterne materializzato nella directory OneDrive sopra indicata.

Session close:
**PASS**. Il presente handoff è l'artifact di chiusura; il relativo commit di chiusura viene eseguito immediatamente dopo la sua materializzazione e il relativo hash è riportato nella risposta finale.
