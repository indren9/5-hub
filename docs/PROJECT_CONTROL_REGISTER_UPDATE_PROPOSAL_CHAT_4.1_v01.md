# PROJECT CONTROL REGISTER — proposta aggiornamenti Chat 4.1 v01

**Chat:** 4.1 — Costruzione universo candidati V2-1
**Data:** 2026-09-21
**Stato:** PROPOSED FOR CHAT 0.2 REVIEW

La Chat 4.1 non assegna autonomamente nuovi codici DEC/ISS né marca artifact ACCEPTED/FROZEN.
Propone alla Chat 0.2 i seguenti aggiornamenti della governance viva.

## DATA_REGISTRY — proposta

Registrare `CANDIDATE_UNIVERSE_v01` come dataset derivato **REVIEW**:
- ruolo: universo dei poligoni candidati V2-1;
- geometria: Polygon, EPSG:6708;
- record: 3.993;
- storage: `04_geodatabases/V2_1_CANDIDATE_UNIVERSE/CANDIDATE_UNIVERSE_v01.gpkg`;
- SHA-256: `78FF0CB21A60C05F7108D54918E7D0491F29A2DAFBE2E08ABA496F8509AB8DD7`;
- logical SHA-256 universe: `648A76F925FE65567CB88CE688A1C41F158DC1C8B90E1E95BCABEA7611D38F39`;
- metodologia: DQ-01 / DEC-0065;
- stato quality gate Chat 4.1: PROPOSED PASS.


Registrare come artifact associati:
- `CANDIDATE_LINEAGE_v01.csv`;
- `CANDIDATE_EXCLUSIONS_v01.csv`;
- `CANDIDATE_SOURCE_GAPS_v01.csv`;
- `CANDIDATE_UNIVERSE_MANIFEST_v01.json`;
- `V2_1_CANDIDATE_UNIVERSE_QA_v01.json`;
- `docs/CANDIDATE_GENERATOR_CLASS_MAPPING_v01.csv`.

## ISSUES — proposta

Valutare se registrare o aggiornare issue non bloccanti per:
1. 5 Comuni `NO_USABLE_POLYGON_SOURCE`: Preone, Stregna, Rivignano Teor,
   Treppo Ligosullo, Valvasone Arzene;
2. 103 Comuni S4 / 1.062 candidati basati su CER 2018 storico;
3. 703 categorie native `GENERATOR_CLASS_UNRESOLVED`, escluse conservativamente;
4. 461 coppie di candidati con overlap areale positivo, mantenute separate in assenza
   di evidenza di identità o soglia di overlap approvata;
5. warning geometrici sorgente OGR/pyogrio, con 0 geometrie invalide residue nell'output.

Questi punti sono limiti di copertura/qualità e non introducono nuovi HARD filter.
