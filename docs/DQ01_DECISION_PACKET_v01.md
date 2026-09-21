# DQ-01 DECISION PACKET v01

**Chat:** 4.0 — Contratto dell'universo dei poligoni candidati
**Data:** 2026-09-21
**Stato:** PROPOSED
**Decisione richiesta:** approvazione/modifica del CANDIDATE_UNIVERSE_CONTRACT prima di costruire l'universo.

## 1. Decisione da prendere

DQ-01 deve stabilire **da quali poligoni nasce l'universo delle alternative territoriali e quali sole trasformazioni preliminari sono ammesse**.

Non riguarda indicatori, score, pesi, ottimizzazione o selezione dei 5 Hub.

## 2. Evidenze che vincolano la decisione

1. Il modello è strategico-territoriale, non catastale/immobiliare/progettuale — DEC-0061/0062.
2. Fase 2 impone poligono come unità, split dei multipart disconnessi, canonicalizzazione dei duplicati e candidate_id stabile separato dalla versione geometrica.
3. F3_SRC_FVG_PRGC_CURRENT_001 è ACCEPTED come baseline urbanistica best-available per generazione/classificazione.
4. La coverage urbanistica copre 215/215 Comuni, ma solo 4 hanno CURRENT_VECTOR_VERIFIED; 207 hanno lineage/currentness incompleta e 4 piano corrente verificato senza vettore corrente.
5. CER D/H deriva da Mosaicatura PRG 2018 ed è HISTORICAL_ONLY / SUPPORT_ONLY.
6. Le 1.377 aree Claude/QGIS non hanno lineage di generazione sufficiente e mostrano un minimo osservato 5.016,2 m² coerente con un filtro storico ~5.000 m².
7. Proprietà/disponibilità commerciale è fuori core.
8. Nessun tematismo ambientale, energetico o di accessibilità può diventare HARD solo per presenza/intersezione senza decisione successiva.

## 3. DQ01-A — famiglia generatrice

### Alternativa A1 — solo vettori urbanistici pienamente correnti
**Vantaggi:** massima currentness dimostrata.
**Svantaggi:** oggi copertura vettoriale verificata insufficiente.
**Bias:** favorisce Comuni con pubblicazione migliore.
**Completezza:** bassa.
**Natura:** scelta progettuale restrittiva.

### Alternativa A2 — urbanistica ufficiale best-available current-first
**Vantaggi:** usa la baseline Fase 3 accettata; copertura regionale controllabile.
**Svantaggi:** currentness eterogenea.
**Bias:** dipende dalla qualità delle fonti comunali.
**Completezza:** alta con proxy dichiarati.
**Natura:** scelta progettuale.

### Alternativa A3 — union di urbanistica + lotti/catasto/disponibilità
**Vantaggi:** maggiore concretezza immobiliare.
**Svantaggi:** fuori scope, copertura non uniforme, duplicazioni.
**Bias:** forte verso aree pubblicate/disponibili.
**Completezza:** distorta.
**Natura:** incompatibile con re-baseline core.

**Raccomandazione PROPOSED:** A2.`r`n`r`n## 4. DQ01-B — fallback quando manca un vettore corrente allineato

### B1 — nessun fallback
Alta purezza, ma perdita sistematica di copertura.

### B2 — migliore geometria ufficiale disponibile + flag
Mantiene copertura e rende esplicita l'incertezza.

### B3 — CER 2018 come fonte ordinaria
Uniforme ma temporalmente obsoleto.

### B4 — gerarchia B2 + CER 2018 solo ultima risorsa
Massimizza copertura senza dichiarare corrente ciò che non lo è.

**Raccomandazione PROPOSED:** B4.

Condizione: ogni fallback deve avere `source_tier`, `currentness_status`, `geometry_proxy_used` e `historical_proxy_used`.

## 5. DQ01-C — categorie generatrici

### C1 — solo produttive/industriali/artigianali
**Pro:** semantica forte; minore rumore.
**Contro:** può omettere commercio, logistica, terminali e aree di servizio.
**Bias:** verso insediamenti industriali tradizionali.

### C2 — produttive + commerciali
Riproduce in parte la logica storica D/H, ma resta incompleta per logistica/speciali.

### C3 — non-residenziale rilevante articolato in G1–G4
- G1 produttivo/industriale/artigianale;
- G2 commerciale/terziario/servizi;
- G3 logistica/trasporti/porto/interporto/terminal;
- G4 misto con componente esplicita G1–G3.

**Pro:** maggiore aderenza alle funzioni strategiche dell'Hub.
**Contro:** richiede mapping dei codici PRGC locali.
**Bias:** più controllabile perché la semantica nativa resta disponibile.
**Completezza:** superiore.

### C4 — tutte le zone non residenziali
Massima recall apparente ma include molte aree irrilevanti.

**Raccomandazione PROPOSED:** C3.

Le categorie ambigue devono essere risolte esplicitamente, non eliminate con keyword opache o regole non auditabili.

## 6. DQ01-D — merge/split/canonicalizzazione

### D1 — dissolve per classe/comune
Semplice ma distrugge l'identità locale e può creare mega-poligoni artificiali.

### D2 — conservare feature sorgente; split multipart; merge solo per stessa identità logica
Massima tracciabilità e coerenza con Fase 2.

### D3 — merge per distanza/overlap con soglia numerica universale
Automatizzabile ma introduce una tolleranza arbitraria non supportata.

**Raccomandazione PROPOSED:** D2.

Regola chiave: contiguità o overlap non bastano a dimostrare che due geometrie siano la stessa alternativa.`r`n`r`n## 7. DQ01-E — superficie minima

### E1 — 5.000 m²
**Pro:** coerente col comportamento storico osservato.
**Contro:** lineage metodologico non dimostrato; vietata l'eredità automatica.
**Bias:** elimina sistematicamente alternative piccole prima di sapere il reale fabbisogno Hub.

### E2 — nuova soglia tecnica fissata ora
Non supportata: Fase 1 re-baselined non quantifica il footprint minimo universale.

### E3 — nessuna soglia in V2-1; area come attributo e QA
**Pro:** preserva completezza; separa generazione da ammissibilità.
**Contro:** aumenta il numero di micro-poligoni da diagnosticare.
**Bias:** minimo; eventuali sliver restano visibili.

**Raccomandazione PROPOSED:** E3.

Qualunque futura soglia richiede nuova decisione con fabbisogno spaziale approvato e sensitivity.

## 8. DQ01-F — HARD prefilter

### F1 — applicare già ambiente/rischio/accesso/energia
Riduce l'universo ma anticipa DQ-02/DQ-03 e rischia falsi negativi.

### F2 — soli gate tecnici/di scope
- geometria poligonale;
- valida o riparabile;
- area positiva;
- territorio FVG;
- categoria generatrice;
- deduplicazione della stessa alternativa.

**Raccomandazione PROPOSED:** F2.

Non sono HARD in DQ-01:
- proprietà/catasto/disponibilità;
- currentness proxy;
- capacità/prossimità elettrica;
- accesso locale/TEN-T;
- PGRA/PAI/PPR/Natura 2000/aree protette/prati stabili;
- superficie <5.000 m².

## 9. DQ01-G — identità e versioning

### G1 — ID progressivo
Semplice ma instabile a fronte di inserimenti/riordinamenti.

### G2 — ID = geometry hash
Riproducibile ma cambia a ogni correzione geometrica, in conflitto con F2-D6.

### G3 — candidate_id logico stabile + candidate_version + geometry_hash
Consente correzioni geometriche senza perdere identità.

**Raccomandazione PROPOSED:** G3.

Proposta tecnica: UUIDv5 iniziale da canonical identity key di lineage; mantenimento dell'ID quando l'alternativa fisica resta la stessa; nuovo ID solo per alternativa logicamente diversa.

## 10. DQ01-H — QA e benchmark storico

### H1 — numero candidati simile a 1.377 come gate
Non valido: trasforma la baseline storica in target.

### H2 — QA strutturale, lineage, currentness e determinismo
Verifica ciò che rende l'universo ricostruibile senza imporre il risultato storico.

**Raccomandazione PROPOSED:** H2.

Il confronto con 1.377 è solo benchmark descrittivo di copertura/cardinalità.

## 11. Pacchetto di approvazione proposto

Approvare come bundle:
- A2 — urbanistica best-available current-first;
- B4 — fallback ufficiale + CER 2018 ultima risorsa;
- C3 — classi G1–G4;
- D2 — split conservativo / merge solo per identità;
- E3 — nessuna superficie minima;
- F2 — soli gate tecnici;
- G3 — ID logico + version + geometry hash;
- H2 — QA strutturale e deterministico.

Stato richiesto dopo approvazione: `DQ-01 = ACCEPTED`.

Solo dopo tale approvazione la Chat Madre potrà autorizzare la costruzione di `CANDIDATE_UNIVERSE_v01`.

## 12. Conseguenze se il bundle viene approvato

La futura implementazione V2-1 dovrà:
1. materializzare/normalizzare le geometrie sorgente secondo la gerarchia approvata;
2. costruire un mapping auditabile delle categorie native a G1–G4;
3. applicare esclusivamente le regole geometriche e i gate tecnici approvati;
4. produrre universo, lineage e QA;
5. non applicare DQ-02/DQ-03 prima della loro approvazione.

Fino ad approvazione esplicita, tutto il pacchetto resta **PROPOSED**.
