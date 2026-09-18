# FASE 2 — Specifica consolidata dell’unità elementare di analisi

**Versione:** v01
**Data:** 2026-09-18
**Stato:** FROZEN — FASE 2 PASS / CLOSED / FROZEN
**Baseline vincolante:** `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md` — FROZEN

## 1. Scopo

La Fase 2 definisce che cosa rappresenta una singola alternativa candidata nel modello di localizzazione dei 5 Hub Energetici Green in Friuli Venezia Giulia.

La specifica consolida le decisioni approvate dall’utente F2-D1…F2-D8. Non costruisce ancora l’universo candidati, non sceglie le fonti definitive dei poligoni, non introduce soglie di superficie, indicatori, pesi o ranking.

## 2. Definizione dell’unità elementare

**F2-D1 — FROZEN.**

L’unità elementare del modello è una **area/poligono fisicamente localizzabile**.

Il candidato non coincide con un comune, con un semplice punto o con un impianto esistente. Il poligono identifica una superficie sulla quale l’Hub potrebbe essere localizzato, ma non rappresenta il layout esecutivo del futuro impianto.

Punto rappresentativo, accessi stradali, road anchor e connector sono geometrie ausiliarie distinte e non sostituiscono l’identità areale del candidato.
## 3. Multipart e continuità fisica

**F2-D2 — FROZEN.**

Le geometrie multipart con componenti spazialmente disconnesse vengono separate di default in candidati distinti.

Un’eccezione è ammessa solo quando esiste continuità operativa reale e documentabile che consenta di trattare le parti come un unico sito. La semplice appartenenza alla stessa categoria o allo stesso identificativo sorgente non è sufficiente.

## 4. Punto rappresentativo

**F2-D3 — FROZEN.**

Il punto rappresentativo è una geometria ausiliaria per usi descrittivi, visualizzazione o calcoli che richiedano necessariamente un singolo punto.

Come default viene utilizzato un punto garantito sulla superficie del poligono (`point-on-surface` o equivalente), non il centroide geometrico.

Il punto rappresentativo non è un accesso stradale implicito e non costituisce l’origine automatica del routing.

## 5. Accessi stradali

**F2-D4 — FROZEN.**

Un candidato può mantenere più accessi stradali potenziali o validati.

Il routing parte dagli accessi e utilizza road anchor distinti sulla rete stradale; non parte automaticamente dal punto rappresentativo o dal centroide.

Ogni futuro indicatore basato sugli accessi dovrà dichiarare esplicitamente la propria regola di aggregazione.
## 6. Sovrapposizioni e duplicati

**F2-D5 — FROZEN.**

Lo stesso sito fisico non deve essere contato più volte solo perché compare in più dataset o layer sorgente.

In Fase 4 sarà quindi obbligatoria una procedura riproducibile di canonicalizzazione capace di distinguere:
- duplicati dello stesso sito;
- sovrapposizioni parziali tra geometrie con significato diverso;
- alternative realmente distinte che condividono solo parte della superficie.

La provenance/lineage di tutte le fonti coinvolte deve essere conservata.

Le soglie quantitative di overlap non sono fissate in Fase 2.

## 7. Identità e versionamento

**F2-D6 — FROZEN.**

L’identità logica del candidato è distinta dalla versione della geometria.

Ogni candidato avrà almeno:
- `candidate_id` stabile;
- `candidate_version`;
- `geometry_hash`;
- lineage delle feature sorgente;
- metadati di creazione, stato ed eventuale supersessione.

Una correzione geometrica non genera automaticamente un nuovo candidato se l’alternativa fisica resta la stessa. Una modifica sostanziale che rappresenta un sito fisicamente diverso può invece richiedere un nuovo `candidate_id`.
## 8. Confini comunali

**F2-D7 — FROZEN.**

Un candidato non viene spezzato automaticamente quando attraversa un confine comunale.

I comuni interessati sono attributi o relazioni territoriali del candidato. Uno split è ammesso solo quando il confine amministrativo coincide con differenze normative, urbanistiche o di fattibilità tali da rendere le porzioni alternative realmente distinte.

## 9. Tolleranze geometriche

**F2-D8 — FROZEN.**

In Fase 2 non viene fissato alcun valore numerico per snap, merge, micro-gap, equivalenza geometrica o overlap.

Le tolleranze quantitative saranno definite in Fase 3–4 sulla base della qualità reale dei dataset: scala, accuratezza posizionale, risoluzione, topologia e semantica geometrica.

Questo evita che un valore arbitrario venga trasformato in una regola metodologica prima di conoscere i dati.

## 10. Tassonomia delle geometrie e delle distanze

Ogni futuro vincolo o indicatore spaziale deve dichiarare esplicitamente:
- geometria di origine;
- geometria target;
- metrica;
- CRS o rete utilizzata;
- regola di aggregazione;
- trattamento della qualità/incertezza;
- ragione semantica della misura.
Le principali geometrie ammesse sono:
- poligono candidato;
- bordo del poligono;
- punto rappresentativo;
- access point;
- road anchor;
- feature o nodo target.

Le distanze stradali, incluse quelle rilevanti per AFIR/TEN-T, devono essere calcolate dalla geometria di accesso appropriata e non sostituite automaticamente da distanze euclidee o dal punto rappresentativo.

## 11. Elementi esplicitamente rinviati

Restano da definire nelle fasi successive:
- fonti definitive dei poligoni candidati;
- procedura concreta di generazione dell’universo candidati;
- CRS operativo definitivo;
- tolleranze numeriche di snap/merge/overlap;
- soglia minima di superficie;
- categorie urbanistiche ammissibili;
- algoritmo definitivo di generazione/validazione degli accessi;
- rete stradale definitiva;
- indicatori, pesi, normalizzazione e ranking.

La fonte e la procedura di generazione dei poligoni saranno oggetto della validazione dati in Fase 3 e della costruzione dell’universo candidati in Fase 4.

## 12. Implicazioni per Fase 3 e Fase 4

La Fase 3 dovrà verificare che le fonti candidate forniscano geometrie poligonali, identificativi e metadati sufficienti a supportare lineage, qualità, scala e semantica del perimetro.

La Fase 4 dovrà produrre candidati areali tracciabili, applicare regole riproducibili di split/merge/canonicalizzazione, associare geometrie ausiliarie e creare ID/versioni stabili senza introdurre punteggi.
## 13. Stato decisionale

Le decisioni F2-D1…F2-D8 sono **FROZEN** su approvazione esplicita dell’utente del 2026-09-18.

Il presente consolidato costituisce la **baseline metodologica FROZEN della FASE 2**.

FASE 2: **PASS / CLOSED / FROZEN**. Qualsiasi modifica futura richiede una nuova versione e una nuova approvazione esplicita dell’utente. La FASE 3 resta NON AVVIATA fino ad autorizzazione esplicita dell’utente.

## 14. Riferimenti

- `docs/FASE_2_UNIT_ANALYSIS_REVIEW_v01.md`
- `docs/HANDOFF_CHAT_2.1_20260918.md`
- `docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md`
- `docs/ROADMAP_METODOLOGICA_v1.md`
- PROJECT_CONTROL_REGISTER: DEC-0019…DEC-0026
