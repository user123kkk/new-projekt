# test-p7: sign-up page for P7 (job application writing)

Plain HTML + CSS, no external resources, system fonts, no tracking, no cookies, no images. Sign-ups go through a Cloudflare Pages Function into Cloudflare KV (no third-party service). Not deployed yet.

## Files
- `index.html`, `danke.html`, `impressum.html`, `datenschutz.html`: the pages.
- `functions/api/vormerken.js`: POST `/api/vormerken`. Validates e-mail and consent, honeypot field `website` must stay empty, stores `{email, created, source:"p7"}` under the lowercase e-mail in KV `VORMERKUNGEN`. Duplicates get the same response. Form posts get 303 to `/danke.html`, JSON requests get `{ok:true}`. No logging, no IP storage, no cookies.
- `wrangler.toml`: `pages_build_output_dir = "."` and the KV binding (id is a placeholder).

## Fill before publishing
1. `[PREIS]` and `[ZEITRAUM]` if still open (owner decides; proposal in IDEEN.md section 11). The sentence "Kein Abo, keine automatische Verlängerung." must stay.
2. `datenschutz.html` is a generated draft (see comment at the top of the file). Have it checked (reputable generator or lawyer) before publishing, then remove the comment.
3. Re-check the quoted t3n sentence against the source (https://t3n.de/news/ki-bewerbung-chatgpt-anschreiben-so-reagieren-personaler-1529440/). It was read through a summarising fetch, not the raw page. Remove the quote if it cannot be confirmed or the owner prefers no third-party quote.
4. Do not enable Cloudflare Web Analytics or any tracking script (rule 6). Cloudflare's own server logs are named in the privacy notice.
5. The photo slot (IDEEN.md section 10) is deliberately not mentioned on the page; the owner decides later.
6. Read the page once more against GRUNDSATZ: no music, no images, no people, no scarcity, no "best" claims.

## Deployment (owner does this; nothing here has been deployed)
1. Cloudflare dashboard: create a KV namespace (Storage & Databases > KV), e.g. `p7-vormerkungen`. Copy its id.
2. Put the id into `wrangler.toml` (`id = "..."`), or leave the file and bind it in the Pages project instead: Settings > Bindings > Add > KV namespace, variable name exactly `VORMERKUNGEN`. If you bind it in the dashboard, remove the `[[kv_namespaces]]` block or keep the ids identical.
3. Create the Pages project: either connect the GitHub repo (root directory `test-p7`, no build command, output directory `.`) or upload the folder (`npx wrangler pages deploy test-p7`, needs your login).
4. Custom domain: Pages project > Custom domains > e.g. `bewerbung.adrabic.com`.
5. Test once with your own address: tick the box, submit, expect `/danke.html`. Check that the entry exists in KV. Then delete your test entry.

## Export and delete sign-ups
```
npx wrangler kv key list --namespace-id <ID>
npx wrangler kv key get "name@example.com" --namespace-id <ID>
npx wrangler kv key delete "name@example.com" --namespace-id <ID>
```
`key list` prints all e-mail addresses (the keys). Add `--remote` if your wrangler version defaults to local storage. Deletion requests arrive by mail to adrabic.de@gmail.com; delete the key. Delete all keys at the latest 12 months after the test ends (promised in the privacy notice).

## Open legal note: double opt-in
Not implemented. Anyone can enter any address, so a third party could sign up someone else, and the single consent checkbox does not prove the address owner agreed. Double opt-in (confirmation mail with a link) would fix that but needs a mail sender, which means another service or domain mail setup, and more data flows to document. Trade-off accepted for the test: one mail only, easy deletion, no sending before launch. Before the real launch mail, decide: either add double opt-in, or send the launch mail only once and accept the residual risk. Get legal advice on this point.

## Measurement plan (3 weeks, from IDEEN.md section 11)
- 10 faceless short videos (text, shapes, screen-style mockups, voice; no music, no people), each pointing to this page.
- Count weekly: views, saves, comments (from the platforms) and sign-ups (KV key count).
- Threshold set by the owner before the first video (proposal: 100 sign-ups). Write it down first.
- Threshold met: build the web app, card payment via Stripe (rule 14). Not met: park P7, no building.
- Collect the comments (questions, objections such as "ChatGPT is free"); they decide the next version of the page.
