"""Prefilters raw posts and splits them into batches for classification.

Usage: python -I tools/nachfrage/prefilter.py [batch_size]
Input:  quellen/nachfrage/raw/*.jsonl
Output: quellen/nachfrage/batches/batch_NNN.jsonl and stats on stdout.
Only removes posts that are clearly empty, removed, or off-limits by GRUNDSATZ.md; judgement is left to classification.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "quellen" / "nachfrage" / "raw"
OUT = ROOT / "quellen" / "nachfrage" / "batches"

# Clearly off-limits domains (GRUNDSATZ.md). Matched on whole words in title + text.
BLOCK = re.compile(
    r"\b(casino|gambl\w*|betting|sportsbook|poker|slots?|dating app|tinder|hinge|bumble|onlyfans|porn\w*|nsfw|"
    r"beer|wine|brewing|cocktail|liquor|vodka|whisk(e)?y|payday loan|music production|beat ?making|spotify playlist)\b",
    re.I,
)


def main():
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 150
    posts, seen_titles = [], set()
    stats = {"raw": 0, "removed_empty": 0, "no_phrase": 0, "removed_block": 0, "dup_title": 0}
    for f in sorted(RAW.glob("*.jsonl")):
        for line in f.read_text(encoding="utf-8").split("\n"):
            if not line.strip():
                continue
            p = json.loads(line)
            stats["raw"] += 1
            text = (p.get("text") or "").strip()
            if text in ("[removed]", "[deleted]"):
                text = ""
            if not p.get("title") and len(text) < 40:
                stats["removed_empty"] += 1
                continue
            # Reddit archive search matches loose words; keep only posts that contain the phrase itself.
            if p["src"] == "reddit" and p["phrase"].lower() not in f"{p.get('title', '')} {text}".lower():
                stats["no_phrase"] += 1
                continue
            if BLOCK.search(f"{p.get('title', '')} {text}"):
                stats["removed_block"] += 1
                continue
            key = re.sub(r"\W+", " ", (p.get("title") or text[:120]).lower()).strip()
            if key in seen_titles:
                stats["dup_title"] += 1
                continue
            seen_titles.add(key)
            posts.append({"id": p["id"], "src": p["src"], "sub": p["sub"], "title": p.get("title", ""),
                          "text": re.sub(r"<[^>]+>", " ", text)[:1500], "score": p["score"],
                          "comments": p["comments"], "url": p["url"]})
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("batch_*.jsonl"):
        old.unlink()
    for i in range(0, len(posts), size):
        (OUT / f"batch_{i // size + 1:03d}.jsonl").write_text(
            "\n".join(json.dumps(p, ensure_ascii=False) for p in posts[i:i + size]) + "\n", encoding="utf-8")
    stats["kept"] = len(posts)
    stats["batches"] = (len(posts) + size - 1) // size
    print(json.dumps(stats))


if __name__ == "__main__":
    main()
