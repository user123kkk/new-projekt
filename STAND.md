# Stand (handoff for the next session)

Updated: 2026-10-28. Read this first, then GRUNDSATZ.md, IDEEN.md (sections 10-14), VIDEO-REGELN.md.

## Where we are
- Sources: stations 01-51 done (47 = duplicate of 39). Map: `python -I tools/build_map.py`.
- Demand search done: NACHFRAGE.md (2,437 demand posts, 132 clusters).
- Idea: P7 (job applications) dropped by the owner: fails K9 (recurring need). Idea choice is OPEN.
- Excluded by owner: learning for students, language learning, calorie tracking.
- Not excluded, candidates: household/couple budget, weekly meal plan without calories, receipts for small firms, P2 photo report for tradespeople, others still to find.
- Owner rules added: no pictogram figures (GRUNDSATZ rule 9); character = voice + personality only; voice "Knurps" (ElevenLabs, "Meine Stimmen"); colours #0b0f14 / #ffffff / #4d5560 / accent #f5b83d, font Inter; marketing before features; slideshows are a valid content format.
- Reusable assets: test-p7/ (sign-up page, Impressum, privacy draft, Cloudflare Pages function), video/p7-01 (HyperFrames video, 11 beats), video/p7-skripte.md.

## In progress when the last session ended
- New sources 52 and 53 (YouTube, downloaded to quellen/videos/52|53/video.mp4, frames every 10 s in frames/):
  - 52: "How I Find App Ideas People Will Actually Pay For!!" (SJCodes, 9:15), youtu.be/x9TFKNgaDjo
  - 53: "100,000 App Downloads From TikTok Slideshows" (Arthur Spalanzani, 16:13), youtu.be/NgsLwjkNo7A
- Transcription: 52 done; 53 was running (`tools/transkribiere.py 52 53`, log quellen/transkribiere_52-53.log). If 53 has no transkript.txt, rerun: `HF_HUB_DISABLE_SYMLINKS_WARNING=1 PYTHONIOENCODING=utf-8 /c/Users/USER/.venvs/whisper/Scripts/python -I tools/transkribiere.py 53`

## Next steps, in order
1. Stations 52 and 53 by a Sonnet agent, same prompt as for 38-51 (PROZESS.md, verbatim, every statement rated by GRUNDSATZ, bild.md from frames at 10 s intervals — note the deviation). The owner wants every tip taken apart word by word: these videos carry experience details.
2. Integrate into INDEX, begriffe, map, VIDEO-REGELN (slideshow format rules from 53), IDEEN (idea-finding method from 52).
3. Idea round with the owner using the method from 52 + K1-K9, then copycat plugin (copycat:copycat, red/blue team) and venture:devils-advocate on the top 1-2.
4. Decide the first thing to start; marketing and branding start early, features stay minimal.

## Working rules
- Owner language German, plain, short (caveman on). Docs in English.
- Routine work to Haiku/Sonnet subagents; Opus only for decisions.
- Check long background runs in the first 10-15 min; report deviations.
- Idea choice is the owner's decision; discuss before going deep.
