# REVIEW CHAT 5.2 — TENT URBAN NODES FVG — CHAT MADRE

**Data:** 2026-09-22
**Chat reviewata:** 5.2 — Delimitazione nodi urbani TEN-T FVG
**Esito Chat Madre:** PASS / ACCEPTED AS EVIDENCE
**Classificazione:** `NO_LEGAL_SPATIAL_BOUNDARY_IDENTIFIED`

## 1. Esito

La Chat Madre recepisce come evidenza valida il risultato della Chat 5.2.

Per Trieste e Udine, separatamente:
- il ruolo di nodo urbano TEN-T è verificato;
- l'obbligo AFIR H2 relativo ai nodi urbani è verificato;
- non è stata identificata al cut-off 22/09/2026 una delimitazione territoriale ufficiale direttamente utilizzabile come confine giuridico per il test AFIR H2;
- il Comune capoluogo non può essere assunto automaticamente come nodo urbano;
- la geometria TENtec verificata è puntuale e non costituisce un perimetro;
- la copertura LAU prevista dal Reg. di esecuzione (UE) 2026/1554 è riferita al reporting/data collection e non è stata dimostrata come confine AFIR H2.

## 2. Conseguenza operativa

Il requisito AFIR «almeno una stazione H2 accessibile al pubblico in ciascun nodo urbano» resta normativamente rilevante ma, allo stato corrente, non è trasformabile in un test GIS territoriale normativamente fondato per Trieste/Udine.

Non viene introdotto alcun proxy implicito.

## 3. Governance

È aperta `ISS-0017` per tracciare il gap.

La questione non richiede una nuova DEC metodologica finché non emerge una fonte ufficiale aggiuntiva o l'utente non approva esplicitamente un proxy progettuale.

## 4. Condizioni di riapertura

Riaprire il tema se si verifica almeno uno dei seguenti eventi:
- pubblicazione della composizione LAU italiana per Trieste/Udine;
- chiarimento ufficiale UE/MIT sulla trasferibilità della delimitazione LAU al requisito AFIR H2;
- pubblicazione di un perimetro ufficiale specifico dei nodi urbani;
- risposta formale DG MOVE/MIT sul criterio territoriale applicabile.

## 5. Quality gate

- artifact Chat 5.2 presenti: PASS
- source register verificato: PASS
- fonti primarie/institutional: PASS
- nessun proxy inventato: PASS
- stato Git verificato: PASS
- `a4f8ad3` e `6d01c38` presenti in `origin/main`: PASS

**Esito finale:** PASS / ACCEPTED AS EVIDENCE / ISSUE OPEN.