---
title: How to Put a Live Counter in a Markdown Page
created: 2026-10-19
modified: 2026-10-19
sources: []
---

Today I learned how to make a Markdown page show a number that dynamically changes, like “I have been alive for 30 years, 5 months, 18 days…”

Imagine a worksheet with this sentence:

> I have been in the world for \_\_\_\_\_.

Markdown lets you drop small pieces of HTML into a normal sentence:

```md
I have been in the world
<span data-age-counter data-birth="1996-05-01">…</span>.
```

To make it dynamic, a small JavaScript script plays the role of the pencil to write a new answer.

You can see the live counter in action on my [about page](https://huam.ing/about).
