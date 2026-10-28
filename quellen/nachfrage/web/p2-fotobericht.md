# P2 Fotobericht: web research (Handwerker photo report app, DE/AT/CH)

Date of research: 2026-10-28. Tools: WebSearch + WebFetch only. About 45 searches/fetches. Complete.

Method notes (read first):
- WebFetch passes pages through a small summarising model. Quotes marked "(fetch)" were returned by that model and not re-checked against raw HTML; treat as "high, not proven". Where the fetcher said it quoted only part of a long text, the quote is the opening fragment.
- `[search summary, unverified]` = taken only from a WebSearch result summary, not from a fetched page.
- No usernames. OMR gives relative dates only. App Store feed dates are exact (ISO).
- Apple's public iTunes search/reviews feed (itunes.apple.com/search, /rss/customerreviews) was used for App Store DE data.

---

## 1. Market size

| Fact | Quote / number | Source |
|---|---|---|
| Handwerksbetriebe DE (Handwerksrolle, 31.12.2025) | "Betriebsbestände Handwerk gesamt" 1,038,126 (-0.0 % yoy); search summary: 641,462 Anlage A, 286,223 B1, 110,224 B2 | https://www.zdh.de/daten-und-fakten/kennzahlen-des-handwerks/wirtschaftlicher-stellenwert-des-handwerks-2025/ (fetch; split A/B1/B2 `[search summary, unverified]`) |
| Beschäftigungsverhältnisse 2025 | 6,237 thousand "BV-Verhältnisse" (jobs, not persons; people with several jobs counted multiple times since 2024) | same (fetch) |
| Umsatz 2025 | 783 Mrd. EUR | same (fetch) |
| Destatis Handwerkszählung 2024 (Anlage A + B1 only) | "rund 564 000 Handwerksunternehmen in Deutschland", down 0.7 %; "rund 6,0 Millionen Personen im Handwerk tätig"; Umsatz 762 Mrd. EUR | https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/04/PD26_143_53211.html (fetch) |
| Small firms 2024 | "kleine Handwerksunternehmen mit weniger als fünf Beschäftigten einen deutlichen Umsatzrückgang von 15,1 %" | same (fetch) |
| Share of small firms (ZDH Handwerkszählung 2024 page) | "beschäftigen weniger als zehn tätige Personen, 56,6 Prozent sogar weniger als 5." Fetcher computed 78.0 % under 10 (not verbatim). "Nur 2,6 Prozent aller Unternehmen beschäftigen 50 und mehr Mitarbeiter." | https://www.zdh.de/ueber-uns/fachbereich-wirtschaft-energie-umwelt/statistik/handwerkszaehlung/handwerkszaehlung-2024/ (fetch) |
| Earlier size split (HWZ 2021, ZDH PDF) | 568,314 firms; 59.4 % under 5 employees, 20.7 % with 5-9 (so about 80 % under 10, my sum). The PDF URL returned 404 on direct fetch; figures from search summary only | https://www.zdh.de/fileadmin/Oeffentlich/Wirschaft_Energie_Umwelt/Themen/Daten_Fakten/Betriebe_Beschaeftigte_Umsaetze/Verteilung-BKL-2021.pdf `[search summary, unverified]` |
| Berlin 2024 example | <5 employees: 10,415 firms; 5-9: 3,479 firms | https://download.statistik-berlin-brandenburg.de/6dcf2766dd22104c/92c8c6d7e774/SB_E05-01-00_2024j01_BE.pdf `[search summary, unverified]` |
| Austria (WKO Gewerbe und Handwerk) | "304.049 aktiven Spartenmitgliedern" (27 Bundesinnungen, 31.12.2025); "251.598 Unternehmen von insgesamt 561.469" have main focus in Gewerbe und Handwerk; "57.575 von 153.782 Arbeitgeberunternehmen" (excl. geringfügig Beschäftigte). No small-firm share on page. WKO counts memberships, not firms. | https://www.wko.at/gewerbe-handwerk/kennzahlen (fetch) |
| Austria legal form (all chamber members) | Einzelunternehmen 439,265 active members (72.5 %) | https://www.wko.at/oe/statistik/jahrbuch/k15.pdf `[search summary, unverified]` |
| Switzerland | "fast 90 %" of Unternehmen have fewer than 10 Beschäftigte (all sectors; KMU-Studie 2024); 99.7 % are KMU. No Gewerbe/Handwerk count found. | https://www.kmu.admin.ch/dam/kmu/en/dokumente/Publications/KMUStudie_2024.pdf.download.pdf/KMUStudie_2024.pdf `[search summary, unverified]` |

Reading: about 1.04 m entries in the Handwerksrolle (incl. handwerksähnlich and zulassungsfrei), about 564k "Unternehmen" in the Destatis count (A + B1); ZDH says 78 % have fewer than 10 people, 56.6 % fewer than 5. So roughly 300k+ DE firms with under 5 people (my arithmetic: 0.566 x 564k = about 319k). AT: about 250-300k Gewerbe/Handwerk members, but many are dormant or one-person. CH: no trade-specific count.

Count: 11 rows.

---

## 2. Incumbents

Prices as shown on vendor pages when fetched (2026-10-28). Net unless stated.

| Product | Price tiers | Free tier | Photo report to customer standalone? | Cancellation | URL |
|---|---|---|---|---|---|
| Craftnote | Baustelle 14,90 EUR, Büro 29,90, Büro Plus 49,90 per user/month, billed annually, excl. VAT. Zeit-Modul 49,90, Fahrzeug 24,90/tracker. PDF-Formular-Paket "Ab 150,00 € / Paket"; custom PDF "Ab 30,00 € / Je PDF" | No; "kostenlose 30-tägigen Probephase" | No. Photos inside project chat/documentation. Büro: "Projektberichte erstellen und teilen" (needs Büro tier at 29,90). Baustelle: "Dokumentiere mit Fotos und digitalen Formularen" | "Der Vertrag über die Büro- und Baustellen-Pakete verlängert sich jeweils automatisch um ein Jahr." Three-month notice before end | https://www.craftnote.de/preise (fetch); https://omr.com/de/reviews/product/craftnote/pricing |
| CompanyCam (US) | Core 63, Crew 129, Scale 199 USD (per month, "Billed Annually"; unclear in fetch). Core: 1 user included, +29 USD each additional | No free plan on page; trial (length not stated) | Core: "Turn job photos into reports"; Crew: "Auto-generate job reports". PDF not named on page. Not DE-localised. | "Cancel anytime" (trial wording) | https://companycam.com/pricing (fetch). Third-party sources conflict on a free tier `[search summary, unverified]` |
| PlanRadar | Basic 26 EUR (max 1 user, 10 plans), Starter 89, Pro 129 per user/month (monthly billing); annual saves "mehr als 10%" | No; 30-day trial, no credit card | Photos attach to tickets on plans; basic report templates in all plans; custom template editor Pro+ | "unter Einhaltung einer einmonatigen Kündigungsfrist"; "keine Gutschrift für die restliche Vertragslaufzeit" | https://www.planradar.com/de/preise/ (fetch) |
| Docu Tools | "starten bei 54 € pro Nutzer und Monat (zzgl. MwSt.)"; Pocket/Combo/Multi; 10 % cheaper annual | No; 14-day trial, no credit card | Pocket: photos on pins; 360 photo add-on from 10 EUR/month | "Monatlich kündbar bei Auswahl der monatlichen Zahlungsweise." | https://www.docu-tools.com/de/preise (fetch) |
| Plancraft | Prices not on landing page (pricing page redirected). Meisterschüler free | 7-day trial, no credit card | Baudokumentation: Bautagesbericht, Regiebericht, Berichtsvorlagen, Abnahmeprotokolle (within full Handwerker suite) | "Jederzeit kündbar", "nur einem Tag" notice | http://plancraft.com/ (fetch) |
| Hero | Select 69 EUR net/user/month with 12-month term (heise); other tests: 59 EUR annual / 79 EUR monthly; OS 119 EUR | 14-day test access | Bautagebuch listed as function in suite; no standalone | not found | https://www.heise.de/download/specials/Handwerkersoftware-im-Vergleich-7206873 ; https://www.fuer-gruender.de/wissen/unternehmen-fuehren/buchhaltung/handwerker-software-vergleich/hero-test/ `[search summary, unverified]` |
| ToolTime | Solo 79 EUR/month (1 person), Team 149 (up to 5), Max 299 (up to 10); intro prices year one; DATEV add-on 19 | not stated | "ToolTime Echo" (voice+photo to work report) marked "Coming soon" at time of the source | not found | https://www.ki-syndikat.de/tools/tooltime/ `[search summary, unverified]` |
| Capmo | "Keine Listenpreise"; "in der Regel im mittleren vierstelligen Bereich" per year; no per-user cost | No, 14-day test | Photos pinned on plans; for larger projects | not found | https://www.ki-syndikat.de/baudokumentation-apps-vergleich/ (fetch) |
| Fieldwire (US) | Basic free (about 5 users, 3 projects, photos); Pro 29-39 USD/user/month annual (sources conflict). Reports/exports only in paid tiers | Yes (Basic) | Reports not in free tier | not found | https://www.capterra.com/p/142801/Fieldwire/pricing/ `[search summary, unverified]` |
| Dalux Field | "Field Basic kostenfrei" | Yes | Photo attached to location automatically | n/a | https://www.ki-syndikat.de/baudokumentation-apps-vergleich/ (fetch) |
| BauMaster | Smart 79, Expert 149 per user/month monthly billing; Expert 109 annual; Bautagesberichte +25 EUR/user | No, 30-day trial | Fotodokumentation in app; Abnahmeprotokolle VOB and ÖNORM | not stated | same (fetch) |
| KEVOX | Basic ab 83, Premium ab 168 per month | No | Photos as proof in report; Abnahme/Prüfdoku focus | not stated | same (fetch) |
| Baukraft | Starter 49,17/month 1 user; Team 107,50 for 3 | No, 7 days | Targets Generalunternehmer/Architekten | not stated | same (fetch) |
| Streit Bautagebuch+ | no prices; "Jetzt Preis ermitteln!"; add-on to Streit software only | n/a | Photos saved to customer/project; PDF not mentioned | not stated | https://www.streit-software.de/fotodokumentation-baustelle (fetch) |
| Onstruc (iOS, DE listing) | App "Kostenlos"; upgrade "Workspace Pro" (no price shown) | Yes | Yes: "detailed, customizable PDF reports"; v2.0.0 up to three signatures (fetch paraphrase). 4.7 stars from 24 ratings | not stated | https://apps.apple.com/de/app/onstruc/id1532766276 (fetch) |
| Pro Doku (iOS) | Free: 3 projects, 10 entries each. Premium listed Monthly 129 / Annual 999 / Lifetime 1,999 in the MX storefront (currency not confirmed, likely MXN) | Yes (limited) | Yes: photo + dictated notes, PDF export, "handovers". No rating yet | not stated | https://apps.apple.com/mx/app/pro-doku/id6754005836 (fetch) |
| Small new apps (App Store DE search, iTunes feed) | all price 0.00: Repolog (1 rating), FieldProof (1), Doclution (0), Bautagebuch DokuAI (18 ratings, 5.0), Dokum365 (5, 5.0), Modocu (0), Baustellenbericht Bautagebuch (0) | free to install | PDF/report apps by tiny publishers, almost no ratings | n/a | https://itunes.apple.com/search?term=fotodokumentation+bericht&country=de&entity=software&limit=15 (fetch, first 9 of 15 results read) |

App Store DE scale (iTunes search, fetch): Craftnote 4.42 from 1,891 ratings; HERO 4.44 from 2,861 ratings.

Observation: Everything with a real customer-facing report sits in 15-30 EUR per user per month (Craftnote Büro 29,90 needed for reports), with auto-renewal for a year at Craftnote. Cheap per-user starter tiers exist but are suites. Free small apps exist (Onstruc) but are barely rated.

Count: 17 rows (plus App Store scale line).

---

## 3. Complaints (verbatim)

Caveat: all quotes below passed through the WebFetch summariser (fetch); for long reviews it returned only the opening fragment, shown as given. No review found complains about a missing "simple photo report" as such; the complaints are about price, complexity, speed/sync, support and lock-in of suites. Trustpilot, Capterra, GetApp, trusted.de (403) and Google Play were not readable; OMR has few reviews for photo-documentation products (Craftnote 1, PlanRadar 0, Docu Tools 0).

### Craftnote, App Store DE (https://itunes.apple.com/de/rss/customerreviews/page=1/id=1327810465/sortby=mostrecent/json , page=2 same pattern). Overall 4.42 from 1,891 ratings (iTunes search). Dates are exact.
1. 3 stars, 2025-05-07, "Bilder": "Ab und an werden die Bilder nicht hochgeladen und neue Nachrichten werden mir auf dem Handy immer noch nicht angezeigt!" (fetch paraphrase: support no longer reachable)
2. 3 stars, 2025-07-19, "Vor der Übernahme deutlich besser!": "Wir nutzen Craftnote bereits seit mehreren Jahren. Wir sind ein Handwerksunternehmen mit circa 18 Mitarbeitern." (fetch paraphrase: service worse after takeover)
3. 1 star, 2025-01-14, "Neuer update": "Es ist viel langsamer geworden seit neue Update und das alte wochen plan tabele war schöner"
4. 3 stars, 2024-12-23, "Gut, leider immer noch iOS bugs": "Seit iOS 18 funktioniert das Teilen nicht mehr. Dateien müssen lokal zwischengespeichert werden."
5. 3 stars, 2024-11-04, "Ausbaufähig": "Leider läuft sie auf meinem iPad (10. Gen) nicht gut!" (fetch paraphrase: photos and new projects do not sync properly)
6. 3 stars, 2024-10-30, "Keine Verbesserung": "Leider alles ausgeblieben. Denken über einen Wechsel nach"
7. 1 star, 2024-01-19, "Sehr schlechter Support und Software Probleme": "Am Ende der Laufzeit hat man keinen Zugriff mehr auf die Daten wie Arbeitsstunden etc." (fetch paraphrase: export failed)
8. 3 stars, 2023-02-07, "Ladezeiten sind grauenhaft": "Das laden der Dateien dauert teilweise ewig."
9. 2 stars, 2022-12-05, "Bewertung": "Nach Software-Update, iOS und Craftnote, öffnet Programm auf Tablet nicht mehr."
10. 1 star, 2022-01-29, "Nicht zufrieden": "Es kommt öfters vor das Ausgefüllte Dokumente beim speichern ihre Inhalte verlieren."
11. 1 star, 2021-02-03, "Nicht glücklich": "ich finde es nicht gut das der gesamte Umfang der App nicht auf dem IPad funktioniert" (fetch paraphrase: logo insertion and PDF-template editing "too expensive")
12. 1 star, 2020-07-14, "Kein Offline Test möglich.": "dass eine Anmeldung und Internetverbindung notwendig sind."
13. 1 star, 2020-07-01, "Nervige Störung": "Es benötigt jedes Mal ewig bis man etwas geöffnet, gesendet oder bearbeitet hat."
14. 2 stars, 2020-06-29, "Öffnen von Projekten": "Es hängt öfters und benötigt viel Zeit bis es etwas öffnet"
15. 1 star, 2020-06-22, "Zu kompliziert": "Habe sie wieder gelöscht und in den Mails von craftnotes wird man immer geduzt ist unhöflich"
16. 1 star, 2020-04-28, "Kann meine Mitarbeiter nicht hinzufügen": "Leider konnte nur einer in unser Projekt beitreten"
17. 1 star, 2020-03-22, "Spam und Undurchsichtige Kosten": "Nicht empfehlenswert"
18. 3 stars, 2019-03-25, "Gute Idee aber langsam": "Die App ist leider recht langsam wenn man Fotos hochladen möchte. Die Performance der App ist noch Verbesserungswürdig."
19. 3 stars, 2019-08-10, "Man lernt....": "Ich habe mich anfangs schwer getan und tue es teilweise immer noch."
20. 2 stars, 2019-04-04, "Demoverstion.": "Demoversion habe ich erst gelesen wo ich es geöffnet habe. Nix ohne Registrierung."
21. 2 stars, 2018-10-26, "Test": "Hallo ,warum kann ich die App nicht testen ,finde ich weniger gut das ich mich erstmal anmelden muss ."
22. 3 stars, 2019-09-02, "Nette Idee": "Nette Idee. Aber wenn ich die Kunden anlege und in den Dokumenten … jedes Mal die Adresse eintragen" (fetch truncated with ellipsis)

### Plancraft, OMR Reviews (https://omr.com/de/reviews/product/plancraft/all). 4.7 from 12 reviews. Relative dates only; stars as shown.
23. 2,5 stars, in den letzten 12 Monaten: "Support Anfragen werden ignoriert. Preiserhöhung im übertriebenen Maße."
24. 5,0 stars, vor mehr als 12 Monaten: "Die monatlichen Kosten sind für uns als mittelständisches Unternehmen in Ordnung, aber für kleinere Betriebe..." (truncated by fetch)
25. 5,0 stars, in den letzten 12 Monaten: "Bisschen teuer, aber jeden Penny wert."
26. 5,0 stars, in den letzten 12 Monaten: "Im Augenblick die Skalierung von Bilder. Alles andere wird sich in Zukunft verbessern lassen."
27. 4,5 stars, in den letzten 12 Monaten: "Man muss immer einen Teil schließen um in einen anderen Teil zu gelangen."
28. 4,5 stars, vor mehr als 12 Monaten: "Durch viele neue Updates verändert sich das Layout ab und an und man muss sich neu zurecht finden."

### Hero, OMR Reviews (https://omr.com/de/reviews/product/hero-handwerkersoftware/all). 9 visible reviews (page rating 4.5). Relative dates only.
29. 4,5 stars, vor mehr als 12 Monaten: "Für Handwerksbetriebe die wenig Erfahrung mit digitalen Tools haben, könnte die Bedienung anfangs kompliziert wirken."
30. 5 stars, vor mehr als 12 Monaten: "Für kleinere Betriebe kann HERO anfangs etwas umfangreich erscheinen, da viele Funktionen integriert sind,"
31. 4 stars, vor mehr als 12 Monaten: "Jährliches Abos, monatliche wären besser."
32. 5 stars, vor mehr als 12 Monaten: "Das Programm bzw. die Software ist sehr umfangreich und ich benötige bei weitem nicht alle Funktionen, die geboten werden."
33. 4,5 stars, vor mehr als 12 Monaten: "Obwohl die App insgesamt gut funktioniert, könnte sie noch schneller sein."
34. 4,5 stars, vor mehr als 12 Monaten: "Rechnungen können bei kleinen Fehlern nicht einfach korrigiert werden, sondern müssen aufwendig storniert"
35. 5 stars, vor mehr als 12 Monaten: "Die Server sind manchmal etwas langsam, aber das ist verständlich, wenn so viele Leute das Programm gleichzeitig nutzen."

### Hero, reviewhero.io (https://www.reviewhero.io/hero-software-fuer-handwerker-goettinger-hof-9-hannover-913a). Fetcher saw 2 critical texts, star values not shown.
36. 11.08.2025: "Ich gehe zum Anwalt. Ich habe im Februar schon meine Firma abgemeldet und habe telefonisch wie schriftlich gekündigt." (continues: "Trotz Kündigung bekam ich einen Rechnung für das Jahr bis Juli 2026.")
37. 29.07.2025: "Ich bin sehr enttäuscht vom Umgang der HERO Software ." (text truncated on page)

### Craftnote, OMR (https://omr.com/de/reviews/product/craftnote/all). Only 1 review visible, 5,0 stars, in den letzten 30 Tagen, reviewer is an Elektro-Betrieb with 0-10 employees.
38. "Es könnten noch mehr Funktionen sein, das Angebots und Rechnungstool ist noch nicht zu ende gedacht."

### PlanRadar, Capterra DE / GetApp (English reviews, via search summary only) `[search summary, unverified]`, https://www.capterra.com.de/software/156698/PlanRadar
39. "The platform can feel a bit overwhelming at first because of the number of features and configuration options. It also takes some time to customize workflows, especially for new users."
40. "report generation feature is often broken" (fragment)
41. "Versioning control could be improved alongside some of the user interfaces / user experience when creating reports."

Pattern: (a) per-user suite pricing with annual auto-renewal and long notice (Craftnote 3 months; Hero cancellation dispute); (b) Hero and Craftnote reviewers themselves say suites feel "umfangreich" and "kompliziert" for small or digitally inexperienced firms; (c) photo upload/sync/speed and iPad/iOS bugs at Craftnote; (d) required sign-in and no offline test; (e) PDF-template editing and logo insertion sold separately at Craftnote (review 11, plus "PDF-Formular-Paket ab 150 EUR" on the pricing page). No review asks for "just photos to a PDF"; that gap is inferred from the pricing structure and the 4.7-star but 24-rating Onstruc.

Count: 41 quotes (about 28 with 3 stars or lower; the 37 App Store/OMR/reviewhero entries are fetch-passed text, 3-4 are search summaries).

---

## 4. Workarounds

| Item | Quote / fact | URL |
|---|---|---|
| Free Word and Excel Abnahmeprotokoll template (vendor lead magnet) | Streit offers "Jetzt kostenlose Excel-Vorlage herunterladen" and "Jetzt kostenlose Word-Vorlage herunterladen." Page says the signature starts the Gewährleistung and "Die Beweislast kehrt sich um. Mängelansprüche müssen von Ihrem Kunden belegt werden" (fetch) | https://www.streit-software.de/vorlagen/abnahmeprotokoll-fuer-handwerker |
| Baudokumentation templates + software push | Streit "Baudokumentation – Muster, Tipps & Software-Anbieter"; mentions free analogue Bautagebuch template `[search summary]` | https://www.streit-software.de/vorlagen/baudokumentation-muster |
| Formilo whitepapers (Abnahmeprotokoll, Arbeitsbericht, Wartungsprotokoll) | Compare PDF, Word, Excel and app solutions; Formilo sells interactive PDF forms (also resold inside Craftnote at "Ab 30,00 € / Je PDF") `[search summary]` | https://www.formilo.com/wp-content/uploads/2025/09/Formilo-Whitepaper-Abnahmeprotokoll.pdf |
| Official-body template | Finanztip points to a simple Abnahmeprotokoll from the Handwerkskammer Freiburg `[search summary, not checked]`; Deutsche Handwerks Zeitung has a Checkliste (Ort, Datum, Betrieb, Auftraggeber, Anwesende, Leistungsbeschreibung, Mängelfreiheit) `[search summary]` | https://www.deutsche-handwerks-zeitung.de/?p=357060 ; https://www.finanztip.de/daily/handwerker-da-vermeide-diese-10-fehler/ |
| Swiss authority PDF with photo placeholders | Canton Basel-Landschaft: "Die Bilder lassen sich direkt in vorgegebene Platzhalter einfügen" (Bauprofile photo-documentation form) `[search summary]` | https://www.baselland.ch/politik-und-behorden/direktionen/bau-und-umweltschutzdirektion/bauinspektorat/formulare-wegleitungen/fotodokumentation-von-bauprofilen |
| Phone gallery and daily folders | Forum advice (bau-forum, not a Handwerker post): daily folder with date and short description, use the smartphone, photograph "so oft und viel wie möglich" `[search summary]`; guide claims photos on private phones "gehen im Streitfall oft verloren, wenn sie keinem Auftrag zugeordnet sind" `[search summary]` | https://www.energiesparhaus.at/forum/65961 ; https://www.ki-syndikat.de/usecases/handwerk/08-qualitaetsdokumentation/ |
| Clipboard + Excel for defects | Practice report: Mängel documented "mittels Klemmbrett und Excel Tabelle", too little transparency `[search summary]` | https://www.docu-tools.com/wp-content/uploads/2025/07/Case-Study_theapro_Final.pdf |
| Forum thread, photo as evidence (bau.de, 15.02.2002, 3 replies) | "Machen Sie Bilder, auch wenn Sie die für sinnlos halten." / "gelten diese Bilder zwar nicht als Beweis, aber immerhin als Hinweis." / reply: "Immer schön dokumentieren, auch wenn es manchmal lästig erscheint." (fetch) | https://bau.de/forum/neubau/12094.php |
| Forum thread, Baumängel photos (bau.de, 2005 original; AI-generated additions dated 17.01.2026) | The AI-written block advises "Sichern Sie die Originaldateien der Fotos." and unchanged EXIF (Datum/Uhrzeit, Geräte-ID) (fetch). Not human advice, not legally reviewed. | https://bau.de/forum/handwerk/10182.php |
| WhatsApp use and its limits | Handwerksblatt/HwK Koblenz article "Handwerker: Vorsicht beim Umgang mit WhatsApp": phonebook sync is a data transfer between firms needing consent; trainer advice to clarify beforehand whether site photos may be sent via WhatsApp, to be noted in Angebot or Auftragsbestätigung `[search summary, unverified]`. A guide calls WhatsApp "der häufigste Praxis-Verstoß" (vendor view, `[search summary]`) | https://www.handwerksblatt.de/themen-specials/das-aktuelle-datenschutzrecht/handwerker-vorsicht-beim-umgang-mit-whatsapp |
| Free iOS photo-to-PDF apps already exist | Onstruc (free, PDF reports, up to three signatures, 4.7 from 24 ratings, fetch); iNeo Bautagebuch (free with in-app purchases, PDF by e-mail) `[search summary]`; projectdocu pro (free, server-based) `[search summary]`; InFoto Pro (labels photos with Ort, Datum, Gewerk; no PDF mentioned) `[search summary]` | https://apps.apple.com/de/app/onstruc/id1532766276 ; https://apps.apple.com/de/app/ineo-bautagebuch-bauberichte/id1072145917 ; https://apps.apple.com/lu/app/projectdocu-pro/id1523981086 ; https://apps.apple.com/bb/app/infoto-pro/id6471486067 |
| AI daily-report one-off | "Doku fix": web app for 17,00 EUR (one-off) with AI daily report, needs a free ChatGPT/Gemini/Claude account `[search summary]` | https://www.digistore24.com/product/738515 |

Not found: a forum thread where Handwerker themselves describe their WhatsApp-plus-gallery routine in their own words. Searches returned vendor guides and consumer-side building forums only.

Count: 12 rows.

---

## 5. Why it matters (rules and practice)

| Topic | Fact (verbatim where possible) | Source |
|---|---|---|
| Abnahme (BGB) | "Der Besteller ist verpflichtet, das vertragsmäßig hergestellte Werk abzunehmen" / "Wegen unwesentlicher Mängel kann die Abnahme nicht verweigert werden." (fetch) | https://www.gesetze-im-internet.de/bgb/__640.html |
| Fiktive Abnahme | A work counts as accepted if the Unternehmer set a reasonable deadline "und der Besteller die Abnahme nicht innerhalb dieser Frist" "unter Angabe mindestens eines Mangels verweigert hat". For a Verbraucher this works only if the Hinweis was given "in Textform" together with the request. (fetch) | same |
| Zustandsfeststellung | § 650g Abs. 1: "Die gemeinsame Zustandsfeststellung soll mit der Angabe des Tages der Anfertigung versehen werden" "und ist von beiden Vertragsparteien zu unterschreiben." Abs. 2: the Unternehmer may do it alone if the Besteller does not show up, must date and sign it and give the Besteller a copy. (fetch) | https://www.gesetze-im-internet.de/bgb/__650g.html |
| Vermutung offenkundiger Mängel | § 650g Abs. 3: if an obvious defect is not noted, "wird vermutet, dass dieser nach der Zustandsfeststellung entstanden" "und vom Besteller zu vertreten ist." (fetch). This is the legal hook for a dated, signed before/after photo report. | same |
| Verjährung BGB | § 634a Abs. 1: two years for production/maintenance/alteration of a thing; "in fünf Jahren bei einem Bauwerk"; start: "Die Verjährung beginnt in den Fällen des Absatzes 1 Nr. 1 und 2 mit der Abnahme." (fetch) | https://www.gesetze-im-internet.de/bgb/__634a.html |
| VOB/B | § 13 Abs. 4 Nr. 1: "Ist für Mängelansprüche keine Verjährungsfrist im Vertrag vereinbart, so beträgt sie für Bauwerke 4 Jahre," (fetch). § 12 Abs. 4 Nr. 1: "Eine förmliche Abnahme hat stattzufinden, wenn eine Vertragspartei es verlangt." / "Der Befund ist in gemeinsamer Verhandlung schriftlich niederzulegen." § 12 Abs. 5 Nr. 1: "gilt die Leistung als abgenommen mit Ablauf von 12 Werktagen" after written notice of completion (fetch) | https://dejure.org/gesetze/VOB-B/13 ; https://dejure.org/gesetze/VOB-B/12 |
| No form prescribed for photos | VOB/B prescribes no particular form of photo documentation; extent and intervals should be fixed in the contract (guide) `[search summary, unverified]` | https://truescreen.io/de/analysen/beweissicherung-baustelle-zustand-dokumentieren/ |
| Evidence burden in practice | "Mit der Zeit wird es immer schwieriger nachzuweisen, dass ein Handwerker fehlerhaft gearbeitet hat." (lawyer guide, advising customers to photograph) `[search summary]`; guide: who cannot prove what was done when "trägt das Beweisrisiko" `[search summary]` | https://anwalt-leverkusen.de/aktuelles/detail/wenn-der-maler-ihnen-den-teppich-versaut-wie-sie-erfolgreich-ihrem-handwerker-die-rechnung-praesentieren.html?pdf=18 |
| Hidden work | "verdeckte Arbeiten (Leitungen, Abdichtung, Dämmung) sind nach dem Schließen unbeweisbar – das Vorher-Foto ist Pflicht." (vendor guide) `[search summary]` | https://www.ki-syndikat.de/usecases/handwerk/08-qualitaetsdokumentation/ |
| Photo evidential value | One forum answer: photos are "nicht als Beweis, aber immerhin als Hinweis"; an AI-generated reply in the same thread says photos can serve as Augenscheinsbeweis in civil proceedings. Treat as unsettled forum opinion, not law. (fetch) | https://bau.de/forum/neubau/12094.php |
| Versicherung | An insurer leaflet advises instructing Handwerksbetriebe to document work steps and cause photographically (Schadenminderung) `[search summary]`; Berufshaftpflicht pages say nothing on photos | https://cdn.pantaenius.com/content/user_upload/Files/SACH/Branchen/Wohnungswirtschaft/Leaflets/SACH_Erste%20Schritte%20nach%20Schadeneintritt_Wohwi_DE_0818_01.pdf |
| Data protection | Sachaufnahmen free, Personenaufnahmen need consent (vendor guide); pre-agreeing photo sending in Angebot/Auftragsbestätigung is advised `[search summary]` | https://www.legiscope.com/blog/dsgvo-handwerk-betriebe.html |
| Austria / Switzerland | Not researched beyond the German rules. ÖNORM Abnahmeprotokolle are offered by BauMaster (ki-syndikat comparison). SIA 118 not checked. | https://www.ki-syndikat.de/baudokumentation-apps-vergleich/ |

Not legal advice. The legal hook that matters for a small tool is the dated, signed Zustandsfeststellung and the note of the Abnahme date, not photos as such; photo evidential value is contested in forums.

Count: 12 rows.

---

## 6. Channels (K7)

| Channel | Type | Visible size | URL | Fit for reach with 100 EUR |
|---|---|---|---|---|
| r/Handwerker (Reddit) | subreddit | "114k members" (GummySearch, fetch; another search summary said 101k), +42k in a year (+59.3 %). Top topics Heizung, Fenster, Wand, Altbau; flair "Bitte um Hilfe" 86 posts, Diskussion 4. Mostly private persons asking for help, not business owners. | https://gummysearch.com/r/Handwerker | Weak target group |
| Bitkom survey, social media in Handwerk (23.10.2025, 504 Handwerksunternehmen ab 1 Beschäftigten) | channel-use data | "lokale Communities wie Nebenan.de oder Nachbarschaft.net (65 Prozent)", "Facebook (57 Prozent)", "Instagram (38 Prozent)", "TikTok (7 Prozent)", "YouTube (6 Prozent)" (share of firms with presence, fetch). This is firms marketing to customers, not where they talk shop. | https://www.bitkom.org/Presse/Presseinformation/Haelfte-des-Handwerks-nutzt-Social-Media | Facebook and Instagram dominate firm presence |
| Deutsche Handwerks Zeitung (DHZ) | print + dhz.net + newsletter | "verkaufte Auflage von knapp 490.000 Exemplaren" (Holzmann press release, undated); "bis zu 617.000 Lesern" combined with handwerk magazin; newsletter size not found `[search summary]` | https://www.presseportal.de/pm/60718/4445175 ; https://www.deutsche-handwerks-zeitung.de/?p=161743 | Ads cost more than 100 EUR; editorial pitch possible |
| Handwerksblatt (HWK-regional pages) | news portal / Kammer newsletter | no counts found; carries regional HWK pages and a newsletter "die handwerkskammern in deutschland" | https://www.handwerksblatt.de/newsletter/die-handwerkskammern-in-deutschland | Needs press-style story |
| Handwerkskammern: Digitalisierungsberatung | Kammer advisers | Kammern advise firms on online marketing and often digitalisation, free or subsidised `[search summary]`; no counts | https://www.handwerksblatt.de/die-handwerkskammern-in-deutschland/hwk-munster/themen-specials/digitales-handwerk/handwerk-4-0-film-ab-youtube-marketing | Advisers can recommend tools; slow, partnership needed |
| Handwerkerforum Trier (association) | regional network | "130 Mitglieder" `[search summary]` | https://www.handwerksblatt.de/die-handwerkskammern-in-deutschland/hwk-trier/trierer-junghandwerk-trifft-mdb-patrick-schnieder | Tiny, local |
| Handwerkerforum Saarland (jung und innovativ) | regional network | no counts | https://www.handwerksblatt.de/die-handwerkskammern-in-deutschland/hwk-saarland/handwerkerforum-jung-und-innovativ | Local |
| Bob von Bosch (B2B tradespeople community) | Facebook group, old | "9,000 members in Germany after about nine months" (old article, undated in result) `[search summary]` | https://wuv.de/Archiv/Das-Profi-Forum-Bob-von-Bosch | Probably inactive; unknown |
| YouTube Handwerk creators | video | Example: electrician channel started Feb 2021, "Community wächst und wächst" (no number); one small Metallbau channel had 35 subscribers. No ranking or subscriber counts of big Handwerk channels found. | https://www.deutsche-handwerks-zeitung.de/?p=351833 | Collaboration with a mid-size creator is the unknown; needs manual search |
| Facebook groups, Instagram, TikTok creators | social | Search found no group or creator with a verifiable size | n/a | Needs manual search inside the platforms |
| Search intent (SEO) | Google | Vendors (Streit, Formilo, ki-syndikat, whk-style content sites) already rank for "Abnahmeprotokoll Vorlage", "Baudokumentation Muster", "Fotodokumentation App" | https://www.streit-software.de/vorlagen/abnahmeprotokoll-fuer-handwerker | Competitive but the template-to-tool funnel is proven by Streit's own free Word/Excel download |
| Software comparison sites | OMR Reviews, ki-syndikat, softwareabc24, heise, fuer-gruender | Listings exist for all suites; small apps (Onstruc etc.) not compared | https://www.ki-syndikat.de/baudokumentation-apps-vergleich/ | Listing is free; low traffic |

Count: 12 rows (2 with hard member/reach numbers beyond search summaries: r/Handwerker, Bitkom).

---

## 7. Summary

1. Market: 1.04 m Handwerksrolle entries in DE (ZDH, end 2025), about 564k Unternehmen in the Destatis 2024 count; ZDH says 78.0 % have under 10 people and 56.6 % under 5, so roughly 300k firms with under 5 people (my arithmetic). AT: about 304k active Gewerbe/Handwerk members (WKO, memberships not firms). CH: about 90 % of all firms under 10 staff, no trade count.
2. Incumbents are suites: Craftnote 14,90-49,90 EUR per user per month, annual auto-renewal and three-month notice; Hero from about 59-69 EUR; ToolTime 79 EUR; PlanRadar Basic 26 EUR for 1 user; Docu Tools from 54 EUR; CompanyCam 63 USD; Plancraft prices not shown. A customer-facing project report at Craftnote needs the Büro tier (29,90 EUR) and PDF templates cost extra.
3. Free or near-free photo-to-PDF apps exist (Onstruc, iNeo, projectdocu pro; Fieldwire Basic and Dalux Field Basic free), but all are thinly rated (Onstruc 24 ratings) and none targets the Abnahme-for-Kleinbetrieb job in German with a company letterhead.
4. Complaints are about suite weight and price ("für kleinere Betriebe ... umfangreich", "kompliziert wirken"), sync and speed of photos, support, annual lock-in, and PDF templates sold separately. Nobody explicitly asks for photos-to-PDF only; that is an inference.
5. Workarounds: phone gallery, WhatsApp (with data-protection caveats), Word/Excel Abnahmeprotokoll from vendors such as Streit (free download as lead magnet). Photo evidential value is contested in forums; the solid legal hook is the dated, signed Zustandsfeststellung (§ 650g BGB) and the Abnahme date that starts Verjährung (§ 634a BGB; VOB/B § 13: 4 years default for Bauwerke).
6. Room for a one-job tool: yes, in the gap below 15 EUR per user, with no contract lock-in. Realistic price: free tier (1-3 reports per month), then 5-9 EUR per month or about 49-79 EUR per year flat per company, monthly cancellable. This is my inference, no willingness-to-pay survey was found.
7. Most reachable channel for 100 EUR and no following: search intent. A free Abnahmeprotokoll / Fotobericht template page in Word and PDF that converts to the app, as Streit already does for its suite. Second: helpful answers in building forums. Social paid reach is expensive; Facebook (57 %) and Instagram (38 %) are where firms are, but no group with verifiable size was found. Kammer advisers are free but slow.
8. Main risk: a free tier or cheap bundle is one feature away (Onstruc is free with PDF and signatures; Craftnote Baustelle is 14,90 EUR; Dalux Field Basic and Fieldwire Basic are free), and small tradespeople may keep using WhatsApp because it costs nothing and is already installed. A second risk is that sending customer photos requires consent and data-protection handling.
9. Unverified: Google Play data, Trustpilot/Capterra/trusted.de complaints, German YouTube/Instagram creator reach, AT/CH tradesperson counts beyond WKO, Plancraft pricing, Hero primary-source price, the HWZ 2024 size-class table itself (only ZDH percentages on the summary page).

Counts per section: 1 market 11 rows; 2 incumbents 17 rows (about 20 products incl. App Store small apps); 3 complaints 41 quotes (about 28 with 3 stars or lower; 3 from search summary); 4 workarounds 12 rows; 5 rules 12 rows; 6 channels 12 rows; 7 summary 9 lines.
