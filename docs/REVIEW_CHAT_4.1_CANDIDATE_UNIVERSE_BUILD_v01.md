# REVIEW — Chat 4.1 — Candidate Universe Build v01

**Reviewer:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Esito:** TECHNICAL BUILD PASS / V2-1 NOT READY FOR ACCEPTANCE
**Decisione DQ-01:** invariata, ACCEPTED con DEC-0065

## 1. Controlli indipendenti superati

La Chat 0.2 ha verificato direttamente gli artifact e rieseguito i controlli principali.

Confermati:
- EPSG:6708 = RDN2008 / UTM zone 33N, CRS proiettato in metri;
- 3.993 candidati finali;
- 3.993/3.993 geometrie Polygon valide, non null e non empty;
- area minima candidato = 8.001,732 m²;
- 0 candidati con area < 8.000 m²;
- 5.125 esclusioni MIN_AREA_8000_NOT_MET, tutte realmente < 8.000 m²;
- massimo escluso per soglia = 7.994,464 m²;
- distribuzione G1–G5 e S1–S4 coerente con il report specialistico;
- 0 candidate_id duplicati;
- 0 geometry_hash duplicati;
- pytest indipendentemente rieseguito: 5/5 PASS;
- py_compile PASS;
- manifest: 10 artifact + 7 input = 17 entry;
- 17/17 file presenti con SHA-256 coerente;
- manifest SHA-256 = 1B36B52444D4B56C6FD23D66AB27956FB13A7B247EE2BE738B576A8BCCC02B40;
- source-gap table = 215/215 Comuni;
- S5 confermati: Preone, Stregna, Rivignano Teor, Treppo Ligosullo, Valvasone Arzene;
- 461 coppie con overlap positivo correttamente mantenute separate in assenza di identità logica documentata.

## 2. Blocker di completezza semantica

Il mapping contiene 703 combinazioni native con stato GENERATOR_CLASS_UNRESOLVED, pari a 3.933 feature sorgente e 4.016 parti post-repair.

La review ha verificato l'impatto potenziale dopo il gate di superficie:
- 1.128 parti unresolved hanno area >= 8.000 m²;
- interessano 70 Comuni;
- superficie lorda complessiva = 161.334.606,080 m².

Queste geometrie non sono marginali rispetto all'universo e possono cambiare materialmente cardinalità e distribuzione dei candidati.

DQ-01 stabilisce che le categorie ambigue non devono essere forzate e che il mapping deve essere risolto prima della generazione definitiva dell'universo.

Pertanto l'esclusione prudenziale delle categorie unresolved è corretta come comportamento temporaneo di REVIEW, ma i 3.993 candidati non possono ancora essere considerati universo definitivo/FROZEN.

## 3. Interpretazione

Non emerge un errore del motore di build né una nuova decisione metodologica.

Il problema è di data interpretation / semantic completeness:
- una sigla urbanistica non può essere classificata G1–G5 o esclusa solo dal codice se la semantica non è sufficientemente documentata;
- occorre consultare legenda/NTA o altra evidenza ufficiale già collegata alla fonte;
- dove la fonte dimostra una classe non generatrice, la riga va chiusa RESOLVED_EXCLUDED;
- dove dimostra una classe G1–G5, va mappata alla classe approvata;
- dove l'evidenza ufficiale resta insufficiente dopo ricerca documentata, il caso deve restare UNRESOLVED_MATERIAL e la sua incidenza deve essere quantificata.

## 4. Source gaps S5

I cinque Comuni S5 sono una limitazione dichiarata ma non un blocker automatico ai sensi di DQ-01: il contratto vieta di inventare geometrie e richiede di quantificare il gap.

Restano pertanto limitazione esplicita, salvo reperimento di una fonte ufficiale migliore in attività successive.

## 5. Overlap

Le 461 coppie con overlap positivo non sono un blocker di questa review.

DQ-01 vieta merge basati sulla sola sovrapposizione. La presenza di overlap deve restare tracciata; eventuale identità logica va dimostrata da lineage, non da una soglia geometrica introdotta ex post.

## 6. Esito

Chat 4.1:
**TECHNICAL BUILD PASS**

Artifact V2-1 v01:
**REVIEW / NOT READY FOR ACCEPTANCE OR FREEZE**

Blocker:
**chiusura semantica delle categorie unresolved materialmente rilevanti per l'universo**.

Non è richiesta una nuova decisione utente per eseguire questa remediation, perché deve applicare le classi G1–G5 già ACCEPTED senza introdurre nuove categorie o criteri.

## 7. Next step

Aprire Chat 4.2 — Chiusura mapping urbanistico unresolved.

La Chat 4.2 deve:
1. concentrarsi prioritariamente sulle combinazioni unresolved che generano almeno una parte >= 8.000 m²;
2. usare evidenza ufficiale di legenda/NTA/descrizione fonte;
3. non inferire la classe dal solo codice;
4. risolvere in G1–G5 o RESOLVED_EXCLUDED quando supportato;
5. mantenere UNRESOLVED_MATERIAL i casi realmente non determinabili;
6. rifare la build in nuova versione e quantificare l'effetto sul candidato universe;
7. non aprire DQ-02.

Il v01 attuale va preservato come review snapshot e non sovrascritto silenziosamente.
