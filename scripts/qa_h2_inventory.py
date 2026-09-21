from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "data" / "interim" / "H2_FVG_INFRASTRUCTURE_INVENTORY_v01.csv"
SOURCES = ROOT / "docs" / "H2_FVG_SOURCE_REGISTER_v01.csv"
LOG = ROOT / "logs" / "H2_FVG_INFRASTRUCTURE_INVENTORY_QA_v01.txt"

ALLOWED_STATUS = {
    "OPERATIONAL",
    "UNDER_CONSTRUCTION",
    "FUNDED_COMMITTED",
    "PLANNED_AUTHORIZED",
    "ANNOUNCED_UNVERIFIED",
    "UNKNOWN",
}
ID_RE = re.compile(r"^FVG_H2_\d{3}$")
VERIFY_DATE = "2026-09-22"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    rows = read_csv(INVENTORY)
    sources = read_csv(SOURCES)
    source_ids = {r["SOURCE_ID"] for r in sources if r.get("SOURCE_ID")}
    ids = [r.get("H2_SITE_ID", "") for r in rows]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate H2_SITE_ID detected.")

    for i, r in enumerate(rows, start=2):
        rid = r.get("H2_SITE_ID", "")
        if not ID_RE.match(rid):
            errors.append(f"Row {i}: invalid H2_SITE_ID {rid!r}.")
        if r.get("STATUS") not in ALLOWED_STATUS:
            errors.append(f"{rid}: invalid STATUS {r.get('STATUS')!r}.")
        if r.get("VERIFIED_ON") != VERIFY_DATE:
            errors.append(f"{rid}: VERIFIED_ON is not {VERIFY_DATE}.")
        if not r.get("PRIMARY_SOURCE_ID"):
            errors.append(f"{rid}: PRIMARY_SOURCE_ID missing.")
        elif r["PRIMARY_SOURCE_ID"] not in source_ids:
            errors.append(f"{rid}: PRIMARY_SOURCE_ID {r['PRIMARY_SOURCE_ID']} not in source register.")
        if not r.get("LOCATION_SOURCE_ID"):
            errors.append(f"{rid}: LOCATION_SOURCE_ID missing.")
        else:
            for sid in r["LOCATION_SOURCE_ID"].split(";"):
                if sid and sid not in source_ids:
                    errors.append(f"{rid}: LOCATION_SOURCE_ID {sid} not in source register.")
        if not r.get("LOCATION_TEXT"):
            errors.append(f"{rid}: LOCATION_TEXT missing.")

        lat, lon = r.get("LATITUDE", ""), r.get("LONGITUDE", "")
        if bool(lat) != bool(lon):
            errors.append(f"{rid}: latitude/longitude must be both present or both blank.")
        if lat and lon:
            try:
                lat_f, lon_f = float(lat), float(lon)
                if not (-90 <= lat_f <= 90 and -180 <= lon_f <= 180):
                    errors.append(f"{rid}: coordinate out of range.")
            except ValueError:
                errors.append(f"{rid}: non-numeric coordinate.")

        for field in ("SECONDARY_SOURCE_ID",):
            for sid in r.get(field, "").split(";"):
                if sid and sid not in source_ids:
                    errors.append(f"{rid}: {field} {sid} not in source register.")
    # Semantic safeguards required by the dispatch.
    for r in rows:
        rid = r["H2_SITE_ID"]
        if r["STATUS"] == "ANNOUNCED_UNVERIFIED" and r["SCOPE_CLASS"] == "CORE_H2_INFRA":
            errors.append(f"{rid}: announced/unverified record cannot be silently tagged CORE_H2_INFRA.")
        # Capacity natures are stored in separate text fields to prevent unit/nature conflation.
        for cap_field in ("ELECTROLYZER_POWER", "PRODUCTION_CAPACITY", "REFUELING_CAPACITY", "STORAGE_CAPACITY", "OTHER_CAPACITY"):
            if cap_field not in r:
                errors.append(f"{rid}: required capacity-nature field {cap_field} missing from schema.")

    name_keys = [(r["NAME"].strip().casefold(), r["COMUNE"].strip().casefold()) for r in rows]
    if len(name_keys) != len(set(name_keys)):
        warnings.append("Potential duplicate NAME+COMUNE detected.")

    status_counts = Counter(r["STATUS"] for r in rows)
    type_counts = Counter(r["TYPE"] for r in rows)
    scope_counts = Counter(r["SCOPE_CLASS"] for r in rows)

    lines = []
    lines.append("H2 FVG INFRASTRUCTURE INVENTORY QA v01")
    lines.append(f"Inventory: {INVENTORY}")
    lines.append(f"Sources: {SOURCES}")
    lines.append(f"Records: {len(rows)}")
    lines.append(f"Source records: {len(sources)}")
    lines.append("")
    lines.append("STATUS COUNTS")
    for k in sorted(ALLOWED_STATUS):
        lines.append(f"{k}: {status_counts.get(k, 0)}")
    lines.append("")
    lines.append("TYPE COUNTS")
    for k, v in sorted(type_counts.items()):
        lines.append(f"{k}: {v}")
    lines.append("")
    lines.append("SCOPE COUNTS")
    for k, v in sorted(scope_counts.items()):
        lines.append(f"{k}: {v}")
    lines.append("")
    lines.append("WARNINGS")
    lines.extend(warnings or ["NONE"])
    lines.append("")
    lines.append("ERRORS")
    lines.extend(errors or ["NONE"])
    lines.append("")
    lines.append("RESULT: " + ("PASS" if not errors else "FAIL"))

    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
