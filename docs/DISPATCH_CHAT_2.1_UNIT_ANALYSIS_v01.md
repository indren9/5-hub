# DISPATCH — Chat 2.1 — Definizione dell’unità elementare di analisi

**Fase:** 2 — Definizione dell’unità elementare di analisi
**Stato mandato:** AUTHORIZED
**Data:** 2026-09-18
**Regia:** Chat Madre 5 HUB

## 1. Obiettivo

Definire in modo metodologicamente solido e riproducibile quale sia l’unità elementare usata dal modello per rappresentare un candidato alla localizzazione di un Hub Energetico Green.

La Chat 2.1 deve produrre una proposta formale da sottoporre alla Chat Madre e all’utente.

**Non deve congelare autonomamente alcuna scelta.**

## 2. Baseline metodologica vincolante

FASE 1 è FROZEN. L’Hub da localizzare:
- integra H₂ pubblico + ricarica elettrica DC pubblica;
- deve servire veicoli leggeri e pesanti;
- è oggetto di un modello di localizzazione, non di progettazione del layout;
- applica i requisiti AFIR/TEN-T solo dove pertinenti alla funzione del sito;
- non richiede FER in sito, H₂ rinnovabile/certificato o altri vettori come componenti universali.
Artifact FROZEN di riferimento:
`docs/FASE_1_HUB_DEFINITION_CONSOLIDATED_v02.md`

Roadmap:
`docs/ROADMAP_METODOLOGICA_v1.md`

La baseline Claude è **HISTORICAL / NON_AUTHORITATIVE**: può essere consultata per capire come il problema era stato rappresentato in precedenza, ma nessuna scelta viene ereditata senza verifica.

## 3. Domanda centrale

La Chat 2.1 deve rispondere in modo esplicito a questa domanda:

> Che cos’è, geometricamente e concettualmente, una singola alternativa candidata che il modello potrà successivamente ammettere, valutare e selezionare?

L’ipotesi indicata nella roadmap — **area candidata fisicamente localizzabile** — è una baseline di lavoro da verificare, non una decisione già FROZEN.

## 4. Questioni da analizzare

### 4.1 Natura dell’unità
Valutare e confrontare almeno:
- area/poligono candidato;
- punto candidato;
- comune o altra unità amministrativa;
- infrastruttura/impianto esistente;
- eventuali modelli ibridi area + punto di accesso/rappresentativo.

Per ogni alternativa indicare vantaggi, limiti e compatibilità con l’obiettivo reale di localizzazione.
### 4.2 Geometria del candidato
Se l’unità proposta è un’area, definire:
- quale geometria rappresenta il candidato;
- come gestire poligoni multipart;
- come trattare aree contigue;
- come trattare sovrapposizioni;
- come evitare duplicazioni dello stesso sito fisico;
- come identificare stabilmente ogni candidato nel tempo.

Non scegliere ancora le fonti definitive dei poligoni: definire i requisiti che tali fonti dovranno soddisfare in Fase 3–4.

### 4.3 Punto rappresentativo
Stabilire se serve e, in caso positivo:
- per quali calcoli;
- come viene determinato;
- perché non deve essere confuso con la futura posizione fisica dell’impianto;
- quando un semplice centroide è inadeguato;
- se può servire più di un punto operativo per candidato.

### 4.4 Accesso stradale
Definire concettualmente:
- cosa rappresenta il punto/segmento di accesso di un candidato;
- come collegare l’area alla rete stradale;
- come evitare che una distanza calcolata dal centroide produca falsi risultati;
- come trattare candidati con più accessi potenziali.
### 4.5 Regole di distanza
Definire una tassonomia esplicita delle distanze da usare in seguito, distinguendo quando pertinente:
- distanza euclidea area-feature;
- distanza dal bordo del poligono;
- distanza dal punto di accesso;
- distanza lungo rete stradale;
- distanza tra aree;
- distanza da uscite TEN-T.

Non calcolare ancora indicatori né fissare soglie arbitrarie.

### 4.6 Scala e precisione
Stabilire quali proprietà minime deve avere la geometria affinché:
- i vincoli localizzativi siano verificabili;
- non si attribuisca falsa precisione a dati troppo grossolani;
- sia possibile passare successivamente dalla selezione territoriale alla verifica puntuale del sito.

## 5. Cose da NON fare

La Chat 2.1 non deve:
- costruire l’universo dei candidati;
- scegliere i 5 Hub;
- creare ranking o punteggi;
- definire indicatori o pesi;
- introdurre soglie di superficie senza evidenza;
- progettare layout o impianti;
- modificare la baseline FROZEN di Fase 1;
- trasformare automaticamente il metodo Claude nella nuova metodologia.
## 6. Output richiesto

Creare nel repository un artifact di review, ad esempio:
`docs/FASE_2_UNIT_ANALYSIS_REVIEW_v01.md`

Il documento deve contenere almeno:
1. definizione delle alternative concettuali considerate;
2. confronto motivato;
3. proposta di unità elementare;
4. specifica formale della geometria;
5. regola del punto rappresentativo;
6. regola dell’accesso stradale;
7. tassonomia delle distanze;
8. gestione di contiguità, sovrapposizioni e multipart;
9. regole per identificativo univoco/versionamento;
10. implicazioni per Fase 3 e Fase 4;
11. questioni aperte e decisioni da sottoporre all’utente.

Distinguere sempre:
- dato osservato;
- requisito normativo;
- assunzione;
- proxy;
- scelta metodologica proposta.

## 7. Quality gate della Chat 2.1

La Chat 2.1 può dichiararsi PASS solo se:
- ogni futuro calcolo spaziale ha una geometria di riferimento concettualmente definita;
- area, punto rappresentativo e accesso stradale non vengono confusi;
- non sono introdotte soglie arbitrarie;
- le alternative scartate sono motivate;
- restano evidenti le decisioni che richiedono approvazione dell’utente;
- artifact, controlli, Git commit e SESSION CLOSE/handoff sono completati.
## 8. Handoff obbligatorio

Alla chiusura riportare alla Chat Madre:
- numero e nome: Chat 2.1 — Definizione dell’unità elementare di analisi;
- obiettivo;
- lavoro svolto;
- proposta metodologica;
- alternative analizzate;
- decisioni richieste all’utente;
- file creati/modificati e percorsi;
- controlli e relativo esito;
- commit Git;
- problemi aperti;
- stato finale;
- prossimo passo suggerito.

**La Chat 2.1 non può dichiarare FASE 2 FROZEN o CLOSED.**
