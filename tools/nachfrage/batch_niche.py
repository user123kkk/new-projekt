"""Batches Reddit posts from niche subreddits that are not in any batch yet (round 2).

Keeps only posts that contain the search phrase itself, as in prefilter.py.
Usage: python -I tools/nachfrage/batch_niche.py [batch_size]
Output: quellen/nachfrage/batches/batch_2NN.jsonl (numbering starts at 201; existing 2NN files are kept).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "quellen" / "nachfrage" / "raw" / "reddit.jsonl"
OUT = ROOT / "quellen" / "nachfrage" / "batches"
IDEA_SUBS = {"SomebodyMakeThis", "AppIdeas", "Lightbulb", "Startup_Ideas", "SideProject"}

sys.path.insert(0, str(Path(__file__).parent))
from prefilter import BLOCK  # noqa: E402


def lines(path):
    return [json.loads(l) for l in path.read_text(encoding="utf-8").split("\n") if l.strip()]


def main():
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    taken, titles = set(), set()
    for f in OUT.glob("batch_*.jsonl"):
        for p in lines(f):
            taken.add(p["id"])
            titles.add(re.sub(r"\W+", " ", p["title"].lower()).strip())
    posts = []
    for p in lines(RAW):
        text = (p.get("text") or "").strip()
        if text in ("[removed]", "[deleted]"):
            text = ""
        hay = f"{p['title']} {text}"
        key = re.sub(r"\W+", " ", p["title"].lower()).strip()
        if p["sub"] in IDEA_SUBS or p["id"] in taken or key in titles:
            continue
        if p["phrase"].lower() not in hay.lower() or BLOCK.search(hay):
            continue
        taken.add(p["id"])
        titles.add(key)
        posts.append({"id": p["id"], "src": p["src"], "sub": p["sub"], "title": p["title"],
                      "text": re.sub(r"<[^>]+>", " ", text)[:1500], "score": p["score"],
                      "comments": p["comments"], "url": p["url"]})
    start = 201 + len(list(OUT.glob("batch_2*.jsonl")))
    for i in range(0, len(posts), size):
        (OUT / f"batch_{start + i // size:03d}.jsonl").write_text(
            "\n".join(json.dumps(p, ensure_ascii=False) for p in posts[i:i + size]) + "\n", encoding="utf-8")
    print(json.dumps({"kept": len(posts), "first": start, "batches": (len(posts) + size - 1) // size}))


if __name__ == "__main__":
    main()
