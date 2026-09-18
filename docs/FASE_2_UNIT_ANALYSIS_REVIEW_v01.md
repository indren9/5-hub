# FASE 2 — Definizione dell’unità elementare di analisi

**Chat:** 2.1 — Definizione dell’unità elementare di analisi
**Data:** 2026-09-18
**Stato del documento:** REVIEW — proposta per decisione della Chat Madre e dell’utente
**Stato metodologico:** NON FROZEN
**Baseline vincolante:** `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN

## 1. Scopo e confini

Questo documento definisce la rappresentazione concettuale e geometrica di una singola alternativa candidata alla localizzazione di un Hub Energetico Green.

Non costruisce l’universo dei candidati, non sceglie fonti definitive dei poligoni, non introduce indicatori, pesi, soglie di superficie o ranking e non modifica la FASE 1.

La baseline FROZEN stabilisce che l’Hub deve ospitare congiuntamente H₂ pubblico e ricarica elettrica DC pubblica, servire veicoli leggeri e pesanti e restare un problema di localizzazione, non di layout.

### 1.1 Classi usate nel documento

- **FROZEN** = elemento già approvato e non modificabile in questa chat.
- **NORM-F1** = requisito normativo già recepito nella baseline FROZEN di Fase 1.
- **METH-PROPOSED** = scelta metodologica proposta dalla Chat 2.1, da approvare.
- **ASSUMPTION** = assunzione esplicita non approvata.
- **PROXY** = sostituto di una grandezza non osservata direttamente.
- **DEFERRED** = dettaglio che deve essere definito solo dopo la validazione dei dati in Fase 3–4.

## 2. Domanda centrale

La domanda della Fase 2 è:

> Che cos’è, geometricamente e concettualmente, una singola alternativa candidata che il modello potrà successivamente ammettere, valutare e selezionare?

La proposta della Chat 2.1 è che il candidato sia una **area fisicamente localizzabile**, rappresentata da un poligono, corredata da geometrie ausiliarie separate per rappresentazione e accesso alla rete.

Il candidato non coincide con un comune, con un punto, con un impianto esistente né con il punto in cui verrà necessariamente collocato il futuro Hub.

## 3. Alternative concettuali considerate

| Alternativa | Vantaggi | Limiti | Compatibilità con il problema |
|---|---|---|---|
| **Punto candidato** | semplice; leggero; facile per distanze | non rappresenta superficie, forma, vincoli interni, accessi multipli o disponibilità fisica; può generare falsa precisione | insufficiente come unità principale |
| **Comune / unità amministrativa** | dati aggregati facilmente disponibili; utile per reporting | troppo grossolano; non identifica un sito fisico; forte dipendenza dai confini amministrativi | inadatto come candidato; utile solo come attributo/contesto |
| **Infrastruttura o impianto esistente** | localizzazione concreta; accesso spesso noto | esclude siti greenfield; confonde una categoria di origine con l’unità del modello | utilizzabile come fonte/categoria, non come unità universale |
| **Area/poligono candidato** | rappresenta superficie e forma; supporta overlay, vincoli e fattibilità | richiede regole per multipart, overlap, accesso e identificazione | adeguato come unità principale |
| **Ibrido area + punti ausiliari** | mantiene la realtà areale e consente routing e calcoli puntuali senza confondere i ruoli | struttura dati più articolata; richiede disciplina metodologica | **proposta preferita** |

### 3.1 Motivazione della proposta

**METH-PROPOSED:** l’unità elementare è l’area candidata, mentre i punti sono rappresentazioni operative derivate.

Questa soluzione è coerente con la roadmap e con il fatto che la Fase 1 richiede verifiche territoriali di spazio, accessibilità, infrastrutture e sicurezza senza localizzare ancora il layout dell’impianto.

Un punto non può dimostrare che l’Hub trovi effettivamente spazio nel sito; un comune non può essere selezionato come se fosse una localizzazione; un impianto esistente è soltanto una possibile origine del candidato.

## 4. Specifica formale proposta

Una versione del candidato `C_i^v` è descritta concettualmente come:

`C_i^v = (P_i^v, R_i^v, A_i^v, L_i^v, M_i^v)`

dove:

- `P_i^v` = geometria poligonale della superficie candidata;
- `R_i^v` = eventuale punto rappresentativo interno, derivato e non autoritativo;
- `A_i^v` = insieme dei punti/accessi operativi associati al candidato;
- `L_i^v` = lineage/provenienza che riconduce la geometria ai dati sorgente;
- `M_i^v` = metadati di versione, qualità geometrica e stato.

### 4.1 Proprietà minime del poligono candidato

**METH-PROPOSED:** `P_i^v` deve:

1. essere una geometria poligonale valida e non vuota;
2. rappresentare una superficie territorialmente localizzabile, non un’entità puramente statistica;
3. avere provenienza ricostruibile fino alle feature sorgente;
4. essere misurabile in un sistema di riferimento metrico appropriato per le elaborazioni;
5. mantenere distinta la geometria sorgente dalla geometria eventualmente corretta/normalizzata;
6. non essere interpretato come layout definitivo dell’Hub;
7. non incorporare precisione maggiore di quella supportata dai dati sorgente.

La superficie candidata indica **dove il progetto potrebbe essere localizzato**, non il perimetro esecutivo del futuro impianto.

## 5. Poligoni multipart

Un candidato fisicamente unitario dovrebbe essere operativamente continuo.

**METH-PROPOSED:** una geometria multipart con componenti spazialmente disconnesse viene, per default, separata in candidati distinti.

Eccezioni sono ammissibili solo se esiste una continuità funzionale reale e documentabile che consenta di trattare le parti come un unico sito operativo.

Non è sufficiente che le parti condividano lo stesso identificativo urbanistico o la stessa categoria sorgente.

La regola evita che superfici separate da strade pubbliche, ferrovie, corsi d’acqua, proprietà estranee o altre discontinuità vengano sommate artificialmente per dimostrare disponibilità di spazio.

La verifica dei layer/barriere necessari è **DEFERRED** a Fase 3–4.

## 6. Aree contigue

La semplice adiacenza geometrica non implica automaticamente che due aree debbano diventare un unico candidato.

**METH-PROPOSED:** la fusione di aree contigue è ammessa solo quando la loro unione rappresenta un unico sito fisicamente e operativamente sviluppabile e la regola di aggregazione è deterministica e riproducibile.

Devono essere preservati gli identificativi delle feature sorgente che hanno contribuito all’unione.

Non viene fissata in Fase 2 alcuna tolleranza numerica per colmare micro-gap o correggere disallineamenti: una tolleranza deve derivare dalla precisione dei dataset validati in Fase 3.

Un contatto soltanto puntuale o una prossimità entro una distanza arbitraria non costituiscono, da soli, prova di continuità operativa.

## 7. Sovrapposizioni e duplicazioni

Due record non devono poter rappresentare due volte la stessa alternativa fisica senza che la duplicazione sia esplicita.

**METH-PROPOSED:** in Fase 4 deve esistere una procedura di canonicalizzazione delle sovrapposizioni che distingua almeno:

- duplicazione quasi completa dello stesso sito proveniente da fonti/strati diversi;
- sovrapposizione parziale tra geometrie con semantica diversa;
- geometrie realmente alternative che condividono solo una parte di superficie.

La regola deve evitare doppio conteggio e ranking duplicato dello stesso sito fisico, preservando però la provenienza di tutte le fonti coinvolte.

La priorità tra fonti, le soglie di overlap e le eventuali regole di partizione sono **DEFERRED** fino a quando Fase 3 avrà misurato qualità, scala e semantica dei dataset.

## 8. Confini amministrativi

Il comune non è l’unità elementare.

**METH-PROPOSED:** un candidato non viene spezzato automaticamente solo perché interseca due comuni.

I comuni interessati vengono trattati come attributi/relazioni territoriali.

Un eventuale split può essere giustificato solo se un confine amministrativo coincide con differenze normative, urbanistiche o di fattibilità che rendono le porzioni effettivamente alternative distinte.

## 9. Punto rappresentativo

Il punto rappresentativo è una geometria ausiliaria, non il candidato.

### 9.1 Usi ammessi

Può essere usato per:

- etichettatura e visualizzazione;
- esportazioni o sistemi che richiedono un punto;
- collegamenti a dati puntuali quando il metodo dell’indicatore lo giustifica esplicitamente;
- coordinate descrittive del candidato.

### 9.2 Regola proposta

**METH-PROPOSED:** se serve un unico punto interno generico, usare un punto garantito sulla superficie del poligono (`point-on-surface` o equivalente), non il centroide geometrico come default.

Un centroide può cadere fuori da poligoni concavi o in aree non rappresentative e non possiede alcun significato automatico di accesso.

Il punto rappresentativo non deve essere usato come origine predefinita delle distanze stradali.

### 9.3 Più punti operativi

Un candidato può richiedere più punti operativi.

In particolare, gli accessi stradali sono una collezione separata `A_i^v = {a_i1, a_i2, ...}` e non devono essere sostituiti dal punto rappresentativo.

## 10. Accesso stradale

L’accesso stradale deve rappresentare il luogo attraverso cui il candidato si collega realmente o potenzialmente alla rete viaria utilizzabile dai veicoli target.

**FROZEN:** il modello deve considerare veicoli leggeri e pesanti.

**NORM-F1:** dove applicabile, i requisiti regionali sugli accessi sono vincoli di fattibilità e non indicatori di merito.

### 10.1 Struttura concettuale

Per ogni potenziale accesso è utile distinguere:

- `access_point`: punto fisico sul bordo/ingresso del candidato;
- `road_anchor`: posizione/nodo sulla rete stradale usata per il routing;
- `connector`: collegamento esplicito tra accesso e rete;
- attributi di validità, fonte e compatibilità veicolare.

Il `road_anchor` non deve essere ottenuto mediante un semplice “nearest road” senza controllo di connettività e barriere.

### 10.2 Candidati con più accessi

**METH-PROPOSED:** mantenere tutti gli accessi potenzialmente validi, senza comprimere il candidato a un solo ingresso in Fase 2.

Ogni futuro indicatore dovrà dichiarare come aggrega gli accessi: minimo, massimo, migliore accesso ammissibile, accesso specifico o altra regola motivata.

L’assenza di un accesso validabile potrà diventare criterio di inammissibilità in Fase 5; non viene anticipata qui la procedura di esclusione.

## 11. Tassonomia delle distanze

Ogni distanza futura deve dichiarare esplicitamente **geometria di origine, geometria target, metrica e regola di aggregazione**.

### 11.1 Distanza area–feature

`d_area(P, F)` = minima distanza planimetrica tra il poligono candidato e una feature.

Uso tipico: prossimità fisica a infrastrutture o elementi territoriali quando l’accessibilità stradale non è il significato della misura.

Se le geometrie si sovrappongono, la distanza può essere zero; l’overlay resta una misura distinta dalla sola distanza.

### 11.2 Distanza dal bordo

`d_boundary(∂P, F)` = distanza dalla frontiera del candidato.

Va usata solo quando il requisito riguarda esplicitamente il margine del sito e non una qualunque parte della superficie.

### 11.3 Distanza da accesso

`d_access(a, F)` = distanza geometrica a partire da un accesso specifico.

È distinta sia dalla distanza dal centroide sia dalla minima distanza del poligono.

### 11.4 Distanza su rete

`d_net(a, x | G)` = distanza o costo lungo una rete stradale `G` da un accesso validato a una destinazione.

Deve dichiarare almeno metrica (metri, tempo, costo), rete/versione, regole di direzione e restrizioni rilevanti.

Per i veicoli pesanti, quando pertinente, la rete/costo deve essere compatibile con il segmento heavy e non assumere automaticamente la stessa accessibilità dei leggeri.

### 11.5 Distanza tra aree

`d_poly(P_i, P_j)` = minima distanza geometrica tra due aree candidate.

Non deve essere usata come sostituto automatico della distanza di viaggio tra due Hub; se il significato è logistico/stradale, occorre una distanza di rete tra accessi.

### 11.6 Distanza da uscite TEN-T

**NORM-F1:** per la funzione AFIR/TEN-T la baseline FROZEN recepisce 10 km stradali per H₂ e 3 km stradali per ricarica elettrica.

**METH-PROPOSED:** tali verifiche devono usare distanza **stradale su rete** da uno o più accessi validi del candidato alla più vicina uscita TEN-T pertinente.

Non usare distanza euclidea né distanza dal punto rappresentativo come sostituti della distanza normativa stradale.

La definizione cartografica delle uscite TEN-T e della rete di routing è **DEFERRED** a Fase 3.

## 12. Contratto geometrico per i futuri indicatori

Per soddisfare il gate della roadmap, ogni indicatore o vincolo spaziale successivo deve specificare almeno:

| Campo | Contenuto richiesto |
|---|---|
| `origin_role` | polygon / boundary / representative_point / access_point / road_anchor |
| `target_role` | feature/polygon/point/network node specificato |
| `metric` | overlay, area, distanza euclidea, distanza su rete, tempo, altro |
| `crs_or_network` | CRS metrico o rete/versione utilizzata |
| `aggregation` | min/max/somma/media/best-access/altra regola |
| `data_quality_rule` | trattamento di geometrie incerte, mancanti o non valide |
| `semantic_reason` | perché quella geometria misura realmente il fenomeno |

Un indicatore senza questo contratto non dovrebbe entrare nel modello.

## 13. Scala e precisione

La precisione dell’output non può superare quella dei dati di input.

**METH-PROPOSED:** per ogni fonte geometrica candidata Fase 3 deve registrare almeno:

- scala/risoluzione o accuratezza posizionale disponibile;
- CRS e unità;
- data/versione;
- regole topologiche;
- validità geometrica;
- completezza territoriale;
- semantica del perimetro;
- stabilità degli identificativi sorgente.

Per misure metriche deve essere usato un CRS proiettato appropriato; la scelta dell’EPSG operativo viene rimandata alla validazione dei dati.

Snap tolerance, buffer tecnici e soglie di equivalenza geometrica non devono essere scelti “a occhio”: devono derivare dalla qualità dichiarata/osservata dei dati.

Se l’incertezza geometrica è dello stesso ordine di grandezza di una futura soglia decisionale, il risultato deve poter essere marcato per revisione anziché produrre un falso PASS/FAIL preciso.

## 14. Identificativo univoco e versionamento

L’identità logica del candidato deve essere distinta dall’esatta versione della geometria.

### 14.1 Campi minimi proposti

- `candidate_id`: identificatore logico stabile e immutabile;
- `candidate_version`: versione della rappresentazione del candidato;
- `geometry_hash`: impronta della geometria normalizzata, usata per integrità/confronto;
- `source_lineage`: elenco/tabella delle feature sorgente contribuenti;
- `created_at` e `supersedes`: tracciamento dell’evoluzione;
- `status`: stato del candidato nel ciclo di vita.

### 14.2 Regola proposta

**METH-PROPOSED:** non usare il solo hash geometrico come identificativo logico.

Una correzione minima della geometria cambierebbe l’hash ma non necessariamente l’identità del sito.

Viceversa, una modifica sostanziale della composizione o dell’estensione deve generare una nuova versione e, quando cambia l’alternativa fisica, un nuovo `candidate_id`.

Il meccanismo concreto di generazione dell’ID (sequenziale gestito, UUID deterministico o altra soluzione) è **DEFERRED** alla Fase 4, purché rispetti stabilità, unicità e lineage.

## 15. Requisiti per le fonti da valutare in Fase 3

Senza scegliere ora i dataset, le fonti dei candidati dovranno poter supportare:

1. geometrie poligonali sufficientemente dettagliate per screening territoriale;
2. identificativi sorgente e versione;
3. significato chiaro del perimetro;
4. copertura territoriale nota;
5. qualità/scala documentabile;
6. conservazione della provenienza dopo dissoluzioni o split;
7. analisi delle sovrapposizioni;
8. passaggio riproducibile da feature sorgente a candidato canonico.

Per la rete stradale serviranno inoltre topologia routabile, direzionalità e informazioni sufficienti a non confondere vicinanza geometrica con accessibilità reale.

## 16. Implicazioni operative per Fase 4

Se la proposta viene approvata, la costruzione di `CANDIDATES_RAW_v01` dovrà:

- partire da poligoni sorgente validati;
- produrre candidati areali, non punti;
- applicare regole riproducibili di split/merge/canonicalizzazione;
- preservare lineage completo;
- creare ID e versioni stabili;
- associare geometrie ausiliarie senza sostituire il poligono;
- non applicare ancora punteggi;
- non usare una superficie minima finché non sarà metodologicamente derivata e approvata.

## 17. Questioni aperte e decisioni da sottoporre all’utente

| ID proposto | Decisione richiesta | Proposta Chat 2.1 |
|---|---|---|
| **F2-D1** | Unità elementare del modello | area/poligono fisicamente localizzabile con punti ausiliari separati |
| **F2-D2** | Multipart disconnessi | split di default; eccezione solo con continuità operativa documentata |
| **F2-D3** | Punto rappresentativo | punto interno garantito per usi descrittivi; centroide non default; mai accesso implicito |
| **F2-D4** | Accessi stradali | collezione di accessi potenziali/validati; routing da accesso, non da centroide |
| **F2-D5** | Sovrapposizioni/duplicati | canonicalizzazione obbligatoria con lineage; soglie quantitative rinviate ai dati |
| **F2-D6** | Identità e versionamento | ID logico stabile separato da versione e hash geometrico |
| **F2-D7** | Confini comunali | nessuno split automatico per confine amministrativo |
| **F2-D8** | Tolleranze geometriche | nessun valore numerico in Fase 2; derivazione dalla qualità dati in Fase 3–4 |

### 17.1 Decisioni che NON vengono richieste ora

Non sono oggetto di approvazione in questa fase:

- fonte definitiva dei poligoni;
- CRS/EPSG definitivo;
- tolleranza numerica di snap/merge;
- soglia di superficie;
- categorie urbanistiche ammissibili;
- algoritmo definitivo di access-point generation;
- rete stradale definitiva;
- indicatori, pesi o normalizzazione.

## 18. Quality Gate Chat 2.1

- [x] Alternative punto, comune, impianto, area e ibrido analizzate.
- [x] Unità principale e geometrie ausiliarie tenute distinte.
- [x] Regole concettuali per multipart, contiguità e overlap definite.
- [x] Punto rappresentativo distinto dall’accesso stradale.
- [x] Distanze classificate per significato e geometria di origine.
- [x] Verifica TEN-T ricondotta a distanza stradale da accesso, coerentemente con Fase 1.
- [x] Nessuna soglia numerica arbitraria introdotta.
- [x] Requisiti minimi di scala/precisione esplicitati.
- [x] Regola di ID/versioning proposta senza dipendere dal solo geometry hash.
- [x] Implicazioni per Fase 3 e Fase 4 documentate.
- [x] Decisioni sostanziali mantenute in stato PROPOSED.
- [x] Nessuna modifica alla baseline FROZEN di Fase 1.

**Esito del review:** READY_FOR_REVIEW.

Il presente esito non chiude né congela la FASE 2. La Chat Madre e l’utente devono decidere sulle proposte F2-D1…F2-D8 prima di produrre una baseline consolidata della fase.
