---
title: Pagefind Exact Search With Double Quotes
created: 2026-10-27
modified: 2026-10-27
sources:
  - https://pagefind.app/docs/multilingual/
---

Today I learned that Pagefind only looks for the **exact phrase** when the query is wrapped in double quotes. Without quotes, it also brings back near-misses.

Think of a librarian. Ask her for “anything about dogs” and she hands you books about dogs, puppies, and dog training. Hand her a note that says `"dogs"` and she brings only the books that say that exact word.

# Quoted vs Unquoted

| Query | What comes back | Results on my site |
| ----- | --------------- | ------------------ |
| `deep work` | also `deep`, `deeply`, `works`, … | 94 |
| `"deep work"` | only the exact phrase | 25 |

The quotes are not decoration. They flip a switch inside Pagefind that turns off “match similar words” mode.

# Making It the Default

I wanted strict search every time, but asking readers to type quotes is rude. So the code adds them just before searching:

```ts
const strictTerm = (term: string) => `"${term.replace(/^"+|"+$/g, "").trim()}"`;
```

The quotes then show up in the result count (`25 results for "deep work"`), so it is obvious the search was strict.

# The Catch with Chinese

Quoting Chinese queries broke them: every one returned 0 results. Pagefind chops Chinese text into words when building the index, and chops it again inside the browser, and the two do not always agree. Strict mode needs an exact word match, so a small disagreement means “nothing found”. Chinese queries are therefore left unquoted.

**Key takeaway:** In Pagefind, double quotes mean “this exact phrase only” — add them in code to make strict search the default, but leave languages without spaces (Chinese, Japanese) unquoted.
