---
title: Using Markdown Image Titles as Captions
description: The title attribute in Markdown images and how to transform it into captions with rehype plugins.
created: 2026-01-31T16:25:38
modified: 2026-02-01T17:51:27
draft: false
featured: false
canonicalPath: 2026/1/31/markdown-image-titles
tags:
  - /Today-I-Learned/
sources:
  - https://daringfireball.net/projects/markdown/syntax#img
  - https://www.codecademy.com/resources/docs/markdown/images
---

Today I learned that Markdown images support a title attribute that creates hover tooltips—and with a rehype plugin, you can transform these titles into captions.

---

Most people are familiar with the standard Markdown image syntax:

```markdown
![Alt Text](/path/to/image.jpg)
```

Here, `Alt Text` serves as alternative text for accessibility—it appears when images fail to load and helps screen readers describe the image.

The path can be:

* A **relative path** to a local file: `./images/photo.jpg`
* An **absolute path**: `/assets/photo.jpg`
* A **remote URL**: `https://example.com/photo.jpg`

---

You can add a **title attribute** as a second parameter:

```markdown
![Alt Text](/path/to/img.jpg "image title")
```

This creates a tooltip that appears when users hover over the image. You can also transform these titles into captions.

---

Markdown doesn’t natively support image captions, which leaves you with some awkward workarounds:

**Option 1:** [Add text below the image](https://stackoverflow.com/questions/19331362/using-an-image-caption-in-markdown-jekyll) using HTML tags:

```html
![](image.png)
<sub><em>This is a caption for the image.</em></sub>
```

**Option 2:** Use raw HTML with `<figure>` elements:

```html
<figure>
	<img src="image.png" alt="Example Image" width="200" height="200">
	<figcaption>This is a caption for the image.</figcaption>
</figure>
```

Both approaches work, but they break the flow of writing in plain Markdown.

---

If you’re writing a blog with a static site generator (like Astro, Next.js, or Gatsby), you can use a [rehype plugin](https://github.com/futuraprime/rehype-figure-title) [^1] that transforms your image titles into captions.

With this plugin, you write clean Markdown:

```markdown
![A descriptive alt text](./img.jpg "The caption")
```

And it becomes:

```html
<figure class="rehype-figure-title">
  <img src="./img.jpg" alt="A descriptive alt text" />
  <figcaption>The caption</figcaption>
</figure>
```

[^1]: Alternatives: [rehype-title-figure](https://github.com/y-temp4/rehype-title-figure) or [rehype-figure](https://github.com/josestg/rehype-figure)
