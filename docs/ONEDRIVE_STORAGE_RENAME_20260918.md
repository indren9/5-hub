# ONEDRIVE STORAGE RENAME — 2026-09-18

## Decisione

Su approvazione esplicita dell’utente, la cartella tecnica OneDrive del progetto è stata rinominata da:

`C:\Users\visen\OneDrive\Università\UniUD\Tesi\project_storage`

a:

`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG`

Motivazione: rendere immediatamente riconoscibile che la cartella appartiene al progetto dei 5 Hub Energetici Green FVG.

## Effetto

La struttura interna resta invariata:
- `00_baseline`
- `01_raw_data`
- `02_external_sources`
- `03_processed_data`
- `04_geodatabases`
- `05_intermediate_outputs`
- `06_final_outputs`
- `07_deliverables`
- `90_archive`

La modifica è una rinomina sullo stesso storage, non una duplicazione dei dati.

Il vecchio percorso `project_storage` è DEPRECATED e non deve più essere usato.

## Verifica

- vecchio percorso assente;
- nuovo percorso presente;
- 9 sottocartelle tecniche presenti;
- baseline QGIS Beltrame ancora accessibile;
- SHA256 del pacchetto QGIS invariato: `AB2591E6DED67D7B165E0702400DF7270EB8EF1966EF80B68C966F0F4459E614`.
