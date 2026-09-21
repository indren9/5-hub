# TRAFFIC INTERCEPTABILITY CRITERION v01

**Data:** 2026-09-21
**Stato:** ACCEPTED — raw formula closed
**Autorità:** DEC-0072 + DEC-0073 + DEC-0074

## 1. Scopo

Il criterio misura il potenziale di traffico veicolare intercettabile da ciascun poligono candidato.

Il criterio è site-level e sostituisce qualsiasi score basato sulla distanza dalla TEN-T.

## 2. Light e Heavy

I flussi Light e Heavy restano distinti.

Per ogni candidato saranno calcolati due valori separati, uno per i flussi Light e uno per i flussi Heavy.

## 3. Raggio di ricerca

Per ogni candidato si considerano gli archi dotati di dati di flusso che ricadono entro **5 km dal bordo del poligono**.

Il raggio di 5 km è una finestra di ricerca e non costituisce da solo una regola di scoring.
## 4. Formula raw e decadimento della distanza

Per ogni arco e entro 5 km dal candidato i, si misura la distanza geometrica d_ie in km fra la geometria del poligono e l'arco.

Il fattore di decadimento è lineare:

`f(d_ie) = 1 - d_ie / 5`, per `0 <= d_ie <= 5`.

Il contributo dell'arco è:

`V_ie = q_e * f(d_ie)`.

Il valore raw del candidato è il massimo contributo fra gli archi entro 5 km:

`F_i = max_e(V_ie)`.

Se non esistono archi utili entro 5 km, `F_i = 0`.

Il calcolo resta separato:
- `F_i^L = max_e(q_e^L * f(d_ie))`;
- `F_i^H = max_e(q_e^H * f(d_ie))`.

## 5. Sensitivity

È ammessa una sensitivity sul raggio di ricerca per verificare la robustezza della scelta dei 5 km.

La sensitivity potrà confrontare 5 km con raggi inferiori o superiori e misurare:
- variazione dell'arco di riferimento;
- variazione dello score;
- variazione del ranking dei candidati;
- eventuale variazione della cinquina finale.

Il raggio baseline resta 5 km salvo futura successor decision.

## 6. Questioni ancora aperte

Restano da definire o verificare:
- artifact canonici dei flussi Light e Heavy;
- unità esatta dei flussi;
- associazione rete/edge ID;
- normalizzazione finale dei due valori raw;
- valori di importanza/peso.
