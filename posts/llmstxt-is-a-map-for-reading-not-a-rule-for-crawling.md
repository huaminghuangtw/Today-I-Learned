---
title: llms.txt is a map for reading, not a rule for crawling
created: 2026-11-28
modified: 2026-11-28
sources:
  - https://frankknow.com/what-is-llms-txt
  - https://medium.com/@kaispriestersbach/the-llms-txt-is-dead-more-precisely-a-dud-ab7bee4f469c
---

Today I learned about `llms.txt`, and it started with a smaller question.

I first met the idea of appending `.md` to a page URL in the summary of [Jakub Krehel](https://jakub.kr)’s [`llms.txt`](https://jakub.kr/llms.txt), which states it as a plain fact: _every post on that site has a markdown version at its URL with `.md` appended._ That made me wonder whether [mine](https://huam.ing) should too. This note is my learning journal on `llms.txt`.

# A guide written for ai to read

The clearest one-line description I’ve seen comes from a [Chinese post,](https://frankknow.com/what-is-llms-txt/) which called it 寫給 AI 看的網站導覽說明書 — “a guide written for AI to read”.

[`llms.txt`](https://llmstxt.org) was proposed by Jeremy Howard — founder of [fast.ai](https://www.fast.ai/) and [Answer.AI](https://www.answer.ai) — in September 2024, and rewritten as a v2 specification in August 2026. It is a markdown file at `/llms.txt` that hands a language model a short, curated map of your site, instead of hoping the model can digest the whole thing.

The premise, in the spec’s own words:

> Context windows, while larger than they were, are still too small for most websites in their entirety, and every wasted token costs time and money. Agents are best served by concise, expert-level information gathered in a single, accessible location.

# The Spec

The file has five parts, in a fixed order:

1. An `H1` with the site or project name — this is the only required part.
2. A blockquote with a short summary.
3. Any number of plain paragraphs of extra context.
4. Any number of `##` sections, each a markdown list of `- [name](url): note`.
5. A `## Optional` section, by convention, for links an agent can skip when its context is tight.

```markdown
# huam.ing

> A personal site about writing, running, and enoughness.

## Writing

- [Today I Learned](https://huam.ing/notes/index.md): short reference notes

## Optional

- [Colophon](https://huam.ing/colophon/index.md): how the site is built
```

It can sit at the site root or at any subpath.

> [!TIP] Hand an agent your `llms.txt`, ask it questions about the site, and see whether it can navigate to the answers. Review it at least every six months: check that the links still resolve and the summaries are still true.

# Comparison

`llms.txt` is easiest to understand next to the two files it is usually mentioned with: `robots.txt` and `sitemap.xml`.

| File          | Question it answers  | What it optimizes for |
| ------------- | -------------------- | --------------------- |
| `robots.txt`  | Who may fetch this?  | access                |
| `sitemap.xml` | Where is everything? | breadth               |
| `llms.txt`    | What matters here?   | precision             |

They are complementary, and none of them replaces another, because each speaks to a different reader.

* `robots.txt` governs permission: which pages a search engine or AI crawler may (or may not) request. It’s the only one of the three with a long-standing, widely obeyed convention — and even that took years to go from proposal to de facto standard.
* `sitemap.xml` is an inventory: every indexable page, so that a search engine misses nothing. Its strength is completeness, and that is exactly what makes it wrong for an agent — in aggregate it is far too large for a **context window** and it contains no judgement about what is worth reading first.
* `llms.txt` selects. It drops the archive pages, the tag pages and the duplicates, keeps the few pages that carry the site’s main purpose, and says in one clause what each one is for.

# A markdown twin per page

v2 added the part that answers my original question. _Every page an agent might need should also serve a clean markdown copy at the same URL — with `.md` appended (`page.html.md`), with the extension replaced (`page.md`), or as `index.md` when the URL has no file name._

# In the wild

Every major AI company publishes one for its own developer documentation, and the four I checked each use it differently.

* **Perplexity** — <https://docs.perplexity.ai/llms.txt>
* **OpenAI** — <https://developers.openai.com/llms.txt>
* **Anthropic** — <https://platform.claude.com/docs/llms.txt>
* **Gemini** — <https://aistudio.google.com/llms.txt>

# What `llms.txt` is not

It is not needed, and it is not required. There is no RFC,[^1] no standards body, and no obligation on anyone to read the file. A site without one is not penalized, blocked or misread: crawlers simply fall back to reading HTML, as they always did. Its legitimate purpose is narrow — **[developer documentation for coding assistants and AI agents](https://medium.com/@kaispriestersbach/the-llms-txt-is-dead-more-precisely-a-dud-ab7bee4f469c)**.

Nor is it an SEO [^2] or GEO [^3] play. No search engine treats the file as a ranking signal, and no AI bot has said it picks citations from it.

**Key takeaway:** `robots.txt` says who may read your site, `sitemap.xml` says where everything is, and `llms.txt` is a map for reading, not a rule for crawling.

[^1]: An RFC is an official rulebook entry for the internet: when something like HTTP or HTML becomes a standard, the document is published as a Request for Comments, and everyone is expected to follow it. `llms.txt` has no such paperwork — it is a proposal that caught on, so nothing forces anybody to read it.
[^2]: = Search Engine Optimization
[^3]: = Generative Engine Optimization
