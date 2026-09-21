# RELATION INTEGRATION RECOMMENDATIONS v01

**Chat:** 90.5 — Audit stralci relazione e integrazione MODEL_v2
**Data:** 2026-09-21
**Stato:** REVIEW INPUT — AUDIT ONLY
**Autorità:** nessuna modifica di governance; decisioni sostanziali riservate all'utente / Chat 0.2

## 1. Esito sintetico

Gli stralci contengono una base metodologica in larga parte compatibile con MODEL_v2, ma mescolano tre epoche diverse: principi ancora validi, formulazioni superate dalla re-baseline del 21/09/2026 e nuove scelte non ancora approvate.

La regola operativa è quindi: **non importare il testo in blocco**. Usare la matrice `RELATION_CLAIM_AUDIT_MATRIX_v01.csv` come filtro claim-by-claim.

Elementi che possono essere integrati subito sono solo quelli classificati `KEEP` e, per i fatti esterni, quelli verificati con caveat espliciti. Gli elementi `ADAPT` devono essere riscritti. `SUPERSEDED` e `CONFLICT` non devono essere usati come metodologia corrente. `NEW_INFORMATION` entra nella coda decisionale o informativa e non diventa automaticamente baseline.

## 2. Cosa integrare subito

### 2.1 Identità funzionale dell'Hub

- Esattamente cinque Hub/poligoni come output strategico del modello.
- Ogni Hub integra **H2 pubblico** e **ricarica DC pubblica**.
- Il modulo EV deve poter servire **Light e Heavy**.
- FER fisica in sito non è obbligatoria.
- H2 rinnovabile/certificato non è requisito universale del nucleo minimo.
- Il modello non predefinisce l'architettura H2; tube trailer, pipeline o elettrolisi in sito contano solo se generano requisiti territoriali rilevanti.
- Biocarburanti e altri vettori restano opzionali.

**Non integrare come obbligatori BESS ed elettrolizzatore.** La relazione li presenta come componenti necessarie, ma ciò modificherebbe la Fase 1 FROZEN; per l'elettrolizzatore esiste inoltre un conflitto diretto con F1-D6/DEC-0011.

### 2.2 Universo candidati

Usare direttamente DQ-01 / DEC-0065, senza la formulazione generica dello stralcio:

- urbanistica ufficiale best-available current-first;
- CER/Mosaicatura PRG 2018 solo fallback storico dichiarato;
- classi generatrici G1–G5;
- multipart disconnessi splittati;
- nessun dissolve/merge generalizzato;
- canonicalizzazione guidata da identità e lineage;
- superficie minima HARD = **8.000 m² lordi** dopo repair/split;
- candidate_id stabile, versioning, geometry_hash e QA deterministico.

La precedente formulazione secondo cui la superficie minima fosse ancora da definire è superata.

### 2.3 Sequenza del MODEL_v2

È corretto mantenere la sequenza: universo → contratto criteri → valori raw/QA → trasformazioni → pesi/score individuale → contratto della cinquina → selezione → robustness → freeze/relazione.

È altresì corretto dichiarare che il ranking individuale **non** determina automaticamente la cinquina finale.

### 2.4 Routing, Light/Heavy e TEN-T

Il testo sul routing deve essere aggiornato. Non è più vero che l'uso operativo di OSM nel 5 HUB sia ancora da scegliere/validare ex novo.

Baseline corrente:
- Light: riuso macro di `G_OSM_operativo`, `Gamma_OSM` e `OD_PATH_SYSTEM_OSM` FROZEN secondo DEC-0054/DEC-0055;
- Heavy: riuso della baseline Heavy 6.0 / Speth-ETISplus secondo DEC-0055;
- il grafo regionale FVG può restare supporto geometrico, ma non è la rete di routing di produzione;
- accessibilità locale definitiva, sagome/manovre e legalità del singolo accesso sono post-model salvo futura operazionalizzazione GIS approvata.

Il crosswalk TEN-T è già validato: 11 sezioni ufficiali aggregate in 6 assi FVG, con 9 CORE, 0 EXTENDED CORE e 2 COMPREHENSIVE-only. La validazione non va descritta come attività ancora da completare.

### 2.5 Ambiente e territorio

Possono essere integrati i principi già coerenti con le DEC correnti:

- nessun tematismo diventa HARD o punteggio per semplice presenza/intersezione;
- PGRA: nessuna esclusione automatica per sola pericolosità/allagabilità;
- PAI vigente come riferimento normativo principale per frane; Catasto Frane/IFFI come supporto;
- Natura 2000: pre-screening/flag, nessuna esclusione o penalizzazione automatica per sola distanza/intersezione, nessun `VINCA_PASSED` automatico;
- parchi/riserve: nessuna esclusione automatica per sola intersezione;
- prati stabili: mantenere `DEROGA_REQUIRED`; **non** assumere già una penalizzazione;
- PPR: `PPR_CHECK_REQUIRED` nei casi prescrittivi; nessun punteggio PPR generico.

Qualsiasi HARD sostanziale o soft score ambientale resta DQ-02/DQ-03 (e, per trasformazioni/pesi, DQ-04/DQ-05).

### 2.6 Energia

Mantenere con enfasi la distinzione:

- prossimità a rete/cabina = proxy territoriale;
- non equivale a MW disponibili;
- aree convenzionali delle cabine primarie non equivalgono né a posizione fisica della cabina né a capacità;
- capacità, punto e costo reale di connessione sono post-model.

L'uso di una distanza da cabina/sottostazione come indicatore concreto è ancora una scelta DQ-02/DQ-03, non una baseline.

## 3. AFIR — testo verificato e modo corretto di integrarlo

Verifica effettuata il 21/09/2026 sul Regolamento (UE) 2023/1804, versione consolidata corrente al 08/01/2026, EUR-Lex.

Fatti normativi verificati:

- definizione «lungo la rete stradale TEN-T»: EV sulla rete o entro **3 km di distanza stradale** dall'uscita TEN-T più vicina; H2 sulla rete o entro **10 km di distanza stradale**;
- entro **31/12/2030**, lungo la **TEN-T core**, stazioni H2 accessibili al pubblico a distanza massima **200 km** tra loro;
- le stazioni dell'art. 6 devono essere progettate per una capacità cumulativa minima di **1 t/giorno** e avere almeno un dispenser a **700 bar**;
- il target 200 km dell'art. 6 riguarda la **core**; l'estensione alla comprehensive è oggetto di valutazione/review, non è il target corrente dell'art. 6.

Fonte primaria: https://eur-lex.europa.eu/eli/reg/2023/1804/2026-01-08

### Applicazione al MODEL_v2

Questi requisiti non devono essere trasformati automaticamente in hard filter di tutti i candidati. F1-D2/DEC-0007 stabilisce già che le specifiche AFIR H2 sono obbligatorie solo per gli Hub cui venga assegnata la funzione AFIR/TEN-T pertinente.

Restano quindi da decidere in DQ-02/DQ-03 e/o DQ-07/DQ-08: quali Hub debbano assolvere quella funzione, come rappresentare la copertura e se la conformità operi come hard del sito, vincolo della cinquina o altro ruolo.

Il **minimo 10 km tra i cinque Hub** è separato: nello stralcio è un requisito di commessa/utente, non una norma AFIR. È nuovo e richiede approvazione esplicita nel configuration contract.

## 4. Monfalcone Lisert — fatti verificati

Le fonti disponibili consentono di verificare:

- soggetto: APT Gorizia;
- localizzazione: nuova sede/area operativa nella zona industriale di Monfalcone Lisert, con accesso da via Consiglio d'Europa;
- progetto: impianto integrato di produzione e distribuzione H2 con elettrolizzatore, accumulo/compressione, stazione di rifornimento e fotovoltaico;
- capacità di produzione pubblicata: **400 kg H2/giorno**;
- configurazione dispenser: **2 × 350 bar** per autobus e **1 × 700 bar** per veicoli;
- stato recente: fonti 2025-2026 descrivono cantiere/lavori in fase avanzata o in realizzazione; **non è stata reperita evidenza sufficiente per dichiarare la stazione operativa/commissionata al 21/09/2026**.

Fonti principali:

- APT EcoMove: https://www.aptgorizia.it/gli-impianti-apt-ecomove/
- APT, lavori in fase avanzata 2026: https://www.aptgorizia.it/apt-news/assemblea-dei-soci-crescita-transizione-ecologica/
- NAHV Testbed Catalogue May 2025: https://www.nahv.eu/wp-content/uploads/2025/05/NAHV-testbeds-catalogue-may-2025.pdf
- Prefettura di Gorizia, cantiere 13/11/2025: https://prefettura.interno.gov.it/it/prefetture/gorizia/notizie/vigilanza-e-tutela-legalita-e-trasparenza-nei-lavori-pubblici
- FVG Energia 2026: https://prod-energia.regione.fvg.it/notizie/article/Mobilita-sostenibile-incontro-con-Apt-Goriziabr--sullo-sviluppo-delle-stazioni-multienergia/

### Cosa NON si può concludere

Non si può ancora trattare Monfalcone come stazione AFIR conforme o come copertura AFIR acquisita. I dati pubblicati dimostrano il dispenser 700 bar, ma i 400 kg/giorno sono dichiarati come **capacità di produzione**, non necessariamente come capacità cumulativa di rifornimento della stazione; inoltre restano da verificare commissioning, accessibilità pubblica e relazione stradale con la TEN-T core.

Quindi: Monfalcone è un **VERIFIED_NEW_FACT / infrastruttura di contesto**. Il modo in cui influisce su score, ridondanza/copertura o configurazione dei cinque Hub è una decisione metodologica successiva.

## 5. Cosa integrare riscrivendo (`ADAPT`)

1. **AFIR/TEN-T come ammissibilità:** mantenere la normativa, ma non pre-classificarla come hard universale; assegnare il ruolo nella futura decision queue.
2. **Accesso stradale:** usare accessibilità macro nel core se approvata; spostare verifica/progettazione definitiva dell'accesso locale post-model.
3. **PGRA e altri vincoli:** mantenere i principi normativi, ma non trasformare automaticamente il testo in hard/score prima di DQ-02/DQ-03.
4. **Energia:** mantenere il proxy; non promettere capacità reale o studio di connessione.
5. **Prati stabili:** mantenere `DEROGA_REQUIRED`, eliminare l'idea di una penalizzazione già presupposta.
6. **Monfalcone:** descrivere come progetto verificato in realizzazione avanzata; non come stazione già operativa o AFIR-compliant.

## 6. Cosa non usare come metodologia corrente

- BESS obbligatorio per tutti i cinque Hub.
- Elettrolizzatore obbligatorio per tutti i cinque Hub.
- OSM solo come supporto e rete operativa ancora da validare.
- Crosswalk TEN-T ancora da completare.
- Verifica urbanistica corrente completa di tutti i Comuni come prerequisito V2-1.
- Due diligence finale di proprietà, accesso locale, urbanistica definitiva e connessione reale come gate del freeze MODEL_v2.
- Penalizzazione automatica dei prati stabili.
- Qualunque formula/peso/normalizzazione o vincolo di cinquina non ancora approvato.

## 7. Nuove decisioni utente necessarie

Le seguenti questioni non vanno risolte dalla Chat 90.5:

1. se BESS debba diventare componente obbligatoria del nucleo minimo;
2. se l'elettrolizzatore debba diventare obbligatorio, modificando F1-D6;
3. ruolo esatto AFIR/TEN-T nel contratto criteri/configurazione;
4. metodo di scoring: pesi 1–5, min-max, somma pesata;
5. criteri specifici e formule raw, inclusa presenza/prossimità a infrastrutture H2;
6. cinque macro-aree e relativi criteri di bilanciamento;
7. vincolo di un Hub per macro-area;
8. preselezione top-10/top-5 prima dell'enumerazione;
9. distanza minima 10 km tra Hub come requisito di configurazione;
10. ruolo di Monfalcone Lisert nella copertura/configurazione.

Queste scelte ricadono principalmente in DQ-02…DQ-09 e devono restare `PROPOSED/PENDING` fino a decisione esplicita.

## 8. Elementi da verificare esternamente in futuro

- commissioning e accessibilità pubblica effettiva della stazione APT Monfalcone immediatamente prima dell'uso nel modello;
- capacità cumulativa di rifornimento della stazione, distinta dalla capacità di produzione di 400 kg/giorno;
- geolocalizzazione/accesso e distanza stradale dalla TEN-T core se Monfalcone viene candidato per copertura AFIR;
- eventuali modifiche normative AFIR successive alla versione consolidata EUR-Lex del 08/01/2026.

## 9. Regola per la futura pipeline Claude

La pipeline futura deve ricevere esclusivamente `CLAUDE_PIPELINE_REQUIREMENTS_INPUT_v01_PROPOSED.md` dopo review Chat 0.2. Il file distingue ciò che è già accettato, requisiti utente ancora da integrare, fatti esterni verificati, scelte metodologiche pendenti e contenuti superseded da non usare.

Questo documento **non approva** nessuna delle questioni pendenti e non costituisce prompt Claude finale.
