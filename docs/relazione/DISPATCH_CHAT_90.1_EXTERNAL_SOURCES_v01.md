# DISPATCH — Chat 90.1 — Fonti esterne e bibliografia

**Parent:** Chat 90.0 — Relazione Builder  
**Data:** 2026-09-21  
**Mandato:** esclusivamente editoriale/documentale  
**Autorità metodologica:** nessuna  
**Governance:** DEC-0060; REVIEW_CHAT_90.0_RELATION_BUILDER_v01.md

## Obiettivo

Costruire il registro verificato delle fonti esterne della relazione, partendo da:
- EXTERNAL_SOURCE_REGISTER_TEMPLATE_v01.csv;
- DATA_REGISTRY;
- fonti già validate nelle Fasi 1–3;
- eventuali piste recuperate dalla baseline storica Claude/QGIS.

Il risultato deve permettere a un lettore esterno di risalire alle fonti originali effettivamente usate nel report.

## Input vincolanti

Leggere prima:
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER, in particolare DATA_REGISTRY;
- docs/relazione/RELATION_ARCHITECTURE_v01.md;
- docs/relazione/EXTERNAL_SOURCE_REGISTER_TEMPLATE_v01.csv;
- docs/relazione/CLAUDE_BASELINE_EDITORIAL_USE_v01.md;
- docs/relazione/REVIEW_CHAT_90.0_RELATION_BUILDER_v01.md;
- baseline/review ACCEPTED o FROZEN che citano le fonti da registrare.

## Attività

1. Trasformare il template in un registro reale e normalizzato.
2. Per ogni fonte individuare, quando esiste:
   - titolo ufficiale;
   - ente/autore;
   - atto o identificatore;
   - versione/data;
   - URL o identificatore persistente;
   - data di accesso;
   - copertura territoriale/temporale;
   - uso effettivo nella relazione;
   - licenza/condizioni di riuso se rilevanti;
   - stato di verifica;
   - eventuale percorso di evidenza preservata.
3. Usare fonti istituzionali/originali come prima scelta.
4. Separare record distinti per dataset distinti: non lasciare record-ombrello se nella relazione vengono citati dataset specifici.
5. Verificare le piste Claude sulla fonte originale prima di promuoverle.
6. Non selezionare letteratura metodologica per tecniche non ancora approvate.
7. Evidenziare fonti non verificabili o versioni non determinabili senza colmare implicitamente il gap.

## Output richiesti

- aggiornamento di docs/relazione/EXTERNAL_SOURCE_REGISTER_v01.csv;
- eventuale docs/relazione/EXTERNAL_SOURCE_NOTES_v01.md per problemi bibliografici o versioning;
- HANDOFF_CHAT_90.1_EXTERNAL_SOURCES_v01.md.

## Quality gate

PASS solo se:
- ogni record usato come fonte corrente ha una fonte originale verificata;
- URL/identificatori e versioni sono compilati quando reperibili;
- portali e singoli dataset sono distinti correttamente;
- Claude non compare come fonte fattuale corrente;
- fonti esterne e riferimenti interni non sono mescolati;
- i gap sono espliciti;
- CSV parsabile e git diff --check PASS.

## Stop condition

Non prendere decisioni su criteri, indicatori, pesi, soglie o interpretazioni metodologiche. In caso di dubbio sostanziale, registrare la questione e riportarla alla Chat 90.0.
