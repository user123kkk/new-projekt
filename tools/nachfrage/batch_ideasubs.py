"""Batches Reddit posts from request/idea subreddits that the phrase filter dropped.

In these subreddits a post is usually a request by itself, so the exact phrase is not required.
Usage: python -I tools/nachfrage/batch_ideasubs.py [batch_size]
Output: quellen/nachfrage/batches/batch_1NN.jsonl (numbering starts at 101).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "quellen" / "nachfrage" / "raw" / "reddit.jsonl"
OUT = ROOT / "quellen" / "nachfrage" / "batches"
SUBS = {"SomebodyMakeThis", "AppIdeas", "Lightbulb", "Startup_Ideas"}

sys.path.insert(0, str(Path(__file__).parent))
from prefilter import BLOCK  # noqa: E402


def main():
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    taken = set()
    for f in OUT.glob("batch_0*.jsonl"):
        for line in f.read_text(encoding="utf-8").split("\n"):
            if line.strip():
                taken.add(json.loads(line)["id"])
    posts, seen = [], set()
    for line in RAW.read_text(encoding="utf-8").split("\n"):
        if not line.strip():
            continue
        p = json.loads(line)
        text = (p.get("text") or "").strip()
        if text in ("[removed]", "[deleted]"):
            text = ""
        if p["sub"] not in SUBS or p["id"] in taken or p["id"] in seen:
            continue
        if BLOCK.search(f"{p['title']} {text}"):
            continue
        seen.add(p["id"])
        posts.append({"id": p["id"], "src": p["src"], "sub": p["sub"], "title": p["title"],
                      "text": re.sub(r"<[^>]+>", " ", text)[:1500], "score": p["score"],
                      "comments": p["comments"], "url": p["url"]})
    for old in OUT.glob("batch_1*.jsonl"):
        old.unlink()
    for i in range(0, len(posts), size):
        (OUT / f"batch_{101 + i // size:03d}.jsonl").write_text(
            "\n".join(json.dumps(p, ensure_ascii=False) for p in posts[i:i + size]) + "\n", encoding="utf-8")
    print(json.dumps({"kept": len(posts), "batches": (len(posts) + size - 1) // size}))


if __name__ == "__main__":
    main()
