# DQ-01 APPROVAL — Candidate Universe Contract v01

**Date:** 2026-09-21
**Status:** ACCEPTED
**Authority:** explicit user approval

## Approved package

DQ-01 is approved with the following configuration:

- A2 — official best-available current-first planning geometry;
- B4 — current-first hierarchy with CER/Mosaicatura PRG 2018 only as declared historical fallback;
- C3+ — five generator classes:
  - G1_PRODUCTIVE;
  - G2_COMMERCIAL_TERTIARY;
  - G3_LOGISTICS_TRANSPORT;
  - G4_MIXED_RELEVANT;
  - G5_TECHNICAL_UTILITY_ENERGY;
- D2 — preserve source features; split disconnected multipart; merge only when logical identity is documented;
- E4 — minimum gross candidate-polygon area = **8,000 m²**, from technical consultancy communicated by the user;
- F2 amended — technical/scope gates only, including the approved 8,000 m² minimum-area gate;
- G3 — stable logical candidate_id + candidate_version + universe_version + geometry_hash;
- H2 — structural, lineage, source-gap and deterministic QA; historical Claude candidate count is not a target.

## Meaning of the 8,000 m² threshold

The minimum-area rule is a genuine HARD prefilter of the candidate universe.

Operational rule:

`area_m2 >= 8000` → eligible to remain in the candidate universe if all other technical gates pass.

`area_m2 < 8000` → exclude with `MIN_AREA_8000_NOT_MET`.

The area is measured after deterministic repair and split of disconnected multipart components and represents gross polygon area, not verified net usable/buildable area.

## Consequence

DQ-01 = ACCEPTED.

Construction of CANDIDATE_UNIVERSE_v01 and CANDIDATE_LINEAGE_v01 may now be authorized under the accepted contract.

DQ-02 and all later multicriteria decisions remain not approved.
