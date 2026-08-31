# EU Citizen-Rights Watch — 2026-08-31

Repo: `flight-rights-mcp` · Branch: `agent/eu-rights-watch-2026-08-31`
Querverweis: `agb-reader-mcp` (Klauselkatalog)
Funde: 3 (1 EuG-Urteil, 1 BGH-Urteil, 1 EU-Gesetzgebungsänderung)

---

## Fund 1 — EuG: Eigene Warteentscheidung der Airline unterbricht die Kausalkette (T-656/24)

- **Überschrift:** Wenn die Airline selbst entscheidet zu warten, kann sie sich später nicht auf „außergewöhnliche Umstände“ berufen.
- **Was sich ändert:** Das Gericht der EU (EuG) entschied im März 2026: Die autonome Entscheidung des ausführenden Luftfahrtunternehmens, auf Passagiere zu warten, die wegen Mängeln bei der Sicherheitskontrolle noch nicht durch die Kontrolle sind, kann den direkten Kausalzusammenhang zwischen diesem außergewöhnlichen Umstand und einer mindestens dreistündigen Ankunftsverspätung eines Folgeflugs unterbrechen. Das Gericht wies das Argument zurück, betriebliche und technische Störungen befreiten automatisch von der Ausgleichszahlung: Technische Probleme, die der normalen Tätigkeit einer Airline innewohnen, sind keine außergewöhnlichen Umstände. Nur Ereignisse wie schweres Wetter, politische Instabilität oder Sicherheitsrisiken können befreien — und nur, wenn die Airline alle zumutbaren Maßnahmen nachweist.
- **Warum:** Vorlage eines deutschen Gerichts; zwei Passagiere klagten nach über drei Stunden Verspätung. Die Airline berief sich auf Personalmangel an einem anderen Flughafen und die daraus folgende Umplanung der Flotte.
- **Gültig ab:** Urteil vom März 2026, wirkt als Auslegung von VO 261/2004 sofort — auch für laufende und Altfälle innerhalb der Verjährung.
- **Frist:** In Deutschland 3 Jahre Verjährung (Ende des 3. Jahres nach dem Flugjahr) — Tool `check_verjaehrung` bleibt unverändert korrekt.
- **Wer ist betroffen:** Passagiere mit Verspätung ab 3 Stunden, bei denen die Airline die Verspätung auf einen *vorherigen* Vorfall (Personalmangel, Sicherheitskontrolle, Umplanung eines anderen Flugs) schiebt.
- **Wie:** Ausgleich nach Art. 7 VO 261/2004 verlangen: 250 € bis 1.500 km, 400 € innereuropäisch bzw. 1.500–3.500 km, 600 € darüber. Beweislast liegt bei der Airline.
- **Bürgertipp:** Wenn die Airline „Verspätung wegen eines Vorflugs / Sicherheitskontrolle / Personalmangel“ schreibt: nachfragen, ob die Airline selbst entschieden hat zu warten oder umzuplanen. Ja = Anspruch bleibt bestehen.

**⚙️ Nötige Tool-Änderung (für den Maintainer):**
- Tool: `check_extraordinary_circumstances` (in `flight_rights_mcp/server.py`), Datenquelle `flight_rights_mcp/data/jurisprudence.json` → `cases[]`.
- Neuen Fall aufnehmen, z. B. `id: "eug-t656-24-kausalkette"`, `topic: "kausalkette_unterbrochen"`, Keywords: `personalmangel`, `staff shortage`, `sicherheitskontrolle`, `security check`, `umplanung`, `vorflug`, `rotation`, `knock-on delay`, `flottenumplanung`.
- `ruling`: eigene Warteentscheidung/Umplanung der Airline unterbricht die Kausalkette → kein Befreiungsgrund. `result_for_passenger`: Anspruch besteht.
- Zusätzlich: `likely_extraordinary` sollte bei Treffern auf „Personalmangel Dritter + eigene Umplanung“ auf `False` gesetzt werden, auch wenn ein anderer Fall (z. B. Wetter) mitmatcht.

**Quellen:**
- https://curia.europa.eu/site/upload/docs/application/pdf/2026-03/cp260026en.pdf
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62024TJ0656
- https://www.jurist.org/news/2026/03/eu-court-strengthens-compensation-rights-for-delayed-air-passengers/
- https://eur-lex.europa.eu/eli/reg/2004/261/oj/eng

### EN
- **Headline:** When the airline itself decides to wait, it cannot later hide behind "extraordinary circumstances".
- **What changed:** In March 2026 the General Court of the EU held that the autonomous decision of the operating air carrier to wait for passengers who have not yet cleared security, due to shortcomings in the security checks, is capable of breaking the direct causal link between that extraordinary circumstance and a delay of at least three hours in the arrival of a subsequent flight. The Court rejected the argument that operational and technical disruptions automatically exempt carriers from paying compensation: technical problems inherent in the normal exercise of an airline's activity are not extraordinary circumstances. Only events such as severe weather, political instability or security risks may justify an exemption — and only if the airline proves it took all reasonable measures.
- **Why:** Referral from a German court; two passengers sued after a delay of more than three hours. The airline invoked staff shortages at another airport and the resulting reorganisation of its aircraft schedule.
- **Effective:** Judgment of March 2026; as an interpretation of Regulation 261/2004 it applies immediately — including to pending and past cases still within the limitation period.
- **Deadline:** In Germany 3 years limitation (end of the 3rd year after the year of the flight) — the `check_verjaehrung` tool remains correct.
- **Who's affected:** Passengers with delays of 3 hours or more where the airline blames an *earlier* incident (staff shortage, security check, rescheduling of another flight).
- **How:** Claim compensation under Art. 7 of Regulation 261/2004: €250 up to 1,500 km, €400 intra-EU or 1,500–3,500 km, €600 beyond. The burden of proof lies with the airline.
- **Citizen tip:** If the airline writes "delay due to inbound flight / security check / staff shortage", ask whether the airline itself decided to wait or to reschedule. If yes, your claim stands.

---

## Fund 2 — EU261-Reform: Politische Einigung vom 15. Juni 2026, 3-Stunden-Schwelle bleibt

- **Überschrift:** Nach 13 Jahren Blockade steht die Reform der Fluggastrechte — die 3-Stunden-Grenze und die Beträge bleiben.
- **Was sich ändert:** Rat und Europäisches Parlament haben sich am 15. Juni 2026 auf die Revision der VO 261/2004 geeinigt. Ausgleich weiterhin bei Ankunft mehr als 3 Stunden verspätet oder Annullierung weniger als 14 Tage vor Abflug; Beträge bleiben im Wesentlichen: 250 € bis 1.500 km, 400 € innereuropäisch bzw. 1.500–3.500 km, 600 € für alle übrigen Flüge. Neu: Airlines müssen bei potenziell ausgleichspflichtiger Verspätung innerhalb von 96 Stunden nach Ankunft elektronisch informieren, Eingang einer Forderung sofort bestätigen und innerhalb von 30 Tagen zahlen oder begründet ablehnen. Betreuung: Erfrischungen alle 2 Stunden, Mahlzeit nach 3 Stunden und dann alle 5 Stunden (max. 3 pro Tag), Internetzugang und zwei Telefonanrufe, bei Übernachtung Hotel und Transfer kostenlos. Umbuchung muss innerhalb von 3 Stunden angeboten werden — sonst Selbstumbuchung mit Erstattung bis 400 % des Ticketpreises. „No-Show“-Regeln (Streichung des Rückflugs, weil der Hinflug nicht angetreten wurde) werden verboten; Handgepäckstück muss im Standardpreis ausgewiesen werden; verstärkte Rechte für Menschen mit Behinderung/eingeschränkter Mobilität, Kinder, unbegleitete Minderjährige und Schwangere. Außergewöhnliche Umstände werden über eine nicht abschließende Liste präzisiert; Beweislast bleibt bei der Airline, inklusive Nachweis aller zumutbaren Maßnahmen und des direkten Kausalzusammenhangs.
- **Warum:** Die Kommission hatte die Revision 2013 vorgeschlagen; Rechtsunsicherheit und wachsende Rechtsprechung machten eine Klarstellung nötig. Der frühere Ratsvorschlag (4/5/6 Stunden) wurde abgewendet.
- **Gültig ab:** Noch nicht in Kraft — die Einigung muss von Parlament und Rat nach der rechtssprachlichen Überarbeitung formell angenommen werden. Bis dahin gilt VO 261/2004 unverändert.
- **Frist:** Keine Bürgerfrist. Für die Praxis: Die Kommission prüft innerhalb von 3 Jahren eine Ausweitung des Anwendungsbereichs auf Drittstaats-Airlines.
- **Wer ist betroffen:** Flüge innerhalb der EU (EU- und Nicht-EU-Airlines), Flüge in die EU aus Drittstaaten mit EU-Airlines, Flüge aus der EU in Drittstaaten mit EU- und Nicht-EU-Airlines.
- **Wie:** Vorerst weiter nach geltender VO 261/2004 fordern. Nach Inkrafttreten gilt zusätzlich die 30-Tage-Antwortpflicht der Airline.
- **Bürgertipp:** Wer den Hinflug verfallen lässt, darf den Rückflug künftig nicht mehr verlieren — und wenn die Airline nach einer Annullierung nicht binnen 3 Stunden umbucht, selbst buchen und bis zu 400 % des Ticketpreises zurückverlangen.

**⚙️ Nötige Tool-Änderung (für den Maintainer):** noch keine Code-Änderung — nur vormerken. Nach formeller Annahme betrifft es `calculate_compensation` (Beträge/Schwellen prüfen), `check_eu261_applicability` (Anwendungsbereich, Drittstaats-Label) und `generate_claim_letter` (30-Tage-Antwortfrist + 96-Stunden-Informationspflicht zitieren). Für `agb-reader-mcp`: neue Klauselverbote „No-Show“ und „Handgepäck nicht im Preis ausgewiesen“ in den Katalog aufnehmen, sobald der Rechtstext veröffentlicht ist.

**Quellen:**
- https://www.consilium.europa.eu/en/press/press-releases/2026/06/15/council-and-parliament-reach-landmark-agreement-on-stronger-eu-air-passenger-rights/
- https://www.consilium.europa.eu/en/press/press-releases/2025/06/05/council-sets-position-on-clearer-and-improved-rules-for-air-passengers/
- https://cms.law/en/int/legal-updates/new-european-regulation-on-air-passenger-rights-what-impact-for-the-air-transport-sector

### EN
- **Headline:** After 13 years of deadlock the air passenger rights reform is agreed — the 3-hour threshold and the amounts stay.
- **What changed:** On 15 June 2026 the Council and the European Parliament agreed on the revision of Regulation 261/2004. Compensation still applies where a flight arrives more than 3 hours late or is cancelled less than 14 days before departure; amounts remain largely the same: €250 up to 1,500 km, €400 intra-EU or 1,500–3,500 km, €600 for all other flights. New: for a delay that could ground compensation, airlines must inform passengers electronically within 96 hours after arrival, immediately acknowledge receipt of a claim and, within 30 days, either pay or give a clear justification for refusing. Assistance: refreshments every 2 hours, a meal after 3 hours and every 5 hours thereafter (max. 3 per day), internet access and two phone calls, and for overnight stays free hotel and transfers. Rerouting must be offered within 3 hours — otherwise passengers may arrange their own and claim up to 400% of the original ticket price. "No-show" (denying boarding because the outbound flight was not taken) is prohibited; fares including one piece of hand baggage must be displayed by default; reinforced rights for persons with disabilities or reduced mobility, children, unaccompanied minors and pregnant passengers. Extraordinary circumstances are clarified through a non-exhaustive list; the burden of proof stays with the airline, including proof of all reasonable measures and of a direct causal link.
- **Why:** The Commission proposed the revision in 2013; legal ambiguity and evolving case law made clarification necessary. The earlier Council position (4/5/6 hours) was averted.
- **Effective:** Not yet in force — the agreement must still be formally adopted by Parliament and Council after legal-linguistic revision. Until then Regulation 261/2004 applies unchanged.
- **Deadline:** No citizen deadline. For the record: the Commission will assess within 3 years whether the scope can be extended to third-country operators.
- **Who's affected:** Flights within the EU (EU and non-EU airlines), flights into the EU from non-EU countries on EU airlines, and flights departing the EU to non-EU countries on EU and non-EU airlines.
- **How:** For now keep claiming under the current Regulation 261/2004. Once in force, the airline's 30-day reply obligation applies on top.
- **Citizen tip:** Skipping your outbound flight will no longer cost you the return — and if the airline fails to reroute you within 3 hours after a cancellation, book it yourself and claim back up to 400% of the ticket price.

---

## Fund 3 — BGH: Laufzeitbeginn erst bei „Freischaltung“ ist unwirksam (III ZR 8/25)

- **Überschrift:** Eine AGB-Klausel, die die 24-Monats-Bindung erst mit der Freischaltung starten lässt, ist unwirksam.
- **Was sich ändert:** Der BGH entschied am 08.01.2026 (III ZR 8/25): Eine AGB-Klausel in Verträgen über Glasfaseranschlüsse, die den Beginn der 24-monatigen Mindestvertragslaufzeit an die „Freischaltung“ des Anschlusses knüpft, ist unwirksam. Sie verstößt gegen § 309 Nr. 9 Buchst. a BGB, der Laufzeiten von mehr als zwei Jahren verbietet. Die relevante Laufzeit beginne bereits mit dem Vertragsschluss, weil der Kunde ab diesem Moment gebunden ist; rechnet man zu den 24 Monaten noch eine variable Wartezeit bis zur Freischaltung, wird die gesetzliche Höchstgrenze zwangsläufig überschritten. Das Argument, § 56 TKG rechtfertige zur Refinanzierung des Netzausbaus eine Ausnahme, wies der Senat zurück: Der Anbieter darf sein Investitionsrisiko bei verzögerten Anschlüssen nicht auf Verbraucher:innen abwälzen.
- **Warum:** Unterlassungsklage der Verbraucherzentrale NRW gegen einen Glasfaseranbieter. Das OLG Hamburg gab der Klage statt, die Revision des Anbieters zum BGH blieb erfolglos.
- **Gültig ab:** Urteil vom 08.01.2026, sofort wirksam.
- **Frist:** Keine Antragsfrist; unwirksame Klauseln entfalten von Anfang an keine Bindung. Rückforderungen von Zahlungen unterliegen der regulären 3-jährigen Verjährung.
- **Wer ist betroffen:** Verbraucher:innen mit Glasfaser- bzw. Telekommunikationsverträgen, deren Mindestlaufzeit erst ab Freischaltung/Bereitstellung zu laufen beginnen soll — und allgemein alle Verträge mit an ein späteres Ereignis gekoppeltem Laufzeitbeginn.
- **Wie:** Kündigung 24 Monate nach *Vertragsschluss* geltend machen, nicht ab Freischaltung; bei Weigerung auf BGH III ZR 8/25 und § 309 Nr. 9 Buchst. a BGB verweisen.
- **Bürgertipp:** Prüfe im Vertrag, ab welchem Datum die Laufzeit läuft. Steht dort „ab Freischaltung“ oder „ab Bereitstellung“, gilt trotzdem das Datum der Unterschrift.

**⚙️ Nötige Tool-Änderung (für den Maintainer):** betrifft `agb-reader-mcp` (nicht dieses Repo). Klauselkatalog erweitern: Kategorie „Laufzeitbeginn an späteres Ereignis gekoppelt“ (Keywords: `Freischaltung`, `Bereitstellung`, `Inbetriebnahme`, `Aktivierung`, `Laufzeit beginnt mit`), Rechtsgrundlage § 309 Nr. 9 Buchst. a BGB, Fundstelle BGH 08.01.2026 – III ZR 8/25, Bewertung: unwirksam.

**Quellen:**
- https://www.vzbv.de/urteile/zur-unwirksamkeit-einer-klausel-zur-laufzeitverlaengerung-durch-spaeten-anschlussbeginn

### EN
- **Headline:** A T&C clause starting the 24-month commitment only at "activation" is invalid.
- **What changed:** On 08.01.2026 the German Federal Court of Justice (BGH, III ZR 8/25) held that a standard-terms clause in fibre-optic connection contracts that ties the start of the 24-month minimum contract term to the "activation" of the connection is invalid. It breaches § 309 no. 9 lit. a BGB, which prohibits terms longer than two years. The relevant term already starts on conclusion of the contract, because the customer is bound from that moment; adding a variable waiting period until activation on top of the 24 months inevitably exceeds the statutory maximum. The Court rejected the argument that § 56 TKG justifies an exception to refinance network rollout: the provider may not shift its investment risk from delayed connections onto consumers.
- **Why:** Injunction action by Verbraucherzentrale NRW against a fibre-optic provider. The Higher Regional Court of Hamburg upheld the action; the provider's appeal to the BGH failed.
- **Effective:** Judgment of 08.01.2026, effective immediately.
- **Deadline:** No application deadline; invalid clauses never bind. Reclaiming payments is subject to the ordinary 3-year limitation period.
- **Who's affected:** Consumers with fibre-optic or telecoms contracts whose minimum term is supposed to start only on activation/provision — and generally any contract whose term start is tied to a later event.
- **How:** Assert termination 24 months after *conclusion of the contract*, not from activation; if refused, cite BGH III ZR 8/25 and § 309 no. 9 lit. a BGB.
- **Citizen tip:** Check from which date your contract term runs. If it says "from activation" or "from provision", the signature date counts instead.

---

*Erstellt automatisch vom EU Citizen-Rights Watch Agent. Kein Rechtsrat. Nicht selbst gemergt — menschliche Prüfung erforderlich.*
