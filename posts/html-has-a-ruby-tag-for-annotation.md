---
title: HTML Has a Ruby Tag for Annotation
created: 2026-11-13
modified: 2026-11-13
sources:
  - https://developer.mozilla.org/en-US/docs/Web/CSS/ruby-align
  - https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby
---

Today I learned that HTML has a dedicated element for annotating a pronunciation next to a word — `<ruby>` — and it is not a tooltip, not an abbreviation, and not something you hack together with `<sup>`.

# Minimal syntax

`<ruby>` is the container. `<rt>` is the small gloss. That is the whole element family.

```html
<ruby>croissant<rt>kwah-SAHN</rt></ruby>
```

# Examples

Japanese furigana and Chinese pinyin are the famous uses, where each character carries its own gloss:

```html
<ruby>漢<rt>かん</rt>字<rt>じ</rt></ruby>
```

```html
<ruby>東京<rt>とうきょう</rt></ruby>
```

# Two CSS values

```css
ruby {
  ruby-position: over; /* `under` if you want pinyin below the characters */
  ruby-align: space-between; /* center | start | end | space-around */
}
```

`ruby-align` decides what happens when the gloss is wider than the base text. The CSS default lets it spill onto the neighbouring text; `space-between` widens the word instead.
