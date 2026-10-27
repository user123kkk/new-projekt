# Reddit via search engine (Sonnet agents)

Goal: find Reddit posts since 2024-01-01 where people state a need for a digital product (app, web tool, software, plugin, template, automation) in their own words.

Method:
- Use WebSearch with exact phrases in quotes plus `site:reddit.com`, e.g. `site:reddit.com "wish there was an app" landlord`.
- Phrases: "wish there was an app", "is there an app that", "is there a tool that", "I would pay for", "I'd pay for", "someone should build", "why is there no app", "can't find an app", "looking for software", "spreadsheet", "doing this manually", "takes me hours", "gibt es eine app", "gibt es ein tool", "würde dafür zahlen". Combine with the area keywords you are given.
- Run up to 40 searches. Use WebFetch on a thread only when the snippet is not enough; reddit.com may block, then try old.reddit.com once, then keep the snippet.
- Skip promotion of the author's own product, news, and posts older than 2024 when the date is visible.
- Skip areas clearly in conflict with: interest/financing/BNPL, gambling, alcohol, music, adult content, dating.

Output: write `quellen/nachfrage/web/reddit-search-<N>.md` in this exact format:

    # Reddit via search engine: <area>

    Searches run: <count>. Blocked or empty: <short note>.

    Entries: <count>

    ### <short problem label, 3-8 words, English>
    - URL: <thread url>
    - Date: <date or "unknown">
    - Who: <role/industry or "unknown">
    - Quote: "<verbatim sentence from the post>" (add "(snippet)" if taken only from the search result)
    - Existing tools named: <list or "none">
    - Signals: <upvotes/comments if visible; any willingness to pay stated verbatim>

Copy quotes exactly. Do not invent or complete text. No usernames. Final reply: area, searches run, entries written, top 5 problem labels with counts.
