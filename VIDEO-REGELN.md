# VIDEO-REGELN

Binding rulebook for our faceless motion-graphics short videos. Derived from all 51 stations (`stationen/01` to `51`; 47 is the same script as 39 and counts once, so 50 distinct videos), their captures (`quellen/videos/NN/bild.md`, `transkript.txt`, `frames_uebersicht.jpg`, `video.mp4`), `INDEX.md` and `begriffe/*.md`. [GRUNDSATZ.md](GRUNDSATZ.md) overrides everything here. Status: draft for the owner (2026-10-28), nothing published. Written once from stations 01 to 37; updated on 2026-10-28 with stations 38 to 51 per [PROZESS.md](PROZESS.md) step 5 (re-measured part A counts, devices A10, rules B34 to B38, patterns C24 to C29, owner decisions O11 to O13).

## 0. How to read this

**Tags on every rule.**
- `[M n/50]` measured by us across n of 50 source videos: stations 01 to 51 with the duplicate 47 counted once with 39 (method in section 0.2). Rules not re-measured for 38 to 51 say so and keep their older count.
- `[S nn s#]` station nn, statement number #, with its rating (usable / conditional / not usable). The station's "required change" is written into the rule text.
- `[P]` platform or capture artifact, not creator design.
- `[I]` our own inference. Not a fact from the sources.

**Cell** = one 3-second frame sample (`frames/f_NNN.jpg`, cell N is at about (N-1) x 3 s). Frames were captured every 3 s. All timing statements about on-screen text and graphics are therefore estimates at 3 s resolution. Transitions, exact cut times and caption sync inside the 3 s cannot be measured from the captures.

### 0.1 Sources are English; our videos are German
All rates (words per second, words per caption) are English. German words are on average longer, so the same rate in German will carry fewer words. Do not use the English numbers as German targets. Transfer is `[I]` and must be checked on the first German voice-over.

### 0.2 Measurement method
- Length, size, fps, audio: `ffprobe` on all 51 `video.mp4` (47 shown separately, counted with 39). Loudness and pause level: `ffmpeg volumedetect` on whole file and on gaps between spoken segments.
- Spoken words and rate: `transkript.txt` (Whisper). Removed as artifacts: lines "...", "Thank you." (37), repeated "So..." (28, 36), repeated "I'll see you next time." (36), all entries after the file end. Words are counted including a trailing cut-off word ("Because..."). Rate denominator is stated each time: **spoken span** (first start 0.00 s to last end) or **file length**.
- Caption text: `bild.md` "On-screen text" lines (392 caption entries in 36 videos, video 36 excluded because it uses a different subtitle style). Annotations in brackets removed before counting words.
- Background and colour: pixel check of all 449 content frames (end-card frames excluded) with Pillow: median pixel luma, share of dark pixels, share of strongly coloured pixels.
- Icons: keyword search over the "Visuals" lines of `bild.md` (about 445 cell descriptions). Keywords in Appendix A. The person/figure list was curated by hand, not by keyword.
- Stations 38 to 51 (added 2026-10-28) were measured with the same scripts: lengths, words and rate (transcript tails after the end of speech removed as Whisper artifacts: 40, 42, 44, 50, 51), caption entries (the method reproduces the earlier 392 entries of 01 to 37 exactly, then adds 163 for 38 to 51 = 555 in 49 videos), pixel check of 178 further content frames (627 in all), loudness and the last-2-s silence, icon keywords over 152 described cells. The 37 older word counts were recounted with one cleaning rule and moved by up to 5 words.
- I looked at five overview sheets myself (01, 05, 11, 19, 36). Claims about caption position, font and fades are limited to those five and are marked.

### 0.3 What was not measured
Music or sound effects (the audio was analysed for loudness and pauses only, nobody listened to it), transitions, caption font and exact position in all videos except five (01, 05, 11, 19, 36), caption-to-voice sync, number of cuts per second, whether the voice is synthetic. Items marked "unmeasured" below need a listening and viewing pass.

---

## A. Form rules (measured)

Counts are over 50 videos: stations 01 to 51, with 47 counted once (it is the same script as 39; its form differs and is named where it matters). Where a rule says "of 37" it was not re-measured for 38 to 51.

### A1 Format and length
- **A1.1 Format.** 9:16 vertical, 576 x 1024 px, 30 fps, AAC stereo 44.1 kHz in 48 of 50. Exceptions: 50 and 51 (@cryothum) are landscape 16:9, 1024 x 576, same codec and fps. `[M 50/50]` The size is the TikTok download size. We render in our own resolution, vertical only. `[I]`
- **A1.2 Length.** File length min 21.0 s (video 49), median 39.5 s, max 90.6 s (video 36). 35 of 50 are between 27.2 and 43.5 s. Two are shorter: 49 (21.0 s) and 39 (24.2 s). Nine are 43.5 to 56.4 s: 05, 06, 09, 11, 12 (45.7 to 52.0), 43 (46.0), 42 (52.7), 46 (54.1), 40 (56.4). Four are over 60 s: 28 (61.7), 51 (73.4), 50 (78.5), 36 (90.6). `[M 50/50]` Video 47 (22.5 s) is not counted separately.
- **A1.3 Our target.** 27 to 45 s file length including our end card. Longer only with a stated reason. `[I]` (The P7 script says 20 to 40 s; see section G. Videos 49 and 39 show that 21 to 24 s exists in the sources.)
- **A1.4 Words.** Spoken words per video: min 43 (49), median 90, max 209 (50, 51; 36 has about 203). `[M 50/50]` English count, see 0.1. Recounted for all 50 with one cleaning rule (see 0.2); the 37 older counts moved by up to 5 words.
- **A1.5 Tail.** File length minus spoken span: median 4.4 s, max 6.8 s. This tail is mostly the platform end card (see A9). `[M 50/50]`, cause `[I]`.

### A2 Voice
- **A2.1 Voice starts at 0.00 s** in 50/50. No logo, jingle or silence before the first word. `[M 50/50]`
- **A2.2 Speech rate.** Spoken-span denominator: min 2.06 words/s (video 34), median 2.58, max 3.74 (video 42, which includes clip speech). 38 of 50 lie between 2.3 and 2.9. The 13 new videos are faster: 8 of them exceed 2.9 (38 3.12, 39 3.52, 40 3.18, 41 3.26, 42 3.74, 43 3.38, 48 3.44, 51 3.02); only 44, 45, 46, 49, 50 are in the older range. Over file length: min 1.89, median 2.31, max 3.45. `[M 50/50]` Video 34 has whole-second timestamps, so its 2.06 is coarse. Do not raise our target because of the faster videos. German rate: check on the first draft, `[I]`.
- **A2.3 Pauses.** Gaps between spoken segments: median 0.68 s, max 1.92 s (298 gaps in 01 to 37; Whisper segments, so a gap is not always a breath). In 38 to 51 (124 gaps) the median is 0.46 s and the longest ordinary gap 1.0 s. One long silence: video 45 has no speech from 2.7 to 9.9 s while two pictures are shown ("buy this or this?"). 40 and 51 have no gap at all in the transcript. `[M]`
- **A2.4 First segment.** The first transcript segment ends at 1.5 to 7.7 s; median 3.3 s in 01 to 37 and 2.9 s in 38 to 51. `[M 50/50]`
- **A2.5 One voice, no person on screen.** 49 of 50 are narrated by one voice over graphics or still pictures. Exception: 42 mixes the narrator with four embedded clips of other speakers. No transcript contains "um" or "uh" (Whisper may drop them). `[M 50/50]` Synthetic or human: unmeasured.
- **A2.6 Level.** Whole-file mean volume -15.7 to -24.7 dB (38 to 51: -15.7 to -22.7), peak about 0 dB in 50/50. Loud, peak-normalised. `[M 50/50]` Our rule: normalise the voice the same way. `[I]`
- **A2.7 Pauses are quiet.** Measured on 01 to 37 only, not re-measured for 38 to 51: median level inside pauses is below -38 dB in 27 of the 30 videos that have a gap of 0.6 s or more (voice about -22 dB). No continuous bed in those. Louder pauses: 06 (-34.5 dB), 08 (-31.2), 36 (-31.4); 15 is borderline (-38.9). Cause unknown (unmeasured, could be sound effects). No measurable gap in 03, 04, 05, 07, 26, 33, 34. `[M]` Music cannot be excluded by this measurement. A burned-in subtitle "(music playing)" in an embedded clip of 42 (cell 7) shows that clip carries music. Our own rule is in C5.

### A3 On-screen text
- **A3.1 Text at 0 s.** A caption is on screen in cell 1 in 49 of 50. Exception: 50 (cell 1 is a pictogram chasing a coin, no text). In 51 cell 1 shows only a product-card label ("$49"). `[M 50/50]`
- **A3.2 Text density.** Text is present in 545 of 598 content cells (91 percent; video 36 excluded). Graphic-only cells: 53, of which 15 in 38 to 51 (50: 7, 51: 5, 46: 2, 43: 1). `[M 49/50]` Text changes at least every 3 s whenever speech runs, except the held layouts in A10.
- **A3.3 Chunk size.** Words per caption entry: min 1, median 3, max 14 (video 46), mean 3.5. Up to 3 words: 58 percent; up to 4: 79 percent; up to 5: 89 percent (555 entries; 01 to 37 alone: 57, 82, 92). `[M 49/50]` The new videos have somewhat longer entries (up to 3: 60, up to 4: 73, up to 5: 82 percent of 163).
- **A3.4 Exceptions.** Long two-line captions of 7 to 10 words: video 11 (12 of 15 cells), video 19 (7 cells), single cells in 05 and 22. Video 36 uses small subtitle lines (median 6, max 9 words) at the bottom and has captions in 21 of 29 cells. In 38 to 51: 41 types full wordings of 11 and 13 words, 46 shows comparison lines of 10 to 14 words, 44 and 51 have single entries of 12 to 13 words, 45 has a median of 5.5 words. Videos 50 and 51 have no caption of the spoken sentences: the on-screen words are labels inside the pictures (HOW IS IT MADE?, WANTS, "works"). `[M]`
- **A3.5 Captions mirror the voice.** Caption wording equals the audio with small deviations listed in the station notes (12 "We humans", 11 "gonna", 36 quote marks). Exceptions with on-screen text that is not spoken: 19 cell 7 (speech bubbles "Keeps going. Just like you"), 26 cell 7 (price tags "$150" and "$80"), 22 cell 1 ("FREE" tag), 29 cell 6 (faint "$ 1"), and in 38 to 51 numbers never spoken: "$ 18,364" (38), "only 5 in stock!" (38), "$ 14,808" (44), "customer loyalty 87%" (43), "$159,400" and "$1,000,000" (50), "12,480 people already buy" (51). `[S 19 s10-11, S 26 notes, S 22 notes, S 29 notes, S 38 notes, S 43 s15, S 44 s10, S 50 V1-V6, S 51 V1]` Our rule: nothing on screen that is not also true and, for numbers, spoken (see C8, C26).
- **A3.6 Emphasis by word, not by effect.** Emphasis appears as case or quotes: 16 "it IS new" / "it FEELS new", 05 "THE BEST", 36 "Say what people already think.", 27 and 05 keyword in quotes. In the profaura_ videos one key word is set large or in the accent colour: 43 "enemies" large in teal (cell 2), 46 "Selling" with a teal underline (cell 1), 40 stage names as large single words. `[M]`
- **A3.7 Position and font.** Seen in sheets 01, 05, 11, 19, 36 only: white sans-serif; top of frame in 01, 05, 11; lower third in 19; small bottom subtitle in 36. Dim, semi-transparent captions in 11 (cell 7) and 19 (cell 9), likely fade in or out. `[I]` Other videos, 38 to 51 included: unmeasured. Our rule: pick one caption position and keep it for all videos (A8).
- **A3.8 Slip to avoid.** In video 10 cell 6 a white dot covers letters of the word ("conv[t]"). `[S 10 notes]` Our rule: no graphic over caption text.
- **A3.9 Slips: spelling and uncaptioned sentences.** Misspellings on screen: 40 ("Eugence schwartz", "imrpove", "not known" for "not knowing"), 41 ("postive", "dont"), 43 ("you customer"). Spoken sentences with no caption: the last sentence of 40 ("so you can make content that converts them...") runs over the end card with no text; in 42 the closing sentence has no caption either. `[S 40 notes, S 41 notes, S 43 notes, S 42 notes]` Our rule: proofread every caption; every spoken sentence is shown as a caption; the end card starts only after the last sentence.

### A4 Background and colour
- **A4.1 Background near-black** in 611 of 627 content frames (449 of 449 in 01 to 37, 162 of 178 in 38 to 51): median luma at most 18 of 255. 49 of 50 videos are built on near-black. The 16 frames above that: all 7 of video 39 (white background, black text), 2 of 40 (cells 1 and 17, white), 41 cell 1, 45 cell 8 (white), 43 cells 10-11 (photo or clip of a boy and an SUV), 46 cells 12-13 (photos), 49 cell 1 (AI image). The dark remake of the same script (47) shows that the white version is a style choice. `[M 50/50]` In 01 to 37 at least 69 percent of pixels were darker than luma 40 in every frame; the 11 frames below 80 percent dark were frames with a large bright object (08 cell 9, 11 cell 9, 19 cell 10, 22 cells 7 and 9, 36 cells 5-7 and 11-13). The metric does not catch phone clips shown inside a black frame (42 passes it, but its cells 3-12 are real people).
- **A4.2 Colour.** In 01 to 37 only 05 (cells 11 and 12, third-party tool) had strongly coloured pixels (more than 0.3 percent of the frame) outside the platform logo and end card. In 38 to 51, 10 of 13 have them (all except 41, 50, 51): 71 of 178 cells. Most come from pictures: AI footage and photos (42, 43, 46, 48, 49), browser or product mock-ups (38, 40, 44) and one teal-and-red diagram on white (39). The designed colour is one accent: the profaura_ videos use black with one teal accent (owner brief; teal or cyan is named in the captures of 38, 40, 42, 43, 44, 46, 47, 48, 49). Red and green appear as signal colours inside pictures: red prohibition icon and green check (41), red badge (38), one red person icon among white ones (43), red strike-through (46), green bar (38, 44). 50 and 51 are white outline and glow on black with no colour at all (0 coloured frames). `[M 11/50]` for coloured frames, accent family `[S 38 to 49 visuals]`. Our rule: the colour decision in "Owner decisions taken" stands (one accent colour, amber #f5b83d, used sparingly). Good and bad are marked by icon shape and by dim versus glow (A10.4, A10.5), not by extra colours.
- **A4.3 Glow.** A soft glow, light cone or spotlight is named in the visual description in 36 of 50 videos (78 cells; 38 to 51 add 38, 39, 43, 50, 51). `[M 36/50]` (Keywords in Appendix A.)
- **A4.4 Style families.** (a) Minimal: thin white outline icons, dots, rings, lines, glow, drawn objects, text. About 38 of 50 videos (the earlier 32 plus 38, 39, 41, 44, 50, 51). (b) Rendered or photographic content: 11 (silver 3D objects: watch, diamond, hourglass, cart, crystal, balance), 22 (silver coins, crystal, battery icons), 19 (photo-like phone and cans, silhouettes), 05 (third-party logos and UI screenshots), 36 (detailed glowing line illustrations, 91 s), and in 38 to 51: 40 (photo of a man), 42 (clips of real people), 43 (AI footage of women, boy, wine), 45 (hikers, woman, camera and supplement), 46 (man in snow, woman), 48 (photos of men), 49 (AI image of a burning store). 12 of 50. Counts by our reading of `bild.md` and the five sheets, `[I]` for the grouping. **Our rule: family (a) only.** Family (b) is the less safe family: it carries the living beings, real logos and photos that GRUNDSATZ 9 and C16 exclude, and AI footage carries generator marks (43: "MINIMAX | Hailuo AI").

### A5 Icons and the white dot
- **A5.1 White dot / focus point.** A dot appears in the visual description of 34 of 50 videos, in about 23 percent of the roughly 597 visual cells. Dot or white sphere: 36 of 50. Exceptions with neither: 05, 12, 31 and 11 of the 13 new videos (only 50 and 51 use dots; the profaura_ and oktocreative videos work with objects, text and tables instead). `[M 34/50 and 36/50]` Dot in the first cell: 01, 02, 04, 06, 16, 17, 22, 30, 32, 34 (ten), white sphere in 19. Typical roles in the descriptions: centre of rings (06, 08, 24), end of a line (01, 13), mover along a line (30), one of a row (08, 16), marker on a text (20 "The 1P Model"), a cloud of dots that turns into coins (51). Our rule: one dot per scene as the point where the eye lands; the dot never covers text. The dot is a feature of the conversion.doc family, not of every source; we keep it as our own look (A8).
- **A5.2 Icon inventory** (keyword counts, videos out of 50 and cells out of about 597; definitions in Appendix A; 38 to 51 counted on 152 described cells, grouped descriptions such as 46 "[2]-[9]" count once):

| Icon type | Videos | Cells |
|---|---|---|
| circle / ring / concentric rings | 42 | 183 |
| dot / sphere | 36 | 138 |
| line, arc, zigzag, path, dashed line | 42 | 109 |
| square / rectangle / cube / box | 36 | 85 |
| glow / light cone / spotlight | 36 | 78 |
| product objects (bottle, can, tube, razor, phone, drill, lipstick, laptop, watch, cart, battery) | 23 | 46 |
| dollar sign / coin / price tag / percent | 15 | 41 |
| eye | 12 | 15 |
| speech bubble / envelope | 13 | 18 |
| diamond / crystal | 10 | 16 |
| check mark / seal | 12 | 15 |
| brain | 9 | 18 |
| light bulb / lamp | 11 | 12 |
| gear / chart / dashboard / browser window / slider | 13 | 21 |
| cursor / pointer / hand | 13 | 18 |
| triangle | 9 | 13 |
| question mark / X / plus / minus | 10 | 13 |
| hourglass / scale / seesaw / map pin / calendar / globe / ribbon / badge | 12 | 18 |
| star | 8 | 12 |
| face / smiley | 5 | 6 |
| heart | 4 | 6 |
| megaphone | 4 | 4 |
| yin-yang | 3 | 4 |
| real brand logo or product name (curated; 38 to 51 add 39, 40, 44, 45, 46, 49) | 11 | about 20 |
| storefront | 1 | 3 |
| person / head / silhouette / photo of a person (hand-curated; 38 to 51 add 39, 40, 42, 43, 45, 46, 48, 50, 51) | 24 | about 85 |

- **A5.3 The icon is the spoken noun, literally.** `[S visuals + I]` Examples from the station notes: 02 "lipstick" is a lipstick tube; 04 "razors" a razor, "water" a blob; 08 "Netflix show" phone plus monitor, "Leave a gap" two squares with a gap; 22 "It's not about price" a struck-through dollar; 27 "confusion with risk" a brain with question marks, "they buy certainty" a circle with check mark; 34 "don't list 100 features" a stack of lines; 09 "isn't just a logo" an outline Apple logo; 38 "yogurt that says 20% fat" two drawn cups with the two labels, "button that says buy now" a drawn browser window with a "buy now" button; 51 "make it just 5% better" a product card with a "+5%" tag. Our rule: every caption chunk gets an object or shape that shows the same thing; if a noun has no safe object, use a shape or diagram (A5.4).
- **A5.4 Abstract concepts are drawn as diagrams**, not as people: ring split into + and - halves for gain and loss (21 cells 7-8); balance scale for value versus cost (11 cells 12-13) and PRICE versus VALUE (50 cell 7); dashed line turning solid for traffic versus conversion (32 cell 8); lines joining nodes for connection; gears against a paper clip for complex versus simple (50 cells 14-15); a large circle "existing market" against a small crossed-out dashed circle "new market" (51 cell 21). `[S visuals]`
- **A5.5 One main motif per cell.** Most of the roughly 597 cell descriptions name one object or one tight cluster; 50 and 51 state it as "one idea per scene". Not counted exactly. `[I]`
- **A5.6 Faceless pictogram figures.** A person drawn as circle head and rounded body, no face: 37 (cell 1), 43 (cells 7-8, one red among white), 50 (cells 1, 3, 10, 17, 18, 20, 25), 51 (cells 2-4, a grid of 18). Rule 9 does not settle whether they count as drawings of living beings; open owner decision O11. Default until decided: not used.

### A6 Rhythm and motion
- **A6.1 A new graphic roughly every 3 s or faster.** In 01 to 37 every one of 449 sampled cells shows a different graphic from the previous one. The real cut interval is below or equal to 3 s and is unmeasured. `[M 37/37]` For 38 to 51 the captures describe a changed picture in almost every cell; the exceptions are built layouts (46: 24 s, 49: 15 s, 40 table) where a new line or row appears per spoken pair (A10.1, A10.2). Our rule: change graphic with each caption chunk, never hold one static picture longer than about 3 s. `[I]`
- **A6.2 Transitions.** Unmeasurable at 3 s sampling. Hints: mid-motion states (blurred capsules 03, blurred trail 13, 16 blurred dot, 29 faded and blurred number), glowing trails, dimmed captions; in 38 to 51 wipes with coloured bars or ribbons (40 teal bars slide away, 46 a ribbon peels each bar, 49 a sliding box). So animated morphs and fades, not hard cuts to other footage. `[I]` Our rule: morph or fade between graphics; no hard cut to footage, no flashes, no shakes.
- **A6.3 Numbers on screen** are animated or counting (29 cell 4 shows a blurred "$999,112" on the way to "$1000000"; 38 and 44 show a counter bar). `[S 29 notes, S 44 notes]`

### A7 Structure of a single video
- **A7.1 Opening sentence types (37 first sentences, 01 to 37).** "This is why / the reason / how / the ... rule" teaser: 10 (01, 02, 10, 11, 12, 15, 17, 18, 31, 37). Direct statement or claim: 24. Question: 2 (08, 16). Invitation to a game: 1 (28). A number in the first sentence: 1 (32, "99%"). Failure, loss or mistake wording in the first sentence: 9 (01, 02, 17, 23, 25, 30, 31, 32, 34). `[M 37/37]`, classification by hand. 38 to 51 (13 distinct first sentences): "How to sell anything to anyone" 2 (38, 44, the same line); "Psychology says ..." 2 (41, 43); question 2 (45, 46); number in the first sentence 1 (49, "Five words that kill your marketing"); direct statement or claim 6 (39, 40, 42, 48, 50, 51). Failure or loss wording: 3 more (43 "gets ignored", 48 "almost no one shows you how", 49 "kill your marketing"). `[M 13/13]`
- **A7.2 Typical shape.** Hook claim (0 to 3 s), reason or mechanism, instruction sentence at about 18 to 25 s (01 at 18.2 s, 14 at 18.7 s, 21 at 20.8 s, 17 at 21.1 s, 15 at 24.6 s), closing line. `[I]` from a sample of five transcripts, not all 37. Added shapes in 38 to 51: list "First, Second, Lastly" (38, 44), paired examples "do this / not that" (41, 45, 49), one worked example then the rule (40, 48).

### A8 Our own consistency rule
- **A8.1** All videos use one look: near-black background, white outline icons, one dot, one caption style and position, one voice. 38 of 50 sources are family (a) (A4.4). `[S 18 s9, S 03 s6, S 09 s8 + I]` Condition from S 18 s9: a "premium" look must match real quality (no false quality claim).

### A9 What is platform, not design
- **A9.1 TikTok watermark** (moving logo plus the creator handle: "@ conversion.doc", "@ profaura_", "@ oktocreative", "@ cryothum") on every content cell of 50/50. `[M 50/50]` `[P]` It moves between corners. Almost certainly added when a video is saved from TikTok. `[I]` Do not copy it.
- **A9.2 End card.** A dark blue panel with the TikTok logo and a search bar (first empty, then the creator handle) in 50/50 (video 36: frame 30, not in `bild.md`). Sampled in 1 to 2 cells, so about 3 to 6 s. The last 2 s have digital silence (-91 dB) in 50/50. `[M 50/50]` `[P]` Not creator design, and imitating TikTok's search bar is a brand imitation. Our own end card is defined by the P7 script and rule B19.
- **A9.3 No creator logo, intro or outro** appears in any capture; the only identity is the platform handle. `[M 50/50]`
- **A9.4 Ending cut off in the middle of a sentence.** 19 of 50 videos end on a dangling connective in audio (and on screen in 01, 35, 31): 01 "And", 02 "and", 03 and 04 "and this is why", 06 "So...", 08 "But...", 10, 14, 15, 17, 21, 31, 32, 34, 35 "Because...", 12 "And...", 23 "And that's why.", 28 "So...", 29 "because...". (20 if the "So..." that Whisper heard in 36 is counted.) None of the 13 videos 38 to 51 is cut off; all end on a finished sentence (the transcript tails after the speech in 40, 42, 44, 50, 51 are Whisper artifacts). `[M 19/50]` The purpose is unknown. A loop back to the first sentence would be one explanation. `[I]` We do not copy it (C13).

### A10 Reusable devices that keep our rules (from stations 38 to 51)
Each device uses only shapes, text, icons and our own objects (GRUNDSATZ 9). Third-party logos and the people or photos in the same sources are not part of the device.
- **A10.1 Two-column comparison built line by line.** Two stacked blocks, each a stack of bars; a ribbon peels each bar away and one line of text appears per spoken pair, five lines per block over about 24 s ("Selling" and "Storytelling": transactions / transformation, what you offer / why it matters, ...). `[S 46 visuals, cells 2-9]` Use for a true A-versus-B (B19: true alternatives). The line must appear when it is spoken.
- **A10.2 Table built one row per spoken pair.** Two columns "Don't say | Say"; each row fills while its pair is spoken; empty bars show the rows still to come; five pairs in about 15 s. `[S 49 visuals, cells 2-6]` The same build is used for stage names against example searches (40 cells 15-16, empty search bars fill one by one).
- **A10.3 Dotted-line word pairs.** A word sits above a dotted vertical line, the contrasting word below ("customers care" over "product", then "outcome"; "Sell" over "what your product makes possible"). `[S 45 visuals, cells 4-5, 7]`, also 46 (cell 10, brand mark over a dotted line, product crossed out below). In our version the pair is our own words or own objects, never a third-party mark. Silence while two pictures are shown ("buy this or this?", 45) works as a beat.
- **A10.4 Before / after as dim versus glow.** The wrong or old version is dimmed to grey, the right one glows: two yogurt cups (38 cell 4), split screen with the dimmed old price pair left and the bright pair right (38 cell 8), a "buy now" button dimmed, then bright (44 cells 2-3). Fits the glow family (A4.3); no extra colour needed. Brief named 40 for this; its captures show an empty-to-filled build (A10.2), not dimming.
- **A10.5 Live-typed wording with a check or prohibition icon.** The sentence types itself in a framed box; a prohibition icon (circle with slash) marks the weaker wording, a check mark the stronger one; two wordings of each pair side by side. `[S 41 visuals, cells 3-8]` Use shapes in white or the accent, not red and green (A4.2). Both wordings must be true (B36).
- **A10.6 Scenes tied one-to-one to spoken phrases.** One idea per scene of about 3 s: coin chased, iceberg tip, balance PRICE versus VALUE (50); product card that the story keeps changing (copy, +5%, "you"), grid of bubbles that dims, dots turning into coins (51). `[S 50 and 51 visuals]` Sources show no caption here (A3.4); we keep a caption per spoken sentence (A3.9).
- **A10.7 Every spoken sentence needs a caption** (negative device, 40). In 40 and 42 the final sentence is spoken over the end card with nothing on screen; the viewer who is not listening loses the call. `[S 40 notes]` See A3.9.

---

## B. Content rules (from stations rated usable or conditional)

Each rule: what to do, source, the station's condition built in. A rule always sits under GRUNDSATZ 1, 3, 5, 7.

### Hook and attention
- **B1 Say the topic in the first seconds.** "If the brain doesn't immediately know what your content is about, it won't stay long enough to find out." `[S 30 s2 usable]` Also `[S 30 s1, s3 usable]`, `[S 13 s1 usable]` ("stop, feel something, and want to know more, all within a few seconds"), `[S 24 s4 usable]` ("understands immediately why it should care"). Measured: voice starts at 0 s in all 50 sources, a caption in 49 of 50 (A2.1, A3.1). Rule: first caption and first spoken words name the topic; first frame is readable.
- **B2 Attention from clarity, not from volume of posting.** "posting more often doesn't help. It simply multiplies confusion." `[S 24 s6-7 usable]`, "Clarity is what creates relevance." `[S 24 s8-9 usable]`. Rule: one clear video before many videos. Frequency is not a fix for a unclear video.
- **B3 Relatable opening.** "Nobody wakes up and thinks, I want someone to sell me something today." `[S 35 s1 usable]`. Allowed as a hook: a plain observation the viewer agrees with.
- **B4 Questions as hooks.** "Have you ever started a Netflix show and suddenly had to finish the whole season?" `[S 08 s1-2 usable]`. Allowed: a rhetorical question that the same video answers (A7.1: 08, 16).

### One message, clarity
- **B5 One message, one offer, one action.** "It's one message, one offer, one clear action." `[S 34 s4 usable]`, `[S 34 s8 usable]` ("the more options, the more confusion"). Condition `[S 34 s11 conditional]`: one reason in the video, full terms available before purchase. Rule: one idea per video, one action at the end, terms on the sign-up page, no "only one reason" that hides price or conditions.
- **B6 Simple enough for a five-year-old.** "If a five-year-old can't understand what you do, most adults won't either." `[S 10 s3-4 usable]`. And "Not the most creative, not the most detailed, the clearest." `[S 27 s8 usable]`; "If your message takes effort to understand, your offer feels risky." `[S 27 s4 usable]`. Condition `[S 27 s10 conditional]`: "the feeling that you know exactly what you're doing" must be backed by real competence. Measured: median 90 words and 3-word captions (A1.4, A3.3). Scannable by design: `[S 39 s5-6 usable]` "while building a website, make it scannable" and the same for ads; `[S 39 s2 usable]` F and Z reading patterns as a tendency, `[S 39 s3 conditional]` not as an exact path of five stops; `[S 39 s4 conditional]` no permission for spelling errors in our texts. 47 is the same script (duplicate).
- **B7 Answer the three questions fast.** "what is this, will it help me, and can I trust it?" `[S 15 s2 usable]`; "make them understand exactly what they will be getting" `[S 15 s6 usable]`. Rule: what it is (first 5 s), how it helps (middle), why trust (honest status: not finished, free sign-up). Do not use "ahead of 90% of marketers" (`[S 15 s3]`, no source).
- **B8 The video may point at itself when true.** "It explains one simple idea with visuals your brain actually enjoys." `[S 10 s5-6 usable]`.

### Customer, problem, outcome
- **B9 Start from the problem the viewer really has.** "a problem well explained is a solution half sold" `[S 17 s2 usable]`; "People don't care about your business. They only care about it when you make them care." `[S 17 s3 usable]`; `[S 17 s4 conditional]`: relevance and truthful understanding, no manufactured emotion. `[S 37 s3 conditional]`: the problem must be real and relevant to this customer. `[S 37 s4 conditional]`: no exaggeration or fear beyond the real size of the problem. `[S 37 s6 usable]` "if they don't see the problem, they won't see the value".
- **B10 Go where the problem is already felt.** "sell water to the thirsty" `[S 14 s1-2 usable]`. Condition `[S 14 s5 conditional]`: the offer really solves the problem, no use of acute distress, no religious obligation as a market gap (GRUNDSATZ 11). `[S 14 s6 conditional]`: "relief, not persuasion" never means hiding that it is an offer. Which stage the viewer is in: B37; making what already sells slightly better `[S 51 s4 usable]`, with the claim "better" defined and proven `[S 51 s5, s9 conditional]`; value is decided by the outcome and a real reason to pay `[S 50 s6-9 usable, s10 conditional]`.
- **B11 Show the viewer's own situation.** "People listen when they feel seen." `[S 19 s6 usable]`; "Focus on one group of people" `[S 19 s5 usable]`; "the customer becomes the hero" `[S 23 s6 usable]`; "Your product is not the destination, it's the tool." `[S 23 s7 usable]`. Conditions: `[S 19 s8 conditional]` understanding comes from real research, no feigned insight; `[S 23 s8 conditional]` customer stories must be real, no invented customers or testimonials. Visual rule: show the viewer's objects (job ad, letter, calendar), not a person.
- **B12 Research the audience; mirror only true beliefs.** `[S 36 s7 usable]` get to know customers (lawfully, with consent); `[S 36 s9-10 usable]`; `[S 36 s2, s5 conditional]` say only what is true, never reinforce a false belief; `[S 36 s11-12 conditional]` fit and understanding must be real.
- **B13 Sell the realistic "after".** "They don't buy the gym membership. They buy who they'll become after going there." `[S 02 s5 conditional]` and "start painting their future" `[S 02 s7 conditional]`. Condition: the future shown is realistic and attainable with the product; no promise of a result the product does not deliver (`[S 02 s6]`: confidence as an experience, no promised compliments). Outcome example that is usable: `[S 33 s4 usable]` the drill is bought for the hung picture.
- **B14 The instant benefit.** `[S 29 s8 conditional]`: usable if the benefit is real and the long-term cost is not hidden. `[S 29 s10 conditional]`: only benefits that really arrive early (for example a first result in the first session). `[S 29 s9 not usable]`: no result promise with a time ("Lose weight in 30 days").

### Emotion, loss, relief
- **B15 Emotion first, truthful.** "People buy emotions and justify with logic." `[S 11 s8 usable]`; "sell the feeling first and the product second" `[S 12 s8 conditional]`: product and terms still stated. `[S 11 s2 conditional]`: real function and terms still stated. `[S 25 s6 conditional]`: emotion is truthful, not manufactured. `[S 25 s8 usable]`: "If people don't feel something, they won't remember anything." Express the emotion by text, voice, objects, shapes. Never by a drawn person.
- **B16 Show the cost of not acting only if real.** "Show them what they are already losing by not acting." `[S 21 s7 conditional]`; "To each goal, there is also an anti-goal." `[S 11 s6 usable]`, `[S 11 s5 conditional]`. Condition: each loss shown is factual and demonstrable; no invented loss, no deadline, no scarcity. `[S 09 s11 conditional]`: no fear claim beyond what can be shown. `[S 11 s10 conditional]`: fear of missing out only about real, verifiable losses. `[S 38 s12, s14 conditional]`: "only a few left" only when it is true and current; no stock counter such as "only 5 in stock!" that is not the real stock (C8, C26).
- **B17 Relief wording.** "People don't buy solutions. They buy relief." `[S 37 s2 usable]`. Never with the shaming frame of `[S 37 s1 not usable]`.
- **B18 Authenticity.** `[S 12 s6-7 conditional]`: "authentic" must be real, not staged. We have no real customer voices yet, so we show none (C20).

### Contrast, priming, open loops
- **B19 Contrast with true alternatives.** "Your brain can't judge value in isolation." `[S 26 s2 usable]`. `[S 26 s1, s8 conditional]`: comparison consists of true alternatives. `[S 26 s5 conditional]`: an anchor is only a real price that is actually charged and is disclosed as such (najsh). Allowed form for us: identical generic letter next to a tailored letter. Not allowed: invented "was" prices, decoy prices, wine example (C11).
- **B20 Context before the offer, not a hidden hook.** Restate `[S 06 s1 conditional]` as "create context before the offer". `[S 06 s4 usable]` a comfort scene before furniture. `[S 06 s3, s6, s7 conditional]`: the primed context is true, the offer fully disclosed, hints never hide terms. No people or families (`[S 06 s5 conditional]`).
- **B21 Open a loop only on content.** "Start it, leave a gap, and let curiosity do the rest." `[S 08 s11 conditional]`. Conditions: the loop is on content, never on price or terms (`[S 08 s8-10 conditional]`), and the gap is filled truthfully inside the video, no unpaid teaser. Source note: the sources themselves cut off 19 of 50 endings (A9.4), which breaks this condition; we do not copy it (the 13 videos 38 to 51 all end on a finished sentence).
- **B22 Content-led discovery, intent visible.** "Make them feel like they found it." `[S 35 s8-9 conditional]`: the commercial intent is not hidden, the decision stays informed, no disguised advertising. `[S 35 s7 conditional]`: no false claims or hidden terms behind the "obvious decision".

### Price, terms, trust
- **B23 Price as perceived value, with full cost.** "Your job is to raise their understanding and therefore increase the perceived value." `[S 22 s7 conditional]` with true information, no inflated value. `[S 22 s6 conditional]`: if the product is overpriced for its value, correct the price, do not defend it. `[S 11 s9 conditional]`: all costs (price, terms, effort) disclosed. If a price is mentioned: price, duration, renewal and cancellation together (GRUNDSATZ 3). Current P7 decision: 9.90 EUR one-time for 30 days, no renewal, always worded as "geplant".
- **B24 Lower the felt cost by real ease.** "Use a simple checkout" `[S 01 s6 usable]`; guarantee `[S 01 s7 conditional]` must be real, conditions in plain words, honoured; trial `[S 01 s8 conditional]`: duration, end, whether payment data is taken, whether it renews. `[S 01 s5 conditional]`: never lower the pain by hiding price or terms. Reciprocity: `[S 44 s7 usable]` giving value first; `[S 44 s6 conditional]` a free trial, sample or resource states duration, price afterwards and how to cancel, is really free and collects no hidden data.
- **B25 Trust through certainty.** "people don't buy risk. They buy certainty." `[S 27 s5-6 usable]`. For us certainty is the honest status line: planned, not finished, free sign-up.
- **B26 Look as good as the product is.** "if you want to be seen as premium, make everything look premium." `[S 18 s9 conditional]`: appearance matches real quality. `[S 18 s5-6 usable]`: weak design makes the offer feel weak. `[S 03 s6 conditional]`: the emotions triggered are not produced by false claims. Perception is not a licence to misrepresent (`[S 18 s10]`, `[S 20 s10]`, both conditional).
- **B27 Social proof only if genuine.** `[S 36 s13 conditional]`: testimonials, case studies and reviews genuine, verifiable, used with consent. `[S 36 s15 conditional]`: data real, cited, not cherry-picked. We have none yet; show none (C20). `[S 44 s4 conditional]`: five-star reviews only if real, from real buyers.

### Call to action
- **B28 One call to action, last sentence, with its content stated.** Sources: DM calls in 05, 10, 13; comment-keyword calls in 24, 25, 27, 30. Conditions: `[S 24 s10, S 25 s10, S 27 s11, S 30 s5 conditional]` state what the offer is and what happens with the contact; `[S 10 s9, S 13 s5 conditional]` price and scope stated when a service is offered; `[S 05 s8 conditional]` trial terms stated. `[S 13 s7 usable]` "DM to get started" as a plain action is usable. The keyword is also shown as caption text (24 cell 11 grey "Attention", 27 cell 12 'Comment the word "attention"', 05 cell 14 'DM me "PARTICL"'). Measured: only 8 of 50 videos have any call to action (48 adds a comment call: "drop the best one in the comments"). 42 of 50 end without one. `[M 8/50]`

### Claims, statistics, effects
- **B29 No unsourced number.** `[S 15 s3]` "90% of marketers", `[S 21 s3]` "twice as powerful", `[S 32 s1]` "99% of businesses", `[S 01 s1-3]`, `[S 04 s7]`: all rated "claim, unverified". Figures shown as results with no source are `[not usable]`: `[S 43 s15]`, `[S 44 s10]`, `[S 50 V1-V3, V6]`, `[S 51 V1]` (C26). The stations rate many sentences "usable" only as framing. Our rule: no statistic and no absolute ("always", "never", "best", "number 1") without proof (GRUNDSATZ 5). Mechanisms such as loss aversion are worded as tendencies. `[I]`
- **B30 Named effects.** `[S 08 s4]`, `[S 18 s3]`, `[S 20 s4]` name effects without source. Using a name is allowed, but we check the spelling and say "often", not "always". Source video 08 spells "Zagarnik"; that is probably Zeigarnik (our own knowledge, check before use). `[I]`
- **B31 Funnel thinking.** "You either have a conversion problem or a traffic problem." `[S 32 s3 usable]`. Videos are traffic, the sign-up page is conversion; measure separately. Condition `[S 32 s7 conditional]`: do not dismiss legal, ethical or quality problems.
- **B32 Study what works, with public material only.** `[S 05 s2 usable]`, `[S 05 s4 conditional]`: only publicly available material, nothing behind logins or against terms. `[S 05 s5-6 conditional]`: any paid or affiliate relation disclosed.
- **B33 Brand consistency across videos.** `[S 03 s6 conditional]`, `[S 09 s8 usable]` ("clear and consistent"): every video uses the A8 look. `[S 07 s2]` marketing gets attention, branding makes people remember; a repeated look is the branding part.

### Technique wording (from stations 38 to 51)
- **B34 The "So You Can" formula.** "You take your product or feature, add So You Can, and then finish with the outcome." `[S 48 s5 conditional]` Example form: "a home alarm system so you can feel safe at night" `[S 48 s6 conditional]`. Conditions: the outcome is what the product really delivers for the typical customer and not more ("feel safe" must not promise protection beyond the product; write "fewer distractions", not "no distractions", `[S 48 s7 conditional]`); product, price and terms stay stated, the outcome is a real need `[S 48 s8 conditional]`. The hook of the same video, "make people feel dumb saying no to your product", is not usable (C28). Fits B7 ("will it help me") and B13.
- **B35 Word swaps only if the new word is true.** Avoid "best", "only here", "must have" and a bare "sale" where nothing proves them `[S 49 s2, s4, s6, s8, s10 usable]`. The replacement is allowed only if it is true `[S 49 s3, s5, s7, s9, s11 conditional]`: "start now" says what happens (account, payment, trial) before the click; "top rated" needs real ratings with source and number; "exclusive" only if the offer is not available elsewhere; "special offer" only for a real reduction or real extra, no invented was-price; "essential" only if truly necessary. A swap that restates the same unproven claim in a softer word is deception (GRUNDSATZ 1, 5).
- **B36 Say the negative first, with full terms.** "Start with the negative and end with the positive." `[S 41 s7 conditional]` The negative (price, limit, condition) is a real fact, stated completely and clearly, and not drowned by the positive ending; the positive ending is true `[S 41 s1, s7 conditional]`. Saying "really expensive" openly is usable `[S 41 s3 conditional]`; "the best in the world" needs proof `[S 41 s2 conditional]`. A money-back promise `[S 41 s5-6 conditional]` follows B24 and also defines the period, what counts as "the results you want", how to claim and how fast the refund comes. The claim that people remember the last thing most `[S 41 s8 usable]` contradicts S 30 (the beginning): owner decision O12.
- **B37 Match the message to the audience's awareness stage.** "each stage requires different types of content" `[S 40 s3, s12 usable]`; the four stages unaware, problem aware, solution aware, product aware `[S 40 s9, s11 usable]`. Conditions: the stage comes from real research on the audience, not an assumption, and nothing guarantees conversion `[S 40 s13 conditional]`; the video names four stages while the model is commonly described with five, so check the source before attributing it and do not name or show the person `[S 40 s2 conditional]`; examples are non-medical, no diagnosis `[S 40 s4, s6]`. Our use `[I]`: write the stage in the script header. The "unaware" stage conflicts with B10 / S 14: owner decision O13.
- **B38 A common enemy is a problem or a condition, never people.** Laziness, being average, cars that use gas `[S 43 s9-11 usable]` are the permitted form. The "enemy" is a real problem the viewer has, named truthfully at its real size, with no invented threat and said openly `[S 43 s1, s7, s12, s13 conditional]`. Never a person, a group, a competitor's people or customers; bonding by hating a person is backbiting and is not used as an example `[S 43 s4-5 conditional]` (C29). "Every cult brand" and "trick" are not our wording (C9). The aim is loyalty from real value `[S 43 s8 conditional]`.

---

## C. GRUNDSATZ filter: patterns we must NOT copy

Each entry: pattern, where it appears, rule that stops it.

| ID | Pattern | Where it appears (station, cell) | Rule |
|---|---|---|---|
| C1 | Person icons, figures, heads, silhouettes, crowds | 24 videos, about 85 cells (38 to 51 add 39 cell 2, 40 cells 3-5, 42 cells 3-12, 43 cells 3-4, 6-8, 10, 45 cells 1 and 6, 46 cells 12-13, 48 cells 1, 3, 4, 8, 9, 50 and 51 pictograms, see C24 and O11): 02 (cell 5 head, cell 11 two persons), 06 (cell 9 three persons), 07 (cell 6 grid of persons), 09 (cell 2), 11 (cells 3, 5, 15), 12 (cells 1-4, 6, 12-14, hooded figure included), 14 (cell 3), 19 (cells 2, 3, 9-11), 25 (cell 7 head with tie), 26 (cells 6-7 person with tie), 27 (cell 2), 33 (cell 8 screen showing people), 35 (cells 1-2), 36 (cells 6, 10-24, many heads), 37 (cell 1) | GRUNDSATZ 9: no drawings or animations of living beings. Not even an icon. |
| C2 | Hands and handshakes | 08 cell 1 (hand with phone), 09 cell 7 (hand cursor), 19 cells 10-11 (hand reaching, clasped hands), 36 cells 7 and 13, 44 cell 4 (hand cursor on "buy now") | GRUNDSATZ 9, default avoid. Owner decision O5 for a plain cursor arrow. |
| C3 | Photographs of people, photo thumbnails | 05 cell 11 (screen capture with photo thumbnails) | GRUNDSATZ 9. No photos in our videos. |
| C4 | Women | No capture records a woman. Statement level: 02 s6 (lipstick, "compliments"), 06 s5 (happy families), 12 s5 (someone happy to drink a Coke) | GRUNDSATZ 10 and 9. Our own prohibition, not a measured pattern. Choose other examples (no lipstick, no families, no drinkers). |
| C4a | Faces and borderline body icons | smiley or upset face: 12 cell 8, 14 cell 8, 21 cell 4, 23 cell 1, 25 cell 6; eye 12 videos, brain 9 videos (A5.2) | Owner decision O5. Default avoid faces; eye and brain avoided until the owner decides. The P7 list does not include them. |
| C5 | Music and sound beds | Cannot be proven or excluded from the audio analysis (A2.7). Louder pauses in 06, 08, 36 (and borderline 15) are unexplained. 42 cell 7 shows a burned-in "(music playing)" in an embedded clip. | GRUNDSATZ 8: no music. Voice, soft interface sounds and silence only. Listen to those videos before using any sound design from them. |
| C6 | TikTok watermark and TikTok search-bar end card | 37/37 (A9) | Platform artifact, imitation of a third-party brand. Do not copy. |
| C7 | Superlatives, outcome promises, hype words | 05 s9 "the best" (cell 15 caption THE BEST), 13 s6 "moves minds" and "hypnotize" (cell 11 caption), 36 s17 "watch your business explode", 07 s6 "watch your business grow", 31 s1 "reason most businesses fail", 04 s2 "illusion sold by coaches" (motive attributed to a group) | GRUNDSATZ 5 and 1. Only with proof. |
| C8 | Fake urgency, scarcity, anchors, exclusivity, unspoken prices | 05 s7 "should not miss this" (no stated deadline); 11 s10 fear of missing out; 38 s12-14 "only a few left in stock" with a badge "only 5 in stock!" (the 5 never spoken); 21 s7 invented loss; 26 s5 anchoring and cell 7 prices $150 and $80 not spoken; 28 s4 "only sold in selected stores"; 22 cell 1 "FREE" tag with no audio | GRUNDSATZ 1 and 4. No deadline, no "only X left", no number of users or sign-ups, no "was" price. |
| C9 | Manipulation wording and covert influence | 36 s1 "easily manipulate your customers" (cell 1 shows this caption) not usable; 37 s1 "make people feel dumb saying no" not usable (cell 1 caption); 12 s1 "dark psychology"; 06 s3 "without them ever realizing it"; 12 s9 "subconsciously" (cell 14 caption); 43 s8 "trick" and "cult brand"; 48 s2 (see C28); 26 s6 "This isn't manipulation"; 35 s9 "not like you sold it"; 14 s6 "not like persuasion"; 37 s5 "without them having to move a finger" | GRUNDSATZ 7 and 6. Allowed: priming, contrast, loss framing, open loops when true and nothing is concealed. Not allowed: the aim of moving a person against their interest, shaming, concealed sales intent. Never use the words "manipulate", "dark psychology", "subconscious", "hypnotize" about our own method. |
| C10 | Illusion of innovation | 16 s5 "complexity to create curiosity" not usable, 16 s9 "because it feels new" not usable (cells 12-13 captions "it IS new" and "it FEELS new"), fancy invented names in 16 cell 4 | GRUNDSATZ 1, ghish. No new-sounding names for ordinary things, no feigned novelty. Station 16 s6 is used only as an observation to avoid misleading. |
| C11 | Wine, alcohol examples and the "same product at 21 times the price" logic | 26 s4, 28 s2-12 (28 s11 not usable), 44 s9 and cells 9-10 (shirt "$5" against "$25", "paying five times more for the same thing", not usable) | Order of authority 1. No alcohol in any example. Identical products are never presented as different in quality. |
| C12 | Time-bound result promise | 29 s9 "Lose weight in 30 days" not usable (cell 10 dial "30") | GRUNDSATZ 1 and 5. Our case: no "in 30 Sekunden fertig", no "garantiert". |
| C13 | Ending cut off on a connective | 19 of 50 videos (A9.4) | B21 and B5: the loop must be paid off, the last sentence is complete. Purpose unknown (`[I]`). |
| C14 | Calls to action that hide the funnel | 24, 25, 27, 30 ("Comment the word attention" with no stated offer), 05 (DM for a trial, no trial terms, no disclosure), 10 and 13 (DM, no price or scope) | B28 and GRUNDSATZ 3. |
| C15 | Undisclosed affiliation | 05 (third-party tool; neither audio nor captions say whether the creator is paid) | `[S 05 s5 conditional]`. We do not promote third-party tools in these videos. |
| C16 | Third-party logos, products, brand names on screen | 05 (Skims, Lululemon, Gymshark, Particl), 09 and 34 (Apple outline), 19 (Samsung phone, Pepsi and Coca-Cola cans), 28 (Walmart), 04 (razor), 39 (Apple store page), 40 (YouTube and Google logos, photo of a named person), 44 (Nike-style swoosh on a shirt), 45 (Canon camera, ON supplement), 46 (Nike, Patagonia, Aesop as brand examples), 49 (Blockbuster sign) | Our own rule, `[I]`: no third-party logo or product image. P7 script already says competitor names are never shown or spoken. Station 19 s3-4 and 34 s5 name brands as examples; use generic objects instead. |
| C17 | Absolutes without proof | "never", "always", "at all", "only": 04 s1, s3, s8; 19 s2-4; 20 s8; 22 s1; 27 s7; 33 s2 | GRUNDSATZ 5; B29. |
| C18 | Unsourced statistics | 15 s3 (90 percent), 21 s3 ("twice"), 32 s1 (99 percent), 01 s1-3, 04 s7; see also C26 | B29. |
| C19 | Staged emotion or "raw and real" authenticity | 12 s6-7 | `[S 12 s6-7 conditional]`: not produced by scripted fake testimonials or actors. |
| C20 | Testimonials, reviews, data as social proof | 36 s13, s15 | B27. None until real ones exist. |
| C21 | Calls on desire for a pain that belongs to religion | none found in the sources | GRUNDSATZ 11. Listed so it stays checked. |
| C22 | Loss-framed claim beyond evidence | 09 s11 "miss the most important opportunity", 01 s1 "lose your customers in the last second" | B16, B29. |
| C23 | Financing or ads in the app | none found in the sources | GRUNDSATZ 2 and 13. Listed so it stays checked. |
| C24 | Photos, AI footage and clips of people or their bodies | 40 cells 3-5 (photo of a man), 42 cells 3-12 (clips of four men, one lifting his shirt), 43 cells 3, 4, 6 (AI clip of women in a club, generator mark "MINIMAX / Hailuo AI") and cell 10 (a boy jogging, shown as the picture of "laziness"), 45 cells 1 and 6 (hikers, woman at a mattress), 46 cells 12-13 (man in snow, woman touching her cheek), 48 cells 1, 3, 4, 8, 9 (photos, intruder silhouette) | GRUNDSATZ 9 and 10; C1, C3. No photo, no AI footage of people, no clip of strangers, and no person shown as the picture of a vice or a feeling. |
| C25 | Alcohol in an example picture | 43 cell 6 (wine glasses in the AI clip) | Order of authority 1; extends C11. |
| C26 | Invented or unsourced figures on screen or in the voice | "$ 18,364" (38 cell 1), "$ 14,808" (44 cell 1), "customer loyalty 87%" (43 cell 14), "THE GOAL $159,400", "$1,000,000", "$0", EFFORT 0%, VALUE 15% (50), "12,480 people already buy", "+5%", "105%" (51), "only 5 in stock!" (38), spoken view counts 900, 29 million, 500, 7 million (42) | B29, C8, C18; GRUNDSATZ 1 and 5. A figure appears only if it is real, sourced and spoken; an example is labelled as an example. |
| C27 | Bundle with a false "free" | 38 s8 not usable: "buy a bag for $49 and get a new watch for free" at the same total price (cell 8: $49.99 = $49.99) | GRUNDSATZ 1 and 4 (ghish, najsh). "Free" only for something that costs nothing extra. A bundle shows the real single prices and a real saving. |
| C28 | Shaming hook "feel dumb saying no" | 48 s2 not usable ("make people feel dumb saying no to your product"); the same hook as 37 s1 (C9) | GRUNDSATZ 7; C9. No shaming and no pressure as the aim. |
| C29 | An enemy that is a person or group; hatred as the bond | 43 s4-5 (two strangers bond by hating a third person), 43 s1 (a brand needs "enemies") | B38. Only a problem or a condition may be named as the enemy. |

---

## O. Owner decisions (contradictions between stations)

These come from `INDEX.md` ("Statements that contradict each other") and from the picture questions the stations raise (O11). The default satisfies both sides where possible. The owner may change any default.

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
- **O11 Faceless pictogram figures.** A person drawn as circle head and rounded body without a face, used in 37 (cell 1), 43 (cells 7-8, one red among white), 50 (7 cells) and 51 (cells 2-4, a grid of 18). `[S 50 visuals, S 51 visuals]` GRUNDSATZ rule 9 says no drawings or animations of living beings; the rule text does not settle whether a faceless pictogram is one. Default until the owner decides: not used (viewers shown as dots, circles, objects or a text label instead). **Decided by the owner (2026-10-28): not used, also written into GRUNDSATZ rule 9.**
- **O12 End with the positive (41) or the beginning matters more (30).** `[S 41 s8]` people remember the last thing most versus `[S 30]` the beginning matters more than the end. Default: the first sentence names the topic (B1); a negative (price, limit) is said in the middle in full (B36); the last sentence is a true positive plus the single action (B28). Both claims are unverified. **Decided (2026-10-28, IDEEN.md section 13): this default applies.**
- **O13 Address the "unaware" audience (40) or only people who already feel the problem (14).** Default: videos speak to problem-aware viewers (B9, B10); the first seconds show the problem so that an unaware viewer becomes problem aware (B37, S 37); no invented need and no created demand. **Decided (2026-10-28, IDEEN.md section 13): this default applies.**

---

## D. Checklist before publishing (answer yes or no; any "no" means do not publish)

1. Voice starts at 0.0 s and a caption is visible in the first frame (A2.1, A3.1)?
2. Do first caption and first sentence say what the video is about (B1)?
3. Is there exactly one message and exactly one action (B5)?
4. Is every number on screen also true, spoken and real, and every spoken number sourced or labelled as an example (B29, C18, C26)?
5. Is the background near-black and everything on screen white, grey or silver plus at most the one approved accent colour, with no white background and no other colour (A4, owner decision on colour)?
6. Is there no person, face, head, hand, silhouette, figure, pictogram figure (until O11 is decided) or photo, AI footage or clip of a living being (C1, C2, C3, C24)?
7. Is no woman depicted or implied by an example (C4)?
8. Are eye, brain, smiley and cursor icons absent unless the owner has allowed them (O7)?
9. Is no music in the audio, only voice, soft interface sounds or silence (C5)?
10. Is there no TikTok watermark, search bar or imitation of any platform end card (C6)?
11. Are there no third-party logos, product images, competitor names or alcohol examples (C11, C16, C25)?
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
25. Is every spoken sentence shown as a caption, spelled correctly, with the end card starting only after the last sentence (A3.9)?
26. If the video uses a technique: is the "so you can" outcome real (B34), is every swapped word true (B35), is the negative stated in full and a guarantee defined (B36), is the audience stage written in the script header (B37), and is any "enemy" a problem and not a person (B38, C29)?
27. Has the video been re-read against GRUNDSATZ rules 1 to 11 and the owner decisions O1 to O13?

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
| 38 | B16, C8, C26, C27, A10.4 |
| 39 | B6 (scannable layout), A4.1 (white background version) |
| 40 | B37, A3.9, A10.2, A10.7, C24, O13 |
| 41 | B36, A10.5, O12 |
| 42 | B15, B13, C24, C26 |
| 43 | B38, C24, C25, C26, C29 |
| 44 | B24, B27, C11, C26 |
| 45 | B13, A10.3, C24 |
| 46 | A10.1, A10.3, C16, C24 |
| 47 | duplicate of 39 (counted once; form differences in A4.1, A5.6) |
| 48 | B34, C24, C28 |
| 49 | B35, A10.2, C16 |
| 50 | B13, A10.6, A5.6, C26, O11 |
| 51 | B10, B31, A10.6, A5.6, C26, O11 |

Form rules A come from the captures of all 50 distinct videos (47 counted with 39), with the exceptions named in each rule.

---

## F. What the sources do that a typical motion-graphics template does not

- Little colour: black, white, grey in most sources; the profaura_ videos add one teal accent, 50 and 51 have none. A template would add several colours.
- One voice, no music, pauses that are quiet. A template adds a music bed.
- Captions are 3 words, not full sentences, and are mirrored by one literal object each (50 and 51 use no captions, only labelled scenes).
- No logo, no brand intro, no lower third, no outro of our own. (The visible end card is TikTok's.)
- Call to action in 8 of 50 videos only. A template adds one to every video.
- 19 of 50 end on a cut-off connective (none of 38 to 51). A template ends on a closed sentence and a CTA.
- Most videos are 27 to 44 s including a 3 to 6 s platform tail (35 of 50).

## G. Differences between `video/p7-skripte.md` and the measurements (file not changed)

- **Length.** P7: 20 to 40 s. Sources: file length 27.2 to 43.5 s in 35 of 50, with a platform tail we do not have. The P7 end card is 5 to 6 s of our own content, so the tail is longer than the platform tail (median 4.4 s). The 20 s lower end is covered: the shortest sources are 21.0 s (49) and 24.2 s (39).
- **End card speech rate.** The P7 end card voice sentence has about 25 German words for 5 to 6 s, which is about 4 words/s. The English sources run 2.06 to 3.74 words/s (median 2.58). The end-card text has three lines for 5 to 6 s, while sources show about 3 words per 3 s. Shorten or lengthen the end card (A2.2, A3.3).
- **Hook.** P7 hook "Ein Anschreiben für alle Stellen?" is 5 words and matches the measured "up to 5 words in 89 percent". First-sentence length: sources have a first segment of median 3.3 s; P7 says "in the first 2 s".
- **Style.** P7 style (near-black, outline icons, one dot, white sans-serif line every 3 s) matches 38 of 50 sources `[M]` (family (a)). P7 allowed icons (circle, square, line, check, X, envelope, document, magnifier, calendar, lock, coin, clock, arrow, mockup) all occur in the sources, except that lock and clock appear only as a keyhole mark (09 cell 16) and a clock-hand shape (09 cell 6). P7 excludes persons, hands, figures; measurement confirms 24 source videos use persons, heads, pictograms or photos and 5 use hands (08, 09, 19, 36, 44), so the exclusion is a real departure from the source style.
- **Sounds.** P7 allows soft interface sounds (tick, click, whoosh). The sources: unmeasured. The P7 sounds are our choice `[I]`.
- **Call to action.** P7 puts the same end card on all 10 videos. Sources: 8 of 50 have a CTA. Own decision, justified by GRUNDSATZ 1 and B22 (intent visible). Not a copy.

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

Keyword search for 38 to 51 ran over the 152 described cells of their `bild.md` (end-card cells skipped). The yin-yang hit in 39 is a false hit and is not counted. Keyword counts can over- or under-count (for example "glow" inside a description of an unrelated object). They show family and order of magnitude, not exact counts. The person list is not keyword-based: it was read cell by cell from the grep output of person, figure, head, silhouette, crowd, hand and handshake descriptions.

## Owner decisions taken
- **Colour and design (2026-10-28):** the owner does not require black. The source look (near-black, white, one dot; 36/37 videos in 01 to 37; the 13 videos 38 to 51 add the profaura_ pattern of black with one teal accent, 49 of 50 videos are built on near-black) stays the base for clarity, but our videos get **one own accent colour** for the focus dot and key words, so they are recognisable as ours and do not copy the source creator's identity. Background: dark (near-black or dark blue-grey). Accent: one colour, used sparingly. Set in video 1 and approved by the owner (2026-10-28): background #0b0f14, ink #ffffff, dim #4d5560, accent amber #f5b83d, font Inter. Kept for all videos.
- **Voice (2026-10-28):** ElevenLabs voice "Knurps" (owner's "Meine Stimmen") for all videos from now on; replaces Balduin. The character behind the brand is voice, name, wording and personality only (GRUNDSATZ rule 9).
