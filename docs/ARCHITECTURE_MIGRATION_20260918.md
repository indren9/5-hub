# ARCHITECTURE MIGRATION — 2026-09-18

## Decisione

Su approvazione esplicita dell’utente, il repository locale del progetto 5 HUB è stato migrato da:

`C:\Tesi\dev`

a:

`C:\dev\5-hub`

Motivazione: `C:\dev` è il workspace generale dei progetti locali; il progetto 5 HUB deve vivere come repository indipendente al suo interno, non dentro `C:\Tesi`.

## Controlli di migrazione

Prima della migrazione:
- HEAD: `71867bcc5551ff3876af33e5eefe1bf21cbb814b`;
- branch: `main`, `review/chat-1.1-posthandoff`;
- working tree: pulito.
Dopo la migrazione:
- Git root: `C:/dev/5-hub`;
- HEAD invariato: `71867bcc5551ff3876af33e5eefe1bf21cbb814b`;
- branch preservati: `main`, `review/chat-1.1-posthandoff`;
- working tree inizialmente pulito;
- vecchio percorso `C:\Tesi\dev` rimosso dopo verifica del residuo `.git` incompleto lasciato da Windows durante il primo `Move-Item`.

## Impatto governance

- `C:\dev\5-hub` diventa il percorso locale ufficiale di sviluppo e repository Git.
- `C:\Tesi\dev` è DEPRECATED e non deve più essere usato.
- OneDrive tecnico resta invariato.
- Google Drive resta invariato per governance viva.
- La baseline FROZEN di Fase 1 non cambia nel contenuto; cambia solo il percorso locale che la contiene.

## Nota storica

L’handoff Chat 0.1 conserva i riferimenti originali a `C:\Tesi\dev` come evidenza storica, con nota di supersessione aggiunta.
