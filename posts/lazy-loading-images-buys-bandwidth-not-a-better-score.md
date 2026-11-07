---
title: Lazy Loading Images Buys Bandwidth, Not a Better Score
created: 2026-11-07
modified: 2026-11-07
draft: true
sources:
  - https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#loading
---

Today I learned that adding `loading="lazy"` to images is a bandwidth habit, not a performance score fix — and on a site where the images already sit below the fold, the score is not allowed to move at all.

**The analogy.** Imagine a waiter who carries every dish on the menu to your table the second you sit down. That is a page loading its images. Lazy loading is the waiter who brings each dish only when you ask for it. If you were going to eat everything anyway, nothing gets faster. You only save work when the guest leaves early.

**What actually changes.** A browser already refuses to *draw* images off screen. What it does eagerly is *download* them. `loading="lazy"` postpones the download until the image is nearly in view, so a reader who quits halfway never pays for the pictures they never reached.

**Why the score does not move.** My post pages load 10 KB of HTML, 15 KB of CSS and 72 KB of preloaded fonts before anything visible appears. That is what the speed number is made of. Twelve images further down the page cannot slow down a finish line they come after.

**When it pays off.** Pages with many pictures near the top, readers on slow phones, and pages where most visitors stop early. My `/bookmarks/book` page is heavy for a different reason — 252 KB of HTML — so lazy thumbnails there are a small win, not a cure.

**Key takeaway:** ask what a rule actually charges you before adopting it — here the fix was three lines and the honest benefit is fewer bytes for readers who leave early, so ship it as hygiene and do not promise a score.
