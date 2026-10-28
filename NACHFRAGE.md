# Demand search, rounds 1 and 2

Status: round 2 (2026-10-28). Round 1 was committed earlier the same day. Basis: [IDEEN.md](IDEEN.md) (criteria K1-K8, G), [GRUNDSATZ.md](GRUNDSATZ.md) (15 rules), `quellen/nachfrage/cluster_stats.md`, `quellen/nachfrage/web/`.

## 1. Summary

We searched for stated demand in three places: Hacker News (3,904 posts), Reddit through an archive (round 1: 9,794 posts, round 2: 18,068 more posts from about 146 niche subreddits) and a web sweep of app-store reviews, review sites, Stack Exchange and forums (264 entries). After classification and removal of GRUNDSATZ conflicts and posts that state no need, 2,437 demand posts remain. They fall into 132 clusters (89 from round 1, 43 new in round 2). The web sweep adds problem groups from paying users of existing software.

Round 1 found two different pictures. The highest-scoring clusters (LLM hosting, private browsers, AI coding cost, ad blocking) come mostly from Hacker News developers and privacy-minded users. They are dominated by large platforms and fail K6 and K7 for a small team. The web sweep pointed at small-business and club administration (invoicing, clubs, landlords, booking, trades), where paying customers of existing tools complain about price rises, hidden cancellation, broken apps and missing support.

Round 2 tested the second picture on Reddit niche subreddits. Result:
- Business niches the web sweep pointed at are thin on Reddit. Landlord and rental property management has 5 posts, HVAC and electrician tools 5, therapist practice management 5, truckers and freight 11, church and nonprofit volunteer admin 10, employee time and shift tracking 8. Trades and field service software is the exception that grew (6 to 20 posts).
- Two business clusters are new and sizeable: bookkeeping for small firms (25 posts, 3 pain 3, 12 pay implied) and Shopify and e-commerce merchant tools (39 posts, but fragmented, no pain 3, no explicit payment).
- Language learning became the largest cluster (52 posts, was 17) but it is weak on pain and payment and crowded.
- Round 2 added almost no explicit payment: 25 of 1,038 round-2 posts say "I would pay" (2%), against 274 of the 1,399 earlier posts (20%, mostly Hacker News). Round 2 is Reddit only.
- German subreddits added nothing usable, but this is a method gap, not evidence of absence: round 2 searched them only with the 6 English phrases. A crude search for common German words finds one German-language quote in all 2,437 posts. Round 2 gives no new German club or Handwerk evidence.

Payment evidence stays weak overall. "I'd pay for X" on Hacker News is mostly hypothetical. Indie Hackers titles say complaints are easy to find and payment is not. The strongest payment evidence is indirect: people already pay incumbents and are angry about the price. In round 2 the "pay implied" label (12 of 25 posts in bookkeeping, against 0 of 20 in freelancer invoicing) carries that signal.

The five clusters rated strongest (section 4.16) are now: German club administration, small-firm bookkeeping, freelancer invoicing and payment chasing, trades office software, and booking for solo providers. Small landlords dropped out. None is rated strong on all criteria. No cluster passes K6 and K7 clearly. This search does not confirm or refute candidates A (explainer videos) and B (shop conversion check) from IDEEN.md. The nearest clusters (content creators, lead generation, online sellers, Shopify merchants) are weak. Two Shopify posts touch candidate B (4.13) and that is all.

## 2. Method and limits

**Sources**
- Hacker News via the Algolia API: 3,904 posts since 2024-01-01, found with phrases like "I'd pay for" and "wish there was an app".
- Reddit via the Arctic Shift archive, round 1: 9,794 posts. The archive matches loose words, so only about 4% contained the exact phrase. A full harvest was possible only for r/SideProject, r/Startup_Ideas, r/AppIdeas, r/SomebodyMakeThis and r/Lightbulb, because the archive throttled us. r/SideProject was excluded from the loose-word classification because it is mostly self-promotion.
- Reddit via Arctic Shift, round 2: about 146 niche subreddits (trades, landlords, teachers, health, e-commerce, German subs and others), 6 phrases ("alternative to", "somebody make", "wish there was an app", "is there an app that", "looking for an app", "wish there was a tool"), 1 page per subreddit and phrase pair. It yielded 18,068 new posts. 2,076 of them contained the exact phrase and were classified (Haiku agents, full text read). 1,132 were judged demand-true.
- Web sweep: 264 entries from app-store reviews (137), review sites (52), Stack Exchange (42), English forums (15), German forums and tenders (13) and Indie Hackers (5).
- Not reachable: Reddit directly and PullPush refused automated access. Search engines do not index Reddit for our tools (see `web/reddit-search-*.md`). G2, Capterra, GetApp, Software Advice, trusted.de, Quora, gutefrage.net, Shopify Community, AccountingWeb, Indie Hackers (HTTP 403), Google Play (404), Chrome Web Store (consent wall) and Lobsters (blocked). Details in `web/00-coverage.md`.

**Funnel**
- Round 1: prefilter, then 7,382 posts classified by Haiku agents, 1,474 judged demand-true.
- Round 2: 2,076 classified, 1,132 judged demand-true.
- Together 2,606. Merge removes 169: 47 GRUNDSATZ flags (music, dating, gambling, financing, adult, images of living beings), 4 non-verbatim quotes, 77 bare alternatives, 3 hand exclusions (age-verification spoofer, shadow-library book search) and 38 duplicates. Result: 2,437.
- New merge rule for all rounds: title-only "alternative to X?" posts with no text are dropped (77). They state no need, and the classifiers judged them inconsistently.
- 43 new clusters were added. Old cluster assignments are unchanged. Cluster numbers are re-sorted by strength, so they differ from round 1 (examples: language learning 19 to 1, freelancer invoicing 38 to 42, trades 84 to 64, small landlords 48 to 60).

**Limits**
- 131 phrase and subreddit pairs of the round-2 run failed with HTTP 500 and are being retried. They are not in this document.
- Round 2 took 1 page per pair. Large subreddits were therefore sampled, not harvested.
- One round-1 classifier read only the first ~450 characters of posts in 4 batches. A recheck found 23 missed demand posts and fixed them. Other batches may have similar small misses. Round 2 read full text.
- "Pay explicit" on Hacker News is mostly hypothetical ("I'd pay for X") in reply threads. It is a weak signal. "Pay implied" is the classifier's label for posts where the poster already pays for or budgets for a tool. It is not in cluster_stats.md. The counts in this document come from `demand.jsonl` and `clusters.json`.
- Indie Hackers counter-evidence (`web/indiehackers.md`): complaints are easy to find, payment is not. Both titles are snippet only (page returned HTTP 403).
- Bias: Hacker News data skews to developers and privacy-minded consumers. The web sweep skews to German club, craft/invoicing, landlord and Shopify software, because those sites were reachable. Round 2 skews to English-language subreddits.
- Reddit "score" in cluster_stats is the post's upvote count. Posts in idea subreddits are often founders describing a problem they want to build for. The "group" column is the group the poster describes, not a verified customer. Examples: 14 of 21 posts in small business operations come from r/Startup_Ideas.
- Many Stack Exchange entries date from 2009-2016. Their signal is view count. SoftGuide tenders are old and mostly closed (one open tender, 26/3608).
- Web counts below are label mentions. An entry can carry a domain label and a problem label. The 264 entries carry 387 labels.
- Cluster quotes in cluster_stats.md show 6 posts per cluster. Counts in this document cover all posts of the cluster, quotes only the 6 shown.

## 3. Top clusters

### 3.1 Reddit and Hacker News (from cluster_stats.md)

Strength = posts + 3 x pay explicit + 3 x pain 3. The first 30 real clusters are listed. Cluster 26 ("misc", 29) is skipped. "Platform" marks clusters dominated by a few large vendors or by the operating system.

| # | Cluster | Group | Posts | Pay explicit | Pain 3 | HN / Reddit | Strength | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | Language learning tools | language learners | 52 | 8 | 0 | 8 / 44 | 76 | Crowded; split (4.15) |
| 2 | LLM hosting, APIs and local models | developers / privacy-minded AI users | 36 | 13 | 0 | 20 / 16 | 75 | Platform |
| 3 | Alternative and private browsers | privacy-conscious browser users | 23 | 15 | 0 | 19 / 4 | 68 | Platform |
| 4 | Travel planning, navigation and local discovery | travellers | 49 | 4 | 1 | 4 / 45 | 64 | Platform |
| 5 | Calendar, scheduling and task reminders | busy professionals | 57 | 2 | 0 | 3 / 54 | 63 | Platform; broad |
| 6 | Photo, video and creative editing tools | photographers / phone users | 42 | 5 | 1 | 11 / 31 | 60 | Platform; G |
| 7 | Job search and application automation | job seekers / recruiters | 32 | 5 | 4 | 5 / 27 | 59 | Crowded |
| 8 | Startup idea validation and founder support | founders / indie hackers | 47 | 2 | 1 | 1 / 46 | 56 | Sampling artifact |
| 9 | AI coding assistant cost, limits and context loss | developers using AI coding tools | 26 | 10 | 0 | 18 / 8 | 56 | Platform |
| 10 | Ad blocking and ad-free services | consumers | 17 | 13 | 0 | 16 / 1 | 56 | Platform |
| 11 | Voice dictation, speech-to-text and text-to-speech | dictation / audio users | 28 | 9 | 0 | 14 / 14 | 55 | Crowded |
| 12 | Developer tooling: editors, debuggers and languages | software developers | 33 | 6 | 1 | 28 / 5 | 54 | Too broad |
| 13 | Personal finance and expense tracking | individuals / households | 39 | 4 | 0 | 4 / 35 | 51 | Split; G |
| 14 | Home cooking, recipes and meal planning | home cooks | 37 | 4 | 0 | 1 / 36 | 49 | Broad, crowded |
| 15 | Social feed control and de-algorithmization | social media users | 28 | 7 | 0 | 8 / 20 | 49 | Platform |
| 16 | Developer tooling: databases, APIs and data | software developers | 25 | 8 | 0 | 18 / 7 | 49 | Too broad |
| 17 | Student study and teaching tools | students | 36 | 3 | 0 | 3 / 33 | 45 | Broad, crowded |
| 18 | Private messaging and social network alternatives | privacy-minded / community users | 27 | 6 | 0 | 13 / 14 | 45 | Network effect |
| 19 | Self-hosted storage, backup and file sync | self-hosters / families | 24 | 6 | 1 | 16 / 8 | 45 | Niche developers |
| 20 | Mac and Windows system performance and maintenance | Mac / Windows / Linux users | 24 | 6 | 1 | 13 / 11 | 45 | Platform |
| 21 | Fitness, sports and workout tracking | gym-goers / athletes | 44 | 0 | 0 | 1 / 43 | 44 | G (workout video) |
| 22 | Document, PDF and spreadsheet tools | office / knowledge workers | 34 | 1 | 2 | 9 / 25 | 43 | Broad, crowded |
| 23 | Streaming, TV and media servers | streaming viewers / media server users | 25 | 6 | 0 | 7 / 18 | 43 | Platform; G |
| 24 | Notes, journaling and personal knowledge management | note-takers / knowledge workers | 30 | 4 | 0 | 7 / 23 | 42 | Crowded |
| 25 | Phone calls: spam blocking, screening and handling | phone users | 21 | 5 | 2 | 7 / 14 | 42 | Platform (OS, carriers) |
| 27 | Android and phone app tools | phone users | 26 | 5 | 0 | 11 / 15 | 41 | Platform |
| 28 | E-commerce store apps and Shopify merchant tools | online store owners / Shopify merchants | 39 | 0 | 0 | 0 / 39 | 39 | Fragmented (4.13) |
| 29 | Developer tooling: git, CI and code review | software developers | 18 | 7 | 0 | 16 / 2 | 39 | Too broad |
| 30 | Frontend and UI building tools | web / frontend developers | 18 | 6 | 1 | 10 / 8 | 39 | Too broad |
| 31 | AI-generated content detection and filtering | social media / web users, website owners | 15 | 8 | 0 | 10 / 5 | 39 | Accuracy |

Observations
- No cluster has more than 4 posts with pain 3. Four clusters have 3 or more: job search (4), freelancer invoicing (4), bookkeeping (3) and small business operations (3). Clusters with high "pay explicit" counts are Hacker News heavy.
- Round 2 pushed Reddit-only consumer clusters up the list on post counts alone: language learning (1), travel (4), calendar (5), photo and video (6). Their pay explicit counts are 2 to 8 and pain 3 counts 0 to 1.
- Business clusters with real money at stake still sit lower: bookkeeping (35, strength 37), freelancer invoicing (42, 35), small business operations (52, 30), community and club admin (61, 25), trades (64, 23). Section 3.2 lists all business and professional clusters.

### 3.2 Niche and business clusters (all clusters whose group is a business or professional role)

Selection: group is a business owner, employer, tradesperson, bookkeeper, teacher, therapist, recruiter or similar. Developer, creator, hobbyist and consumer clusters are left out, as are mixed groups (for example cluster 60 "homeowners / renters / landlords", 19 posts, 1 pay explicit, 1 pain 3). "Pay implied" is from `demand.jsonl`.

| # | Cluster | Group | Posts | Pay explicit | Pay implied | Pain 3 | Strength |
|---|---|---|---|---|---|---|---|
| 28 | E-commerce store apps and Shopify merchant tools | online store owners / Shopify merchants | 39 | 0 | 9 | 0 | 39 |
| 35 | Bookkeeping, accounting and tax filing for small firms | bookkeepers / accountants | 25 | 1 | 12 | 3 | 37 |
| 42 | Freelancer invoicing, payment chasing and client admin | freelancers / solo workers | 20 | 1 | 0 | 4 | 35 |
| 52 | Small business operations and booking software | small business owners | 21 | 0 | 0 | 3 | 30 |
| 50 | Lead generation and sales outreach | sales teams / founders | 24 | 0 | 0 | 2 | 30 |
| 51 | IT admin and MSP tooling | sysadmins / MSPs | 24 | 0 | 3 | 2 | 30 |
| 61 | Community, club and event organizer admin | community and club organizers | 19 | 1 | 1 | 1 | 25 |
| 64 | Field service and trades business software | tradespeople / field service owners | 20 | 0 | 2 | 1 | 23 |
| 69 | Recruiting, ATS and HR admin | recruiters / HR | 13 | 1 | 4 | 2 | 22 |
| 70 | AI and automation for small-business admin | small business owners / founders | 12 | 1 | 1 | 2 | 21 |
| 73 | Amazon, dropshipping and print-on-demand sellers | Amazon / dropship / POD sellers | 14 | 1 | 1 | 1 | 20 |
| 74 | Social media management and influencer marketing | social media managers / marketers | 14 | 1 | 0 | 1 | 20 |
| 72 | SEO, PPC and web analytics for marketers | SEO / PPC marketers | 20 | 0 | 1 | 0 | 20 |
| 81 | Classroom and teacher tools | teachers | 15 | 1 | 0 | 0 | 18 |
| 101 | Truckers and freight logistics | truck drivers / logistics | 11 | 0 | 1 | 0 | 11 |
| 107 | Church and nonprofit volunteer admin | church / nonprofit staff and volunteers | 10 | 0 | 1 | 0 | 10 |
| 111 | Business phone numbers, call centers and VoIP | small business owners | 9 | 0 | 3 | 0 | 9 |
| 115 | Employee time, shift and mileage tracking | employers / hourly workers | 8 | 0 | 0 | 0 | 8 |
| 116 | Real estate agents and home buyers | realtors / home buyers | 8 | 0 | 2 | 0 | 8 |
| 118 | Landlord and rental property management | landlords / property managers | 5 | 0 | 1 | 1 | 8 |
| 122 | Professional exam prep and CE tracking | nurses / licensed professionals | 7 | 0 | 0 | 0 | 7 |
| 128 | HVAC and electrician technical tools | HVAC techs / electricians | 5 | 0 | 0 | 0 | 5 |
| 130 | Therapist practice management | therapists | 5 | 0 | 2 | 0 | 5 |

Reading
- Thin on Reddit, although the web sweep pointed at them: landlord and rental property management (5), HVAC and electrician tools (5), therapist practice management (5), truckers and freight (11), church and nonprofit volunteer admin (10), employee time and shift tracking (8). None has more than 1 pain 3 post or any explicit payment.
- Bookkeeping stands out for payment: 12 of 25 posts are pay implied, 18 come from r/Bookkeeping.
- E-commerce merchants have 39 posts but only 2 subreddits (r/shopify 28, r/ecommerce 11), 0 explicit and 0 pain 3.
- Lead generation (24) and small business operations (21) are mostly idea-subreddit pitches.

### 3.3 Web sweep problem groups (264 entries, 387 labels)

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

Scale: strong / medium / weak / no. "Unknown" means no source speaks to it. Quotes are copied from `cluster_stats.md` or `web/*.md` unchanged. Where a quote is a search snippet, that is stated. Sections 4.1 to 4.12 are the round-1 assessments, re-checked against the 2,437 posts. Where round 2 changed the evidence, the K1 line says so. Sections 4.13 to 4.15 are new.

### 4.0 Overview

| # | Cluster (source) | K1 | K2 | K3 | K4 | K5 | K6 | K7 | G |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Club and association admin, German (web 18 + cluster 61) | strong | medium | yes | yes | medium | weak | unknown | pass, 3 notes |
| 2 | Freelancer invoicing and payment chasing (cluster 42 + web invoicing 21) | medium | strong | split | yes | medium | weak | unknown | pass, 2 notes |
| 3 | Small landlords (web 8 + clusters 60, 118) | medium, web only | medium | yes | yes | medium | weak | medium | pass |
| 4 | Booking for solo providers and small practices (web 9 + clusters 52, 130) | strong | medium | split | yes | medium | weak | weak | pass, 1 note |
| 5 | Trades and craft office software (cluster 64 + web) | medium | medium | yes | no | medium | weak | weak | pass |
| 6 | School, daycare and teacher apps (web 20 + cluster 81) | medium | medium | split | medium | weak | weak | no | flag (rule 9) |
| 7 | Job search automation (cluster 7) | strong | medium | broad | yes | medium | weak | medium | pass, 1 note |
| 8 | Offline voice dictation (cluster 11) | medium | weak | no | yes | strong | weak | weak | pass |
| 9 | Family caregivers: elder care, scam calls (clusters 68, 25) | weak | strong | yes | no | weak | medium | unknown | pass, 2 notes |
| 10 | Doomscrolling and feed control (clusters 40, 15) | medium | medium | no | yes | medium | no | weak | pass, 1 note |
| 11 | Receipt scanning and bookkeeping, web side (web 13) | medium | medium | split | yes | strong | weak | weak | pass |
| 12 | Subscription and cancellation tracking (cluster 105 + web) | weak | medium | no | yes | medium | weak | weak | pass |
| 13 | Shopify and e-commerce merchant tools (cluster 28) | medium | weak | yes | no | medium | weak | unknown | pass |
| 14 | Small-firm bookkeeping (cluster 35) | strong | medium | yes | medium | medium | weak | medium | pass, 3 notes |
| 15 | Language learning (cluster 1) | medium | weak | split | yes | medium | weak | unknown | pass, 3 notes |

Order of strength is not the table order. Section 4.16 gives the ranking.

---

### 4.1 Club and association administration (German)
Group: boards, treasurers and secretaries of small clubs in Germany/Austria/Switzerland.

- **K1 strong.** 18 web entries carry this label, from OMR reviews of five products (VereinsGuru, Vereinsplaner, WISO MeinVerein, easyVerein, ClubDesk), forum threads and SoftGuide tenders including one open tender (26/3608, 6,000 records). Reddit side is small (cluster 61: 19 posts after round 2, 1 pay explicit, 1 pay implied). The 5 round-2 posts in that cluster come from event, church, web-community and agency contexts; none is a German club. Round 2 therefore adds no German club evidence (see section 2). Caveat: the web sweep was biased toward German clubs because those sites were reachable.
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

- **K1 medium.** Cluster 42: 20 posts (13 in round 1), pain 3 = 4, pay explicit 1, pay implied 0. The 7 round-2 posts are pain 1 to 2 and name no payment. Web: 21 invoicing labels, most from paying users of Invoice Simple, Invoice 2go, Invoice Maker, lexoffice, sevdesk. Counter-evidence from Indie Hackers (below): a founder found 71 people complaining and none willing to pay.
- **K2 strong.** Money lost. Posts claim "$2-5K/year" lost to late clients. Those figures are the posters' claims in idea posts and are not verified.
- **K3 split.** "Freelancers" is broad. Needs one trade and one country.
- **K4 yes.** "Send the invoice, chase the payment."
- **K5 medium.** The reminder helps at once. Cash arrival does not.
- **K6 weak.** Very crowded. The visible incumbent failures (price increases, hidden cancellation, no support, app down at payment time) are the only opening.
- **K7 unknown.**
- **G pass, with notes.** Rule 3 is a real differentiator here: competitor reviews are full of hidden cancellation and trial charges. Rule 2 applies to the dunning feature (no default interest, as in 4.1).

Quotes
- "freelancers losing $2-5K/year on clients who ghost invoices." (cluster 42) https://www.reddit.com/comments/1r73tui
- "lost a partnership because I forgot to followup in time" (cluster 42) https://www.reddit.com/comments/1sqtcfr
- "Right now I'm juggling between Notion, Google Docs, and email, but it feels messy." (cluster 42, freelancer, round 2) https://www.reddit.com/comments/1hflwgv
- "They are now wanting to charge me £60 for 3 invoices per month when it used to be £20 every year for unlimited." (Trustpilot, 1 star) https://www.trustpilot.com/review/invoicesimple.com
- Counter-evidence, snippet only (title): "I found 71 people complaining about the same problem. Not one would pay to fix it." https://www.indiehackers.com/post/i-found-71-people-complaining-about-the-same-problem-not-one-would-pay-to-fix-it-209e2bf18e

### 4.3 Small landlords
Group: landlords with about 1 to 30 units, mostly US in the sources (BiggerPockets); one German tender and one 2004 thread.

- **K1 medium, web only.** 8 web entries, 5 BiggerPockets threads with 6 to 37 replies and up to 2,069 views. Cluster 60 (home, property, tenants, landlords) has 19 mixed posts (1 pay explicit); most are tenants or homeowners, not landlords. Round 2 adds the dedicated landlord cluster 118: only 5 posts (r/Landlord 2, r/PropertyManagement 3), 0 pay explicit, 1 pay implied, 1 pain 3. The Reddit side stays thin, so K1 rests on the BiggerPockets threads only.
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
- "I have houses to rent and looking for an app that can save me some dollar on hiring an admin." (cluster 118, landlord, round 2) https://www.reddit.com/comments/1t72hf6
- "Currently my office is calculating these increases per space, every month." (cluster 118, mobile home park operator, pain 3, round 2) https://www.reddit.com/comments/1ibqc9v
- "the more advanced systems (like bildium) will have you spend more time learning the software than anything else." https://www.biggerpockets.com/forums/899/topics/1259131-which-property-management-software-is-good-to-use-just-starting-out

### 4.4 Booking for solo providers and small practices
Group: hairdressers, therapists, physio practices and similar one-to-few-person businesses.

- **K1 strong.** 9 web labels. Booksy's Trustpilot profile alone shows 16,583 reviews; Setmore, Dikidi, Beautinda, Salonist, Phorest and SoftGuide tenders (physio, therapy centre) add more. Cluster 52 (small business operations and booking software): 21 posts, pay none, pain 3 = 3, but 14 of the 21 come from r/Startup_Ideas, so they are mostly pitches. Round 2 adds cluster 130 (therapist practice management): 5 posts, all from r/therapists, 2 pay implied.
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
- "Simple Practice is so very pricey." (cluster 130, therapist, pay implied, round 2) https://www.reddit.com/comments/1c4tqur
- "Too many cancellations because clients reply to those reminders." (App Store) https://apps.apple.com/us/app/setmore-appointment-scheduling/id665859578

### 4.5 Trades and craft office software
Group: small Handwerk and trades businesses (plumbing, electrical, HVAC, carpentry, pressure washing).

- **K1 medium.** Cluster 64: 20 posts (6 in round 1), pay explicit 0, pay implied 2, pain 3 = 1, from 10 subreddits (r/Contractor 5, r/AppIdeas 4). Reddit scores of 57 and 71 show interest, but both are idea-subreddit pitches. Round 2 adds 14 posts, many from tradespeople and office staff themselves. The technical-tool cluster 128 (HVAC and electricians) has only 5 posts and no payment signal. Web: OMR reviews of Plancraft, Tooltime, Hero and OpenHandwerk, plus two old SoftGuide tenders (15/178, 15/269).
- **K2 medium.** Forgotten invoices, photos and job tracking.
- **K3 yes.** One group in principle.
- **K4 no.** Quotes, invoices, photos, time tracking and crew are five jobs. Needs cutting to one (for example only before/after photo reports).
- **K5 medium.**
- **K6 weak.** Specialist incumbents with trade-specific features (GAEB, wholesaler prices). Reviewers complain about price rises and ignored support.
- **K7 weak.** No known channel to tradespeople.
- **G pass.**

Quotes
- "there is a plumber right now who is owed a few thousand dollars because he finished a job, meant to send the second invoice, got called to the next emergency and forgot." (cluster 64) https://www.reddit.com/comments/1wisa84
- "Taking before-after photos and organizing them and sending them to the client takes up so much time." (cluster 64, pressure washing owner) https://www.reddit.com/comments/1x8dmwr
- "working out of a notebook is starting to not be manageable" (cluster 64, electrician, round 2) https://www.reddit.com/comments/1oxvcfa
- "Preiserhöhung im übertriebenen Maße." (OMR, Plancraft, owner of construction business) https://omr.com/de/reviews/product/plancraft/all

### 4.6 School, daycare and teacher apps
Group: parents, teachers, daycare staff. The buyer is usually the institution.

- **K1 medium.** 20 web labels (10 school/daycare, 10 teacher), all App Store reviews and one SoftGuide tender (Kita, 17/750). Cluster 81 (teacher tools): 15 posts after round 2 (9 new, mostly r/Teachers), 1 pay explicit.
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
Group: job seekers (Reddit side 27 of 32 posts).

- **K1 strong.** 32 posts (3 new in round 2), 5 pay explicit, pain 3 = 4. Ties with freelancer invoicing for the most pain 3 posts of any cluster. Round 2 changes little here.
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

- **K1 medium.** 28 posts (10 new in round 2, all Reddit), 9 pay explicit (none added in round 2), 14 from Hacker News. Hypothetical payment.
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
Group: adult children and carers of elderly parents or people with dementia. Two clusters (68 elder care, 13 posts; 25 phone calls, 21 posts) that share this group only in part.

- **K1 weak.** Small counts. Cluster 68 has 1 pay explicit (the quote below); cluster 25 has 5, not checked for caregivers specifically.
- **K2 strong.** Pain 3 = 2 in each cluster. Carers give up careers, sit through every session.
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
Group: smartphone and social media users (clusters 40, 15).

- **K1 medium.** Cluster 40: 32 posts, 1 pay. Cluster 15: 28 posts, 7 pay. Mostly Reddit.
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

### 4.11 Receipt scanning and bookkeeping (web side)
Group: micro-businesses and households (split). The Reddit side of business bookkeeping is a separate, stronger cluster, assessed in 4.14.

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

- **K1 weak.** Cluster 105 has 8 posts and 1 pay explicit. The web side has 15 "cancellation hidden" labels and 44 "price" labels, but those are complaints about other products, not requests for a tracker.
- **K2 medium.**
- **K3 no.**
- **K4 yes.**
- **K5 medium.**
- **K6 weak.** Bank-linked trackers exist, and bank data access is a regulatory and integration burden.
- **K7 weak.**
- **G pass.** Fits rules 3 and 6 as a position, but better as a trait of any product than as a product.

Quotes
- "add up to hundreds or thousands of dollars a year." (cluster 105) https://www.reddit.com/comments/1lwf4eh
- Snippet only: "The company is purposely hiding the 'cancel subscription' option." (Trustpilot, Invoice 2go) https://se.trustpilot.com/review/invoice.2go.com?page=5
- "Invoice Simple have continued to withdraw money from my account for the passed 7 months." (Trustpilot) https://www.trustpilot.com/review/invoicesimple.com

### 4.13 Shopify and e-commerce merchant tools (new in round 2)
Group: Shopify and other online store owners (cluster 28).

- **K1 medium.** 39 posts, all from round 2, from only two subreddits (r/shopify 28, r/ecommerce 11). 0 pay explicit, 9 pay implied, 0 pain 3, 29 of 39 at pain 2 or higher. The 9 pay-implied posts are merchants who already pay for an app and want a cheaper or better one.
- **K2 weak.** Pain 2 at most. Asks are feature gaps and price (subscriptions, returns and exchanges, shipping cost, reporting, store search), not money lost.
- **K3 yes.** One group, one buyer role.
- **K4 no.** The 39 posts ask for 39 different things. No single problem recurs often enough to be one product. The cluster text lists subscriptions, returns, shipping, reporting, upsells and store search.
- **K5 medium.**
- **K6 weak.** Shopify is the platform and its app marketplace is the incumbent for every ask (Shopify named 19 times, Recharge 2). Each ask is a feature the existing apps partly cover.
- **K7 unknown.** The group is visible on r/shopify and r/ecommerce. No tested route.
- **G pass.** Rule 3 and rule 4 matter for apps in this field (trial and pricing clarity). Rule 15: selling to all merchants is allowed as long as the product is halal.
- **Link to candidate B (conversion check).** Two posts touch it and no more: a game shop owner who lacks visibility into the checkout experience (https://www.reddit.com/comments/1by9sak) and a merchant asking whether the standard Shopify reports show conversion per traffic source (https://www.reddit.com/comments/190uvf0). Both are single posts at pain 1 to 2 with no payment signal. Candidate B stays unconfirmed.

Quotes
- "Or does anyone know if there's another shipping software that would give the true cost of sending a letter-size flat envelope?" (stationery shop owner) https://www.reddit.com/comments/1bddruw
- "My experience has been pretty frustrating and I am looking for an alternative." (Shopify seller with Kickstarter, pay implied) https://www.reddit.com/comments/1b7iy0f
- "What are your favorite subscription management services?" (Shopify subscription merchant) https://www.reddit.com/comments/1atn84p

### 4.14 Small-firm bookkeeping (new in round 2)
Group: bookkeepers and in-house accountants of small firms (cluster 35). The tools named (QuickBooks Online 6, QuickBooks 5, Xero 4, QuickBooks Desktop 3, Wave 2, Dext 2) and the 1099 and W-2 tasks point to the US.

- **K1 strong.** 25 posts, all from round 2. 18 come from r/Bookkeeping, 3 from r/Accounting, the other 4 from three other subreddits. 1 pay explicit, 12 pay implied, 3 pain 3, 18 of 25 at pain 2 or higher. The posters are professionals who pay for the tools already, and the pay-implied share is the highest of any business cluster (12 of 25; e-commerce 9 of 39, trades 2 of 20, freelancer invoicing 0 of 20). Caveat: one community supplies most posts, and "pay implied" is a classifier label, not a stated price.
- **K2 medium.** Time and price. One bookkeeper loses days each month to data entry. Price rises are named repeatedly. The posts do not describe lost money.
- **K3 yes.** Bookkeepers of small firms. The buyer and the user are the same professional.
- **K4 medium.** The cluster holds several jobs (cheaper QuickBooks, receipt and bill entry, 1099 filing, payroll). It needs one, for example "client receipts become spreadsheet or ledger entries".
- **K5 medium.**
- **K6 weak.** QuickBooks, Xero, Wave and Dext are all named and are the targets of the complaints. A small team cannot match a full accounting suite. The opening is one job done cheaper. Related: the web-side receipt scanners (4.11).
- **K7 medium.** The group gathers visibly and in volume on r/Bookkeeping. We have no tested route and no following.
- **G pass, with notes.** (a) Tax and filing accuracy: no claims like "error-free" or "audit-proof" without proof (rules 1, 5). (b) No loan, interest or financing features (rule 2; owner to confirm that books recording interest are not a conflict). (c) Client financial data needs strict privacy and no hidden tracking (rule 6).

Quotes
- "Each month I spend literal DAYS organizing, scanning and inputting their expenses into a spreadsheet" (small company accountant, pain 3, pay explicit) https://www.reddit.com/comments/1ijzqx4
- "We are getting priced out with their insane price hikes" (bookkeeper for small business, pain 3, pay implied) https://www.reddit.com/comments/1j9mb0p
- "QB's complexity, subscription nightmare, and drive to get everyone into the cloud is making bookkeeping and accounting a nightmare activity." (bookkeeper, score 14) https://www.reddit.com/comments/1clzuma

### 4.15 Language learning (largest cluster after round 2)
Group: language learners (cluster 1). Japanese has its own cluster (79, 16 posts) and is not counted here.

- **K1 medium.** 52 posts (17 in round 1), 44 from Reddit (31 from r/languagelearning) and 8 from Hacker News. 8 pay explicit (7 Hacker News, 1 Reddit), 1 pay implied, 0 pain 3, 25 of 52 at pain 2 or higher. The explicit payment is the hypothetical kind ("I would pay for"). Many posts are "alternative to" requests for Duolingo, Pimsleur, LingQ, Language Reactor or Tandem.
- **K2 weak.** Pain 2 at most. Asks are for better pronunciation feedback, readable texts for small languages, offline translation, subtitle tools. Nothing is lost if they stay unmet.
- **K3 split.** Language, level and skill (speaking, reading, listening) are different products. One language and level would have to be chosen.
- **K4 yes.** For example "speak and get pronunciation feedback".
- **K5 medium.**
- **K6 weak.** Duolingo (9 mentions), Anki (4), Language Reactor (3), Pimsleur (2), LingQ (2), Google Translate (2) are named. The gaps people name (pronunciation, small languages, offline, no tracking) are buildable with current models, but others can ship the same.
- **K7 unknown.** The group gathers visibly on r/languagelearning. No tested route.
- **G pass, with notes.** (a) Rule 11: an Arabic-learning product is excluded as a market gap (religious obligation). General language tools are not excluded. No post in the set asks for Arabic learning; the only Arabic mention is an Arabic speaker asking for an offline translation app (https://www.reddit.com/comments/190vwo1). (b) Rule 8: no songs or music-based lessons. Voice and sounds are allowed. (c) Rules 9, 10: no mascots, photos or avatars of people. Recorded or synthetic voices need an owner decision, as in 4.8.

Quotes
- "I would pay for an equivalent app that helped my German pronunciation" (German learner, Hacker News) https://news.ycombinator.com/item?id=42393548
- "This is such an amazing idea and I would pay for it right now as finding text for A1-A2 is virtually impossible if your language is not incredibly popular" (language learner, Hacker News) https://news.ycombinator.com/item?id=43925345
- "I am trying to give a subscription to an ESL app as a gift" (gift giver for a newly arrived refugee, Reddit, pay explicit) https://www.reddit.com/comments/1bygnmj

### 4.16 Ranking of the five strongest

1. **German club administration (4.1).** Unchanged at first place. Most independent sources (18 web entries, five products), one buyer role, already paying and angry about price. Weak on K6 and unknown on K7. Round 2 adds nothing for or against: the 5 new Reddit posts in the cluster are not German clubs, and German subreddits yielded almost nothing. The evidence is still web-only and German-only.
2. **Small-firm bookkeeping (4.14).** New, enters at second place. The only cluster that combines a professional buyer, a pay-implied share of 12 of 25 and 3 pain 3 posts, with a community (r/Bookkeeping) that talks about it in volume. Held back by QuickBooks and Xero (K6), a US focus and K4 (needs one job).
3. **Freelancer invoicing and payment chasing (4.2).** Down from second place. Pain is still the strongest (4 posts at pain 3, lost money), and rule 3 is still a differentiator. Round 2 adds 7 posts, all at pain 1 to 2 with no payment, and the Indie Hackers counter-evidence stands. 0 of 20 posts are pay implied.
4. **Trades office software (4.5).** Up from fifth place. The cluster grew from 6 to 20 posts, from 10 subreddits, with 2 pay implied and tradespeople describing the pain themselves (r/Contractor 5). Still fails K4 until cut to one job, and K7 is weak.
5. **Booking for solo providers (4.4).** Down one place. Round 2 adds only the therapist cluster (5 posts, 2 pay implied, price anger about Simple Practice), which supports the price-anger pattern but is small. Cluster 52 is mostly idea-subreddit pitches. Needs one trade chosen.

Dropped out of the five: **small landlords (4.3).** Down from third place. The dedicated Reddit cluster has 5 posts (1 pay implied, 1 pain 3) and cluster 60 is mostly tenants and homeowners, so K1 rests on BiggerPockets alone. It stays a candidate, not a leader.

Considered and not in the five:
- **Language learning (4.15)** has the highest strength score in the table (76) but 0 pain 3, hypothetical payment, a split group and Duolingo-class incumbents.
- **Shopify merchant tools (4.13)** has 39 posts but no recurring problem (K4), no pain 3 and no explicit payment.

Watch item: family caregivers (4.9) still have the strongest pain with the thinnest evidence (cluster 68 grew from 8 to 13 posts).

---

## 5. Not pursued

Cluster numbers are the round-2 numbers.

**Big-platform or operating-system dominance (fail K6 and K7 for a small team)**
- 2 LLM hosting, APIs and local models. "Can we have a ChatGPT4 without system prompt? I would pay for that." https://news.ycombinator.com/item?id=39300541 Vendors own the models and the pricing.
- 3 Private browsers. "I'd pay for firefox if they stripped out the google and pocket crap." https://news.ycombinator.com/item?id=41170109 A browser engine is not a small-team product.
- 9 AI coding assistant cost. The limits are set by the model vendors.
- 10 Ad blocking. "I would pay for something that blocks all ads everywhere, including when I'm at a friend's house watching TV or YT and they don't have an ad blocker." https://news.ycombinator.com/item?id=44403635 Free blockers exist and the platforms fight them.
- 38 Private search engines, 18 messaging alternatives (network effect), 20 OS maintenance, 4 travel and navigation, 48 tab/bookmark management, 65 YouTube customization, 56 email clients.
- 25 Phone call blocking. Depends on operating-system and carrier access. The caregiver angle is kept as a watch item (4.9).

**Too broad or no single group (K3, K4)**
- Developer tooling (12, 16, 29, 30, 45, 57, 75, 84, 95): many sub-niches, Hacker News audience, mostly free or open-source competition.
- 26 misc, 86 project management, 5 calendar and reminders (57 posts, 2 pay explicit, 0 pain 3), 24 notes, 22 documents, 46 habits, 114 wellness: undifferentiated or dominated by large vendors. The web "personal task and note apps" group (21 labels) is the same: Todoist, TickTick, Notion and the platforms' own apps.
- 50 Lead generation and sales outreach (24 posts) and 52 small business operations (21 posts): mostly idea-subreddit pitches (22 of 24 and 18 of 21 from r/Startup_Ideas, r/AppIdeas or r/SomebodyMakeThis), no payment signal.

**Sampling artifact**
- 8 Startup idea validation and founder support (47 posts, 46 from Reddit). The posts come from idea subreddits, where founders talk about founders. It is not independent demand.

**GRUNDSATZ conflicts**
- Music: 66 music and audio, parts of 23 and 44. Rule 8.
- Images of living beings, women: 6 photo/video editing and photo cleanup (users' photos are mostly of people), 23 streaming and media, 21 fitness (workout video), 106 clothing and outfit planning, 80 and 93 meeting people. Rules 9 and 10. Photo gallery cleanup (quote: "Then you open your Gallery and end up spending 2–3 hours manually going through hundreds or thousands of photos and videos", https://www.reddit.com/comments/1x6i7wo) is an owner decision, since the app would display users' photos.
- Finance and trading: 96 retail investing and trading (rules 2 and 3 on interest and gharar; rule against personal financial advice). 13 personal finance is possible only without interest products and credit scoring.
- Gaming (44): music and depictions in most games.
- Healthcare, mental health (63, 92): sensitive data, regulated, and no evidence of a reachable buyer.

**Religious obligations (rule 11)**
- No cluster in the kept data is a religious-obligation market (see `web/00-coverage.md`: none appeared in kept entries). Language learning has no Arabic-learning request (4.15).
- Church and congregation administration apps appear in the web sweep (Realm, Tithe.ly; "Community organization admin", 4 labels). Round 2 adds Reddit cluster 107, church and nonprofit volunteer admin: 10 posts, 0 pay explicit, 1 pay implied. Not pursued: they serve another religion's worship. This is not covered by the 15 rules, so it is an owner decision.

**Thin on Reddit in round 2, not rejected**
- 118 Landlord and rental property management (5), 128 HVAC and electrician tools (5), 130 therapist practice management (5), 101 truckers and freight (11), 115 employee time and shift tracking (8). The web sweep pointed at these groups, but Reddit shows little. They are not proof that no demand exists. The archive sampled 1 page per pair, and these groups may sit elsewhere (forums, Facebook groups, trade media).

**Weak, not rejected**
- 31 AI-generated content detection (15 posts, 8 pay explicit): detection accuracy is the product, and the sources do not show it can be met. 37 news overload: crowded, with no specific gap shown. 19 self-hosted backup: small developer niche.
- Shopify merchants are assessed in 4.13. App-store reviews show merchant anger about app pricing and support (for example LimeSpot, Trustpilot app, Smile). That is evidence about apps merchants buy, not about demand for a conversion check (candidate B).

## 6. Open

1. **Failed round-2 pairs.** 131 phrase and subreddit pairs failed with HTTP 500 and are being retried. When they arrive, merge them and re-run `cluster_stats.md`. Check first whether they include the thin groups (landlords, HVAC, therapists, trades) and any German subreddits.
2. **Targeted 1-2 star reviews of competitors for the top candidates.** App Store reviews are reachable (public RSS feed). Candidates: WISO MeinVerein, easyVerein, ClubDesk, Vereinsplaner; QuickBooks Online, Xero, Dext, Wave; Invoice Simple, lexoffice, sevdesk; Plancraft, Tooltime, Hero; Booksy, Setmore, Treatwell, Phorest, Simple Practice. Count recurring complaints per product, not single quotes. Landlord apps (Avail, TurboTenant, Stessa) are lower priority after round 2.
3. **Payment evidence.** Record incumbents' price pages and the plans angry reviewers are on. Test the Indie Hackers counter-evidence for the top 3: ask whether anyone in the complaint threads names what they pay now. For bookkeeping, check what the "pay implied" posters pay (QuickBooks Online and Dext price pages).
4. **Blocked sources.** G2, Capterra, Google Play and the Chrome Web Store were not reachable. Another route is needed or the gap stands.
5. **Reaching the group (K7).** For each top candidate, find where the group already gathers and whether we can reach it without a following. Known so far: bookkeepers on r/Bookkeeping (18 posts), tradespeople on r/Contractor (5), Shopify merchants on r/shopify (28). German club boards: no source. No source shows a tested route.
6. **K3 choice.** For 4.2, 4.4 and 4.14 pick one trade or country each, so the group is one group. For 4.14 also pick one job (K4).
7. **German-language evidence.** Round 2 found almost no German-language posts, because German subreddits were searched with English phrases only. If a German market is chosen (club admin, Handwerk), search German sources directly: forums, Facebook groups and app-store reviews, since Reddit does not carry them.
8. **Classifier recheck.** Re-run the first-450-characters round-1 batches with full text for the clusters that make the shortlist.
9. **Candidates A and B from IDEEN.md.** Search separately for explainer-video buyers and shop conversion audits. This round has two single Shopify posts for B (4.13) and no direct evidence for A.
