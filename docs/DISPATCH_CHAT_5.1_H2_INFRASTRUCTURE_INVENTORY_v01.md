# DISPATCH â€” CHAT 5.1 â€” INVENTARIO INFRASTRUTTURE H2 FVG

**Progetto:** 5 HUB
**Chat:** 5.1 â€” Inventario infrastrutture H2 FVG
**Regia:** Chat 0.2 â€” Chat Madre 5 HUB
**Data:** 2026-09-22
**Stato:** DISPATCH / OPERATIVE
**Fase:** MODEL_v2 â€” V2-2 Contratto di criteri e indicatori

## 1. Obiettivo

Costruire un inventario verificato, georiferibile e tracciabile delle infrastrutture H2 esistenti o concretamente programmate in Friuli Venezia Giulia, con particolare attenzione a:

- elettrolizzatori / impianti di produzione di idrogeno;
- stazioni di rifornimento H2;
- infrastrutture di stoccaggio o distribuzione materialmente localizzabili, se rilevanti;
- progetti H2 con sito fisico identificabile e stato sufficientemente documentato.

L'inventario servirÃ  come base dati per il futuro criterio site-level di prossimitÃ /sinergia H2 del MODEL_v2.

La chat NON deve ancora definire formula di score, pesi, soglie o normalizzazione.

## 2. Principio metodologico

Non confondere:
- impianto operativo;
- impianto in costruzione;
- progetto finanziato/committed;
- progetto pianificato/autorizzato;
- semplice annuncio o idea progettuale.

Ogni record deve avere uno stato documentato e una fonte corrente.

Non usare una fonte secondaria quando Ã¨ disponibile una fonte primaria/ufficiale.

Non trasformare capacitÃ  di produzione, capacitÃ  di rifornimento e capacitÃ  nominale di progetto in grandezze equivalenti.

## 3. Classificazione minima richiesta

Per ogni infrastruttura/progetto censito produrre almeno:

- `H2_SITE_ID` stabile;
- nome;
- comune;
- indirizzo/localitÃ ;
- coordinate o geometria georiferibile;
- tipologia:
  - `ELECTROLYZER_PRODUCTION`
  - `REFUELING_STATION`
  - `STORAGE_DISTRIBUTION`
  - `INTEGRATED_H2_SITE`
  - altra tipologia motivata;
- stato:
  - `OPERATIONAL`
  - `UNDER_CONSTRUCTION`
  - `FUNDED_COMMITTED`
  - `PLANNED_AUTHORIZED`
  - `ANNOUNCED_UNVERIFIED`
  - `UNKNOWN`;
- data di verifica dello stato;
- soggetto promotore/gestore;
- capacitÃ  dichiarata e relativa unitÃ , se disponibile;
- natura della capacitÃ : produzione / rifornimento / stoccaggio / altra;
- tecnologia, se documentata;
- pressione di erogazione, se pertinente;
- accesso pubblico/privato, se pertinente;
- relazione con TEN-T / AFIR solo come attributo descrittivo, senza giudizio automatico di conformitÃ ;
- fonte primaria;
- fonte secondaria/cross-check, se utile;
- livello di qualitÃ /confidenza della localizzazione;
- note e limitazioni.

## 4. Fonti da privilegiare

Ordine indicativo:
1. Regione Autonoma Friuli Venezia Giulia;
2. Ministeri / PNRR / atti pubblici nazionali;
3. Commissione europea / CINEA / NAHV e documentazione progettuale ufficiale;
4. Comune / ente pubblico / autoritÃ  portuale / concessionario pubblico;
5. gestore/promotore ufficiale dell'impianto;
6. altre fonti istituzionali;
7. stampa o aggregatori solo come pista, mai come unica evidenza se la fonte primaria Ã¨ recuperabile.

La ricerca deve essere current-first alla data del 2026-09-22.

## 5. Elementi noti da verificare, non assumere

Verificare esplicitamente almeno:
- Monfalcone / Lisert;
- Trieste;
- Porpetto;
- eventuali altri testbed/progetti NAHV in FVG;
- eventuali progetti PNRR/MASE/MIMIT o regionali localizzati in FVG.

Monfalcone NON va automaticamente classificata come operativa o AFIR-compliant: verificare commissioning, accesso, capacitÃ  e stato corrente.

## 6. Output richiesti

Produrre nel repository almeno:

- `docs/H2_FVG_INFRASTRUCTURE_INVENTORY_REVIEW_v01.md`
- `data/interim/H2_FVG_INFRASTRUCTURE_INVENTORY_v01.csv` oppure percorso leggero equivalente coerente con l'architettura del repo;
- `docs/H2_FVG_SOURCE_REGISTER_v01.csv`
- `docs/HANDOFF_CHAT_5.1_H2_INFRASTRUCTURE_INVENTORY_v01.md`

Se dati o allegati pesanti devono essere materializzati, salvarli in OneDrive secondo l'architettura del progetto e registrarne il percorso.

## 7. Quality gate minimo

PASS solo se:
- ogni record ha una fonte verificabile;
- lo stato Ã¨ esplicito e non inferito oltre l'evidenza;
- le coordinate/localizzazioni sono tracciabili;
- duplicati e denominazioni alternative sono risolti;
- produzione, rifornimento e altre capacitÃ  non sono confuse;
- gli elementi `ANNOUNCED_UNVERIFIED` sono separati dagli asset concretamente utilizzabili;
- limiti e gap sono dichiarati;
- output e fonti permettono di ricostruire l'inventario.

Se non Ã¨ possibile stabilire uno stato corrente, usare `UNKNOWN` o `ANNOUNCED_UNVERIFIED`, non inventare.

## 8. Vincoli

NON:
- definire lo score H2;
- decidere quanti siti devono entrare nel criterio;
- attribuire pesi;
- fissare soglie di distanza;
- dichiarare conformitÃ  AFIR senza verifica completa;
- modificare decisioni ACCEPTED/FROZEN;
- usare il materiale Claude come fonte autorevole.

## 9. Handoff

L'handoff deve contenere:
- numero e nome chat;
- obiettivo;
- fonti consultate;
- inventario finale e conteggi per stato/tipologia;
- file creati/modificati e percorsi;
- controlli e relativo esito;
- commit Git;
- problemi aperti;
- raccomandazione alla Chat Madre su quali record siano sufficientemente solidi per una baseline del criterio H2.

La Chat Madre deciderÃ  successivamente se approvare la baseline e quale formula di prossimitÃ  applicare.
