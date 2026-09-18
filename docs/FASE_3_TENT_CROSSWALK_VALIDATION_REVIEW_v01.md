# FASE 3 â€” TEN-T FVG CROSSWALK VALIDATION REVIEW v01

**Chat:** 3.7 â€” Crosswalk TEN-T FVG e rilevanza delle uscite AFIR
**Data:** 2026-09-18
**Stato:** REVIEW tecnico-operativo
**Regia metodologica:** Chat Madre 5 HUB
**Branch:** `chat-3.7-tent-crosswalk`

## 1. Mandato e perimetro

Il mandato Ã¨ costruire il crosswalk route-level completo e verificabile tra la rete stradale TEN-T vigente in Friuli Venezia Giulia e le strade reali FVG, distinguendo Core, Extended Core e Comprehensive; quindi verificare se esista almeno un tratto TEN-T FVG privo di vere rampe/svincoli e caratterizzato da intersezioni ordinarie a raso tale da rendere materialmente rilevante il problema interpretativo della â€œnearest TEN-T exitâ€ previsto dallâ€™AFIR.

FASE 1 e FASE 2 restano PASS / CLOSED / FROZEN. Nessuna decisione metodologica sostanziale viene chiusa da questa chat. Non sono stati costruiti candidati, distanze candidatoâ€“TEN-T o `TENT_EXIT_SET_v01`.

## 2. Fonte TEN-T corrente autorevole

Ãˆ stato individuato e materializzato il servizio pubblico corrente DG MOVE / TENtec:

`https://tentec.transport.ec.europa.eu/api/public/gis/TENT_Regulation_2024/MapServer`

Il servizio dichiara esplicitamente il Regolamento (UE) 2024/1679 e separa le strade nei tre livelli correnti:
- layer 8 â€” Core;
- layer 9 â€” Extended Core;
- layer 10 â€” Comprehensive.

Questa fonte supera il limite del servizio TENtec legacy usato in Chat 3.3, che esponeva soltanto Core/Comprehensive. OSM non Ã¨ stato utilizzato per stabilire appartenenza o classe TEN-T.

## 3. Metodo del crosswalk

Sono stati interrogati i tre layer stradali correnti per lâ€™Italia nel bounding box FVG. La classificazione esclusiva Ã¨ stata ottenuta rispettando la gerarchia dei layer: una feature giÃ  presente nel livello superiore non viene ricontata come â€œcomprehensive-onlyâ€.

Per verificare che le sezioni ufficiali intersechino materialmente il territorio FVG e identificare la strada reale corrispondente, le geometrie TENtec sono state campionate ogni 1 km e confrontate con il grafo stradale regionale FVG giÃ  materializzato in Chat 3.3.

La soglia `<=100 m` usata nello script Ã¨ **esclusivamente un parametro tecnico di QA del crosswalk geometrico**. Non Ã¨ una soglia di snap del modello, non Ã¨ un requisito AFIR, non Ã¨ una regola di routing e non costituisce una decisione metodologica futura.

Artifact:
`05_intermediate_outputs\F3_CHAT_3_7\TENT_FVG_ROUTE_CROSSWALK_v01.csv`

SHA-256:
`1AAAAC6EB9E74CF0C86BD6BB31FBF2FD6390547956D5148F958477A54EADFEBF`

## 4. Risultato route-level corrente FVG

Il crosswalk corrente contiene **11 sezioni TENtec che intersecano materialmente il FVG**:

| Livello esclusivo | Sezioni | Strade FVG |
|---|---:|---|
| CORE | 9 | A4, A23, RA13, RA14, A/SS202 |
| EXTENDED CORE | 0 | nessuna |
| COMPREHENSIVE-only | 2 | A28 |
| **Totale** | **11** | |

Dettaglio:
1. CORE â€” OID 999 â€” Palmanova (J. A4/A23) â†” Sistiana-Visogliano â€” A4.
2. CORE â€” OID 2416 â€” Sistiana-Visogliano â†” Villa Opicina (J. RA13/RA14) â€” RA13.
3. CORE â€” OID 4550 â€” Udine â†” Tarvisio â€” A23.
4. CORE â€” OID 3632 â€” Palmanova (J. A4/A23) â†” Udine â€” A23.
5. CORE â€” OID 472 â€” Villa Opicina â†” Padriciano (Trieste porto R13) â€” RA13.
6. CORE â€” OID 862 â€” Rabuiese â†” Padriciano (Trieste porto R13) â€” A/SS202.
7. CORE â€” OID 4504 â€” Fernetti â†” Villa Opicina â€” RA14.
8. CORE â€” OID 370 â€” Palmanova â†” Portogruaro â€” A4.
9. CORE â€” OID 3640 â€” Tarvisio â†” confine IT/AT â€” A23.
10. COMPREHENSIVE-only â€” OID 1508 â€” Conegliano â†” Schiavoi, quota FVG â€” A28.
11. COMPREHENSIVE-only â€” OID 2725 â€” Schiavoi â†” Portogruaro, quota FVG â€” A28.

Il layer Extended Core corrente non restituisce alcuna sezione stradale materialmente sovrapposta al FVG.

## 5. Audit morfologia accessi

Artifact:
`05_intermediate_outputs\F3_CHAT_3_7\TENT_FVG_EXIT_RELEVANCE_AUDIT_v01.csv`

SHA-256:
`8FDCA0E64B4A3DB24E4184412E7FC3175C650D371A0633E8B5FDC54B7D34D1A6`

Esito per asse:
- **A4 CORE:** TENtec = Motorways; rete gestita come autostrada con svincoli; nessun caso ordinario a raso rilevato.
- **A23 CORE:** TENtec = Motorways; rete autostradale con uscite/svincoli; nessun caso ordinario a raso rilevato.
- **RA13 CORE:** TENtec = Rural road with separate directions; documentazione ANAS descrive il tratto attraverso svincoli e contesto autostradale/interconnesso; supporto OSM frozen non evidenzia accessi ordinari diretti a raso.
- **RA14 CORE:** stesso esito: innesto/svincoli e morfologia a livelli separati; nessun accesso ordinario a raso rilevato.
- **A/SS202 CORE:** ANAS descrive le sezioni attraverso svincoli; il caso â€œNuova Sopraelevata / Via della Rampaâ€ giÃ  isolato nello screening topologico Ã¨ una struttura link/rampa, non unâ€™intersezione ordinaria di mainline.
- **A28 COMPREHENSIVE-only:** Ã¨ lâ€™unico asse aggiunto dal crosswalk completo rispetto allo screening core/corridoi. Autostrade Alto Adriatico la identifica come autostrada Portogruaroâ€“Conegliano e pubblica lâ€™elenco degli svincoli autostradali; non introduce quindi un tratto a intersezioni ordinarie a raso.
- **EXTENDED CORE:** nessun tratto FVG corrente da auditare.

Il supporto OSM Ã¨ stato usato solo dove utile alla lettura geometrico-topologica e non per classificare TEN-T.

## 6. Rilevanza materiale di Q-METH-3.3-A

**Esito tecnico osservato:** nel dominio stradale TEN-T corrente FVG completamente crosswalkato non Ã¨ stato identificato alcun tratto in cui lâ€™accesso alla TEN-T debba essere rappresentato da unâ€™intersezione ordinaria a raso in assenza di una vera rampa/uscita/svincolo.

Di conseguenza, sulla base delle evidenze correnti, **il problema interpretativo Q-METH-3.3-A non risulta materialmente necessario per il dominio FVG osservato**.

Questa frase Ã¨ un risultato tecnico da sottoporre alla Chat Madre, non una chiusura metodologica autonoma. Non viene proposta nÃ© inventata una definizione alternativa di â€œnearest TEN-T exitâ€.

## 7. Limiti e cautele

1. Il crosswalk stabilisce appartenenza/classe TEN-T dalla fonte corrente DG MOVE/TENtec; il grafo FVG serve soltanto al riscontro della strada reale.
2. La verifica morfologica non autorizza ancora la costruzione del definitivo `TENT_EXIT_SET_v01`.
3. Le storiche 23 uscite Claude/QGIS non sono state promosse nÃ© riutilizzate come fonte corrente.
4. Il futuro calcolo di distanze stradali resta condizionato da ISS-0004: il routing diretto Light/Heavy non Ã¨ stato validato da Chat 3.3.
5. Una modifica futura della rete TEN-T o dei tracciati richiede nuova materializzazione/versione; non va sovrascritta questa evidenza.

## 8. Evidenze materializzate

Root:
`C:\Users\visen\OneDrive\UniversitÃ \UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_7`

Principali:
- `TEN_T\TENT_Regulation_2024_MapServer_metadata_20260918.json`
- subset GeoJSON Core / Extended Core / Comprehensive;
- metadati dei layer 8 / 9 / 10;
- `operator_evidence\ANAS_soccorso_stradale_unita_FVG_2026.pdf`
- `operator_evidence\Autostrade_Alto_Adriatico_network_20260918.html`
- `operator_evidence\MIT_elenco_strade_TEN_principali_2024.pdf`
- `evidence_manifest_v01.json`

Hash rilevanti:
- TENtec service metadata: `908E76799CCCEB2D1DE05A91CCCA2A5A236D37A349BA3F54D942B4B06A3493E4`
- Core GeoJSON: `B397912C6E3ED3D21FC4F4FBB4B7C383533DA2C947237D094DFA81CFAFF043BA`
- Extended Core GeoJSON vuoto: `C3311FCCB903EE2126AF2CF493ED98DAA5DAA7B7962F5344A25E397E46CBD3C4`
- Comprehensive GeoJSON: `1A44F76B37029B30FD14F08D89EE6079892995DD3FE4CC5ABC8C63BBFE9737DB`
- ANAS evidence: `D15EB8B9708809259B9AC4C1AB825010CAB105B8AA32B98115472755FDDE6FFC`
- Autostrade Alto Adriatico HTML: `22C6ED432B16739F3143FB325FC70BF3F3E9CFF3A609CA1EB942AD7CE9CA2B56`
- MIT evidence: `2C5BA39A7F22FEB273A25D4C43CC59C32C9CB96AEABB1195BD5E4AB39897F8C4`

## 9. Governance

Il PROJECT_CONTROL_REGISTER Ã¨ stato aggiornato solo con informazione tecnica:
- `F3_SRC_TENTEC_001` resta **REVIEW**;
- `ISS-0005` resta **OPEN**;
- la prossima azione richiede review indipendente della Chat Madre prima di qualsiasi chiusura.

Il PROJECT_SOURCE_OF_TRUTH non viene modificato dalla Chat 3.7.

## 10. Quality gate Chat 3.7

| Controllo | Esito |
|---|---|
| Dispatch e baseline vincolanti letti | PASS |
| Governance viva verificata | PASS |
| Fonte TEN-T corrente Reg. 2024/1679 identificata | PASS |
| Tre livelli Core / Extended Core / Comprehensive coperti | PASS |
| Crosswalk route-level FVG completo e tracciabile | PASS |
| Extended Core FVG esplicitamente verificato come assente | PASS |
| OSM escluso dalla classificazione normativa TEN-T | PASS |
| Morfologia accessi verificata per tutti gli assi FVG risultanti | PASS |
| A28 comprehensive-only verificata separatamente | PASS |
| Q-METH-3.3-A dimostrata/non dimostrata senza scelta implicita | PASS â€” non materialmente rilevante nel dominio osservato |
| Storiche 23 uscite non promosse | PASS |
| `TENT_EXIT_SET_v01` non costruito | PASS |
| Nessuna decisione metodologica/issue chiusa autonomamente | PASS |
| Artifact OneDrive + hash + script riproducibili | PASS |
| Review indipendente Chat Madre prima della chiusura ISS-0005 | REQUIRED / PENDING |

**Esito operativo Chat 3.7: PASS tecnico-operativo, soggetto a review della Chat Madre.**
Non equivale a chiusura di ISS-0005, non equivale a FASE 3 CLOSED/FROZEN e non autorizza la costruzione del definitivo exit set.
