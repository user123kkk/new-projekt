# Classification instructions (Haiku)

Input: `quellen/nachfrage/batches/batch_NNN.jsonl`, one post per line (fields: id, src, sub, title, text, score, comments, url).
Output: `quellen/nachfrage/classified/batch_NNN.jsonl`, exactly one JSON line per input post, same order, same id.

Judge only what the post says. Do not guess. If unsure, set `demand` to false.

`demand` is true only if the author (or the post) states a need, wish or complaint that a **digital product** (app, web tool, software, plugin, template, automation) could address. Promotion of the author's own product, news, and general discussion are false.

For `demand: false` write only: {"id": "...", "demand": false}

For `demand: true` write:
{"id": "...", "demand": true,
 "problem": "short English label, 3-8 words, reusable across posts (e.g. 'landlord rent tracking', 'invoice creation for tradespeople')",
 "who": "role or industry of the person with the problem, or 'unknown'",
 "product": "app | web tool | desktop software | plugin/extension | template | automation | other",
 "pain": 1-3 (1 = nice to have, 2 = recurring annoyance, 3 = costs real time or money, stated),
 "pay": "explicit | implied | none" (explicit = says they would pay or already pay; implied = pays for a tool they dislike; none),
 "tools": ["existing tools named"],
 "quote": "one verbatim sentence from title or text that shows the need, copied exactly",
 "flag": "none" or a short reason if the product area clearly conflicts with: interest/financing/BNPL, gambling, alcohol, music, adult content, dating, depicting women, images of living beings as the core product}

Write valid JSON, one object per line, no extra text in the file. Then reply with one line: batch number, posts in, demand true count.
