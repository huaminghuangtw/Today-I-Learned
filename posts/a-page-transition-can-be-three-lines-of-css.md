---
title: A Page Transition Can Be Three Lines of CSS
created: 2026-11-09
modified: 2026-11-09
draft: true
sources: []
---

Today I learned that the smooth fade between two pages of a website does not need a JavaScript router — the browser can animate two real pages by itself.

**The analogy.** Think of two photos. A JavaScript router is a machine that wipes the first photo off a single sheet of paper and paints the second one onto the same sheet; it has to remember everything it painted before, and it has to keep repainting. The browser's own cross-page transition holds up the first photo while the second one is printed, then cross-fades them. Two sheets, and the browser already knows how to overlap them.

**Same animation, different machine.**

- A JavaScript router catches the click, fetches the page, swaps the body, keeps the old page's state alive, and animates the swap. Because the page never really reloads, every feature must re-initialise on the router's own event — mine had 32 places waiting for that event.
- The CSS at-rule lets the page navigate normally, then animates the old document into the new one. No state survives, and every script simply runs the way it does on any page load.

**What the swap costs.** Forward clicks get slower without the router's hover prefetch, and back/forward changes from "re-render" to the browser's own cache — which is usually faster. The real cost is the migration: the CSS is three lines, but you must first find every feature that assumes the router's event exists.

**And check it where you will ship it.** My editor's built-in browser never ran the transition at all — even for a two-file test page with nothing but the at-rule and a link — so "it works" had to be confirmed in a normal browser.

**Key takeaway:** the animation is three lines of CSS; the migration is the audit — count how many places depend on the router's event before you delete the router.
