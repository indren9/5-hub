# CANDIDATE UNIVERSE CONTRACT v01 — ACCEPTED

**Chat:** 4.0 — Contratto dell'universo dei poligoni candidati
**Data:** 2026-09-21
**Decisione:** DQ-01
**Stato:** ACCEPTED — approvato esplicitamente dall'utente il 2026-09-21
**Vincolo:** questo documento NON costruisce l'universo candidato definitivo.

## 1. Scopo

Il contratto definisce come dovrà essere costruito, in V2-1, l'universo dei poligoni candidati del MODEL_v2.

Il candidato è una **alternativa localizzativa territoriale strategica**. Non è una particella catastale, un lotto immobiliare verificato, il footprint definitivo dell'Hub o un sito già autorizzabile/cantierabile.

Il contratto disciplina esclusivamente:
- fonti e categorie generatrici;
- regole geometriche di costruzione e canonicalizzazione;
- trattamento di currentness/proxy;
- eventuale superficie minima;
- soli prefiltri HARD indispensabili;
- lineage, identità/versioning e QA.

Restano fuori: indicatori, normalizzazioni, pesi, score, funzione obiettivo, ottimizzazione e selezione della cinquina.

## 2. Baseline vincolanti

Prevalgono, nell'ordine applicabile:
- DEC-0061, DEC-0062, DEC-0063, DEC-0064;
- PROJECT_MODEL_CONTRACT_REBASELINE_v01 — FROZEN;
- ROADMAP_METODOLOGICA_v2 — ACCEPTED / OPERATIVE;
- FASE_1_HUB_DEFINITION_REBASELINED_v03 — FROZEN;
- FASE_2_UNIT_ANALYSIS_CONSOLIDATED_v01 — FROZEN;
- REBASELINE_APPROVAL_AND_PHASE3_CLOSE_v01 — ACCEPTED;
- PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER vivi.

Evidenze Fase 3 rilevanti:
- F3_SRC_FVG_PRGC_CURRENT_001 = ACCEPTED come baseline urbanistica best-available per generazione/classificazione;
- coverage urbanistica = 215/215 Comuni;
- stato corrente: 4 CURRENT_VECTOR_VERIFIED, 4 CURRENT_PLAN_VERIFIED_NO_VECTOR, 207 CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE;
- CER D/H 2018 = HISTORICAL_ONLY / SUPPORT_ONLY;
- baseline Claude/QGIS 1.377 candidati = HISTORICAL SUPPORT;
- ISS-0002 = RESOLVED AS HISTORICAL;
- ISS-0010 = RESOLVED proceduralmente con uso di migliore geometria ufficiale disponibile e flag di currentness.

## 3. Principio generale proposto

**CU-01 — ACCEPTED.** L'universo deve privilegiare **completezza territoriale controllata e tracciabilità**, non la falsa precisione immobiliare.

La generazione usa una **sola famiglia semantica principale: poligoni di pianificazione urbanistica/territoriale ufficiale best-available**, acquisiti tramite più canali sorgente current-first.

Non si propone, nella v01, di sommare automaticamente una seconda famiglia autonoma di lotti disponibili, particelle catastali, immobili o perimetri commerciali/consortili.

Razionale:
- è coerente con la scala strategica del MODEL_v2;
- evita duplicazioni eterogenee e bias verso territori con migliore pubblicazione di lotti;
- usa la baseline Fase 3 già accettata;
- mantiene proprietà e disponibilità commerciale fuori core.

## 4. Gerarchia delle fonti generatrici

**CU-02 — ACCEPTED.** Per ogni Comune si applica la seguente gerarchia, senza fallback silenziosi.

### Tier S1 — vettore urbanistico corrente verificato
Usare il vettore ufficiale quando variante/piano e geometria risultano allineati e la currentness è verificata.

Flag: `CURRENT_VECTOR_VERIFIED`.

### Tier S2 — vettore ufficiale best-available con currentness non chiusa
Usare geometrie ufficiali Regione/IRDAT/Eagle/Comune quando il vettore è disponibile ma la vigenza/allineamento non è dimostrata integralmente.

Flag obbligatori:
- `PLANNING_CURRENTNESS_NOT_VERIFIED`;
- stato lineage/currentness nativo della coverage.

Questo uso è un **proxy urbanistico**, non una attestazione di vigenza.

### Tier S3 — piano corrente verificato ma geometria proxy
Quando il piano corrente è verificato ma non esiste un vettore corrente allineato, usare la migliore geometria ufficiale disponibile solo se la sua natura di proxy è esplicita.

Flag:
- `CURRENT_PLAN_VERIFIED_NO_VECTOR`;
- `GEOMETRY_PROXY_USED`.

### Tier S4 — CER 2018 come ultima risorsa storica
I layer:
- F3_SRC_FVG_ZONING_IND_001;
- F3_SRC_FVG_ZONING_COM_001

possono essere usati solo se non esiste una geometria urbanistica ufficiale migliore per la categoria necessaria.

Flag:
- `HISTORICAL_GEOMETRY_PROXY`;
- `PLANNING_CURRENTNESS_NOT_VERIFIED`;
- anno/base `MOSAICATURA_PRG_2018`.

CER 2018 non può essere dichiarato corrente.

### Tier S5 — nessuna geometria utilizzabile
Non si digitalizza o inventa un poligono per colmare il gap.

Il Comune/categoria entra nel QA come `NO_USABLE_POLYGON_SOURCE`; l'effetto sulla completezza deve essere quantificato.

## 5. Categorie generatrici

**CU-03 — ACCEPTED.** La selezione avviene sulla semantica urbanistica nativa, con mapping esplicito e conservazione integrale di codice e descrizione sorgente.

Classi generatrici armonizzate approvate:
- `G1_PRODUCTIVE`: industriale, artigianale, produttivo/manifatturiero, deposito/magazzino quando esplicitamente previsto;
- `G2_COMMERCIAL_TERTIARY`: commerciale, direzionale, terziario, grande distribuzione e servizi economici non residenziali; sono esclusi i servizi pubblici generici, sociali, sanitari e scolastici privi di una componente economico-produttiva pertinente;
- `G3_LOGISTICS_TRANSPORT`: logistica, interporto, terminal, porto, autoporto, trasporto e aree di servizio trasportistiche areali;
- `G4_MIXED_RELEVANT`: zone miste che contengono esplicitamente almeno una componente G1, G2, G3 o G5;
- `G5_TECHNICAL_UTILITY_ENERGY`: aree areali esplicitamente destinate a impianti tecnologici, utility, servizi tecnici, infrastrutture energetiche o funzioni equivalenti.

Le classi non sono categorie di idoneità né punteggi. Servono solo a stabilire quali poligoni entrano nell'universo da valutare.

Non devono generare candidati, salvo successiva decisione:
- residenziale puro;
- agricolo puro;
- verde/parco/tutela puro;
- acqua/alveo;
- servizi pubblici generici senza componente produttiva/commerciale/logistica/trasportistica esplicita;
- infrastrutture lineari prive di area localizzativa;
- categorie non interpretabili con sufficiente evidenza.

Le categorie ambigue non vengono escluse in silenzio: devono essere marcate `GENERATOR_CLASS_UNRESOLVED` e risolte nel mapping prima della generazione definitiva.

## 6. Unione di più famiglie territoriali

**CU-04 — ACCEPTED.** Non si propone una union indiscriminata di famiglie territoriali eterogenee.

Sono ammessi più **canali sorgente** della stessa famiglia urbanistica (Comune, IRDAT, Eagle, Regione, CER fallback) perché servono a coprire 215 Comuni con currentness diversa.

Non sono generatori autonomi nella v01:
- particelle catastali;
- patrimonio disponibile;
- lotti pubblicati dai Consorzi;
- immobili in vendita/assegnazione;
- punti di porti/interporti;
- CORINE/land cover;
- poligoni Claude/QGIS.

Perimetri ufficiali di porti, interporti, terminali o agglomerati industriali potranno entrare in una futura versione solo se:
1. sono registrati e validati come dataset areali;
2. aggiungono alternative non già rappresentate dall'urbanistica;
3. viene definita una canonicalizzazione inter-famiglia riproducibile;
4. l'utente approva la modifica del contratto.

## 7. Regole geometriche

**CU-05 — ACCEPTED.** La geometria candidata deriva dalla geometria sorgente; non si crea un lotto sintetico tramite buffer, centroide, nearest-road o access point.

Regole:
1. geometrie non poligonali non generano candidati;
2. geometrie multipart con componenti disconnesse sono splittate di default, coerentemente con F2-D2;
3. nessuno split automatico sul confine comunale, coerentemente con F2-D7;
4. nessun dissolve automatico per Comune o per classe armonizzata;
5. poligoni contigui vengono uniti solo se rappresentano lo stesso oggetto logico sorgente o una frammentazione tecnica documentata;
6. non si colmano gap spaziali con buffer o snap universali non giustificati;
7. nessuna tolleranza metrica universale è approvata in DQ-01.Se in implementazione servirà una tolleranza non nulla per errori topologici, dovrà essere derivata dalla qualità/accuratezza della fonte, configurata, documentata e sottoposta a QA.

## 8. Geometrie invalide, multipart e riparazioni

**CU-06 — ACCEPTED.**

Pipeline geometrica minima:
1. leggere la geometria sorgente senza semplificazione;
2. verificare tipo, null/empty e validità;
3. applicare una riparazione deterministica equivalente a `make_valid` quando necessario;
4. estrarre solo le componenti poligonali risultanti;
5. splittare le componenti spazialmente disconnesse;
6. registrare ogni trasformazione nel lineage;
7. ricalcolare geometry hash.

Esclusione tecnica ammessa solo quando, dopo riparazione:
- la geometria è nulla o vuota;
- non resta alcuna componente poligonale;
- l'area è nulla/non positiva;
- la geometria non è ricostruibile in modo deterministico.

La riparazione non deve cambiare silenziosamente la semantica del perimetro.

## 9. Sovrapposizioni, duplicati e canonicalizzazione

**CU-07 — ACCEPTED.**

Principio F2-D5: lo stesso sito fisico non va contato più volte solo perché compare in più fonti.

Regole approvate:
- duplicati geometrici esatti/topologicamente equivalenti con stessa identità logica: un solo candidato, lineage combinato;
- stessa feature pubblicata da più canali: priorità al Tier di currentness più alto, le altre versioni restano fonti di supporto;
- geometrie non identiche ma riferite allo stesso oggetto logico: scegliere la geometria con source/currentness priority più alta; registrare `SOURCE_GEOMETRY_CONFLICT`;
- sovrapposizioni parziali tra oggetti con semantica diversa: non unire automaticamente;
- contiguità o overlap da soli non provano identità;
- nessuna soglia percentuale universale di overlap è approvata.

I casi non risolvibili con lineage/identità sorgente devono restare nel QA, non essere fusi per convenienza.

## 10. Superficie minima

**CU-08 — ACCEPTED.** **Superficie minima del poligono candidato = 8.000 m².**

Fonte del requisito: input da consulenza tecnica comunicato dall'utente il 2026-09-21. Il valore è assunto come requisito progettuale del MODEL_v2 e non deriva dalla precedente baseline Claude/QGIS.

Regola operativa:
- calcolare `area_m2` sulla geometria candidata dopo repair deterministico e split delle componenti disconnesse, in CRS metrico documentato;
- `area_m2 >= 8000` → il poligono può entrare nell'universo, se supera anche gli altri gate tecnici;
- `area_m2 < 8000` → esclusione HARD dall'universo con motivo `MIN_AREA_8000_NOT_MET`.

Gli 8.000 m² rappresentano in V2-1 la superficie lorda geometrica del poligono, non una stima della superficie netta effettivamente utilizzabile.

La vecchia soglia osservata di circa 5.000 m² resta solo benchmark storico e non contribuisce alla scelta degli 8.000 m².

Il requisito potrà essere rivisto solo con nuova decisione esplicita e nuova evidenza tecnica.

## 11. Prefiltri HARD ammessi in DQ-01

**CU-09 — ACCEPTED.** Non viene approvato alcun HARD di idoneità territoriale.

Sono ammessi solo gate tecnici/di scope:
- geometria poligonale esistente;
- geometria valida o riparabile deterministicamente;
- area positiva e `area_m2 >= 8000`;
- appartenenza al perimetro territoriale FVG;
- appartenenza a una categoria generatrice approvata;
- rimozione di duplicati della stessa alternativa fisica.

L'appartenenza alla categoria generatrice definisce l'universo, non rappresenta un giudizio di ammissibilità finale.

## 12. Cosa NON deve diventare hard filter in DQ-01

Non devono escludere automaticamente candidati:
- proprietà, catasto, disponibilità commerciale o prezzo;
- edifici/manufatti o stato immobiliare;
- currentness urbanistica non dimostrata;
- prossimità/capacità elettrica;
- accessibilità locale, accessi o geometria TEN-T;
- PGRA, PAI/frane, PPR, Natura 2000, parchi/riserve, biotopi, prati stabili;
- distanza da infrastrutture o domanda;
- presenza di proxy o dato mancante;
- appartenenza/non appartenenza alla baseline Claude/QGIS;
- nessuna soglia di area diversa da CU-08; in particolare la vecchia soglia ~5.000 m² non ha alcun ruolo operativo.

Eventuali HARD sostanziali appartengono a DQ-02/DQ-03 e richiedono decisione esplicita separata.

## 13. Currentness e proxy

**CU-10 — ACCEPTED.** Ogni candidato deve avere un currentness/proxy status machine-readable.

Campi minimi:
- `source_tier`;
- `currentness_status`;
- `planning_currentness_verified` boolean/tri-state;
- `geometry_proxy_used`;
- `historical_proxy_used`;
- `proxy_reason`;
- `source_gap_flag`.

Proxy/currentness non modificano automaticamente score o ammissibilità in DQ-01.

Il QA deve riportare candidati e superficie per Tier S1–S5 e per Comune, così da rendere visibile il bias territoriale introdotto dalla qualità disomogenea delle fonti.

## 14. Lineage minimo obbligatorio

**CU-11 — ACCEPTED.** Per ogni candidato devono essere ricostruibili almeno:

- `candidate_id`;
- `candidate_version`;
- `universe_version`;
- `geometry_hash`;
- `source_dataset_id` del DATA_REGISTRY;
- ente/fonte e source tier;
- snapshot/versione/data di acquisizione;
- URL/percorso e hash del file sorgente quando disponibile;
- codice ISTAT e Comuni interessati;
- piano/variante/stato procedurale se disponibile;
- `currentness_status` ed evidenza;
- layer e feature ID nativi;
- codice zona/sottozona e descrizione/destinazione native;
- `generator_class` e regola di mapping;
- CRS sorgente e CRS operativo;
- sequenza ordinata delle trasformazioni geometriche;
- gruppo di canonicalizzazione/duplicato;
- eventuali predecessori/successori;
- script/config/commit di generazione.

Nessun candidato senza lineage minimo può entrare nella baseline V2-1.

## 15. candidate_id, versioning e geometry_hash

**CU-12 — ACCEPTED.**

Schema:
- `candidate_id`: identificatore logico stabile;
- `candidate_version`: intero crescente della rappresentazione del candidato;
- `universe_version`: versione dell'intero universo;
- `geometry_hash`: hash della geometria normalizzata.

Proposta tecnica:
- generazione iniziale di `candidate_id` tramite UUIDv5 da una `canonical_identity_key` basata sul lineage logico sorgente, non sull'area o sul geometry hash;
- il candidate_id resta invariato quando cambia solo la geometria/lineage ma l'alternativa fisica è la stessa;
- se la modifica rappresenta un sito logicamente diverso, si crea un nuovo candidate_id e si registra `supersedes_candidate_id`;
- geometry_hash cambia a ogni modifica geometrica effettiva.

Il geometry hash deve essere calcolato su una rappresentazione geometrica normalizzata e su un CRS operativo documentato; il CRS numerico esatto resta parametro tecnico da congelare nell'implementazione, non viene inventato in DQ-01.

## 16. QA minimo dell'universo futuro

**CU-13 — ACCEPTED.** V2-1 potrà passare solo se sono verificati almeno:

- 100% candidate_id univoci e non nulli;
- 100% candidate_version/universe_version valorizzati;
- 100% geometry_hash valorizzati;
- 0 geometrie null/empty/non poligonali;
- 0 geometrie invalide non gestite;
- multipart disconnessi trattati secondo F2-D2;
- 100% lineage minimo presente oppure candidate escluso tecnicamente con motivo;
- 100% generator_class risolto;
- 100% currentness/proxy status valorizzato;
- report dei source gap per 215/215 Comuni;
- report duplicati/canonicalizzazione;
- report overlap non risolti;
- conteggi e superfici per source tier, Comune e generator class;
- verifica 100% del gate `area_m2 >= 8000` per i candidati inclusi; distribuzione area dei candidati inclusi ed esclusi per soglia; benchmark storico ~5.000 m² solo descrittivo;
- rerun deterministico con stessi input/config = stessi ID, conteggi e hash;
- nessun indicatore, peso, score o filtro DQ-02 applicato.

## 17. Benchmark Claude/QGIS

Le 1.377 aree storiche possono essere usate solo per:
- confronto di copertura geografica;
- confronto di cardinalità;
- individuazione di categorie o fonti storicamente considerate;
- controllo qualitativo di differenze anomale.

Non costituiscono target numerico. Il nuovo universo non deve essere forzato a convergere a 1.377 candidati né alla soglia ~5.000 m².

## 18. Stato decisionale

Il presente contratto è **ACCEPTED** con approvazione esplicita dell'utente il 2026-09-21.

DQ-01 è chiusa. È autorizzata la successiva implementazione dell'universo candidato secondo CU-01…CU-13.

DQ-02 e successive restano non approvate.

## 19. Raccomandazione sintetica DQ-01

Pacchetto DQ-01 ACCEPTED:
1. universo generato da urbanistica ufficiale best-available current-first;
2. cinque classi generatrici G1–G5 secondo C3+;
3. CER 2018 solo fallback storico dichiarato;
4. nessuna seconda famiglia catastale/commerciale;
5. multipart disconnessi splittati; no dissolve/merge generalizzato;
6. canonicalizzazione guidata da lineage, non da soglie geometriche arbitrarie;
7. superficie minima HARD = 8.000 m² di area lorda del poligono post-repair/split;
8. altri soli gate tecnici come hard prefilter;
9. currentness/proxy sempre visibile e mai tradotto automaticamente in esclusione;
10. candidate_id stabile + versioning + geometry hash + lineage completo.

