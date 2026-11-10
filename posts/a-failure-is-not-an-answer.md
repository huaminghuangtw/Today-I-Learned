---
title: A Failure Is Not an Answer
created: 2026-11-07
modified: 2026-11-09
draft: true
sources: []
---

Today I learned that when a lookup fails, writing down “there is nothing there” is not saving time. It is quietly turning a temporary problem into a permanent one.

Think of a librarian who is asked for a book. If the shelves are lit, she looks and says “we don’t have it”. Fair enough — that answer is worth writing in the catalogue. But if the lights are off and she cannot see anything, saying “we don’t have it” is a lie. She should write “ask me again later” instead.

A computer cache is that catalogue. It needs two different notes: “I checked, there is nothing” and “I could not check”.

# What Went Wrong

My bookmark thumbnail fetcher stores one answer per bookmark. Three states were possible, but I only had two:

* a URL — **found** it
* `null` — **checked**, and there is no thumbnail
* _(no entry at all)_ — **don’t know yet**, go and look next time

When Google’s book API answered `429` — “too many requests, try later” — my code returned `null`. So a temporary “I couldn’t look” was written down as the permanent fact “this book has no cover”. The next run saw an answer already in the catalogue, skipped the book, and the cover never appeared.

Even worse: the book was new. It had been re-exported with an author prefix added to its name, which changed its URL, which changed its cache key. So it arrived, hit the rate limit, and was marked “no cover” on its very first day.

# The Fix

Make the failure loud instead of quiet. A `429` now throws an error, so the caller never reaches the line that writes `null`:

```js
if (res.status === 429 || res.status === 403) {
  throw new Error(`Google Books unavailable (HTTP ${res.status})`)
}
```

The entry stays missing. Missing means “don’t know yet”. The next run asks again, and by then the light is back on.

# The Rule

Before writing an empty value into a cache, ask: _did I learn this, or did I fail to learn it?_

* A search that returned zero results → safe to store.
* A timeout, a `429`, a `500`, an unplugged network → **do not store**. Leave a hole.

A hole costs one extra request. A wrong fact costs the thing itself.

**Key takeaway:** Only write a “none” into a cache when the lookup actually succeeded — a failed lookup should leave no entry at all, so the next run can try again.
