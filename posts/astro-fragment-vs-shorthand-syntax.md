---
title: Astro Fragment vs Shorthand Syntax
created: 2026-08-09
modified: 2026-08-09
sources:
  - https://docs.astro.build/en/reference/astro-syntax/#fragments
---

Today I learned that Astro supports both the `<> </>` shorthand and a built-in `<Fragment />` component for grouping siblings—and how to pick between them.

Both forms compile to the same output, so the choice comes down to **what you need from the wrapper**:

# The `<>` Shorthand

* Purely a grouping wrapper — **no attributes allowed**, ever
* Use it for simple cases where you just render multiple siblings together without styling or behavior

# The `<Fragment />` Component

* The full component, so it can accept attributes. The ones you'll actually use:

	* **`set:html`** — the big one. `<>` **cannot** do this:

		```astro
		<Fragment set:html={rawHtml} />
		```

	* `class` / `id` / `data-*` — occasionally useful to target the group with CSS or JS

* More explicit and greppable than `<>` — easy to find in a codebase

# Best Practice

| Need | Use |
| ---- | --- |
| Just group siblings | `<>` |
| Inject raw HTML | `<Fragment set:html={...} />` |
| Attach `class` / `id` / `data-*` to the group | `<Fragment class="..." />` |
