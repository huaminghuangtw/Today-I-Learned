---
title: An Empty Box Is Not Zero
created: 2026-11-06
modified: 2026-11-09
draft: true
sources: []
---

Today I learned that JavaScript turns an empty text box into the number zero, and that this quiet zero can make a filter say “yes” to something it never looked at.

Think of a form with a box that asks “how many minutes?”. If you leave it blank, a careful clerk says “no answer”. `Number("")` is not a careful clerk. It says “zero minutes”.

# What Went Wrong

The bookmarks table can filter videos by length, in three buckets:

* `≤ 14 min`
* `15–45 min`
* `> 45 min`

Books have no length at all — their `data-duration` attribute is `""`. The check looked like this:

```js
const minutes = Number(row.dataset.duration ?? 0) // Number("") === 0
if (minutes >= 0 && minutes <= 14) return true
```

So every book landed in “≤ 14 minutes”. Picking two buckets at once returned 785 rows, all of them books, essays, movies and podcasts that have no runtime at all.

# The Fix

Ask about empty first, then compare:

```js
const raw = row.dataset.duration ?? ""
if (raw === "") return false

const minutes = Number(raw)
```

# The Traps

* `??` does not help here. It only catches `null` and `undefined`, and `""` is neither.
* `Number(" ")` is `0` as well, and so is `Number("\n")`. Whitespace behaves like nothing at all.
* `parseInt("")` gives `NaN`, which fails every comparison instead of passing one — sometimes the safer tool.

**Key takeaway:** before turning a `data-*` value into a number, check that it is not an empty string — `Number("")` is `0`, so a missing value quietly passes every `>= 0` test.
