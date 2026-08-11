# EU Rights-Watch Digest — 2026-08-11

Watchdog run for `flight-rights-mcp` (extraordinary-circumstances checker) and cross-reference `agb-reader-mcp` (clause catalog).
All findings cite a real source URL. Where a ruling affects a tool's logic, the exact tool + change needed is noted.

---

## 1. CJEU C-399/24 — Lightning strike + mandatory safety inspection MAY be an "extraordinary circumstance"
- **Ruling:** CJEU (3rd Chamber), *AirHelp Germany GmbH v Austrian Airlines AG*, **C-399/24, 16 Oct 2025**. A lightning strike on a *preceding* flight that triggers mandatory safety inspections delaying the subsequent flight **can** qualify as an "extraordinary circumstance" under Art. 5(3) — **but only if** the airline proves it took all reasonable measures. The Court stressed the safety objective: classifying this as extraordinary prevents airlines being incentivised to prioritise punctuality over safety. It does **not** automatically exempt the carrier.
- **Right changed:** Refines the Art. 5(3) exemption boundary (narrowly favourable to carriers here, still subject to strict reasonable-measures proof).
- **Citizen impact:** If your delay was caused by a lightning-struck aircraft + mandatory inspection, you may **not** automatically win compensation — the airline must still prove all reasonable measures were taken. Don't assume an automatic payout, but don't accept a blanket refusal either.
- **TOOL CHANGE NEEDED:** `flight_rights_mcp/data/jurisprudence.json` + `check_extraordinary_circumstances()` in `server.py`. ADD a new case entry (topic e.g. `blitzeinschlag`/`lightning`), analogous to *Pesková* (bird strike): ruling = lightning + mandatory safety inspection **can** be extraordinary **with reasonable-measures caveat**; matched logic should treat it as a *qualified* "yes" (passenger must still check reasonable-measures proof).
- **Sources:**
  - https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62024CJ0399
  - https://aire.aero/the-cjeu-clarifies-extraordinary-circumstances-in-case-of-lightning-struck-aircraft/

---

## 2. General Court T-656/24 — Carrier's own operational decision can break the causal chain
- **Ruling:** General Court, *NI, HZ v European Air Charter AG*, **T-656/24, 4 Mar 2026**. A carrier's **autonomous decision to wait** for passengers delayed by a security-staff shortage (an extraordinary circumstance on an earlier rotation) can **break the direct causal link** between that extraordinary circumstance and a later flight's delay. Following *Austrian Airlines* (C-826/19), mere *sine-qua-non* is insufficient; the carrier's discretionary, non-legally-required decision may become the *determining cause*, defeating the Art. 5(3) defence.
- **Right changed:** Narrows when carriers may rely on an earlier-flight extraordinary circumstance; shifts the burden — the carrier must show its own intervention was not the determining cause.
- **Citizen impact:** If your delay followed an airline's own re-scheduling / waiting decision after some earlier disruption, you likely **still qualify** for compensation even if the airline cites "extraordinary circumstances."
- **TOOL CHANGE NEEDED:** `flight_rights_mcp/data/jurisprudence.json` + `check_extraordinary_circumstances()`. ADD a case entry on "causal-chain break / carrier's own discretionary operational decision" so the checker flags that an airline's intervening decision can defeat an EC defence. Consider a heuristic: if the carrier's own re-routing/waiting decision is the determining cause, the EC defence fails.
- **Sources:**
  - https://curia.europa.eu/site/upload/docs/application/pdf/2026-03/cp260026en.pdf
  - https://www.jurist.org/news/2026/03/eu-court-strengthens-compensation-rights-for-delayed-air-passengers/
  - https://www.lexology.com/library/detail.aspx?g=638e6a8b-7560-4b45-8cb5-c358e5668191

---

## 3. EU air passenger-rights reform — political agreement (not yet in force)
- **Policy:** European Parliament & Council reached a **political agreement (15 Jun 2026)** on the first overhaul of EU air passenger rights in 20+ years (revision of Reg. 261/2004).
  - Compensation thresholds **unchanged**: €250 (<1,500 km) / €400 (1,500–3,500 km) / €600 (>3,500 km) at the 3-hour delay threshold.
  - Airlines must **proactively inform** passengers of their rights + claims procedure **within 96 hours** of a disruption.
  - Extraordinary circumstances **codified in a defined list** with refined application rules (more consistent across Member States).
  - **Ban on no-show policies** for return flights (cannot deny boarding the return leg if outbound was missed; no fee).
  - Fare transparency incl. hand-baggage charges; improved rights for passengers with reduced mobility; optional "EU Passenger Rights" label.
  - **NOT yet in force:** applies 12 months after publication in the Official Journal (pending formal adoption).
- **Right changed:** Procedural reinforcement (96h proactive info), codified EC list, no-show ban. Substantive compensation standard preserved.
- **Citizen impact:** Soon — clearer rights, airlines must tell you proactively, no penalty for missing the outbound leg. Watch for entry-into-force.
- **TOOL CHANGE NEEDED (future):** When in force, align `jurisprudence.json`'s EC list with the codified list; `server.py` could add a "proactive information within 96h" entitlement note. **For now: monitor adoption — do not change logic yet.**
- **Sources:**
  - https://transport.ec.europa.eu/news-events/news/commission-welcomes-landmark-agreement-revised-air-passenger-rights-2026-06-15_en
  - https://cms.law/en/int/legal-updates/new-european-regulation-on-air-passenger-rights-what-impact-for-the-air-transport-sector

---

## 4. Airline policy scan — Lufthansa / Ryanair
No **new compensation-policy change** by a specific airline found in this scan. Lufthansa's published passenger-rights page remains standard EU261 text (lists strikes, security risks, unexpected flight-safety deficiencies as EC examples). The Feb 2026 Lufthansa strike was a discrete event (internal staff strikes are **not** extraordinary circumstances → compensation owed), not a policy change. No agb-reader-mcp clause-catalog impact identified this run.
- Source (reference): https://www.lufthansa.com/dk/en/passenger-rights

---

### Summary
- **2** CJEU/General Court rulings changing extraordinary-circumstances jurisprudence (C-399/24, T-656/24).
- **1** major EU-level policy change (revised Air Passenger Rights Regulation political agreement).
- Both rulings require `jurisprudence.json` + `check_extraordinary_circumstances()` updates (maintainer action — agent did not edit source).
