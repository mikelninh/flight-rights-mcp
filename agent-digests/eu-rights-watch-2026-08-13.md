# EU Rights-Watch — 2026-08-13

**Repo:** flight-rights-mcp · **Branch:** agent/eu-rights-watch-2026-08-13
**Wachhund-Lauf:** 2026-08-13 · **Schwerpunkt:** EuGH/Air-Passenger-Rights + EU-Verbraucherschutz + AGB-Klauselkatalog (agb-reader-mcp)

**Zusammenfassung:** 5 relevante Fundstellen (3 Gerichtsurteile EU261, 2 Politik-Pakete). 1 Urteil erfordert eine Ergänzung des `jurisprudence.json`-Katalogs (`check_extraordinary_circumstances`). 1 Politik-Paket betrifft den AGB-Klauselkatalog (agb-reader-mcp) und den Anspruchsprozess. Alle Funde zweisprachig (DE + EN).

---

## Fund 1 — EuGH C-399/24: Blitzeinschlag kann „außergewöhnlicher Umstand“ sein

- **Headline:** EuGH erlaubt Blitzeinschlag + Pflichtinspektion als außergewöhnlichen Umstand (aber: Beweislast bei Airline).
- **Was hat sich geändert:** Der EuGH (3. Kammer) entschied am 16.10.2025 (ECLI:EU:C:2025:791), dass ein Blitzeinschlag auf einem Flugzeug, der eine zwingende Sicherheitsinspektion auslöst, **grundsätzlich** ein „außergewöhnlicher Umstand“ i.S.d. Art. 5 Abs. 3 VO 261/2004 sein kann — sofern die Airline nachweist, dass sie **alle zumutbaren Maßnahmen** getroffen hat, um die Verspätung zu vermeiden. Die Entscheidung liegt bei der nationalen Instanz (hier: Landesgericht Korneuburg).
- **Warum:** Der EuGH stellt klar: Aus Sicherheitsgründen darf eine Airline nicht durch Pünktlichkeitsdruck zur Vernachlässigung von Sicherheitschecks gezwungen werden. Gleichzeitig bleibt die Ausnahme eng — die Airline trägt die volle Beweislast für die getroffenen Vorsorgemaßnahmen.
- **Wirkung:** Neu seit 16.10.2025. Bisher im `jurisprudence.json` (10 Fälle, Stand 2021) **nicht enthalten** → Katalog-Lücke.
- **Betroffene:** Fluggäste mit Großverspätung/Annullierung, deren Airline sich auf Blitzschlag/Gewitterinspektion beruft (v.a. Austrian Airlines und vergleichbare Fälle).
- **So geht's:** Anspruch schriftlich geltend machen; von der Airline die **konkreten** Vorsorgemaßnahmen und die Inspektionsdokumentation einfordern. Schafft die Airline den Beweis nicht, besteht der Anspruch.
- **Bürgertipp:** „Blitzschlag“ ist keine automatische Freikarte für die Airline. Fordern Sie die Beweislast-Unterlagen — in den meisten Fällen kann die Airline die „allen zumutbaren Maßnahmen“ nicht nachweisen.
- **Quellen:** [EUR-Lex C-399/24 (ECLI:EU:C:2025:791)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A62024CJ0399) · [aire.aero Analyse](https://aire.aero/the-cjeu-clarifies-extraordinary-circumstances-in-case-of-lightning-struck-aircraft/)

### EN
- **Headline:** CJEU allows lightning strike + mandatory inspection as an extraordinary circumstance (but burden of proof stays with the airline).
- **What changed:** The CJEU (Third Chamber) held on 16 Oct 2025 (ECLI:EU:C:2025:791) that a lightning strike on an aircraft triggering a mandatory safety inspection may in principle qualify as an "extraordinary circumstance" under Art. 5(3) Reg. 261/2004 — provided the airline proves it took all reasonable measures to avoid the delay. The final assessment is for the national court (here: Landesgericht Korneuburg, Austria).
- **Why:** For safety reasons, airlines must not be incentivised to skip mandatory safety checks to protect punctuality. The exception remains narrow; the airline carries the full burden of proving the precautions taken.
- **Effective:** 16 October 2025. Not yet present in `jurisprudence.json` (10 cases, last dated 2021) — catalogue gap.
- **Deadline:** None (case law applies now). Claim within your national limitation period.
- **Who's affected:** Passengers with long delay/cancellation where the airline invokes lightning strike / storm inspection (e.g. Austrian Airlines and comparable cases).
- **How:** Assert the claim in writing; demand the airline's concrete precautionary measures and inspection records. If the airline cannot prove "all reasonable measures", compensation is due.
- **Citizen tip:** "Lightning strike" is NOT an automatic free pass for the airline. Demand the burden-of-proof documents — in most cases the airline cannot show it took all reasonable measures.

---

## Fund 2 — EuGH C-558/24: Verspätung zählt ab URSPRÜNGLICHEM Flugplan

- **Headline:** EuGH schließt Schlupfloch: Verspätung wird zum ursprünglichen Plan gemessen, nicht zur neuen Buchungsbestätigung.
- **Was hat sich geändert:** Der EuGH (Corendon Airlines ./. Myflyright GmbH, C-558/24, Urteil veröffentlicht 30.10.2025) stellte klar: Wird ein Flug kurz vor Abflug verschoben und eine **neue Buchungsbestätigung** mit anderen Zeiten ausgestellt, muss die Verspätung trotzdem am **ursprünglich geplanten Ankunftszeitpunkt** gemessen werden. Eine Vorverlegung/ Verschiebung durch die Airline darf den Entschädigungsanspruch nicht aushebeln.
- **Warum:** Andernfalls könnten Airlines beliebig „umplanen", um Betroffene unter die 3-Stunden-Schwelle zu drücken — das würde den Schutzzweck der VO 261/2004 unterlaufen. Ein verschobener Flug mit gleicher Route/Flugnummer bleibt eine „Verspätung", keine Annullierung.
- **Wirkung:** Neu seit 30.10.2025. Bestätigt die Sturgeon-Linie (C-402/07); schließt ein von Airlines genutztes Umgehungs-Manöver.
- **Betroffene:** Alle Fluggäste, deren Airline kurzfristig umplant und dann die Verspätung „neu berechnet" (typisch bei Corendon, aber analog für alle Carrier).
- **So geht's:** Bei der Entschädigungsberechnung immer die **Differenz zur ursprünglichen Ankunftszeit** ansetzen — nicht zur neuen Bestätigung. Im Forderungsschreiben die ursprüngliche Buchung als Maßstab zitieren.
- **Bürgertipp:** Hat die Airline Ihren Flug verschoben und behauptet „unter 3 Stunden Verspätung"? Rechnen Sie vom ursprünglichen Plan — ab 3 h ist der volle Anspruch fällig.
- **Quellen:** [Myflyright Pressemitteilung (C-558/24)](https://myflyright.com/about-us/press/court-of-justice-european-union-rules-in-favour-of-myflyright/) · [aire.aero Analyse](https://aire.aero/cjeu-rules-original-flight-arrival-time-determines-passenger-compensation/)

### EN
- **Headline:** CJEU closes loophole: delay is measured against the ORIGINAL schedule, not the new booking confirmation.
- **What changed:** The CJEU (Corendon Airlines v Myflyright GmbH, C-558/24, judgment published 30 Oct 2025) clarified that when a flight is postponed shortly before departure and a new booking confirmation with different times is issued, the delay must still be measured against the originally scheduled arrival time. A rescheduling by the airline cannot defeat the compensation claim.
- **Why:** Otherwise airlines could reshuffle timings at will to push affected passengers below the 3-hour threshold, undermining the protective aim of Reg. 261/2004. A postponed flight with the same route/flight number remains a "delay", not a cancellation.
- **Effective:** 30 October 2025. Confirms the Sturgeon line (C-402/07); closes an airline avoidance manoeuvre.
- **Deadline:** None (applies now).
- **Who's affected:** All passengers whose airline reschedules shortly before departure and then "recalculates" the delay (typical of Corendon, but analogously all carriers).
- **How:** Always base the compensation calculation on the difference to the ORIGINAL arrival time — not the new confirmation. Cite the original booking as the benchmark in your demand letter.
- **Citizen tip:** Did the airline move your flight and claim "under 3 hours late"? Calculate from the original schedule — at 3+ hours the full claim is due.

---

## Fund 3 — Gericht erster Instanz T-656/24: Eigenes Warten des Carriers bricht Kausalkette

- **Headline:** EuG: Entscheidet sich die Airline freiwillig zu warten, fällt der Schutz der „außergewöhnlichen Umstände" weg.
- **Was hat sich geändert:** Das Gericht erster Instanz (T-656/24, NI & HZ ./. European Air Charter, Urteil 04.03.2026) entschied: Ein Carrier kann sich auf einen außergewöhnlichen Umstand eines Vorflugs (hier: Personalausfall an der Sicherheitskontrolle) nur berufen, wenn eine **direkte Kausalkette** zur Verspätung des Folgeflugs besteht. Die **freiwillige Entscheidung der Airline, auf verspätete Passagiere zu warten**, kann diese Kausalkette unterbrechen — dann haftet die Airline für den Folgeflug.
- **Warum:** Eine „Interessenabwägung" zwischen Passagiegruppen ist keine Befreiungsklausel des Art. 5 Abs. 3. Trifft die Airline eine eigene, nicht rechtlich gebotene Entscheidung, die zur Verspätung wird, entfällt der Ausnahmeschutz.
- **Wirkung:** 04.03.2026 (rechtskräftig, sofern nicht binnen 2 Monaten zuerstinstanzlich angefochten). Stärkt die strenge Auslegung des Art. 5 Abs. 3.
- **Betroffene:** Fluggäste auf Folgeflügen, deren Airline sich auf einen Vorfall am Vorflug beruft, aber selbst operativ eingegriffen hat.
- **So geht's:** Prüfen, ob die Airline eigenmächtig umdisponiert hat (anderer Flieger, Warten, Verschiebung). Falls ja: Kausalkette bestreiten und Anspruch geltend machen.
- **Bürgertipp:** „Der Vorflug hatte Verspätung" ist keine Ausrede, wenn die Airline selbst umgeplant hat. Nachforschungen zum tatsächlichen Ablauf lohnen sich.
- **Quellen:** [DAC Beachcroft Analyse (T-656/24)](https://www.dacbeachcroft.com/en/What-we-think/EU261-flight-delay-claims-when-airline-choices-break-the-causal-chain)

### EN
- **Headline:** General Court: a carrier's voluntary decision to wait breaks the "extraordinary circumstances" shield.
- **What changed:** The General Court (T-656/24, NI & HZ v European Air Charter, judgment 4 Mar 2026) held that a carrier may rely on an extraordinary circumstance of a preceding flight only if a direct causal link to the delay of the subsequent flight exists. The carrier's voluntary decision to wait for delayed passengers can break that causal link — then the carrier is liable for the later flight.
- **Why:** A balancing of interests between passenger groups is no exemption clause under Art. 5(3). Where the airline takes its own, non-legally-required decision that becomes the cause of the delay, the protective shield falls away.
- **Effective:** 4 March 2026 (final unless appealed on points of law within 2 months). Reinforces the strict reading of Art. 5(3).
- **Deadline:** None (applies now).
- **Who's affected:** Passengers on subsequent rotations where the airline invokes a preceding-flight incident but intervened operationally itself.
- **How:** Check whether the airline reorganised on its own (different aircraft, waiting, rescheduling). If so, dispute the causal link and claim.
- **Citizen tip:** "The previous flight was delayed" is no excuse if the airline reshuffled operations itself. Investigating the actual sequence pays off.

---

## Fund 4 — EU-Parlament reformiert Fluggastrechte (Trilog-Einigung, 07.07.2026)

- **Headline:** EU-Parlament verabschiedet Upgrade der Fluggastrechte: 9-Monats-Frist, 30-Tage-Zahlung, kostenloses Handgepäck, Sitzplatz für Kinder.
- **Was hat sich geändert:** Das EU-Parlament bestätigte am 07.07.2026 (646:12:3) die im Conciliation Committee erzielte Einigung zur Reform der Fluggastrechte (VO 261/2004-Nachfolge). Kernpunkte: Fluggäste haben **9 Monate** Zeit, einen Entschädigungsantrag zu stellen; Airlines haben **30 Tage**, um zu zahlen oder außergewöhnliche Umstände darzulegen; automatische Erstattungsoption; **ein persönliches Mitführgepäckstück kostenlos** (und im Ticketpreis von Anfang an ausgewiesen); **kostenloser Sitzplatz neben begleitenden Personen für Kinder <14 J., Behinderte, Schwangere**; kostenlose Korrektur von Rechtschreibfehlern im Namen und kostenloser Ausdruck der Bordkarte; **Rückflug auch ohne genutzten Hinflug** nutzbar. Entschädigungshöhen (250/400/600 €) und 50%-Regel bleiben.
- **Warum:** Mehr als 13 Jahre Blockade wurden beendet; bestehende Rechte (Erstattung, 3-h-Schwelle, Ausgleich) wurden verteidigt und durch family-/verbraucherfreundliche Regeln ergänzt.
- **Wirkung:** Noch **nicht in Kraft**. Rat muss bis **Anfang August 2026** bestätigen; Inkrafttreten 20 Tage nach Veröffentlichung im Amtsblatt; **1 Jahr** Umsetzungsfrist für Mitgliedstaaten/Unternehmen.
- **Betroffene:** Alle EU-Flugreisenden (künftig); betrifft direkt den **AGB-Klauselkatalog (agb-reader-mcp)** — Klauseln zu Handgepäck-Zusatzgebühren und Sitzplatz-Zusatzentgelten werden nach Inkrafttreten unzulässig. Auch der Anspruchsprozess in flight-rights-mcp (30-Tage-Frist, 9-Monats-Fenster) ist betroffen.
- **So geht's:** Noch gelten die aktuellen nationalen Verjährungsfristen (DE 3 J). Sobald die Reform in Kraft ist, das 9-Monats-Antragsfenster im Blick behalten.
- **Bürgertipp:** Die neuen Regeln sind noch nicht wirksam — aktuell weiter nach EU261 + nationaler Verjährung vorgehen. Sobald in Kraft: innerhalb von 9 Monaten den Antrag stellen, sonst verfällt der Anspruch.
- **Quellen:** [Europäisches Parlament, Pressemitteilung 20260703IPR46273](https://www.europarl.europa.eu/news/en/press-room/20260703IPR46273/european-parliament-achieves-upgrade-to-air-passenger-rights) · [Gemeinsamer Text des Rates (PE-39-2026-INIT)](https://data.consilium.europa.eu/doc/document/PE-39-2026-INIT/en/pdf)

### EN
- **Headline:** EU Parliament adopts air passenger rights upgrade: 9-month filing window, 30-day payment, free carry-on, child seating.
- **What changed:** On 7 July 2026 (646:12:3) the European Parliament confirmed the Conciliation Committee deal reforming air passenger rights (successor to Reg. 261/2004). Key points: passengers get a 9-month window to file a compensation request; airlines have 30 days to pay or invoke extraordinary circumstances; automatic reimbursement option; one personal carry-on item free (and shown in the fare from the start); free adjacent seat for companions of children under 14, persons with disabilities and pregnant travellers; free name-spelling correction and free printed boarding pass; return leg of a round trip usable without the outbound leg. Compensation amounts (€250/400/600) and the 50% rule are maintained.
- **Why:** Ends 13+ years of deadlock; existing rights (refund, 3-hour threshold, compensation) defended and supplemented with family/consumer-friendly rules.
- **Effective:** NOT yet in force. Council must confirm by early August 2026; entry into force 20 days after Official Journal publication; 1-year implementation period for member states/companies.
- **Deadline:** Council confirmation expected by beginning of August 2026.
- **Who's affected:** All EU air travellers (future); directly affects the AGB clause catalogue (agb-reader-mcp) — clauses on carry-on surcharges and seating fees become prohibited once in force. The claims process in flight-rights-mcp (30-day rule, 9-month window) is also affected.
- **How:** Until in force, current national limitation periods apply (DE 3 years). Once in force, watch the 9-month filing window.
- **Citizen tip:** The new rules are not yet effective — proceed under EU261 + national limitation for now. Once in force: file within 9 months or the claim lapses.

---

## Fund 5 — EU-Verbraucherschutz 2026: Digital Fairness Act, Widerrufsbutton, Garantiehinweis

- **Headline:** EU-Verbraucherschutz-Paket 2026 greift bei AGB/Dark Patterns: Widerrufsbutton (19.06.2026), Garantiehinweis (27.09.2026), Digital Fairness Act (Q4 2026).
- **Was hat sich geändert:** Mehrere EU-Verbraucherschutz-Neuerungen 2026 betreffen Allgemeine Geschäftsbedingungen (AGB) und Online-Verträge: **verpflichtender Widerrufsbutton** für Fernabsatzverträge ab **19.06.2026** (Änderung der Verbraucherrechterichtlinie 2011/83/EU); **einheitlicher gesetzlicher Garantiehinweis + Haltbarkeitslabel** ab **27.09.2026** (RL (EU) 2024/825 + VO (EU) 2025/1960); **Digital Fairness Act** (geplant Q4 2026) gegen Dark Patterns, addictive Design, Influencer-Marketing, personalisierte Preise, digitale Abo-Fallen.
- **Warum:** Schließung von Lücken im EU-Verbraucherrecht, Harmonisierung über Mitgliedstaaten hinweg, stärkerer Schutz vor unlauteren Online-Praktiken.
- **Wirkung:** Widerrufsbutton und Garantiehinweis bereits ab Mitte/Ende 2026 wirksam (nach Umsetzung); DFA in Q4 2026 erwartet (Entwurf).
- **Betroffene:** Online-Händler und -Dienste; direkter Bezug zum **AGB-Klauselkatalog (agb-reader-mcp)**: Klauseln mit verschleierten Widerrufs-Hürden, Dunkelmustern oder intransparenten Preisen werden angreifbar. Auch für Flug-AGB (z.B. Sitzplatz-/Gepäck-Zuschläge) relevant im Zusammenspiel mit Fund 4.
- **So geht's:** AGB auf Dark Patterns, verschleierte Widerrufsbuttons und intransparente Zusatzkosten prüfen; Betroffene sollten den neuen Widerrufsbutton nutzen.
- **Bürgertipp:** Ab 19.06.2026 muss Online-Widerruf ein einfacher Button sein — fehlt er, ist die Klausel fragwürdig. Bei Flug-AGB besonders auf versteckte Gepäck-/Sitzplatz-Zuschläge achten.
- **Quellen:** [EU-Kommission Verbraucherschutzrecht](https://commission.europa.eu/law/law-topic/consumer-protection-law_en) · [RL (EU) 2024/825 (EUR-Lex)](https://eur-lex.europa.eu/eli/dir/2024/825/oj/eng) · [Global Policy Watch 2026 Consumer Protection](https://www.globalpolicywatch.com/2026/02/what-to-watch-in-2026-key-developments-in-emea-consumer-protection/)

### EN
- **Headline:** EU 2026 consumer-protection package hits AGB/dark patterns: withdrawal button (19.06.2026), guarantee notice (27.09.2026), Digital Fairness Act (Q4 2026).
- **What changed:** Several 2026 EU consumer-protection updates affect general terms (AGB) and online contracts: a mandatory online withdrawal button for distance contracts from 19.06.2026 (amendment of Consumer Rights Directive 2011/83/EU); a harmonised statutory guarantee notice + commercial durability label from 27.09.2026 (Dir. (EU) 2024/825 + Reg. (EU) 2025/1960); the Digital Fairness Act (expected Q4 2026) targeting dark patterns, addictive design, influencer marketing, personalised pricing and digital subscription traps.
- **Why:** Closes gaps in EU consumer law, harmonises across member states, strengthens protection against unfair online practices.
- **Effective:** Withdrawal button and guarantee notice effective mid/late 2026 (post-transposition); DFA expected Q4 2026 (draft).
- **Deadline:** Withdrawal button from 19 June 2026; guarantee notice/label from 27 September 2026.
- **Who's affected:** Online traders and services; direct relevance to the AGB clause catalogue (agb-reader-mcp): clauses with hidden withdrawal hurdles, dark patterns or opaque pricing become challengeable. Also relevant for airline AGB (seating/baggage surcharges) alongside Finding 4.
- **How:** Review AGB for dark patterns, obscured withdrawal buttons and non-transparent surcharges; affected consumers should use the new withdrawal button.
- **Citizen tip:** From 19.06.2026 online withdrawal must be a simple button — if it's missing, the clause is questionable. For airline AGB, watch hidden baggage/seating surcharges.

---

## ⚙️ Empfohlene Tool-Änderungen (für Maintainer)

**Fund 1 (C-399/24) erfordert eine Ergänzung von `flight_rights_mcp/data/jurisprudence.json`** — der `check_extraordinary_circumstances`-Tool prüft gegen diesen Katalog. Vorgeschlagener Eintrag für das `cases`-Array (kopieren & einfügen):

```json
{
  "id": "airhelp-c399-24",
  "citation": "EuGH, Urt. v. 16.10.2025 — C-399/24 (AirHelp Germany ./. Austrian Airlines)",
  "topic": "blitzeinschlag",
  "keywords": ["lightning", "Blitzschlag", "Blitz", "Gewitter", "lightning strike", "election", "electrical storm", "Pflichtinspektion", "Sicherheitsinspektion"],
  "ruling": "Ein Blitzeinschlag auf dem Flugzeug, der eine zwingende Sicherheitsinspektion auslöst, KANN ein außergewöhnlicher Umstand sein — sofern die Airline nachweist, dass sie alle zumutbaren Maßnahmen getroffen hat, die Verspätung zu vermeiden.",
  "result_for_passenger": "Kein Anspruch, WENN die Airline die zumutbaren Vorsorgemaßnahmen nachweist; sonst Anspruch besteht.",
  "exceptions": "Airline muss alle zumutbaren Maßnahmen beweisen; nationales Gericht prüft im Einzelfall.",
  "source_url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A62024CJ0399"
}
```

**Fund 2 (C-558/24):** Tool-Logik bleibt (berechnet aus übergebener `delay_hours`), aber der Ratgebertext von `generate_claim_letter` / `calculate_compensation` sollte betonen: Verspätung ist zum **ursprünglichen** Plan zu messen. Optional: ein neuer `cases`-Eintrag zum Thema „umgeplanter Flug / Verspätung ab Ursprungsplan".

**Fund 4 & 5:** Betreffen primär **agb-reader-mcp** (Klauselkatalog: Handgepäck-Zusatzgebühren, Sitzplatz-Entgelte, Widerrufs-Hürden, Dark Patterns) — dort bei Inkrafttreten der Reform entsprechende Klausel-Muster als „unzulässig" markieren.

---

*Erstellt vom EU-CITIZEN-RIGHTS-WATCH-Agent · read-only watchdog · keine merges/force-pushes. Quellen sind echte URLs (EUR-Lex, Europäisches Parlament, EU-Kommission, Fachanalysten).*
