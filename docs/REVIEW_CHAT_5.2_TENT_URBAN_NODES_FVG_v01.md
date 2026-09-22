# REVIEW CHAT 5.2 — DELIMITAZIONE NODI URBANI TEN-T FVG v01

**Chat:** 5.2 — Delimitazione nodi urbani TEN-T FVG  
**Regia:** Chat 0.2 — Chat Madre 5 HUB  
**Data di verifica:** 2026-09-22  
**Stato operativo:** REVIEW / evidenza pronta per decisione Chat Madre  
**Classificazione finale:** `NO_LEGAL_SPATIAL_BOUNDARY_IDENTIFIED`

## 1. Obiettivo

Determinare se, al 22/09/2026, i nodi urbani TEN-T di **Trieste** e **Udine** dispongono di una delimitazione territoriale ufficiale, corrente e giuridicamente utilizzabile per formalizzare il requisito AFIR H2.

Il mandato vieta di:
- assumere nodo urbano = Comune capoluogo;
- inventare buffer, centroidi o proxy metropolitani;
- confondere una geometria TENtec con una delimitazione giuridica;
- trasferire automaticamente una delimitazione usata per reporting/SUMP al requisito AFIR H2.

## 2. Conclusione sintetica

**No.** Nelle fonti primarie UE/TENtec/MIT verificate non è stata identificata, al 22/09/2026, una delimitazione territoriale ufficiale di Trieste o Udine che possa essere usata direttamente come confine giuridico del requisito AFIR H2.

Trieste e Udine sono entrambe formalmente nodi urbani TEN-T, ma:
1. il Regolamento (UE) 2024/1679 fornisce una definizione funzionale/infrastrutturale di nodo urbano, non un perimetro GIS o amministrativo;
2. l'Allegato II elenca le **città al centro** dei nodi urbani, tra cui Trieste e Udine, senza delimitazione territoriale;
3. il Regolamento di esecuzione (UE) 2026/1554 introduce una copertura geografica per LAU esclusivamente ai fini della raccolta/presentazione dei dati di mobilità urbana;
4. l'elenco italiano delle LAU per ciascun nodo deve essere comunicato alla Commissione entro il 31/12/2026 e non è stato reperito come pubblicato per Trieste/Udine alla data di cut-off;
5. il layer pubblico TENtec “Urban Nodes” verificato è puntuale (`esriGeometryPoint`), non poligonale.

## 3. Quadro giuridico TEN-T

### 3.1 Definizione del nodo urbano

Il Regolamento (UE) 2024/1679, art. 3(6), definisce il nodo urbano come un'area urbana nella quale elementi dell'infrastruttura TEN-T per passeggeri e merci, situati nell'area urbana e attorno ad essa, sono connessi con altri elementi TEN-T e con le infrastrutture del traffico regionale e locale, incluse le modalità attive.

Questa è una **definizione giuridica funzionale**. Non identifica:
- un confine amministrativo;
- un elenco di comuni;
- un poligono;
- una distanza radiale;
- una relazione automatica con il solo Comune capoluogo.

L'art. 40(1) specifica inoltre che il nodo comprende, in particolare, l'infrastruttura TEN-T nel nodo e i punti di accesso alla TEN-T, tra cui porti, aeroporti, stazioni ferroviarie, terminal autobus e terminal merci multimodali.

L'art. 40(2) precisa che l'Allegato II elenca le **città al centro di ciascun nodo urbano**. La formulazione non equivale a definire il nodo come territorio amministrativo della città elencata.

### 3.2 Trieste e Udine

Nell'Allegato II del Regolamento (UE) 2024/1679:
- **Trieste** è marcata come `URBAN NODE = X`; sono inoltre indicati aeroporto comprehensive, porto marittimo core, porto interno core e terminal ferroviario-stradale core (Fernetti);
- **Udine** è marcata come `URBAN NODE = X`.

Quindi l'identità giuridica dei due nodi è verificata; ciò non fornisce un confine territoriale.

### 3.3 Continuità normativa con AFIR

AFIR, Regolamento (UE) 2023/1804 art. 6(1), richiede entro il 31/12/2030 almeno una stazione H2 pubblicamente accessibile in ciascun nodo urbano.

Il testo AFIR originario rinvia alla precedente disciplina TEN-T. Il Regolamento (UE) 2024/1679, art. 68, abroga il Regolamento (UE) 1315/2013 e dispone che i riferimenti al regolamento abrogato siano intesi come riferimenti al Regolamento (UE) 2024/1679 secondo la tavola di concordanza.

Ne consegue che il requisito AFIR resta applicabile ai nodi urbani, ma la normativa TEN-T corrente non fornisce per Trieste o Udine una geometria territoriale utilizzabile direttamente per decidere se un sito ricade “nel nodo”.

## 4. Regolamento di esecuzione (UE) 2026/1554: LAU

Il Regolamento di esecuzione (UE) 2026/1554, adottato il 09/07/2026 ed efficace dal 30/07/2026, disciplina la raccolta e presentazione alla Commissione dei dati di mobilità urbana ai sensi dell'art. 41(2) TEN-T.

Il considerando 4 e l'art. 6 stabiliscono che:
- gli Stati membri definiscono la copertura geografica dei **dati raccolti** mediante Local Administrative Units (LAU);
- la copertura può comprendere una o più LAU;
- la copertura coincide con i confini delle LAU selezionate;
- ogni LAU è assegnata univocamente a un nodo urbano;
- il primo elenco dei codici LAU deve essere presentato entro il **31/12/2026**.

La clausola decisiva è il perimetro di scopo: l'art. 6(1) parla di copertura geografica dei dati raccolti per ciascun nodo urbano **“ai fini del presente regolamento”**.

### 4.1 Valore per questa chat

La composizione LAU è quindi una **delimitazione ufficiale di reporting/data collection**, non una disposizione che dichiara quei confini come confine legale generale del nodo urbano per ogni altra normativa.

Non è stato trovato nel Regolamento 2026/1554:
- un rinvio ad AFIR art. 6 che renda la composizione LAU il confine applicabile al requisito H2;
- un allegato con la composizione LAU di Trieste;
- un allegato con la composizione LAU di Udine.

Per l'Italia, il MIT chiarisce nelle proprie slide della Rete Nazionale Nodi Urbani che le LAU corrispondono ai comuni e ribadisce il termine del 31/12/2026. Questo non autorizza a presumere che la LAU di Trieste sia solo il Comune di Trieste o che la LAU di Udine sia solo il Comune di Udine: la norma consente una o più LAU per nodo e l'elenco concreto è una scelta nazionale da comunicare alla Commissione.

## 5. Stato italiano al 22/09/2026

La pagina MIT PUMS, aggiornata il 03/08/2026, documenta il Programma Nazionale di sostegno ai 50 nodi urbani italiani e il 5° incontro della Rete Nazionale dei Nodi Urbani del 22/07/2026.

La ricerca current-first su MIT, Commissione/DG MOVE e TENtec non ha restituito un elenco pubblico italiano dei codici LAU attribuiti specificamente a Trieste o Udine.

Il termine legale del 31/12/2026 non era ancora scaduto alla data di cut-off. L'assenza di un elenco pubblico reperito è quindi coerente con una procedura ancora in corso e non va colmata per inferenza.

## 6. Geometrie TENtec

È stato interrogato direttamente il servizio pubblico ufficiale ArcGIS REST di TENtec:

`https://webgate.ec.europa.eu/getis/rest/services/TENTec/tentec_public_services_ext/MapServer`

I layer denominati **Urban Nodes** verificati nel servizio pubblico (ID 5 e ID 13) dichiarano:
- `type = Feature Layer`;
- `geometryType = esriGeometryPoint`.

Il layer 5 restituisce 50 record con `COUNTRY_CODE = IT`, coerenti con i 50 nodi urbani italiani richiamati dal MIT.

Questa geometria è una **rappresentazione cartografica tecnica puntuale**. Non costituisce una superficie di appartenenza e non consente di testare “candidate polygon inside urban node”.

Non è stata identificata nel servizio pubblico verificato una geometria poligonale ufficiale dei nodi urbani di Trieste o Udine.

## 7. Matrice di classificazione

| Aspetto | Trieste | Udine | Valore per AFIR H2 |
|---|---|---|---|
| Nodo urbano TEN-T identificato legalmente | SÌ, Annex II | SÌ, Annex II | SÌ: obbligo AFIR rilevante |
| Definizione giuridica funzionale | SÌ, art. 3(6) | SÌ, art. 3(6) | Definisce il concetto, non il confine |
| Confine amministrativo = Comune capoluogo | NON STABILITO | NON STABILITO | NON UTILIZZABILE senza fonte |
| Composizione ufficiale LAU pubblicata | NON IDENTIFICATA al 22/09/2026 | NON IDENTIFICATA al 22/09/2026 | Nessun test spaziale disponibile |
| Regola LAU prevista | SÌ, Reg. 2026/1554 | SÌ, Reg. 2026/1554 | Reporting/data collection only |
| Geometria TENtec pubblica | POINT | POINT | Tecnica, non perimetro legale |
| Poligono ufficiale AFIR/TEN-T identificato | NO | NO | NO |
| Proxy tecnico autorizzato dal mandato | NO | NO | NON CREATO |

## 8. Classificazione finale

**`NO_LEGAL_SPATIAL_BOUNDARY_IDENTIFIED`**

La classificazione vale separatamente per **Trieste** e **Udine** alla data del 22/09/2026.

È contemporaneamente presente un processo normativo di definizione di una copertura **LAU per reporting**, con termine 31/12/2026. Questo fatto viene registrato come elemento pending, ma non cambia la classificazione finale perché la chat non ha trovato una base giuridica che renda quella copertura LAU il confine AFIR H2.

## 9. Conseguenze metodologiche per Chat 0.2

Questa chat **non formalizza** il vincolo AFIR di configurazione. Consegna invece le seguenti evidenze:

1. non è metodologicamente lecito usare automaticamente il confine del Comune di Trieste;
2. non è metodologicamente lecito usare automaticamente il confine del Comune di Udine;
3. i punti TENtec non possono essere trasformati in buffer o superfici senza una decisione metodologica esplicita dell'utente;
4. una futura composizione LAU ufficiale potrà essere materializzata come geometria riproducibile, ma dovrà essere distinto il suo valore di reporting dalla sua eventuale applicabilità ad AFIR;
5. prima di usare le future LAU come confine AFIR serve una fonte UE/MIT che ne stabilisca l'applicabilità, oppure una decisione progettuale esplicita e dichiarata come proxy, non come dato normativo.

### Opzione di controllo raccomandata

Mantenere aperta la formalizzazione spaziale del requisito “una HRS H2 in ciascun nodo urbano” fino a quando si verifica almeno una delle seguenti condizioni:
- pubblicazione della composizione LAU italiana e chiarimento ufficiale sulla sua applicabilità ad AFIR;
- pubblicazione di un perimetro ufficiale specifico dei nodi;
- chiarimento formale DG MOVE/MIT sul criterio territoriale da usare per AFIR H2.

Questa è una raccomandazione operativa, non una decisione ACCEPTED/FROZEN.

## 10. Fonti primarie verificate

Registro dettagliato: `docs/TENT_URBAN_NODES_FVG_SOURCE_REGISTER_v01.csv`.

Fonti chiave:
- Regolamento (UE) 2024/1679: art. 3(6), art. 40, art. 41, art. 68, Allegato II;
- Regolamento (UE) 2023/1804 consolidato al 08/01/2026: art. 6(1), considerando 40;
- Regolamento di esecuzione (UE) 2026/1554: considerando 4, art. 1, art. 6, art. 7;
- Commissione europea / DG MOVE: TENtec Information System and TEN-T map library;
- servizio pubblico TENtec ArcGIS REST: metadata dei layer Urban Nodes;
- MIT: pagina PUMS / CEF Technical Assistance 2 Italy for TEN-T 2025–2027;
- MIT: 4° incontro Rete Nazionale Nodi Urbani, slide “Copertura geografica della raccolta dati”.

## 11. Ricerca negativa e limiti

Una ricerca negativa non prova l'inesistenza assoluta di un atto non indicizzato o non pubblico. La conclusione è formulata quindi come **“nessuna delimitazione giuridica spaziale identificata nelle fonti primarie ufficiali verificate al cut-off”**, non come affermazione metafisica che nessun documento possa esistere.

Non sono state usate fonti secondarie per sostituire una fonte primaria. Fonti non ufficiali sono state escluse dalla base probatoria finale.

## 12. Quality gate del dispatch

| Controllo | Esito |
|---|---|
| Fonti primarie UE/TENtec/MIT verificate | PASS |
| Trieste trattata separatamente | PASS |
| Udine trattata separatamente | PASS |
| Currentness al 22/09/2026 esplicita | PASS |
| Definizione giuridica distinta da LAU reporting | PASS |
| Geometria TENtec distinta da confine legale | PASS |
| Nessun buffer/proxy inventato | PASS |
| Conclusione riproducibile tramite source register | PASS |
| Formalizzazione finale AFIR lasciata alla Chat Madre | PASS |

**Esito tecnico Chat 5.2: PASS / REVIEW metodologica.**

## 13. Elementi da non confondere

- **“città al centro del nodo”** ≠ perimetro del Comune;
- **“urban area”** nella definizione TEN-T ≠ automaticamente FUA statistica, PUMS area o Comune;
- **LAU reporting** ≠ automaticamente confine AFIR;
- **punto TENtec** ≠ area del nodo;
- **10 km dalla nearest TEN-T exit** per la nozione “along TEN-T” ≠ delimitazione del nodo urbano;
- **perimetro PUMS** ≠ confine AFIR salvo esplicita fonte che stabilisca tale equivalenza.

## 14. Stato da consegnare alla Chat Madre

Nessuna decisione metodologica esistente è stata modificata.

La Chat 0.2 deve decidere:
- se registrare un issue ufficiale sulla delimitazione AFIR dei nodi urbani;
- se attendere la composizione LAU italiana entro/fino al 31/12/2026;
- quale evidenza ufficiale richiedere prima di rendere computabile il vincolo nel MODEL_v2.

Fino ad allora, l'esistenza dei nodi Trieste/Udine è **fatto normativo verificato**, mentre il loro confine operativo AFIR resta **non determinato da una delimitazione legale identificata**.
