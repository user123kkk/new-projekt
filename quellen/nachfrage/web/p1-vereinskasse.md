# P1 Vereinskasse: web research (Kassenwart tool, DE/AT/CH)

Date of research: 2026-10-28. Tools: WebSearch + WebFetch only (about 40 searches).

Method notes (read first):
- German quotes are copied from fetched pages. WebFetch passes pages through a small summarising model, so short quoted fragments were returned by that model; they were NOT re-checked against the raw HTML, except the PDFs (ZiviZ, DOSB, LSB Hessen), which I extracted locally. Treat quote exactness as "high, not proven".
- Where a claim only comes from a WebSearch result summary (not from a fetched page), it is marked `[search summary, unverified]`.
- No usernames. OMR shows only relative dates ("In den letzten 6 Monaten"), not exact dates.
- Not reachable from here: trusted.de (403), Capterra (403), mikrocontroller.net (403), vereinsguru.de and clubdesk help (connection refused / 404), vereinsmeier.de (DNS failure), Google Play app pages (404). No Trustpilot page for any of the products exists in results. No Reddit/Facebook/YouTube content surfaced through search.

---

## 1. Market size

| Fact | Quote (verbatim) | Source |
|---|---|---|
| Registered Vereine DE, March 2026 | "628.992 Vereine waren im März 2026 im Vereinsregister eingetragen." | ZiviZ Discussion Paper Sept 2026, https://www.ziviz.de/sites/ziv/files/2026-09/vereinssterben_oder_neue_gruendungsdynamik.pdf |
| New registrations 2024 | "erreichte im Jahr 2024 mit 13.534 Neugründungen den höchsten Wert seit knapp zehn Jahren" | same |
| Net growth 2024 | "Im Jahr 2024 betrug das Netto-Wachstum 4.370 Vereine." | same |
| Sports clubs DE | "So können die rund 86.000 Sportvereine im Land derzeit rund 29,3 Millionen Mitgliedschaften aufweisen." (Stichtag 1.1.2025) | DOSB press release via https://www.basketball-bund.de/wp-content/uploads/sites/2/2025/11/2025_11_11_PM-Bestandserhebung-2025_Mitgliederrekord.pdf |
| Sports clubs avg size (my arithmetic) | 29.3 m memberships / 86,000 clubs is about 340 memberships per club (memberships, not persons; mean, skewed by big clubs) | derived |
| Size split, nationwide, all civil-society orgs (not only e.V.) | Chart in Berlin Länderbericht: "Bundesweit" 63 % klein (bis 100 Mitglieder), 24 % mittelgroß (101 bis 300), 13 % groß (mehr als 300) | ZiviZ-Survey 2023, Berlin, https://www.ziviz.de/sites/ziv/files/ziviz-survey_2023_laenderbericht_berlin.pdf (numbers read from the chart text "63 24 13 Bundesweit") |
| Berlin | "68 Prozent der Organisationen in Berlin haben bis zu 100 Mitglieder" | same |
| Sport clubs are bigger | "Nach wie vor hat mehr als jeder zweite Sportverein (58 Prozent) mehr als 100 Mitglieder." (2017 survey) | ZiviZ-Survey 2017, https://www.ziviz.de/download/file/fid/276 |
| Rhineland-Palatinate 2017 | "Die meisten Vereine sind kleine Vereine mit bis zu 100 Mitgliedern." | https://ziviz.de/download/file/fid/597 |
| Austria | "Alle Vereine werden im Zentralen Vereinsregister (ZVR) beim Bundesministerium für Inneres geführt." No count on the page. Older figure `[search summary, unverified]`: about 100,000 Vereine (BMI magazine 2006, https://www.bmi.gv.at/magazinfiles/2006/01_02/files/zentralesvereinsregister.pdf) | https://www.oesterreich.gv.at/themen/reisen_und_freizeit/vereine/Seite.220200.html |
| Switzerland | No count of Vereine found. `[search summary, unverified]`: about 858,000 volunteers in clubs/organisations (Swiss Olympic factsheet 2022); "three quarters of the population belong to a club" (Marchanzeiger). | https://marchanzeiger.ch/2023/07/05/ein-grosses-engagement-abseits-des-rampenlichts |

Reading: about 629k registered Vereine in DE; roughly 60-65 % of civil-society organisations have 100 members or fewer. For e.V. only, the bottom of the market is therefore roughly 350-400k clubs with up to 100 members (my estimate; the 63 % is for all orgs, and Vereine make up the large majority). Sports clubs are larger. AT/CH counts not found in primary sources.

Count: 12 rows.

---

## 2. Incumbents

Prices as shown on vendor pages when fetched (2026-10-28). Net/gross as stated.

| Product | Price tiers | Free tier | Fee tracking / bank import / reminders | Cancellation | URL |
|---|---|---|---|---|---|
| easyVerein | Small "19,38 € / Monat" bis 100 Mitglieder; Medium "30,69 € / Monat" bis 250; Large "41,99 € / Monat" bis 500; individuell "mehr als 3000". Annual billing "Jährlich (-15%)". Package names: Office "ab15,30€", Professional "ab19,38€" per Monat | No: Demo "0,00€", "zeitlich unbegrenzt kostenlos getestet", limited data | Page lists "Buchhaltung", "Finanzverwaltung", "Datenimport- und Export"; page does NOT name SEPA, Mahnung, CSV/Excel-Import, Bankanbindung | "Kündigungsfrist beträgt dabei immer 14 Tage zum Laufzeitende." | https://easyverein.com/vereinsverwaltungssoftware/preise/ |
| ClubDesk | Free "EUR 0" (50 Mitglieder, 100 MB); S "EUR 120" pro Jahr (100 Mitglieder); M "EUR 192" (250); L "EUR 336" (500); XL "EUR 396". "Preise inkl. MwSt., Abrechnung jährlich." | Yes, 50 members, "eingeschränkt" | SEPA direct debit for Mitgliederbeiträge; imports "Kontoauszüge in den Formaten camt.053 und CSV" and camt.054 / ESR (CH); Mahnung not mentioned on page | not stated | https://www.clubdesk.de/preise |
| Vereinsplaner | Free "€0,00"; PRO "jährliches Abo 149€"; PREMIUM "jährliches Abo 239€"; ULTIMATE "jährliches Abo 599€". Unlimited members; Free has "bis 5" accounts | Yes, "Dauerhaft kostenlos" | Beitragsklassen monatlich..jährlich; "SEPA Datenträgergenerierung" from PRO; bank connection from PREMIUM ("1 Bankverbindung"); finance import via Excel only in higher tiers; no Mahnfunktion on page | none stated; "Die Abos werden jährlich im Voraus abgerechnet." | https://www.vereinsplaner.de/preise |
| WISO MeinVerein Web | XS bis 100: three unlabelled figures "11,00 / 7,70 € / 13,00 €"; S bis 250 "22,00"; M bis 500 "40,00"; L unbegrenzt "60,00". "Alle Preise sind netto zzgl. USt." Offer is B2B only ("richtet sich nur an Unternehmer (§ 14 BGB)") | No: "14 Tage kostenlos testen" (a third party claims a free tier up to about 15 members, conflicts) | "Spenden- & Beitragswesen", "Banking & Kasse", "Rechnungen & Lastschriften"; Mahnung not on page. (Search summary: desktop version has Mahnungen) | "Keine automatische Verlängerung" | https://www.meinverein.de/preise/ |
| campai | "30 € bis 100 Mitglieder, danach 8 € je weitere 50. Über 1.000: individuelles Angebot." | No: 14-day trial | "Beiträge & Spenden", "Überweisung/Lastschrift"; Mahnung/Import not on page | "ein Monat Vertragslaufzeit mit monatlicher Verlängerung, ohne Frist kündbar" | https://www.campai.com/de/preise |
| Vereinsguru | XS "7,00 €/ Monat" bis 50 Mitglieder; S "14,00" bis 100; M "22,00" bis 250; L "39,00" bis 500; XL "59,00" unbegrenzt | No: "Kostenlose Testversion (14 Tage)" | "SEPA-Lastschriften", "Spenden- & Beitragswesen"; SoftGuide lists "Automatische Zahlungserkennung für Beiträge, Lastschriften, Rücklastschriften und Auslagen", "Import von Bankauszügen", "Excel-Import", "Mahnwesen" | not stated | https://omr.com/de/reviews/product/vereinsguru/pricing and https://www.softguide.de/programm/vereinsguru |
| Netxp-Verein | `[search summary, unverified]` about 7.50 EUR/month (<250 members) plus one-off setup 99 EUR; "Testen Sie uns einen Monat kostenlos und unverbindlich". Own page: "Beitragseinzug, Online-Banking, Buchhaltung"; "feste oder altersabhängige Beiträge" | No (1 month trial) | no SEPA/Mahnung/CSV wording on home page | not stated | https://www.netxp-verein.de ; https://trusted.de/netxp-verein-kosten |
| S-Verein / SPG-Verein | S-Verein starts 6.90 EUR/month per price table (no free tier). SPG-Verein: no pricing found. | No | not checked | not stated | https://www.softwareabc24.de/verein-software/preise-uebersicht |
| JVerein / openJVerein | open source, free; named in "Genannte kostenlose Tools" list | Yes | not checked | n/a | https://selbststaendigkeit.de/buchhaltung-fuer-gruender/vereinssoftware-kostenlos/ |
| Others from price table (starting prices) | Sportmember 0.00 EUR (free basic), KURABU 0.00 yearly, Collmex Verein 9.95/month, VereinOnline.org 1.00/month, Sewobe 29.90/month, MTH Vereins-Manager 60.00/year, Unsere Vereinssoftware 12.50/month | mixed | n/a | n/a | https://www.softwareabc24.de/verein-software/preise-uebersicht (page says data partly from vendors, no guarantee) |

Observation: cheapest paid entry for a 100-member club is about 84-120 EUR/year (Vereinsguru S 14 EUR/month = 168/yr; ClubDesk S 120/yr; Vereinsplaner PRO 149/yr; campai 30 EUR/month = 360/yr; easyVerein Small 19,38/month = 233/yr). Free tiers: ClubDesk (50 members), Vereinsplaner (5 accounts), Sportmember, JVerein.

Bank-side competitor: Sparkasse/VR banks ship club accounts and tools (e.g. "Vereinsmeister", "Mitgliederverwaltung und Beitragsbuchung für Vereine" PDF from a Raiffeisenbank, link 404 on fetch) `[search summary]`.

Count: 10 rows (about 22 named products incl. price table).

---

## 3. Complaints (verbatim)

Source for all OMR rows: OMR Reviews, relative dates only. Stars as shown. Most OMR ratings are 4.0-5.0; the critical text sits in the "Was gefällt dir nicht?" field. Real 1-2 star reviews are rare on OMR.

### WISO MeinVerein Web (https://omr.com/de/reviews/product/wiso-meinverein-web/all , /all/2 , /all/3)
1. 0,5 stars, vor mehr als 12 Monaten: "Das Programm wird nun aber zum dreifachen Preis verkauf und hat noch nicht mal die Hälfte der LEistungen"
2. 0,5 stars, in den letzten 12 Monaten: "Zusätzlich hilft der Support nur eingeschränkt weiter"
3. 2,5 stars, vor mehr als 12 Monaten: "An erster Stelle muss ich wirklich sagen, dass ich den Preis für schon mehr als sportlich halte."
4. 3,0 stars, vor mehr als 12 Monaten: "Die Preisgestaltung ist durchaus eher im höheren Segment"
5. 3,5 stars, in den letzten 6 Monaten: "Die mobile App überzeugt uns bislang nicht."
6. 4,0 stars, vor mehr als 12 Monaten: "Außerdem gab es in der Vergangenheit schon einige schleichende Preiserhöhungen."
7. 4,0 stars, vor mehr als 12 Monaten: "Leider ist die Software nicht ganz billig."
8. 4,0 stars, vor mehr als 12 Monaten: "Es erfordert eine gewisse Einarbeitungszeit, sich mit der Benutzeroberfläche vertraut zu machen."
9. 4,5 stars, in den letzten 6 Monaten: "Fehlgeschlagene SEPA-(Sammel)Lastschriften können nicht einfach als ungebucht gekennzeichnet werden."
10. 4,5 stars, in den letzten 6 Monaten: "Kosten sind etwas zu hoch"
11. 4,5 stars, in den letzten 12 Monaten: "Der Preis ist recht hoch für einen kleinen Förderverein."
12. 4,5 stars, in den letzten 12 Monaten: "Die Beitagsabrechnung mit den Rückbuchung sollte vereinfacht werden."
13. 4,5 stars, vor mehr als 12 Monaten: "Wie haben den Beitragseinzug noch nicht verstanden"
14. 4,5 stars, vor mehr als 12 Monaten: "Neben dem Excel-Import wäre die Anbindung weiterer Schnittstellen wünschenswert."
15. 4,5 stars, vor mehr als 12 Monaten: "Es fehlen noch Importmöglichkeiten von Excelsheets für freie Listen."
16. 4,5 stars, in den letzten 6 Monaten: "Die Vorarbeiten sind aufwendig"
17. 4,5 stars, in den letzten 6 Monaten: "Wenn man noch nicht viel mit Computern/Software gearbeitet hat, muss man sich natürlich etwas reinarbeiten"
18. 5,0 stars, in den letzten 3 Monaten: "Dass die Abrechnung der Beiträge immer buchhalterisch im Vormonat erfasst werden müssen"
19. 5,0 stars, in den letzten 6 Monaten: "Die Erstellung von Belegen und die Verbuchung ist nicht intuitiv"
20. 5,0 stars, vor mehr als 12 Monaten: "Die Benutzeroberfläche ist nicht besonders intuitiv."
21. 5,0 stars, vor mehr als 12 Monaten: "Das Programm ist verschachtelt, und manchmal bin ich auf der Suche nach den Möglichkeiten."
22. 5,0 stars, in den letzten 6 Monaten: "Das anmelden in der APP war für viele Mitglieder schwierig."

### Vereinsplaner (https://omr.com/de/reviews/product/vereinsplaner/all)
23. 5,0 stars, vor mehr als 12 Monaten: "Die Finanzverwaltung ist leider noch ausgereift genug." (sic)
24. 4,5 stars, vor mehr als 12 Monaten: "Die Finanzverwaltung könnte noch etwas ausgebaut werden."
25. 4,5 stars, vor mehr als 12 Monaten: "Manche Funktionen wie die Finanzverwaltung ist doch noch etwas in den Kinderschuhen."
26. 5,0 stars, in den letzten 6 Monaten: "wären für kleinere Vereine mit begrenztem Budget noch flexiblere Modelle oder zusätzliche Einstiegsmöglichkeiten"
27. 5,0 stars, vor mehr als 12 Monaten (Excel migration): "ich bei der Migration von Excel etwas gebraucht habe (Vorbereitung der Daten und nicht die Schuld vom Tool)"

### ClubDesk (https://omr.com/de/reviews/product/clubdesk/all)
28. 3,0 stars, in den letzten 6 Monaten: "Keine Flexibilität bei Vorauszahlung"
29. 3,0 stars, in den letzten 6 Monaten: "Im Basispaket nur 250 Adressen"
30. 5,0 stars, in den letzten 6 Monaten: "für Laien etwas kompliziert bis man alles eingestellt und eingerichtet hat."
31. 5,0 stars, in den letzten 6 Monaten: "Zu Beginn fand ich die Seite sehr kompliziert."
32. 4,5 stars, in den letzten 3 Monaten: "Es ist nicht alles ganz intuitiv, aber mit lesen und mit den Hilfen kommt man weiter."

### easyVerein (https://www.omr.com/de/reviews/product/easyverein ; 3 reviews only, rating 4,5)
33. 4,0 stars, vor mehr als 12 Monaten: "Die komplizierte Einstellung der Abrechnungsintervalle kann zu Frustration führen"
34. 4,0 stars, same review: "Die unklare logische Verortung von Features führt zu einer ineffizienten Nutzung"

### Vereinsguru (https://omr.com/de/reviews/product/vereinsguru/all)
35. 5,0 stars, in den letzten 12 Monaten: "Man muss sich am Anfang erst etwas reinfinden, vor allem bei den ganzen Einstellungen für Beiträge."

### campai (https://omr.com/de/reviews/product/campai/all; all 6 visible reviews 4,5-5,0)
36. 5,0 stars, in den letzten 30 Tagen: "Manchmal ist es schwierig von den Möglichkeiten nicht erschlagen zu werden."
37. 5,0 stars, in den letzten 30 Tagen: "Da campai viele Funktionen und Einstellungsmöglichkeiten bietet, braucht man am Anfang etwas Zeit"

### Apple App Store DE, easyVerein app (https://apps.apple.com/de/app/easyverein-vereinsverwaltung/id1582761507)
Overall shown as 3.4 of 5 from 46 ratings (a web search snippet said 3,5 / 41; the page itself says 3.4 / 46). Star ratings per review not shown by fetcher.
38. 12.07.2024, title "Aktuell nicht zu gebrauchen": "Hier muss dringend ein Update her."
39. 06.11.2023, title "Profilbild Update funktioniert nicht": "Leider funktioniert das Hochladen eines neuen Profilbildes bei mir gar nicht."

### Not fetchable (indirect)
- trusted.de aggregates easyVerein at 3.7 from 97 ratings; its own 3 reviews average 2.3. Complaints named in the search summary (not verified): online-banking import not working, weak support, refused cancellation, complicated interface. `[search summary, unverified]` https://trusted.de/easyverein-bewertung

Pattern: complaints concentrate on (a) price relative to a tiny club ("Förderverein", "kleinen Vereine mit begrenztem Budget"), (b) setup/learning effort for ehrenamtliche users, (c) Beitragsabrechnung/Rücklastschrift handling, (d) finance module maturity, (e) Excel import gaps. None of the reviews is by a user who wanted only "who has not paid".

Count: 39 quotes (8 with 3.5 stars or lower).

---

## 4. Workarounds

| Item | Quote / fact | URL |
|---|---|---|
| Free Excel template as lead magnet | File "Vereinsverwaltung_Excel_Vorlage.xlsx" covering Mitgliederdaten, Beitragszahlungen, Kassenbuch. Site text: "Excel ist auf fast jedem Computer vorinstalliert und erfordert keine monatlichen Abo-Kosten." and "Für Vorstände und Kassenwarte bietet es maximale Flexibilität." Limits: "Sobald der Verein wächst, mehrere Personen gleichzeitig auf die Daten zugreifen müssen" | https://www.whk-controlling.de/wissen/vereinssoftware-kostenlos-excel |
| Templates by same publisher (rank high in search for this query) | Kassenbericht-Vorlage, Vereinskassenbuch, Jahresabschluss Excel-Vorlage 2026 | https://www.whk-controlling.de/wissen/vereinskassenbuch-richtig-fuehren , https://www.whk-controlling.de/wissen/kassenbericht-verein-vorlage |
| Excel pain | "Am häufigsten liegt die Mitgliederliste als Excel-Datei auf mehreren privaten Rechnern." / "Niemand weiß, welche Fassung aktuell ist, und Änderungen gehen verloren." / "Mahnungen einzeln geschrieben, Rücklastschriften später entdeckt." / "Zahlungen werden einzeln abgeglichen, Mahnungen und Rücklastschriften kosten Zeit." | https://www.drweb.de/vereinssoftware-vergleich/ |
| Excel as accepted default | "Ja, grundsätzlich dürfen Vereine Mitgliederdaten in Excel führen, wenn die Daten angemessen geschützt sind." | same |
| Swiss free Excel Kassabuch | Vereinsbuchhaltung.ch offers a free Excel cash book (CHF) `[search summary]` | https://www.drweb.de/vereinssoftware-vergleich/ |
| Bank CSV matching by hand | Forum advice (mikrocontroller.net, thread "Buchungen einzelnen Personen zuweisen mit Excel"; page 403 on fetch, so text only via search summary): "Falls in der Mitgliederliste (Stammdaten) die Kontonummer hinterlegt ist, und diese auch in der csv-Datei (im gleichem Format) steht, dann die csv-Datei als 2.Blatt einlesen, und die Zuordnung mittels SVERWEIS vornehmen." `[search summary, unverified]` | https://www.mikrocontroller.net/topic/453693 |
| Forum: newcomer Kassenwart (administrator.de, 01.11.2011, 6438 views) | "Hallo, ich soll demnächst die Buchhaltung für unseren kleinen Gemeinützige Verein übernehmen." / "Ich wurde gern das mit Excel machen aber ich habe keine Ahnung wie das geht." Reply: "Oder such nach einer fertigen Vereinsverwaltung, da sind die alle Konten, Masken und Berichte schon fertig vorhanden" | https://administrator.de/forum/excel-datein-175614.html |
| JuraForum, 19.06.2026 (512 views, 3 replies) | "Wie kann ein kleiner e.V. Mitgliedsbeiträge von nicht zahlenden Mitgliedern einfordern." / "Und das Mitglied wurde bereits mehrfach auf seine Zahlungspflicht hingewiesen und meldet sich jetzt nicht mehr." Reply: "Unjuristisch: Hausbesuch durch den (trinkfesten) Vorstand." | https://www.juraforum.de/forum/t/mitgliedsbeitraege-einfordern.760569/ |
| JuraForum, 24.12.2025 (791 views, 5 replies) | "Trotzdem gibt es immer wieder Mitglieder, die das nicht wollen und auf einer Rechnung bestehen." Reply: "Zu einer bestimmten Zahlungsweise kann der Verein die Mitglieder aber nur per Satzung verpflichten." | https://www.juraforum.de/forum/t/vereins-beitraege-per-rechnung-und-per-lastschrift.758462/ |
| JuraForum, 02.12.2025 (434 views) | "Ein Vorstandsmitglied kümmert sich um das Mahnwesen." (thread about a deceased treasurer's Mahnverfahren paper box; shows single-person risk) | https://www.juraforum.de/forum/t/mahnverfahren-mahnbescheide-im-verein.758120/ |
| Tool vendors steering away from Excel | "Wer Mitgliederdaten, Beiträge und Termine noch per Excel verwaltet, verliert wertvolle Zeit." | https://selbststaendigkeit.de/buchhaltung-fuer-gruender/vereinssoftware-kostenlos/ |
| Free-tier ceilings | ClubDesk: "Die Gratisversion unterstützt bis zu 50 Mitglieder und 100 MB Speicher." Vereinsplaner Free: "bis zu 15 aktiven Mitgliedern und 5 Gruppen" (3rd-party claim; vendor page says "bis 5" accounts) | same |
| Open-source | JVerein / openJVerein | same |

Prominence: whk-controlling (a Controlling/Unternehmensberatung site) ranks repeatedly for Excel/Kassenbuch queries, i.e. the free-template space is occupied by a vendor-neutral content site, not by a tool.

No Google Sheets template for "Beitrag bezahlt" surfaced; search found only generic membership forms.

Count: 12 rows.

---

## 5. Channels (K7)

| Channel | Type | Visible size | URL | Fit for reach |
|---|---|---|---|---|
| JuraForum Vereinsrecht | public forum, anonymous Q&A | "1 von 119" listing pages; threads 350-800 views, 2-11 replies; posts dated 2025/2026 | https://www.juraforum.de/forum/f/vereinsrecht/ | Real treasurer questions on Beiträge, Mahnung, Lastschrift; link posts are possible but moderated; legal framing |
| Vereinsknowhow | static portal / forum label | "Das Forum für Vereine und andere Nonprofit-Organisationen"; no counts; frameset page, forum not reachable by fetch | https://www.vereinsknowhow.de | unknown |
| Vereinsbesteuerung.info | forum site | maintenance page on fetch: "Diese Seite befindet sich derzeit in Wartung." | https://www.vereinsbesteuerung.info | not usable now |
| Deutsches Ehrenamt (Benedetto monthly e-magazine, Online-Ratgeber) | content + newsletter | no counts: "Kostenfreie Fachinformationen in unserem Online-Ratgeber und unserem monatlich erscheinenden Vereinsmagazin Benedetto" | https://www.deutsches-ehrenamt.de | insurance-funded; sponsoring possible |
| VB VereinsBrief (IWW) | paid newsletter/magazine | no counts; "Die wichtigsten Neuigkeiten im Vereinsrecht, Vereinssteuerrecht, Satzungsrecht und Vereinsmanagement"; paid sub 18,30 EUR/month `[search summary]` | https://www.iww.de/vb/newsletter-anmeldung/57 | publisher-controlled |
| Verbandsbüro | advice blog | article "Mitgliedsbeitrag nicht gezahlt: Tipps" dated 29.08.2025, 503 views | https://www.verbandsbuero.de/mitgliedsbeitrag-nicht-gezahlt-tipps/ | SEO target; shows demand for "nicht gezahlt" content |
| Landessportbünde education portals | course catalogues | e.g. LSB Sachsen course "Digitale Vereins- und Mitgliederverwaltung (Online)" 8 LE; LSB Niedersachsen Vereinsmanagement seminars 250,00 EUR (2022 flyer) | https://bildungsportal.sport-fuer-sachsen.de/ , https://bildungsportal.lsb-niedersachsen.de/ | requires partnership; slow |
| VIBSS (LSB NRW) | state service for club boards | free info/advice/training `[search summary]` | not fetched | partnership |
| Vereinsforen (in person) | local events: WTB Vereinsforum 2025, Heidelberger Vereinsforum, Landkreis Vereinsforum | no counts | https://www.heidelberg.de/HD/Leben/heidelberger+vereinsforum.html | local, free to attend |
| Swiss: vitamin B Fachstelle für Vereine | FAQ/Vereinswissen | FAQ page exists; no counts | https://www.vitaminb.ch/vereinswissen/faq/ | CH niche |
| Facebook groups, YouTube channels, Reddit | not found | searches returned no group/channel/subreddit with a verifiable size | n/a | unknown, needs manual search inside the platforms |

Count: 11 rows (2 verified with counts: JuraForum threads, Verbandsbüro views).

---

## 6. Rules

| Topic | Fact (verbatim where possible) | Source |
|---|---|---|
| SEPA pre-notification | "mindestens 14 Tage vor der Fälligkeit zugesandt werden" (unless another period agreed). Content: collection date, creditor ID, exact amount, mandate reference. | https://gocardless.com/de/handbuch/sepa/vorabankuendigungen |
| Recurring same amount | "kann eine Vorabinformation auch mehrere Lastschriften ankündigen" and "reicht eine einmalige Unterrichtung des Zahlungspflichtigen vor dem ersten Lastschrifteinzug" | same |
| Creditor ID | needed by the club as originator; Bundesbank application `[search summary]` | https://www.vrbank-mkb.de/... SEPA_Informationen_fuer_Vereine.pdf (moved to regionalbank.de, empty on download) |
| Payment method binding | "Zu einer bestimmten Zahlungsweise kann der Verein die Mitglieder aber nur per Satzung verpflichten." / "Ein Beschluss der Mitgliederversammlung oder die Beitragsordnung reichen nicht." (forum quote citing IWW) | https://www.juraforum.de/forum/t/vereins-beitraege-per-rechnung-und-per-lastschrift.758462/ |
| DSGVO: DPO threshold | "Der Verein muss einen Datenschutzbeauftragten benennen, wenn sich mindestens 20 Personen ständig mit der Verarbeitung personenbezogener Daten beschäftigen." | LSB Hessen, https://www.landessportbund-hessen.de/fileadmin/media/Vereinsmanagement/Datenschutz/Erste_Hilfe_DS-GVO.pdf |
| DSGVO: Art. 30 register | "Nach Art. 30 DSGVO ist der Verantwortliche verpflichtet, ein Verzeichnis von Verarbeitungstätigkeiten zu führen." Exemption does not apply to a club that "seine Mitgliederverwaltung auf dem Laufenden hält" | same |
| DSGVO: legal basis | Art. 6 Abs. 1 lit. b (membership as contract) covers data needed for administration `[search summary, unverified]` | https://nexvyra.de/fakten/dsgvo-vereinsrecht |
| Excel allowed | "Ja, grundsätzlich dürfen Vereine Mitgliederdaten in Excel führen, wenn die Daten angemessen geschützt sind." | https://www.drweb.de/vereinssoftware-vergleich/ |
| Dunning: legal | § 286 Abs. 1 BGB: "Leistet der Schuldner auf eine Mahnung des Gläubigers nicht, die nach dem Eintritt der Fälligkeit erfolgt, so kommt er durch die Mahnung in Verzug." Abs. 2 Nr. 1: Mahnung entbehrlich wenn "für die Leistung eine Zeit nach dem Kalender bestimmt ist". Abs. 3: Verzug "spätestens", wenn nicht "innerhalb von 30 Tagen nach Fälligkeit und Zugang einer Rechnung oder gleichwertigen Zahlungsaufstellung" geleistet wird; for Verbraucher only if the Rechnung pointed to this. | https://www.gesetze-im-internet.de/bgb/__286.html |
| Dunning: club practice | "Der Verein muss eine Frist setzen und den Rückstand verbindlich mahnen, bevor die Mitgliedschaft endet." / "Sobald ein Mitglied mit der Zahlung in Verzug gerät, folgt die erste freundliche Erinnerung." | https://www.verbandsbuero.de/mitgliedsbeitrag-nicht-gezahlt-tipps/ |
| Exclusion | "Nicht jede verspätete Zahlung rechtfertigt jedoch sofort den Ausschluss." | https://kanzlei-herfurtner.de/vereinsbeitrag-nicht-geleistet/ |
| Fee order | "Häufig ist die Mitgliederversammlung für die Beitragsordnung zuständig." | same |
| Bylaw example | "Ein Mitglied kann durch Beschluss des Vorstands von der Mitgliederliste gestrichen werden, wenn es trotz Mahnung mit der Bezahlung seines Mitgliederbeitrages länger als drei Monate im Rückstand ist." (single club's bylaw, not law) | surfaced via search; one of the club rule PDFs, URL not individually confirmed |

There is no statutory requirement that a Verein send a Mahnung as such; whether one is needed for Verzug depends on whether the due date is fixed by calendar (§ 286 II Nr. 1) and on the Satzung/Beitragsordnung for removal. Not legal advice.

Count: 12 rows.

---

## 7. Summary

1. Market is large: 628,992 registered Vereine in DE (March 2026); about 63 % of civil-society organisations have 100 members or fewer; sports clubs are larger (about 340 memberships per club on average). AT/CH counts not found.
2. Incumbents cluster at 7-60 EUR/month for 100-250 members; ClubDesk offers a free tier to 50 members, Vereinsplaner a free tier with 5 accounts. Entry cost for a 100-member club is roughly 120-360 EUR/year.
3. Feature coverage is broad (SEPA, bank import, Beitragsabrechnung). Mahnung/Zahlungserinnerung is often not named on pricing pages. Vereinsguru lists Mahnwesen and Zahlungserkennung.
4. Complaints are about price for very small clubs, setup effort for volunteers, Rücklastschrift/Abrechnung handling and immature finance modules. Nobody in the reviews asks for a "who has not paid" view alone, but the "everything-suite" shape is the repeated friction.
5. The workaround is Excel plus bank CSV plus SVERWEIS; the template space is held by content sites (whk-controlling), not by tools. Treasurer questions on JuraForum are about collecting unpaid fees and Lastschrift vs Rechnung.
6. Room exists for a one-job tool only for clubs below about 100 members that find even 120-170 EUR/year plus setup too much. A realistic price is 0 for a small free tier, then 3-6 EUR/month or 29-59 EUR/year flat, below ClubDesk S and Vereinsguru S. This is my inference, not a surveyed willingness to pay.
7. Risk: ClubDesk Free (50 members, SEPA, camt/CSV import) already covers the smallest segment for 0 EUR; a new tool must beat it on speed of first result (import two files, see unpaid list in minutes) and on reminder wording.
8. Rules are light: DSGVO needs a Verarbeitungsverzeichnis and a DPO only at 20+ people; SEPA needs a 14-day pre-notification and a creditor ID; a reminder is not a legal precondition when the due date is fixed by calendar.
9. Most reachable channel with 100 EUR and no following: search-intent content (SEO page/template for "Mitgliedsbeiträge Excel Vorlage" and "Mitgliedsbeitrag nicht gezahlt Mahnung Muster") plus helpful answers in JuraForum Vereinsrecht threads. These topics already draw 400-800 views per thread and 500 views per advice article. Landessportbund seminars and Facebook/YouTube could not be sized from here.
10. Unverified: Facebook groups, YouTube, Reddit, Capterra/Trustpilot, AT/CH market size.

Counts per section: 1 market 12 rows; 2 incumbents 10 rows (about 22 products); 3 complaints 39 quotes; 4 workarounds 12 rows; 5 channels 11 rows; 6 rules 12 rows; 7 summary 10 lines.
