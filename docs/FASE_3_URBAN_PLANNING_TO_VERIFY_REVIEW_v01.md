# FASE 3 — URBAN PLANNING TO_VERIFY REVIEW v01

**Chat:** 3.9 — Chiusura dei 43 Comuni urbanistici TO_VERIFY  
**Data:** 2026-09-19  
**Stato:** REVIEW  
**TECHNICAL_QUALITY_GATE:** PASS  
**PHASE_4_READINESS:** NOT_READY  
**ISS-0010:** OPEN — decisione finale riservata alla Chat Madre

## 1. Mandato e perimetro

L'attività esegue DISPATCH_CHAT_3.9_CLOSE_URBAN_PLANNING_TO_VERIFY_v01.md
secondo DEC-0032, DEC-0045 e DEC-0046.

Perimetro esclusivo: i 43 Comuni TO_VERIFY dello snapshot
FASE_3_CURRENT_URBAN_PLANNING_TO_VERIFY_BASELINE_v01.csv.

SHA-256 atteso e verificato:
EEDFD368D1B1182E73124D6C816383E25EE178E5B81FB0051F2A15EC4FC9D2C6.

Sono rimasti fuori scope i 167 casi lineage-incomplete della Chat 3.8,
Grado e i 4 Comuni CURRENT_VECTOR_VERIFIED.

## 2. Regola applicata

È stata applicata la procedura current-first di DEC-0032.
Per ogni Comune è stata ricercata prima una fonte ufficiale comunale e poi, quando necessario, evidenza istituzionale regionale o BUR di supporto.

La classificazione è stata conservativa. CURRENT_PLAN_VERIFIED_NO_VECTOR è usato solo con evidenza esplicita e sufficientemente corrente della vigenza. CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE è usato quando la fonte ufficiale è utile ma manca almeno un passaggio di lineage.

Nessuna adozione è stata trattata automaticamente come efficacia. Nessun PDF o WebGIS è stato trattato automaticamente come vettore corrente. IRDAT, Eagle e CER 2018 non sono stati promossi silenziosamente a prova di vigenza.

## 3. Risultato sui 43 Comuni

Tutti i 43 casi sono stati processati con fonte ufficiale e gap residuo esplicito.

Esito sui 43:
- 3 CURRENT_PLAN_VERIFIED_NO_VECTOR;
- 40 CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE;
- 0 nuovi CURRENT_VECTOR_VERIFIED;
- 0 TO_VERIFY residui.

I tre casi con piano corrente verificato ma senza vettore corrente acquisito sono Arba, Cordenons e Porcia.

## 4. Nuova distribuzione dei 215 Comuni

Prima: 4 CURRENT_VECTOR_VERIFIED, 1 CURRENT_PLAN_VERIFIED_NO_VECTOR, 167 CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE, 43 TO_VERIFY.

Dopo: 4 CURRENT_VECTOR_VERIFIED, 4 CURRENT_PLAN_VERIFIED_NO_VECTOR, 207 CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE, 0 TO_VERIFY.

Totale invariato: 215 Comuni e 215 codici ISTAT univoci.
Il confronto automatico non rileva alcuna modifica nelle 172 righe fuori perimetro.

## 5. Evidenze e preservazione

Le 43 fonti primarie sono registrate con URL e data di accesso.
La materializzazione automatica ha salvato 34 sorgenti in OneDrive.
Nove fonti non sono state materializzate per errori SSL/certificato o timeout del server; il mancato download non è stato interpretato come assenza della fonte e resta registrato nel manifest.

Per i 34 artifact materializzati:
- byte e SHA-256 sono registrati nel manifest;
- preservation check: PASS;
- mismatch SHA-256: 0.

Nessuna nuova geometria vettoriale è stata acquisita o promossa in questa attività.

## 6. Quality gate

TECHNICAL_QUALITY_GATE = PASS.

Controlli:
- baseline hash: PASS;
- 43/43 codici processati: PASS;
- perimetro 43 codici univoci: PASS;
- coverage 215/215 e codici univoci: PASS;
- modifiche fuori scope: 0, PASS;
- TO_VERIFY residui: 0;
- evidenza e gap espliciti 43/43: PASS;
- fonti storiche non promosse a correnti: PASS;
- manifest e preservation degli artifact materializzati: PASS;
- Fase 1 e Fase 2 FROZEN non modificate: PASS;
- nessun candidato Hub costruito: PASS.

## 7. ISS-0010 e PHASE_4_READINESS

ISS-0010 resta OPEN. La Chat 3.9 non ne dichiara la chiusura.

Il problema dei 43 casi senza evidenza sufficiente è stato eliminato, ma il problema residuo cambia forma: 207 Comuni sono ora CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE e 4 hanno piano corrente verificato senza vettore corrente. Solo 4 Comuni dispongono di CURRENT_VECTOR_VERIFIED.

PHASE_4_READINESS = NOT_READY.

Motivo: i gap di lineage e geometria ancora presenti possono modificare l'universo poligonale. La prossima attività dovrebbe affrontare i 207 casi lineage-incomplete secondo mandato separato della Chat Madre.

## 8. Artifact

Repository:
- FASE_3_URBAN_PLANNING_TO_VERIFY_RESULTS_v01.csv
- FASE_3_CURRENT_URBAN_PLANNING_COVERAGE_v02.csv
- FASE_3_URBAN_PLANNING_TO_VERIFY_EVIDENCE_v01.json
- FASE_3_URBAN_PLANNING_TO_VERIFY_QA_v01.json
- chat3_9_source_evidence_v01.jsonl
- close_urban_planning_to_verify_chat3_9_v01.py
- HANDOFF_CHAT_3.9_URBAN_PLANNING_TO_VERIFY_v01.md

Storage tecnico: 5_HUB_FVG/02_external_sources/F3_CHAT_3_9/.
Manifest: source_manifest_v01.json.

## 9. Stato finale

Chat 3.9: COMPLETED / TECHNICAL PASS.
Il raggiungimento di TO_VERIFY = 0 non equivale a PHASE_4_READY e non chiude ISS-0010.
