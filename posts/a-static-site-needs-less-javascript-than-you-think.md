---
title: A Static Site Needs Less JavaScript Than You Think
created: 2026-11-09
modified: 2026-11-10
draft: true
sources: []
---

Today I learned that most of the JavaScript on my own site was doing jobs the browser already knows how to do — and deleting it made the site smaller, faster, and harder to break.

Imagine hiring a helper to stand next to a light switch and turn the light on every time you walk into the room. You are paying a person to do what the switch already does, and if the helper falls asleep the room stays dark. A page that ships JavaScript to imitate a browser feature is the same deal: extra work, one more thing that can fail, just overkill.

**What the browser already had.**

* A reading-progress bar was a script with a `requestAnimationFrame` loop that never stopped. It became one CSS rule, `animation-timeline: scroll(root block)`.
* A month dropdown was a `<select>` plus code to scroll or redirect. It became `<details>` and plain links.
* Copying text used the [clipboard.js](https://clipboardjs.com/) library. It became `navigator.clipboard.writeText`.
* The fade between pages was a JavaScript router. It became `@view-transition { navigation: auto }`.
* Three overlays — a graph modal, an image zoom, a footnote sheet — each hand-rolled a backdrop `div`, an Escape `keydown` listener, a `document.body.style.overflow` lock, focus moves and a removal `setTimeout`. They became `<dialog>` and `showModal()`. The scroll lock is now one rule: `body:has(dialog[open]) { overflow: hidden }`.

**Why the extra code hurts even when it works.** Every script is downloaded, parsed, and run. Some of mine waited for a custom event before starting, so forgetting that one event meant the feature silently never started — no error, no clue. Deleting the script deletes the failure mode too. On one page the JavaScript went from 13.4 KB to 8.2 KB, and an npm dependency disappeared.

**The invisible half: scaffolding.** A page that never really reloads can initialise the same widget twice, so every widget needs a guard — `data-bound`, `data-built`, `dataset.ready` — or a cleanup function that undoes the previous run. Once pages reload for real, none of that can happen twice, and the guards came out of a dozen components without losing a single feature. The JavaScript bill includes the code you wrote to survive being run twice.

**Animating one needs no timer.** `@starting-style` describes the frame before `showModal()` runs, and `transition-behavior: allow-discrete` keeps `display` and `overlay` alive during the exit, so a bottom sheet slides up and back down without the `setTimeout(…, 300)` I used to run before removing the node. What is left in the script is filling in the content and one `close()` call.

**The honest other half.** Some JavaScript is real work: a clock that ticks, a chart, a footnote preview on hover. Those stay. The rule is not “no JavaScript”, it is “no JavaScript where an attribute, an at-rule, or a built-in API already says the same thing”.

**Key takeaway:** before writing a script, ask whether the browser already does this — `@view-transition`, `<details>`, `<dialog>`, `:has()`, `navigator.clipboard` and scroll-driven CSS each deleted a whole file from my site.
