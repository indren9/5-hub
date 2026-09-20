# NOTE — ISS-0014 — Riparazione preservation copy G_OSM_operativo_v01

**Data:** 2026-09-20
**Chat:** Chat 0.2 — Chat Madre 5 HUB
**Issue:** ISS-0014
**Stato finale:** RESOLVED
**Ambito:** preservation / integrità artifact, non metodologia scientifica

## 1. Problema

La copia:

`TESI_BASELINE_SAFE\04_FROZEN_CHECKPOINTS\OSM_5_6\grafo_operativo_osm\G_OSM_operativo_v01.gpkg`

aveva SHA-256:

`EB2953DFB05EE71D11688A38D6EEED67412A939F95040DD874FB2B9D192CAB37`

diverso dall'hash FROZEN atteso:

`F1D87245D1BC28F3ECAB16E126514F8A3AB718B73CE7BD244DB2F12628697EF3`

Due copie indipendenti preservate coincidevano invece con l'hash FROZEN atteso.

## 2. Verifica logica prima della riparazione

La Chat 0.2 ha confrontato in sola lettura la copia difforme e una copia FROZEN hash-corretta.

Entrambe:
- dimensione file: 244.686.848 byte;
- `PRAGMA quick_check = ok`;
- stesso schema SQLite/GeoPackage;
- stessi pragma principali;
- stessi conteggi per tutte le tabelle;
- layer principale `G_OSM_operativo_segments_v01`: 944.219 record in entrambe.

È stato inoltre calcolato un hash logico record-per-record sulle tabelle dati principali, includendo i BLOB geometrici.

Esito:
- `G_OSM_operativo_metadata_v01`: MATCH;
- `G_OSM_operativo_segments_v01`: MATCH;
- tabelle `gpkg_*` principali: MATCH;
- `ALL_BASE_TABLES_MATCH = True`.

Hash logico del layer principale:

`CD9C316C779CC94A383B0A880A775AD4789CC269B5C6F9FA673A68B1C6C4CA01`

identico tra copia difforme e copia FROZEN.

Conclusione: la differenza SHA-256 del file era una differenza di serializzazione fisica SQLite/GeoPackage, non una differenza dei dati scientifici o delle geometrie del layer principale.

## 3. Procedura di riparazione

Non è stata effettuata una sovrascrittura in place.

La copia byte-difforme è stata spostata in:

`C:\Users\visen\OneDrive\Università\UniUD\Tesi\90_ARCHIVE\PRESERVATION_REPAIRS\ISS-0014_20260920\G_OSM_operativo_v01_TESI_BASELINE_SAFE_byte_different_EB2953DF.gpkg`

La sorgente usata per ripristinare `TESI_BASELINE_SAFE` è stata:

`TESI_THESIS_STORAGE\04_FROZEN_CHECKPOINTS\RECOVERED_BASELINE\OSM_5_6\grafo_operativo_osm\G_OSM_operativo_v01.gpkg`

Prima della copia è stato verificato l'hash FROZEN della sorgente.

La nuova copia è stata prima materializzata come file temporaneo, verificata con SHA-256, quindi rinominata nel percorso finale.

## 4. Esito

Percorso operativo ripristinato:

`TESI_BASELINE_SAFE\04_FROZEN_CHECKPOINTS\OSM_5_6\grafo_operativo_osm\G_OSM_operativo_v01.gpkg`

SHA-256 dopo la riparazione:

`F1D87245D1BC28F3ECAB16E126514F8A3AB718B73CE7BD244DB2F12628697EF3`

Esito: **PASS**.

La copia difforme resta conservata in archivio come evidenza preservation e non deve essere usata come baseline operativa.

## 5. Impatto sul progetto 5 HUB

Nessuna decisione metodologica cambia.

La baseline Light approvata con DEC-0054 / DEC-0055 resta valida.

ISS-0014 può essere chiusa come `RESOLVED` perché:
- il file operativo in `TESI_BASELINE_SAFE` è stato ripristinato all'hash FROZEN;
- la copia difforme è stata preservata separatamente;
- il confronto logico ha escluso una divergenza dei dati scientifici.
