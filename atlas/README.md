# Atlas

A personal, breadth-first learning system. One repo that is, at the same time, your
**curriculum**, your **memory**, and your **second brain** — driven by a Claude Code skill
that teaches you one well-made page at a time and remembers everything you've covered.

It exists to answer the hardest question in self-teaching: *what don't I know that I should?*
Atlas keeps a map of the territory, lights up the parts you've walked, and always has a
defensible answer for where to go next.

---

## What it actually does

You talk to it inside Claude Code. Two things happen:

- **"Teach me consistent hashing"** → it researches what it needs to, writes a single
  right-sized HTML lesson into `pages/`, marks the topic learned in `atlas.json`, wires the
  new page into your map, and rebuilds the home page.
- **"What should I learn next?"** → it looks at everything you *haven't* covered, biases
  toward breadth (domains you've barely touched) and unlocked prerequisites, and offers a few
  real options with a one-line hook each. You pick. It teaches.

Open `index.html` in a browser at any point to see the whole map: every domain, every topic,
what's learned, what's frontier.

## Why it's built the way it is

**The repo is the memory — not a model's session memory.** `atlas.json` is the single source
of truth: the topic map, what's learned, prerequisites, and the links between topics. It's
plain JSON, version-controlled, and you can hand-edit it. Because it lives in git, your
learning history is durable, diffable, and yours.

**Pages are sized to the topic, not to a word count.** A small idea gets one screen. A big one
(say, transformers) gets as many pages or sections as it actually needs. Length follows the
real surface area of the subject — never a target.

**The learning science is applied, never announced.** The skill is grounded in real cognitive
research — Feynman-style plain explanation, Bjork's *desirable difficulties* (retrieval,
spacing, productive struggle), dual coding (concrete before abstract, words + relevant
visuals). But you'll never see a section literally titled "Your Feynman Intuition." The
techniques shape the writing invisibly; they are scaffolding the reader isn't meant to notice.
The full rationale lives in `.claude/skills/atlas/references/pedagogy.md`.

## Layout

```
atlas/
  atlas.json              the map + memory: domains, topics, status, prereqs, links
  index.html              the home map — GENERATED, never hand-edited
  assets/atlas.css        the design system (one file; retheme here)
  pages/                  one HTML lesson per learned topic
  scripts/build_index.py  rebuilds index.html from atlas.json
  .claude/skills/atlas/
    SKILL.md              the teacher's brain (modes, workflow, the rules that matter)
    references/
      pedagogy.md         learning science as adaptable goals, not a template
      page-template.md    the page contract: fixed shell, free interior
      atlas-schema.md     atlas.json schema + the next-topic (BFS) logic
```

## Using it

1. **Open the repo in Claude Code.** The skill in `.claude/skills/atlas/` is picked up
   automatically.
2. **Ask it to teach or to suggest.** "Teach me CRDTs", "explain MVCC properly", or "I don't
   know what to learn — suggest something."
3. **Read the page** it writes into `pages/`, linked from the home map.
4. **Watch the map fill in.** Each lesson updates `atlas.json` and regenerates `index.html`.

To rebuild the home page yourself at any time:

```bash
python3 scripts/build_index.py
```

It reads `atlas.json` and writes `index.html`. The skill runs this for you after each lesson;
you'd only run it by hand after editing `atlas.json` directly.

## Seeding your own topics

`atlas.json` ships with ~95 topics across 12 domains as a starting territory. Add your own by
appending objects to the `topics` array (see `references/atlas-schema.md` for the shape):

```json
{
  "id": "raft",
  "title": "Raft Consensus",
  "domain": "concurrency",
  "status": "frontier",
  "hook": "How a cluster agrees on one truth without a single boss.",
  "prereqs": ["leader-election"],
  "links": ["paxos", "consensus"]
}
```

Set `status` to `frontier` for things you want to learn, `learned` for things you already
know (so the skill stops suggesting them). Re-run the build script and they appear on the map.

## The design system

One CSS file, `assets/atlas.css`, deliberately avoiding the usual generated-UI defaults. It
uses a warm paper-and-ink palette with a single confident indigo accent (reserved for *you
are here* / active / frontier), and a three-typeface system:

- **Fraunces** — display headings
- **Newsreader** — reading body
- **JetBrains Mono** — labels, chrome, and code

Retheming is a one-file change: swap the font `@import` and the `--font-*` / color variables at
the top of `atlas.css` and the whole system follows. The signature element is the **knowledge
constellation** — a small graph on each lesson showing the topic among its neighbors, with the
ones you've learned filled in. It's there to serve the "map of the territory" goal, not for
decoration.

---

Built to be lived in. Learn one good page at a time; let the map remember the rest.
