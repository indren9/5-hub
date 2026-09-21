# LOGISTICS INDUSTRIAL PROXIMITY CRITERION v01

**Data:** 2026-09-22
**Stato:** ACCEPTED
**Autorità:** DEC-0079 + DEC-0080

## 1. Scopo

Il criterio misura quanto ciascun poligono candidato sia ben posizionato rispetto ai poli logistici/industriali della baseline operativa.

## 2. Baseline dati

Si usa `LOGISTICS_FVG_v02.gpkg / LOGISTICS_FVG_POINTS`, approvato con DEC-0079.

Il dataset contiene 26 `SITE_ID` con geometrie POINT in EPSG:32632.

## 3. Distanze

Per ogni candidato i si calcolano le 26 distanze geometriche point-to-polygon e si ordinano in senso crescente.

Si prendono le due distanze minori:
- `d_i(1)` = distanza dal polo più vicino;
- `d_i(2)` = distanza dal secondo polo più vicino.

## 4. Valore aggregato

Si calcola:

`D_i = (d_i(1) + d_i(2)) / 2`.

Quindi un candidato viene favorito se è vicino non a un solo polo, ma a due poli.

## 5. Normalizzazione data-driven

Sull'intero universo candidati si calcola:

`D_max = max_i(D_i)`.

Lo score è:

`S_i_LOG = 1 - D_i / D_max`.

Proprietà:
- score in [0,1];
- candidato più svantaggiato = 0;
- nessuna soglia artificiale;
- nessun bonus aggiuntivo;
- nessun peso diverso per tipologia di polo;
- tutti i 26 poli servono solo a identificare i due più vicini.

## 6. Caveat

`SITE_ID 25 — ZIMA` mantiene il flag `NEEDS_HUMAN_CHECK`.

Il dataset Tesi resta PASS_WITH_LIMITATION / WORKING / NOT FROZEN, ma è baseline operativa ACCEPTED nel MODEL_v2.

Se cambia l'universo candidati può cambiare `D_max` e quindi la scala degli score.

## 7. Stato

Formula e normalizzazione: ACCEPTED con DEC-0080.

L'importanza/peso del criterio sarà assegnata successivamente dall'utente.
