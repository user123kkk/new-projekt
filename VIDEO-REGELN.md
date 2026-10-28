# VIDEO-REGELN

Binding rulebook for our faceless motion-graphics short videos. Derived from all 37 stations (`stationen/01` to `37`), their captures (`quellen/videos/NN/bild.md`, `transkript.txt`, `frames_uebersicht.jpg`, `video.mp4`), `INDEX.md` and `begriffe/*.md`. [GRUNDSATZ.md](GRUNDSATZ.md) overrides everything here. Status: draft for the owner (2026-10-28), nothing published. Written once; later stations update it per [PROZESS.md](PROZESS.md) step 5.

## 0. How to read this

**Tags on every rule.**
- `[M n/37]` measured by us across n of 37 source videos (method in section 0.2).
- `[S nn s#]` station nn, statement number #, with its rating (usable / conditional / not usable). The station's "required change" is written into the rule text.
- `[P]` platform or capture artifact, not creator design.
- `[I]` our own inference. Not a fact from the sources.

**Cell** = one 3-second frame sample (`frames/f_NNN.jpg`, cell N is at about (N-1) x 3 s). Frames were captured every 3 s. All timing statements about on-screen text and graphics are therefore estimates at 3 s resolution. Transitions, exact cut times and caption sync inside the 3 s cannot be measured from the captures.

### 0.1 Sources are English; our videos are German
All rates (words per second, words per caption) are English. German words are on average longer, so the same rate in German will carry fewer words. Do not use the English numbers as German targets. Transfer is `[I]` and must be checked on the first German voice-over.

### 0.2 Measurement method
- Length, size, fps, audio: `ffprobe` on all 37 `video.mp4`. Loudness and pause level: `ffmpeg volumedetect` on whole file and on gaps between spoken segments.
- Spoken words and rate: `transkript.txt` (Whisper). Removed as artifacts: lines "...", "Thank you." (37), repeated "So..." (28, 36), repeated "I'll see you next time." (36), all entries after the file end. Words are counted including a trailing cut-off word ("Because..."). Rate denominator is stated each time: **spoken span** (first start 0.00 s to last end) or **file length**.
- Caption text: `bild.md` "On-screen text" lines (392 caption entries in 36 videos, video 36 excluded because it uses a different subtitle style). Annotations in brackets removed before counting words.
- Background and colour: pixel check of all 449 content frames (end-card frames excluded) with Pillow: median pixel luma, share of dark pixels, share of strongly coloured pixels.
- Icons: keyword search over the "Visuals" lines of `bild.md` (about 445 cell descriptions). Keywords in Appendix A. The person/figure list was curated by hand, not by keyword.
- I looked at five overview sheets myself (01, 05, 11, 19, 36). Claims about caption position, font and fades are limited to those five and are marked.

### 0.3 What was not measured
Music or sound effects (the audio was analysed for loudness and pauses only, nobody listened to it), transitions, caption font and exact position in 32 of 37 videos, caption-to-voice sync, number of cuts per second, whether the voice is synthetic. Items marked "unmeasured" below need a listening and viewing pass.

---

## A. Form rules (measured)

### A1 Format and length
- **A1.1 Format.** 9:16 vertical, 576 x 1024 px, 30 fps, AAC stereo 44.1 kHz. `[M 37/37]`. The size is the TikTok download size. We render in our own resolution (also vertical). `[I]`
- **A1.2 Length.** File length min 27.2 s (video 30), median 39.5 s, max 90.6 s (video 36). 30 of 37 are between 27.2 and 43.5 s. Five are 45.7 to 52.0 s (05, 06, 09, 11, 12). Exceptions: 28 (61.7 s) and 36 (90.6 s). `[M 37/37]`
- **A1.3 Our target.** 27 to 45 s file length including our end card. Longer only with a stated reason. `[I]` (The P7 script says 20 to 40 s; see section G.)
- **A1.4 Words.** Spoken words per video: min 66, median 87, max 203 (video 36). `[M 37/37]` English count, see 0.1.
- **A1.5 Tail.** File length minus spoken span: median 4.4 s, max 6.2 s. This tail is mostly the platform end card (see A9). `[M 37/37]`, cause `[I]`.

### A2 Voice
- **A2.1 Voice starts at 0.00 s** in 37/37. No logo, jingle or silence before the first word. `[M 37/37]`
- **A2.2 Speech rate.** Spoken-span denominator: min 2.06 words/s (video 34), median 2.53, max 3.18 (video 30). 34 of 37 lie between 2.3 and 2.9. Over file length: min 1.89, median 2.26, max 2.64. `[M 37/37]` Video 34 has whole-second timestamps, so its 2.06 is coarse. German rate: check on the first draft, `[I]`.
- **A2.3 Pauses.** Gaps between spoken segments: median 0.68 s, max 1.92 s (298 gaps; Whisper segments, so a gap is not always a breath). `[M 37/37]`
- **A2.4 First segment.** The first transcript segment ends at 1.6 to 7.7 s, median 3.3 s. `[M 37/37]`
- **A2.5 One voice, no person on screen.** All 37 are narrated by one voice over graphics. No transcript contains "um" or "uh" (Whisper may drop them). `[M 37/37]` Synthetic or human: unmeasured.
- **A2.6 Level.** Whole-file mean volume -19.4 to -24.7 dB, peak about 0 dB in 37/37. Loud, peak-normalised. `[M 37/37]` Our rule: normalise the voice the same way. `[I]`
- **A2.7 Pauses are quiet.** Median level inside pauses is below -38 dB in 27 of the 30 videos that have a gap of 0.6 s or more (voice about -22 dB). No continuous bed in those. Louder pauses: 06 (-34.5 dB), 08 (-31.2), 36 (-31.4); 15 is borderline (-38.9). Cause unknown (unmeasured, could be sound effects). No measurable gap in 03, 04, 05, 07, 26, 33, 34. `[M]` Music cannot be excluded by this measurement. Our own rule is in C5.

### A3 On-screen text
- **A3.1 Text at 0 s.** A caption is on screen in cell 1 in 37/37. `[M 37/37]`
- **A3.2 Text density.** A caption is present in 382 of 420 content cells (91 percent; video 36 excluded). 38 cells have none (graphic only). `[M 36/37]` Text changes at least every 3 s whenever speech runs; finer timing is unmeasured.
- **A3.3 Chunk size.** Words per caption entry: min 1, median 3, max 10, mean 3.5. Up to 3 words: 57 percent; up to 4: 82 percent; up to 5: 92 percent (392 entries). `[M 36/37]`
- **A3.4 Exceptions.** Long two-line captions of 7 to 10 words: video 11 (12 of 15 cells), video 19 (7 cells), single cells in 05 and 22. Video 36 uses small subtitle lines (median 6, max 9 words) at the bottom and has captions in 21 of 29 cells. `[M]`
- **A3.5 Captions mirror the voice.** Caption wording equals the audio with small deviations listed in the station notes (12 "We humans", 11 "gonna", 36 quote marks). Exceptions with on-screen text that is not spoken: 19 cell 7 (speech bubbles "Keeps going. Just like you"), 26 cell 7 (price tags "$150" and "$80"), 22 cell 1 ("FREE" tag), 29 cell 6 (faint "$ 1"). `[S 19 s10-11, S 26 notes, S 22 notes, S 29 notes]` Our rule: nothing on screen that is not also true and, for numbers, spoken (see C8).
- **A3.6 Emphasis by word, not by effect.** Emphasis appears as case or quotes: 16 "it IS new" / "it FEELS new", 05 "THE BEST", 36 "Say what people already think.", 27 and 05 keyword in quotes. `[M]`
- **A3.7 Position and font.** Seen in sheets 01, 05, 11, 19, 36 only: white sans-serif; top of frame in 01, 05, 11; lower third in 19; small bottom subtitle in 36. Dim, semi-transparent captions in 11 (cell 7) and 19 (cell 9), likely fade in or out. `[I]` Other 32 videos: unmeasured. Our rule: pick one caption position and keep it for all videos (A8).
- **A3.8 Slip to avoid.** In video 10 cell 6 a white dot covers letters of the word ("conv[t]"). `[S 10 notes]` Our rule: no graphic over caption text.

### A4 Background and colour
- **A4.1 Background near-black** in 449 of 449 content frames. Median luma is at most 18 of 255 in every frame; at least 69 percent of pixels are darker than luma 40 in every frame. The 11 frames below 80 percent dark are frames with a large bright object (08 cell 9, 11 cell 9, 19 cell 10, 22 cells 7 and 9, 36 cells 5-7 and 11-13). `[M 37/37]`
- **A4.2 Monochrome.** White, grey and silver on black. Strongly coloured pixels (more than 0.3 percent of the frame) outside the platform logo and end card occur only in 05 cells 11 and 12 (screen capture of a third-party tool with blue buttons and photos). `[M 36/37]`
- **A4.3 Glow.** A soft glow, light cone or spotlight is named in the visual description in 31 of 37 videos (69 cells). `[M 31/37]` (Keywords in Appendix A.)
- **A4.4 Two style families.** (a) Minimal: thin white outline icons, dots, rings, lines, glow. About 32 videos. (b) Rendered or photographic exceptions: 11 (silver 3D objects: watch, diamond, hourglass, cart, crystal, balance), 22 (silver coins, crystal, battery icons), 19 (photo-like phone and cans, silhouettes), 05 (third-party logos and UI screenshots), 36 (detailed glowing line illustrations, 91 s). Counts by our reading of `bild.md` and the five sheets, `[I]` for the grouping. **Our rule: family (a) only.** Family (b) is the less safe family: it carries the living beings, real logos and photos that GRUNDSATZ 9 and C16 exclude (11, 19, 05, 36 all do).

### A5 Icons and the white dot
- **A5.1 White dot / focus point.** A dot appears in the visual description of 32 of 37 videos, in about 29 percent of the roughly 445 visual cells. Dot or white sphere: 34 of 37. Exceptions with neither: 05, 12, 31. `[M 32/37 and 34/37]` Dot in the first cell: 01, 02, 04, 06, 16, 17, 22, 30, 32, 34 (ten), white sphere in 19. Typical roles in the descriptions: centre of rings (06, 08, 24), end of a line (01, 13), mover along a line (30), one of a row (08, 16), marker on a text (20 "The 1P Model"). Our rule: one dot per scene as the point where the eye lands; the dot never covers text.
- **A5.2 Icon inventory** (keyword counts, videos out of 37 and cells out of about 445; definitions in Appendix A):

| Icon type | Videos | Cells |
|---|---|---|
| circle / ring / concentric rings | 37 | 171 |
| dot / sphere | 34 | 132 |
| line, arc, zigzag, path, dashed line | 32 | 78 |
| square / rectangle / cube / box | 31 | 74 |
| glow / light cone / spotlight | 31 | 69 |
| product objects (bottle, can, tube, razor, phone, drill, lipstick, laptop, watch, cart, battery) | 16 | 37 |
| dollar sign / coin / price tag / percent | 11 | 22 |
| eye | 12 | 15 |
| speech bubble / envelope | 11 | 15 |
| diamond / crystal | 10 | 16 |
| check mark / seal | 10 | 11 |
| brain | 9 | 18 |
| light bulb / lamp | 9 | 9 |
| gear / chart / dashboard / browser window / slider | 9 | 13 |
| cursor / pointer / hand | 9 | 14 |
| triangle | 8 | 12 |
| question mark / X / plus / minus | 8 | 11 |
| hourglass / scale / seesaw / map pin / calendar / globe / ribbon / badge | 8 | 12 |
| star | 6 | 9 |
| face / smiley | 5 | 6 |
| heart | 4 | 6 |
| megaphone | 4 | 4 |
| yin-yang | 3 | 4 |
| real brand logo or product name | 5 | 9 |
| storefront | 1 | 3 |
| person / head / silhouette (hand-curated) | 15 | about 46 |

- **A5.3 The icon is the spoken noun, literally.** `[S visuals + I]` Examples from the station notes: 02 "lipstick" is a lipstick tube; 04 "razors" a razor, "water" a blob; 08 "Netflix show" phone plus monitor, "Leave a gap" two squares with a gap; 22 "It's not about price" a struck-through dollar; 27 "confusion with risk" a brain with question marks, "they buy certainty" a circle with check mark; 34 "don't list 100 features" a stack of lines; 09 "isn't just a logo" an outline Apple logo. Our rule: every caption chunk gets an object or shape that shows the same thing; if a noun has no safe object, use a shape or diagram (A5.4).
- **A5.4 Abstract concepts are drawn as diagrams**, not as people: ring split into + and - halves for gain and loss (21 cells 7-8); balance scale for value versus cost (11 cells 12-13); dashed line turning solid for traffic versus conversion (32 cell 8); lines joining nodes for connection. `[S visuals]`
- **A5.5 One main motif per cell.** Most of the 445 cell descriptions name one object or one tight cluster. Not counted exactly. `[I]`

### A6 Rhythm and motion
- **A6.1 A new graphic roughly every 3 s or faster.** Every one of 449 sampled cells shows a different graphic from the previous one. The real cut interval is below or equal to 3 s and is unmeasured. `[M 37/37]` Our rule: change graphic with each caption chunk, never hold one static picture longer than about 3 s. `[I]`
- **A6.2 Transitions.** Unmeasurable at 3 s sampling. Hints: mid-motion states (blurred capsules 03, blurred trail 13, 16 blurred dot, 29 faded and blurred number), glowing trails, dimmed captions. So animated morphs and fades, not hard cuts to other footage. `[I]` Our rule: morph or fade between graphics; no hard cut to footage, no flashes, no shakes.
- **A6.3 Numbers on screen** are animated or counting (29 cell 4 shows a blurred "$999,112" on the way to "$1000000"). `[S 29 notes]`

### A7 Structure of a single video
- **A7.1 Opening sentence types (37 first sentences).** "This is why / the reason / how / the ... rule" teaser: 10 (01, 02, 10, 11, 12, 15, 17, 18, 31, 37). Direct statement or claim: 24. Question: 2 (08, 16). Invitation to a game: 1 (28). A number in the first sentence: 1 (32, "99%"). Failure, loss or mistake wording in the first sentence: 9 (01, 02, 17, 23, 25, 30, 31, 32, 34). `[M 37/37]`, classification by hand.
- **A7.2 Typical shape.** Hook claim (0 to 3 s), reason or mechanism, instruction sentence at about 18 to 25 s (01 at 18.2 s, 14 at 18.7 s, 21 at 20.8 s, 17 at 21.1 s, 15 at 24.6 s), closing line. `[I]` from a sample of five transcripts, not all 37.

### A8 Our own consistency rule
- **A8.1** All videos use one look: near-black background, white outline icons, one dot, one caption style and position, one voice. 32 of 37 sources already do. `[S 18 s9, S 03 s6, S 09 s8 + I]` Condition from S 18 s9: a "premium" look must match real quality (no false quality claim).

### A9 What is platform, not design
- **A9.1 TikTok watermark** (moving logo plus "@ conversion.doc") on every content cell of 37/37. `[M 37/37]` `[P]` It moves between corners. Almost certainly added when a video is saved from TikTok. `[I]` Do not copy it.
- **A9.2 End card.** A dark blue panel with the TikTok logo and a search bar (first empty, then "@ conversion.doc") in 37/37 (video 36: frame 30, not in `bild.md`). Sampled in 1 to 2 cells, so about 3 to 6 s. The last 2 s have digital silence (-91 dB) in 37/37. `[M 37/37]` `[P]` Not creator design, and imitating TikTok's search bar is a brand imitation. Our own end card is defined by the P7 script and rule B19.
- **A9.3 No creator logo, intro or outro** appears in any capture; the only identity is the platform handle. `[M 37/37]`
- **A9.4 Ending cut off in the middle of a sentence.** 19 of 37 videos end on a dangling connective in audio (and on screen in 01, 35, 31): 01 "And", 02 "and", 03 and 04 "and this is why", 06 "So...", 08 "But...", 10, 14, 15, 17, 21, 31, 32, 34, 35 "Because...", 12 "And...", 23 "And that's why.", 28 "So...", 29 "because...". (20 if the "So..." that Whisper heard in 36 is counted.) `[M 19/37]` The purpose is unknown. A loop back to the first sentence would be one explanation. `[I]` We do not copy it (C13).

---

## B. Content rules (from stations rated usable or conditional)

Each rule: what to do, source, the station's condition built in. A rule always sits under GRUNDSATZ 1, 3, 5, 7.

### Hook and attention
- **B1 Say the topic in the first seconds.** "If the brain doesn't immediately know what your content is about, it won't stay long enough to find out." `[S 30 s2 usable]` Also `[S 30 s1, s3 usable]`, `[S 13 s1 usable]` ("stop, feel something, and want to know more, all within a few seconds"), `[S 24 s4 usable]` ("understands immediately why it should care"). Measured: voice and text both start at 0 s in all sources (A2.1, A3.1). Rule: first caption and first spoken words name the topic; first frame is readable.
- **B2 Attention from clarity, not from volume of posting.** "posting more often doesn't help. It simply multiplies confusion." `[S 24 s6-7 usable]`, "Clarity is what creates relevance." `[S 24 s8-9 usable]`. Rule: one clear video before many videos. Frequency is not a fix for a unclear video.
- **B3 Relatable opening.** "Nobody wakes up and thinks, I want someone to sell me something today." `[S 35 s1 usable]`. Allowed as a hook: a plain observation the viewer agrees with.
- **B4 Questions as hooks.** "Have you ever started a Netflix show and suddenly had to finish the whole season?" `[S 08 s1-2 usable]`. Allowed: a rhetorical question that the same video answers (A7.1: 08, 16).

### One message, clarity
- **B5 One message, one offer, one action.** "It's one message, one offer, one clear action." `[S 34 s4 usable]`, `[S 34 s8 usable]` ("the more options, the more confusion"). Condition `[S 34 s11 conditional]`: one reason in the video, full terms available before purchase. Rule: one idea per video, one action at the end, terms on the sign-up page, no "only one reason" that hides price or conditions.
- **B6 Simple enough for a five-year-old.** "If a five-year-old can't understand what you do, most adults won't either." `[S 10 s3-4 usable]`. And "Not the most creative, not the most detailed, the clearest." `[S 27 s8 usable]`; "If your message takes effort to understand, your offer feels risky." `[S 27 s4 usable]`. Condition `[S 27 s10 conditional]`: "the feeling that you know exactly what you're doing" must be backed by real competence. Measured: median 87 words and 3-word captions (A1.4, A3.3).
- **B7 Answer the three questions fast.** "what is this, will it help me, and can I trust it?" `[S 15 s2 usable]`; "make them understand exactly what they will be getting" `[S 15 s6 usable]`. Rule: what it is (first 5 s), how it helps (middle), why trust (honest status: not finished, free sign-up). Do not use "ahead of 90% of marketers" (`[S 15 s3]`, no source).
- **B8 The video may point at itself when true.** "It explains one simple idea with visuals your brain actually enjoys." `[S 10 s5-6 usable]`.

### Customer, problem, outcome
- **B9 Start from the problem the viewer really has.** "a problem well explained is a solution half sold" `[S 17 s2 usable]`; "People don't care about your business. They only care about it when you make them care." `[S 17 s3 usable]`; `[S 17 s4 conditional]`: relevance and truthful understanding, no manufactured emotion. `[S 37 s3 conditional]`: the problem must be real and relevant to this customer. `[S 37 s4 conditional]`: no exaggeration or fear beyond the real size of the problem. `[S 37 s6 usable]` "if they don't see the problem, they won't see the value".
- **B10 Go where the problem is already felt.** "sell water to the thirsty" `[S 14 s1-2 usable]`. Condition `[S 14 s5 conditional]`: the offer really solves the problem, no use of acute distress, no religious obligation as a market gap (GRUNDSATZ 11). `[S 14 s6 conditional]`: "relief, not persuasion" never means hiding that it is an offer.
- **B11 Show the viewer's own situation.** "People listen when they feel seen." `[S 19 s6 usable]`; "Focus on one group of people" `[S 19 s5 usable]`; "the customer becomes the hero" `[S 23 s6 usable]`; "Your product is not the destination, it's the tool." `[S 23 s7 usable]`. Conditions: `[S 19 s8 conditional]` understanding comes from real research, no feigned insight; `[S 23 s8 conditional]` customer stories must be real, no invented customers or testimonials. Visual rule: show the viewer's objects (job ad, letter, calendar), not a person.
- **B12 Research the audience; mirror only true beliefs.** `[S 36 s7 usable]` get to know customers (lawfully, with consent); `[S 36 s9-10 usable]`; `[S 36 s2, s5 conditional]` say only what is true, never reinforce a false belief; `[S 36 s11-12 conditional]` fit and understanding must be real.
- **B13 Sell the realistic "after".** "They don't buy the gym membership. They buy who they'll become after going there." `[S 02 s5 conditional]` and "start painting their future" `[S 02 s7 conditional]`. Condition: the future shown is realistic and attainable with the product; no promise of a result the product does not deliver (`[S 02 s6]`: confidence as an experience, no promised compliments). Outcome example that is usable: `[S 33 s4 usable]` the drill is bought for the hung picture.
- **B14 The instant benefit.** `[S 29 s8 conditional]`: usable if the benefit is real and the long-term cost is not hidden. `[S 29 s10 conditional]`: only benefits that really arrive early (for example a first result in the first session). `[S 29 s9 not usable]`: no result promise with a time ("Lose weight in 30 days").

### Emotion, loss, relief
- **B15 Emotion first, truthful.** "People buy emotions and justify with logic." `[S 11 s8 usable]`; "sell the feeling first and the product second" `[S 12 s8 conditional]`: product and terms still stated. `[S 11 s2 conditional]`: real function and terms still stated. `[S 25 s6 conditional]`: emotion is truthful, not manufactured. `[S 25 s8 usable]`: "If people don't feel something, they won't remember anything." Express the emotion by text, voice, objects, shapes. Never by a drawn person.
- **B16 Show the cost of not acting only if real.** "Show them what they are already losing by not acting." `[S 21 s7 conditional]`; "To each goal, there is also an anti-goal." `[S 11 s6 usable]`, `[S 11 s5 conditional]`. Condition: each loss shown is factual and demonstrable; no invented loss, no deadline, no scarcity. `[S 09 s11 conditional]`: no fear claim beyond what can be shown. `[S 11 s10 conditional]`: fear of missing out only about real, verifiable losses.
- **B17 Relief wording.** "People don't buy solutions. They buy relief." `[S 37 s2 usable]`. Never with the shaming frame of `[S 37 s1 not usable]`.
- **B18 Authenticity.** `[S 12 s6-7 conditional]`: "authentic" must be real, not staged. We have no real customer voices yet, so we show none (C20).

### Contrast, priming, open loops
- **B19 Contrast with true alternatives.** "Your brain can't judge value in isolation." `[S 26 s2 usable]`. `[S 26 s1, s8 conditional]`: comparison consists of true alternatives. `[S 26 s5 conditional]`: an anchor is only a real price that is actually charged and is disclosed as such (najsh). Allowed form for us: identical generic letter next to a tailored letter. Not allowed: invented "was" prices, decoy prices, wine example (C11).
- **B20 Context before the offer, not a hidden hook.** Restate `[S 06 s1 conditional]` as "create context before the offer". `[S 06 s4 usable]` a comfort scene before furniture. `[S 06 s3, s6, s7 conditional]`: the primed context is true, the offer fully disclosed, hints never hide terms. No people or families (`[S 06 s5 conditional]`).
- **B21 Open a loop only on content.** "Start it, leave a gap, and let curiosity do the rest." `[S 08 s11 conditional]`. Conditions: the loop is on content, never on price or terms (`[S 08 s8-10 conditional]`), and the gap is filled truthfully inside the video, no unpaid teaser. Source note: the sources themselves cut off 19 of 37 endings (A9.4), which breaks this condition; we do not copy it.
- **B22 Content-led discovery, intent visible.** "Make them feel like they found it." `[S 35 s8-9 conditional]`: the commercial intent is not hidden, the decision stays informed, no disguised advertising. `[S 35 s7 conditional]`: no false claims or hidden terms behind the "obvious decision".

### Price, terms, trust
- **B23 Price as perceived value, with full cost.** "Your job is to raise their understanding and therefore increase the perceived value." `[S 22 s7 conditional]` with true information, no inflated value. `[S 22 s6 conditional]`: if the product is overpriced for its value, correct the price, do not defend it. `[S 11 s9 conditional]`: all costs (price, terms, effort) disclosed. If a price is mentioned: price, duration, renewal and cancellation together (GRUNDSATZ 3). Current P7 decision: 9.90 EUR one-time for 30 days, no renewal, always worded as "geplant".
- **B24 Lower the felt cost by real ease.** "Use a simple checkout" `[S 01 s6 usable]`; guarantee `[S 01 s7 conditional]` must be real, conditions in plain words, honoured; trial `[S 01 s8 conditional]`: duration, end, whether payment data is taken, whether it renews. `[S 01 s5 conditional]`: never lower the pain by hiding price or terms.
- **B25 Trust through certainty.** "people don't buy risk. They buy certainty." `[S 27 s5-6 usable]`. For us certainty is the honest status line: planned, not finished, free sign-up.
- **B26 Look as good as the product is.** "if you want to be seen as premium, make everything look premium." `[S 18 s9 conditional]`: appearance matches real quality. `[S 18 s5-6 usable]`: weak design makes the offer feel weak. `[S 03 s6 conditional]`: the emotions triggered are not produced by false claims. Perception is not a licence to misrepresent (`[S 18 s10]`, `[S 20 s10]`, both conditional).
- **B27 Social proof only if genuine.** `[S 36 s13 conditional]`: testimonials, case studies and reviews genuine, verifiable, used with consent. `[S 36 s15 conditional]`: data real, cited, not cherry-picked. We have none yet; show none (C20).

### Call to action
- **B28 One call to action, last sentence, with its content stated.** Sources: DM calls in 05, 10, 13; comment-keyword calls in 24, 25, 27, 30. Conditions: `[S 24 s10, S 25 s10, S 27 s11, S 30 s5 conditional]` state what the offer is and what happens with the contact; `[S 10 s9, S 13 s5 conditional]` price and scope stated when a service is offered; `[S 05 s8 conditional]` trial terms stated. `[S 13 s7 usable]` "DM to get started" as a plain action is usable. The keyword is also shown as caption text (24 cell 11 grey "Attention", 27 cell 12 'Comment the word "attention"', 05 cell 14 'DM me "PARTICL"'). Measured: only 7 of 37 videos have any call to action. 30 of 37 end without one. `[M 7/37]`

### Claims, statistics, effects
- **B29 No unsourced number.** `[S 15 s3]` "90% of marketers", `[S 21 s3]` "twice as powerful", `[S 32 s1]` "99% of businesses", `[S 01 s1-3]`, `[S 04 s7]`: all rated "claim, unverified". The stations rate many sentences "usable" only as framing. Our rule: no statistic and no absolute ("always", "never", "best", "number 1") without proof (GRUNDSATZ 5). Mechanisms such as loss aversion are worded as tendencies. `[I]`
- **B30 Named effects.** `[S 08 s4]`, `[S 18 s3]`, `[S 20 s4]` name effects without source. Using a name is allowed, but we check the spelling and say "often", not "always". Source video 08 spells "Zagarnik"; that is probably Zeigarnik (our own knowledge, check before use). `[I]`
- **B31 Funnel thinking.** "You either have a conversion problem or a traffic problem." `[S 32 s3 usable]`. Videos are traffic, the sign-up page is conversion; measure separately. Condition `[S 32 s7 conditional]`: do not dismiss legal, ethical or quality problems.
- **B32 Study what works, with public material only.** `[S 05 s2 usable]`, `[S 05 s4 conditional]`: only publicly available material, nothing behind logins or against terms. `[S 05 s5-6 conditional]`: any paid or affiliate relation disclosed.
- **B33 Brand consistency across videos.** `[S 03 s6 conditional]`, `[S 09 s8 usable]` ("clear and consistent"): every video uses the A8 look. `[S 07 s2]` marketing gets attention, branding makes people remember; a repeated look is the branding part.

---

## C. GRUNDSATZ filter: patterns we must NOT copy

Each entry: pattern, where it appears, rule that stops it.

| ID | Pattern | Where it appears (station, cell) | Rule |
|---|---|---|---|
| C1 | Person icons, figures, heads, silhouettes, crowds | 15 videos, about 46 cells: 02 (cell 5 head, cell 11 two persons), 06 (cell 9 three persons), 07 (cell 6 grid of persons), 09 (cell 2), 11 (cells 3, 5, 15), 12 (cells 1-4, 6, 12-14, hooded figure included), 14 (cell 3), 19 (cells 2, 3, 9-11), 25 (cell 7 head with tie), 26 (cells 6-7 person with tie), 27 (cell 2), 33 (cell 8 screen showing people), 35 (cells 1-2), 36 (cells 6, 10-24, many heads), 37 (cell 1) | GRUNDSATZ 9: no drawings or animations of living beings. Not even an icon. |
| C2 | Hands and handshakes | 08 cell 1 (hand with phone), 09 cell 7 (hand cursor), 19 cells 10-11 (hand reaching, clasped hands), 36 cells 7 and 13 | GRUNDSATZ 9, default avoid. Owner decision O5 for a plain cursor arrow. |
| C3 | Photographs of people, photo thumbnails | 05 cell 11 (screen capture with photo thumbnails) | GRUNDSATZ 9. No photos in our videos. |
| C4 | Women | No capture records a woman. Statement level: 02 s6 (lipstick, "compliments"), 06 s5 (happy families), 12 s5 (someone happy to drink a Coke) | GRUNDSATZ 10 and 9. Our own prohibition, not a measured pattern. Choose other examples (no lipstick, no families, no drinkers). |
| C4a | Faces and borderline body icons | smiley or upset face: 12 cell 8, 14 cell 8, 21 cell 4, 23 cell 1, 25 cell 6; eye 12 videos, brain 9 videos (A5.2) | Owner decision O5. Default avoid faces; eye and brain avoided until the owner decides. The P7 list does not include them. |
| C5 | Music and sound beds | Cannot be proven or excluded from the audio analysis (A2.7). Louder pauses in 06, 08, 36 (and borderline 15) are unexplained. | GRUNDSATZ 8: no music. Voice, soft interface sounds and silence only. Listen to those videos before using any sound design from them. |
| C6 | TikTok watermark and TikTok search-bar end card | 37/37 (A9) | Platform artifact, imitation of a third-party brand. Do not copy. |
| C7 | Superlatives, outcome promises, hype words | 05 s9 "the best" (cell 15 caption THE BEST), 13 s6 "moves minds" and "hypnotize" (cell 11 caption), 36 s17 "watch your business explode", 07 s6 "watch your business grow", 31 s1 "reason most businesses fail", 04 s2 "illusion sold by coaches" (motive attributed to a group) | GRUNDSATZ 5 and 1. Only with proof. |
| C8 | Fake urgency, scarcity, anchors, exclusivity, unspoken prices | 05 s7 "should not miss this" (no stated deadline); 11 s10 fear of missing out; 21 s7 invented loss; 26 s5 anchoring and cell 7 prices $150 and $80 not spoken; 28 s4 "only sold in selected stores"; 22 cell 1 "FREE" tag with no audio | GRUNDSATZ 1 and 4. No deadline, no "only X left", no number of users or sign-ups, no "was" price. |
| C9 | Manipulation wording and covert influence | 36 s1 "easily manipulate your customers" (cell 1 shows this caption) not usable; 37 s1 "make people feel dumb saying no" not usable (cell 1 caption); 12 s1 "dark psychology"; 06 s3 "without them ever realizing it"; 12 s9 "subconsciously" (cell 14 caption); 26 s6 "This isn't manipulation"; 35 s9 "not like you sold it"; 14 s6 "not like persuasion"; 37 s5 "without them having to move a finger" | GRUNDSATZ 7 and 6. Allowed: priming, contrast, loss framing, open loops when true and nothing is concealed. Not allowed: the aim of moving a person against their interest, shaming, concealed sales intent. Never use the words "manipulate", "dark psychology", "subconscious", "hypnotize" about our own method. |
| C10 | Illusion of innovation | 16 s5 "complexity to create curiosity" not usable, 16 s9 "because it feels new" not usable (cells 12-13 captions "it IS new" and "it FEELS new"), fancy invented names in 16 cell 4 | GRUNDSATZ 1, ghish. No new-sounding names for ordinary things, no feigned novelty. Station 16 s6 is used only as an observation to avoid misleading. |
| C11 | Wine, alcohol examples and the "same product at 21 times the price" logic | 26 s4, 28 s2-12 (28 s11 not usable) | Order of authority 1. No alcohol in any example. Identical products are never presented as different in quality. |
| C12 | Time-bound result promise | 29 s9 "Lose weight in 30 days" not usable (cell 10 dial "30") | GRUNDSATZ 1 and 5. Our case: no "in 30 Sekunden fertig", no "garantiert". |
| C13 | Ending cut off on a connective | 19 of 37 videos (A9.4) | B21 and B5: the loop must be paid off, the last sentence is complete. Purpose unknown (`[I]`). |
| C14 | Calls to action that hide the funnel | 24, 25, 27, 30 ("Comment the word attention" with no stated offer), 05 (DM for a trial, no trial terms, no disclosure), 10 and 13 (DM, no price or scope) | B28 and GRUNDSATZ 3. |
| C15 | Undisclosed affiliation | 05 (third-party tool; neither audio nor captions say whether the creator is paid) | `[S 05 s5 conditional]`. We do not promote third-party tools in these videos. |
| C16 | Third-party logos, products, brand names on screen | 05 (Skims, Lululemon, Gymshark, Particl), 09 and 34 (Apple outline), 19 (Samsung phone, Pepsi and Coca-Cola cans), 28 (Walmart), 04 (razor) | Our own rule, `[I]`: no third-party logo or product image. P7 script already says competitor names are never shown or spoken. Station 19 s3-4 and 34 s5 name brands as examples; use generic objects instead. |
| C17 | Absolutes without proof | "never", "always", "at all", "only": 04 s1, s3, s8; 19 s2-4; 20 s8; 22 s1; 27 s7; 33 s2 | GRUNDSATZ 5; B29. |
| C18 | Unsourced statistics | 15 s3 (90 percent), 21 s3 ("twice"), 32 s1 (99 percent), 01 s1-3, 04 s7 | B29. |
| C19 | Staged emotion or "raw and real" authenticity | 12 s6-7 | `[S 12 s6-7 conditional]`: not produced by scripted fake testimonials or actors. |
| C20 | Testimonials, reviews, data as social proof | 36 s13, s15 | B27. None until real ones exist. |
| C21 | Calls on desire for a pain that belongs to religion | none found in the sources | GRUNDSATZ 11. Listed so it stays checked. |
| C22 | Loss-framed claim beyond evidence | 09 s11 "miss the most important opportunity", 01 s1 "lose your customers in the last second" | B16, B29. |
| C23 | Financing or ads in the app | none found in the sources | GRUNDSATZ 2 and 13. Listed so it stays checked. |

---

## O. Owner decisions (contradictions between stations)

These come from `INDEX.md` ("Statements that contradict each other"). The default satisfies both sides where possible. The owner may change any default.

- **O1 Attention first (30) or understanding first (24).** `[S 30 s4]` "You gain attention first in order to build understanding later on." versus `[S 24 s4]` "understands immediately why it should care". Default: the first sentence states the topic and the reason to care in one line (B1). Both stations agree the first seconds decide.
- **O2 Customer's story (23) or founder story (25).** `[S 23 s4]` "your customer doesn't care about your story" versus `[S 25 s7]` "people love founder stories". Default: the viewer's situation leads (B11). Our own story only as a true one-line status ("Eigenes Projekt, noch nicht fertig"), conditional per `[S 25 s7]` (true, no private data of others).
- **O3 Withhold (08) or answer fast (15, 27, 34, 10).** Default: the hook may open a question, the video answers it before the end (B4, B21). No cut-off ending, no gap on price or terms. Complexity as curiosity (16) is excluded (C10).
- **O4 Long-term "after" (02) or instant benefit (29).** Default: show the realistic after (B13) and, if true, the first benefit the user gets at first use (B14). No time promise.
- **O5 "This isn't manipulation" (26) or "manipulate your customers" (36).** Default: judge by aim (GRUNDSATZ 7). Both phrases are excluded from our wording (C9). Technique is allowed when true and open.
- **O6 Product does not matter (20) or product matters when outcome is understood (33).** Default: show the real product, as an honest mockup of what exists, with the outcome (B13). No claim that perception beats reality (`[S 18 s10]`, `[S 20 s10]` conditional).
- **O7 Borderline icons.** Eye, brain, smiley face, cursor arrow, hand (C2, C4a). Default: avoid. The owner may allow eye, brain and cursor as non-living objects.
- **O8 Style family.** Minimal outline-and-dot (A4.4a) versus rendered silver 3D (11, 22). Default: minimal only.
- **O9 Caption position and font.** Measured only in five sheets (A3.7). Default: choose one and keep it. Owner picks.
- **O10 Length and speaking pace in German.** Default: 27 to 45 s, pace checked on the first German voice-over (A2.2).

---

## D. Checklist before publishing (answer yes or no; any "no" means do not publish)

1. Voice starts at 0.0 s and a caption is visible in the first frame (A2.1, A3.1)?
2. Do first caption and first sentence say what the video is about (B1)?
3. Is there exactly one message and exactly one action (B5)?
4. Is every number on screen also true, and every spoken number sourced or labelled as an example (B29, C18)?
5. Is the background near-black and everything on screen white, grey or silver, with no other colour (A4)?
6. Is there no person, face, head, hand, silhouette, figure or photo of a living being (C1, C2, C3)?
7. Is no woman depicted or implied by an example (C4)?
8. Are eye, brain, smiley and cursor icons absent unless the owner has allowed them (O7)?
9. Is no music in the audio, only voice, soft interface sounds or silence (C5)?
10. Is there no TikTok watermark, search bar or imitation of any platform end card (C6)?
11. Are there no third-party logos, product images, competitor names or alcohol examples (C11, C16)?
12. Does each caption chunk have at most about 5 words (A3.3) and is a graphic that shows the same noun on screen at the same time (A5.3)?
13. Does the graphic change at least every 3 s with a morph or fade, no flashes (A6)?
14. Is there one dot as focus point and does it cover no text (A5.1, A3.8)?
15. Do all captions look like the previous videos: same position, same font, same look (A8, O9)?
16. Is the last sentence complete and does every opened question get answered inside the video (B21, C13)?
17. Does the end state what is offered, that it is not finished, and that sign-up is free (B28, B25)?
18. If a price is named: price, duration, renewal and cancellation are all stated, as "geplant" if not built (B23)?
19. Are there no superlatives, "garantiert", "Nr. 1", deadlines, scarcity, user numbers or invented was-prices (C7, C8)?
20. Are all losses, problems and benefits shown real and demonstrable, with no invented fear or shaming (B9, B16, C9)?
21. Is the sales intent visible, and is nothing hidden that the viewer would need to decide (B22, GRUNDSATZ 6)?
22. Are any testimonials, reviews or data real and cited, or absent (B27)?
23. Is the spoken rate in a natural range and checked in German (A2.2), with level normalised like the sources (A2.6)?
24. Is total length between 27 and 45 s, or is the reason for a different length written down (A1.3)?
25. Has the video been re-read against GRUNDSATZ rules 1 to 11 and the owner decisions O1 to O10?

---

## E. Coverage: every station and where it lands

| Station | Where it is used |
|---|---|
| 01 | B23, B24, B29, C18 |
| 02 | B13, C4 |
| 03 | B26, B33 |
| 04 | B29, C7, C16, C17 |
| 05 | B28, B32, C3, C7, C8, C14, C15, C16 |
| 06 | B20, C9 |
| 07 | B33, C7 (brand and attention only; no further video rule) |
| 08 | B4, B21, O3 |
| 09 | B16, B33, C7, C22 |
| 10 | B6, B8, B28 |
| 11 | B15, B16, C8 |
| 12 | B15, B18, C4, C9, C19 |
| 13 | B1, B28, C7 |
| 14 | B10, C9 |
| 15 | B7, B29, C18 |
| 16 | C10 (not usable; only s6 as warning) |
| 17 | B9 |
| 18 | B26, B33, O6 |
| 19 | B11, C1, C16 |
| 20 | B26, B33, O6 (brand definition only; no further video rule) |
| 21 | B16, C8, C18 |
| 22 | B23 |
| 23 | B11, O2 |
| 24 | B1, B2, B28, O1 |
| 25 | B15, B28, O2 |
| 26 | B19, C8, C11, O5 |
| 27 | B6, B25, B28 |
| 28 | C11 (mechanism only: honest description of a real experience) |
| 29 | B14, C12, O4 |
| 30 | B1, B28, O1 |
| 31 | B26 (brand over product), C7 |
| 32 | B31, C18 |
| 33 | B13, O6 |
| 34 | B5, C16 |
| 35 | B3, B22, C9 |
| 36 | B12, B27, C9, C20 |
| 37 | B9, B17, C9 |

Form rules A come from the captures of all 37 videos, with the exceptions named in each rule.

---

## F. What the sources do that a typical motion-graphics template does not

- No colour at all. Black, white, grey. A template would add an accent colour.
- One voice, no music, pauses that are quiet. A template adds a music bed.
- Captions are 3 words, not full sentences, and are mirrored by one literal object each.
- No logo, no brand intro, no lower third, no outro of our own. (The visible end card is TikTok's.)
- Call to action in 7 of 37 videos only. A template adds one to every video.
- 19 of 37 end on a cut-off connective. A template ends on a closed sentence and a CTA.
- Most videos are 30 to 43 s including a 3 to 6 s platform tail.

## G. Differences between `video/p7-skripte.md` and the measurements (file not changed)

- **Length.** P7: 20 to 40 s. Sources: file length 27.2 to 43.5 s in 30 of 37, with a platform tail we do not have. The P7 end card is 5 to 6 s of our own content, so the tail is longer than the platform tail (median 4.4 s). Check the 20 s lower end: the shortest source is 27.2 s.
- **End card speech rate.** The P7 end card voice sentence has about 25 German words for 5 to 6 s, which is about 4 words/s. The English sources run 2.06 to 3.18 words/s. The end-card text has three lines for 5 to 6 s, while sources show about 3 words per 3 s. Shorten or lengthen the end card (A2.2, A3.3).
- **Hook.** P7 hook "Ein Anschreiben für alle Stellen?" is 5 words and matches the measured "up to 5 words in 92 percent". First-sentence length: sources have a first segment of median 3.3 s; P7 says "in the first 2 s".
- **Style.** P7 style (near-black, outline icons, one dot, white sans-serif line every 3 s) matches 32 of 37 sources `[M]`. P7 allowed icons (circle, square, line, check, X, envelope, document, magnifier, calendar, lock, coin, clock, arrow, mockup) all occur in the sources, except that lock and clock appear only as a keyhole mark (09 cell 16) and a clock-hand shape (09 cell 6). P7 excludes persons, hands, figures; measurement confirms 15 source videos use persons or heads and 4 use hands (08, 09, 19, 36), so the exclusion is a real departure from the source style.
- **Sounds.** P7 allows soft interface sounds (tick, click, whoosh). The sources: unmeasured. The P7 sounds are our choice `[I]`.
- **Call to action.** P7 puts the same end card on all 10 videos. Sources: 7 of 37 have a CTA. Own decision, justified by GRUNDSATZ 1 and B22 (intent visible). Not a copy.

---

## Appendix A. Keyword definitions used for A5

Case-insensitive search over the "Visuals" lines of `bild.md` (lines naming only the TikTok logo skipped).

- dot / sphere: `\bdots?\b|\bsphere`
- circle / ring: `\bcircles?\b|\brings?\b|concentric`
- square / rectangle / cube / box: `\bsquares?\b|rectangle|\bcube|\bbox\b|rounded square`
- diamond / crystal: `diamond|crystal`
- triangle: `triangle`
- brain: `\bbrain`
- eye: `\beye\b`
- light bulb / lamp: `light ?bulb|lamp`
- check mark / seal: `check ?mark|checkbox|check-seal|rosette|check seal`
- dollar / coin / price: `dollar|coin|\$|price tag|percent`
- heart: `\bheart`
- face / smiley: `smiley|upset face`
- cursor / hand: `cursor|pointer|\bhand\b`
- speech bubble / envelope: `speech bubble|envelope`
- megaphone: `megaphone|speaker`
- star: `\bstars?\b`
- product objects: `bottle|\bcan\b|cans|tube|razor|phone|smartphone|drill|lipstick|laptop|monitor|watch|shopping cart|battery|batteries|skincare`
- gear / chart / browser: `\bgear|chart|dashboard|browser|window|bar chart|progress bar|slider|toggle`
- line / arc / path: `zigzag|\barrows?\b|\bline\b|\bpath|\barc\b|dashed|\bwavy`
- glow / light cone: `light cone|spotlight|glow`
- question / X / plus / minus: `\?|\bX\b|"\+"|"-"`
- yin-yang: `yin`
- hourglass / scale / pin and similar: `hourglass|scale|seesaw|map pin|calendar|globe|ribbon|badge|pentagon|keyhole`
- real brand: `apple|skims|lululemon|gymshark|particl|pepsi|coca|samsung|walmart`
- storefront: `storefront`

Keyword counts can over- or under-count (for example "glow" inside a description of an unrelated object). They show family and order of magnitude, not exact counts. The person list is not keyword-based: it was read cell by cell from the grep output of person, figure, head, silhouette, crowd, hand and handshake descriptions.
