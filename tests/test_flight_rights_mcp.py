"""flight-rights-mcp tests — hermetic. Pins EU261 calc rules + jurisprudence."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from flight_rights_mcp.server import (  # noqa: E402
    calculate_compensation,
    check_eu261_applicability,
    check_extraordinary_circumstances,
    check_verjaehrung,
    generate_claim_letter,
    get_airport_distance,
)


# ── get_airport_distance ─────────────────────────────────────────────


def test_distance_short_haul_within_germany():
    r = get_airport_distance("BER", "MUC")
    assert r["tier"] == "short"
    assert 400 < r["distance_km"] < 700


def test_distance_medium_haul_within_europe():
    r = get_airport_distance("BER", "MAD")
    assert r["tier"] == "medium"
    assert 1700 < r["distance_km"] < 2200


def test_distance_long_haul_transatlantic():
    r = get_airport_distance("FRA", "JFK")
    assert r["tier"] == "long"
    assert 6000 < r["distance_km"] < 6500


def test_distance_long_haul_to_asia():
    r = get_airport_distance("FRA", "BKK")
    assert r["tier"] == "long"
    assert 8800 < r["distance_km"] < 9400


def test_unknown_iata_returns_error():
    r = get_airport_distance("BER", "ZZZ")
    assert r.get("error") == "unknown_iata"
    assert "ZZZ" in r["searched"]


def test_distance_case_insensitive():
    upper = get_airport_distance("BER", "MUC")
    lower = get_airport_distance("ber", "muc")
    assert upper["distance_km"] == lower["distance_km"]


# ── calculate_compensation ───────────────────────────────────────────


@pytest.mark.parametrize(
    "distance,delay,expected",
    [
        (800, 3.5, 250),  # short, > 3h → 250
        (1500, 4, 250),  # boundary short
        (2500, 3.5, 400),  # medium
        (3500, 3.5, 400),  # boundary medium
        (5000, 4.5, 600),  # long, ≥ 4h → 600
        (5000, 3.5, 300),  # long, 3-4h → 50% reduction
        (5000, 2.5, 0),  # < 3h
        (500, 2.9, 0),  # short < 3h
        (10000, 12, 600),  # long, very delayed → still 600 max
    ],
)
def test_compensation_calculations(distance, delay, expected):
    r = calculate_compensation(distance_km=distance, delay_hours=delay)
    assert r["compensation_eur"] == expected, (
        f"distance={distance}, delay={delay}: got {r['compensation_eur']}, want {expected}"
    )


def test_compensation_negative_inputs_rejected():
    assert calculate_compensation(-100, 5).get("error") == "invalid_input"
    assert calculate_compensation(1000, -1).get("error") == "invalid_input"


def test_long_haul_3_to_4h_marks_reduction():
    r = calculate_compensation(distance_km=5000, delay_hours=3.5)
    assert r["reduced_by_50_pct"] is True


def test_under_3h_rationale_mentions_sturgeon():
    r = calculate_compensation(distance_km=800, delay_hours=2.5)
    assert "Sturgeon" in r["rationale"]


# ── check_eu261_applicability ────────────────────────────────────────


def test_eu261_departure_from_germany_applies():
    r = check_eu261_applicability("DE", "US")
    assert r["applicable"] is True
    assert r["regulation"] == "EU261"


def test_uk261_for_uk_departure():
    r = check_eu261_applicability("GB", "GB")
    assert r["regulation"] == "UK261"


def test_eu_airline_to_eu_destination_applies():
    r = check_eu261_applicability("US", "DE")
    assert r["applicable"] is True


def test_non_eu_no_eu_airline_not_applicable():
    r = check_eu261_applicability("US", "US")
    assert r["applicable"] is False


# ── check_extraordinary_circumstances ────────────────────────────────


def test_technical_issue_not_extraordinary():
    r = check_extraordinary_circumstances("There was a technical issue with the aircraft.")
    assert r["match_count"] >= 1
    assert r["likely_extraordinary"] is False
    citations = " ".join(m["citation"] for m in r["matched_cases"])
    assert "Wallentin" in citations


def test_german_technisches_problem_matches():
    r = check_extraordinary_circumstances("Aufgrund eines technischen Problems")
    assert r["match_count"] >= 1
    assert r["likely_extraordinary"] is False


def test_wildcat_strike_not_extraordinary():
    r = check_extraordinary_circumstances(
        "Wilder Streik der Crew nach Umstrukturierungs-Ankündigung"
    )
    assert r["match_count"] >= 1
    assert r["likely_extraordinary"] is False


def test_atc_strike_is_extraordinary():
    r = check_extraordinary_circumstances("ATC strike caused the delay")
    assert r["match_count"] >= 1
    assert r["likely_extraordinary"] is True


def test_volcano_is_extraordinary():
    r = check_extraordinary_circumstances("Aschewolke nach Vulkanausbruch")
    assert r["match_count"] >= 1
    assert r["likely_extraordinary"] is True


def test_no_excuse_given_returns_zero_match():
    r = check_extraordinary_circumstances("")
    assert r["match_count"] == 0


def test_unknown_excuse_default_advises_no_compensation_doubt():
    r = check_extraordinary_circumstances("just delayed because something")
    assert r["match_count"] == 0
    assert r["likely_extraordinary"] is False


# ── check_verjährung ─────────────────────────────────────────────────


def test_verjaehrung_for_germany_3_year_end_of_year():
    r = check_verjaehrung("2024-03-15", "DE")
    assert r["years"] == 3
    assert r["deadline_iso"] == "2027-12-31"


def test_verjaehrung_for_uk_6_years():
    r = check_verjaehrung("2024-03-15", "GB")
    assert r["years"] == 6
    assert "Limitation Act" in r["rule"]


def test_verjaehrung_for_switzerland_2_years():
    r = check_verjaehrung("2024-03-15", "CH")
    assert r["years"] == 2


def test_verjaehrung_unknown_country_returns_error():
    r = check_verjaehrung("2024-03-15", "ZZ")
    assert r.get("error") == "unknown_country"


def test_verjaehrung_invalid_date_returns_error():
    r = check_verjaehrung("not-a-date", "DE")
    assert r.get("error") == "invalid_date"


def test_verjaehrung_expired_for_old_flight():
    r = check_verjaehrung("2018-01-01", "DE")
    assert r["expired"] is True
    assert r["days_remaining"] < 0


# ── generate_claim_letter ────────────────────────────────────────────


def test_generate_letter_contains_amount_and_passenger_name():
    r = generate_claim_letter(
        passenger_name="Anna Müller",
        flight_number="LH458",
        flight_date_iso="2024-08-15",
        iata_departure="FRA",
        iata_arrival="JFK",
        delay_hours=4.5,
    )
    assert r["compensation_eur"] == 600
    assert "Anna Müller" in r["letter_markdown"]
    assert "LH458" in r["letter_markdown"]
    assert "600" in r["letter_markdown"]


def test_generate_letter_with_excuse_includes_citation():
    r = generate_claim_letter(
        passenger_name="Anna Müller",
        flight_number="LH458",
        flight_date_iso="2024-08-15",
        iata_departure="FRA",
        iata_arrival="JFK",
        delay_hours=4.5,
        airline_excuse="technical issue with the aircraft",
    )
    assert len(r["matched_jurisprudence"]) >= 1
    assert "Wallentin" in r["letter_markdown"] or "Wallentin" in str(r["matched_jurisprudence"])


def test_generate_letter_zero_compensation_returns_error():
    r = generate_claim_letter(
        passenger_name="Test",
        flight_number="X1",
        flight_date_iso="2024-01-01",
        iata_departure="BER",
        iata_arrival="MUC",
        delay_hours=2.0,
    )
    assert r.get("error") == "no_compensation"


def test_generate_letter_missing_name_rejected():
    r = generate_claim_letter(
        passenger_name="",
        flight_number="LH1",
        flight_date_iso="2024-01-01",
        iata_departure="BER",
        iata_arrival="MUC",
        delay_hours=4,
    )
    assert r.get("error") == "invalid_input"


def test_generate_letter_unknown_iata_propagates_error():
    r = generate_claim_letter(
        passenger_name="X",
        flight_number="LH1",
        flight_date_iso="2024-01-01",
        iata_departure="ZZZ",
        iata_arrival="MUC",
        delay_hours=4,
    )
    assert r.get("error") == "unknown_iata"


def test_generate_letter_with_iban_includes_it():
    r = generate_claim_letter(
        passenger_name="Anna Müller",
        flight_number="LH458",
        flight_date_iso="2024-08-15",
        iata_departure="FRA",
        iata_arrival="JFK",
        delay_hours=4.5,
        iban="DE89 3704 0044 0532 0130 00",
    )
    assert "DE89 3704 0044 0532 0130 00" in r["letter_markdown"]


# ── JSON-serialisability across all tools ────────────────────────────


def test_all_tool_returns_are_json_serialisable():
    json.dumps(get_airport_distance("BER", "MUC"))
    json.dumps(calculate_compensation(2000, 4))
    json.dumps(check_eu261_applicability("DE", "US"))
    json.dumps(check_extraordinary_circumstances("technical issue"))
    json.dumps(check_verjaehrung("2024-01-01", "DE"))
    json.dumps(
        generate_claim_letter(
            passenger_name="X",
            flight_number="LH1",
            flight_date_iso="2024-01-01",
            iata_departure="FRA",
            iata_arrival="JFK",
            delay_hours=4.5,
        )
    )
