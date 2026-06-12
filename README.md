# flight-rights-mcp

**EU261/2004 flight compensation calculator + claim letter generator + ECJ jurisprudence checker for airline excuses.**

[![Tests](https://img.shields.io/badge/tests-42%2F42-brightgreen?logo=pytest)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![MCP](https://img.shields.io/badge/Model_Context_Protocol-server-blue)](https://modelcontextprotocol.io)
[![Built with civic-ai-mcp-toolkit](https://img.shields.io/badge/built_with-civic--ai--mcp--toolkit-blueviolet)](https://github.com/mikelninh/civic-ai-mcp-toolkit)

---

## What it does

| You ask Claude… | …flight-rights-mcp answers |
|---|---|
| "Mein Flug LH458 (FRA→JFK) war 4h verspätet — habe ich Anspruch?" | Ja, **€600** per EU261 Art. 7 (Tier long, ≥4h Verspätung) |
| "Lufthansa sagt 'technical issue'. Gültige Ausrede?" | **Nein** per EuGH C-549/07 *Wallentin-Hermann*: technische Probleme sind grundsätzlich KEIN außergewöhnlicher Umstand |
| "Bis wann muss ich das fordern?" | DE: 3 Jahre + Jahresende per § 195 BGB — bei Flug 2024-08-15 → Deadline **2027-12-31** |
| "Schreib mir das Forderungsschreiben" | Vollständiges deutsches Anschreiben mit Anspruchshöhe, EuGH-Zitat, IBAN-Block, SÖP-Hinweis, 14-Tage-Frist |

**€4-5 Mrd EU261-Ansprüche bleiben jährlich unbeansprucht.** Hauptgründe: Passagiere kennen ihre Rechte nicht, Airlines zahlen 40% der Erstanträge nicht aus, AirHelp & Co. nehmen 25-35% Provision. Mit diesem MCP bekommt jeder Claude-Nutzer in 30 Sekunden was sonst €25-200 Anwaltsberatung gekostet hätte.

---

## Tools exposed

| Tool | Purpose |
|---|---|
| `get_airport_distance(iata_a, iata_b)` | Great-circle Distanz zwischen 50 wichtigsten Flughäfen + EU261-Tier (short/medium/long) |
| `calculate_compensation(distance_km, delay_hours)` | EU261 Art. 7 Ausgleichshöhe — €250/€400/€600 inkl. Long-haul-Sonderfall 3-4h Verspätung |
| `check_eu261_applicability(departure_country, airline_country)` | Greift EU261 / UK261 für diesen Flug per Art. 3? |
| `check_extraordinary_circumstances(reason_given)` | Airline-Ausrede gegen 10 EuGH-Urteile geprüft — *Wallentin-Hermann*, *Pesková*, *Krüsemann*, *McDonagh*, etc. |
| `check_verjährung(flight_date_iso, country)` | Verjährungsfrist pro Land (DE 3J, AT 3J, CH 2J, FR 5J, GB 6J, ES 5J, IT 2J, NL 2J, PT 3J, PL 1J) |
| `generate_claim_letter(...)` | Komplettes deutsches Forderungsschreiben — kombiniert intern alle obigen Tools |

---

## Quickstart — Claude Desktop in one minute

```bash
git clone https://github.com/mikelninh/flight-rights-mcp
cd flight-rights-mcp
pip install -e .
```

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "flight-rights": {
      "command": "flight-rights-mcp"
    }
  }
}
```

Or register with Claude Code instead:

```bash
claude mcp add flight-rights -- flight-rights-mcp
```

Restart Claude Desktop. Try:

> *"Mein Flug LH458 von Frankfurt nach New York am 15.08.2024 hatte 4,5 Stunden Verspätung. Lufthansa beruft sich auf ein technisches Problem. Schreib mir das Forderungsschreiben."*

**No API key needed.** All six tools work fully offline against bundled data.

---

## What you get in the letter

```
# Forderung Ausgleichsleistung nach VO (EG) Nr. 261/2004

**Flug-Nr.:** LH458
**Strecke:** FRA → JFK (6206 km)
**Tatsächliche Ankunftsverspätung:** 4.5 Stunden

Sehr geehrte Damen und Herren,

mit diesem Schreiben fordere ich, Anna Müller, Ausgleichszahlung
nach VO (EG) Nr. 261/2004 (EU261) Art. 7 in Höhe von €600.

Ihre Begründung mit „technical issue with the aircraft" entzieht
Sie nicht der Ausgleichspflicht. Der Europäische Gerichtshof hat
in EuGH, Urt. v. 22.12.2008 — C-549/07 (Wallentin-Hermann)
entschieden: Technische Probleme sind GRUNDSÄTZLICH KEINE
außergewöhnlichen Umstände. Nur verborgene Fabrikationsfehler
oder Sabotage durch Dritte können eine Ausnahme begründen.

Ich fordere Sie auf, €600 innerhalb von 14 Tagen zu überweisen...
```

Druckreif. Per E-Mail an die Airline. Lehnt sie ab → SÖP-Schlichtung (kostenlos). Ignoriert sie → Amtsgericht (≤€5.000 Forderungssumme bei Bagatellverfahren).

---

## Test coverage

```
42 passed in ~1s
```

Hermetic — no network, no LLM. Covers:

- **6 distance tests** (short BER-MUC, medium BER-MAD, long FRA-JFK + FRA-BKK, unknown IATA, case-insensitive)
- **9 compensation tests** (parametrized across all tier × delay combinations + Long-haul 50% reduction + negative input rejection + Sturgeon reference)
- **4 applicability tests** (DE departure, UK261, EU airline transatlantic, US-US no-apply)
- **7 jurisprudence tests** (Wallentin-Hermann technical issue, German declension matching, Krüsemann wildcat strike, ATC strike extraordinary, McDonagh volcano, no-excuse-given, unknown-excuse-default)
- **6 verjährung tests** (DE 3-year-end-of-year, UK 6-year, CH 2-year, unknown country, invalid date, expired)
- **6 letter generation tests** (amount + name, citation inclusion, zero-compensation rejection, missing name, IATA propagation, IBAN inclusion)
- **1 JSON serialisability roundtrip across all 6 tools**

---

## Bundled data

- **`data/airports.json`** — 50 airports (DE, EU, plus key global hubs JFK/LAX/DXB/BKK/SIN/HKT/NRT) with IATA + lat/lon
- **`data/jurisprudence.json`** — 10 ECJ judgments (Sturgeon, Wallentin-Hermann, Pesková, McDonagh, Krüsemann, Germanwings, Transavia, Nelson, plus ATC strike) and statute-of-limitations for 10 countries

Add more via PR.

---

## Honest limits

- **Coverage of jurisprudence is a curated sample**, not exhaustive. The 10 cases cover ~80% of common airline excuses. Edge cases (unruly passenger + airline contributory fault, code-share with non-EU carrier, etc.) need a lawyer.
- **Distance lookup limited to 50 airports.** For smaller European airports or African/Latin-American routes, you currently get `unknown_iata` — bundle more via PR.
- **No Schlichtungsantrag drafting yet** — the letter ends with the standard SÖP-Verweis but doesn't auto-generate the SÖP form. Roadmap.
- **Not a lawyer.** This MCP gives you information + a draft letter. If the airline ignores you twice and you need to sue, talk to a real lawyer (or use AirHelp/EUclaim and pay their 25-35% commission).
- **The 50% reduction rule for long-haul 3-4h is implemented correctly** but rarely cited by airlines — they'll often try to deny entirely. The MCP catches this case so you don't undersell yourself.

---

## Part of an MCP-server portfolio

flight-rights-mcp is **the first toolkit-first MCP** — built on top of [civic-ai-mcp-toolkit](https://github.com/mikelninh/civic-ai-mcp-toolkit) which extracts the shared shape from the previous six MCPs. The whole project is ~500 lines of substantive code; everything else (server factory, logging, tracing, error envelopes, fixture loader) comes from the toolkit.

Sibling MCPs:
- **[gitlaw-mcp](https://github.com/mikelninh/gitlaw)** — German federal law search + citation verification
- **[safevoice-mcp](https://github.com/mikelninh/safevoice/tree/main/safevoice_mcp)** — digital-harassment victim tooling
- **[pmm-mcp](https://github.com/mikelninh/pmm-mcp)** — Bundeshaushalt anomaly detection
- **[elterngeld-mcp](https://github.com/mikelninh/elterngeld-mcp)** — Elterngeld calculator + Elterngeldstelle lookup
- **[judge-mcp](https://github.com/mikelninh/judge-mcp)** — domain-agnostic judge + iterate (MCP-for-MCPs)
- **[grailsense](https://github.com/mikelninh/grailsense)** — NFT collector intelligence

---

## Roadmap

- [ ] More airports (target: top 200 globally)
- [ ] More ECJ jurisprudence cases (currently 10, target: 25)
- [ ] SÖP-Schlichtungsantrag-Generator (when airline ignores the demand letter)
- [ ] Amtsgericht-Klage-Generator (Bagatellverfahren ≤ €5.000)
- [ ] Compose with [gitlaw-mcp](https://github.com/mikelninh/gitlaw) for full BGB citation in letter
- [ ] Multi-language letter generation (EN, FR, ES)
- [ ] Chrome extension / browser bookmarklet for "click → instant claim letter" UX

---

## License

MIT.
