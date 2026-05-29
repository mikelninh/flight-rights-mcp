"""
flight-rights-mcp — EU261/2004 flight compensation calculator + claim drafting
+ ECJ jurisprudence checker for airline "extraordinary circumstances" excuses.

Built on civic-ai-mcp-toolkit. Six tools, all working offline against bundled
data. The first toolkit-first MCP in the portfolio.

What it answers for a passenger via Claude / Cursor:
  - "Mein Flug LH458 ist 4h verspätet — habe ich Anspruch?"
  - "Lufthansa beruft sich auf 'technical issue' — ist das eine gültige Ausrede?"
  - "Wie hoch ist meine Entschädigung bei BER → JFK?"
  - "Bis wann muss ich die Forderung stellen?"
  - "Schreib mir das Forderungsschreiben."

What this MCP is NOT:
  - Eine Anwaltskanzlei (Vertretung bei Klage → Anwalt)
  - Eine Inkassodienstleistung (wenn Airline trotzdem nicht zahlt → AirHelp / EUclaim)
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

from civic_ai_mcp import (
    configure_logging,
    create_mcp_server,
    error_envelope,
    load_fixture,
    run_main,
    traced,
)


HERE = Path(__file__).resolve().parent

mcp = create_mcp_server("flight-rights", default_port=8011)


# ── Helpers ──────────────────────────────────────────────────────────


def _airports() -> dict[str, Any]:
    return load_fixture(HERE, "airports.json")["airports"]


def _jurisprudence() -> dict[str, Any]:
    return load_fixture(HERE, "jurisprudence.json")


def _haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Great-circle distance via the haversine formula. Earth radius 6371 km."""
    R = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))


_EU_EEA_PLUS_CH_GB_COUNTRIES = {
    # EU-27
    "AT",
    "BE",
    "BG",
    "HR",
    "CY",
    "CZ",
    "DK",
    "EE",
    "FI",
    "FR",
    "DE",
    "GR",
    "HU",
    "IE",
    "IT",
    "LV",
    "LT",
    "LU",
    "MT",
    "NL",
    "PL",
    "PT",
    "RO",
    "SK",
    "SI",
    "ES",
    "SE",
    # EEA
    "IS",
    "LI",
    "NO",
    # CH (bilateral)
    "CH",
    # UK (kept EU261 in domestic law as UK261)
    "GB",
}


# ── Tool 1: get_airport_distance ─────────────────────────────────────


@mcp.tool()
@traced("get_airport_distance")
def get_airport_distance(iata_a: str, iata_b: str) -> dict[str, Any]:
    """
    Compute great-circle distance between two airports (km) — the basis for
    EU261 compensation tier classification.

    Returns:
      {iata_a, name_a, country_a, iata_b, name_b, country_b, distance_km, tier}
      where tier ∈ {"short" (≤1500), "medium" (1500-3500), "long" (>3500)}.
      Or {"error": "unknown_iata", ...} when a code isn't bundled.
    """
    a = iata_a.strip().upper()
    b = iata_b.strip().upper()
    airports = _airports()
    if a not in airports or b not in airports:
        missing = [c for c in (a, b) if c not in airports]
        return error_envelope(
            "unknown_iata",
            f"airport code(s) not in bundled registry: {missing}",
            searched=missing,
            available_count=len(airports),
        )
    pa, pb = airports[a], airports[b]
    km = _haversine_km(pa["lat"], pa["lon"], pb["lat"], pb["lon"])
    if km <= 1500:
        tier = "short"
    elif km <= 3500:
        tier = "medium"
    else:
        tier = "long"
    return {
        "iata_a": a,
        "name_a": pa["name"],
        "country_a": pa["country"],
        "iata_b": b,
        "name_b": pb["name"],
        "country_b": pb["country"],
        "distance_km": round(km),
        "tier": tier,
    }


# ── Tool 2: calculate_compensation ───────────────────────────────────


@mcp.tool()
@traced("calculate_compensation")
def calculate_compensation(distance_km: float, delay_hours: float) -> dict[str, Any]:
    """
    Compute EU261 Art. 7 compensation based on distance + arrival delay.

    Rules:
      Short  (≤1500 km)        — €250 if delay ≥ 3h
      Medium (1500-3500 km)    — €400 if delay ≥ 3h
      Long   (>3500 km)        — €600 if delay ≥ 4h, €300 if delay 3-4h (Art. 7(2)(c))
      < 3h delay → €0 (Sturgeon C-402/07 threshold)

    Returns:
      {tier, delay_hours, compensation_eur, rationale (German), reduced_by_50_pct}
    """
    if distance_km < 0 or delay_hours < 0:
        return error_envelope("invalid_input", "distance and delay must be ≥ 0")

    if distance_km <= 1500:
        tier, full, threshold = "short", 250, 3.0
    elif distance_km <= 3500:
        tier, full, threshold = "medium", 400, 3.0
    else:
        tier, full, threshold = "long", 600, 4.0

    if delay_hours < 3.0:
        return {
            "tier": tier,
            "delay_hours": delay_hours,
            "compensation_eur": 0,
            "rationale": (
                "Verspätung unter 3 Stunden — kein Ausgleichsanspruch nach EU261 "
                "(Sturgeon C-402/07). Verpflegung/Betreuung können trotzdem bestehen."
            ),
            "reduced_by_50_pct": False,
        }

    if tier == "long" and 3.0 <= delay_hours < threshold:
        return {
            "tier": tier,
            "delay_hours": delay_hours,
            "compensation_eur": full // 2,
            "rationale": (
                f"Langstrecke (>3500 km), Verspätung {delay_hours}h zwischen 3-4h: "
                f"€{full // 2} (50%-Reduktion per EU261 Art. 7(2)(c)). "
                f"Ab 4h Verspätung: voller Betrag €{full}."
            ),
            "reduced_by_50_pct": True,
        }

    return {
        "tier": tier,
        "delay_hours": delay_hours,
        "compensation_eur": full,
        "rationale": (
            f"Tier '{tier}' ({distance_km:.0f} km), Verspätung {delay_hours}h ≥ "
            f"{threshold}h: voller Ausgleich €{full} per EU261 Art. 7."
        ),
        "reduced_by_50_pct": False,
    }


# ── Tool 3: check_eu261_applicability ────────────────────────────────


@mcp.tool()
@traced("check_eu261_applicability")
def check_eu261_applicability(
    departure_country: str,
    airline_country: str,
) -> dict[str, Any]:
    """
    Does EU261 (or UK261 mirror) apply to this flight per Art. 3?

      EU261 applies if departure country is EU/EEA/CH/UK — OR
      if airline is registered in EU/EEA/CH/UK with arrival in EU/EEA/CH/UK.

    Returns: {applicable, regulation, reason (German)}.
    """
    dep = departure_country.strip().upper()
    air = airline_country.strip().upper()

    if dep in _EU_EEA_PLUS_CH_GB_COUNTRIES:
        regulation = "UK261" if dep == "GB" else "EU261"
        return {
            "applicable": True,
            "regulation": regulation,
            "reason": (
                f"Abflug aus {dep} (EU/EEA/CH/UK) → EU261 Art. 3(1)(a) anwendbar, "
                f"unabhängig von der Airline."
            ),
        }
    if air in _EU_EEA_PLUS_CH_GB_COUNTRIES:
        return {
            "applicable": True,
            "regulation": "EU261",
            "reason": (
                f"Airline aus {air} (EU/EEA) → EU261 Art. 3(1)(b) anwendbar, "
                f"sofern Flug in einem EU/EEA-Land endet. Bei Drittstaaten-Endpunkt prüfen."
            ),
        }
    return {
        "applicable": False,
        "regulation": "none",
        "reason": (
            f"Weder Abflug ({dep}) noch Airline ({air}) im EU/EEA/CH/UK-Raum — "
            f"EU261 nicht anwendbar. Lokales Recht prüfen (US: 4-CFR-Pt. 250, Canada: APPR)."
        ),
    }


# ── Tool 4: check_extraordinary_circumstances ────────────────────────


@mcp.tool()
@traced("check_extraordinary_circumstances")
def check_extraordinary_circumstances(reason_given: str) -> dict[str, Any]:
    """
    Check whether the airline's stated reason qualifies as extraordinary
    circumstances under EU261 Art. 5(3), per ECJ case law.

    Returns:
      {match_count, matched_cases [{citation, topic, ruling, result_for_passenger,
       exceptions, source_url}], likely_extraordinary, advice (German)}
    """
    reason_lower = reason_given.lower().strip()
    if not reason_lower:
        return {
            "match_count": 0,
            "matched_cases": [],
            "likely_extraordinary": False,
            "advice": (
                "Keine Ausrede angegeben — Airline trifft die Beweislast für jeden Befreiungsgrund."
            ),
        }

    cases = _jurisprudence()["cases"]
    matches: list[dict[str, Any]] = []
    for case in cases:
        for kw in case["keywords"]:
            if kw.lower() in reason_lower:
                matches.append(
                    {
                        "citation": case["citation"],
                        "topic": case["topic"],
                        "ruling": case["ruling"],
                        "result_for_passenger": case["result_for_passenger"],
                        "exceptions": case.get("exceptions", ""),
                        "source_url": case.get("source_url", ""),
                    }
                )
                break

    if not matches:
        return {
            "match_count": 0,
            "matched_cases": [],
            "likely_extraordinary": False,
            "advice": (
                "Keine bekannte EuGH-Rechtsprechung zu dieser Ausrede gefunden. "
                "Airline trägt die volle Beweislast für 'außergewöhnliche Umstände' "
                "— im Zweifel Anspruch stellen."
            ),
        }

    extraordinary = [
        "Kein Anspruch" in m["result_for_passenger"]
        or "Kein Ausgleich" in m["result_for_passenger"]
        for m in matches
    ]
    likely = all(extraordinary) if extraordinary else False

    advice = (
        "Diese Ausrede ist nach EuGH grundsätzlich anerkannt — Airline trägt "
        "aber weiter die Beweislast (Vorsorge-Maßnahmen). Im Zweifel Belege anfordern."
        if likely
        else "Nach EuGH-Rechtsprechung ist diese Ausrede VORAUSSICHTLICH KEIN außergewöhnlicher "
        "Umstand — Anspruch besteht. Forderungsschreiben mit Zitat aufsetzen."
    )

    return {
        "match_count": len(matches),
        "matched_cases": matches,
        "likely_extraordinary": likely,
        "advice": advice,
    }


# ── Tool 5: check_verjährung ─────────────────────────────────────────


@mcp.tool()
@traced("check_verjaehrung")
def check_verjaehrung(flight_date_iso: str, country: str = "DE") -> dict[str, Any]:
    """
    Compute the country-specific statute-of-limitations deadline for an EU261 claim.

    Args:
      flight_date_iso: ISO-8601 date of the original (planned) flight.
      country:         ISO-2 (DE, AT, CH, FR, GB, ES, IT, NL, PT, PL). Default "DE".

    Returns: {country, years, rule, flight_date, deadline_iso, days_remaining, expired}.
    """
    from datetime import date, datetime

    rules = _jurisprudence()["statute_of_limitations"]
    c = country.strip().upper()
    if c not in rules:
        return error_envelope(
            "unknown_country",
            f"country {c} not in registry",
            available=sorted(rules.keys()),
        )

    try:
        flight_date = datetime.fromisoformat(flight_date_iso).date()
    except (ValueError, TypeError):
        return error_envelope(
            "invalid_date",
            f"could not parse '{flight_date_iso}' as ISO date",
        )

    years = rules[c]["years"]

    if c == "DE":
        # § 195 BGB: Schluss des Jahres + 3 Jahre
        deadline = date(flight_date.year + years, 12, 31)
    else:
        try:
            deadline = flight_date.replace(year=flight_date.year + years)
        except ValueError:
            deadline = date(flight_date.year + years, 2, 28)

    today = date.today()
    days_remaining = (deadline - today).days
    return {
        "country": c,
        "years": years,
        "rule": rules[c]["rule"],
        "flight_date": flight_date_iso,
        "deadline_iso": deadline.isoformat(),
        "days_remaining": days_remaining,
        "expired": days_remaining < 0,
    }


# ── Tool 6: generate_claim_letter ────────────────────────────────────


@mcp.tool()
@traced("generate_claim_letter")
def generate_claim_letter(
    passenger_name: str,
    flight_number: str,
    flight_date_iso: str,
    iata_departure: str,
    iata_arrival: str,
    delay_hours: float,
    airline_excuse: str = "",
    iban: str = "",
    passenger_address: str = "",
    airline_address: str = "",
) -> dict[str, Any]:
    """
    Build a German-language EU261 demand letter the passenger can send directly
    to the airline. Internally calls the calculator + jurisprudence checker so
    the letter cites the right compensation AND the relevant ECJ case against
    the airline's excuse.

    Returns: {letter_markdown, compensation_eur, matched_jurisprudence, instructions}.
    """
    if not passenger_name.strip():
        return error_envelope("invalid_input", "passenger_name is required")
    if not flight_number.strip():
        return error_envelope("invalid_input", "flight_number is required")

    distance_info = get_airport_distance(iata_departure, iata_arrival)
    if "error" in distance_info:
        return distance_info
    distance_km = distance_info["distance_km"]

    comp = calculate_compensation(distance_km=distance_km, delay_hours=delay_hours)
    if "error" in comp:
        return comp

    eur = comp["compensation_eur"]
    if eur == 0:
        return error_envelope(
            "no_compensation",
            "Auf Basis der Eingaben besteht KEIN Ausgleichsanspruch — Verspätung < 3h.",
            calculator_result=comp,
        )

    case_info = (
        check_extraordinary_circumstances(airline_excuse)
        if airline_excuse
        else {"matched_cases": [], "likely_extraordinary": False, "advice": ""}
    )

    citation_block = ""
    if case_info.get("matched_cases"):
        first = case_info["matched_cases"][0]
        citation_block = (
            f'\n\nIhre Begründung mit „{airline_excuse}" entzieht Sie nicht der '
            f"Ausgleichspflicht. Der Europäische Gerichtshof hat in "
            f"**{first['citation']}** entschieden: {first['ruling']}\n"
        )

    iban_block = f"\n\n**IBAN für Überweisung:** `{iban}`" if iban else ""
    pax_addr = f"\n\n{passenger_address}\n" if passenger_address else ""
    air_addr = f"\n\n{airline_address}\n" if airline_address else ""

    letter = f"""# Forderung Ausgleichsleistung nach VO (EG) Nr. 261/2004
{pax_addr}
**An:**{air_addr}

**Flug-Nr.:** {flight_number}
**Datum:** {flight_date_iso}
**Strecke:** {distance_info["iata_a"]} → {distance_info["iata_b"]} ({distance_km} km)
**Tatsächliche Ankunftsverspätung:** {delay_hours} Stunden

Sehr geehrte Damen und Herren,

mit diesem Schreiben fordere ich, **{passenger_name}**, als Fluggast des oben
genannten Fluges Ausgleichszahlung nach Verordnung (EG) Nr. 261/2004 (EU261)
Art. 7 in Höhe von **€{eur}**.

Der Flug wies eine Ankunftsverspätung von {delay_hours} Stunden auf — die
EuGH-Rechtsprechung (C-402/07 *Sturgeon*) gewährt bei einer Ankunftsverspätung
ab 3 Stunden die volle Ausgleichszahlung gemäß Art. 7 VO 261/2004.{citation_block}

Ich fordere Sie hiermit auf, den Betrag von **€{eur}** innerhalb von **14 Tagen**
nach Zugang dieses Schreibens auf das nachstehende Konto zu überweisen.{iban_block}

Nach Ablauf der Frist behalte ich mir die Geltendmachung über die Schlichtungsstelle
für den öffentlichen Personenverkehr (SÖP, https://www.soep-online.de) oder
gerichtliche Schritte ausdrücklich vor.

Mit freundlichen Grüßen

{passenger_name}
"""

    return {
        "letter_markdown": letter.strip(),
        "compensation_eur": eur,
        "matched_jurisprudence": case_info.get("matched_cases", []),
        "instructions": (
            "1. Brief unterschreiben + per E-Mail / Einschreiben senden. "
            "2. Lehnt Airline ab oder ignoriert: SÖP-Schlichtung (kostenlos, ohne Anwalt). "
            "3. Verjährungsfrist mit check_verjährung prüfen — bei DE drei Jahre + Jahresende."
        ),
    }


# ── Entry point ─────────────────────────────────────────────────────


def main() -> None:
    configure_logging(logger_name="flight_rights_mcp")
    run_main(mcp)


if __name__ == "__main__":
    main()
