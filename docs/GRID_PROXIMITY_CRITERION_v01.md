# GRID PROXIMITY CRITERION v01

**Data:** 2026-09-22
**Stato:** ACCEPTED
**Autorità:** DEC-0053 + DEC-0078

## 1. Scopo

Il criterio misura la prossimità territoriale di ciascun poligono candidato alla cabina primaria più vicina.

La distanza è usata esclusivamente come proxy di:
- costo potenziale di connessione;
- complessità potenziale della connessione;
- fattibilità energetica territoriale preliminare.

Non rappresenta capacità disponibile o fattibilità tecnica reale.

## 2. Baseline dati

Si usa la baseline elettrica approvata con DEC-0053:
- oggetti/localizzazioni rappresentative OSM `power=substation` validati come CP-proxy;
- aree convenzionali ufficiali FVG/GSE come controllo territoriale e gestore;
- fonti DSO ufficiali come cross-check di currentness, ruolo e tensione.

Restano validi tutti i limiti documentati in `REVIEW_CHAT_3.5_ELECTRIC_GRID_PROXY_v01.md`.

## 3. Distanza raw

Per ogni candidato i:

`d_i = distanza geometrica minima tra il poligono candidato e la cabina primaria più vicina`.

La distanza è misurata dalla geometria del poligono, non dal centroide.

Direzione:
- minore distanza = migliore condizione;
- maggiore distanza = peggiore condizione.

## 4. Normalizzazione data-driven

Sull'intero universo dei candidati si calcola:

`d_max = max_i(d_i)`.

Lo score normalizzato è:

`S_i_GRID = 1 - d_i / d_max`.

Proprietà:
- score in [0,1];
- il candidato più svantaggiato vale 0;
- un candidato con distanza prossima a 0 tende a 1;
- nessuna soglia di distanza artificiale;
- se cambia l'universo candidati può cambiare `d_max` e quindi la scala degli score.

## 5. Interpretazione

Lo score indica esclusivamente la prossimità relativa a una cabina primaria nella baseline territoriale approvata.

Non deve essere interpretato come:
- MW disponibili;
- capacità residua;
- garanzia di connessione;
- fattibilità tecnica definitiva;
- costo reale di connessione;
- punto di consegna;
- necessità o meno di opere di rete.

Tali verifiche restano post-model e richiedono interlocuzione/dati del gestore.

## 6. Stato

Formula e normalizzazione: ACCEPTED con DEC-0078.

L'importanza/peso del criterio sarà assegnata successivamente dall'utente.
