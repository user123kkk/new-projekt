# new-projekt

Source base for finding and building an app. Every decision is measured against [GRUNDSATZ.md](GRUNDSATZ.md).

## Structure
- `quellen/` – raw sources. `videos/NN/` holds transcript, visual capture and frame overview per video. Video files stay local.
- `stationen/` – one station per source: verbatim text, every statement, assessment, links.
- `begriffe/` – concepts linking the stations.
- `INDEX.md` – overview of stations, concepts and clusters.
- `map/index.html` – graph of all stations and concepts. Open in a browser.
- `tools/` – `transkribiere.py` (local Whisper), `build_map.py` (regenerates the map).
- [PROZESS.md](PROZESS.md) – how new sources are added.

The folder can also be opened directly as an Obsidian vault.
