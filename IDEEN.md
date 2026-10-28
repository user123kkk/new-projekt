# Idea search

Status: round 2 (2026-10-28), based on [NACHFRAGE.md](NACHFRAGE.md). Round 1 (2026-10-27) is kept below section 6. Basis: [[INDEX]], [GRUNDSATZ.md](GRUNDSATZ.md).

## 1. What the sources give and what they do not
The 37 stations teach **how to sell**, not **what to build**. They contain no market data. Only a few stations say anything about choosing an idea. Those are turned into selection criteria below. Every idea therefore needs outside evidence of demand before anything is built.

## 2. Selection criteria from the stations
| # | Criterion | Source (verbatim) |
|---|---|---|
| K1 | Demand already exists. Do not create it. | [[14-sell-water-to-the-thirsty]]: "understand what people are already looking for and where they are", "Most marketing fails because it tries to create demand." |
| K2 | The problem is already painful. The offer is relief. | [[14-sell-water-to-the-thirsty]]: "go where the problem is already painful enough"; [[37-sell-the-problem-first]]: "People don't buy solutions. They buy relief." |
| K3 | One defined group, not everyone. | [[19-sell-to-everyone-sell-to-no-one]]: "Focus on one group of people and make it your target audience." |
| K4 | Explainable in one sentence to a five-year-old. One message, one offer, one action. | [[10-the-five-year-old-rule]], [[34-one-message-one-offer-one-action]], [[15-three-questions-every-customer-asks]] |
| K5 | Benefit is felt immediately. | [[29-sell-the-instant-benefit]] |
| K6 | The product does not need to be unique. Branding and distribution decide. A boring product is fine. | [[04-there-is-no-winning-product]]: "Boring products with great marketing will win over fancy products with bad marketing." |
| K7 | We can reach the group ourselves (traffic). | [[32-conversion-problem-or-traffic-problem]] |
| K8 | Study what already works before building. | [[05-study-what-works-particl]]: "The smartest brands don't guess their marketing. They study what works." |
| G | Every rule of GRUNDSATZ.md holds, for the product and for its marketing. | [GRUNDSATZ.md](GRUNDSATZ.md) |

## 3. Candidates

### A. Explainer videos in the @conversion.doc style: abstract motion graphics, no music, no living beings
- **What:** Short vertical explainer videos for businesses. Shapes, text, icons, voice. First offered as a service, later as an app that generates them.
- **Why from the sources:** [[13-animations-that-turn-your-message-into-a-story]] is exactly this offer, sold by the creator of the sources. Problem as stated there: "most brands explain too much and say too little". The style itself is the proof: all 37 source videos meet GRUNDSATZ rules 8, 9 and 10 by default (abstract graphics, no people). Clarity cluster: 10, 24, 27, 30, 34.
- **K1:** Demand is visible: @conversion.doc sells this via DM. Size of that demand is unverified.
- **K2:** Medium. Pain = content that gets no attention. Pain exists but is not urgent for every business.
- **K3:** Open. Possible groups: small online shops, app founders, Muslim-owned businesses that want content without music or people.
- **K6:** Strong. Generic tools exist (Canva, Vyond, Jitter, AI video generators). The edge is the style plus rule compliance, not the technology.
- **K7:** Strong. The videos are their own marketing. Each post is a sample of the product ([[35-make-them-feel-they-found-it]]).
- **G:** Passes. Clients whose product is haram are refused.
- **Risk:** A service scales by hours. An app version competes with large tools.

### B. Conversion check for small online shops
- **What:** Enter a shop or landing page URL. You get a report on the three customer questions, clarity, checkout friction, and traffic vs. conversion.
- **Why:** [[32-conversion-problem-or-traffic-problem]], [[15-three-questions-every-customer-asks]], [[01-reduce-the-pain-of-paying]], [[27-the-more-people-think-the-less-they-trust]], [[34-one-message-one-offer-one-action]]. The stations are the checklist.
- **K1:** Shop owners with visitors but no sales search for exactly this. Unverified.
- **K2:** Strong. Money is lost every day ([[21-people-want-to-stop-losing]]).
- **K5:** Strong. The report comes in minutes.
- **K6/K7:** Weak. Many CRO and audit tools exist. Reaching shop owners needs a channel we do not have yet.
- **G:** Passes. The tool does not recommend fake scarcity, fake "was" prices or BNPL. That is a visible difference to other tools, not a religious selling point.

### C. Ad and marketing library ("study what works")
- **Why:** [[05-study-what-works-particl]].
- **Rejected:** Particl, Meta Ad Library and others already do this with large data budgets. No edge (K6 alone does not carry it without K7).

### D. "Halal marketing" compliance checker for Muslim businesses
- **Rejected:** It sells adherence to the religion as a product to Muslims. That is GRUNDSATZ rule 11. The compliance stays inside A and B as a quality standard, not as the selling point.

## 4. Assessment
| | K1 | K2 | K3 | K4 | K5 | K6 | K7 | G |
|---|---|---|---|---|---|---|---|---|
| A | visible, size open | medium | open | yes | yes | yes | strong | yes |
| B | likely, unverified | strong | shop owners | yes | strong | weak | weak | yes |

A leads because of K7: there is an existing reach model in which the product is its own advertisement, and it fits the rules without adjustment. B has the stronger pain but no channel.

## 5. Next step: evidence, not building (K1, K8)
1. Decide the group for A (K3).
2. Research: who sells abstract explainer videos, at what prices, with what demand. @conversion.doc is the first data point.
3. Test: make 3 to 5 videos in this style for the chosen group, post them, and count inquiries. Without inquiries, nothing gets built.
4. Only then decide whether the app (generator) is worth building or whether the service carries itself.

## Open inputs from the owner
- Skills and time available (design, motion, code).
- Language market: German, English or both.
- Existing reach (accounts, network).
- Budget.

---

## 6. Round 2: products derived from the demand search

Round 1 had no market data. [NACHFRAGE.md](NACHFRAGE.md) now gives 2,437 demand posts in 132 clusters plus 264 web findings. The five strongest clusters there are broad fields, not products. Each is cut here to **one job** (K4), because every one of them fails K4 or K6 as a full suite.

Selection rules used:
- Paying users who are angry at an incumbent count more than hypothetical "I'd pay" (K1, Indie Hackers counter-evidence).
- One job, one group, one sentence (K4, K3, [[34-one-message-one-offer-one-action]]).
- The first result must come in minutes, from the user's own existing data (K5, [[29-sell-the-instant-benefit]]).
- We do not try to beat a suite. We do the one job the suite does badly, at an honest price (K6, [[04-there-is-no-winning-product]]).
- GRUNDSATZ is a design constraint, not a selling point (rule 11).

### P1. Club fee tracker ("Vereinskasse") for small German clubs
- **Job:** the treasurer imports the member Excel file and the bank statement (CSV). The tool shows who has paid the annual fee and who has not, and sends polite reminders.
- **One sentence:** "See in one minute which members have not paid, and remind them."
- **Evidence (NACHFRAGE 4.1):** price tripled at WISO MeinVerein; boards run everything in Excel ("Der bisherige VOrstand hat alles mit einem Exel Dokument gemacht"); reviewers name fee settings as hard; one forum asks for Excel import. The web evidence is German-only and from reachable sites only (bias).
- **K5:** strong. Excel + bank CSV in, open list out. No migration of the whole club.
- **K6:** the suites (easyVerein, ClubDesk, Vereinsplaner, WISO) do this inside many features. Edge: only this job, cheaper, nothing to learn.
- **G:** reminders yes, no default interest or penalty fees (rule 2). No member photos (rules 9, 10). Clear price and cancellation (rule 3). Member data stays private (rule 6).
- **Unknowns:** how many clubs pay per year (market size), and K7.

### P2. Photo report for tradespeople
- **Job:** on site, take before and after photos of the work. The app makes a dated PDF report with the company name and sends it to the customer.
- **One sentence:** "Photos in, finished report to the customer out."
- **Evidence (NACHFRAGE 4.5):** "Taking before-after photos and organizing them and sending them to the client takes up so much time." (score 57); cluster grew to 20 posts from 10 subreddits; German OMR reviews show price anger at Plancraft, Tooltime, Hero.
- **K5:** strong. First report in the first job.
- **K6:** CompanyCam does this in the US (named once). In German-speaking markets the suites bundle it. Edge: one job, low price.
- **G:** photos show buildings and work, not people; the app must not encourage photographing people (rule 9: real need only). No music in any demo (rule 8).
- **Unknowns:** whether tradespeople pay for a single-job app; K7.

### P3. Receipt-to-entries for small-firm bookkeepers
- **Job:** a bookkeeper's client photographs receipts; the tool turns them into rows for a spreadsheet or a QuickBooks/Xero import.
- **Evidence (NACHFRAGE 4.14):** "Each month I spend literal DAYS organizing, scanning and inputting their expenses into a spreadsheet"; 12 of 25 posts already pay for a tool; r/Bookkeeping is one visible community.
- **K6:** weak. Dext and Hubdoc do exactly this. Edge would be price only.
- **Market:** US. Owner language and market fit unknown.

### P4. Payment reminders for freelancers
- **Job:** the freelancer adds open invoices; the tool sends polite, timed reminders until paid.
- **Evidence (NACHFRAGE 4.2):** strongest pain (money lost), 4 posts at pain 3. But 0 of 20 posts pay implied, and the Indie Hackers title "Not one would pay to fix it" is direct counter-evidence for this exact field.
- **K6:** every invoicing app has reminders. Weak.

### Not carried forward
- Booking for solo providers (NACHFRAGE 4.4): needs one trade chosen and competes with marketplaces (Booksy). Kept as a watch item.
- Small landlords (4.3): Reddit evidence too thin after round 2.
- Language learning, Shopify tools: see NACHFRAGE 4.15, 4.13.

### Ranking
| | Job (K4) | K1 | K2 | K3 | K5 | K6 | K7 | G |
|---|---|---|---|---|---|---|---|---|
| P1 Club fee tracker | yes | strong, web only | medium | yes | strong | medium (one job vs suites) | open | pass |
| P2 Photo report | yes | medium | medium | yes | strong | medium | open | pass |
| P3 Receipt-to-entries | yes | strong | medium | yes | strong | weak | medium (r/Bookkeeping) | pass |
| P4 Payment reminders | yes | medium, counter-evidence | strong | split | medium | weak | open | pass |

**Lead: P1, then P2.** Both are one job with an instant result from the user's own files, both target a group that already pays and complains about price, and both fit GRUNDSATZ without changes. P1 has the most independent sources. P3 has the best payment signal but a direct incumbent doing the same job. P4 is held back by the counter-evidence.

K7 is open for every candidate. It decides more than any other criterion ([[32-conversion-problem-or-traffic-problem]]) and depends on the owner (section 7).

## 7. Owner inputs (2026-10-28)
- Market: German-speaking (DACH).
- Own access to a target group: none. Reach must come from content, search and small ads (K7).
- Skills: the owner does not code; Claude builds, the owner tests.
- Budget for the first test: up to 100 EUR.

Consequence: P1 is the lead. It is German-market, has the most German evidence, and has a natural free entry point (a fee-list Excel template that people already search for and use, see the Excel quotes in NACHFRAGE 4.1). That fits [[35-make-them-feel-they-found-it]] and a 100 EUR budget. P2 stays second.

## 8. Next step: evidence before building (K8)
1. Done: owner inputs (section 7).
2. For P1: collect 1-2 star app-store and OMR reviews of the incumbents and their prices (K8, [[05-study-what-works-particl]]).
3. Test demand before code: a one-page offer with the one sentence, price and a sign-up, shown to the group through the reachable channel. Count sign-ups. No sign-ups, nothing gets built.

### K8 result for P1 (2026-10-28)
Source: [quellen/nachfrage/web/p1-vereinskasse.md](quellen/nachfrage/web/p1-vereinskasse.md). Quotes there were extracted through a summarising fetch tool; only PDF quotes are proven exact, the rest are marked.
- Market: 628,992 registered Vereine in Germany (ZiviZ, March 2026); about 63% of civil-society organisations have 100 members or fewer.
- Price for a 100-member club today: about 120-360 EUR per year (ClubDesk S 120 EUR/year, Vereinsguru S 14 EUR/month, easyVerein Small 19.38 EUR/month, campai 30 EUR/month).
- **Main risk:** ClubDesk Free covers up to 50 members at 0 EUR, with SEPA and bank-file import. For the smallest clubs the job is already free.
- Complaints are price for very small clubs, setup effort for volunteers, returned debits and fee billing, weak finance modules. Nobody asks for "who has not paid" on its own. This weakens P1 as a stand-alone product.
- Workaround: Excel plus bank CSV plus VLOOKUP. The free-template space is held by a content site, not a tool.
- Reachable channel with 100 EUR: search content (fee-list Excel template, "Mitgliedsbeitrag nicht gezahlt" reminder template) and answers in JuraForum Vereinsrecht.
- Assessment: P1 survives only for clubs of roughly 50-100 members that find 120 EUR/year plus setup too much, at about 29-59 EUR/year. That price is an inference, not measured willingness to pay. K6 drops from medium to weak.

Next: the same K8 check for P2, so the choice between P1 and P2 rests on the same kind of evidence.

### K8 result for P2 (2026-10-28)
Source: [quellen/nachfrage/web/p2-fotobericht.md](quellen/nachfrage/web/p2-fotobericht.md). Apart from ZDH, Destatis, WKO and statute pages, quotes are fetch summaries or search snippets and are marked as such.
- Market: 1,038,126 Handwerksrolle entries in Germany (ZDH, end of 2025); 56.6% of firms have under 5 people, roughly 300,000 firms (own arithmetic).
- Incumbents are suites: Craftnote 14.90-49.90 EUR per user per month (customer report needs the 29.90 tier, annual lock-in, three months' notice), Hero about 59-69 EUR, ToolTime 79 EUR, PlanRadar 26 EUR for one user, Docu Tools from 54 EUR, CompanyCam 63 USD. Free: Onstruc (iOS, 24 ratings), Fieldwire Basic, Dalux Field Basic. None targets the Abnahme report for small German trade firms.
- Complaints: price and weight for small firms, photo sync and speed, support, annual lock-in, PDF templates sold as extras. Nobody asks for "just photos to PDF" in those words (inference, as with P1).
- Workaround: phone gallery, WhatsApp, free Word/Excel Abnahmeprotokoll templates (Streit uses its template as lead magnet).
- Legal reason the job matters: dated Zustandsfeststellung under § 650g BGB; the Abnahme date starts the limitation period (§ 634a BGB, five years for a Bauwerk; VOB/B § 13 four years).
- Price inference: free tier, then about 5-9 EUR per month or 49-79 EUR per year per company, cancellable monthly.
- Main risk: WhatsApp is free and installed; a suite can add the feature. Customer photos need consent.

### Decision: P2 is the lead (2026-10-28)
| | P1 club fee tracker | P2 photo report |
|---|---|---|
| Direct free competitor for the core segment | yes, ClubDesk Free up to 50 members | no German Abnahme-focused one (Onstruc thin) |
| Buyer | volunteer treasurer, club budget | business owner, business expense |
| Price room vs incumbents | 29-59 EUR/year vs 120+ | 49-79 EUR/year vs 180-950+ per user |
| Reason beyond comfort (K2) | annoyance, time | legal: § 650g BGB Zustandsfeststellung, start of warranty period |
| Instant benefit (K5) | after Excel + bank import | first report on the first job |
| GRUNDSATZ | pass | pass: photos of work and buildings only (rule 9, real need); no people in demo material; no music (rule 8) |

P2 wins on K2, K6 and buyer. P1 stays as fallback. Both still lack direct evidence that people pay for the single job; only the test below can supply that.

## 9. Demand test for P2 (before any code)
1. **Free entry point:** a page with a free "Abnahmeprotokoll mit Fotodokumentation" template (PDF/Word), searchable in German. This is the channel with the best fit for no following and 100 EUR ([[35-make-them-feel-they-found-it]], [[14-sell-water-to-the-thirsty]]).
2. **Offer on the same page:** one sentence, one price, one action ([[34-one-message-one-offer-one-action]]): "Fotos auf der Baustelle machen, fertiges Abnahmeprotokoll als PDF an den Kunden." Price shown honestly with monthly cancellation (rules 3, 4). Action: "Vormerken" with e-mail (no payment yet, stated plainly so nothing is concealed, rules 1, 6).
3. **Traffic:** search content first (0 EUR); then up to 100 EUR in search ads on "Abnahmeprotokoll Vorlage" type terms.
4. **Measure:** template downloads, sign-ups, sign-up rate per visitor. Decision threshold set before launch by the owner.
5. **Required before publishing:** German Impressum and privacy notice (legal duty for a commercial page), a domain, hosting. These need the owner's real name and address.

## 10. Selection rule agreed with the owner (2026-10-28)
The question is not "where is the gap" but **where people already spend money, and where faceless short videos get attention cheaply**. A crowded category is acceptable ([[04-there-is-no-winning-product]], K6) if both hold:
1. Proven spending: people already pay for products in the category (subscriptions, one-time purchases).
2. Cheap attention: the benefit can be shown in a few seconds with text, shapes, voice and screen recordings, without music and without people (GRUNDSATZ rules 8-10), so the videos themselves carry the reach (K7, [[35-make-them-feel-they-found-it]]).

Owner decisions so far: calorie tracking excluded by the owner. Candidate under review: German reading for beginners (P5, research running).
