# EU Rights-Watch Digest — 2026-08-30

Watchdog-Report für `flight-rights-mcp` (cross-ref: `agb-reader-mcp`).
Status: **3 Befunde** — 2 neue EuGH/EuG-Rechtsprechungen + 1 gesetzgeberische Grundsatzeinigung.
Hinweis: Es wurden **keine** Tool-Quelldateien verändert (Guardrail: nur `agent-digests/` + `agent-logs/`). Die nötigen Änderungen sind unten als Maintainer-Anleitung notiert.

---

## Befund 1 — EuGH C-399/24: Blitzeinschlag + Pflichtinspektion = außergewöhnlicher Umstand

- **Recht ändert sich:** Der EuGH (3. Kammer) hat am **16.10.2025** (ECLI:EU:C:2025:791, AirHelp Germany ./. Austrian Airlines, Vorlage LG Korneuburg) entschieden, dass ein Blitzeinschlag auf ein Flugzeug, der zu einer zwingenden Sicherheitsinspektion und verspäteter Wiederinbetriebnahme führt, ein „außergewöhnlicher Umstand“ i.S.d. Art. 5 Abs. 3 VO 261/2004 **sein kann** — sofern die Airline nachweist, dass sie alle zumutbaren Maßnahmen ergriffen hat. Die Beweislast (Vorsorge) liegt bei der Airline.
- **Bürgerauswirkung:** Bei Verspätung/Annullierung wegen Blitzeinschlag + Inspektion besteht **in der Regel KEIN** Ausgleichsanspruch nach Art. 7 — anders als bei gewöhnlichen technischen Defekten (Wallentin-Hermann, C-549/07). Die Betreuungs- (Art. 9) und Erstattungsansprüche (Art. 8) bleiben aber voll bestehen.
- **Tool-Änderung nötig (flight-rights-mcp):** In `data/jurisprudence.json` einen neuen Eintrag für `check_extraordinary_circumstances` anlegen, z.B.:
  - `id`: `"airhelp-c399-24"` · `citation`: `"EuGH, Urt. v. 16.10.2025 — C-399/24 (AirHelp ./. Austrian Airlines)"` · `topic`: `"blitzeinschlag"`
  - `keywords`: `["Blitz","lightning","Blitzeinschlag","Einschlag","Gewitter","Sicherheitsinspektion","Pflichtinspektion"]`
  - `ruling`: `"Blitzeinschlag mit anschließender zwingender Sicherheitsinspektion ist außergewöhnlicher Umstand nach Art. 5(3), sofern die Airline alle zumutbaren Maßnahmen nachweist."`
  - `result_for_passenger`: `"Kein Ausgleich i.d.R., wenn Airline Vorsorge nachweist; Betreuung/Erstattung (Art. 8/9) bleiben bestehen."` (Muss „Kein Ausgleich“ enthalten, damit der Tool-Flag `likely_extraordinary` korrekt greift.)
  - `source_url`: `"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A62024CJ0399"`
- **Quelle:** https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A62024CJ0399

### EN
- **Headline:** CJEU C-399/24 — lightning strike plus mandatory inspection can be an extraordinary circumstance
- **What changed:** The Court of Justice (Third Chamber), judgment of 16 October 2025 (ECLI:EU:C:2025:791, AirHelp Germany v Austrian Airlines), held that a lightning strike on an aircraft triggering mandatory safety inspections and a delayed return to service may qualify as an "extraordinary circumstance" under Article 5(3) of Regulation 261/2004 — provided the airline proves it took all reasonable measures. Burden of proof stays with the airline.
- **Why:** Passenger safety is a fundamental objective; classifying such a lightning event as extraordinary prevents airlines from being incentivised to prioritise punctuality over safety, while the strict two-pronged test (not inherent + outside control) still applies.
- **Effective:** Ruling delivered 16 October 2025; applies immediately in national proceedings (remitted to the Austrian court for the facts).
- **Deadline:** None — binding on referring courts now.
- **Who's affected:** Passengers on flights delayed/cancelled due to a lightning strike and subsequent mandatory inspection (e.g. Austrian Airlines, and any EU carrier).
- **How:** File/just defend a claim: the airline may escape Article 7 compensation only by proving all reasonable measures; care (Art. 9) and reimbursement (Art. 8) rights remain regardless.
- **Citizen tip:** If the airline blames a "lightning strike," ask for written proof of the mandatory inspection AND proof of all reasonable measures taken — otherwise keep pushing for compensation; care and refund rights still apply.

---

## Befund 2 — EuG T-656/24: Eigenentscheidung der Airline kann Kausalkette zum außergewöhnlichen Umstand unterbrechen

- **Recht ändert sich:** Das Europäische Gericht (Pressemitteilung Nr. 26/26 vom **04.03.2026**, European Air Charter, Vorlage LG Düsseldorf) stellte klar: Eine Airline kann sich bei einem Folgeflug in einer Flugrotation **nicht** auf einen außergewöhnlichen Umstand aus einem Vorflug berufen, wenn ihre eigene autonome Entscheidung (z.B. Warten auf durch Sicherheitskontroll-Engpässe verspätete Passagiere, anschließende Umbuchung auf Ersatzflugzeug) die **bestimmende Ursache** der Verspätung des Folgeflugs ist.
- **Bürgerauswirkung:** Entscheidet die Airline den Folgeflug „aus eigenem Antrieb“ (nicht rechtlich gezwungen) anders als der außergewöhnliche Umstand es erfordert, reißt die Kausalkette — der Ausgleichsanspruch (Art. 7) bleibt bestehen, obwohl am Vorflug ein echter außergewöhnlicher Umstand lag.
- **Tool-Änderung nötig (flight-rights-mcp):** `check_extraordinary_circumstances` um einen Hinweis ergänzen, dass die Kausalität bei eigenmächtigen Airline-Entscheidungen (Rotations-/Umbuchungs-Entscheidung) reißen kann. Empfohlene Ergänzung in `jurisprudence.json` (eigenes Feld oder Notiz im `ruling` eines „Rotations“-Eintrags):
  - `keywords`: `["Rotationsentscheidung","eigenmächtige Verzögerung","Sicherheitskontrolle Vorflug","Umbuchung Ersatzflugzeug"]`
  - `ruling`: „Eine autonome Airline-Entscheidung (z.B. Warten auf verspätete Passagiere eines Vorflugs) kann die direkte Kausalität zwischen außergewöhnlichem Umstand und Folgeflug-Verspätung unterbrechen — dann besteht der Anspruch.“
  - `result_for_passenger`: „Anspruch besteht, wenn die Airline den Folgeflug eigenmächtig verzögert hat (Kausalität unterbrochen).“ (Darf NICHT „Kein Ausgleich“ enthalten, sonst falscher Flag.)
  - `source_url`: `"https://curia.europa.eu/site/upload/docs/application/pdf/2026-03/cp260026en.pdf"`
- **Quelle:** https://curia.europa.eu/site/upload/docs/application/pdf/2026-03/cp260026en.pdf

### EN
- **Headline:** General Court T-656/24 — an airline's own decision can break the causal link to an extraordinary circumstance
- **What changed:** The General Court (press release No 26/26 of 4 March 2026, European Air Charter, reference from the Regional Court Düsseldorf) held that an airline may not rely on an extraordinary circumstance affecting an earlier flight in a rotation if its autonomous decision (e.g. waiting for passengers delayed by security-check shortcomings, then reassigning to a replacement aircraft) is the determining cause of the subsequent flight's delay.
- **Why:** Regulation 261/2004 does not define the required "direct" causal link; by analogy to EU non-contractual liability, the link must be sufficiently direct so that the airline's conduct is the determining cause. The airline's commercial interest in transporting earlier passengers is not a valid defence.
- **Effective:** Ruling of 4 March 2026; final once no review is proposed by the First Advocate General within one month.
- **Deadline:** None for citizens; national court assesses the facts.
- **Who's affected:** Passengers on a later flight in a rotation where the airline "absorbed" a delay from an earlier flight's extraordinary circumstance by its own operational choice.
- **How:** Argue the causal chain broke: the airline's own decision — not the original extraordinary event — caused your delay. The burden is on the airline to show it was legally obliged to act as it did.
- **Citizen tip:** If the airline says "earlier flight's weather/security problem caused your delay," check whether the airline voluntarily waited or rebooked — that autonomous choice can restore your compensation claim.

---

## Befund 3 — EU: Historische Grundsatzeinigung zur Stärkung der Fluggastrechte (15.06.2026)

- **Recht ändert sich:** Rat und Europäisches Parlament erzielten am **15.06.2026** nach 13 Jahren Verhandlung eine Grundsatzeinigung zur ersten Reform der EU-Fluggastrechte seit 2004. Kernpunkte: Airline muss den Entschädigungsanspruch binnen **96 Stunden** elektronisch mitteilten und binnen **30 Tagen** zahlen oder schriftlich begründet ablehnen; „außergewöhnliche Umstände“ müssen kausal sein und die **Beweislast** liegt bei der Airline (inkl. Nachweis aller zumutbaren Maßnahmen); **No-Show-Verbot** (kein Entzug der Rückflug-/Anschlussrechte bei Nichtantritt des Hinflugs); **Handgepäck im Basispreis inkludiert** (Preistransparenz); gestärkte Rechte für PRM (Menschen mit Behinderung), Schwangere, Kinder, Unaccompanied Minors (Sitzplatzgarantie, kostenlose Assistenz, Ersatz bei Verlust von Mobilitätshilfen).
- **Bürgerauswirkung:** Schnellere, transparentere Ansprüche; klarere Beweislast zulasten der Airline bei außergewöhnlichen Umständen; keine No-Show-Strafen mehr; besserer Schutz vulnerabler Gruppen. **Entschädigungshöhen BLEIBEN bei €250 / €400 / €600** (BEUC warnte zuvor vor einer Kürzung um 67 % auf €83 — die Einigung verhindert dies).
- **Hinweis agb-reader-mcp (Cross-Referenz):** No-Show-Klauseln und separat berechnetes Handgepäck in AGB deutscher Airlines/Reiseveranstalter werden künftig EU-rechtswidrig und sollten im Klausel-Katalog als „unzulässig (künftig/stand-by bis Inkrafttreten)“ markiert werden.
- **Status / Effektiv:** Noch **nicht in Kraft** — formelle Annahme durch Parlament und Rat nach rechts- und sprachlicher Prüfung steht aus (Stand 30.08.2026). Kommission prüft binnen 3 Jahren eine Ausweitung auf Drittstaats-Airlines.
- **Tool-Änderung nötig (flight-rights-mcp):** `calculate_compensation` / `check_eu261_applicability`: **vorerst KEINE Zahländerung** (Beträge unverändert). Sobald die Verordnung in Kraft tritt: Dokumentation/FAQ um neue Fristen (96h Info, 30 Tage Antwort) und No-Show-Verbot ergänzen; optional neue Tools/Felder für „PRM-Rechte“ und „Handgepäck inklusive“.
- **Quelle:** https://www.consilium.europa.eu/en/press/press-releases/2026/06/15/council-and-parliament-reach-landmark-agreement-on-stronger-eu-air-passenger-rights/
- **Zusatzquelle (Risiko-Kontext):** https://www.beuc.eu/letters/joint-call-eu-policymakers-uphold-and-strengthen-air-passenger-rights

### EN
- **Headline:** EU institutions agree landmark overhaul of air passenger rights (15 June 2026)
- **What changed:** On 15 June 2026 the Council and European Parliament reached a provisional agreement on the first revision of EU air passenger rights since 2004. Airlines must inform passengers of a compensation claim electronically within 96 hours and either pay or give a reasoned refusal within 30 days; "extraordinary circumstances" require a direct causal link with the burden of proof on the airline; a "no-show" clause ban (no loss of return/connecting rights if you miss the outbound leg); hand baggage included in the displayed base fare; and reinforced rights for passengers with reduced mobility, pregnant travellers, children and unaccompanied minors.
- **Why:** After 13 years of legal uncertainty from evolving case law, the modernised framework aims to deliver certainty, fairness and stronger protection while keeping a level playing field for airlines.
- **Effective:** NOT yet in force. Formal adoption by Parliament and Council after legal-linguistic review is pending (as of 30 August 2026). Commission to assess extension to third-country carriers within 3 years.
- **Deadline:** Watch for the final adoption/entry-into-force date — to be confirmed.
- **Who's affected:** All air passengers on EU routes (intra-EU, into the EU on EU carriers, and departing the EU on any carrier).
- **How:** Once in force: claim electronically, expect airline acknowledgement + decision within 30 days; no-show no longer forfeits your return flight; hand baggage is included by default; PRM/children get free seating together and priority assistance.
- **Citizen tip:** Compensation amounts stay €250/€400/€600 — don't accept airline offers to cut them. Track the entry-into-force date; until then, current 261/2004 rights apply. Note: BEUC had warned of a planned 67% cut to €83 — the agreement preserves the current levels.

---

## Zusammenfassung / Quellen

Geteilte Quellenliste (alle Befunde):
- EuGH C-399/24 (Lightning): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A62024CJ0399
- EuG T-656/24 (Rotations-Kausalität): https://curia.europa.eu/site/upload/docs/application/pdf/2026-03/cp260026en.pdf
- Rat/Parlament Grundsatzeinigung (15.06.2026): https://www.consilium.europa.eu/en/press/press-releases/2026/06-15/council-and-parliament-reach-landmark-agreement-on-stronger-eu-air-passenger-rights/
- BEUC Warnung (67%-Kürzung): https://www.beuc.eu/letters/joint-call-eu-policymakers-uphold-and-strengthen-air-passenger-rights

**Maintainer-Aktionen (Menschliche Prüfung erforderlich — Agent mergt NICHT):**
1. `jurisprudence.json` um Eintrag `airhelp-c399-24` (Blitz) ergänzen.
2. `jurisprudence.json` um Rotations-/Kausalitäts-Hinweis (EuG T-656/24) ergänzen.
3. `calculate_compensation`/`check_eu261_applicability` Dokumentation um 96h/30-Tage-Fristen + No-Show-Verbot ergänzen, sobald Verordnung in Kraft.
4. `agb-reader-mcp`: No-Show- und Handgepäck-Klauseln als künftig EU-rechtswidrig markieren.
