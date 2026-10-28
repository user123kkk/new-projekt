# Process: ingesting sources

Applies to the first videos and to every video added later.

## 1. Intake
- Copy the video to `quellen/videos/NN/video.mp4` (next free number).
- Add it to `quellen/index.csv`: `NN,original_filename`.
- Check for duplicates by MD5. Duplicates are not ingested.
- Video files stay local (`.gitignore`). Only text goes into the repo.

## 2. Capture
- Audio: `python -I tools/transkribiere.py NN` (local Whisper, `large-v3-turbo`), writes `transkript.txt` with timestamps and `transkript.json`.
- Image: one frame every 3 seconds in `frames/`, overview in `frames_uebersicht.jpg`. On-screen text and visuals are captured from these.
- The transcript is checked against the on-screen text. Differences are marked, not silently corrected.

## 3. Station
- One station per video: `stationen/NN-title.md`.
- Content: original text verbatim, every single statement as its own point, visual content, links.
- Assessment, sentence by sentence: usable, conditional, not usable. If only a small part is usable, only that part is taken over. The standard is [GRUNDSATZ.md](GRUNDSATZ.md).

## 4. Linking
- Obsidian-style links `[[NN-title]]` between stations and to concepts in `begriffe/`.
- Map: `map/index.html` is generated from the links.

## 5. Update the rulebooks
- A new station that says something about video form, editing or motion graphics updates [VIDEO-REGELN.md](VIDEO-REGELN.md): new or changed rule with the station id, counts re-measured.
- A new station about selling or ideas updates the criteria in [IDEEN.md](IDEEN.md) if it changes one.
- Existing videos are re-checked against the updated checklist before the next one is published.
