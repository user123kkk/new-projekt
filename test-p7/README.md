# test-p7: sign-up page for P7 (job application writing)

Local only. Not published. Plain HTML + CSS, no external resources, system fonts, no tracking, no images.

## Fill before publishing
1. `[PREIS]` and `[ZEITRAUM]` in the offer (owner decides; proposal in IDEEN.md section 11: a pass for e.g. 30 days, one payment, no renewal). The sentence "Kein Abo, keine automatische Verlängerung." must stay.
2. Impressum with the owner's real name and address (legally required in DE for a commercial page). Replace the `[IMPRESSUM]` link and create the page.
3. Datenschutzerklärung covering exactly what happens: e-mail collected only to notify at launch, form provider named as processor, hosting provider (Cloudflare) server logs, how to unsubscribe. Replace the `[DATENSCHUTZ]` link.
4. Form provider: set `action` and `method` in the `<form>` (see TODO comment). Use a provider with a data processing agreement; keep the form to one field (e-mail). Double opt-in is advisable in DE.
5. Re-check the quoted t3n sentence against the source (https://t3n.de/news/ki-bewerbung-chatgpt-anschreiben-so-reagieren-personaler-1529440/). It was read through a summarising fetch, not the raw page. Remove the quote if it cannot be confirmed or the owner prefers no third-party quote.
6. Hosting: Cloudflare Pages, under adrabic.com (subdomain or path). Do not enable Cloudflare Web Analytics or any tracking script (rule 6). If counts are needed, use only server-side counts and say so in the privacy notice.
7. The photo slot (IDEEN.md section 10) is deliberately not mentioned on the page; the owner decides later.
8. Read the page once more against GRUNDSATZ: no music, no images, no people, no scarcity, no "best" claims.

## Measurement plan (3 weeks, from IDEEN.md section 11)
- 10 faceless short videos (text, shapes, screen-style mockups, voice; no music, no people), each pointing to this page.
- Count weekly: views, saves, comments (from the platforms) and sign-ups (from the form provider).
- Threshold set by the owner before the first video (proposal: 100 sign-ups). Write it down first.
- Threshold met: build the web app, card payment via Stripe (rule 14). Not met: park P7, no building.
- Collect the comments (questions, objections such as "ChatGPT is free"); they decide the next version of the page.
