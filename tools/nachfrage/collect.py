"""Collects posts where people state a need themselves (Reddit via Arctic Shift, Hacker News via Algolia).

Usage: python -I tools/nachfrage/collect.py [reddit|hn ...]
Output: quellen/nachfrage/raw/<source>.jsonl (one post per line, deduplicated by id, resumable).
No usernames are stored.
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "quellen" / "nachfrage" / "raw"
CFG = json.loads((Path(__file__).parent / "config.json").read_text(encoding="utf-8"))
UA = {"User-Agent": "new-projekt-research/0.1"}


def get(url, tries=6):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                d = json.load(r)
            if d.get("error"):
                raise RuntimeError(d["error"])
            return d
        except Exception as e:
            wait = 3 * (i + 1)
            print(f"  retry {i + 1} in {wait}s: {e}", flush=True)
            time.sleep(wait)
    return None


class Store:
    def __init__(self, name):
        RAW.mkdir(parents=True, exist_ok=True)
        self.path = RAW / f"{name}.jsonl"
        self.seen = set()
        if self.path.exists():
            # split("\n"), not splitlines(): post texts can contain U+2028 and similar separators.
            for line in self.path.read_text(encoding="utf-8").split("\n"):
                if line.strip():
                    self.seen.add(json.loads(line)["id"])
        self.f = self.path.open("a", encoding="utf-8")

    def add(self, rec):
        if rec["id"] in self.seen:
            return False
        self.seen.add(rec["id"])
        self.f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        self.f.flush()
        return True


def reddit():
    st = Store("reddit")
    done_path = RAW / "reddit_done.txt"
    done = set(done_path.read_text(encoding="utf-8").splitlines()) if done_path.exists() else set()
    fields = "id,title,selftext,score,num_comments,created_utc,subreddit"
    skip = set(CFG.get("reddit_skip_subs", []))
    for sub in CFG["subreddits"]:
        if sub in skip:
            continue
        for phrase in CFG.get("reddit_phrases", CFG["phrases"]):
            key = f"{sub}|{phrase}"
            if key in done:
                continue
            # The archive matches loose words, not the exact phrase; cap pages so broad pairs cannot dominate.
            after, new = CFG["since"], 0
            for _ in range(CFG.get("reddit_max_pages", 2)):
                q = urllib.parse.urlencode({"subreddit": sub, "query": phrase, "after": after, "limit": 50,
                                            "sort": "asc", "fields": fields})
                d = get(f"https://arctic-shift.photon-reddit.com/api/posts/search?{q}")
                time.sleep(CFG.get("reddit_sleep", 1.5))
                if not d or not d["data"]:
                    break
                for p in d["data"]:
                    new += st.add({"src": "reddit", "id": "r_" + p["id"], "sub": p["subreddit"], "phrase": phrase,
                                   "title": p["title"], "text": p.get("selftext") or "", "score": p["score"],
                                   "comments": p["num_comments"], "created": p["created_utc"],
                                   "url": "https://www.reddit.com/comments/" + p["id"]})
                if len(d["data"]) < 50:
                    break
                after = d["data"][-1]["created_utc"] + 1
            print(f"reddit {sub} | {phrase}: +{new}", flush=True)
            with done_path.open("a", encoding="utf-8") as f:
                f.write(key + "\n")


def hn():
    st = Store("hn")
    since = int(time.mktime(time.strptime(CFG["since"], "%Y-%m-%d")))
    for phrase in CFG["phrases"]:
        for tag in ("story", "comment"):
            new, page = 0, 0
            while page < 20:
                q = urllib.parse.urlencode({"query": f'"{phrase}"', "tags": tag, "hitsPerPage": 100, "page": page,
                                            "numericFilters": f"created_at_i>{since}"})
                d = get(f"https://hn.algolia.com/api/v1/search?{q}")
                time.sleep(0.5)
                if not d or not d["hits"]:
                    break
                for h in d["hits"]:
                    text = h.get("comment_text") or h.get("story_text") or ""
                    new += st.add({"src": "hn", "id": "h_" + h["objectID"], "sub": tag, "phrase": phrase,
                                   "title": h.get("title") or h.get("story_title") or "", "text": text,
                                   "score": h.get("points") or 0, "comments": h.get("num_comments") or 0,
                                   "created": h["created_at_i"],
                                   "url": f"https://news.ycombinator.com/item?id={h['objectID']}"})
                page += 1
                if page >= d.get("nbPages", 0):
                    break
            print(f"hn {tag} | {phrase}: +{new}", flush=True)


if __name__ == "__main__":
    for name in sys.argv[1:] or ["hn", "reddit"]:
        {"reddit": reddit, "hn": hn}[name]()
