# atlas-go.json — schema, updates, and the suggestion logic

`atlas-go.json` is the single source of truth: the territory, what's learned, and how topics
connect. It's plain JSON on purpose — version-controlled, diffable, hand-editable. The user
owns it and can re-domain, rename, or prune anything.

## Schema

```jsonc
{
  "meta":   { "name", "subtitle", "version", "created" },
  "reader": { "level", "wants", "respect" },   // read before every lesson; write to this person
  "domains": [
    { "id", "name", "blurb" }                  // id is a slug used by topics
  ],
  "topics": [
    {
      "id":        "consistent-hashing",        // slug; also the page filename
      "title":     "Consistent Hashing",
      "domain":    "systems",                   // must match a domain id
      "subdomain": "distribution",              // free-text, short
      "status":    "frontier",                  // "frontier" | "learned" | "seen"
      "hook":      "Add a server without reshuffling everything.",  // one line, specific
      "prereqs":   ["hash-tables"],             // topic ids that should ideally come first
      "links":     ["sharding", "gossip"],      // related topic ids (the constellation/web)

      // present once learned:
      "page":      "pages/consistent-hashing.html",
      "learned_on":"2026-06-21"
    }
  ]
}
```

Status meanings:
- **frontier** — on the map, not yet learned. Fair game to suggest/teach.
- **learned** — has a page. Never suggest as "next"; do cross-link and may surface for review.
- **seen** — mentioned/skimmed but not given a full page (e.g. the user said "I kind of know
  this"). Lower priority to suggest than fresh frontier, but available.

## Update protocol (run after every lesson)

1. **Mark learned.** Set `status: "learned"`, add `page` and today's `learned_on`. Keep the
   topic's `links`/`prereqs`; refine them if the lesson revealed better ones.
2. **Grow the frontier.** For each genuinely worthwhile adjacent concept the lesson surfaced
   that isn't already a topic, append a new topic with `status: "frontier"`, the right
   `domain`, a one-line `hook`, and `links` back to the topic just taught. Add real neighbors
   only — 0 to 3 is typical. This is how the map expands toward what's worth learning next;
   don't inflate it with noise.
3. **Keep ids honest.** New `id`s are slugs (lowercase, hyphenated) and double as page
   filenames. If a `link` points to an id that doesn't exist yet, that's fine — it's a
   not-yet-mapped neighbor; render it as plain text in the rail, not a link.
4. **Rebuild the home page:** `python scripts/build_index.py`. Never hand-edit `index.html`.

Edit the JSON precisely (it's data, not prose) and keep it valid — a broken `atlas-go.json`
breaks the whole system. After editing, a quick `python -c "import json;json.load(open('atlas-go.json'))"`
is a cheap safety check.

## Suggestion logic (Mode B) — breadth-first on purpose

The user's whole goal is breadth: touch many areas, not tunnel into one. So "what's next?"
should spread coverage, not deepen a single vein. When suggesting, pick **3** topics by this
reasoning (it's a heuristic to apply with judgment, not an algorithm to execute literally):

1. **Eligible set:** `status != "learned"`, and ideally `prereqs` mostly satisfied (their
   prereq topics are `learned`, or have none) — so the suggestion is *learnable now*, not
   blocked on something unlearned.
2. **Favor under-covered domains.** Compute, roughly, how many `learned` topics each domain
   has. Bias suggestions toward domains the user has touched *least*. If they've done three
   systems topics and zero security, lean security. Breadth = evening out the map.
3. **Spread the three.** Offer options from **different domains** where possible, so the
   choice itself broadens their horizon. One can be a near-neighbor of something recently
   learned (momentum); the others should reach into fresh territory.
4. **Lead with the hook.** Present each as its one-line `hook`, plus its domain, so the user
   chooses by curiosity. Example:

   > A few directions, all new ground for you:
   > - **Bloom filters** *(CS · probabilistic)* — a set that's wrong on purpose, to stay tiny and fast.
   > - **TLS, actually** *(Networking · security)* — the handshake that turns an open wire private.
   > - **The bias-variance tradeoff** *(AI · theory)* — the one lens that explains over- and under-fitting.
   >
   > Or name your own — what's been nagging at you?

5. **Respect steering.** If they constrain it ("something in AI", "something short", "the
   weirdest thing on the map"), filter to that first, then apply the same breadth bias within
   it.

Never suggest something already `learned`. If the user asks for something genuinely not on
the map, just teach it (Mode A) and add it — the map is theirs to outgrow.
