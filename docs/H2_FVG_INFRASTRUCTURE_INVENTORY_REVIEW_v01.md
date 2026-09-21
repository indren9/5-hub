# H2 FVG INFRASTRUCTURE INVENTORY — REVIEW v01

**Chat:** 5.1 — Inventario infrastrutture H2 FVG  
**Regia:** Chat 0.2 — Chat Madre 5 HUB  
**Data di verifica:** 2026-09-22  
**Stato artifact:** REVIEW — technical inventory complete; methodological acceptance reserved to Chat Madre/user  
**Mandato:** docs/DISPATCH_CHAT_5.1_H2_INFRASTRUCTURE_INVENTORY_v01.md

## 1. Obiettivo e perimetro

Questo lavoro costruisce un inventario current-first, georiferibile e tracciabile delle infrastrutture H2 esistenti o concretamente programmate in Friuli Venezia Giulia, includendo produzione/elettrolisi, rifornimento, stoccaggio/distribuzione materialmente localizzabile e testbed/progetti H2 con sito fisico documentabile.

Non vengono definiti score, pesi, soglie di distanza o normalizzazione. La relazione con AFIR/TEN-T è conservata solo come attributo descrittivo; nessun record è dichiarato AFIR-compliant in automatico.

L'inventario è separato in:
- `CORE_H2_INFRA`: infrastruttura di produzione/rifornimento H2 fisica o finanziata con sito identificabile;
- `H2_TESTBED_CONTEXT`: testbed o infrastrutture di ricerca/industriali fisiche utili a descrivere l'ecosistema, ma non equivalenti automaticamente a un nodo H2 di produzione/rifornimento;
- `ANNOUNCED_CONTEXT`: annuncio fisicamente localizzabile ma non verificato come asset H2 realizzato.

## 2. Regola di classificazione dello stato

La tassonomia applicata è quella prescritta dal dispatch:
- `OPERATIONAL`: prova primaria corrente di esercizio/commissioning della componente H2;
- `UNDER_CONSTRUCTION`: fonte corrente che documenta lavori/realizzazione/implementazione fisica;
- `FUNDED_COMMITTED`: CUP/concessione/finanziamento o progetto formalmente committed, senza prova corrente sufficiente di lavori;
- `PLANNED_AUTHORIZED`: progetto pianificato con autorizzazione documentata ma non ricadente in classi più avanzate;
- `ANNOUNCED_UNVERIFIED`: intenzione/progetto annunciato, con stato fisico non verificato o sito finale non fissato;
- `UNKNOWN`: stato non determinabile.

Le date programmate o scadute non sono state usate come prova di entrata in esercizio. La semplice esistenza della stazione carburanti ospitante non prova che la componente H2 sia operativa.

## 3. Inventario finale

Sono censiti **10 record**:
- `UNDER_CONSTRUCTION`: 3;
- `FUNDED_COMMITTED`: 5;
- `ANNOUNCED_UNVERIFIED`: 2;
- `OPERATIONAL`: 0;
- `PLANNED_AUTHORIZED`: 0;
- `UNKNOWN`: 0.

Per scope:
- `CORE_H2_INFRA`: 5;
- `H2_TESTBED_CONTEXT`: 4;
- `ANNOUNCED_CONTEXT`: 1.

### 3.1 Core H2 infrastructure

| ID | Sito | Stato | Evidenza principale | Readiness spaziale |
|---|---|---|---|---|
| FVG_H2_001 | Hydrogen Hub Trieste | UNDER_CONSTRUCTION | NAHV 16/06/2026: advanced stage of construction; AU regionale 5 MW | HIGH |
| FVG_H2_002 | APT EcoMove Monfalcone/Lisert | UNDER_CONSTRUCTION | FVG Energia 22/07/2026: infrastruttura in realizzazione; APT current page | HIGH |
| FVG_H2_003 | Q8 Porpetto PNRR HRS | FUNDED_COMMITTED | OpenCUP ACTIVE, CUP G42C22000860004; current Q8 site does not list H2 | MEDIUM_HIGH |
| FVG_H2_004 | SOLHX Manzano | FUNDED_COMMITTED | Decreto regionale 70970/2025, CUP D92C25000190003 | MEDIUM — municipality only |
| FVG_H2_005 | ABS Pozzuolo/Cargnacco | FUNDED_COMMITTED | Decreto regionale 70969/2025, CUP D62C25000260003; NAHV ABS site address | HIGH |

**Risultato current-first critico:** nessuno dei cinque record core dispone, alla data di verifica, di una prova primaria corrente sufficiente per essere classificato `OPERATIONAL`.

### 3.2 Capacità: nessuna conversione impropria

- Trieste: 5 MW elettrolizzatore; fino a 370 t H2/anno; 2 t di stoccaggio in sito. Sono tre grandezze distinte.
- Monfalcone: 1 MW elettrolizzatore; fino a 400 kg H2/giorno di produzione; 350/700 bar sono pressioni di erogazione, non capacità.
- ABS: 82,55 t/anno è il valore corretto nel decreto ai fini della quota di H2 rinnovabile prodotta con gli impianti addizionali asserviti; il decreto esplicita che 138 t/anno includeva anche energia GO da rete. Il valore non viene trasformato in nameplate universale.
- Faber: >300 L è volume d'acqua del recipiente composito e >=500 bar è pressione; non sono convertiti in massa H2 stoccata.

## 4. Verifiche richieste dal dispatch

### Monfalcone / Lisert
PASS. Il sito è identificato nella zona industriale di Monfalcone con accesso da via Consiglio d'Europa. APT documenta elettrolizzatore 1 MW, produzione/stoccaggio/rifornimento, tre dispenser e PV 1,67 MW. Fonti 2026 continuano a descrivere la componente H2 come in realizzazione/lavori avanzati. Classificazione: `UNDER_CONSTRUCTION`, non `OPERATIONAL`. Nessuna conformità AFIR è inferita.

### Trieste
PASS. Hydrogen Hub Trieste è autorizzato in via Carlo Errera; 5 MW elettrolisi, 4,85 MWp PV, fino a 370 t/anno e 2 t storage. NAHV il 16/06/2026 lo descrive in fase avanzata di costruzione. Classificazione: `UNDER_CONSTRUCTION`. La data attesa di completamento non viene usata come prova di commissioning.

### Porpetto
PASS WITH LIMITATION. OpenCUP mantiene ATTIVO il CUP G42C22000860004 per una stazione H2 PNRR lungo la Variante SP80. Il nuovo sito Q8 è fisicamente aperto, ma la pagina operatore corrente elenca carburanti/servizi senza H2. Classificazione della componente H2: `FUNDED_COMMITTED`, non operativa.

### NAHV in FVG
PASS WITH DECLARED LIMITATIONS. I testbed sono stati verificati e deduplicati per sito fisico:
- Testbed VIII Acegas e III Snam/Cubogas confluiscono nel record Trieste Hub;
- Testbed II ABS confluisce nel record ABS;
- Testbed IV Ferriere Nord resta record contestuale a Osoppo;
- Testbed XIII Faber resta record contestuale a Cividale;
- Testbed XII CTS resta `ANNOUNCED_UNVERIFIED` perché il sito finale HRS non risulta fissato;
- Testbed IX rete gas FVG non viene trasformato in un punto artificiale;
- Testbed XV: la componente APT confluisce in Monfalcone; la componente Trieste Trasporti non ha un sito finale fisico sufficientemente documentato per un record spaziale autonomo.

### PNRR / MASE / MIMIT / Regione FVG
PASS. Sono stati verificati:
- PNRR M2C2 I3.1: Hydrogen Hub Trieste;
- PNRR/MIT M2C2 I3.3: Porpetto e Monfalcone;
- Progetti Bandiera MASE + Regione: SOLHX e ABS finanziati; HYNEX e HYBIO ammessi ma senza agevolazione per esaurimento risorse e quindi non inseriti come siti committed;
- Accordo MIMIT/Invitalia/Regione sul più ampio programma ABS: non genera un secondo sito H2, essendo riferito allo stesso complesso industriale di Cargnacco e non costituendo da solo prova di una distinta infrastruttura H2;
- IPCEI/Fincantieri e altre iniziative tecnologiche senza asset stazionario FVG fisicamente dimostrato non sono state trasformate in siti.

## 5. False positive e casi da non sovrastimare

### Pontebba
Il comunicato regionale 2022 può essere letto superficialmente come se l'idrogeno fosse già parte dell'impianto. La comunicazione regionale 2024 parla invece di futura intenzione di dotarsi della distribuzione H2; il sito operatore corrente elenca diesel, HVO, benzina, CNG, LNG ed EV, ma non H2. Record mantenuto come `ANNOUNCED_UNVERIFIED`.

### Porpetto
L'apertura del grande impianto Q8 non equivale all'apertura della componente H2 PNRR. I due fatti sono separati nel dataset.

### Date-obiettivo
Le scadenze 30/06/2026 o altre date previsionali non sono state usate per avanzare automaticamente lo stato a `OPERATIONAL`.

## 6. Georeferenziazione e qualità localizzazione

Il dataset conserva `LOCATION_TEXT`, `LOCATION_PRECISION`, `LOCATION_CONFIDENCE` e `LOCATION_SOURCE_ID`. Le coordinate numeriche sono riportate solo quando una fonte istituzionale esplicita le fornisce; non sono state inventate tramite geocoding non tracciato.

Readiness:
- HIGH: Trieste Hub, Monfalcone, ABS, Ferriere Nord, Faber, H2SmartCampus, Pontebba;
- MEDIUM_HIGH: Porpetto, con corridoio/sito PNRR fisicamente identificabile;
- MEDIUM: SOLHX, perché la concessione è certa ma la localizzazione recuperata è solo a livello comunale;
- LOW: CTS, perché Brugnera è la sede/leader e non il sito finale HRS.

**Gap bloccante per una futura distanza site-to-site:** SOLHX richiede il recupero del lotto/indirizzo/coordinate definitive; CTS non è utilizzabile come target spaziale fino alla fissazione del sito.

## 7. Raccomandazione dati alla Chat Madre

Senza decidere formula, soglie o peso:
- Trieste, Monfalcone, Porpetto e ABS hanno evidenza sufficiente per entrare in una baseline fattuale di infrastrutture H2 esistenti/programmate con localizzazione utilizzabile a scala regionale, mantenendo lo stato corrente;
- SOLHX ha status/funding sufficientemente solidi, ma non deve essere usato in calcoli di distanza puntuali finché la localizzazione non viene raffinata oltre il Comune di Manzano;
- Ferriere Nord, Faber e H2SmartCampus sono utili come contesto/testbed e non devono essere assimilati automaticamente a stazioni/impianti core;
- Pontebba e CTS devono restare separati come `ANNOUNCED_UNVERIFIED`.

Questa è una raccomandazione di qualità del dato, non una decisione metodologica sul futuro criterio H2.

## 8. QA e riproducibilità

Controlli minimi previsti/eseguiti tramite `scripts/qa_h2_inventory.py`:
- ID univoci e pattern `FVG_H2_NNN`;
- stato appartenente all'enum del dispatch;
- `VERIFIED_ON = 2026-09-22`;
- fonte primaria presente e risolta nel source register;
- localizzazione testuale sempre valorizzata;
- coordinate numeriche complete a coppie e in range quando presenti;
- separazione esplicita tra potenza elettrolizzatore, capacità di produzione, rifornimento, stoccaggio e altre capacità;
- duplicati di nome/comune;
- conteggi per stato, tipo e scope;
- controllo specifico che `ANNOUNCED_UNVERIFIED` non venga confuso con asset core utilizzabile.

Artifact:
- `data/interim/H2_FVG_INFRASTRUCTURE_INVENTORY_v01.csv`
- `docs/H2_FVG_SOURCE_REGISTER_v01.csv`
- `docs/H2_FVG_INFRASTRUCTURE_INVENTORY_REVIEW_v01.md`
- `scripts/qa_h2_inventory.py`
- `logs/H2_FVG_INFRASTRUCTURE_INVENTORY_QA_v01.txt`

## 9. Limiti aperti

1. SOLHX: recuperare fonte primaria con sito/particella/indirizzo definitivo.
2. Porpetto: cercare eventuale atto corrente che documenti avvio lavori/commissioning specifico H2; il CUP attivo non basta.
3. Monfalcone: aggiornare a `OPERATIONAL` solo dopo evidenza primaria di commissioning/esercizio H2.
4. Trieste: aggiornare a `OPERATIONAL` solo dopo evidenza primaria di commissioning/esercizio.
5. CTS/Trieste Trasporti: mantenere fuori dai target spaziali finché non esiste sito definitivo.
6. Nessuna dichiarazione AFIR-compliant è prodotta da questa chat.

