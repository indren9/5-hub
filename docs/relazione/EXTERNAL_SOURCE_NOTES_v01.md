# EXTERNAL_SOURCE_NOTES_v01

## Stato

- Chat: **90.1 — Fonti esterne e bibliografia**
- Data verifica: **2026-09-21**
- Branch: `chat-90.1-external-sources`
- Stato artifact: **REVIEW**
- Autorità: esclusivamente editoriale/documentale; nessuna modifica metodologica.

## Regole applicate

1. **Fonte esterna ≠ tracciabilità interna.** DEC, ISS, DATA_REGISTRY, artifact, review, handoff e commit non sono bibliografia.
2. **Portale ≠ dataset.** IRDAT compare come record di catalogo/licenza, mentre i dataset usati hanno record distinti e identificabili.
3. **Atto ≠ geometria.** TEN-T, PGRA e PPR separano riferimento normativo/currentness e dataset cartografico.
4. **Currentness esplicita.** Una fonte è dichiarata corrente solo con evidenza originale verificata o con originale già preservato e hashato.
5. **Nessuna metodologia futura anticipata.** Non sono state aggiunte fonti MCDM, ranking, normalizzazione, pesi o ottimizzazione.
6. **Claude/QGIS non sostiene claim correnti.** È stato usato soltanto come archivio/pista; ogni fonte promossa è stata ricondotta all'originale.

## Normativa europea e regionale

### AFIR

È verificata la versione consolidata del Regolamento (UE) 2023/1804 al **08-01-2026**.
Per i claim già consolidati nel progetto sono pertinenti:
- art. 2(3)(b): per l'idrogeno, una stazione è “along the TEN-T road network” se è sulla rete oppure entro **10 km di distanza stradale** dall'uscita TEN-T più vicina;
- art. 4: target per infrastruttura pubblica di ricarica dei veicoli pesanti;
- art. 6: target H2 sulla TEN-T core al 2030, inclusi capacità cumulativa minima e pressione di erogazione previste dal regolamento.

Questi requisiti descrivono l'obbligo AFIR pertinente e non vengono trasformati da Chat 90.1 in requisiti universali della configurazione minima di ogni Hub.

### TEN-T e LR FVG 19/2012

Il Regolamento (UE) 2024/1679 e le geometrie TENtec sono registrati separatamente. Il dataset operativo verificato dal progetto è il servizio `TENT_Regulation_2024`, con layer stradali Core 8, Extended Core 9 e Comprehensive 10.

Per la LR FVG 19/2012 sono verificati metadati e testo coordinato Lexview vigente dal **01-01-2026**. Lexview avverte che il testo coordinato non sostituisce la pubblicazione ufficiale. Gli artt. 34 e 51 vanno citati soltanto quando il claim della relazione li richiede.

## Urbanistica

I dataset regionali `CER:ZONE_INDUSTRIALI_ARTIG_D` e `CER:ZONE_COMMERCIALI_H` restano **HISTORICAL_SUPPORT_ONLY**: derivano dalla Mosaicatura PRG 2018 e non sono prova generalizzata del PRGC vigente nel 2026.

Nel registro sono stati promossi come correnti solo gli otto casi già chiusi dalla validazione Fase 3:
- **CURRENT_VECTOR_VERIFIED:** Tavagnacco, Gorizia, Monfalcone, San Canzian d'Isonzo;
- **CURRENT_PLAN_VERIFIED_NO_VECTOR:** Grado, Arba, Cordenons, Porcia.

Per i quattro casi vettoriali sono separati la fonte comunale di currentness e il dataset IRDAT identificato (12217, 12238, 12239, 12194).

**Gap intenzionale:** gli altri 207 Comuni non sono dichiarati nel registro come “PRGC corrente verificato”. La baseline di screening best-available approvata dal progetto resta valida con i suoi flag di currentness, ma la bibliografia esterna va estesa puntualmente quando una fonte comunale specifica entra effettivamente nella relazione o nella verifica dei finalisti.

## PGRA e PAI

Per il PGRA sono separati:
- la Delibera 12/2025 e il quadro vigente dal **22-01-2026**;
- il WFS `sigma:Pericolo_direttiva_alluvioni`;
- il WFS `sigma:Rischio`.

Resta esplicito il limite già accettato: le capabilities/schema WFS live non espongono un binding machine-readable alla Delibera 12/2025 / set adottato in salvaguardia.

Per il PAI il registro distingue corpus generale e discipline di 4 Bacini, Fella, Livenza e UoM ITR061. Durante il re-check 90.1 il sito del Distretto è risultato intermittente; gli originali già materializzati e hashati dalla Chat 3.11 restano l'evidenza preservata.

## PPR, Natura 2000 e aree protette

Il PPR vigente con Variante 2, efficace dal **18-12-2025**, è separato dal subset WFS effettivamente usato. I typenames completi restano documentati nella matrice specialistica Fase 3 e il registro identifica il set come dataset specifico, non come generico “PPR/IRDAT”.

Natura 2000 mantiene record distinti per `SITI_PROT:SIC` e `SITI_PROT:ZPS`. Il typename `SIC` è tecnico/legacy e non sostituisce lo status legale della singola feature.

Per i biotopi resta il gap noto: **40 geometrie WFS** contro **42 biotopi nel quadro legale/istituzionale**. I D.P.Reg. 065/2026 e 066/2026 sono registrati separatamente come fonti legali puntuali.

La Chat 3.12 è ancora operativa sul pre-screening Natura 2000: il registro documenta le fonti già verificate, ma non anticipa né congela il ruleset finale.

## Energia

La baseline documentale del proxy energetico è distinta in:
- OSM `power=substation` come proxy fisico;
- `CER:AREECONVENZIONALI_CP` come copertura territoriale delle aree convenzionali/cabine primarie;
- GSE per semantica e mappa nazionale delle aree convenzionali;
- E-Distribuzione, AcegasApsAmga e SECAB come cross-check DSO ufficiali.

Terna/TE.R.R.A. è registrata **CONTEXT_ONLY**: non esiste nel progetto un dataset operativo di capacità disponibile materializzato e accettato. Non deve essere citata come se fornisse MW disponibili al singolo sito.

OpenInfraMap non è registrata come fonte dati autonoma: nel gate elettrico è stata trattata correttamente come viewer di dati OpenStreetMap.

## Light / ISTAT

La fonte ufficiale ISTAT “Matrice di pendolarismo per lavoro - Censimento permanente 2021” è verificata: riferimento 31-12-2021, pubblicazione 02-10-2025 e nota metodologica aggiornata 03-11-2025.

Il manifest della baseline Light dimostra che `LIGHT_DIRTY_OD_v01` usa `ISTAT_commuting_LIGHT_v0.xlsx`, ma non dimostra ancora un binding byte-to-byte fra quel file interno e lo specifico download ufficiale ISTAT corrente.

Per questo il registro usa lo stato:
`SOURCE_AND_DATASET_SEMANTICS_VERIFIED_LINEAGE_BINARY_BINDING_OPEN`.

Non trasformare questo gap in una falsa certezza bibliografica.

## Heavy / Speth-ETISplus

La baseline Heavy 6.0 è ricondotta a due fonti esterne verificabili:
- Speth et al., *Synthetic European road freight transport flow data*, Data in Brief 40 (2022), DOI `10.1016/j.dib.2021.107786`;
- dataset Mendeley Data **Version 1**, DOI `10.17632/py2zkrb65h.1`, pubblicato 24-09-2021, licenza CC BY 4.0.

Il repository Mendeley ha oggi una **Version 2 (2025)**, ma non viene sostituita implicitamente alla V1 perché la baseline Heavy frozen deriva dalla V1.

Queste voci documentano un dato Heavy effettivamente usato; non costituiscono anticipazione della futura letteratura metodologica su ranking/MCDM/ottimizzazione.

## Baseline Claude/QGIS — esito delle piste

La baseline storica è stata consultata come archivio intelligente. Nessuna voce del registro è stata promossa perché presente in Claude/QGIS.

Le fonti correnti sono state ricondotte a:
- fonte originale web verificata; oppure
- documento/dataset originale preservato nei package Fase 3 con evidenza e hash.

Non sono emerse piste Claude uniche necessarie a colmare i gap rimasti.

## Gap da riportare alla Chat 90.0

1. **Light / ISTAT:** binding binario/documentale definitivo tra `ISTAT_commuting_LIGHT_v0.xlsx` e lo specifico download ufficiale ISTAT ancora aperto.
2. **Light / OSM stradale:** l'origine OSM della baseline è nota, ma 90.1 non ha ricostruito con certezza bibliografica il timestamp/estratto OSM esatto da cui fu generato `G_OSM_operativo_v01`; nessun record fittiziamente preciso è stato creato.
3. **PRGC:** solo 8/215 casi hanno currentness chiusa al livello richiesto per una citazione puntuale; i restanti casi mantengono la limitazione best-available già approvata.
4. **Natura 2000:** dataset verificati; ruleset finale dipendente dalla chiusura della Chat 3.12.
5. **PGRA WFS:** resta il limite di binding della versione già accettato.
6. **Licenze/riuso:** per alcuni atti, pagine comunali e documenti DSO le condizioni di riuso non sono state inferite quando non esplicite; il campo resta prudenzialmente non verificato.

## Letteratura metodologica

Nessuna voce è stata aggiunta per MCDM, ranking, normalizzazione, pesi o ottimizzazione. Questa famiglia resta **NOT_READY** finché le tecniche corrispondenti non saranno approvate nel nuovo progetto.
