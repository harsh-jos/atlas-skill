#!/usr/bin/env python3
"""
build_index.py — regenerate index.html (the knowledge garden) from atlas.json.

Deterministic on purpose: the skill edits atlas.json, then runs this. No hand-editing
of index.html. Run from the repo root:  python scripts/build_index.py
"""
import json
import html
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ATLAS = ROOT / "atlas.json"
OUT = ROOT / "index.html"


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def main() -> int:
    if not ATLAS.exists():
        print(f"error: {ATLAS} not found", file=sys.stderr)
        return 1
    try:
        data = json.loads(ATLAS.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"error: atlas.json is not valid JSON — {e}", file=sys.stderr)
        return 1

    meta = data.get("meta", {})
    domains = data.get("domains", [])
    topics = data.get("topics", [])

    learned = [t for t in topics if t.get("status") == "learned"]
    total = len(topics)
    n_learned = len(learned)
    n_domains_touched = len({t["domain"] for t in learned})
    pct = round(100 * n_learned / total) if total else 0

    by_domain = {d["id"]: [] for d in domains}
    orphans = []
    for t in topics:
        bucket = by_domain.get(t.get("domain"))
        (orphans if bucket is None else bucket).append(t)

    # domains ordered by the atlas; topics within: learned first, then frontier, alpha by title
    def topic_sort(t):
        return (0 if t.get("status") == "learned" else 1, t.get("title", "").lower())

    name = esc(meta.get("name", "Atlas"))
    subtitle = esc(meta.get("subtitle", "a breadth-first map of the things worth knowing"))

    parts = []
    parts.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — your knowledge garden</title>
<link rel="stylesheet" href="assets/atlas.css">
</head>
<body>
<main class="page">

  <header class="home-head">
    <h1 class="wordmark">{name}</h1>
    <p class="tagline">{subtitle}</p>
    <div class="stats">
      <div class="stat"><div class="n">{n_learned}</div><div class="l">learned</div></div>
      <div class="stat"><div class="n">{total}</div><div class="l">on the map</div></div>
      <div class="stat"><div class="n">{n_domains_touched}<span style="color:var(--ink-faint);font-size:1.4rem">/{len(domains)}</span></div><div class="l">domains touched</div></div>
    </div>
    <div class="progress-track" style="max-width:520px"><div class="progress-fill" style="width:{pct}%"></div></div>
  </header>
""")

    for d in domains:
        ts = sorted(by_domain.get(d["id"], []), key=topic_sort)
        if not ts:
            continue
        d_learned = sum(1 for t in ts if t.get("status") == "learned")
        parts.append(f"""
  <section class="domain">
    <h2>{esc(d['name'])} <span class="count">{d_learned} / {len(ts)}</span></h2>
    <p class="blurb">{esc(d.get('blurb',''))}</p>
    <div class="cards">""")
        for t in ts:
            status = t.get("status", "frontier")
            klass = "card learned" if status == "learned" else "card frontier"
            hook = esc(t.get("hook", ""))
            title = esc(t.get("title", t.get("id", "")))
            sub = esc(t.get("subdomain", ""))
            label = "learned" if status == "learned" else status
            inner = f"""
        <div class="c-name">{title}</div>
        <div class="c-meta"><span class="glyph"></span>{esc(sub)} · {label}</div>
        <div class="c-hook">{hook}</div>"""
            if status == "learned" and t.get("page"):
                href = esc(t["page"])
                parts.append(f'      <a class="{klass}" href="{href}">{inner}\n      </a>')
            else:
                parts.append(f'      <div class="{klass}">{inner}\n      </div>')
        parts.append("    </div>\n  </section>")

    if orphans:
        parts.append('\n  <section class="domain"><h2>Unfiled</h2><div class="cards">')
        for t in sorted(orphans, key=topic_sort):
            parts.append(
                f'    <div class="card frontier"><div class="c-name">{esc(t.get("title",""))}</div>'
                f'<div class="c-hook">{esc(t.get("hook",""))}</div></div>'
            )
        parts.append("  </div></section>")

    parts.append(f"""
  <footer class="home-foot">
    {n_learned} learned · {total} mapped · rebuilt {date.today().isoformat()} ·
    edit <code>atlas.json</code> and run <code>scripts/build_index.py</code> to refresh
  </footer>

</main>
</body>
</html>
""")

    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} — {n_learned}/{total} learned across "
          f"{n_domains_touched}/{len(domains)} domains")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
