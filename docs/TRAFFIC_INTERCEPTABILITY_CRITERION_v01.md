# TRAFFIC INTERCEPTABILITY CRITERION v01

**Data:** 2026-09-21
**Stato:** ACCEPTED — partial specification
**Autorità:** DEC-0072 + DEC-0073

## 1. Scopo

Il criterio misura il potenziale di traffico veicolare intercettabile da ciascun poligono candidato.

Il criterio è site-level e sostituisce qualsiasi score basato sulla distanza dalla TEN-T.

## 2. Light e Heavy

I flussi Light e Heavy restano distinti.

Per ogni candidato saranno calcolati due valori separati, uno per i flussi Light e uno per i flussi Heavy.

## 3. Raggio di ricerca

Per ogni candidato si considerano gli archi dotati di dati di flusso che ricadono entro **5 km dal bordo del poligono**.

Il raggio di 5 km è una finestra di ricerca e non costituisce da solo una regola di scoring.
## 4. Ruolo della distanza

La distanza fra poligono e arco deve incidere sul criterio mediante una funzione di penalizzazione/decadimento.

La funzione non è ancora approvata.

Non è quindi ancora approvata la formula raw finale del criterio.

## 5. Sensitivity

È ammessa una sensitivity sul raggio di ricerca per verificare la robustezza della scelta dei 5 km.

La sensitivity potrà confrontare 5 km con raggi inferiori o superiori e misurare:
- variazione dell'arco di riferimento;
- variazione dello score;
- variazione del ranking dei candidati;
- eventuale variazione della cinquina finale.

Il raggio baseline resta 5 km salvo futura successor decision.

## 6. Questioni ancora aperte

Restano da definire:
- artifact canonici dei flussi Light e Heavy;
- unità esatta dei flussi;
- associazione rete/edge ID;
- funzione di penalizzazione della distanza;
- regola di selezione/aggregazione tra più archi entro 5 km;
- gestione dei candidati senza archi utili entro 5 km;
- normalizzazione;
- valori di importanza/peso.
