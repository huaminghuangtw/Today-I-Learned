---
title: A Page Should Have Only One Address
created: 2026-11-16
modified: 2026-11-17
sources:
  - https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/
  - https://docs.astro.build/en/reference/configuration-reference/#trailingslash
---

Today I learned that one web page can quietly have two addresses, and that search engines treat those as two different pages.

Think of a house with two front doors. Same house, same family. But the postman has two routes to you, so he keeps two folders — one for each door. Now your letters are split in half, and he has to guess which folder is the real one.

# Two addresses, one page

[My site](https://huam.ing) served every page as a folder with an `index.html` inside. So the page about me lives at `/about/`. But `/about` — _no slash at the end_ — also reaches it. The server answers `/about` with a small note: “the real address is `/about/`”. That note is called a **redirect**. The redirect is not broken. It is **wasted work**. Google counted them as a separate pile: X pages “with redirect”.

# Why it happens

When someone asks for `/about` and the file is really `/about/`, the server has to choose. Cloudflare’s default choice is to redirect.

Astro has a setting for exactly this choice: [`trailingSlash`](https://docs.astro.build/en/reference/configuration-reference/#trailingslash). It takes `'always'`, `'never'` or `'ignore'`, and it defaults to `'ignore'`:

```ts title="astro.config.ts"
trailingSlash: 'ignore' // the default I never changed
```

`'ignore'` means “match the route whether or not a slash is there”. In development, `/about` and `/about/` are the same page and nobody complains. The problem only shows up on the production site, where a different machine (e.g., Cloudflare) makes the choice. It chose the redirect.

Neither tool was wrong. I just never picked a shape.

# The fix was a shape, not a feature

I picked one shape: **always use the slash**. First I said it out loud in the config:

```ts title="astro.config.ts"
trailingSlash: 'always'
```

This changes route matching in dev and for on-demand routes. It does not rewrite a single link.

So the shape also has to live in the code that builds links via a helper function:

```text
withTrailingSlash(href):
    if href points outside the site      → leave it alone
    if href points at a file or the root → leave it alone
    otherwise add "/" at the end, if missing
    keep the query and the hash in place
```

The exceptions are the design: a file URL must keep its extension, and the root is already a single slash. Everything else gets exactly one slash.

Components render links through `withTrailingSlash()`, so `/A` ships as `/A/`.

I stopped disagreeing with myself.

# The trap I avoided

The tempting move is to flip the shape: **drop the slash everywhere instead**. That would have been worse. Why? Google already knows all those addresses with the slash. Flipping means every one of them becomes an old address, and I would have to re-buy every existing URL as a redirect.

So: keep the shape that is already known, and change the links to match it.

**Key takeaway:** Pick one URL shape and make every link, canonical tag and sitemap entry match it.
