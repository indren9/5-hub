# EXTERNAL SOURCE NOTES v01

**Data:** 2026-09-21
**Owner:** Chat 90.0 / seed per Chat 90.1
**Stato:** WORKING

## Seed verificato

È stato avviato il controllo editoriale delle fonti esterne più stabili.

### AFIR
Verificata su EUR-Lex la fonte ufficiale del Regolamento (UE) 2023/1804. EUR-Lex indica come versione consolidata corrente quella del 2026-01-08. Il controllo svolto riguarda metadati, identificatore e currentness della fonte; la Chat 90.1 deve ancora verificare gli articoli effettivamente richiamati nella relazione.

### TEN-T
Verificato su EUR-Lex il Regolamento (UE) 2024/1679. La fonte normativa deve restare separata dal dato cartografico TENtec.

### LR FVG 19/2012
Verificata la pagina Lexview regionale della Legge regionale 11 ottobre 2012, n. 19, "Norme in materia di energia e distribuzione dei carburanti". Lexview espone un testo vigente dal 2026-01-01 e dichiara esplicitamente di non sostituire la pubblicazione ufficiale. La verifica degli articoli concretamente rilevanti resta compito della Chat 90.1.

### TENtec
Verificata la pagina ufficiale della Commissione europea che descrive TENtec come sistema informativo della Commissione per la politica TEN-T e collega la map library delle reti comprehensive, extended core e core. Il record deve essere ulteriormente riconciliato con il dataset/geometria esatto già validato nel progetto 5 HUB.

## Cosa NON è ancora verificato

Il seed non chiude il registro. Restano da normalizzare/verificare almeno: singoli dataset IRDAT; PGRA e PAI; PPR; Natura 2000 e prevalutazioni quando consolidati; OSM/Overpass; dataset ISTAT distinti; fonti GSE/DSO/Terna distinte; eventuale letteratura metodologica solo dopo approvazione delle tecniche effettivamente adottate.

## Regola

SOURCE_METADATA_VERIFIED significa soltanto che identità, ente, identificatore/versione e fonte primaria sono stati controllati. Non equivale a verifica di ogni claim normativo che verrà scritto nel report.
