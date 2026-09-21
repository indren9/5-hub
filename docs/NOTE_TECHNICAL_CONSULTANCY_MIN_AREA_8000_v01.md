# NOTE — Technical consultancy minimum area 8,000 m²

**Date:** 2026-09-21
**Status:** ACCEPTED INPUT / provenance limitation declared

## Source

The user reports that a technical consultancy identified **8,000 m²** as the minimum area to use for candidate Hub polygons.

No underlying consultancy report, signed note, calculation sheet, consultant identity, or other primary documentary evidence has been provided to Chat 0.2 in the current project workspace.

The value is therefore recorded as:

- a **technical requirement communicated by the user**;
- authoritative for the MODEL_v2 because the user is the final project decision authority;
- not independently verified by Chat 0.2;
- not derived from the historical Claude/QGIS threshold of approximately 5,000 m².

## Operational interpretation

For V2-1:

- compute `area_m2` on the candidate polygon after deterministic geometry repair and split of disconnected multipart components;
- use a documented metric CRS;
- include only polygons with `area_m2 >= 8000`;
- exclude polygons with `area_m2 < 8000` using reason `MIN_AREA_8000_NOT_MET`.

The 8,000 m² value refers to **gross polygon area** at strategic-planning scale. It is not a claim that 8,000 m² of net usable/buildable area is available.

If documentary evidence from the consultancy is later supplied, it should be registered and linked without changing the approved threshold unless its content materially contradicts the current interpretation.
