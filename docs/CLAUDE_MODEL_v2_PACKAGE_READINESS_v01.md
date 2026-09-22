# CLAUDE MODEL_v2 PACKAGE READINESS v01

**Data:** 2026-09-22
**Stato:** REVIEW — PROMPT/MANIFEST READY, FINAL ZIP BLOCKED

## 1. Esito

Il prompt operativo e il manifest minimale del package sono stati costruiti e verificati.

Il package ZIP finale **non è stato creato** perché il preflight fallisce correttamente sull'unico blocker sostanziale ancora aperto: l'universo candidati definitivo non è ancora materializzato/accettato nella versione prevista dopo la chiusura semantica urbanistica.

La snapshot candidata v01 esistente non viene usata come sostituto implicito: è tecnicamente valida ma resta REVIEW e può cambiare materialmente per la risoluzione delle categorie urbanistiche unresolved >= 8.000 m².

## 2. Struttura consolidata del package

Il manifest contiene 14 righe dati:
- 3 artifact candidati obbligatori ancora BLOCKING_PENDING;
- 11 artifact già bindati a sorgenti concrete e verificati con hash, inclusi i ruoli condivisi Heavy geometry / FVG boundary.

Materiale escluso intenzionalmente:
- baseline Claude storica;
- chat e governance completa;
- documenti metodologici interni;
- cache e raw source non necessari all'esecuzione;
- PDF/evidenze già tradotti in dati operativi;
- dataset ambientali non usati nello scoring corrente;
- output di presentazione non necessari;
- duplicati fisici del confine FVG.

## 3. Preflight corrente

Comando:
~~~text
python scripts/build_claude_model_v2_package_v01.py
~~~

Esito atteso e ottenuto:
~~~text
PACKAGE_PREFLIGHT=FAIL
~~~

Cause residue:
1. CANDIDATE_UNIVERSE_v02.gpkg non ancora presente e marcato BLOCKING_PENDING;
2. CANDIDATE_LINEAGE_v02.csv non ancora presente e marcato BLOCKING_PENDING;
3. machine QA v02 non ancora presente e marcato BLOCKING_PENDING.

Dopo la correzione del manifest PGRA, non risultano altri errori di presenza/hash sugli input già disponibili.

## 4. Controllo delle importanze

Il prompt contiene esattamente i sette campi da compilare manualmente:

~~~text
LIGHT = ____
HEAVY = ____
GRID = ____
LOG = ____
PGRA = ____
H2 = ____
COVERAGE = ____
~~~

Nessun valore, default o suggerimento numerico è assegnato.

Se almeno un campo resta vuoto, il prompt ordina alla pipeline di non calcolare Q(H) e di non dichiarare una cinquina selezionata.

## 5. Coerenza metodologica incorporata nel prompt

Sono trascritte direttamente:
- selezione di esattamente 5 poligoni candidati;
- sei criteri site-level LIGHT, HEAVY, GRID, LOG, PGRA e H2;
- aggregazione site-level tramite media dei 5 Hub;
- criterio di copertura territoriale D_COV / Z_COV;
- funzione obiettivo unica Q(H);
- assenza di un vincolo generale Hub-Hub di 10 km;
- separazione AFIR/TEN-T dallo scoring;
- proxy comunali Trieste e Udine dichiarate come assunzioni progettuali;
- regola H2 <=10 km stradali dalla nearest TEN-T exit ai fini della conteggiabilità AFIR;
- requisito massimo 200 km lungo TEN-T Core sul perimetro valutabile;
- trattamento Monfalcone/Lisert senza penalizzazione per il deficit di capacità;
- nessuna invenzione di pesi o dati mancanti.

## 6. Caveat computazionali già resi espliciti

- LIGHT: baseline Dirty FRLM operativa ma non canonica rispetto alla tesi.
- HEAVY: edge-flow 2030 da ricostruire deterministicamente dai path-flow; scenario con limiti di calibrazione locale.
- GRID: prossimità a CP-proxy, non capacità o fattibilità reale.
- LOG: caveat ZIMA / SITE_ID 25.
- PGRA: area-weighted con classe peggiore nelle sovrapposizioni; AA/F solo flag.
- H2: quattro target core ammessi; spatialization auditabile necessaria quando mancano coordinate numeriche.
- TEN-T: il package FVG può non bastare a dimostrare la compliance dei tratti esterni/regionali del requisito 200 km.
- Universo candidati: nessuna run finale finché il dataset definitivo non è accettato.

## 7. Procedura di sblocco del package

Dopo l'accettazione dell'universo candidati definitivo:
1. bindare nel manifest i tre artifact candidati effettivi;
2. sostituire BLOCKING_PENDING con lo stato approvato;
3. inserire bytes e SHA-256 reali;
4. eseguire il preflight;
5. creare lo ZIP solo se il preflight restituisce PASS;
6. registrare hash dello ZIP e verificare contenuto/manifest.

Lo script di assembly è fail-closed: con un blocker o hash incoerente non crea il package.

## 8. Quality gate Chat 5.3

- prompt autosufficiente: PASS;
- file descritti operativamente: PASS;
- pesi lasciati vuoti: PASS;
- formule/constraint tradotti nel prompt: PASS;
- assunzioni distinte da requisiti: PASS;
- requisito AFIR 200 km esplicito: PASS;
- manifest minimale/motivato: PASS;
- preflight sugli artifact disponibili: PASS;
- package finale utile/tracciabile: NOT EXECUTED — BLOCKED BY CANDIDATE UNIVERSE;
- prompt/package coerenti: PASS condizionale al binding del candidato definitivo.

**Stato complessivo:** REVIEW / BLOCKED FOR FINAL ZIP, senza conflitto metodologico.
