"""Authoritative implementation rules for V2-1 candidate-universe build."""
from __future__ import annotations

import hashlib
import re
import unicodedata

import pandas as pd
import shapely
from shapely.geometry import GeometryCollection, MultiPolygon, Polygon

EXCLUDE_PATH = re.compile(
    r"acust|vincol|ppr|pai|pgra|pericol|bosch|acqu|alber|prat|fasce|rispett|"
    r"elettrod|metanod|incend|ciclab|supporto|patrimonio|salvaguard|bonifica|"
    r"argine|sponde|strad|telefon", re.I
)
GOOD_PATH = re.compile(
    r"zonizz|azzon|zone.?omogene|zona1|prgzone|prgc.?coordinato|"
    r"(^|[/\\])zone?([_. /\\]|$)", re.I
)
ZONE_FIELD = re.compile(r"(^|[|])(ZONA_OM|ZONA_OMOGE|ZTO)([|]|$)", re.I)

SEMANTIC_FIELDS = {
    "ZONA_OM", "ZONA_OMOGE", "ZONA", "ZONE", "ZTO", "TIPO", "CODICE_ZON",
    "CODICE", "SIGLA", "CATEGORIA", "ZONA_DESC", "DEST_PREV", "DESCRIZION",
    "DESCRIZ", "DESCRIZIONE", "LEGENDA", "TESTO_VIS", "TESTO_VISIB",
    "TESTO_VISI", "SOTTOZONA", "CLASSIFICA", "CLASSIFICAZ", "NOTE_DES",
    "NOTE", "ART_NTA", "NOME_OGG", "TIPO_SERV", "TIPO_SERVI", "SERVIZIO",
}
CODE_FIELDS = [
    "ZONA_OM", "ZONA_OMOGE", "ZTO", "ZONA", "ZONE", "TIPO",
    "CODICE_ZON", "CODICE", "SIGLA", "CATEGORIA",
]


def norm(value: object) -> str:
    s = unicodedata.normalize("NFKD", str(value or ""))
    s = "".join(ch for ch in s if not unicodedata.combining(ch)).lower()
    return re.sub(r"\s+", " ", s).strip()


def first_value(row: pd.Series, priorities: list[str] = CODE_FIELDS) -> str:
    cols = {c.upper(): c for c in row.index}
    for p in priorities:
        c = cols.get(p.upper())
        if c and pd.notna(row[c]) and str(row[c]).strip():
            return str(row[c]).strip()
    return ""


def semantic_evidence_text(row: pd.Series) -> str:
    parts = []
    for c, value in row.items():
        if c.upper() not in SEMANTIC_FIELDS or pd.isna(value):
            continue
        text = str(value).strip()
        if text:
            parts.append(f"{c}={text}")
    return " | ".join(parts)[:4000]


def eligible_layer(row: dict) -> bool:
    if "polygon" not in row.get("geometry_type", "").lower():
        return False
    rel = row.get("layer_rel", "")
    if EXCLUDE_PATH.search(rel):
        return False
    return bool(GOOD_PATH.search(rel) or ZONE_FIELD.search(row.get("fields", "")))


def map_category(code: str, evidence: str, source_kind: str) -> tuple[str, str, str]:
    if source_kind == "CER_D":
        return "G1_PRODUCTIVE", "CER_LAYER_D", "RESOLVED_INCLUDED"
    if source_kind == "CER_H":
        return "G2_COMMERCIAL_TERTIARY", "CER_LAYER_H", "RESOLVED_INCLUDED"

    c = norm(code)
    t = norm(code + " " + evidence)

    if (
        re.match(r"^(dh|hd)(?:$|[_./-])", c)
        or re.match(r"^d\d+(?:[_./-]?h\d*)(?:$|[_./-])", c)
        or re.match(r"^h\d+(?:[_./-]?d\d*)(?:$|[_./-])", c)
        or re.search(r"artigianal.{0,20}commercial|industrial.{0,20}commercial|mista.{0,12}commercial", t)
    ):
        return "G4_MIXED_RELEVANT", "FVG_DH_MIXED_ZONE_CODE", "RESOLVED_INCLUDED"
    if re.search(r"dem[_ -]?milit|zona militare|interesse militare|\bmilit(?:are)?\b", t):
        return "", "MILITARY_NON_GENERATOR", "RESOLVED_EXCLUDED"
    if re.match(r"^d", c) and not re.match(r"^distrib", c):
        return "G1_PRODUCTIVE", "FVG_D_FAMILY_ZONE_CODE", "RESOLVED_INCLUDED"
    if re.match(r"^h", c):
        return "G2_COMMERCIAL_TERTIARY", "FVG_H_FAMILY_ZONE_CODE", "RESOLVED_INCLUDED"

    signals = set()
    if re.search(r"\b(logistic|interport|autoport|terminal|portual|porto\b|trasport|scalo ferrovi|ferroviar|aeroport)", t):
        signals.add("G3_LOGISTICS_TRANSPORT")
    if re.search(r"ferrov|ferr[_ -]?a|\bfs\b|staz[_ -]?serv|stazion.{0,10}servizio|area.{0,10}servizio.{0,10}autostrad|serv[_ -]?aut", t):
        signals.add("G3_LOGISTICS_TRANSPORT")
    if re.search(r"impiant.{0,10}tecnolog|servizi.{0,10}tecnic|imptec|utility|depur|discar|energet|centrale elet|sottostaz|cabina elet|acquedott", t):
        signals.add("G5_TECHNICAL_UTILITY_ENERGY")
    if re.search(r"industrial|artigian|produttiv|manifattur|deposit|magazzin", t):
        signals.add("G1_PRODUCTIVE")
    if re.search(r"commercial|terziar|direzional|grande distrib|ricettiv|alberghier|hotel", t):
        signals.add("G2_COMMERCIAL_TERTIARY")

    if len(signals) > 1 or (re.search(r"\bmist[aoe]\b|polifunzional", t) and signals):
        return "G4_MIXED_RELEVANT", "MULTI_RELEVANT_SIGNAL", "RESOLVED_INCLUDED"
    if len(signals) == 1:
        g = next(iter(signals))
        return g, f"EXPLICIT_SIGNAL_{g}", "RESOLVED_INCLUDED"

    if re.search(r"prpc|piano.{0,12}attuativ|amb[_ -]?prpc", t):
        return "", "IMPLEMENTATION_PLAN_BOUNDARY_NON_GENERATOR", "RESOLVED_EXCLUDED"
    if (
        re.search(r"\bservizi?\b|\battrezzature? collettiv|opera di interesse pubblico", t)
        or re.match(r"^serv(?:_|$)", c)
    ):
        return "", "GENERIC_SERVICE_WITHOUT_RELEVANT_COMPONENT", "RESOLVED_EXCLUDED"
    if (
        re.search(r"risp[_ -]?stra|fascia.{0,10}rispetto.{0,10}strad|\bstr\b|viabil|pedonal", t)
        or re.match(r"^viab(?:_|$)", c)
    ):
        return "", "ROAD_OR_ROAD_SETBACK_NON_GENERATOR", "RESOLVED_EXCLUDED"
    if re.search(r"parchegg|\bpark", t):
        return "", "GENERIC_PARKING_NON_GENERATOR", "RESOLVED_EXCLUDED"
    if (
        re.search(r"residen|residnzial|abitaz|agricol|rurale|bosch|forest|verde|\bvp\b|parco|tutela|"
                  r"acqua|alveo|culto|scol|scuol|sanitar|osped|social|sport|cimiter|"
                  r"fluviale|greto|archeo|ambiental|bonifica|\bprato\b|zona degli orti|"
                  r"geol|area priva di zonizzazione|traiettorie di caduta", t)
        or c in {"idro", "pert_fluv", "pert_fluviale"}
    ):
        return "", "EXPLICIT_NON_GENERATOR_SEMANTICS", "RESOLVED_EXCLUDED"
    if re.match(r"^[abcef]", c):
        return "", "STANDARD_NON_GENERATOR_ZONE_FAMILY", "RESOLVED_EXCLUDED"
    if re.match(r"^s(?:\d|\b|[_./-])", c):
        return "", "GENERIC_SERVICE_WITHOUT_RELEVANT_COMPONENT", "RESOLVED_EXCLUDED"
    if not c and not t:
        return "", "EMPTY_CATEGORY", "RESOLVED_EXCLUDED"
    return "", "INSUFFICIENT_SEMANTIC_EVIDENCE", "GENERATOR_CLASS_UNRESOLVED"


def polygon_parts(geom) -> list[Polygon]:
    if geom is None or geom.is_empty:
        return []
    if isinstance(geom, Polygon):
        return [geom]
    if isinstance(geom, MultiPolygon):
        return [g for g in geom.geoms if not g.is_empty]
    if isinstance(geom, GeometryCollection):
        parts = []
        for g in geom.geoms:
            parts.extend(polygon_parts(g))
        return parts
    return []


def geometry_hash(geom) -> str:
    normalized = shapely.normalize(geom)
    return hashlib.sha256(shapely.to_wkb(normalized, hex=False, byte_order=1)).hexdigest().upper()


def repair_and_split(geom) -> tuple[list[Polygon], list[str]]:
    transformations = []
    if geom is None or geom.is_empty:
        return [], transformations
    if not shapely.is_valid(geom):
        geom = shapely.make_valid(geom)
        transformations.append("MAKE_VALID")
    parts = polygon_parts(geom)
    if len(parts) > 1:
        transformations.append(f"SPLIT_MULTIPART_{len(parts)}")
    return parts, transformations
