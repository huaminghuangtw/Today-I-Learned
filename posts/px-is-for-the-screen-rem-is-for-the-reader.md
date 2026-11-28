---
title: px is for the screen, rem is for the reader
created: 2026-11-27
modified: 2026-11-28
sources:
  - https://developer.mozilla.org/en-US/docs/Web/CSS/length
---

I rebuilt [my site](https://huam.ing)’s styles using `rem` instead of `px`, then put a few `px` back. This is the rule I wish I had before I started.

A `px` is one pixel, a fixed dot on the screen. A `rem` is one copy of the page’s base text size, which is whatever the reader picked in their browser settings (usually 16px). Think of `rem` as the page’s measuring cup: it is only as big as the reader’s text.

# How to decide

One question per number: **should this grow when the reader’s text grows?**

| If the number is about… | Use | Because |
| --- | --- | --- |
| text, the space around it, rounded corners, how wide a line gets | `rem` | it should keep its proportion to the text |
| a thin line: a border, a divider, an outline | `px` | it is a mark on the screen, not a size of text |
| a rule the browser fixed, like the 16px below which iPhone zooms into form fields | `px` | it is baked into the browser, not a size you pick |

A reader who makes the text a quarter bigger should get the gaps, corners and lines of text a quarter bigger too, so the page keeps its shape. Without `rem`, they get a giant font squeezed into the same small box.

A divider written in `rem` turns into a fat bar for when the reader asks for bigger text. A divider written in `px` stays a thin line, which is what it is.

**Key takeaway:** `rem` follows the text, `px` follows the screen. A page written entirely in one of them is usually answering the wrong question somewhere.
