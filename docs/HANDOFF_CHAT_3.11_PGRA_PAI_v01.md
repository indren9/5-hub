# HANDOFF — Chat 3.11 — Baseline idrogeologica corrente PGRA + PAI

**Chat:** 3.11 — Baseline idrogeologica corrente PGRA + PAI
**Data:** 2026-09-20
**Destinatario:** Chat 0.2 — Chat Madre 5 HUB
**Stato finale operativo:** PASS_WITH_LIMITATIONS / REVIEW
**Branch:** `chat-3.11-pgra-pai-current-baseline`
**Commit principale:** `e56f545` — `feat(data): validate current PGRA and PAI baseline`

## 1. Obiettivo

Chiudere il quality gate dati corrente PGRA + PAI a scala di pianificazione macro regionale, senza riaprire DEC-0039/DEC-0040, senza scoring o hard filter e senza aprire Fase 4.

## 2. Lavoro svolto

Sono stati:
- letti dispatch, baseline F1/F2, review/role matrix/handoff Chat 3.4;
- verificati PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER;
- verificato il quadro PGRA vigente 2026;
- cercato un binding forte WFS↔versione PGRA vigente;
- materializzato il fallback autorizzato DEC-0039;
- identificato il corpus PAI vigente applicabile al FVG;
- acquisiti cartografia-indice, discipline ufficiali e supporti GIS regionali;
- documentato il gap residuo dei vettori PAI ufficiali completi/current-versioned.
## 3. PGRA — esito

Currentness ufficiale:
- Delibera n. 12 del 18-12-2025;
- avviso G.U. n. 16 del 21-01-2026;
- efficacia dal 22-01-2026.

Binding forte WFS↔Delibera/PGRA2027:
**NON TROVATO** nelle capabilities/schema e nelle fonti pubbliche verificate.

È stato quindi applicato il fallback DEC-0039:
**WFS ufficiale live + caveat/version lineage esplicito**.

Snapshot:
- pericolosità: 187.230 feature, EPSG:3035;
- rischio: 132.840 feature, EPSG:3035;
- conteggi WFS = conteggi DBF;
- ZIP integrity PASS.

**Proposta ISS-0006: PROPOSE_RESOLVED_PROCEDURALLY.**
## 4. PAI / frane — esito

Corpus pertinente FVG identificato:
- Isonzo ITN004;
- Livenza ITN006;
- Piave ITN007;
- Tagliamento ITN009;
- sottobacino Fella;
- bacini regionali FVG ITR061.

Sono state materializzate le pagine ufficiali cartografiche e indicizzati 627 link PDF di bacino.
Sono state materializzate le discipline principali PAI 4 Bacini, Fella, Livenza e PAIR/FVG.

La documentazione regionale ufficiale indica il Distretto come soggetto da cui ottenere i file vettoriali della cartografia PAI.
Non è stato trovato un pacchetto vettoriale pubblico unico/completo/current-versioned che dimostri equivalenza al PAI vigente comprensivo degli aggiornamenti e delle zone di attenzione.

**Proposta ISS-0012: READY_WITH_LIMITATIONS.**
## 5. Catasto Frane / supporto regionale

Confronto WFS live 2026-09-20:
- `UTIL_TER:VW_DATA_FRANE_PERICOLOSITA`: 2.904;
- `UTIL_TER:VW_DATA_FRANE_PERIMETRO`: 6.919;
- `IRDAT:VW_FR_IFFI`: 6.568;
- `IRDAT:CATFRANE_PERICOLOSITA`: 830;
- `IRDAT:CATFRANE_PERIMFRANE`: 4.989.

Le popolazioni CATFRANE legacy e le viste correnti UTIL_TER/VW non sono equivalenti per conteggio e lineage.

Regola mantenuta:
**CATFRANE / UTIL_TER / IFFI = SUPPORT_ONLY**, non PAI completo e non fonte di esclusione automatica.

Una geometria IFFI non viene interpretata automaticamente come zona di attenzione PAI.
## 6. Artifact repository

Creati:
- `docs/FASE_3_PGRA_PAI_CURRENT_BASELINE_VALIDATION_REVIEW_v01.md`;
- `docs/FASE_3_PGRA_PAI_SOURCE_MATRIX_v01.csv`;
- `scripts/acquire_validate_pgra_pai_chat3_11_v01.py`;
- `docs/HANDOFF_CHAT_3.11_PGRA_PAI_v01.md`.

Commit principale:
`e56f545 feat(data): validate current PGRA and PAI baseline`

Questo handoff viene committato separatamente al termine della sessione.

## 7. Artifact OneDrive

Root:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_11\`

Sottocartelle:
- `pgra\`;
- `pai\`;
- `official_discipline\`;
- `regional_support\`.
File controllo:
- `source_manifest_v01.json`;
- `qa_validation_v01.json`;
- `pai\pai_official_map_links_v01.csv`.

Hash:
- manifest SHA-256: `24E9FD460EA1D72A020C624C15A2A2DAC819B1D7B7E22B111BFA6E4177C0F67C`;
- QA SHA-256: `FC6F7EA395DA7F68745095479F879706FB2B95827BE35215C254D40C009DB945`.

Gli ZIP PGRA e regionali hanno tutti integrity check PASS.

## 8. Governance viva aggiornata

PROJECT_CONTROL_REGISTER:
- ISS-0006 → `REVIEW`, owner Chat 0.2, proposta `PROPOSE_RESOLVED_PROCEDURALLY`;
- ISS-0012 → `REVIEW`, owner Chat 0.2, proposta `READY_WITH_LIMITATIONS`;
- F3_SRC_PGRA_001 aggiornato con baseline Chat 3.11;
- F3_SRC_FVG_LANDSLIDE_001 aggiornato con confronto layer;
- aggiunto `F3_SRC_PAI_001`;
- aggiunto `F3_SRC_FVG_LANDSLIDE_002`.

Nessuna issue è stata chiusa autonomamente.
## 9. Quality checks

Esiti:
- acquisition/validation script: PASS;
- `python -m py_compile`: PASS;
- CSV source matrix parse: PASS;
- WFS counts vs DBF counts: PASS;
- ZIP integrity: PASS;
- PGRA strong-binding probe: NOT FOUND, fallback correttamente applicato;
- `git diff --check`: PASS;
- Fase 4: NON APERTA.

## 10. Decisioni/proposte emerse

Nessuna nuova decisione metodologica è stata introdotta.

Proposte alla Chat Madre:
1. accettare il quality gate PGRA e chiudere proceduralmente ISS-0006 se ritiene soddisfatto DEC-0039;
2. mantenere ISS-0012 come READY_WITH_LIMITATIONS / REVIEW finché non viene acquisito il vettore PAI ufficiale completo dal Distretto o un binding equivalente;
3. non promuovere le viste regionali Catasto Frane a PAI normativo completo;
4. non aprire Fase 4 sulla sola base di questo handoff.
## 11. Problemi aperti

**PAI vector gap:** manca una baseline vettoriale pubblica unica e dimostrabilmente completa/current-versioned del PAI vigente FVG.
Il canale ufficiale indicato dalla Regione è il Distretto.

**PGRA version binding:** il WFS live è ufficiale e corrente come servizio, ma il legame machine-readable con Delibera 12/2025/PGRA2027 non è stato trovato.
Il caveat è parte integrante della baseline.

**Licenze/redistribuzione:** condizioni specifiche di riuso dei file SIGMA/PAI devono essere verificate prima di eventuale redistribuzione esterna; l'uso interno di progetto resta tracciato.

## 12. Prossimo passo

Chat 0.2 deve:
- revieware gli artifact e il commit;
- decidere lo stato effettivo di ISS-0006 e ISS-0012;
- aggiornare il PROJECT_SOURCE_OF_TRUTH solo se accetta gli esiti;
- valutare l'eventuale acquisizione dei vettori PAI ufficiali dal Distretto.

**STOP Chat 3.11. FASE 4 non aperta.**
