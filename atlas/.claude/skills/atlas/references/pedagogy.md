# Pedagogy — how to actually teach a topic

This is the difference between Atlas and a summarizer. Read it before every lesson.
Everything here is a **goal**, drawn from cognitive science. None of it is a section to
print. You pick the goals this topic needs and meet them invisibly. (See SKILL.md → *The
line that matters*.)

The reader is a sharp engineer learning breadth-first. The job of a page is to take a
concept they've maybe only heard the name of and leave them with a real mental model, a
sense of where it sits on the map, and the judgment to know when to reach for it.

---

## What the research says (and why these goals)

A handful of findings in cognitive science are unusually robust and unusually relevant to
writing a lesson. Brief, so you know *why* each goal exists:

- **The fluency illusion is the enemy.** Re-reading and highlighting feel like learning but
  mostly build short-term familiarity, not durable memory. The Bjorks' work on *desirable
  difficulties* shows that conditions which make learning feel harder in the moment —
  effortful retrieval, spacing, interleaving, generating an answer yourself — produce better
  long-term retention and transfer. A page that's smooth to skim can leave nothing behind.
  So: build in *some* friction the reader has to push through.

- **Storage strength ≠ retrieval strength.** A memory can be well-stored yet hard to access;
  the *effort* of accessing it is what strengthens future access. This is why making the
  reader predict or reconstruct something beats handing it to them. The useful target is a
  *productive* struggle — roughly 20–40% failure, reaching not flailing — never a wall.

- **Concrete before abstract (dual coding & the concreteness effect).** People encode and
  recall concrete things far better than abstract ones, and pairing a verbal explanation
  with a *relevant* visual builds two retrieval paths instead of one (Paivio). Lead with a
  vivid concrete anchor — a scenario, an object, a number — then generalize. A diagram earns
  its place only when it clarifies structure or relationship; decoration adds load and
  subtracts trust.

- **Explaining simply exposes the gaps (Feynman).** The discipline of explaining a thing in
  plain language, without leaning on jargon, is what reveals where understanding is thin.
  Write as if explaining to a smart peer who's never met this concept: define the
  non-obvious terms, refuse to hand-wave. If you can't put it plainly, you don't yet
  understand it well enough to teach it — go research until you can.

- **Knowledge is a web, not a list (transfer & mental models).** Concepts that are connected
  to what the learner already knows transfer to new situations; isolated facts don't. Every
  lesson should locate the topic on the map — its neighbors, its kin, its opposites — and
  tie back to topics already `learned`. This is also what makes breadth-first learning
  compound instead of evaporate.

You don't need to cite any of this on the page. It's the reason the page is shaped the way
it is.

---

## The teaching goals (a toolkit, not a checklist)

Reach for the ones this topic needs. A small idea might need three of these; a big one might
need all of them across ten screens. The *order* is a strong default, not a law.

**1. Open on the itch, not the definition.** Start with the problem the topic exists to
solve, or the surprising thing about it. What pain predated it? What breaks without it?
Curiosity is a gap between what you know and want to know — open that gap in the first two
sentences. Never open with "X is a technique used to…".

**2. Anchor it concretely.** Before the abstraction, give one vivid, specific instance — a
real scenario, a tiny worked example, a physical analogy that actually holds. Make it
something the reader can *picture*. Then lift from the instance to the general principle.

**3. Build the model.** Now the actual mechanism, explained plainly enough that the reader
could re-explain it. This is the core. Define the non-obvious terms inline. Use a diagram or
the constellation only where structure genuinely needs to be *seen*.

**4. Locate it on the map.** Where does this sit? What's it a cousin of, an alternative to,
a building block for? Name the neighbors — especially ones the reader has already learned —
and draw the contrasts ("unlike a queue, a log doesn't delete on read…"). This is the
breadth payoff and it belongs on nearly every page.

**5. The engineer's lens — trade-offs and when *not* to use it.** This is what separates a
decision-maker from a vibe-coder, and it's this reader's favorite part. Costs, failure
modes, the situation where the obvious choice is wrong, what you'd reach for instead. Be
specific and honest. A page that only sells the concept is incomplete.

**6. One real beat of effort.** Where it fits naturally — not on every page — plant a single
moment that makes the reader *do* something: predict an outcome before you reveal it, spot
why a tempting approach breaks, reconstruct the next step. One good beat beats five weak
ones. It should feel like a question a good teacher drops mid-explanation, not a quiz.

**7. Leave threads to pull.** Close by naming a couple of honest next rabbit holes this
opens — the adjacent unknowns. Not a link dump; one or two "if this hooked you, look at…"
that genuinely follow. These feed the frontier and the reader's next BFS step.

---

## Calibration

- **Depth matches the topic, never a target length.** Right-sizing *is* the skill. Refuse
  both failure modes: the bloated essay that pads a simple idea, and the listicle that
  flattens a deep one.
- **Respect the reader's level.** Don't define "API" or "thread" for this audience. Do
  define the genuinely new primitive. When unsure, assume competence and explain the *new*
  thing well.
- **Specific beats clever.** Concrete numbers, real tool names, actual trade-offs. Cut every
  sentence that could appear unchanged on a page about a different topic.
- **Voice:** a brilliant senior engineer explaining something they love over coffee —
  precise, unhurried, a little opinionated, zero filler. Warm, not whimsical. It can have a
  point of view ("most teams reach for this too early") as long as it's earned.
- **Honesty about uncertainty.** If something is contested or version-dependent, say so
  plainly rather than flattening it into false confidence.

The test for a finished page: would *this specific reader* come away able to explain the
idea to a colleague, know when to use it, and feel one notch more curious than when they
started — with nothing on the page that reads as boilerplate? If yes, ship it.
