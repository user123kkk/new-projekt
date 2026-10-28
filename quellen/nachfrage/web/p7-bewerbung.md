# P7 Bewerbung: web research (Lebenslauf + Anschreiben for a specific job ad, DACH)

Date of research: 2026-10-28. Tools: WebSearch + WebFetch only. About 45 searches/fetches. Complete. Reddit (www and old) is blocked for WebFetch; r/arbeitsleben was read via the public Arctic Shift archive API (works for r/arbeitsleben, flaky for r/de; r/Bewerbung has no user threads).

Method notes:
- WebFetch passes pages through a small summarising model. "(fetch)" = returned by that model, not re-checked against raw HTML. `[search summary, unverified]` = taken only from a WebSearch result summary.
- Some official PDFs (BA Monatsbericht) returned 403. The Jobcenter Köln PDF was read locally with pdftotext (primary text).
- No usernames.

---

## 1. Market

| Fact | Quote / number | Source |
|---|---|---|
| DE unemployed, Sept 2026 | "Arbeitslosenzahl im September: -67.000 auf 2.994.000"; Quote 6,4 %; Unterbeschäftigung 3.615.000; gemeldete Stellen "660.000" | https://www.arbeitsagentur.de/presse/2026-37-arbeitsmarkt-im-september-2026 (fetch) |
| DE unemployed July 2026 | "Mit Beginn der Sommerpause ist die Arbeitslosigkeit im Juli 2026 um 71.000 auf 3.007.000 gestiegen." | same press series `[search summary, unverified]` |
| DE Arbeitsuchende (Bestand) | Not on press page; Monatsbericht PDF returned 403. Not found. | https://statistik.arbeitsagentur.de/Statistikdaten/Detail/202609/arbeitsmarktberichte/monatsbericht-monatsbericht/monatsbericht-d-0-202609-pdf.pdf (403) |
| DE job turnover | IW: turnover of socially insured employees "roughly 25 to 30 percent a year" (2011 release, old); 15-24 year olds change job about every 2 years, 50+ about every 6 years | https://www.presseportal.de/download/document/5979d2ef450000836c760779-pm43arbeitskra ftefluktuation.pdf `[search summary, unverified]` (URL as returned, contains a space) |
| DE graduates | "Im Prüfungsjahr 2025 haben rund 527.600 Studierende und Promovierende einen Abschluss an einer deutschen Hochschule erworben." (+3 %); Bachelor +4 % (10.400), Master (ohne Lehramt) 150.800 | https://www.forschung-und-lehre.de/lehre/hochschulabschluesse-2025-um-3-prozent-gestiegen-7935 `[search summary, unverified]` |
| DE Ausbildung starters | BIBB: 475.950 neue duale Ausbildungsverträge 2025 (-2,1 %, -10.300) | https://www.bibb.de/de/pressemitteilung_215396.php `[search summary, unverified]` |
| AT unemployed July 2026 | 298.885 arbeitslos, +8.917 yoy; about 364.000 incl. Schulung; Quote 6,9 % | https://orf.at/stories/3438038/ ; AMS https://www.ams.at/content/dam/download/arbeitsmarktdaten/%C3%B6sterreich/berichte-auswertungen/001_uebersicht_0726.pdf `[search summary, unverified]` |
| CH Sept 2026 | 140'480 Arbeitslose, Quote 3,0 %; Stellensuchende Aug 2026: 227'248 (4,8 %) | https://www.seco.admin.ch/de/newnsb/OfSdV0mM5gUa `[search summary, unverified]` |

Reading: about 3.0 m registered unemployed (stock), but stock is not the buyer pool: monthly inflows, employed changers (turnover 25-30 % of jobs per IW, old), 0.53 m graduates and 0.48 m new apprentices per year add up to several million Bewerbungen-writers per year. No official "job changers per year" figure found.

---

## 2. Can they pay: Vermittlungsbudget (§ 44 SGB III)

- Legal basis: § 44 SGB III, discretionary ("Ermessensleistung"); no legal entitlement (arbeitslosenselbsthilfe.org, fetch).
- Jobcenter Köln Arbeitshilfe (state 31.07.2023), primary text read via pdftotext, section 2.1 Bewerbungsbemühungen: "Pauschale Erstattung i. H. v. 5,00 € pro Bewerbung" ; "Grundsätzlich keine Kostenübernahme für Online-Bewerbungen." ; "Ausnahme: Kostenübernahme für Erstellung von Bewerbungen/Bewerbungsunterlagen im Internetcafé soweit nachgewiesen (Rechnung/Quittung) und keine Möglichkeit der Nutzung eines privaten PC/PC in JobBörse o. ä." ; "Kosten für (digitale) Bewerbungsfotos können - soweit angemessen und nachgewiesen (Rechnung) - grundsätzlich übernommen werden." ; "Die Bewerbung muss zielgerichtet/passgenau erfolgen und erfolgversprechend sein." https://www.jobcenterkoeln.de/wp-content/uploads/2023/08/AH-EW-II-16-III-44-Vermittlungsbudget_ID_9914_ab_31.07.23_bfrei.pdf
- arbeitslosenselbsthilfe.org (fetch): "pauschal meistens ein Betrag von 5 Euro pro schriftlicher Bewerbung"; "Für eine Online-Bewerbung erhalten Arbeitslose jeweils 20 Cent."; "Höchstbetrag von 260 Euro pro Jahr"; "wird im Vorfeld beantragt"; "Eine Genehmigung im Nachhinein ist nicht möglich." Software/paid application services not listed. https://www.arbeitslosenselbsthilfe.org/bewerbungs
- SG Nürnberg 29.01.2021 S 22 AL 207/20 `[search summary, unverified]`: 5 € flat per online application "nicht mehr zeitgemäß"; refusing above 250 € with uncapped Eingliederungsvereinbarung was Ermessensfehler. https://www.gesetze-bayern.de/Content/Rtf/Y-300-Z-BECKRS-B-2021-N-786?all=False
- Conclusion: amounts local and tiny (0.20-5 EUR per application); no source says a paid software subscription or AI service is reimbursed. Only possible case: Erstellung im Internetcafé with receipt. Treat as NOT a payer.

---


## 3. Competitors in DACH

Prices as shown when fetched 2026-10-28 unless marked.

| Product | Price model | Free tier | Tailoring to job ad | Source |
|---|---|---|---|---|
| lebenslauf.de | "1 Monat 16,99 € inkl. MwSt.", "3 Monate für 29,70 € inkl. MwSt.", "6 Monate für 41,40 € inkl. MwSt."; page says "Einmalzahlung", "Kein Abo" | Editor free; watermark-free download is Premium | Anschreiben templates, text helper "SmartWrite"; no job-ad paste on the page | https://www.lebenslauf.de (fetch) |
| lebenslauf.com | Prices not on page; footer has "Premium", "ProJobs", "Mitgliedschaft kündigen" | "Jetzt kostenlos gestalten" | Yes: "Lass die KI blitzschnell Dein Anschreiben verfassen." (details + job description) | https://www.lebenslauf.com (fetch) |
| bewerbung.net | 403 on fetch, not read | - | - | https://www.bewerbung.net |
| BewerbungGPT | 1 Anschreiben free without account; free account 3 more/month, PDF watermark; one-time pack 7,99 EUR for 5 letters, 12 months, no renewal; Premium 12,99/month or 79,99/year, "Premium verlängert sich automatisch" | Yes | Yes: profile or PDF CV plus job ad as text or link; marketing "keine Fakten erfunden", terms call letters "Vorschläge" | https://www.ki-syndikat.de/tools/bewerbunggpt/ (fetch of a review page, not the vendor) |
| ResuFit | Pro "€14.90 /Monat", "€34.90 /Quartal"; "Neukunden: 2,99 € für die ersten 7 Tage"; renewal terms not stated on page | Free: profile, tailored-document preview, resume checker; PDF export is Pro | Yes: job link in, tailored CV + Anschreiben out; "~90 Sek. pro maßgeschneiderter Bewerbung" | https://resufit.com/de/ (fetch). Also publishes the comparison blog posts cited below, so those are competitor-authored |
| JACVault | "Core 39 € im Monat für drei Bewerbungen", Professional 69 € (15), Power 119 € (30); first full application free; "cancellable anytime" per page | 1 application | Per page, per-application tailoring | https://jacvault.de/ (via drweb.de, which is a paid placement) |
| Zety | Giga: "14-tägigen Zugang für 2,70 Euro oder einen Jahreszugang für 69,99 Euro"; "sich der 14-tägige Zugang automatisch um 4 Wochen verlängert"; "23,70 Euro pro Monat" until cancelled | Free cannot export a usable CV (resufit, competitor) | not checked | https://www.giga.de/artikel/zety-lebenslauf-online-erstellen-achtung-kosten/ (fetch) |
| Resume.io | "7-Tage-Test" 2,95 $; "Verlängert sich automatisch auf 29,95 $ alle 4 Wochen"; quarterly 49,95 $ | "1 Lebenslauf, 1 Anschreiben, nur TXT-Download" | "Manuell" (competitor-authored) | https://resufit.com/de/blog/resumeio-test-preise-vorlagen-lohnt-es-sich/ (fetch) |
| Kickresume | Pro $39 monthly, $23/month quarterly, $16.50/month half-yearly (vendor comparison page); students 6 months Premium | Yes, limited | Job ad can be pasted (Trustpilot reviewer); AI Writer English-only per reviewers | https://www.kickresume.com/de/hilfecenter/kickresume-vs-enhancv/ `[search summary, unverified]` |
| MyPerfectResume | 14-day trial 2.95 $, then 23.95 $ per 4 weeks; free plan txt only | txt only | - | https://resufit.com/de/blog/myperfectresume-bewertung-kosten-leistungen-und-preis-leistungs-verhaeltnis/ `[search summary, unverified]` |
| cvmaker.de | 2,95 EUR, then after 7 days a subscription at 14,95 EUR/month (Mimikama, via search summary; page itself 403) | - | - | https://www.mimikama.org/?p=239587 `[search summary, unverified]` |
| Cvneed | Verbraucherzentrale: bills of 30 EUR/month people say they never agreed to | - | - | https://www.verbraucherzentrale.de/wissen/vertraege-reklamation/abzocke/cvneed-achtung-abofalle-106793 (fetch) |
| Enhancv | free Anschreiben generator, no account (upload CV, paste job ad) | Yes | Yes | https://enhancv.com/de/anschreiben-generator/ `[search summary, unverified]` |
| KiBewerben, iweaver | price not found | - | paste job ad | https://www.iweaver.ai/de/agents/ai-cover-letter-generator/ `[search summary, unverified]` |
| Europass, Reactive Resume, Canva, Microsoft Create | Europass: "Das kostenlose Angebot der Europäischen Union"; Reactive Resume free open source; Canva/Microsoft price not on page | Yes | No | https://www.drweb.de/lebenslauf-erstellen-vergleich/ (fetch) |
| ChatGPT | free tier as substitute; guides say paste job ad plus personal data | Yes | Yes | https://www.leinetal24.de/leben/karriere/bewerbungen-mit-chatgpt-ki-lebenslauf-anschreiben-schreiben-das-sollte-man-dabei-beachten-zr-92234069.html `[search summary, unverified]` |
| Novorésumé | only 5 DE Trustpilot reviews; Canva, Novorésumé prices not read | - | - | https://de.trustpilot.com/review/novoresume.com (fetch) |
| App Store DE apps | all free to install: "Lebenslauf, Anschreiben mit KI" 4.55 from 33 ratings; "Lebenslauf : Bewerbungs app" 3.87 from 566; "Lebenslauf erstellen: CV-Maker" 4.45 from 707; "Bewerbung Schreiben Schnell" 3.5 from 2, premium subscription auto-renewing (description) | free install | several with AI Anschreiben | https://itunes.apple.com/search?term=lebenslauf+anschreiben&country=de&entity=software&limit=15 (fetch, first 9 of 15) |

Reading: three price models. (a) Cheap trial (1,95-2,99) then 15-35 per month or 4 weeks, auto-renewing: Zety, Resume.io, MyPerfectResume, cvmaker, probably lebenslauf.com. (b) Fixed-term pass without renewal: lebenslauf.de (16,99 for 1 month). (c) Per-letter pack: BewerbungGPT 7,99 for 5 letters. So an honest one-time price already exists; the combination "free preview + job-ad paste + full CV and Anschreiben + no renewal" is only partly covered (BewerbungGPT: letters; ResuFit: has job-URL tailoring but subscription).

Count: 18 rows.

---

## 4. Complaints (verbatim)

Trustpilot DE quotes passed through the WebFetch summariser "(fetch)". Dates as shown on page. No usernames.

### Zety, https://de.trustpilot.com/review/zety.com (fetch)
1. 1 star, 2026-10-09: "wenn man nicht kündigt, kriegt man die teure Version."
2. 1 star, 2026-10-03: "Kündigen unmöglich, email ist nicht erreichbar und Button funktioniert nicht."
3. 3 stars, 2026-07-20: "Alles ist Super nur der Preis,es sollte nicht mehr als 5€ Monat kosten,sonst würde ich 5 Sterne geben"
4. 1 star, 2026-06-16: "Das Abo habe ich somit umsonst abgeschlossen und gezahlt."
5. 5 stars, 2026-10-07 (positive): "Schnell, einfach und günstig. Abo jederzeit kündbar."
6. Giga: "Im Kleingedruckten steht, dass sich der 14-tägige Zugang automatisch um 4 Wochen verlängert." https://www.giga.de/artikel/zety-lebenslauf-online-erstellen-achtung-kosten/ (fetch)

### Resume.io, https://de.trustpilot.com/review/resume.io (fetch)
7. 1 star, 2026-10-06: "Komplett intransparentes Abo-Modell: Nach Abschluss eines siebentägigen Trials gerät man automatisch in ein 25-Euro-Abo"
8. 1 star, 2026-09-05: "man tappt extrem schnell in eine kostenpflichtige Abo-Falle, da die Preise nicht transparent kommuniziert werden."
9. 1 star, 2025-11-14: "Kassieren monatliche Gebühren ohne, dass jemals ein Abo gebucht wurde."
10. 1 star, 2025-06-19: "Trotzdem wurden mir vier Monate lang 14,99 € abgebucht – ohne Rechnungen oder Hinweise per Mail."
11. 1 star, 2025-03-12: "Am Ende denkt man, das war erfolgreich und einem fällt Monate später auf, dass man ja immer noch zahlt."
12. 1 star, 2025-03-05: "Diese Firma hat mir vier Monate lang ohne abgeschlossenen Vertrag jeweils 12,50 € abgebucht"

### lebenslauf.com, https://de.trustpilot.com/review/lebenslauf.com (fetch; 5 reviews on page)
13. 1 star, 2026-08-06: "Arglistige Täuschung, nach 1,95€ wurden völlig intransparent nach 5 Tagen 34,95€ eingezogen."
14. 1 star, 2026-02-11: "Betrüger!!!! Nach 3 Tagen wurden automatisch 35 Euro vom Konto abgebucht."
15. 1 star, 2025-11-26: "Vorsicht wird eine abo fällig ob du wilst oder nicht das ist egal."
16. 1 star, 2024-06-15: "Da hast du dann ein Abo egal ob du das willst oder nicht. 29.55 fr. Pro Monat musst du nachher bezahlen."
17. 5 stars, 2024-10-22 (positive): "XING bietet diesen Service online an, ohne dass ein Abo abgeschlossen werden muss."

### lebenslauf.de, https://de.trustpilot.com/review/lebenslauf.de (fetch)
18. 3 stars, 2026-10-24: "Leider hat mich die Korrektur enttäuscht. Kleine eingebaute „Fehler" blieben unentdeckt"
19. 4 stars, 2026-10-19: "Teuer und automatische Verlängerung war mir nicht bewusst. Sonst gutes Angebot."
20. 1 star, 2026-10-20: "Sowas von ein schlechtes Tool. Ich kann gut verstehen, dass man Premium Versionen anbieten"

### Kickresume, https://de.trustpilot.com/review/kickresume.com (fetch)
21. 2 stars, 2026-08-25 (as the fetcher gave it): "KI support ist nur für Englisch, keine support für Deutsch."
22. 2 stars, 2026-04-29: "dass ich die bereits fertige Bewerbungen bzw. Lebensläufe nach Ablauf der Pro Testwoche nicht mal mehr herunterladen kann"
23. 4 stars, 2026-02-28 (positive): "Die überarbeiteten Textvorschläge und die Möglichkeit, die Stellenanzeige einzufügen sind super!"
24. 2 stars, 2025-09-29: "Intransparente Preise (mobile vs desktop)" and "AI Writer nur auf Englisch"
25. 2 stars, 2025-07-07: "Man ist durch dieses Abo-Modell gezwungen, wenn man kurzfristig nochmal die letzte Version runterladen will"

### Others
26. Novorésumé, 1 star, 2025-02-26: "The templates are awful and unsuitable for the German market." https://de.trustpilot.com/review/novoresume.com (fetch)
27. cvmaker.de, 1 star, 2026-10-05: "Frechheit ein 21,99€ mit anzuhängen, ohne Bemerkung!" https://de.trustpilot.com/review/cvmaker.de (fetch)
28. cvmaker.de, 1 star, 2026-10-20: "Auch ich habe schlechte Erfahrungen gemacht und kann mich nicht an eine zweite Zahlung nach 14 Tagen erinnern." same URL (fetch)
29. MyPerfectResume, 1 star, 2024-03-26: "Wann hören Sie endlich auf weiter Gebühren von meinem Konto abzubuchen!!!???" https://de.trustpilot.com/review/myperfectresume.com (fetch)
30. Verbraucherzentrale on Cvneed: "Über 1.000 Beschwerden von Verbraucher:innen über Cvneed sind seit Juli 2024 bundesweit in den Verbraucherzentralen eingegangen." https://www.verbraucherzentrale.de/wissen/vertraege-reklamation/abzocke/cvneed-achtung-abofalle-106793 `[search summary, unverified]`
31. t3n, HR expert on a ChatGPT letter: "An einigen Stellen merkt man, dass es sich um eine Übersetzung von Englisch auf Deutsch handelt." https://t3n.de/news/ki-bewerbung-chatgpt-anschreiben-so-reagieren-personaler-1529440/ (fetch)
32. Same article, HR expert: "Als potenzieller PR-Manager wärst du raus, sorry"
33. Same article: "Das Anschreiben sieht auf den ersten Blick professionell aus" (followed by criticism of filler phrases)

Reddit (r/arbeitsleben, read through the Arctic Shift archive, fetch), thread https://www.reddit.com/comments/1vi7ui8 , title "Anschreiben - wird dies in Zeiten von KI überhaupt noch gelesen?" (score 13):
34. post: "ist das Anschreiben nicht mittlerweile in die Kategorie *Spam* zu stecken?"
35. comment (score 3): "Man kann schon deutlich unterscheiden, wer stumpf KI kopiert und ein Mist Anschreiben hat"
36. comment (score 4): "Ich sag mal so: KI Anschreiben ist nicht schlimm sofern du das vernünftig machst."

Gaps: no Reddit thread about a named resume-builder subscription found (Reddit blocked, archive search flaky). App Store DE review feeds for the CV apps came back empty. Trustpilot complaints are almost all about billing; text-quality complaints are few (Kickresume English-only AI, lebenslauf.de Korrektur, Novorésumé templates).

Count: 36 entries, 4 of them positive; 32 complaint or criticism quotes.

---

## 5. Wishes and pains of applicants

| # | Quote / number | Source |
|---|---|---|
| 1 | Joblift study: 37 % of job seekers in Germany find the Anschreiben hard, 54 % of the younger; 32 % would apply more often without a required letter (52 % of the younger) (fetcher paraphrase) | https://www.personalwirtschaft.de/?p=131619 (fetch) |
| 2 | Same: 35 % spend 30 to 60 minutes, 30 % under 30, 20 % over an hour; 21 % send the first draft unchanged except address and contact person (fetcher paraphrase) | same |
| 3 | Same: 86 % struggle to present their advantages, 81 % to state their benefit to the company, 77 % to explain why that employer (fetcher paraphrase) | same |
| 4 | Joblift CCO: "Auf ein Bewerbungsanschreiben zu bestehen wirkt (…) wie ein Bremsklotz für die eigene Mitarbeitersuche" | same |
| 5 | Uni Bamberg 2017: on average 55 minutes to write and assemble an application; 58.1 % say the Anschreiben takes very long or long (search summary) | https://www.Uni-Bamberg.de/fileadmin/isdl/5_Bewerbung_der_Zukunft_20170210_WEB.pdf `[search summary, unverified]` |
| 6 | meinestadt.de via Statista: 57 % do not know what to write, 19 % say it costs a lot of time (search summary) | https://de.statista.com/infografik/amp/12264/einstellung-der-befragten-zum-bewerbungsanschreiben `[search summary, unverified]` |
| 7 | Softgarden survey: about 13 % use AI for the Anschreiben (search summary) | https://www.leinetal24.de/leben/karriere/bewerbungen-mit-chatgpt-ki-lebenslauf-anschreiben-schreiben-das-sollte-man-dabei-beachten-zr-92234069.html `[search summary, unverified]` |
| 8 | t3n HR expert: "Ein einfacher CV oder ein gepflegtes Linkedin-Profil sind für den ersten Eindruck bereits ausreichend" | https://t3n.de/news/ki-bewerbung-chatgpt-anschreiben-so-reagieren-personaler-1529440/ (fetch) |
| 9 | r/arbeitsleben title "Über 50 individuelle Bewerbungen, Anschreiben und Lebenslauf überarbeitet – trotzdem keine Einladung. Was mache ich falsch?" (score 6); body: "Seitdem habe ich über 50 Bewerbungen verschickt, leider ohne eine einzige Einladung zum Vorstellungsgespräch." | https://www.reddit.com/comments/1x4xb8j (fetch via archive) |
| 10 | r/arbeitsleben: "ich habe jetzt mein Anschreiben fertig und sitze schon seit einigen Tagen daran." | https://www.reddit.com/comments/1w2ggip (fetch via archive) |
| 11 | r/arbeitsleben: "Es ist wirklich hart draußen, daher will ich Bewerbungsunterlagen die mich möglichst nicht direkt aussortieren." | https://www.reddit.com/comments/1vtu0li (fetch via archive) |
| 12 | r/arbeitsleben: "Ich habe mich Anfang Juli auf eine Stelle bei einem Großkonzern beworben und bisher keine Rückmeldung erhalten." | https://www.reddit.com/comments/1w5hptk (fetch via archive) |
| 13 | r/arbeitsleben titles: "Freiwilliges Anschreiben bei Bewerbungen" and "Motivations- und Anschreiben?" (whether to send a letter when optional) | https://www.reddit.com/comments/1x4og3b ; https://www.reddit.com/comments/1wdcmqj (fetch via archive) |
| 14 | r/arbeitsleben: 15 of the last ~15 hits for "Lebenslauf" are feedback or advice requests, e.g. "Hi, würde mich über konstruktives Feedback zu meinem Lebenslauf freuen." | https://www.reddit.com/comments/1xgzkzb (fetch via archive) |
| 15 | Is the Anschreiben still expected? Same thread: "Ich schicke immer ein Anschreiben mit wenn gewünscht." (score 26); "Für mich ist das Anschreiben dann wichtig, wenn der Lebenslauf nicht genau das ist, was ich erwarte." (24); "Wir stützen uns primär auf den Lebenslauf, das Anschreiben kann aber die entscheidenden letzten 5% ausmachen." (14) | https://www.reddit.com/comments/1vi7ui8 (fetch via archive) |
| 16 | Stepstone survey (2017): CV ranked first by 68 % (search summary) | https://www.deutsche-handwerks-zeitung.de/bewerbungsverfahren-was-jobsuchende-abschreckt-160912/ `[search summary, unverified]` |
| 17 | Existing evidence (NACHFRAGE.md 4.7): "Spent 6 hours today especially tailoring my resume for the 10 companies that I applied to." (English, pain 3) | https://www.reddit.com/comments/1lwlxpq |
| 18 | Existing evidence: "I would pay for this when it is stable. Specially filling out workday applications." | https://news.ycombinator.com/item?id=42020550 |

Reading: the Anschreiben is a real pain (37 % find it hard, 86 % cannot show their advantage), but the pain is "what do I write", not typing speed. It is still sent when the ad asks for it, and recruiters on Reddit say it decides borderline cases. It is shrinking in importance (HR: a plain CV can suffice). No source for DACH-wide share of ads that require a letter was confirmed (a URL slug hinted at "about a quarter"; the page text did not confirm it).

Count: 18 rows.

---

## 6. Short-video evidence

Weak. TikTok, Instagram and YouTube pages cannot be read with WebFetch (empty pages), and WebSearch returned no German career-tip creator pages or view counts.

- https://www.tiktok.com/tag/bewerbungstipps returned only the title "TikTok - Make Your Day." (fetch, no data).
- YouTube search page returned only footer text (fetch, no data).
- Robert Half: more than 19 million people use TikTok in Germany (search summary) https://www.roberthalf.com/de/de/insights/bewerbungs-tipps/tik-tok-bewerbungen-mit-einem-kurzen-video-zum-naechsten-job `[search summary, unverified]`
- TikTok Resumes pilot 2021 (US): hashtag reportedly "more than 260 million views" (search summary, old, US) https://www.ypulse.com/newsfeed/2021/07/29/tiktok-resumes-has-been-a-hit-and-video-resumes-could-be-a-new-trend/ `[search summary, unverified]`
- Ahrefs organic-visit estimates (global, not DE): zety.com about 1.4 m, resume.io about 1.5 m, kickresume.com about 259k (search summary) https://ahrefs.com/websites/zety.com/competitors `[search summary, unverified]`. Suggests rivals live on Google; no evidence of their short-video reach.
- Faceless format feasibility (my judgement, not a source): screen recording "job ad in, tailored bullets out", before/after text, checklists work without people or music.

Verdict: not proven. Owner should check manually the view counts of the top videos for "Lebenslauf Tipps" and "Anschreiben" on TikTok and YouTube Shorts.

Count: 5 sourced items, 0 verified view counts.

---

## 7. Summary

1. Market: DE has about 3.0 m registered unemployed (Sept 2026, stock), 0.53 m graduates and 0.48 m new apprentices per year; IW (2011) puts job turnover at 25-30 % of jobs per year; AT about 0.30 m unemployed (July 2026), CH 140k (Sept 2026). No official count of applications or Arbeitsuchende found.
2. Public money does not pay: Vermittlungsbudget is discretionary, 5 EUR per written application, "Grundsätzlich keine Kostenübernahme für Online-Bewerbungen" (Jobcenter Köln 2023); no source covers software or online services. Users pay themselves.
3. Proven spending: yes. lebenslauf.de 16,99 EUR for one month, Zety 23,70 EUR per 4 weeks after a 2,70 trial, Resume.io 29,95 USD per 4 weeks, BewerbungGPT 7,99 EUR for five letters, ResuFit 14,90 EUR per month.
4. Strongest gap: honest price. Trustpilot DE is full of trial-to-subscription complaints (Zety, Resume.io, lebenslauf.com, cvmaker); Verbraucherzentrale counts 1,000+ complaints on one rival. A clear one-time pass with no renewal fits GRUNDSATZ rule 3. Second gap: German quality (Kickresume AI "nur für Englisch", HR hears translated English).
5. Not empty: BewerbungGPT (one-time pack, job ad paste, "keine Fakten erfunden"), lebenslauf.com (AI Anschreiben from job description) and ResuFit (job URL, free preview) already do the core job.
6. Main risk: ChatGPT as a free substitute for the Anschreiben. Only about 13 % use AI for it, and HR says plain AI text is noticeable, but paste-into-ChatGPT costs nothing.
7. Pain is real (37 % find the letter hard, 86 % cannot show their advantage) but the letter is losing weight and is still optional for many ads.
8. Fit with IDEEN section 10: proven spending is met. Cheap attention is unproven: no view counts could be read; rivals appear Google-driven. Faceless demos are feasible (screen recordings).
9. The honesty rule (rule 1) can be a real differentiator only if demonstrable, for example every sentence linked to a fact from the user's own CV.
10. Open: bewerbung.net, Canva and Novorésumé prices not read; DE short-video sizes not verified; Reddit billing complaints not found.
