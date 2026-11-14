---
title: A Table's Filters Belong in the URL
created: 2026-11-14
modified: 2026-11-14
draft: true
sources: []
---

Today I learned that when a page lets me narrow a list — a year, a collection, a search word — that narrowing should live in the address bar, not only inside the page's memory.

Think of reading a big book with ten bookmarks in it. If I pull out a drawer and pick a chapter, the bookmark should move with me. If I close the book and open it again and the bookmark is blank, I have to hunt for where I was. And if a friend wants to see the exact page I am reading, I cannot just say "open the book" — I have to be able to hand them the bookmark too.

# What Was Wrong

On `/archive` the filters were JavaScript variables. Clicking 部落格 narrowed the table to 47 rows, and the address bar still said `/archive`. So:

- reloading threw the choice away
- the back button did nothing, because nothing had changed as far as the browser knew
- there was no link I could paste into a message saying "look at these 47 rows"

# What a Query String Gives Back

Each choice becomes one `key=value` pair, and the page reads them on load:

```text
/archive?collection=blog&day=2024-01-07
```

Now reload restores the view, a shared link opens the same view, and the address bar always tells the truth about what is on screen.

# The One Nuance

Not every change deserves a new history entry. Picking a filter is a decision, so it should be undoable:

```js
history.pushState({}, "", url);   // filter changed
history.replaceState({}, "", url); // typing in the search box
```

Typing "writing" one letter at a time should not give me a backlog of eleven pages to press Back through. Filtering to one collection is a step I might want to take back.

**Key takeaway:** If the page can be narrowed, the narrowing belongs in the URL — write filter changes with `pushState` and search typing with `replaceState`, so the address bar stays shareable without turning Back into a maze.
