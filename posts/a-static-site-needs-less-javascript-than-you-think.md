---
title: A Static Site Needs Less JavaScript Than You Think
created: 2026-11-09
modified: 2026-11-09
draft: true
sources: []
---

Today I learned that most of the JavaScript on my own site was doing jobs the browser already knows how to do — and deleting it made the site smaller, faster, and harder to break.

**The analogy.** Imagine hiring a helper to stand next to a light switch and turn the light on every time you walk into the room. You are paying a person to do what the switch already does, and if the helper falls asleep the room stays dark. A page that ships JavaScript to imitate a browser feature is the same deal: extra weight, extra work, and one more thing that can fail.

**What the browser already had.**

- A reading-progress bar was a script with a `requestAnimationFrame` loop that never stopped. It became one CSS rule, `animation-timeline: scroll(root block)`.
- A month dropdown was a `<select>` plus code to scroll or redirect. It became `<details>` and plain links.
- A year filter toggled `display` in JavaScript. It became radio buttons and one generated `:has()` rule.
- Copying text used a small library. It became `navigator.clipboard.writeText`.
- The fade between pages was a JavaScript router. It became `@view-transition { navigation: auto }`.

**Why the extra code hurts even when it works.** Every script is downloaded, parsed, and run. Some of mine waited for a custom event before starting, so forgetting that one event meant the feature silently never started — no error, no clue. Deleting the script deletes the failure mode too. On one page the JavaScript went from 13.4 KB to 8.2 KB, and an npm dependency disappeared.

**The honest other half.** Some JavaScript is real work: a clock that ticks, a chart, a footnote preview on hover. Those stay. The rule is not "no JavaScript", it is "no JavaScript where an attribute, an at-rule, or a built-in API already says the same thing".

**Key takeaway:** before writing a script, ask whether the browser already does this — `@view-transition`, `<details>`, `:has()`, `navigator.clipboard` and scroll-driven CSS each deleted a whole file from my site.
