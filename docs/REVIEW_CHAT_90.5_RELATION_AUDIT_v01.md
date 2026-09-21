# REVIEW — Chat 90.5 — Audit stralci relazione e integrazione MODEL_v2

**Reviewer:** Chat 0.2 — Chat Madre 5 HUB
**Data:** 2026-09-21
**Esito:** PASS WITH FACTUAL CORRECTION APPLIED
**Effetto governance:** nessuna nuova metodologia approvata

## 1. Controlli indipendenti

Confermati:
- matrice audit = 114 claim;
- status: KEEP 55, ADAPT 18, SUPERSEDED 16, NEW_INFORMATION 19, CONFLICT 2, DUPLICATE 3, EDITORIAL_ONLY 1;
- claim_id univoci;
- campi obbligatori valorizzati;
- queue = 20 elementi;
- git diff check PASS;
- nessuna modifica autonoma a governance/DQ/FROZEN.

La separazione claim-by-claim è metodologicamente corretta e impedisce di importare in blocco formulazioni storiche o nuove scelte non approvate.

## 2. Findings confermati

Confermati come corretti:
- BESS obbligatorio = modifica sostanziale della definizione Fase 1 e non requisito corrente;
- elettrolizzatore obbligatorio = conflitto con F1-D6/DEC-0011;
- pesi 1–5, min-max e somma pesata = metodologia pendente;
- cinque macro-aree, uno-per-area, top-k e distanza minima 10 km = configuration choices/requisiti pendenti;
- 10 km tra Hub è distinto dai 10 km AFIR dalla TEN-T exit;
- routing OSM/TEN-T storico correttamente riallineato alle baseline già validate;
- verifiche proprietà/accesso locale/connessione reale restano post-model secondo rebaseline.

## 3. AFIR — verifica indipendente

Confermati sul Regolamento (UE) 2023/1804 consolidato:
- EV lungo TEN-T: rete o entro 3 km driving distance dalla nearest exit;
- H2 lungo TEN-T: rete o entro 10 km driving distance dalla nearest exit;
- entro 31/12/2030 sulla TEN-T core: H2 pubblico con massimo 200 km tra stazioni;
- stazioni progettate per capacità cumulativa minima 1 t/giorno;
- almeno un dispenser 700 bar.

L'audit applica correttamente questi fatti senza trasformarli automaticamente in hard universali dei cinque Hub.

## 4. Correzione Monfalcone applicata dalla review

La formulazione originaria della Chat 90.5 trattava 400 kg H2/giorno come singolo dato tecnico verificato.

La review ha trovato una discrepanza tra fonti pubbliche:
- NAHV Testbed Catalogue, maggio 2025: 400 kg H2/giorno di produzione;
- pagina ufficiale APT EcoMove corrente: 453 kg H2/giorno di produzione massima e circa 300 kg H2/giorno di capacità media di rifornimento;
- IIT Hydrogen: 400 kg/giorno di capacità per il progetto in realizzazione.

La correzione è stata applicata a:
- RELATION_CLAIM_AUDIT_MATRIX_v01.csv;
- RELATION_NEW_INFORMATION_QUEUE_v01.csv;
- RELATION_INTEGRATION_RECOMMENDATIONS_v01.md;
- CLAUDE_PIPELINE_REQUIREMENTS_INPUT_v01_PROPOSED.md;
- HANDOFF_CHAT_90.5_RELATION_AUDIT_v01.md.

Regola risultante:
non esiste ancora un singolo valore canonico di capacità H2 da usare nel modello. Conservare fonte, data e semantica e, se AFIR diventa operativo, validare specificamente la capacità cumulativa di rifornimento.

## 5. Stato Monfalcone

Confermato:
- progetto APT Gorizia a Monfalcone;
- area industriale Lisert / via Consiglio d'Europa;
- elettrolizzatore e impianto produzione/distribuzione;
- 2 dispenser 350 bar + 1 dispenser 700 bar;
- fonti 2025-2026 descrivono realizzazione/cantiere;
- operatività/commissioning non dimostrata alla data della review.

Monfalcone è quindi informazione di contesto verificata, non copertura AFIR automaticamente acquisita e non uno dei cinque Hub automaticamente selezionato.

## 6. Esito sugli artifact

Gli artifact Chat 90.5 sono ACCEPTED come:
- audit documentale;
- supporto alla relazione;
- coda di nuove informazioni/decisioni;
- base controllata per costruire il futuro prompt Claude.

Questa accettazione NON rende ACCEPTED:
- BESS obbligatorio;
- elettrolizzatore obbligatorio;
- scoring 1–5/min-max/somma pesata;
- macro-aree;
- uno-per-area;
- top-k;
- minimo 10 km tra Hub;
- ruolo operativo AFIR;
- ruolo modellistico di Monfalcone.

## 7. Prossimo passo

Prima del prompt Claude finale, Chat 0.2 deve portare all'utente le decisioni sostanziali necessarie e aggiornare il pacchetto input solo dopo approvazione.

Procedere per decisioni separate, evitando un'approvazione omnibus.
