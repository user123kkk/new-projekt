# Coverage and limits (2026-10-27)

Method: about 65 WebSearch queries, about 90 WebFetch calls, plus the public Stack Exchange API and the public iTunes customer-review RSS feed. Reddit and Hacker News skipped by instruction.

## Not reachable (no entries)
- G2, Capterra, GetApp, Software Advice, trusted.de, Quora, gutefrage.net, Shopify Community, AccountingWeb, nachi.org, hardforum: HTTP 403 to WebFetch.
- Indie Hackers: HTTP 403; only post titles seen in search results are recorded, marked snippet only.
- Chrome Web Store: redirects to a Google consent wall. Google Play: 404.
- Lobsters: blocked by Anubis. Dev.to: the one relevant post had 0 comments.
- Product Hunt: only two pages returned usable text.

## Reading notes
- WebSearch returns summaries, not raw snippets. Anything taken only from a search summary is marked "Quote (snippet only)".
- OMR Reviews give only relative dates ("older than 12 months").
- SoftGuide tenders state needs in the organisation's own words but are old and closed; they show requirements, not emotion.
- Stack Exchange material is mostly 2009-2016; demand signal there is view count.
- Heavy skew: club software (Germany), landlords (BiggerPockets), craft/invoicing software (OMR, Trustpilot), Shopify merchants.
- Indie Hackers titles are counter-evidence for K1: complaints are easy to find, willingness to pay is not.
- Domains skipped as haram per GRUNDSATZ.md: none appeared in kept entries. No [owner decision] items.
