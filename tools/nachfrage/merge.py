"""Merges demand-true classifications into one compact file for clustering.

Usage: python -I tools/nachfrage/merge.py
Output: quellen/nachfrage/demand.jsonl and stats on stdout.
Drops records with a GRUNDSATZ flag, quotes that are not verbatim, duplicates by quote,
and the areas listed in EXCLUDE_IDS (judged by hand: circumvention, piracy, covert surveillance).
"""
import glob
import html
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
N = ROOT / "quellen" / "nachfrage"
# Reviewed by hand: age-verification spoofer, shadow-library search (ghish / taking others' rights).
EXCLUDE_IDS = {"r_1r14927", "r_1ge8xou", "r_1itz1ft"}
# Title-only "alternative to X?" states no need (CLASSIFY.md); classifiers judged these inconsistently.
BARE_ALTERNATIVE = re.compile(r"^\W*(\w+\W+){0,3}alternatives?\s+(to|for)\b", re.I)


def lines(path):
    return [json.loads(l) for l in Path(path).read_text(encoding="utf-8").split("\n") if l.strip()]


def main():
    stats = {"demand": 0, "flagged": 0, "bad_quote": 0, "bare_alternative": 0, "excluded": 0, "dup_quote": 0}
    out, seen = [], set()
    for f in sorted(glob.glob(str(N / "classified" / "batch_*.jsonl"))):
        src = {p["id"]: p for p in lines(N / "batches" / os.path.basename(f))}
        for o in lines(f):
            if not o.get("demand"):
                continue
            stats["demand"] += 1
            p = src[o["id"]]
            hay = html.unescape(f"{p['title']} {p['text']}").lower()
            quote = html.unescape(o.get("quote", ""))
            if o.get("flag", "none") != "none":
                stats["flagged"] += 1
            elif quote.lower() not in hay:
                stats["bad_quote"] += 1
            elif len(p["text"].strip()) < 40 and BARE_ALTERNATIVE.search(p["title"]):
                stats["bare_alternative"] += 1
            elif o["id"] in EXCLUDE_IDS:
                stats["excluded"] += 1
            elif quote.lower() in seen:
                stats["dup_quote"] += 1
            else:
                seen.add(quote.lower())
                out.append({"id": o["id"], "src": p["src"], "sub": p["sub"], "problem": o["problem"],
                            "who": o["who"], "product": o["product"], "pain": o["pain"], "pay": o["pay"],
                            "tools": o.get("tools", []), "quote": quote, "score": p["score"],
                            "comments": p["comments"], "url": p["url"]})
    (N / "demand.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in out) + "\n",
                                    encoding="utf-8")
    stats["kept"] = len(out)
    print(json.dumps(stats))


if __name__ == "__main__":
    main()
