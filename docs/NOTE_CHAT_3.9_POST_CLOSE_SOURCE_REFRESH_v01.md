# NOTE — Chat 3.9 post-close source refresh v01

**Data verifica:** 2026-09-20  
**Tipo:** nota tecnica di preservation, senza modifica metodologica

Dopo la chiusura operativa e la review Chat Madre della Chat 3.9, il processo di acquisizione fonti è stato rieseguito una volta sui medesimi 43 URL istituzionali.

## Esito

Stato alla SESSION CLOSE / DEC-0047:
- 34 fonti materializzate;
- 9 fonti non materializzate.

Stato dopo il refresh post-close:
- 35 fonti materializzate;
- 8 fonti non materializzate.

Manifest corrente:
- `5_HUB_FVG\02_external_sources\F3_CHAT_3_9\source_manifest_v01.json`
- SHA-256: `CE020A4D15E33D7E43B7D91F05EA04DDD5A0E6FE68092A2B7D2F11DBE4AB4CA4`

Preservation corrente:
- 43 item;
- 35 materializzati;
- 8 non materializzati;
- 0 file mancanti;
- 0 mismatch SHA-256;
- 0 mismatch dimensione.

## Controllo di non regressione

Confronto con gli output accettati con DEC-0047:
- differenze non legate a preservation nella coverage: 0;
- differenze non legate a preservation nei risultati: 0;
- coverage invariata: 215 Comuni, 215 codici ISTAT univoci;
- distribuzione invariata: 4 CURRENT_VECTOR_VERIFIED / 4 CURRENT_PLAN_VERIFIED_NO_VECTOR / 207 CURRENT_SOURCE_FOUND_LINEAGE_INCOMPLETE / 0 TO_VERIFY.

Il refresh modifica esclusivamente campi di materializzazione/hash e il relativo riepilogo QA/evidence.

## Interpretazione

La SESSION CLOSE originale resta storicamente corretta: al momento della chiusura risultavano 34 fonti materializzate e 9 non materializzate.

Il refresh post-close non riapre Chat 3.9, non modifica DEC-0047, non altera la coverage urbanistica e non introduce nuove decisioni metodologiche.

Gli output correnti vengono versionati per mantenere allineati repository e storage tecnico con lo stato effettivo della preservation.
