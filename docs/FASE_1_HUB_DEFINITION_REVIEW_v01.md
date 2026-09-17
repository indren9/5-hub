# FASE 1 — Definizione operativa dell’Hub Energetico Green

**Chat:** 1.1 — Definizione operativa dell’Hub Energetico Green
**Data:** 2026-09-17
**Stato del documento:** REVIEW — proposta per decisione della Chat Madre
**Stato metodologico:** NON FROZEN

## 1. Scopo e confini

Questo documento definisce che cosa debba contenere, ai fini del modello, un “Hub Energetico Green”. Non definisce l’unità elementare di analisi, non costruisce candidati, non introduce indicatori o pesi e non seleziona siti.

Le fonti sono classificate come segue:

- **NORM** = requisito normativo applicabile;
- **PROJ** = requisito o indirizzo documentato del progetto/committente;
- **METH** = scelta metodologica proposta, da approvare;
- **ASS** = assunzione esplicita, non ancora verificata/decisa;
- **BASE** = informazione della baseline Claude, solo storica e non probatoria.

## 2. Conclusioni principali del review

1. Il Regolamento (UE) 2023/1804 (AFIR) **non definisce un “Hub Energetico Green” come oggetto impiantistico unico**. Stabilisce obblighi e caratteristiche per infrastrutture di ricarica elettrica e di rifornimento di idrogeno, che restano giuridicamente distinte.
2. La legge regionale FVG 9 giugno 2026, n. 5, art. 152, inserisce tra le attività di FVG Energia l’analisi di strutture innovative di **fornitura integrata di vettori energetici** che permettano un uso diretto di energie rinnovabili per la mobilità sostenibile. È una base istituzionale del progetto, non una specifica tecnica completa del singolo Hub.
3. La comunicazione pubblica di FVG Energia del 22/07/2026 descrive la futura rete regionale come rete di “stazioni multienergia” e richiama elettrico, idrogeno, biocarburanti e altri vettori; cita inoltre il modello Apt Gorizia con idrogeno, fotovoltaico ed elettrificazione. Non prova che ogni singolo Hub debba contenere tutti i vettori.
4. Non esiste nelle fonti verificate una **superficie minima universale in m²** per un Hub di questo tipo. La superficie va derivata dal layout della configurazione minima e dalle distanze di sicurezza effettivamente applicabili.
5. L’AFIR non richiede, come condizione generale della stazione H₂, che l’idrogeno erogato sia “verde/rinnovabile”. Se il progetto vuole attribuire al termine “Green” un requisito sul vettore H₂, questo deve essere deciso e documentato separatamente.

## 3. Definizione operativa proposta

**Proposta METH da sottoporre alla Chat Madre:**

> Un Hub Energetico Green è un sito multienergia destinato alla mobilità stradale, progettato per integrare nello stesso ambito operativo almeno un modulo di rifornimento di idrogeno e un modulo di ricarica elettrica accessibili al pubblico, con le relative infrastrutture energetiche, di sicurezza, accesso e gestione. Il sito deve essere compatibile con l’uso diretto di energia rinnovabile; produzione rinnovabile in sito, accumulo ed elettrolisi sono moduli integrabili ma non diventano obbligatori finché la Chat Madre non lo decide.

Questa definizione separa deliberatamente tre livelli:

- **identità minima dell’Hub:** H₂ + ricarica elettrica + infrastrutture di supporto;
- **carattere “Green”:** compatibilità concreta con uso diretto di energia rinnovabile e possibilità di documentare l’origine rinnovabile dei vettori quando dichiarata;
- **moduli evolutivi:** produzione FER in sito, BESS, elettrolizzatore, altri vettori e servizi energetici.

La co-localizzazione H₂ + elettrico è una **scelta metodologica proposta**, non una prescrizione AFIR. È coerente con l’indirizzo regionale verso strutture integrate e con il concetto pubblico di stazioni multienergia, ma richiede approvazione esplicita della Chat Madre.

## 4. Componenti dell’Hub

| Componente | Stato proposto | Classe | Motivazione / limite |
|---|---|---|---|
| Stazione di rifornimento H₂ accessibile al pubblico | **OBBLIGATORIA** | METH | Costituisce il modulo H₂ della configurazione minima proposta. AFIR disciplina le stazioni che concorrono ai target, ma non impone che ogni “Hub” progettuale abbia H₂. |
| Sistema H₂ completo: alimentazione/produzione, eventuale buffer/stoccaggio, compressione, erogazione e sicurezza | **OBBLIGATORIA** | METH + NORM | Necessario per rendere il modulo H₂ fisicamente realizzabile; architettura e taglie restano da definire. |
| Dispenser H₂ a 700 bar | **OBBLIGATORIA se il sito deve concorrere al target AFIR art. 6** | NORM | AFIR richiede almeno un dispenser a 700 bar per le stazioni del target TEN-T core 2030. |
| Capacità H₂ di riferimento 1 t/giorno | **DA DECIDERE come requisito di progetto; riferimento normativo AFIR** | NORM + METH | AFIR usa 1 t/giorno per le stazioni del target lungo la TEN-T core; esiste una deroga fino al 50% solo nelle condizioni dell’art. 6(4). Non va trasformata automaticamente in requisito universale di ogni sito. |
| Ricarica elettrica DC accessibile al pubblico | **OBBLIGATORIA** | METH | Secondo modulo minimo della configurazione multienergia proposta. |
| Potenza aggregata e numero/potenza dei punti EV | **DA DECIDERE** | METH | Dipendono dal segmento servito (leggeri, pesanti o misto) e dal ruolo TEN-T. Non viene inventata una soglia unica. |
| Connessione elettrica, quadri/protezioni, trasformazione/cabina se necessaria | **OBBLIGATORIA** | METH + tecnica | Necessaria per alimentare ricarica e ausiliari H₂; taglia da dimensionare sul carico reale. |
| Produzione rinnovabile in sito (es. FV) | **DA DECIDERE** | PROJ + METH | Coerente con l’indirizzo regionale sull’uso diretto di rinnovabili; non è risultata una norma che imponga un impianto FER in ogni Hub. |
| Predisposizione fisica/energetica all’uso diretto di energia rinnovabile | **OBBLIGATORIA nella proposta** | METH | Evita che “Green” sia solo un’etichetta; la modalità concreta va definita senza anticipare il sito. |
| Accumulo elettrico BESS | **OPZIONALE** | METH | Può ridurre picchi, supportare FER e servizi di rete, ma non è requisito AFIR generale. |
| Elettrolizzatore H₂ in sito | **OPZIONALE** | METH | Non necessario per una HRS alimentata da H₂ prodotto altrove; se presente, si applica la regola VVF del DM 07/07/2023 e aumenta fabbisogni/spazi. |
| Trattamento/acqua per elettrolisi | **OPZIONALE / dipendente** | METH | Necessario solo nella configurazione con produzione H₂ in sito, secondo tecnologia e qualità acqua. |
| Sistemi di pagamento, informazione e gestione per servizi pubblici | **OBBLIGATORIA dove applicabile AFIR** | NORM | I punti accessibili al pubblico devono rispettare gli obblighi AFIR applicabili a ricarica/rifornimento. |
| Aree di accesso, manovra, sosta/ricarica, rifornimento e approvvigionamento H₂ | **OBBLIGATORIA** | METH + sicurezza | Parte fisica indispensabile del sito; geometria dipendente dai veicoli serviti e dalla supply H₂. |
| Distanze/aree di sicurezza e sistemi antincendio H₂ | **OBBLIGATORIA** | NORM | Da determinare sulla configurazione concreta secondo DM 23/10/2018 e norme correlate. |
| Biocarburanti / altri vettori | **OPZIONALE** | PROJ + METH | Richiamati nel concetto pubblico regionale di stazione multienergia, ma non verificati come requisito minimo di ogni Hub. |
| Servizi accessori (ristoro, officina, parcheggi aggiuntivi, servizi logistici) | **OPZIONALE** | METH | Non necessari per definire l’oggetto energetico minimo. |

## 5. Requisiti normativi e implicazioni per il modello

### 5.1 Idrogeno — AFIR

**NORM — Regolamento (UE) 2023/1804, versione consolidata corrente 08/01/2026.**

Per le infrastrutture H₂ che concorrono al target dell’art. 6:

- entro il 31/12/2030 sono previste stazioni H₂ accessibili al pubblico lungo la rete centrale TEN-T con distanza massima di 200 km;
- tali stazioni sono progettate per capacità cumulativa minima di **1 t/giorno** e almeno un dispenser a **700 bar**;
- la stazione deve essere progettata per poter essere utilizzata da veicoli leggeri e veicoli pesanti;
- in ciascun nodo urbano è richiesto almeno un punto/stazione H₂ accessibile al pubblico secondo l’art. 6;
- l’art. 6(4) consente allo Stato membro una riduzione fino al 50% della capacità nelle specifiche condizioni di basso traffico pesante e mancata giustificazione socioeconomica, mantenendo distanza massima e pressione del dispenser.
Ai fini AFIR, “lungo la rete stradale TEN-T” significa per l’H₂ ubicazione sulla rete oppure entro **10 km di distanza stradale** dall’uscita TEN-T più vicina. Questa soglia è una definizione normativa per il conseguimento dei target AFIR, non un requisito universale di qualsiasi Hub regionale.

L’Allegato II AFIR contiene inoltre specifiche tecniche di interoperabilità e qualità. Nella versione consolidata 08/01/2026, per l’H₂ gassoso sono richiamati, tra gli altri, EN 17127:2024 per interoperabilità/algoritmo di rifornimento, EN 17124:2022 per qualità dell’idrogeno e EN ISO 17268:2020 per i connettori nei termini previsti dal regolamento.

### 5.2 Ricarica elettrica — AFIR

**NORM — Regolamento (UE) 2023/1804.**

AFIR impone target differenti in funzione della rete e della categoria di veicolo. Ad esempio, lungo la TEN-T core per veicoli leggeri i gruppi di ricarica devono essere disposti in ciascun senso di marcia a intervalli massimi di 60 km; dal 31/12/2027 il gruppo deve offrire almeno 600 kW e almeno due punti da 150 kW. Questi sono requisiti del **gruppo di ricarica nel contesto AFIR**, non automaticamente una specifica minima del singolo Hub di questo progetto.

Ai fini AFIR, per la ricarica elettrica “lungo la rete stradale TEN-T” significa ubicazione sulla rete oppure entro **3 km di distanza stradale** dall’uscita TEN-T più vicina.

**Conseguenza metodologica:** prima di fissare una potenza EV minima dell’Hub occorre decidere esplicitamente se la configurazione minima serve veicoli leggeri, pesanti o entrambi e quale funzione AFIR/TEN-T si vuole attribuire ai 5 Hub.

### 5.3 Prevenzione incendi — distribuzione H₂

**NORM — DM Ministero dell’Interno 23/10/2018.**

Il decreto disciplina progettazione, costruzione ed esercizio degli impianti di distribuzione di idrogeno per autotrazione e introduce distanze e condizioni che incidono direttamente sulla geometria del sito. Non viene qui trasformato in una superficie minima unica.

Un vincolo spaziale verificato utile per il futuro dimensionamento è quello relativo alle linee elettriche aeree: per tensioni superiori a 1000 V AC o 1500 V DC, tra gli elementi pericolosi dell’impianto e la proiezione in pianta della linea è prescritta una distanza di **45 m**; i piazzali non devono essere attraversati da tali linee.

**Conseguenza metodologica:** la superficie minima deve essere calcolata da un layout che rispetti le distanze del decreto e le condizioni al contorno reali; non basta sommare aree nominali delle apparecchiature.

### 5.4 Produzione H₂ mediante elettrolisi

**NORM condizionata — DM Ministero dell’Interno 07/07/2023.**

Se viene installato un elettrolizzatore, si applica la regola tecnica di prevenzione incendi per progettazione, realizzazione ed esercizio degli impianti di produzione di idrogeno mediante elettrolisi e dei relativi sistemi di stoccaggio. Poiché l’elettrolisi è proposta come modulo opzionale, questa norma non deve essere usata per sovradimensionare automaticamente tutti i candidati.

### 5.5 Indirizzo regionale FVG

**NORM / mandato istituzionale — LR FVG 9 giugno 2026, n. 5, art. 152.**

La norma aggiunge tra le funzioni di FVG Energia l’analisi e l’elaborazione di scenari e azioni per strutture innovative di fornitura integrata di vettori energetici che permettano un uso diretto di energie rinnovabili per la transizione dei trasporti stradali.

Questo supporta il carattere **multienergia + rinnovabili** dell’oggetto di studio, ma non stabilisce numero di colonnine, potenza, capacità H₂, presenza obbligatoria di FV/BESS/elettrolisi o superficie minima del singolo Hub.

### 5.6 Significato di “idrogeno verde/rinnovabile”

Il DM MASE 5 giugno 2026 disciplina un meccanismo di sostegno alla produzione di idrogeno di origine rinnovabile. È utile per distinguere una dichiarazione di “H₂ rinnovabile” dal semplice fatto che una stazione eroghi idrogeno, ma **non è il fondamento dell’obbligo AFIR di installare HRS**.

**METH proposta:** nel modello non usare “idrogeno verde” come sinonimo automatico di “idrogeno”. Se in futuro il progetto richiede H₂ rinnovabile, dovranno essere fissati e verificati i criteri di origine/certificazione applicabili alla specifica filiera.

## 6. Requisiti minimi di accesso

Per la configurazione minima proposta:

- accessibilità al pubblico dei moduli H₂ ed EV, se devono essere conteggiati ai fini AFIR;
- collegamento stradale effettivamente utilizzabile dai veicoli target;
- spazio per ingresso, uscita, manovra, sosta/rifornimento/ricarica senza conflitti incompatibili con la sicurezza;
- accesso tecnico per manutenzione e, nella configurazione con H₂ consegnato, per il mezzo di approvvigionamento;
- separazioni e distanze di sicurezza richieste dalla configurazione H₂ reale;
- verifica della relazione con TEN-T solo quando il modello attribuirà al sito una funzione AFIR: 10 km stradali per H₂ e 3 km per ricarica elettrica secondo le definizioni del regolamento.

Non vengono fissati in FASE 1 raggi di svolta, larghezze o geometrie arbitrarie: dipendono dalla classe dei veicoli da servire e dal layout di riferimento che la Chat Madre dovrà approvare.

## 7. Requisiti energetici

La configurazione minima richiede una connessione elettrica tecnicamente dimensionabile, ma **non è giustificato fissare ora un valore universale in kW/MW**.

Il fabbisogno di progetto dovrà comprendere almeno:

`P_connessione = P_ricarica_EV + P_ausiliari_H2 + P_elettrolisi(se presente) + P_servizi - contributi gestiti FER/BESS`

con fattori di contemporaneità e logiche di gestione espliciti. La formula è uno schema di bilancio, non un dimensionamento definitivo.

## 8. Superficie minima: cosa può essere congelato ora

Non è stata verificata una norma che imponga una superficie minima unica dell’Hub. Una soglia in m² introdotta ora sarebbe arbitraria e influenzerebbe indebitamente la futura costruzione dei candidati.

La superficie minima deve invece essere derivata da un **layout tecnico di riferimento**:

`A_min = inviluppo_geometrico(H2 + EV + elettrico + accessi/manovre + sicurezza + servizi_minimi)`

Non è una semplice somma aritmetica, perché distanze di sicurezza, fasce di rispetto, viabilità e aree funzionali possono sovrapporsi o condizionarsi geometricamente.

Per stimarla servono almeno questi input, da fissare prima di applicare qualsiasi soglia territoriale:

- modalità di approvvigionamento H₂: tube trailer / pipeline / produzione in sito / altra;
- capacità H₂ di progetto e quantità/configurazione dello stoccaggio/buffer;
- numero e pressione dei dispenser e veicoli serviti simultaneamente;
- segmento EV (leggeri/pesanti/misto), numero di punti e potenze;
- cabina/trasformazione e apparecchiature elettriche;
- classe dimensionale dei veicoli e geometrie di manovra;
- aree di attesa e di approvvigionamento H₂;
- distanze di sicurezza H₂ e interferenze con elettrodotti/usi sensibili;
- eventuali moduli FER, BESS ed elettrolisi;
- servizi tecnici indispensabili.

**Proposta METH:** in FASE 1 congelare i componenti e gli input necessari al layout, non un numero di m² non ancora derivato. La futura soglia di superficie dovrà essere generata da un layout documentato della configurazione minima approvata.

## 9. Baseline Claude: elementi recuperati ma NON accettati automaticamente

**BASE — non probatoria.** La relazione generale storica descriveva cinque localizzazioni comuni a stazioni H₂ e Hub Green e distingueva quattro configurazioni, dalla HRS alimentata tramite tube trailer fino a Hub con produzione rinnovabile, accumulo ed eventuale elettrolisi.

Questi elementi sono stati usati soltanto per individuare temi da verificare. In particolare:

- la co-localizzazione H₂ + Hub non viene trattata come requisito del committente finché non esiste evidenza autorevole nel nuovo progetto;
- il tube trailer non viene assunto automaticamente come architettura obbligatoria;
- elettrolisi, accumulo e FER non vengono ereditati come componenti obbligatorie;
- le soglie AFIR sono state ricontrollate su EUR-Lex aggiornato.

## 10. Proposta di configurazione minima da congelare

La seguente è la **proposta della Chat 1.1**, non una decisione FROZEN:

### HUB_MIN_v01 — proposta

1. **Modulo H₂ accessibile al pubblico**, comprensivo della catena tecnica necessaria a ricevere/produrre, condizionare, stoccare/bufferizzare ove richiesto e dispensare H₂ in sicurezza.
2. **Compatibilità AFIR del modulo H₂**: almeno 700 bar; se il modello richiede che ogni Hub valga come stazione del target TEN-T core, usare come riferimento di progetto 1 t/giorno e compatibilità con veicoli leggeri e pesanti, salvo deroga normativa formalmente applicabile. La Chat Madre deve decidere se questo requisito AFIR-core vale per tutti i 5 Hub o solo per quelli con quella funzione.
3. **Modulo di ricarica elettrica DC accessibile al pubblico**. Presenza obbligatoria nella configurazione minima; potenza e numero di punti non vengono inventati e devono essere fissati dopo la decisione sul segmento veicolare e sulla funzione AFIR.
4. **Infrastruttura elettrica di supporto** dimensionabile per i carichi simultanei previsti e per gli ausiliari H₂.
5. **Accessi, circolazione, manovra, aree operative e sicurezza** compatibili con i veicoli target e con la filiera di approvvigionamento H₂ scelta.
6. **Compatibilità con uso diretto di energia rinnovabile** come requisito funzionale del carattere “Green”. La presenza fisica obbligatoria di FV/altre FER nel lotto resta da decidere.
7. **BESS, elettrolisi in sito, biocarburanti/altri vettori e servizi accessori** non appartengono al nucleo minimo e restano moduli opzionali salvo diversa decisione della Chat Madre.

Questa configurazione è sufficientemente definita per stabilire che cosa debba fisicamente contenere l’Hub, ma evita di congelare numeri non giustificati. Prima di derivare una soglia di superficie sono necessarie le decisioni elencate sotto.

## 11. Decisioni richieste alla Chat Madre

| ID | Decisione richiesta | Proposta Chat 1.1 |
|---|---|---|
| F1-D1 | Tutti i 5 Hub devono co-localizzare H₂ + ricarica elettrica pubblica? | **Sì**, come identità minima del modello. |
| F1-D2 | Tutti i 5 moduli H₂ devono essere dimensionati come stazioni AFIR TEN-T core da 1 t/giorno e ≥700 bar? | **700 bar sì**; **1 t/giorno da approvare esplicitamente** perché non è requisito universale di ogni Hub. |
| F1-D3 | Quale segmento EV deve servire il minimo: leggeri, pesanti o misto? | **Da decidere prima di fissare kW e numero punti.** |
| F1-D4 | Produzione FER fisicamente in sito obbligatoria? | **No nel minimo v01**; obbligatoria la compatibilità con uso diretto di FER. |
| F1-D5 | L’H₂ deve essere rinnovabile/certificato come requisito dell’Hub? | **Da decidere**; non deriva da AFIR. |
| F1-D6 | Architettura H₂ di riferimento per il futuro layout minimo? | **Da decidere**; non ereditare automaticamente il tube trailer dalla baseline. |
| F1-D7 | Biocarburanti/altri vettori nel minimo? | **No**, mantenerli opzionali/future-ready. |

## 12. Fonti verificate

**S1 — NORM. Regolamento (UE) 2023/1804 (AFIR), versione consolidata corrente 08/01/2026.**
EUR-Lex: https://eur-lex.europa.eu/eli/reg/2023/1804/2026-01-08
Usata per definizioni TEN-T, target H₂, target EV e specifiche tecniche.

**S2 — NORM. Regolamento (UE) 2024/1679 sulla rete TEN-T.**
EUR-Lex: https://eur-lex.europa.eu/eli/reg/2024/1679/oj
Riferimento per l’assetto della rete TEN-T richiamata da AFIR; nessun sito viene analizzato in questa fase.

**S3 — NORM / mandato regionale. LR FVG 9 giugno 2026, n. 5, art. 152.**
BUR FVG, I Supplemento ordinario n. 14 del 10/06/2026: https://bur.regione.fvg.it/newbur/visionaBUR?bnum=2026%2F06%2F10%2F14
Usata per il mandato relativo a fornitura integrata di vettori energetici e uso diretto di energie rinnovabili.

**S4 — PROJ / contesto pubblico. FVG Energia, 22/07/2026, “Mobilità sostenibile, incontro con Apt Gorizia sullo sviluppo delle stazioni multienergia”.**
https://prod-energia.regione.fvg.it/notizie/article/Mobilita-sostenibile-incontro-con-Apt-Goriziabr--sullo-sviluppo-delle-stazioni-multienergia/
Usata solo per documentare l’indirizzo pubblico multienergia; non come capitolato tecnico.

**S5 — NORM. DM Ministero dell’Interno 23/10/2018 — impianti di distribuzione H₂ per autotrazione.**
Indice VVF: https://www.vigilfuoco.it/servizi-le-aziende-e-i-professionisti/prevenzione-incendi/norme-di-prevenzione-incendi
Testo coordinato: https://anniversario-sca.vigilfuoco.it/sites/default/files/testiCoordinati/COORD_DM_23_10_2018.pdf

**S6 — NORM. Lettera Circolare VVF 06/03/2019 n. 3300 — distanze da linee elettriche aeree.**
https://www.vigilfuoco.it/sites/default/files/coordinated-text/COORD_LC_06_03_2019_n_3300_LINEE_ELETTRICHE_AEREE.pdf
Usata per verifica esplicita del vincolo 45 m relativo al distributore stradale di idrogeno.

**S7 — NORM condizionata. DM Ministero dell’Interno 07/07/2023 — produzione H₂ mediante elettrolisi e relativo stoccaggio.**
Pagina VVF regole tecniche: https://www.vigilfuoco.it/servizi-le-aziende-e-i-professionisti/prevenzione-incendi/testi-coordinati-di-prevenzione/testi-coordinati-di-prevenzione-regole-tecniche-suddivise-per-attivita
Testo coordinato: https://www.vigilfuoco.it/sites/default/files/2023-08/COORD_DM_07_07_2023_produzione_idrogeno.pdf

**S8 — NORM / contesto H₂ rinnovabile. DM MASE 5 giugno 2026, “Meccanismo di sostegno alla produzione di idrogeno di origine rinnovabile”.**
Gazzetta Ufficiale n. 182 del 07/08/2026: https://www.gazzettaufficiale.it/eli/id/2026/08/07/26A03843/SG
Usata per mantenere distinta la qualificazione dell’H₂ rinnovabile dagli obblighi infrastrutturali AFIR.

**S9 — BASE. Baseline storica Claude.**
Pacchetto: `21624001 FVG Energia Spa – Studio mobilità sostenibile.zip`, in particolare `deliverable/relazione_generale.docx`.
Stato: HISTORICAL / NON_AUTHORITATIVE; nessuna prescrizione è stata accettata sulla sola base di questa fonte.

## 13. Questioni aperte

Le questioni aperte sostanziali coincidono con F1-D1…F1-D7. In particolare, senza la decisione sul segmento EV e sull’architettura H₂ di riferimento non è metodologicamente corretto derivare una potenza elettrica minima unica né una superficie minima in m².

Non è stato trovato nel materiale autorevole del nuovo progetto un capitolato/verbale del committente che stabilisca esplicitamente che ciascuno dei 5 Hub debba coincidere con una HRS o che FV, BESS o elettrolisi debbano essere presenti in tutti i siti. Se tale documento esiste, deve essere acquisito e registrato prima del freeze definitivo della FASE 1.

## 14. Quality Gate Chat 1.1

- [x] Ogni componente proposta ha una motivazione.
- [x] Requisiti normativi, indirizzi di progetto, scelte metodologiche, assunzioni e baseline storica sono distinti.
- [x] Le principali fonti sono identificabili e aggiornate/verificate su fonti primarie.
- [x] Non è stata inventata una superficie minima né una potenza elettrica minima priva di base.
- [x] Le questioni irrisolte sono esplicite.
- [x] Esiste una proposta chiara di configurazione minima `HUB_MIN_v01`.
- [x] Non sono stati costruiti candidati, indicatori, pesi o ranking.
- [x] Il documento è salvato nel percorso richiesto.
- [x] Il documento è destinato a un commit Git dedicato; la verifica del commit è riportata nel SESSION CLOSE.

**Esito del review:** READY_FOR_COMMIT. La Chat 1.1 può dichiarare PASS nel SESSION CLOSE solo dopo la verifica del commit; il PASS non congela la configurazione e non chiude automaticamente FASE 1.
