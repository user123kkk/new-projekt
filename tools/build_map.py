"""Builds map/index.html: an Obsidian-style graph of stationen/ and begriffe/ from their [[links]].

Usage: python tools/build_map.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[\[([^\]|#]+)")


def collect():
    nodes, edges = {}, set()
    for kind, folder in (("station", "stationen"), ("concept", "begriffe")):
        for f in sorted((ROOT / folder).glob("*.md")):
            text = f.read_text(encoding="utf-8")
            title = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), f.stem)
            nodes[f.stem] = {"id": f.stem, "kind": kind, "title": title, "path": f"{folder}/{f.name}", "text": text}
    for src, n in nodes.items():
        for target in LINK.findall(n["text"]):
            target = target.strip()
            if target in nodes and target != src:
                edges.add(tuple(sorted((src, target))))
    return list(nodes.values()), [{"source": a, "target": b} for a, b in sorted(edges)]


def main():
    nodes, edges = collect()
    html = (ROOT / "tools" / "map_template.html").read_text(encoding="utf-8")
    html = html.replace("/*DATA*/", json.dumps({"nodes": nodes, "links": edges}, ensure_ascii=False))
    out = ROOT / "map" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"{len(nodes)} nodes, {len(edges)} links -> {out}")


if __name__ == "__main__":
    main()
