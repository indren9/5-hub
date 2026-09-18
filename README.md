# 5 Hub Energetici Green FVG — dev

Repository locale di sviluppo del progetto per la localizzazione dei 5 Hub Energetici Green in Friuli Venezia Giulia.

## Ruolo di questa cartella

`C:\dev\5-hub` contiene codice, configurazioni, test, script, notebook, documentazione tecnica e file leggeri necessari alla riproducibilità.

I dati pesanti e gli output voluminosi devono vivere in:
`C:\Users\visen\OneDrive\Università\UniUD\Tesi\project_storage`

La governance viva e i documenti autorevoli restano su Google Drive.

## Struttura

- `src/` — codice principale
- `config/` — configurazioni e parametri
- `tests/` — test e controlli
- `scripts/` — utility e procedure operative
- `notebooks/` — analisi esplorative
- `docs/` — documentazione tecnica
- `environment/` — ambiente e dipendenze
- `logs/` — log locali
- `tmp/` — file temporanei non autorevoli

## Regole essenziali

Non incorporare automaticamente materiale storico. Non versionare dati pesanti, geodatabase, raster, output voluminosi o credenziali. Preferire percorsi configurabili agli hard-code negli script.
