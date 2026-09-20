# REVIEW — Chat 3.11 — Baseline idrogeologica corrente PGRA + PAI

**Reviewer:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-20
**Mandato:** review indipendente del quality gate Chat 3.11
**Decisioni di riferimento:** DEC-0039, DEC-0040, DEC-0056
**Artifact specialistico:** `docs/FASE_3_PGRA_PAI_CURRENT_BASELINE_VALIDATION_REVIEW_v01.md`
**Handoff:** `docs/HANDOFF_CHAT_3.11_PGRA_PAI_v01.md`

## 1. Esito generale

**TECHNICAL_QUALITY_GATE = ACCEPTED_WITH_LIMITATIONS**

La review indipendente conferma il PASS tecnico della Chat 3.11.

La review separa due esiti:
- PGRA: chiusura procedurale tecnicamente giustificata secondo DEC-0039;
- PAI/frane: quality gate accettato, ma la chiusura procedurale richiede una scelta metodologica esplicita dell'utente perché DEC-0040 pone il PAI vigente completo come riferimento principale.

## 2. Controlli indipendenti eseguiti

La Chat Madre ha verificato direttamente:
- branch e commit specialistici;
- `git diff --check`;
- controllo sintattico Python;
- manifest OneDrive;
- hash del manifest e QA file;
- esistenza/integrità di tutti i file dichiarati nel manifest;
- conteggi WFS/DBF degli snapshot PGRA e regionali frane;
- numero e unicità dei link cartografici PAI indicizzati;
- fonti istituzionali correnti Regione FVG / Autorità di Distretto.

Esiti:
- file nel manifest: 41;
- missing/hash/size mismatch: 0;
- PGRA pericolosità: 187.230 WFS = 187.230 DBF;
- PGRA rischio: 132.840 WFS = 132.840 DBF;
- frane pericolosità regionale corrente: 2.904;
- perimetri frane regionali correnti: 6.919;
- punti IFFI: 6.568;
- link PDF PAI indicizzati: 627, tutti URL unici;
- ZIP materializzati: integrity PASS;
- `py_compile`: PASS.

## 3. PGRA

La currentness giuridica è sufficientemente dimostrata:
- Delibera n. 12 del 18-12-2025;
- avviso G.U. n. 16 del 21-01-2026;
- entrata in vigore delle mappe aggiornate dal 22-01-2026.

La documentazione ufficiale SIGMA conferma l'adozione in salvaguardia delle mappe aggiornate e segnala il sistema in aggiornamento per la consultazione dei tematismi.

La Chat 3.11 non ha trovato un identificatore machine-readable nelle capabilities/schema WFS che leghi formalmente le feature live a `PGRA2027` / Delibera 12/2025.

Questo è esattamente il caso di fallback già previsto da DEC-0039.

**DISPOSIZIONE TECNICA:**
- usare il WFS ufficiale live come geometria operativa corrente;
- mantenere il flag/caveat di version lineage;
- non dichiarare equivalenza formale non dimostrata;
- nessun hard filter automatico per classe.

**ISS-0006: RESOLVED PROCEDURALLY.**

## 4. PAI / frane

La Chat 3.11 ha correttamente ricostruito il quadro:
- il PAI continua a valere per pericolosità geologica e da valanga;
- la componente idraulica è stata ricondotta al PGRA;
- il corpus pertinente al FVG è multi-bacino;
- le cartografie e discipline ufficiali sono pubblicate dal Distretto;
- Regione FVG indica esplicitamente che i file vettoriali ufficiali PAI possono essere richiesti al Distretto.

Non è stato trovato un pacchetto pubblico unico, completo e current-versioned dei vettori PAI per il FVG.

Le viste regionali correnti `UTIL_TER` / IFFI sono utili per screening e contesto ma non sono dimostrate equivalenti al PAI vigente completo.

**TECHNICAL_STATUS PAI = READY_WITH_LIMITATIONS.**

## 5. Distinzione obbligatoria PAI / supporto regionale

Il seguente assetto è tecnicamente corretto:
- PAI ufficiale Distretto: riferimento normativo/cartografico;
- NTA e aggiornamenti: interpretazione normativa;
- `UTIL_TER:VW_DATA_FRANE_PERICOLOSITA`: supporto/pre-screening;
- `UTIL_TER:VW_DATA_FRANE_PERIMETRO`: inventario/supporto;
- `IRDAT:VW_FR_IFFI`: contesto/supporto;
- layer legacy `CATFRANE_*`: supporto storico/comparativo.

Nessuno dei layer regionali viene promosso implicitamente a PAI normativo completo.

## 6. Osservazione sulla pipeline

Lo script di acquisizione preserva gli snapshot esistenti e, se un file è già presente, lo riusa registrandolo nel manifest.

Questo è corretto per la riproducibilità dello snapshot di questa sessione, ma non forza un refresh futuro della fonte.

Per futuri aggiornamenti della baseline occorre:
- usare un nuovo timestamp/versione di output; oppure
- introdurre una modalità esplicita di refresh.

Questa osservazione non invalida il gate corrente.

## 7. Decisione metodologica finale sul PAI

**DEC-0058 — ACCEPTED.**

L'utente approva esplicitamente il fallback macro proposto dalla Chat 0.2. La Fase 3 non viene bloccata in attesa di un pacchetto vettoriale PAI ufficiale unico/completo/current-versioned richiesto al Distretto.

Assetto approvato:
1. cartografie e NTA ufficiali PAI restano il riferimento normativo/cartografico;
2. viste regionali correnti frane sono usate solo per pre-screening territoriale;
3. `CATFRANE_*` resta supporto/confronto e non viene promosso a PAI completo;
4. applicare `PAI_POINTWISE_CHECK_REQUIRED` ai candidati che sopravvivono allo screening / finalisti;
5. verificare puntualmente cartografia e disciplina PAI ufficiale prima della conferma finale del sito;
6. acquisire i vettori ufficiali dal Distretto solo se diventano necessari per automatizzare o risolvere casi specifici.

**ISS-0012 = RESOLVED PROCEDURALLY.**

La risoluzione non significa che il gap vettoriale sia scomparso: significa che il gap non è più un blocker della pianificazione macro perché viene gestito con controllo puntuale sui casi rilevanti.

## 8. Stato finale review

- Chat 3.11: ACCEPTED_WITH_LIMITATIONS
- ISS-0006: RESOLVED PROCEDURALLY
- ISS-0012: RESOLVED PROCEDURALLY
- Fase 4: NON APERTA

La review Chat 3.11 non lascia decisioni metodologiche residue su PGRA/PAI.
