# DISPATCH — Chat 90.2 — Matrice di tracciabilità interna

**Parent:** Chat 90.0 — Relazione Builder  
**Data:** 2026-09-21  
**Mandato:** esclusivamente editoriale/documentale  
**Autorità metodologica:** nessuna  
**Governance:** DEC-0060; REVIEW_CHAT_90.0_RELATION_BUILDER_v01.md

## Obiettivo

Consolidare la matrice di tracciabilità interna della relazione senza trasferire la governance interna nel corpo narrativo destinato al lettore esterno.

## Input vincolanti

Leggere:
- PROJECT_SOURCE_OF_TRUTH;
- PROJECT_CONTROL_REGISTER: DECISIONS, DATA_REGISTRY, ISSUES;
- docs/relazione/RELATION_ARCHITECTURE_v01.md;
- docs/relazione/RELATION_TRACEABILITY_MATRIX_v01.csv;
- docs/relazione/EDITORIAL_GAPS_v01.md;
- docs/relazione/REVIEW_CHAT_90.0_RELATION_BUILDER_v01.md;
- baseline FROZEN, review ACCEPTED, artifact e handoff pertinenti.

## Attività

1. Verificare riga per riga la matrice v01 contro governance viva e repository.
2. Produrre una v02 che mantenga almeno:
   - sezione della relazione;
   - claim/tema;
   - readiness;
   - stato interno;
   - decisioni rilevanti;
   - baseline FROZEN/ACCEPTED;
   - DATA_REGISTRY;
   - review/handoff;
   - artifact tecnico;
   - commit quando materialmente utile;
   - issue/gap;
   - note di aggiornamento.
3. Inserire DEC-0060 e la review Chat 90.0 solo dove servono per governance editoriale/Appendice A, non come sostegno di claim scientifici.
4. Controllare che ogni capitolo READY abbia una lineage sufficiente.
5. Controllare che PARTIAL/NOT_READY non siano rappresentati come consolidati.
6. Segnalare contraddizioni tra fonti interne autorevoli senza risolverle autonomamente.

## Output richiesti

- docs/relazione/RELATION_TRACEABILITY_MATRIX_v02.csv;
- eventuale docs/relazione/TRACEABILITY_NOTES_v01.md;
- HANDOFF_CHAT_90.2_TRACEABILITY_v01.md.

## Quality gate

PASS solo se:
- ogni riga è riconciliata con la governance corrente;
- nessun DEC/ISS è usato come bibliografia esterna;
- nessun claim scientifico dipende solo da una conversazione;
- READY/PARTIAL/NOT_READY restano coerenti con lo stato scientifico;
- contraddizioni e gap sono espliciti;
- CSV parsabile e git diff --check PASS.

## Stop condition

Non modificare stati metodologici e non interpretare il silenzio come approvazione. Qualunque conflitto sostanziale viene riportato alla Chat 90.0.
