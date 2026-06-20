# Page template — the HTML contract

A consistent *frame*, a free *interior*. The masthead, shell, and meta-rail are fixed so
every page feels like part of one atlas. What goes inside `.prose` is chosen per topic — the
CSS gives you components to reach for, never a skeleton to fill. (If you find yourself using
the same interior structure on every page, you're doing it wrong; see pedagogy.md.)

All styling lives in `assets/atlas.css`. **Do not write per-page CSS or inline styles** for
anything the design system already covers; use the classes below. Retheming happens in one
place — the CSS — so pages must not hardcode colors or fonts.

## The shell

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{TITLE}} — Atlas</title>
  <link rel="stylesheet" href="../assets/atlas.css">
</head>
<body>
<main class="page">

  <!-- MASTHEAD (fixed structure) -->
  <header>
    <p class="eyebrow">
      <span>{{DOMAIN NAME}}</span><span class="dot"></span>
      <span>{{subdomain}}</span><span class="dot"></span>
      <span class="here">you are here</span>
    </p>
    <h1 class="title">{{TITLE}}</h1>
    <p class="standfirst">{{one or two sentences: what this is and why it's worth your time}}</p>
  </header>

  <hr class="openrule">

  <div class="layout">
    <!-- READING COLUMN (free interior) -->
    <article class="prose">
      {{the lesson — structure chosen for THIS topic}}

      <!-- threads at the end -->
      <div class="threads">
        <h4>Threads worth pulling</h4>
        <p class="thread"><span class="lead-in">If the trade-offs hooked you — </span>{{...}}</p>
        <p class="thread"><span class="lead-in">One level down — </span>{{...}}</p>
      </div>
    </article>

    <!-- META RAIL (fixed structure) -->
    <aside class="rail">
      <div class="block">
        <h4>Where this sits</h4>
        <svg class="constellation" viewBox="0 0 240 200">...</svg>
      </div>
      <div class="block">
        <h4>Connects to</h4>
        <ul>
          <li><a href="consistent-hashing.html">Consistent hashing</a></li>
          <li><span class="meta-line">rate limiting · frontier</span></li>
        </ul>
      </div>
      <div class="block">
        <h4>Domain</h4>
        <p class="meta-line">{{Domain}} · {{subdomain}}</p>
      </div>
    </aside>
  </div>

</main>
</body>
</html>
```

Link to other pages with relative hrefs (`consistent-hashing.html`) when that topic is
already `learned`. For frontier neighbors that have no page yet, show them as plain
`.meta-line` text, not links.

## Interior components (reach for what fits)

Inside `.prose`, write normal semantic HTML — `<h2>`, `<h3>`, `<p>`, `<ul>`, `<pre>`. Plus
these purpose-built pieces, used *only when the moment calls for one*:

| Class | What it's for | Use when |
|---|---|---|
| `.pull` | one big idea, set large in the display face | there's a single sentence worth stopping on. **Max one per page.** |
| `.lens` (with `.lens-tag`) | the engineer's lens — a trade-off / "when not to" aside | flagging a cost, failure mode, or wrong-tool warning |
| `.beat` (with `.beat-tag`) | a "predict before you read on" moment | you're planting the one real beat of effort (pedagogy goal 6) |
| `.term` | italicizes a concept being named for the first time | first introduction of a key term |
| `<pre class="...">` + `.pre-label` | code, with an optional small label above | showing a real, minimal example |

The tags on `.lens` and `.beat` are short and human ("watch out", "your call", "predict")
— **never** name the learning technique. Don't reach for all of these; a clean page might
use none of them and just be excellent prose.

Example of the effort beat (note the human tag, not "Retrieval Practice"):
```html
<div class="beat">
  <span class="beat-tag">predict</span>
  Two writers hit the same key at the same instant on different replicas. Before you read
  on — what does the system have to decide, and what's the cheapest correct answer?
</div>
```

Example of the engineer's lens:
```html
<div class="lens">
  <span class="lens-tag">when not to</span>
  If your producers can't actually slow down — sensors, market ticks, other people's
  webhooks — backpressure has nowhere to push. You're now choosing what to drop, and a
  bounded buffer with an explicit shed policy beats pretending you have flow control.
</div>
```

## The constellation (the signature)

A small SVG in the rail showing this topic as a node among its neighbors: a quiet "map of
the territory" the reader can see. It directly serves the breadth goal, so most pages should
have one. Keep it simple — 4 to 8 nodes.

Rules:
- The current topic is the `.here` node, centered-ish, accent-ringed.
- Neighbors that are `learned` use `.node.learned` (filled accent). Frontier neighbors use
  the default `.node` (outlined). This lets the reader *see* what they've covered around it.
- Edges connect `here` to each neighbor; edges touching `here` get class `edge active`.
- Labels are short (the topic's short name), in mono, via the CSS — don't style inline.
- Lay nodes out by hand around the center; this is a handful of points, not a force sim.
- **Labels radiate outward, centered on their own node** (`text-anchor="middle"`): place each
  label *above* a node in the top arc (`y="-13"`) and *below* a node in the bottom arc
  (`y="20"`). Never anchor a side label *inward* toward the center — at 9px mono, two such
  labels on the same row collide (a real bug we hit). Centered-outward labels never touch.
- Give the box room: a ~280-wide viewBox leaves space for long labels like "reactive streams".

Minimal shape:
```html
<svg class="constellation" viewBox="0 0 280 200" role="img"
     aria-label="Map: Backpressure sits among queues, rate limiting, and circuit breakers">
  <!-- edges first so nodes sit on top -->
  <line class="edge active" x1="140" y1="92" x2="62"  y2="40"/>
  <line class="edge active" x1="140" y1="92" x2="218" y2="40"/>
  <line class="edge active" x1="140" y1="92" x2="44"  y2="118"/>
  <line class="edge"        x1="62"  y1="40" x2="218" y2="40"/>

  <g class="node learned" transform="translate(62,40)">
    <circle r="7"/><text x="0" y="-13" text-anchor="middle">queues</text>
  </g>
  <g class="node" transform="translate(218,40)">
    <circle r="7"/><text x="0" y="-13" text-anchor="middle">rate limiting</text>
  </g>
  <g class="node" transform="translate(44,118)">
    <circle r="7"/><text x="0" y="22" text-anchor="middle">circuit breaker</text>
  </g>
  <g class="node here" transform="translate(140,92)">
    <circle r="9"/><text x="0" y="-15" text-anchor="middle">backpressure</text>
  </g>
</svg>
```
Keep labels centered on their node and nothing clips the 280×200 box. Correctness
of the *relationships* matters more than visual polish — but keep it tidy.

## Quality floor (non-negotiable, never announced)

- Responsive: the layout collapses to one column under 880px; on mobile the rail (with the
  map) comes first. The CSS handles this — just don't fight it.
- Real `<title>`, `lang="en"`, a meaningful `aria-label` on the constellation.
- No inline styles, no `<style>` block, no JS unless a topic genuinely needs a small
  interactive demo (then keep it vanilla, self-contained, and respect `prefers-reduced-motion`).
- Code blocks must be real and runnable-looking, never pseudo-handwaving.
