---
title: Enforce a Rule Where It Cannot Be Bypassed
created: 2026-11-08
modified: 2026-11-08
draft: true
sources: []
---

Today I learned that a rule kept in one doorway is not a rule for the house.

Imagine a school with two gates. A teacher stands at the front gate and checks every kid's homework. The back gate is open, and nobody stands there. Kids who use the back gate walk straight in with no homework. It is not because the teacher is lazy. It is because the check was put at a gate, not at the school.

Code works the same way. A rule written inside one function only covers the things that go through that function. Anything that takes a different route never sees the rule, and nothing warns you.

# Before: The Rule Lived in a Builder

Every markdown page on my site ended with a "Back to /me" link. The rule was simple: if the page is one of the pages listed in `SLASH_PAGES`, add the link.

That rule lived in `getSlashArticle()` in `src/lib/article.ts`. Five pages — `/about`, `/beliefs`, `/mission`, `/uses`, `/colophon` — reach the page through `MarkdownPageLayout`, which calls that builder. They all got the link for free.

`/now` does not. It is built by `NowPage.astro`, which composes `Layout` on its own and never calls the builder. So `/now` had no link, and nothing anywhere said so. I only found it because I was asked why `/now` was missing it.

# After: The Rule Reads the Source of Truth

`src/components/SlashIndexLink.astro` takes no props at all. It looks at the current route, checks the first path segment against `SLASH_PAGES`, and renders the link when it matches — or nothing when it does not.

Two things changed by moving it there:

* The rule is stated once, next to the data it depends on, so it cannot drift from `SLASH_PAGES`.
* Any page can mount it with one line. `MarkdownPageLayout` mounts it, and so does `NowPage`. A page written next year only needs that one line, and a page that forgets still fails in an obvious, visible way instead of a quiet one.

The old version also needed a helper to work out `/me` vs `/me/en`. The new one reads the route's own language segment, so the English pages link to the English index without any extra data.

# The Smell That Gave It Away

The clue was that the rule was *data* in one object (`meta.indexPage`) built by one function. If a value only exists when one code path runs, every other code path silently has nothing. Moving the rule into the component that draws the thing means the rule runs wherever the thing is drawn.

The same lesson applies to the required `title` and `description` on `Layout.astro`: they are checked at the layout boundary, which every page must pass through, so no page can arrive without them.

**Key takeaway:** put a shared rule on the one path everything must take — or inside the component that renders it — not in a helper that only some callers happen to use.
