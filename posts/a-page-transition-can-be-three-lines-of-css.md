---
title: A Page Transition Can Be Three Lines of CSS
created: 2026-11-09
modified: 2026-11-10
draft: true
sources: []
---

Today I learned that the smooth fade between two pages of a website does not need a JavaScript router — the browser can animate two real pages by itself.

**The analogy.** Think of two photos. A JavaScript router is a machine that wipes the first photo off a single sheet of paper and paints the second one onto the same sheet; it has to remember everything it painted before, and it has to keep repainting. The browser’s own cross-page transition holds up the first photo while the second one is printed, then cross-fades them. Two sheets, and the browser already knows how to overlap them.

**Same animation, different machine.**

* A JavaScript router catches the click, fetches the page, swaps the body, keeps the old page’s state alive, and animates the swap. Because the page never really reloads, every feature must re-initialise on the router’s own event — mine had 32 places waiting for that event.
* The CSS at-rule lets the page navigate normally, then animates the old document into the new one. No state survives, and every script simply runs the way it does on any page load.

**What the swap costs.** Forward clicks get slower without the router’s hover prefetch, and back/forward changes from “re-render” to the browser’s own cache — which is usually faster. The real cost is the migration: the CSS is three lines, but you must first find every feature that assumes the router’s event exists. On my site the 32 `astro:page-load` registrations collapsed into one registry in `src/scripts/page-init.ts` that runs on `DOMContentLoaded` — that single file is what let the per-widget guards come out.

**When you would still need a router.** Only when something has to survive the reload and cannot be rebuilt cheaply: a sound or video that keeps playing while the reader moves to another post, in-progress state nobody serialised (an unsaved draft, a half-filled wizard), or a live connection such as a socket that must not drop. Nothing on my site fits. Filters and toggles belong in the URL or `localStorage`, the clocks re-read the time on load, and back/forward already returns the scroll position from the browser’s cache.

**What going back would cost.** Not the 5.6 KB — the scaffolding. A router can initialise the same widget twice, so every widget carries a guard or a cleanup: `data-bound`, `data-built`, `dataset.ready`, a `cleanups` array. I deleted those from a dozen components once pages really reloaded. Putting a router back means restoring them and re-auditing every interactive feature, not just re-adding the component.

**And check it where you will ship it.** My editor’s built-in browser never ran the transition at all — even for a two-file test page with nothing but the at-rule and a link — so “it works” had to be confirmed in a normal browser.

**Key takeaway:** the animation is three lines of CSS; the migration is the audit — count how many places depend on the router’s event before you delete the router.
