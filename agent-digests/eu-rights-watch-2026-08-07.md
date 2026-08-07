# EU Citizen-Rights Watch — 2026-08-07

Repo: `flight-rights-mcp` · Branch: `agent/eu-rights-watch-2026-08-07`
Scope: EU261 jurisprudence, EU consumer-protection law, airline policy.
**3 findings — 1 legislative (high impact), 2 case-law.**

---

## 1. 🔴 EU261 REVISION ADOPTED — Council final clearance, 13 July 2026

- **What:** The Council gave final green light to the Regulation amending Reg. (EC) 261/2004 and (EC) 2027/97. Ends 13 years of deadlock.
- **What it changes:**
  - **Codified definition of "extraordinary circumstances"** (previously purely case-law driven).
  - **"No-show" clauses banned** — an airline may no longer cancel your return leg because you skipped the outbound.
  - **Price transparency** — fares must be displayed including one piece of hand baggage, before booking starts.
  - Reinforced rights for PRM/disabled passengers, children, unaccompanied minors, pregnant passengers.
  - Improved rerouting, assistance, information and airline-communication duties.
- **Citizen impact:** Broader and clearer entitlements, but **not yet in force** — applies **12 months + 20 days after OJ publication** (~H2 2027). Claims today still run under the current EU261 text.
- **Source:** https://www.consilium.europa.eu/en/press/press-releases/2026/07/13/council-gives-final-clearance-for-stronger-air-passenger-rights/
- **Legislative act (PDF):** https://data.consilium.europa.eu/doc/document/ST-11389-2026-INIT/en/pdf
- **Trilogue deal (15 June 2026):** https://www.consilium.europa.eu/en/press/press-releases/2026/06/15/council-and-parliament-reach-landmark-agreement-on-stronger-eu-air-passenger-rights/

### 🔧 Maintainer action — `flight-rights-mcp`
- **Tool `check_extraordinary_circumstances`** (`flight_rights_mcp/server.py:268`) and **`flight_rights_mcp/data/jurisprudence.json`**: plan a *dual-regime* mode. Once the OJ date is known, the checker should branch on flight date: pre-application → current Art. 5(3) case law; post-application → the new codified list. Suggested: add `"regime": "eu261_2004"` field to each case entry + a `applicable_from`/`applicable_until` guard.
- **Tool `calculate_compensation`** (`server.py:154`): amounts (€250/400/600) are **unchanged** in the final text — no immediate change needed. Delay thresholds must be re-verified against the OJ text before any edit; do **not** change the 3-hour threshold on press-release evidence alone.
- **`agb-reader-mcp` clause catalog:** add a new red-flag clause type **"No-Show-Klausel"** (return-flight forfeiture after unused outbound) — now expressly prohibited by the amending regulation, on top of existing German BGH case law invalidating such AGB clauses.

---

## 2. ⚖️ NI and HZ v European Air Charter AG — T-656/24, judgment 04 March 2026

- **What:** A carrier may rely on an extraordinary circumstance that hit an **earlier flight in the same aircraft rotation** *only where there is a direct causal link* with the later flight's delay. Where the delay stems from the carrier's **own operational choice** — here, waiting for late-connecting passengers from a preceding flight — the excuse fails.
- **Citizen impact:** Two passengers won **€400 each**. Kills a very common airline defence ("the delay came from an earlier leg, not our fault"). If the airline *chose* to wait, or the chain of causation is broken, **compensation is due**.
- **Sources:**
  - https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62024TJ0656
  - https://euperspectives.eu/2026/03/delay-due-to-waiting-for-late-passengers-from-an-earlier-flight-triggers-compensation-top-court-rules/
  - https://airlawdigest.com/case/ni-and-hz-v-european-air-charter-ag-2026-t656-24-eugc/

### 🔧 Maintainer action — `flight-rights-mcp`
- **`data/jurisprudence.json`**: add case `european-air-charter-t656-24`, `topic: "vorflug_rotation"`, keywords: `["vorflug", "rotation", "verspäteter zubringer", "previous flight", "earlier flight", "umlauf", "anschlusspassagiere", "warten auf passagiere"]`. Ruling: rotation excuse requires a **direct causal link**; a carrier's own decision to wait is not extraordinary → **compensation payable**.
- This currently returns *no match* in `check_extraordinary_circumstances` — the rotation excuse is a top-5 real-world airline defence and is a genuine coverage gap.

---

## 3. ⚖️ C-45/24 — Refund must include intermediary commission, judgment 15 January 2026

- **What:** Where a flight is cancelled, the Art. 8(1)(a) refund of "the full cost of the ticket at the price at which it was bought" **includes the booking-portal / agency commission**, where the carrier accepted that the intermediary issues tickets in its name and for its account — even if the carrier never received that commission.
- **Citizen impact:** Passengers who booked via Opodo, eDreams and similar OTAs get the **service/commission fee back too**, not just the bare fare. Extends the 2018 line of case law by removing the "carrier must have known the amount" limitation.
- **Sources:**
  - https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=15.01.2026&Aktenzeichen=C-45/24
  - https://www.lto.de/recht/nachrichten/n/c4524-eugh-flugausfall-airline-muss-provision-erstatten
  - https://www.beck-aktuell.de/heute-im-recht/rechtsprechung/eugh-c4524-flugannullierung-airline-vermittlerprovision-erstattung-opodo-2026-01-15

### 🔧 Maintainer action — `flight-rights-mcp`
- **Tool `generate_claim_letter`** (`server.py:403`): for cancellation claims, add an optional `booking_via_portal` / `commission_eur` input and a claim paragraph citing **EuGH C-45/24 (15.01.2026)** demanding refund of the intermediary commission alongside the fare.
- **`agb-reader-mcp`:** flag OTA/airline AGB clauses that exclude service or booking fees from refunds — now contrary to C-45/24.

---

## Not changed this run
- Compensation bands €250 / €400 / €600 — unchanged.
- German limitation period (`check_verjaehrung`, `server.py:345`) — unchanged (3 years, § 195 BGB, from year-end).
- No airline-specific policy change (Lufthansa, Ryanair et al.) found meeting the citation bar this run.

*Automated watchdog run. Read-only: no tool logic was modified — maintainer review required.*
