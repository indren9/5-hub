# REVIEW — Chat 90.1 — Fonti esterne e bibliografia

**Reviewer:** Chat 90.0 — Relazione Builder
**Data:** 2026-09-21
**Stato:** ACCEPTED_WITH_DOCUMENTED_GAPS
**Mandato:** DISPATCH_CHAT_90.1_EXTERNAL_SOURCES_v01.md
**Handoff:** HANDOFF_CHAT_90.1_EXTERNAL_SOURCES_v01.md

## 1. Esito

La Chat 90.1 è accettata sul piano editoriale/documentale.

Il registro delle fonti esterne è sufficientemente normalizzato e verificato per supportare i prossimi workstream editoriali, con i gap residui esplicitamente documentati e senza trasformarli in false certezze.

L'accettazione non modifica lo stato scientifico delle fonti, delle fasi o delle issue ufficiali.

## 2. Controlli indipendenti della Chat 90.0

La Chat 90.0 ha verificato branch e commit dichiarati, handoff 90.1, struttura e parsing del registro, distribuzione delle categorie, completezza dei campi core, stati di verifica, separazione fra bibliografia esterna e governance interna, assenza di fonti Claude/QGIS promosse come correnti e coerenza dei gap dichiarati con lo stato vivo del progetto.

Esiti:
- record esterni: 52;
- categorie: 5 REG, 25 DATA, 15 PLAN, 5 TECH, 1 STAT, 1 LIT;
- citation key duplicate: 0;
- campi core mancanti verificati: 0;
- riferimenti Claude/QGIS nel registro corrente: 0;
- riferimenti DEC/ISS/chat/commit nel registro esterno: 0;
- git diff --check: PASS.

## 3. Punti accettati

Sono accettati:
- lo split dei record generici in fonti identificabili;
- la separazione tra atto normativo e dataset/geometria;
- il trattamento dell'urbanistica corrente verificata solo dove realmente dimostrata;
- la distinzione fra PGRA vigente e WFS operativo con caveat di version binding;
- la distinzione tra PAI normativo e fonti regionali/supporto;
- la separazione fra proxy elettrico e capacità reale;
- la lineage Heavy verso Speth et al. e Mendeley Data V1;
- l'esclusione di letteratura MCDM/ranking/ottimizzazione non ancora metodologicamente approvata.

## 4. Gap residui da preservare

### G90.1-01 — Light / ISTAT
La semantica e la fonte ISTAT sono identificate, ma non è ancora dimostrato il binding binario tra il file interno Light e lo specifico download ufficiale.

Conseguenza editoriale: il futuro capitolo mobilità può descrivere la fonte ISTAT e il ruolo della baseline Light, ma non deve affermare una lineage byte-to-byte non dimostrata.

### G90.1-02 — Light / OSM stradale
Non è ricostruito con sufficiente certezza bibliografica l'estratto/timestamp OSM esatto che ha generato G_OSM_operativo_v01.

Conseguenza editoriale: citare OSM come fonte del sistema stradale solo con formulazione coerente con la lineage effettivamente disponibile, evitando uno snapshot inventato.

### G90.1-03 — Urbanistica PRGC
La currentness puntuale è bibliograficamente chiusa per gli 8 casi già verificati; gli altri Comuni restano nel regime best-available con limitazione già approvata.

Conseguenza editoriale: non trasformare la baseline di screening in prova generalizzata di vigenza urbanistica.

### G90.1-04 — Natura 2000
Il corpus fonti è sufficientemente strutturato per il registro, ma ruleset e classificazioni operative dipendono ancora dalla review/accettazione della Chat 3.12.

Conseguenza editoriale: nessun claim operativo definitivo prima dell'accettazione del relativo artifact scientifico.

### G90.1-05 — PGRA WFS
Resta il caveat già accettato sull'assenza di binding machine-readable WFS ↔ Delibera 12/2025.

Conseguenza editoriale: distinguere currentness normativa e lineage della geometria operativa.

## 5. Rapporto con Claude/QGIS

PASS.

Nessuna fonte corrente è sostenuta esclusivamente dalla baseline storica Claude/QGIS. Il materiale storico è stato usato solo come pista di recupero, coerentemente con CLAUDE_BASELINE_EDITORIAL_USE_v01.md.

## 6. Decisione editoriale

**Chat 90.1: ACCEPTED_WITH_DOCUMENTED_GAPS.**

Il quality gate tecnico PASS_WITH_DOCUMENTED_GAPS proposto dalla chat figlia è confermato.

Non è richiesta escalation metodologica alla Chat 0.2 per i gap sopra, perché non introducono nuove scelte progettuali: restano vincoli di tracciabilità e formulazione editoriale.

## 7. Impatto sui workstream successivi

- Chat 90.2 può partire immediatamente.
- Chat 90.3 può usare il registro 90.1 come base bibliografica, ma la stabilizzazione delle bozze resta dipendente anche dalla lineage verificata prodotta dalla 90.2.
- I capitoli PARTIAL legati a Light, urbanistica, PGRA e Natura 2000 devono preservare i caveat sopra.
- Il registro fonti resta incrementale e dovrà essere aggiornato quando nuove fonti entrano in artifact ACCEPTED/FROZEN.

## 8. Git

Commit 90.1 revisionati:
- 6a2e3bb57c61bbb0db7fec8b2ddd12a46247625e — normalize external source register;
- 7dd96a3522260b8eea6fc55f707a339cea3a88e7 — handoff external source review.

I commit sono stati integrati con fast-forward nel branch editoriale parent chat-90.0-relation-architecture.

## 9. Prossimo passo

Avviare Chat 90.2 — Matrice di tracciabilità interna usando DISPATCH_CHAT_90.2_TRACEABILITY_v01.md.

Chat 90.1 può essere riaperta solo per aggiornamenti incrementali quando nuove fonti diventano effettivamente rilevanti o quando uno dei gap di lineage viene risolto.

