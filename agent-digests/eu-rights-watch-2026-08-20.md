# EU Rights-Watch — Digest 2026-08-20

Automatisierter Watchdog-Lauf für `flight-rights-mcp` (und Querverweis `agb-reader-mcp`).
Zweisprachig: Deutsche Felder, dann `### EN`-Block (gleiche Fakten). Quellen sind geteilt.

---

## Fund 1 — EuGH: Blitzeinschlag am Flugzeug = außergewöhnlicher Umstand

- **Fund:** EuGH, Urt. v. 16.10.2025 — C-399/24 (AirHelp Germany GmbH / Austrian Airlines AG)
- **Was sich ändert:** Ein Blitzeinschlag am Flugzeug eines *Vorflugs*, der zwingende Sicherheitsprüfungen durch zertifizierte Techniker nach sich zieht, ist ein „außergewöhnlicher Umstand“ i.S.d. Art. 5 Abs. 3 VO (EG) 261/2004 — vom Gericht ausdrücklich vergleichbar mit einem Vogelschlag (Pešková, C-315/15). Die Airline haftet für die dadurch verspätete *Folge*-Maschine NICHT auf Ausgleich nach Art. 7.
- **Bürgerwirkung:** Wer wegen eines Blitzschadens am Vorflug (Sicherheitscheck ca. 5 Std.) mehr als 3 h verspätet ankommt, hat in der Regel KEINEN Entschädigungsanspruch — anders als bei bloßen „technischen Problemen“ (Wallentin-Hermann, C-549/07). Die Betreuungspflicht nach Art. 9 (Verpflegung/Hotel) bleibt bestehen. Bürger sollten die Ausrede „technisches Problem“ nicht verwechseln: Blitzschaden am Flugzeug ist rechtlich anders zu bewerten als ein Motorschaden.
- **Tool-Änderung (flight-rights-mcp):** `flight_rights_mcp/data/jurisprudence.json` um einen neuen Fall ergänzen (z.B. id `airhelp-c399-24`, topic `blitzeinschlag`), keywords `["lightning","Blitzeinschlag","blitz","gewitter am flugzeug","lightning strike"]`, ruling = außergewöhnlich/kein Anspruch (analog Pešková). `check_extraordinary_circumstances` muss diesen Treffer als `likely_extraordinary = True` auswerten.

**Quellen:**
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:62024CJ0399
- https://www.lexology.com/library/detail.aspx?g=1dc2fbe2-18d8-47fe-a25b-078df172150d

### EN
- **Headline:** CJEU: lightning strike on an aircraft is an extraordinary circumstance (Case C-399/24)
- **What changed:** A lightning strike on a preceding flight's aircraft that triggers mandatory safety inspections by certified technicians is an "extraordinary circumstance" under Article 5(3) of Regulation (EC) 261/2004, explicitly compared to a bird strike (Pešková, C-315/15). The carrier is therefore not liable for compensation under Article 7 for the consequent delayed flight.
- **Why:** Article 5(3) is a derogation from the passenger's right to compensation and must be strictly interpreted; a lightning strike is, by its nature, comparable to a collision with a foreign body (bird strike), unlike a premature technical malfunction of aircraft components.
- **Effective:** Judgment of 16 October 2025 (applicable law now).
- **Deadline:** None — already in force as case law.
- **Who's affected:** Passengers on flights delayed >3h because the operating aircraft was struck by lightning on a prior rotation.
- **How:** Claim handler should recognise the airline's "lightning/technical" excuse as valid only where it concerns an actual strike on the aircraft requiring mandatory inspection; care rights (Art. 9) still apply.
- **Citizen tip:** If your delay was caused by a lightning strike on the plane itself, compensation is likely denied — but if the airline just says "technical problem," that is NOT an extraordinary circumstance (Wallentin-Hermann). Know the difference.

---

## Fund 2 — EuG: Vorflug-Umstand schützt nicht bei eigener Warte-Entscheidung

- **Fund:** Gericht der EU (EuG), Urt. v. 04.03.2026 — T-656/24 (European Air Charter)
- **Was sich ändert:** Eine Airline darf sich NICHT auf einen außergewöhnlichen Umstand berufen, der einen *Vorflug* in einer Rotation betraf, wenn ihre eigene autonome Entscheidung (hier: Warten auf Passagiere eines Vorflugs, die wegen Security-Check-Engpässen am Flughafen Köln/Bonn zu spät kamen) die *bestimmende Ursache* der Verspätung des Folgeflugs ist.
- **Bürgerwirkung:** Auch wenn am Vorflug ein außergewöhnlicher Umstand vorlag (z.B. Chaos bei Sicherheitskontrollen), kann die eigene Warte-Entscheidung der Airline die Kausalkette unterbrechen. Der Entschädigungsanspruch kann dann BESTEHEN. Bürger sollten die „Vorflug-Ausrede“ nicht ungeprüft akzeptieren — entscheidend ist die bestimmende Ursache.
- **Tool-Änderung (flight-rights-mcp):** `check_extraordinary_circumstances` um einen Hinweis ergänzen, dass die Kausalitätsprüfung („determinierende Ursache“) die EC-Ausnahme brechen kann; ggf. neue Fall-ID `rotation-kausalitaet` in `jurisprudence.json` mit Keyword `["rotation","vorflug","waiting for passengers","sicherheitscheck vorflug"]`.

**Quellen:**
- https://curia.europa.eu/site/upload/docs/application/pdf/2026-03/cp260026en.pdf

### EN
- **Headline:** General Court: airline cannot hide behind an earlier-flight event if its own wait decision caused the delay (Case T-656/24)
- **What changed:** An air carrier may not rely on an extraordinary circumstance affecting an earlier flight in a rotation if its autonomous decision (here: waiting for passengers of a prior flight delayed by security-check shortcomings at Cologne/Bonn Airport) is the determining cause of the delay of the subsequent flight.
- **Why:** Regulation 261/2004 does not define the "direct" nature of the causal link; by analogy to EU non-contractual liability, the link must be sufficiently direct so that the conduct complained of is the determining cause of the damage. The carrier is not required to weigh the interests of different passenger groups.
- **Effective:** Judgment of 4 March 2026 (preliminary ruling from the General Court; may exceptionally be reviewed by the CJEU).
- **Deadline:** None.
- **Who's affected:** Passengers on a later flight in a rotation delayed because the airline voluntarily waited for delayed-transfer passengers.
- **How:** When the airline cites an earlier-flight disruption, challenge the causal chain: was the airline's own operational decision the determining cause?
- **Citizen tip:** If the airline says "it was the previous flight's fault," ask whether THEY chose to wait. Their own decision can break the excuse and you may still be owed compensation.

---

## Fund 3 — EU-Reform der Fluggastrechte 2026 (noch nicht in Kraft)

- **Fund:** EU-Reform der Fluggastrechte — Rats-Schlussfreigabe am 13.07.2026 (vorläufige Einigung Rat/Parlament Juni 2026)
- **Was sich ändert:** U.a. (1) Airline muss nach Ankunft binnen 96 h elektronisch über Entschädigungsrechte informieren; (2) Antrag wird sofort bestätigt, Antwort (Zahlung oder begründete Ablehnung) binnen 30 Tagen; (3) Verbot des „No-Show“-Boardingerwerbs (denied boarding, weil Hinflug nicht angetreten); (4) Handgepäck im angezeigten Grundpreis standardmäßig inkludiert; (5) gestärkte Rechte für PRM (Personen mit eingeschränkter Mobilität), u.a. Sitzplatzgarantie kostenlos, Ersatz bei Verlust/Beschädigung von Mobilitätshilfen.
- **Bürgerwirkung:** Ab Inkrafttreten (voraussichtlich August 2027) deutlich einfachere und schnellere Rechtsdurchsetzung; „No-Show“-Klauseln und separat berechnetes Handgepäck werden rechtswidrig. Bis dahin gelten die alten Regeln.
- **Tool-Änderung (flight-rights-mcp & agb-reader-mcp):** flight-rights-mcp: Wissen zur künftigen No-Show-Regel + Handgepäck-Inklusion ergänzen (als „geplant, ab ~08/2027“). agb-reader-mcp: Klausel-Katalog — No-Show-Ausschlussklauseln sowie Handgepäck-Zusatzentgelt-Klauseln ab Inkrafttreten als unwirksam markieren (vorher als „geplant unwirksam“ kennzeichnen).
- **Effective:** Voraussichtlich August 2027 (noch nicht in Kraft).

**Quellen:**
- https://www.consilium.europa.eu/en/press/press-releases/2026/07/13/council-gives-final-clearance-for-stronger-air-passenger-rights/
- https://www.consilium.europa.eu/en/policies/consumer-protection-travel-rights/
- https://www.mondaq.com/aviation/1826102/strengthening-eu-air-passenger-rights-the-2026-reform-explained
- https://www.euronews.com/my-europe/2026/07/10/inside-the-eus-bittersweet-deal-to-update-air-passenger-rights

### EN
- **Headline:** 2026 EU air passenger-rights reform agreed — easier claims, no-show ban, hand baggage included (not yet in force)
- **What changed:** Council final clearance on 13 July 2026 (provisional agreement June 2026) introduces: (1) airline must electronically inform passengers of compensation rights within 96h of arrival; (2) acknowledge claims immediately and reply within 30 days (pay or justify); (3) ban on denying boarding for "no-show" (unused outbound); (4) hand baggage included by default in displayed fares; (5) strengthened rights for passengers with reduced mobility (free seating together, replacement of lost/damaged mobility equipment).
- **Why:** First overhaul of EU261 in 22 years — to simplify, harmonise and improve enforcement of passenger rights across all transport modes and better protect the most vulnerable.
- **Effective:** Expected August 2027 (not yet in force).
- **Deadline:** None for citizens yet; carriers must prepare.
- **Who's affected:** All EU air passengers once in force; especially no-show travellers and PRM.
- **How:** Once in force, cite the new regulation for no-show and hand-baggage disputes; until then, old rules apply.
- **Citizen tip:** From ~August 2027 your airline can no longer punish you for missing the outbound flight, and hand baggage must be in the headline price. Watch this space — the tools will flag these clauses as unlawful once the law applies.

---

## Fund 4 — Lufthansa-Warnstreik 12.02.2026: interne Streiks bleiben kein EC

- **Fund:** Lufthansa-Warnstreik am 12.02.2026 — massenhafte Annullierungen/Delays
- **Was sich ändert:** Bestätigt die gefestigte Rspr. (Krüsemann, C-195/17): Streiks des *eigenen* Personals sind KEIN außergewöhnlicher Umstand. Lufthansa ist voll entschädigungspflichtig (bis €600).
- **Bürgerwirkung:** Betroffene Passagiere haben Anspruch auf Ausgleich (€250 / €400 / €600 je nach Distanz) plus Betreuung (Art. 9). Die Airline darf die Forderung nicht mit „Streik“ ablehnen. Antragsfrist (DE): 3 Jahre.
- **Tool-Änderung (flight-rights-mcp):** Keine neue Logik nötig — bestehender Fall `kruesemann-c195-17` deckt es ab; ggf. Keyword-Ergänzung `["Lufthansa Streik 2026","warnstrike","warnings strike"]` zwecks besserer Auffindbarkeit.

**Quellen:**
- https://www.flight-delayed.com/en/news/2026/02/11/lufthansa-strike-feb-2026
- https://www.lufthansa.com/us/en/passenger-rights

### EN
- **Headline:** Lufthansa warning strike 12 Feb 2026 — internal strikes remain NOT an extraordinary circumstance
- **What changed:** Confirms settled case law (Krüsemann, C-195/17): strikes by the carrier's own staff are NOT an extraordinary circumstance. Lufthansa is fully liable for compensation up to €600.
- **Why:** Staff problems of the airline itself are its own business risk; only third-party strikes (e.g. ATC) count as extraordinary.
- **Effective:** 12 February 2026 (event); law unchanged.
- **Deadline:** Claim within 3 years (Germany).
- **Who's affected:** Lufthansa passengers cancelled/delayed >3h by the 12 Feb 2026 strike.
- **How:** File an EU261 claim; the airline cannot refuse on "strike" grounds.
- **Citizen tip:** If Lufthansa cancelled your flight due to its own staff strike, you are owed up to €600 — don't accept a voucher instead of cash.
