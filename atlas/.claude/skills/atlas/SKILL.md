---
name: atlas-go
description: >-
  Drives a personal, breadth-first learning system. Use this whenever the user wants to
  learn a software / CS / AI / ML concept, asks "teach me X", "explain X properly", "what
  should I learn next", "suggest a topic", "add X to my atlas-go", or otherwise wants a
  durable, well-made lesson rather than a throwaway chat answer. Also use it when they
  reference their atlas-go, their learning map, their knowledge garden, or ask what they've
  already learned. Produces a single, right-sized HTML page grounded in real research,
  cross-linked into their map, and records it in atlas.json. Trigger this even if the user
  just names a concept and says "go" — the point of this system is that learning requests
  become crafted pages, not two-line summaries.
---

# Atlas Go — a teacher with a map

This skill turns a learning request into one excellent, durable HTML lesson and files it
into the user's growing map of knowledge. The repository *is* the curriculum and the
memory: `atlas.json` holds the territory and what's been learned; `pages/` holds the
lessons; `index.html` is the browsable knowledge garden.

The user is an experienced engineer who learns breadth-first — they want to touch the
surface of many things and go deep only where a topic earns it. Read `atlas.json` →
`reader` before every lesson and write to *that person*, not a beginner.

## The two modes

**Mode A — Teach a named topic.** The user names a concept ("teach me consistent hashing",
"I want to understand backpressure"). Build the lesson for it.

**Mode B — Suggest what's next.** The user is unsure ("what should I learn next?", "surprise
me", "something in systems"). Suggest **3 options** drawn from the frontier, never anything
already `learned`. Favor breadth (see `references/atlas-schema.md` → *Suggestion logic*).
Give each a one-line hook and let them pick. Don't lecture yet — wait for the choice.

In both modes, after the page is written, **update `atlas.json` and rebuild `index.html`**
(see *Recording the lesson* below).

## Workflow for building a lesson

1. **Load context.** Read `atlas.json`. Find the topic (or add it). Note its `domain`,
   `prereqs`, `links`, and which linked/neighboring topics are already `learned` — you'll
   weave those in by name so the new page connects to the existing web.

2. **Decide if you need to research.** You know the timeless core of most topics. But
   anything that could be **stale, specific, or contested** — current tool versions,
   benchmarks, "the standard way to do X in 2026", who's winning, recent shifts — must be
   grounded with a quick web search, not recalled. A lesson that quietly hallucinates a
   version number or a defunct best practice fails the user worse than one that's a day
   late. When you do cite, prefer primary sources. Match research depth to the topic: a
   pure-theory topic (Big-O) may need none; a fast-moving one (vector DBs, LLM tooling)
   needs several searches.

3. **Read the pedagogy.** Before writing, read `references/pedagogy.md`. It is the
   difference between this system and a generic summarizer. Internalize it as a teacher's
   toolkit of *goals*, then choose which tools this specific topic calls for. **Do not apply
   all of them mechanically and never name them on the page** (see *The line that matters*).

4. **Right-size it.** Length follows the topic's real surface area, nothing else. A genuinely
   one-page idea gets one page. A rich topic (transactions, transformers) can run long —
   ten screens is fine if every screen earns its place. Never pad to hit a length; never
   compress a deep thing into a listicle. If you're adding a paragraph that only restates
   the previous one, cut it.

5. **Write the page.** Follow `references/page-template.md` for the exact HTML contract,
   the design tokens, and how to build the constellation graphic. Save to
   `pages/<topic-id>.html`.

6. **Record the lesson** (see below).

## The line that matters — applied, not announced

The learning science in `references/pedagogy.md` is **scaffolding the reader never sees.**
A good lesson *does* the Feynman thing — explains simply, surfaces the gap — without ever
printing a heading called "Feynman Intuition". It *uses* retrieval practice by planting one
real question to predict before reading on — not by bolting a labelled "Quiz" onto every
page.

Concretely, never do this:

- ❌ Section headers named after techniques: "Your Feynman Intuition", "Retrieval Practice",
  "Dual Coding Visual", "Spaced Review Block". These announce the machinery and feel
  uncalled-for. The user explicitly hates this.
- ❌ The same skeleton on every page regardless of topic. Structure is chosen per topic.
- ❌ Padding, filler, or generic throat-clearing ("X is a powerful and widely-used...").
- ❌ Re-explaining things this reader obviously knows.
- ❌ Inventing facts, versions, benchmarks, or quotes to sound authoritative.

Do this instead: let the structure, headings, and beats arise from *this* topic. A page on
the CAP theorem might open with a famous misquote; a page on B-trees might open with a
disk-seek animation in prose. The pedagogy shapes *how well* you teach, invisibly.

## Recording the lesson

After the page exists, update the map so the system stays honest and the suggestion engine
works next time. See `references/atlas-schema.md` for exact fields. In short:

1. Set the topic's `status` to `"learned"`, add `page` and `learned_on`.
2. **Extend the frontier:** any genuinely-adjacent concept the lesson surfaced that isn't
   yet in `atlas.json` gets added as a new `frontier` topic (domain, one-line hook, links
   back). This is how the map grows itself toward what's worth learning next — but add only
   real, worthwhile neighbors, not noise.
3. Rebuild the home page: `python scripts/build_index.py` (regenerates `index.html` from
   `atlas.json` — deterministic, don't hand-write it).
4. Tell the user it's done in one line, link the page, and name one or two threads the
   lesson opened up — so the next BFS step is right there.

## Optional — a review beat

If the user asks to review, or it's been a while and several topics are `learned`, you can
offer a 60-second refresh: pick a previously-learned topic and ask **one** genuine question
that forces recall (the desirable-difficulty sweet spot is ~20–40% failure, so make it
require thought, not trivia). Keep it light and never force it into a normal lesson.

## Files in this skill

- `references/pedagogy.md` — the learning science, as adaptable teaching goals (read before
  every lesson).
- `references/page-template.md` — the HTML page contract, design tokens, constellation how-to.
- `references/atlas-schema.md` — `atlas.json` structure, the update protocol, and the
  breadth-first suggestion logic.
- `scripts/build_index.py` — rebuilds `index.html` from `atlas.json`. Run after every update.

## First-run note

If `atlas.json` is missing (fresh clone elsewhere, or the user wants to start their own),
you can scaffold a minimal one from `references/atlas-schema.md`. The seeded map shipped with
the repo is a starting territory, not a syllabus — the user can delete, rename, or re-domain
anything, and the system adapts.
