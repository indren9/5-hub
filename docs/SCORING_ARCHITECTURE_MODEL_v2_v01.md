# SCORING ARCHITECTURE MODEL_v2 v01

**Data:** 2026-09-21
**Stato:** ACCEPTED
**Autorità:** DEC-0070

## 1. Principio generale

L'architettura di scoring del MODEL_v2 deve essere semplice, trasparente e decomponibile.

Una volta costruito l'universo candidato secondo la baseline approvata, non è prevista una seconda fase ordinaria di eliminazione site-level.

I candidati sono considerati ammissibili per costruzione e vengono successivamente confrontati mediante criteri di valutazione.

Restano possibili:
- correzioni QA;
- aggiornamenti della baseline approvati;
- vincoli applicati alla configurazione complessiva dei cinque Hub.

## 2. Importanza dei criteri e pesi

Per ogni criterio j viene assegnata un'importanza intera:

r_j ∈ {1, 2, 3, 4, 5}

I valori vengono convertiti in pesi percentuali normalizzati:

w_j = r_j / Σ_j r_j

Di conseguenza:

Σ_j w_j = 1

I valori concreti r_j non sono ancora approvati.

## 3. Normalizzazione degli indicatori

Ogni criterio viene trasformato/normalizzato su una scala comune prima dell'aggregazione.

Per il candidato i e il criterio j si indica con:

z_ij = valore normalizzato del criterio j per il candidato i

La specifica trasformazione/normalizzazione di ciascun indicatore resta da definire insieme alla relativa formula raw, direzione preferenziale, trattamento dei missing e degli eventuali outlier.

Non viene qui imposto automaticamente il min-max per tutti gli indicatori.

## 4. Score del singolo candidato

Lo score complessivo del candidato i è:

S_i = Σ_j (w_j × z_ij)

Essendo i pesi normalizzati a somma 1, S_i è una media pesata dei criteri normalizzati.

Per ogni candidato devono restare tracciabili:
- valori raw;
- valori normalizzati;
- importanza 1–5;
- peso percentuale risultante;
- contributo di ciascun criterio;
- score complessivo.

## 5. Score della cinquina

Per una configurazione C composta esattamente da cinque Hub:

Q(C) = (1/5) × Σ_{i∈C} S_i

La qualità individuale della cinquina è quindi la media aritmetica degli score dei cinque siti.

Poiché tutte le configurazioni contengono esattamente cinque Hub, massimizzare la media equivale a massimizzare la somma degli score individuali; la media viene mantenuta perché più leggibile e confrontabile.

## 6. Vincoli di configurazione

Lo score Q non rende automaticamente valida una cinquina.

La selezione finale confronta solo configurazioni che soddisfano i vincoli di configurazione approvati.

In particolare DEC-0069 stabilisce che la conformità AFIR/TEN-T opera a livello della configurazione complessiva.

Quindi:
1. si valuta ogni candidato;
2. si costruiscono/verificano le cinquine ammissibili rispetto ai vincoli di configurazione;
3. tra le cinquine valide, si confronta/massimizza Q.

## 7. Cosa è chiuso e cosa resta aperto

ACCEPTED:
- niente seconda fase ordinaria di esclusione site-level;
- importanza criteri su scala 1–5;
- conversione delle importanze in pesi percentuali;
- normalizzazione prima dell'aggregazione;
- score candidato come media pesata;
- score cinquina come media dei cinque score;
- separazione fra score e vincoli di configurazione.

PENDING:
- elenco definitivo dei criteri;
- formule raw;
- trasformazioni/normalizzazioni criterio-specifiche;
- valori di importanza 1–5;
- trattamento missing/outlier;
- formalizzazione computazionale dei vincoli di configurazione;
- eventuali macro-aree/top-k/distanza minima tra Hub.
