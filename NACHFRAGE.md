# Demand search, round 1

Status: round 1 (2026-10-28). Basis: [IDEEN.md](IDEEN.md) (criteria K1-K8, G), [GRUNDSATZ.md](GRUNDSATZ.md) (15 rules), `quellen/nachfrage/cluster_stats.md`, `quellen/nachfrage/web/`.

## 1. Summary

We searched for stated demand in three places: Hacker News (3,904 posts), Reddit through an archive (9,794 posts) and a web sweep of app-store reviews, review sites, Stack Exchange and forums (264 entries). After classification and removal of GRUNDSATZ conflicts, 1,402 demand posts remain. They fall into 89 clusters. The web sweep adds problem groups from paying users of existing software.

The two sources point in different directions. The highest-scoring clusters (LLM hosting, private browsers, AI coding cost, ad blocking) come mostly from Hacker News developers and privacy-minded users. They are dominated by large platforms and fail K6 and K7 for a small team. The web sweep points at small-business and club administration (invoicing, clubs, landlords, booking, trades). There, paying customers of existing tools complain about price rises, hidden cancellation, broken apps and missing support. These groups are concrete (K3) and already pay (K1), but they are crowded (K6) and we have no known channel to them (K7).

Payment evidence is weak overall. "I'd pay for X" on Hacker News is mostly hypothetical. Indie Hackers titles say complaints are easy to find and payment is not. The strongest payment evidence is indirect: people already pay incumbents and are angry about the price.

The five clusters rated strongest are in section 4: German club administration, freelancer invoicing and payment chasing, small landlords, booking for solo providers, and trades office software. None is rated strong on all criteria. No cluster passes K6 and K7 clearly. This search does not confirm or refute candidates A (explainer videos) and B (shop conversion check) from IDEEN.md. The nearest clusters (content creators, lead generation, online sellers) are weak.

## 2. Method and limits

**Sources**
- Hacker News via the Algolia API: 3,904 posts since 2024-01-01, found with phrases like "I'd pay for" and "wish there was an app".
- Reddit via the Arctic Shift archive: 9,794 posts. The archive matches loose words, so only about 4% contained the exact phrase. A full harvest was possible only for r/SideProject, r/Startup_Ideas, r/AppIdeas, r/SomebodyMakeThis and r/Lightbulb, because the archive throttled us. r/SideProject was excluded from the loose-word classification because it is mostly self-promotion.
- Web sweep: 264 entries from app-store reviews (137), review sites (52), Stack Exchange (42), English forums (15), German forums and tenders (13) and Indie Hackers (5).
- Not reachable: Reddit directly and PullPush refused automated access. Search engines do not index Reddit for our tools (see `web/reddit-search-*.md`). G2, Capterra, GetApp, Software Advice, trusted.de, Quora, gutefrage.net, Shopify Community, AccountingWeb, Indie Hackers (HTTP 403), Google Play (404), Chrome Web Store (consent wall) and Lobsters (blocked). Details in `web/00-coverage.md`.

**Funnel**
- Prefilter, then 7,382 posts classified by Haiku agents.
- 1,474 judged demand-true.
- Minus 36 GRUNDSATZ flags (music, dating, gambling, financing, adult, images of living beings), 4 non-verbatim quotes, 3 hand exclusions (age-verification spoofer, shadow-library book search) and 29 duplicates. Result: 1,402.

**Limits**
- One classifier read only the first ~450 characters of posts in 4 batches. A recheck found 23 missed demand posts and fixed them. Other batches may have similar small misses.
- A slow Arctic Shift run over about 146 niche subreddits (trades, landlords, teachers, e-commerce, health, German subs) with 6 phrases is still running (about 6 hours). Its results are not in this document. They come in round 2.
- "Pay explicit" on Hacker News is mostly hypothetical ("I'd pay for X") in reply threads. It is a weak signal.
- Indie Hackers counter-evidence (`web/indiehackers.md`): complaints are easy to find, payment is not. Both titles are snippet only (page returned HTTP 403).
- Bias: Hacker News data skews to developers and privacy-minded consumers. The web sweep skews to German club, craft/invoicing, landlord and Shopify software, because those sites were reachable.
- Reddit "score" in cluster_stats is the post's upvote count. Posts in idea subreddits are often founders describing a problem they want to build for. The "group" column is the group the poster describes, not a verified customer.
- Many Stack Exchange entries date from 2009-2016. Their signal is view count. SoftGuide tenders are old and mostly closed (one open tender, 26/3608).
- Web counts below are label mentions. An entry can carry a domain label and a problem label. The 264 entries carry 387 labels.

## 3. Top clusters

### 3.1 Reddit and Hacker News (from cluster_stats.md)

Strength = posts + 3 x pay explicit + 3 x pain 3. The first 25 real clusters are listed. Cluster 24 ("misc", 36) is skipped. "Platform" marks clusters dominated by a few large vendors or by the operating system.

| # | Cluster | Group | Posts | Pay explicit | Pain 3 | HN / Reddit | Strength | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | LLM hosting, APIs and local models | developers / privacy-minded AI users | 28 | 13 | 0 | 20 / 8 | 67 | Platform |
| 2 | Alternative and private browsers | privacy-conscious browser users | 20 | 15 | 0 | 19 / 1 | 65 | Platform |
| 3 | Job search and application automation | job seekers / recruiters | 29 | 5 | 4 | 5 / 24 | 56 | Crowded |
| 4 | AI coding assistant cost, limits and context loss | developers using AI coding tools | 26 | 10 | 0 | 18 / 8 | 56 | Platform |
| 5 | Ad blocking and ad-free services | consumers | 17 | 13 | 0 | 16 / 1 | 56 | Platform |
| 6 | Startup idea validation and founder support | founders / indie hackers | 46 | 2 | 1 | 1 / 45 | 55 | Sampling artifact |
| 7 | Developer tooling: editors, debuggers, languages | software developers | 30 | 6 | 1 | 28 / 2 | 51 | Too broad |
| 8 | Developer tooling: databases, APIs and data | software developers | 24 | 8 | 0 | 18 / 6 | 48 | Too broad |
| 9 | Social feed control and de-algorithmization | social media users | 24 | 7 | 0 | 8 / 16 | 45 | Platform |
| 10 | Voice dictation, speech-to-text, text-to-speech | dictation / audio users | 18 | 9 | 0 | 14 / 4 | 45 | Crowded |
| 11 | Travel planning, navigation, local discovery | travellers | 30 | 4 | 0 | 4 / 26 | 42 | Platform |
| 12 | Streaming, TV and media servers | streaming viewers / media server users | 24 | 6 | 0 | 7 / 17 | 42 | Platform; G |
| 13 | Photo, video and creative editing tools | photographers / phone users | 26 | 4 | 1 | 11 / 15 | 41 | Platform; G |
| 14 | Private messaging and social network alternatives | privacy-minded / community users | 22 | 6 | 0 | 13 / 9 | 40 | Network effect |
| 15 | Developer tooling: git, CI, code review | software developers | 18 | 7 | 0 | 16 / 2 | 39 | Too broad |
| 16 | Self-hosted storage, backup and file sync | self-hosters / families | 18 | 6 | 1 | 16 / 2 | 39 | Niche developers |
| 17 | Mac and Windows system performance and maintenance | Mac / Windows / Linux users | 18 | 6 | 1 | 14 / 4 | 39 | Platform |
| 18 | Content creator tools and growth | content creators | 26 | 3 | 1 | 4 / 22 | 38 | Crowded |
| 19 | Language learning tools | language learners | 17 | 7 | 0 | 8 / 9 | 38 | Crowded |
| 20 | AI-generated content detection and filtering | social media / web users, website owners | 14 | 8 | 0 | 10 / 4 | 38 | Accuracy |
| 21 | News and newsletter overload | news readers | 16 | 7 | 0 | 7 / 9 | 37 | Crowded |
| 22 | Frontend and UI building tools | web / frontend developers | 16 | 6 | 1 | 10 / 6 | 37 | Too broad |
| 23 | Phone calls: spam blocking, screening, handling | phone users | 16 | 5 | 2 | 7 / 9 | 37 | Platform (OS, carriers) |
| 25 | Alternative and private search engines | privacy-conscious searchers | 9 | 9 | 0 | 9 / 0 | 36 | Platform |
| 26 | Video games and gaming | gamers / game developers | 16 | 6 | 0 | 8 / 8 | 34 | G |

Observations
- No cluster has more than 4 posts with pain 3. Clusters with high "pay explicit" counts are Hacker News heavy.
- Clusters with many Reddit posts and real money at stake sit lower: 38 freelancer invoicing (strength 28, pain 3 = 4), 40 small business operations (27, pain 3 = 3), 61 community and club admin (17), 48 landlords (23), 84 trades software (9, but see the web table).

### 3.2 Web sweep problem groups (264 entries, 387 labels)

Domain groups

| Domain group | Label count |
|---|---|
| Personal task and note apps | 21 |
| Invoicing and quotes for small business | 21 |
| Club or association member and fee administration | 18 |
| Time tracking and shift scheduling | 15 |
| Receipt scanning and bookkeeping | 13 |
| Teacher grades and class admin | 10 |
| School or daycare administration and parent communication | 10 |
| Appointment booking, reminders, no-shows | 9 |
| Personal budget and household accounts | 8 |
| Landlord rent and tenant tracking | 8 |
| Calendar and data sync between services | 7 |
| Data export or migration between services | 7 |
| Tool request for small-business admin | 6 |
| Inventory tracking for small shops | 4 |
| PDF editing and scanning | 4 |
| Family organizer | 4 |
| Community organization admin | 4 |
| Client management for small business (CRM) | 4 |
| Tool request (specific, no known app) | 22 |

Problem types

| Problem type | Label count |
|---|---|
| Missing feature (specific) | 59 |
| Subscription too expensive or price increases | 44 |
| App unreliable: crashes, login failures, missing notifications | 27 |
| Cancellation hidden or charged after cancelling | 15 |
| Support unreachable | 14 |
| Spreadsheets or paper as workaround | 11 |
| Too complicated or too much to learn | 7 |
| Data lost or sync broken after update | 6 |
| One-time purchase turned into subscription | 5 |
| Platform fees or commissions too high | 3 |
| Software too expensive for small scale | 3 |
| Fragmented data across many lists or tools | 3 |
| Willingness to pay unproven (counter-evidence) | 2 |

Reading: most web entries are 1-2 star reviews of products people already use or pay for. That is evidence of an existing paying market, and of an angry share of it. It is not evidence that those people would switch.

## 4. Assessment

Scale: strong / medium / weak / no. "Unknown" means no source in round 1 speaks to it. Quotes are copied from `cluster_stats.md` or `web/*.md` unchanged. Where a quote is a search snippet, that is stated.

### 4.0 Overview

| # | Cluster (source) | K1 | K2 | K3 | K4 | K5 | K6 | K7 | G |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Club and association admin, German (web 18 + cluster 61) | strong | medium | yes | yes | medium | weak | unknown | pass, 3 notes |
| 2 | Freelancer invoicing and payment chasing (cluster 38 + web invoicing 21) | medium | strong | split | yes | medium | weak | unknown | pass, 2 notes |
| 3 | Small landlords (web 8 + cluster 48) | medium | medium | yes | yes | medium | weak | medium | pass |
| 4 | Booking for solo providers and small practices (web 9 + cluster 40) | strong | medium | split | yes | medium | weak | weak | pass, 1 note |
| 5 | Trades and craft office software (cluster 84 + web) | medium | medium | yes | no | medium | weak | weak | pass |
| 6 | School, daycare and teacher apps (web 20) | medium | medium | split | medium | weak | weak | no | flag (rule 9) |
| 7 | Job search automation (cluster 3) | strong | medium | broad | yes | medium | weak | medium | pass, 1 note |
| 8 | Offline voice dictation (cluster 10) | medium | weak | no | yes | strong | weak | weak | pass |
| 9 | Family caregivers: elder care, scam calls (clusters 63, 23) | weak | strong | yes | no | weak | medium | unknown | pass, 2 notes |
| 10 | Doomscrolling and feed control (clusters 54, 9) | medium | medium | no | yes | medium | no | weak | pass, 1 note |
| 11 | Receipt scanning and bookkeeping (web 13) | medium | medium | split | yes | strong | weak | weak | pass |
| 12 | Subscription and cancellation tracking (cluster 81 + web) | weak | medium | no | yes | medium | weak | weak | pass |

Order of strength is not the table order. Section 4.13 gives the ranking.

---

### 4.1 Club and association administration (German)
Group: boards, treasurers and secretaries of small clubs in Germany/Austria/Switzerland.

- **K1 strong.** 18 web entries carry this label, from OMR reviews of five products (VereinsGuru, Vereinsplaner, WISO MeinVerein, easyVerein, ClubDesk), forum threads and SoftGuide tenders including one open tender (26/3608, 6,000 records). Reddit side is small (cluster 61: 14 posts, 1 pay explicit). Caveat: the web sweep was biased toward German clubs because those sites were reachable.
- **K2 medium.** Annoyance and cost, not acute loss. Price tripling, missing finance features, Excel as fallback.
- **K3 yes.** One group with one buyer role (the treasurer or board).
- **K4 yes.** "Members, fees, reminders in one place."
- **K5 medium.** Benefit appears after migrating member data. Not instant.
- **K6 weak.** At least five incumbents with years of features. The edge could only be price, simplicity or the specific gaps (budget view, Excel import, mobile finance). Boring is fine under K6, but we have no technical edge.
- **K7 unknown.** Clubs gather in forums and associations, but no source shows a channel we could use.
- **G pass, with notes.** (a) Member lists usually carry photos: no photos of people (rules 9, 10). (b) Dunning (Mahnwesen) is a standard club feature: reminders yes, default interest or penalty charges on late payment no (rule 2; owner to confirm). (c) One reviewer is the chair of a religious-affiliated association. Serving such customers is rule 15. Marketing it as a religious product would be rule 11.

Quotes
- "Das Programm wird nun aber zum dreifachen Preis verkauf" (treasurer, civic organization) https://omr.com/en/reviews/product/wiso-meinverein-web/all/3
- "Der bisherige VOrstand hat alles mit einem Exel Dokument gemacht" (board member) https://omr.com/en/reviews/product/vereinsguru/all
- "Leider sind nicht alle Funktionen, z.B. Finanzen, nicht in der App nutzbar und man muss weiterhin über den Browser gehen. Dadurch wird de APP nutzlos. Hoffe, dass sich das bald ändert." (App Store review) https://apps.apple.com/de/app/easyverein-vereinsverwaltung/id1582761507

### 4.2 Freelancer invoicing and payment chasing
Group: freelancers and solo workers; the web side adds micro-businesses using invoice apps.

- **K1 medium.** Cluster 38: 13 posts, pain 3 = 4, pay explicit 1. Web: 21 invoicing labels, most from paying users of Invoice Simple, Invoice 2go, Invoice Maker, lexoffice, sevdesk. Counter-evidence from Indie Hackers (below): a founder found 71 people complaining and none willing to pay.
- **K2 strong.** Money lost. Posts claim "$2-5K/year" lost to late clients. Those figures are the posters' claims in idea posts and are not verified.
- **K3 split.** "Freelancers" is broad. Needs one trade and one country.
- **K4 yes.** "Send the invoice, chase the payment."
- **K5 medium.** The reminder helps at once. Cash arrival does not.
- **K6 weak.** Very crowded. The visible incumbent failures (price increases, hidden cancellation, no support, app down at payment time) are the only opening.
- **K7 unknown.**
- **G pass, with notes.** Rule 3 is a real differentiator here: competitor reviews are full of hidden cancellation and trial charges. Rule 2 applies to the dunning feature (no default interest, as in 4.1).

Quotes
- "freelancers losing $2-5K/year on clients who ghost invoices." (cluster 38) https://www.reddit.com/comments/1r73tui
- "lost a partnership because I forgot to followup in time" (cluster 38) https://www.reddit.com/comments/1sqtcfr
- "They are now wanting to charge me £60 for 3 invoices per month when it used to be £20 every year for unlimited." (Trustpilot, 1 star) https://www.trustpilot.com/review/invoicesimple.com
- Counter-evidence, snippet only (title): "I found 71 people complaining about the same problem. Not one would pay to fix it." https://www.indiehackers.com/post/i-found-71-people-complaining-about-the-same-problem-not-one-would-pay-to-fix-it-209e2bf18e

### 4.3 Small landlords
Group: landlords with about 1 to 30 units, mostly US in the sources (BiggerPockets); one German tender and one 2004 thread.

- **K1 medium.** 8 web entries, 5 BiggerPockets threads with 6 to 37 replies and up to 2,069 views. Cluster 48 adds 17 mixed posts (1 pay explicit); most of those are tenants or homeowners, not landlords.
- **K2 medium.** Time and errors, not acute loss. Spreadsheets "don't flag" partial payments or lease ends.
- **K3 yes.** Small landlords.
- **K4 yes.** "Rent payments, balances, lease dates."
- **K5 medium.**
- **K6 weak.** Avail, TurboTenant, Stessa, Buildium, AppFolio, QuickBooks all appear. Free tiers exist. The gap named in the sources is price and complexity for 1 to 25 units.
- **K7 medium.** The group gathers visibly (BiggerPockets). We have no tested route.
- **G pass.** No mortgage or interest features. No tenant credit scoring that depends on interest-bearing credit data (owner to confirm if screening is ever added).

Quotes
- "Software packages that do offer what you want, are too expensive for just one door." https://www.biggerpockets.com/forums/52/topics/1193472-property-management-software-for-1-sfr
- "It won't tell you that a tenant's lease expires in 45 days and you need to send a renewal notice." https://www.biggerpockets.com/forums/52/topics/1277850-free-google-sheets-rent-payment-tracker-template-for-landlords?page=1
- "the more advanced systems (like bildium) will have you spend more time learning the software than anything else." https://www.biggerpockets.com/forums/899/topics/1259131-which-property-management-software-is-good-to-use-just-starting-out

### 4.4 Booking for solo providers and small practices
Group: hairdressers, therapists, physio practices and similar one-to-few-person businesses.

- **K1 strong.** 9 web labels. Booksy's Trustpilot profile alone shows 16,583 reviews; Setmore, Dikidi, Beautinda, Salonist, Phorest and SoftGuide tenders (physio, therapy centre) add more. Cluster 40 (small business operations): 18 posts, pay none.
- **K2 medium.** Lost clients when calendars break. Fees taken behind the provider's back.
- **K3 split.** The group needs one trade (for example physio practices) before it is one group.
- **K4 yes.** "Clients book, get reminded, fewer no-shows."
- **K5 medium.**
- **K6 weak.** Large incumbents with network effects (client marketplaces). A tool without marketplace has to win on honest fees.
- **K7 weak.** Providers are many and dispersed. No tested channel.
- **G pass, with note.** Rule 3/4 fit: transparent fees. The app must not depict people. Segment choice (physio vs hair/beauty) is the owner's call.

Quotes
- "I pay a monthly subscription to book my clients, not to have Booksy compete with me for their payments." (App Store) https://apps.apple.com/us/app/booksy-biz-for-businesses/id725335996
- "when I asked to cancel my subscription they were still taking money out of my account" (Trustpilot, hairdresser) https://www.trustpilot.com/review/booksy.com
- "Too many cancellations because clients reply to those reminders." (App Store) https://apps.apple.com/us/app/setmore-appointment-scheduling/id665859578

### 4.5 Trades and craft office software
Group: small Handwerk and trades businesses (plumbing, electrical, HVAC, carpentry, pressure washing).

- **K1 medium.** Cluster 84: 6 posts, pay explicit 0, pain 3 = 1. Reddit scores of 57 and 71 show interest. Web: OMR reviews of Plancraft, Tooltime, Hero and OpenHandwerk, plus two old SoftGuide tenders (15/178, 15/269).
- **K2 medium.** Forgotten invoices, photos and job tracking.
- **K3 yes.** One group in principle.
- **K4 no.** Quotes, invoices, photos, time tracking and crew are five jobs. Needs cutting to one (for example only before/after photo reports).
- **K5 medium.**
- **K6 weak.** Specialist incumbents with trade-specific features (GAEB, wholesaler prices). Reviewers complain about price rises and ignored support.
- **K7 weak.** No known channel to tradespeople.
- **G pass.**

Quotes
- "there is a plumber right now who is owed a few thousand dollars because he finished a job, meant to send the second invoice, got called to the next emergency and forgot." (cluster 84) https://www.reddit.com/comments/1wisa84
- "Taking before-after photos and organizing them and sending them to the client takes up so much time." (cluster 84, pressure washing owner) https://www.reddit.com/comments/1x8dmwr
- "Preiserhöhung im übertriebenen Maße." (OMR, Plancraft, owner of construction business) https://omr.com/de/reviews/product/plancraft/all

### 4.6 School, daycare and teacher apps
Group: parents, teachers, daycare staff. The buyer is usually the institution.

- **K1 medium.** 20 web labels (10 school/daycare, 10 teacher), all App Store reviews and one SoftGuide tender (Kita, 17/750). Cluster 83 (teacher tools): 6 posts.
- **K2 medium.** Missed notifications and broken sync before report-card week.
- **K3 split.** Parents, teachers and institutions want different things.
- **K4 medium.**
- **K5 weak.**
- **K6 weak.** Remind, TalkingPoints, Kita-App and similar are mandated by schools.
- **K7 no.** The school picks the app. A small team cannot reach the decision makers, and notification delivery is partly a platform problem.
- **G flag.** Daycare apps share photos of children (rule 9). Would need a no-photo design.

Quotes
- "I get notifications about 20% of the messages. I’m missing important time-sensitive messages." https://apps.apple.com/us/app/families-talkingpoints/id1320244591
- "Bildschirm bleibt weiß Keine Daten werden geladen Ausloggen und neu einloggen hilft auch nicht Auch löschen und die App neu installieren hilft nicht" https://apps.apple.com/de/app/kita-app/id1546184555
- "Nächste Woche stehen die Zeugnisse an und ich kann nichts mehr synchronisieren. Da muss ich leider jetzt den Anbieter wechseln." (teacher) https://apps.apple.com/de/app/teacherstudio/id1145795564

### 4.7 Job search and application automation
Group: job seekers (Reddit side 24 of 29 posts).

- **K1 strong.** 29 posts, 5 pay explicit, pain 3 = 4. Highest consumer-side count in the table.
- **K2 medium.** Hours lost to tailoring resumes and checking boards.
- **K3 broad.** Job seekers in general. Needs one field.
- **K4 yes.** "Search all boards once, apply faster."
- **K5 medium.**
- **K6 weak.** Many auto-apply and resume tools exist, and the boards (LinkedIn, Indeed) control access. Scraping boards is a terms-of-service problem.
- **K7 medium.** The group is visibly active online. The space is saturated.
- **G pass, with note.** Rule 1: generated applications must not invent experience or claims. Rule 5: no "guaranteed interview" language.

Quotes
- "I'm tired of checking 5 different sites for the same job title." https://www.reddit.com/comments/1u03sjr
- "Spent 6 hours today especially tailoring my resume for the 10 companies that I applied to." https://www.reddit.com/comments/1lwlxpq
- "I would pay for this when it is stable. Specially filling out workday applications." (Hacker News) https://news.ycombinator.com/item?id=42020550

### 4.8 Offline voice dictation
Group: mixed (Mac, Android, iPhone users, privacy-minded, accessibility).

- **K1 medium.** 18 posts, 9 pay explicit (14 Hacker News). Hypothetical payment.
- **K2 weak.** Pain 2 or below throughout.
- **K3 no.** Several groups with different devices.
- **K4 yes.**
- **K5 strong.**
- **K6 weak.** The cluster itself names Aqua Voice, Wispr Flow, Superwhisper, macOS dictation and Google Assistant. "Offline" is the gap people name, and local models make it buildable, but others can ship the same.
- **K7 weak.** Hacker News audience.
- **G pass.** Speech-to-text is voice, not music (rule 8). A text-to-speech product would need an owner decision on voices (rule 10).

Quotes
- "I would pay for a completely offline version of this, cloud voice data is non-starter for me though unfortunately" https://news.ycombinator.com/item?id=43642885
- "I wish there was something where I could transcribe iPhone voice memos to text." https://news.ycombinator.com/item?id=41002148
- "I think I would pay for this in a heartbeat if it was more "available", as in not just a web app." https://news.ycombinator.com/item?id=39840160

### 4.9 Family caregivers: elder care and scam calls
Group: adult children and carers of elderly parents or people with dementia. Two clusters (63 elder care, 8 posts; 23 phone calls, 16 posts) that share this group only in part.

- **K1 weak.** Small counts. One explicit pay statement with 9 upvotes.
- **K2 strong.** Pain 3 appears in both clusters. Carers give up careers, sit through every session.
- **K3 yes.**
- **K4 no.** The posts ask for different things (call protection, medication reminders, activities for dementia).
- **K5 weak.**
- **K6 medium.** Niche, but call blocking depends on operating-system and carrier permissions, which limits what a small team can ship.
- **K7 unknown.** Caregiver communities exist. No tested route.
- **G pass, with notes.** Health data needs strict privacy (rule 6). Reminiscence apps built on family photos would conflict with rule 9.

Quotes
- "I would pay a lot of money for a cell phone app that I could install on his phone." (caregiver of person with dementia) https://www.reddit.com/comments/1ai8ncn
- "The scammer is available 24/7 for grandma. Her family isn't." https://www.reddit.com/comments/1teuu3c
- "I have to sit with her during the entire session just to manually load the next appropriate game." https://www.reddit.com/comments/1w266zn

### 4.10 Doomscrolling and feed control
Group: smartphone and social media users (clusters 54, 9).

- **K1 medium.** Cluster 54: 17 posts, 1 pay. Cluster 9: 24 posts, 7 pay. Mostly Reddit.
- **K2 medium.**
- **K3 no.** Everyone with a phone.
- **K4 yes.**
- **K5 medium.**
- **K6 no.** Apple Screen Time, Google Digital Wellbeing and many blocker apps already exist. Controlling other apps' feeds needs platform permissions.
- **K7 weak.**
- **G pass, with note.** One Hacker News quote asks for an app that will "play music" (rule 8: none in the app).

Quotes
- "I feel like screen time limits right now have 0 failure cost." https://www.reddit.com/comments/1swcgu9
- "I would pay for a social network that lets me decide how I consume the content" https://www.reddit.com/comments/1mxfpcd
- "Time lock it based on my prefs so that it respects me as a human being, doesn't try to feed off of me as a data source and I'll pay for that." https://news.ycombinator.com/item?id=48611307

### 4.11 Receipt scanning and bookkeeping
Group: micro-businesses and households (split).

- **K1 medium.** 13 receipt labels plus 8 personal-budget labels (App Store, OMR, Stack Exchange). Trials and subscriptions are the main complaint.
- **K2 medium.**
- **K3 split.** Business bookkeeping and household budgeting are different products.
- **K4 yes.** "Photo of a receipt becomes a bookkeeping entry."
- **K5 strong.** Result in seconds.
- **K6 weak.** Many scanners and accounting tools (lexoffice, sevdesk, bexio). Bank interface failures are a named gap, but they are an integration problem, not a feature we could add alone.
- **K7 weak.**
- **G pass.** Rule 3 differentiator again (competitor shows a $75 fee after one scan).

Quotes
- "Realized you’d have to manually put in every single information, or pay $99/yr for OCR extraction" (App Store) https://apps.apple.com/us/app/smart-receipts-expenses-tax/id905698613
- "Die Schnittstelle zu den Banken funktioniert oft nicht richtig." (OMR, lexoffice) https://omr.com/de/reviews/product/lexoffice/all
- "Is there and app (preferably for Android or Linux) that would support receipt OCR, so I could just take photos of receipts after shopping?" (Stack Exchange, old) https://softwarerecs.stackexchange.com/questions/4194/receipt-ocr-personal-finance-management-app-for-android

### 4.12 Subscription and cancellation tracking
Group: consumers, with a business variant.

- **K1 weak.** Cluster 81 has 6 posts and 1 pay explicit. The web side has 15 "cancellation hidden" labels and 44 "price" labels, but those are complaints about other products, not requests for a tracker.
- **K2 medium.**
- **K3 no.**
- **K4 yes.**
- **K5 medium.**
- **K6 weak.** Bank-linked trackers exist, and bank data access is a regulatory and integration burden.
- **K7 weak.**
- **G pass.** Fits rules 3 and 6 as a position, but better as a trait of any product than as a product.

Quotes
- "add up to hundreds or thousands of dollars a year." (cluster 81) https://www.reddit.com/comments/1lwf4eh
- Snippet only: "The company is purposely hiding the 'cancel subscription' option." (Trustpilot, Invoice 2go) https://se.trustpilot.com/review/invoice.2go.com?page=5
- "Invoice Simple have continued to withdraw money from my account for the passed 7 months." (Trustpilot) https://www.trustpilot.com/review/invoicesimple.com

### 4.13 Ranking of the five strongest

1. **German club administration (4.1).** Most independent sources, one buyer role, already paying and angry about price. Weak on K6 and unknown on K7.
2. **Freelancer invoicing and payment chasing (4.2).** Strongest pain and a rule 3 differentiator. Held back by the Indie Hackers counter-evidence and the crowded field.
3. **Small landlords (4.3).** One clear group, clear "too expensive for just one door" statements, spreadsheets as the rival. US-centric, free tiers.
4. **Booking for solo providers (4.4).** Strongest paying-customer anger (fees, cancellation). Needs one trade chosen.
5. **Trades office software (4.5).** Real pain and price anger, but it fails K4 until cut to one job.

Watch item: family caregivers (4.9) have the strongest pain with the thinnest evidence.

---

## 5. Not pursued

**Big-platform or operating-system dominance (fail K6 and K7 for a small team)**
- 1 LLM hosting, APIs and local models. "Can we have a ChatGPT4 without system prompt? I would pay for that." https://news.ycombinator.com/item?id=39300541 Vendors own the models and the pricing.
- 2 Private browsers. "I'd pay for firefox if they stripped out the google and pocket crap." https://news.ycombinator.com/item?id=41170109 A browser engine is not a small-team product.
- 4 AI coding assistant cost. The limits are set by the model vendors.
- 5 Ad blocking. "I would pay for something that blocks all ads everywhere, including when I'm at a friend's house watching TV or YT and they don't have an ad blocker." https://news.ycombinator.com/item?id=44403635 Free blockers exist and the platforms fight them.
- 25 Private search engines, 14 messaging alternatives (network effect), 17 OS maintenance, 11 travel and navigation, 30 tab/bookmark management, 53 YouTube customization, 51 email clients.
- 23 Phone call blocking. Depends on operating-system and carrier access. The caregiver angle is kept as a watch item (4.9).

**Too broad or no single group (K3, K4)**
- Developer tooling (7, 8, 15, 22, 27, 36, 59, 62, 67): many sub-niches, Hacker News audience, mostly free or open-source competition.
- 24 misc, 88 project management, 35 calendar, 33 notes, 43 documents, 52 habits, 86 wellness: undifferentiated or dominated by large vendors. The web "personal task and note apps" group (21 labels) is the same: Todoist, TickTick, Notion and the platforms' own apps.

**Sampling artifact**
- 6 Startup idea validation and founder support (46 posts, 45 from Reddit). The posts come from idea subreddits, where founders talk about founders. It is not independent demand.

**GRUNDSATZ conflicts**
- Music: 60 music and audio, parts of 12 and 26. Rule 8.
- Images of living beings, women: 13 photo/video editing and photo cleanup (users' photos are mostly of people), 12 streaming and media, 34 fitness (workout video), 80 clothing and outfit planning, 55 and 79 meeting people. Rules 9 and 10. Photo gallery cleanup (quote: "Then you open your Gallery and end up spending 2–3 hours manually going through hundreds or thousands of photos and videos", https://www.reddit.com/comments/1x6i7wo) is an owner decision, since the app would display users' photos.
- Finance and trading: 68 retail investing and trading (rules 2 and 3 on interest and gharar; rule against personal financial advice). 29 personal finance is possible only without interest products and credit scoring.
- Gaming (26): music and depictions in most games.
- Healthcare, mental health (45, 71): sensitive data, regulated, and no evidence of a reachable buyer.

**Religious obligations (rule 11)**
- No cluster in the kept data is a religious-obligation market (see `web/00-coverage.md`: none appeared in kept entries).
- Church and congregation administration apps appear in the web sweep (Realm, Tithe.ly; "Community organization admin", 4 labels). Not pursued: they serve another religion's worship. This is not covered by the 15 rules, so it is an owner decision.

**Weak in round 1, not rejected**
- 20 AI-generated content detection (14 posts, 8 pay explicit): detection accuracy is the product, and the sources do not show it can be met. 21 news overload and 19 language learning: crowded, with no specific gap shown. 16 self-hosted backup: small developer niche.
- Shopify merchants: app-store reviews show merchant anger about app pricing and support (for example LimeSpot, Trustpilot app, Smile). That is evidence about apps merchants buy, not about demand for a conversion check (candidate B).

## 6. Open for round 2

1. **Niche subreddit run.** About 146 subreddits (trades, landlords, teachers, e-commerce, health, German subs), 6 phrases, still running. Check whether it adds Reddit evidence for clusters 4.1 to 4.5, in particular German-language posts on clubs and Handwerk, and landlords outside the US.
2. **Targeted 1-2 star reviews of competitors for the top candidates.** App Store reviews are reachable (public RSS feed). Candidates: WISO MeinVerein, easyVerein, ClubDesk, Vereinsplaner; Invoice Simple, lexoffice, sevdesk; Avail, TurboTenant, Stessa; Booksy, Setmore, Treatwell, Phorest; Plancraft, Tooltime, Hero. Count recurring complaints per product, not single quotes.
3. **Payment evidence.** Record incumbents' price pages and the plans angry reviewers are on. Test the Indie Hackers counter-evidence for the top 2: ask whether anyone in the complaint threads names what they pay now.
4. **Blocked sources.** G2, Capterra, Google Play and the Chrome Web Store were not reachable. Round 2 needs another route or accepts the gap.
5. **Channel (K7).** For each top candidate, find where the group already gathers and whether we can reach it without a following. No source answers this yet.
6. **K3 choice.** For clusters 4.2 and 4.4, pick one trade/country each, so the group is one group.
7. **Classifier recheck.** Re-run the first-450-characters batches with full text for the clusters that make the shortlist.
8. **Candidates A and B from IDEEN.md.** Search separately for explainer-video buyers and shop conversion audits. This round has no direct evidence for either.
