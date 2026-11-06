---
title: Absolute URLs in Data Always Point at Production
created: 2026-11-06
modified: 2026-11-06
draft: true
sources: []
---

Today I learned that when my site stored a source link as a full address starting with `https://huam.ing/…`, every place that pasted that string into a link sent the reader to the live site — even while I was working on my own laptop.

Think of a party invitation. If I print my home address on every invitation, then the day I rent a hall for the party, my guests still drive to my house. The address was correct. It was just the wrong address for that day. A link written as `/love#q-t69lxn` means “the party, in whatever building we are in right now”. A link written as `https://huam.ing/love#q-t69lxn` means “my house, always”.

# What Happened

`/quotes` fetches `/quotes.json` and turns each row into a link:

```js
link.href = item.href; // "https://huam.ing/abandon-your-ego#q-l84ys2"
```

In development the page runs at `localhost:4321`. Clicking a row opened `huam.ing` — the deployed site — which did not have the new anchors yet, so it landed at the top of the post. It looked like the anchor was broken. It was never used: the browser had already left.

# Where an Absolute URL Is Right

Some places need the full address, because the reader is not standing on my site:

| Place | Needs | Why |
| --- | --- | --- |
| `/quotes.json` | absolute | other programs read it |
| `/quotes.xml` (RSS) | absolute | feed readers live on other machines |
| `<a href>` inside the site | relative | it should follow whatever host serves the page |

One string cannot be right in all three places. The absolute form is the one worth storing, because the relative form can always be rebuilt from it.

# The Fix

Keep the data absolute, and make the link relative where it is rendered:

```js
const { pathname, hash } = new URL(item.href, location.href);
link.href = pathname + hash; // "/abandon-your-ego#q-l84ys2"
```

Now dev, preview and production each stay on their own host, and the JSON keeps the full address for everyone else.

**Key takeaway:** Store absolute URLs for the outside world, but strip them back to a path when you render a link inside your own site — otherwise every dev build quietly sends your own clicks to production.
