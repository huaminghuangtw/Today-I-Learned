---
title: Exposing a JSON API and CORS
created: 2026-11-04
modified: 2026-11-04
draft: true
sources: []
---

Today I learned what it takes to let other people and other websites read your data, and why the browser says no when you forget one small note.

# A public JSON file is already an API

Think of a library. Anyone can walk in and read the index cards on the front desk. They don’t need a special pass, a password, or a special room.

A file on your site works the same way. If `https://huam.ing/quotes.json` is simply a file that exists, then anything on the internet can ask for it and get a list back. That is already an API. You do not need a version number, a wrapper object, or an account system to call it one.

One detail: the links **inside** that file should be full addresses (`https://huam.ing/…`), not short ones (`/quotes`). A reader might be on a completely different site, and a short link would point at _their_ site, not yours.

# The browser has a guard at the door

Now the tricky part. Imagine a rule at school: you may not take a book from another school unless that school writes a note saying “everyone is welcome here.”

Browsers have exactly this rule, and it is called **CORS** (Cross-Origin Resource Sharing). A page on `someone-else.com` is not allowed to read data from `huam.ing` unless `huam.ing` sends a note with the answer. That note is a response header:

```text
Access-Control-Allow-Origin: *
```

The `*` means “any site may read this.” Without that note, the browser blocks the answer before your page ever sees it, and the network tab shows a red CORS error.

# What confused me

The rule lives in the **browser**, not on the server. So `curl` and the server logs show a perfectly normal `200 OK` while the browser shows an error. Both are telling the truth — one of them just doesn’t have a guard.

I also learned that these header files only apply where the host reads them. On Cloudflare, a `public/_headers` file works when the site is served by the deployed worker, but locally (`astro dev`) the file is not used, so the header only appears in production.

# Key takeaway:

If you want other websites to read your data, three things must be true: the file is reachable at a stable URL, the links inside it are absolute, and the response carries `Access-Control-Allow-Origin` — otherwise the browser blocks a request that the server happily answered.
