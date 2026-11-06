---
title: One JSON Shape Per Type, Not a Union of Nulls
created: 2026-11-06
modified: 2026-11-06
draft: true
sources: []
---

Today I learned that when you publish data as JSON, each kind of thing should carry only the fields it really has. Not one big shape with empty slots for all of them.

Think of a lunchbox. Some kids get a sandwich and a juice. Some kids get a sandwich and an apple. If you hand everyone the same box with a sandwich slot, a juice slot, and an apple slot, then half the slots are always empty. An empty juice slot tells you nothing. Did this kid get no juice? Or does this box just not do juice? You cannot tell by looking.

That is what a `null` field does in an API.

# Before: One Wide Row

Every bookmark type got the same keys. A book looked like this:

```json
{
  "type": "book",
  "title": "Walking",
  "author": "Henry David Thoreau",
  "channel": null,
  "year": null,
  "genre": null,
  "duration": null
}
```

A book has no channel. A video has no author. The `null`s were the API saying “not applicable” — but a consumer has to already know the type table to read that, and then check `type` before touching any field.

# After: Only Its Own Fields

```json
{
  "type": "book",
  "title": "Walking",
  "url": "https://www.google.com/search?q=Henry+David+Thoreau+Walking",
  "category": "❤️ Favorites",
  "favorite": true,
  "author": "Henry David Thoreau"
}
```

Now `"author" in row` is an honest question. Books carry `author`. Videos carry `channel` and `minutes`. Movies carry `year` and `genres`. Essays and podcasts carry nothing extra.

# Name the Field After Its Job

One internal field, `creator`, was doing two jobs: it was the author for books and the channel for videos. The API renames it per type. The parsing layer already knew which position in the reminder name meant what, so the meaning was there all along — it just needed a name that says it.

# Keep the Wide Shape Where It Earns Its Place

The website’s table page still builds one wide row per bookmark, with every column, `null`s and all. Its filter menus list every type, every genre, and every year, so they need one uniform column to scan. Two shapes, two readers, both built from the same parsed items. The wide shape did not disappear. It moved to the only place that needs it.

**Key takeaway:** Give each record only the fields it actually has, and let the page that needs a wide table build its own wide rows — the empty slots cost more than they save.
