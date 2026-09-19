# DISPATCH — Chat 3.9 — Chiusura dei 43 Comuni urbanistici TO_VERIFY

**Fase:** 3 — Inventario e validazione dei dati  
**Data:** 2026-09-19  
**Stato mandato:** AUTHORIZED  
**Regia:** Chat Madre 5 HUB

## 1. Obiettivo

Lavorare esclusivamente sui 43 Comuni classificati `TO_VERIFY` dalla Chat 3.8, per identificare e validare la migliore evidenza ufficiale disponibile sul PRGC vigente e, quando possibile, sulla relativa geometria corrente.

La Chat 3.9 NON deve affrontare i 167 casi già classificati `CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE`.

Obiettivo operativo prioritario: ridurre il numero di `TO_VERIFY` fino a zero, se le fonti ufficiali disponibili lo consentono, senza colmare i gap con assunzioni o dati storici.

## 2. Perimetro vincolante

Baseline dei 43 casi:

`docs/FASE_3_CURRENT_URBAN_PLANNING_TO_VERIFY_BASELINE_v01.csv`

SHA-256 baseline:
`EEDFD368D1B1182E73124D6C816383E25EE178E5B81FB0051F2A15EC4FC9D2C6`

La baseline contiene esattamente 43 codici ISTAT univoci.

Sono fuori scope:
- i 167 casi con lineage incompleto;
- Grado, già `CURRENT_PLAN_VERIFIED_NO_VECTOR`;
- i 4 `CURRENT_VECTOR_VERIFIED`.

## 3. Baseline e decisioni vincolanti

READ ONLY:
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN;
- `docs/FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01.md` — FROZEN;
- `docs/FASE_3_CURRENT_URBAN_PLANNING_VALIDATION_REVIEW_v01.md`;
- `docs/FASE_3_CURRENT_URBAN_PLANNING_COVERAGE_v01.csv`;
- `docs/FASE_3_CURRENT_URBAN_PLANNING_EVIDENCE_v01.json`;
- `docs/HANDOFF_CHAT_3.8_CURRENT_URBAN_PLANNING_v01.md`;
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER.

Decisioni vincolanti:
- `DEC-0032`: procedura urbanistica current-first / ibrida;
- `DEC-0045`: PASS tecnico Chat 3.8 accettato, Fase 4 NOT_READY, `ISS-0010` OPEN.

I layer CER D/H basati sulla Mosaicatura PRG 2018 restano HISTORICAL / SUPPORT ONLY.

## 4. Domanda da risolvere per ciascuno dei 43 Comuni

Per ogni Comune determinare, con evidenza ufficiale:
1. quale PRGC risulta vigente;
2. quale sia l'ultima variante efficace/esecutiva pertinente;
3. quale atto o pagina istituzionale sostenga tale conclusione;
4. se esista una geometria ufficiale corrente;
5. se la geometria possa essere dimostrata allineata alla versione vigente;
6. quale gap rimanga se uno dei punti precedenti non è chiudibile.

## 5. Gerarchia delle fonti

Ordine di priorità:
1. sito ufficiale del Comune / sezione urbanistica / amministrazione trasparente;
2. atti comunali ufficiali e relativi allegati;
3. BUR FVG e altri atti regionali ufficiali pertinenti;
4. IRDAT / EagleFVG solo come fonte ufficiale di pubblicazione/discovery, da verificare rispetto alla vigenza;
5. altre fonti istituzionali solo come supporto.

Motori di ricerca e snippet possono servire per discovery, ma non costituiscono prova finale.

Per ogni fonte utilizzata registrare URL, data di accesso, tipo di documento, atto/variante, stato procedurale e motivo per cui l'evidenza è ritenuta sufficiente o insufficiente.

## 6. Regole di classificazione

Una riga può essere promossa a:
- `CURRENT_VECTOR_VERIFIED` solo se piano/variante corrente e geometria sono allineati con evidenza sufficiente;
- `CURRENT_PLAN_VERIFIED_NO_VECTOR` se la vigenza è verificata ma non è disponibile/acquisibile un vettore corrente;
- `CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE` se esiste una fonte istituzionale utile ma manca ancora almeno un passaggio di lineage;
- `TO_VERIFY` solo se, dopo ricerca documentata, non esiste evidenza sufficiente per una classificazione superiore.

Non inventare nuove classi sostanziali senza sottoporle alla Chat Madre.

## 7. Principio di ricerca efficiente

Prima cercare pattern riutilizzabili:
- portali condivisi;
- famiglie di URL comunali;
- servizi IRDAT;
- strutture ricorrenti di atti/BUR;
- convenzioni territoriali o sistemi informativi sovracomunali.

Automatizzare discovery, download, checksum e parsing quando affidabile.

La verifica finale della vigenza deve però restare basata su evidenza istituzionale leggibile e tracciabile.

Ogni caso manuale deve restare esplicito: nessun esito può derivare solo da una deduzione implicita dello script.

## 8. Geometrie

Se emerge un vettore ufficiale:
- acquisire il pacchetto originale quando pratico;
- conservare URL, byte, SHA-256, formato e CRS;
- eseguire QA di integrità;
- verificare, per quanto documentabile, l'allineamento con la variante corrente.

Se esiste solo PDF/WebGIS non scaricabile:
- non digitalizzare automaticamente come unica fonte autorevole;
- classificare il caso secondo l'evidenza realmente disponibile.

## 9. Output obbligatori

Repository locale:
- `docs/FASE_3_URBAN_PLANNING_TO_VERIFY_REVIEW_v01.md`;
- `docs/FASE_3_URBAN_PLANNING_TO_VERIFY_RESULTS_v01.csv`;
- `docs/FASE_3_CURRENT_URBAN_PLANNING_COVERAGE_v02.csv`;
- `docs/FASE_3_URBAN_PLANNING_TO_VERIFY_EVIDENCE_v01.json`;
- `docs/HANDOFF_CHAT_3.9_URBAN_PLANNING_TO_VERIFY_v01.md`;
- script/moduli leggeri necessari alla riproducibilità.

La coverage v02 deve contenere ancora tutti i 215 Comuni e differire dalla v01 esclusivamente nelle 43 righe del perimetro Chat 3.9, salvo correzioni tecniche esplicitamente motivate.

Storage pesante:
`5_HUB_FVG\02_external_sources\F3_CHAT_3_9\`

Tutti gli artifact materializzati devono essere coperti da manifest con URL/fonte, data, byte e SHA-256.

Branch:
`chat-3.9-close-urban-planning-to-verify`.

## 10. Quality gate

Il TECHNICAL_QUALITY_GATE può essere PASS solo se:
- i 43 codici ISTAT della baseline sono tutti processati;
- nessun Comune fuori perimetro viene modificato senza motivazione esplicita;
- ogni esito ha evidenza e gap residuo tracciati;
- nessuna fonte storica viene promossa silenziosamente a corrente;
- eventuali vettori acquisiti superano QA tecnico;
- coverage v02 mantiene 215 codici ISTAT univoci;
- i conteggi pre/post sono riproducibili;
- manifest/hash/preservation sono verificati;
- Fase 1 e Fase 2 FROZEN restano invariate;
- nessun candidato Hub viene costruito;
- SESSION CLOSE e handoff sono completi.

Target operativo:
`TO_VERIFY = 0`.

Il target non è però una condizione che autorizza a forzare le fonti: se alcuni casi restano realmente non verificabili, devono restare `TO_VERIFY` con ricerca documentata.

## 11. Readiness e governance

Al termine calcolare nuovamente:
- distribuzione dei 215 Comuni per `currentness_status`;
- numero residuo di `TO_VERIFY`;
- implicazioni per `ISS-0010`;
- `PHASE_4_READINESS`.

La Chat 3.9 NON può:
- chiudere autonomamente `ISS-0010`;
- dichiarare autonomamente la Fase 4 READY;
- attaccare i 167 lineage incompleti;
- introdurre una nuova metodologia urbanistica.

Qualsiasi proposta di modifica sostanziale va riportata alla Chat Madre.

## 12. Criterio di successo

La Chat Madre deve poter rispondere a due domande separate:

1. “Quanti dei 43 veri buchi urbanistici sono stati eliminati con evidenza ufficiale?”
2. “Dopo questo passaggio, qual è esattamente il problema residuo prima di affrontare i 167 casi con lineage incompleto?”

Anche se alcuni Comuni restano `TO_VERIFY`, il lavoro è utile solo se rende esplicito perché non sono verificabili e quali azioni realistiche restano possibili.

**La Chat 3.9 deve chiudersi con PASS/FAIL tecnico, nuovo conteggio dei 215 Comuni, PHASE_4_READINESS e handoff completo.**

