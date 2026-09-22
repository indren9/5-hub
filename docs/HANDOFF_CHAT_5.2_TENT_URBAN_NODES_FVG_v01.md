# HANDOFF — Chat 5.2 — Delimitazione nodi urbani TEN-T FVG

**Chat:** 5.2 — Delimitazione nodi urbani TEN-T FVG  
**Regia:** Chat 0.2 — Chat Madre 5 HUB  
**Data:** 2026-09-22  
**Stato operativo:** PASS tecnico / REVIEW metodologica  
**Classificazione:** `NO_LEGAL_SPATIAL_BOUNDARY_IDENTIFIED`  
**Artifact commit:** `a4f8ad3` — `docs(tent): verify FVG urban-node boundary status`

## 1. Obiettivo

Determinare se i nodi urbani TEN-T di Trieste e Udine dispongano, al 22/09/2026, di una delimitazione territoriale ufficiale utilizzabile per formalizzare il configuration constraint AFIR H2 del MODEL_v2.

Il lavoro ha distinto:
- definizione giuridica TEN-T;
- copertura LAU per reporting/data collection;
- geometria tecnica TENtec;
- eventuale proxy operativo.

Nessun proxy è stato introdotto.

## 2. Risultato principale

Per **Trieste** e **Udine** la ricerca conclude:

`NO_LEGAL_SPATIAL_BOUNDARY_IDENTIFIED`

Entrambi sono nodi urbani TEN-T formalmente identificati, ma non è stata individuata nelle fonti primarie verificate una superficie ufficiale già utilizzabile come confine giuridico del requisito AFIR H2.

Il Comune capoluogo non è stato assunto come nodo urbano.

## 3. Evidenze decisive

### Regolamento (UE) 2024/1679

- art. 3(6): il nodo urbano è definito funzionalmente come area urbana con infrastrutture TEN-T e connessioni regionali/locali;
- art. 40: il nodo comprende infrastruttura TEN-T e punti di accesso;
- art. 40(2): l'Allegato II elenca le **città al centro** dei nodi;
- Allegato II: Trieste e Udine sono entrambe marcate come urban nodes;
- nessuna di queste disposizioni fornisce il perimetro territoriale dei due nodi.

### AFIR — Regolamento (UE) 2023/1804

L'art. 6(1) richiede entro il 31/12/2030 almeno una stazione H2 accessibile al pubblico in ciascun nodo urbano.

La norma stabilisce l'obbligo, ma non fornisce una geometria del nodo.

### Regolamento di esecuzione (UE) 2026/1554

Introduce una copertura geografica per LAU:
- una o più LAU per nodo;
- confini coincidenti con le LAU selezionate;
- assegnazione univoca;
- elenco nazionale da inviare entro 31/12/2026.

La regola è espressamente riferita alla **copertura geografica dei dati raccolti ai fini del regolamento di reporting sulla mobilità urbana**.

Non è stata trovata una disposizione che renda automaticamente questa copertura LAU il confine AFIR H2.

## 4. Stato specifico Trieste / Udine

### Trieste
- nodo urbano TEN-T: VERIFICATO;
- confine legale territoriale AFIR: NON IDENTIFICATO;
- composizione LAU ufficiale pubblicata al cut-off: NON IDENTIFICATA;
- geometria TENtec pubblica verificata: POINT;
- proxy introdotto: NO.

### Udine
- nodo urbano TEN-T: VERIFICATO;
- confine legale territoriale AFIR: NON IDENTIFICATO;
- composizione LAU ufficiale pubblicata al cut-off: NON IDENTIFICATA;
- geometria TENtec pubblica verificata: POINT;
- proxy introdotto: NO.

## 5. TENtec technical check

Interrogazione diretta del servizio pubblico TENtec ArcGIS REST:
`https://webgate.ec.europa.eu/getis/rest/services/TENTec/tentec_public_services_ext/MapServer`

Esito:
- layer Urban Nodes ID 5: `esriGeometryPoint`;
- layer Urban Nodes ID 13: `esriGeometryPoint`;
- query layer 5 per `COUNTRY_CODE='IT'`: 50 feature.

Il punto TENtec è stato classificato come rappresentazione tecnica, non come perimetro legale.

## 6. Fonti

Fonti primarie/institutional registrate: **7**.

Registro:
`docs/TENT_URBAN_NODES_FVG_SOURCE_REGISTER_v01.csv`

Principali autorità:
- EUR-Lex / legislazione UE;
- Commissione europea / DG MOVE;
- TENtec;
- MIT.

## 7. File creati

- `docs/REVIEW_CHAT_5.2_TENT_URBAN_NODES_FVG_v01.md`
- `docs/TENT_URBAN_NODES_FVG_SOURCE_REGISTER_v01.csv`
- `docs/HANDOFF_CHAT_5.2_TENT_URBAN_NODES_FVG_v01.md`

Nessun dataset pesante creato.
OneDrive non modificato.
PROJECT_SOURCE_OF_TRUTH non modificato.
PROJECT_CONTROL_REGISTER non modificato.

## 8. Quality gate

Controlli eseguiti:
- fonti primarie UE/TENtec/MIT: PASS;
- Trieste separata: PASS;
- Udine separata: PASS;
- cut-off 22/09/2026 esplicito: PASS;
- distinzione legal definition / LAU reporting / TENtec geometry: PASS;
- source register: 7 record, 7 ID univoci, 0 URL mancanti, 0 fonti marcate non-primary;
- TENtec live geometry check: PASS;
- nessun buffer/proxy inventato: PASS;
- `git diff --check`: PASS;
- decisioni ACCEPTED/FROZEN modificate: NO.

**Quality gate Chat 5.2: PASS tecnico.**

La review resta metodologica e deve essere ricevuta dalla Chat 0.2.

## 9. Questione da riportare alla Chat Madre

La formalizzazione computazionale del requisito AFIR:
“almeno una HRS H2 in ciascun nodo urbano”
non dispone ancora di un confine giuridico spaziale identificato per Trieste/Udine.

La Chat 5.2 non risolve il gap con un proxy.

## 10. Opzioni da valutare in Chat 0.2

Senza assumere alcuna decisione:
1. mantenere il requisito urban-node AFIR non ancora computabile spazialmente;
2. monitorare la pubblicazione/comunicazione italiana delle LAU prevista entro il 31/12/2026;
3. dopo la pubblicazione LAU, verificare separatamente se una fonte UE/MIT ne estenda l'uso al requisito AFIR H2;
4. se necessario, chiedere chiarimento formale a DG MOVE/MIT;
5. usare un eventuale proxy solo dopo decisione esplicita dell'utente e qualificandolo come proxy, non come confine normativo.

## 11. Problemi aperti proposti

Proposta alla Chat 0.2, senza creazione autonoma nel registro:

**URBAN-NODE-AFIR-BOUNDARY-GAP**  
Per Trieste e Udine non è identificata al 22/09/2026 una delimitazione legale spaziale direttamente applicabile all'art. 6 AFIR. È in corso un processo distinto di definizione LAU per reporting con deadline 31/12/2026.

La Chat Madre valuterà se trasformare questa proposta in una ISS ufficiale.

## 12. Git

Artifact commit:
`a4f8ad3 docs(tent): verify FVG urban-node boundary status`

Il presente handoff viene committato separatamente alla chiusura della chat.

## 13. Prossimo passo raccomandato

Chat 0.2:
- review indipendente degli artifact;
- eventuale registrazione del gap in ISSUES;
- nessuna formalizzazione spaziale AFIR basata sul solo Comune o sui punti TENtec;
- riapertura quando emerge una fonte ufficiale aggiuntiva o la composizione LAU italiana.

**Stato finale Chat 5.2: PASS tecnico / REVIEW metodologica.**
