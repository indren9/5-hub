# HANDOFF — Chat 3.5 — Proxy territoriale di prossimità alla rete elettrica

**Chat:** 3.5 — Proxy territoriale di prossimità alla rete elettrica
**Data:** 2026-09-20
**Destinatario:** Chat 0.2 — Chat Madre 5 HUB
**Stato finale operativo:** **READY_WITH_LIMITATIONS / REVIEW**
**Mandato:** `docs/DISPATCH_CHAT_3.5_ELECTRIC_GRID_ENERGY_FEASIBILITY_v02.md`

## 1. Obiettivo

Eseguire esclusivamente il quality gate minimo OSM/OpenInfraMap previsto dal dispatch v02 e dalla nota preliminare, senza stimare capacità disponibile, hosting capacity, costi di connessione o fattibilità elettrica di dettaglio.

Il gate doveva verificare se una geometria fisica OSM delle sottostazioni può essere proposta come base territoriale per un futuro proxy di prossimità, mantenendo separati:
- infrastruttura fisica;
- area convenzionale servita;
- capacità elettrica reale.

## 2. Lavoro svolto

1. Verificate integralmente baseline Fase 1 e Fase 2 FROZEN e il dispatch v02.
2. Verificati PROJECT_SOURCE_OF_TRUTH e PROJECT_CONTROL_REGISTER: DEC-0050 ACCEPTED; ISS-0007 OPEN; F3_SRC_FVG_CP_001 SCREENING_ONLY.
3. Estratti e conservati raw OSM `power=substation` su envelope FVG + bordi, con 9 query Overpass riproducibili.
4. Classificati gli attributi OSM e conservato il JSON completo dei tag.
5. Costruito un filtro QA prudente per geometrie plausibili CP / AT-MT, distinto dalla classificazione OSM generica.
6. Confrontata la copertura con tutte le 57 aree `CER:AREECONVENZIONALI_CP`.
7. Eseguito cross-check mirato con fonti ufficiali e-distribuzione, AcegasApsAmga e SECAB.
8. Identificati gap interni, gap extraregionali e conflitti semantici.
9. Materializzati fonti e output pesanti su OneDrive con SHA-256.

## 3. Risultati principali

Estrazione OSM:
- 8.206 elementi `power=substation` deduplicati nell'envelope;
- 92 posizioni rappresentative incluse nel sottoinsieme QA CP-proxy;
- 89 `A_DSO_HV_PLAUSIBLE`;
- 3 `B_DISTRIBUTION_HV_OPERATOR_MISSING`;
- distribuzione operatori nel sottoinsieme: 81 e-distribuzione, 7 AcegasApsAmga, 1 SECAB, 3 mancanti.

Copertura aree convenzionali:
- 57 aree ufficiali totali;
- 44 `EXTRAFVG=0`, 13 `EXTRAFVG=1`;
- 48/57 con almeno una geometria CP-proxy interna;
- sulle 44 aree interne FVG: **42/44 = 95,5%** con geometria plausibile interna e gestore coerente;
- 2/44 gap interni: `AC001E00999` e `AC001E00994`;
- 7/13 aree extraregionali senza geometria CP-proxy interna.

Cross-check DSO:
- e-distribuzione: 10 casi campione con corrispondenza nominale/ruolo forte; Redipuglia confermata ufficialmente come CP ma senza distinta geometria OSM e-distribuzione isolata;
- AcegasApsAmga: tutte le 5 CP AT/MT ufficiali del Piano 2025-2029 ritrovate in OSM a 132 kV;
- SECAB: CP Paluzza 132/20 kV confermata ufficialmente; OSM plausibile per operatore/tensione ma con `substation=industrial`.

## 4. Interpretazione tecnica

Il risultato **non** dimostra che OSM sia un inventario ufficiale completo delle cabine primarie.

Dimostra invece che OSM è sufficientemente ricco, uniforme e riproducibile da poter essere sottoposto alla Chat 0.2 come sorgente fisica per un proxy territoriale di prossimità, con limiti espliciti e triangolazione ufficiale.

OpenInfraMap resta esclusivamente un visualizzatore di OSM e non viene trattata come fonte autonoma.

La regola QA >=60 kV è stata usata solo per non perdere cabine ufficialmente rilevanti come Barcis. Non è una soglia metodologica approvata, non è una soglia di connessione e non deve essere trasferita automaticamente nel modello.

## 5. Gap e problemi aperti

### Gap interno `AC001E00999`
Fonte ufficiale e-distribuzione conferma una CP “REDIPUGLIA”. OSM rappresenta nel sito la stazione Terna “Redipuglia” 380 kV e una sottostazione ferroviaria, ma il gate non ha isolato una distinta geometria OSM e-distribuzione classificabile come CP-proxy.

### Gap interno `AC001E00994`
OSM contiene “Opicina”, e-distribuzione, `substation=distribution`, 132 kV, ma la geometria risulta circa 1,80 km fuori dal poligono convenzionale. Non è stata introdotta alcuna tolleranza ad hoc.

### Limite semantico generale
Il filtro OSM può sovra-includere: nel territorio Acegas restituisce 7 geometrie plausibili mentre il Piano ufficiale identifica 5 CP AT/MT. Il dataset derivato va quindi chiamato “CP-proxy plausibile”, non “cabine primarie ufficiali”.

### ISS-0007
**Resta OPEN.** Il gate non colma il gap di capacità elettrica disponibile né deve farlo secondo DEC-0050. La Chat 3.5 non chiude autonomamente l'issue.

## 6. Artifact repository

Commit sostanziale:
`ff5edc3073b02d32a8a0d366f89f24d0d8de08d7`
Messaggio: `feat(f3): validate OSM electric grid proxy`

File:
- `docs/FASE_3_ELECTRIC_GRID_PROXY_VALIDATION_REVIEW_v01.md`;
- `docs/FASE_3_ELECTRIC_GRID_PROXY_SOURCE_MATRIX_v01.csv`;
- `scripts/acquire_validate_electric_grid_proxy_chat3_5_v01.py`;
- presente handoff `docs/HANDOFF_CHAT_3.5_ELECTRIC_GRID_PROXY_v01.md`.

Branch:
`chat-3.5-electric-grid-energy`

## 7. Artifact OneDrive

Root:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\02_external_sources\F3_CHAT_3_5\`

Manifest autorevole del package:
`source_manifest_v01.json`

Contiene bytes e SHA-256 per:
- WFS ufficiale FVG;
- 9 raw Overpass;
- inventario OSM completo;
- subset QA;
- GeoJSON CP-proxy;
- coverage 57 aree;
- summary;
- fonti DSO materializzate;
- cross-check DSO.

Hash chiave:
- WFS: `dea1b982b2f7c5a2029e4e901df797e9f4302a3d0d0756292c13d1cfd2a1a822`;
- CP-proxy CSV: `23ffb98b8716c5423ff58882c0625076308ec908b53b184f46c68d7bb43d1351`;
- CP-proxy GeoJSON: `9360ecc0675814b8a3d58b59690c5153862405206a99ebba1f909b8b7e42c967`;
- coverage CSV: `fb22971c80d0c5b15e0d2483d165691faac20e6aea394b3ec41eba6c0dc97a2f`;
- DSO cross-check CSV: `6049f5ccfd8a944e94ae56c35e658ad85a23737df0a4626431f76e559cbafe50`.

## 8. Controlli eseguiti

- esecuzione completa script: PASS;
- `python -m py_compile`: PASS;
- `git diff --check`: PASS;
- conteggi finali: 8206 / 92 / 57 / 17 coerenti;
- materializzazione e hash: PASS;
- nessun MW o capacità inventata: PASS;
- nessuna modifica alle baseline FROZEN: PASS;
- nessuna apertura della Fase 4: PASS.

## 9. Decisioni / proposte

Nessuna nuova decisione metodologica è stata approvata dalla Chat 3.5.

Proposta tecnica da sottoporre alla Chat 0.2:
**OSM substation objects / representative locations + aree convenzionali ufficiali FVG/GSE + cross-check DSO ufficiale** come base dati candidata del futuro proxy territoriale. La geometria target finale (punto rappresentativo oppure geometria OSM completa) resta una scelta metodologica successiva.

Una futura metrica potrebbe misurare la minima distanza tra poligono candidato e geometrie CP-proxy validate in CRS metrico, ma questa scelta resta **PROPOSED** e non è stata implementata né approvata.

## 10. Stato finale e prossimo passo

**READY_WITH_LIMITATIONS / REVIEW**

La Chat 0.2 deve svolgere review indipendente prima di qualsiasi ACCEPTED/FROZEN:
1. verificare la regola QA e i due gap interni;
2. confermare che il livello di copertura sia sufficiente per una pianificazione regionale di massima;
3. decidere se accettare formalmente la combinazione proposta come baseline del proxy;
4. mantenere distinta la futura verifica elettrica reale sui candidati finalisti.

FASE 4: **NON APERTA**.
