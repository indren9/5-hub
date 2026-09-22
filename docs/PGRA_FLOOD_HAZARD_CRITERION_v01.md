# PGRA FLOOD HAZARD CRITERION v01

**Data:** 2026-09-22
**Stato:** ACCEPTED
**Autorità:** DEC-0082 + DEC-0084

## 1. Baseline

Il criterio usa la baseline PGRA operativa verificata in Chat 3.11:
`sigma:Pericolo_direttiva_alluvioni`
materializzata nello snapshot FVG/envelope del 2026-09-20.

Schema rilevante:
- `OBJECTID`;
- `PDESCRIPT`.

Classi osservate nel layer:
- `AA` = Zona di Attenzione;
- `F` = Area fluviale;
- `P1_ST` = Pericolosità idraulica moderata (P1) da criterio storico;
- `P1_SM` = Pericolosità idraulica moderata (P1) da scolo meccanico;
- `P1` = Pericolosità idraulica moderata;
- `P2` = Pericolosità idraulica media;
- `P3A` = Pericolosità idraulica elevata (P3a);
- `P3B` = Pericolosità idraulica elevata (P3b).

`P1_ST` e `P1_SM` sono trattate come sottotipi di `P1`, non come livelli autonomi.

## 2. Scala approvata

| Classe | Score |
|---|---:|
| Fuori P1–P3B | 1.00 |
| P1 / P1_ST / P1_SM | 0.75 |
| P2 | 0.50 |
| P3A | 0.25 |
| P3B | 0.00 |

`AA` e `F` non entrano nella graduatoria P1–P3B e restano informazioni/flag separati.

## 3. Score candidato

Per ogni candidato si calcola la quota di superficie ricadente in ciascuna classe.

Lo score è la media pesata per superficie:

`S_i_PGRA = sum_k (share_ik * score_k)`

dove `share_ik` è la quota di superficie del candidato assegnata alla classe k.

In caso di sovrapposizione geometrica tra più classi, sulla superficie sovrapposta prevale la classe peggiore, evitando doppio conteggio.

## 4. Interpretazione

Score alto = minore esposizione territoriale alle classi di pericolosità PGRA considerate.

Lo score non sostituisce la verifica normativa o idraulica puntuale del finalista e non equivale a dichiarazione di edificabilità o fattibilità.

## 5. Stato

Formula e scala: ACCEPTED con DEC-0084.
