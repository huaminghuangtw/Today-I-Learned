---
title: Using Markdown Image Titles as Captions
created: 2026-01-31
modified: 2026-08-11
sources:
  - https://daringfireball.net/projects/markdown/syntax#img
  - https://www.codecademy.com/resources/docs/markdown/images
---

Today I learned that Markdown images support a title attribute that creates hover tooltips—and with a rehype plugin, you can transform these titles into captions.

---

You are probably familiar with the standard Markdown image syntax:

```markdown
![alt text](image.jpg)
```

Here, `Alt Text` serves as alternative text for accessibility—it appears when images fail to load and helps screen readers describe the image.

The path can be:

* A **relative path** to a local file: `./images/photo.jpg`
* An **absolute path**: `/assets/photo.jpg`
* A **remote URL**: `https://example.com/photo.jpg`

---

You can add a **title attribute** as a second parameter:

```markdown
![alt text](image.jpg "This is the tooltip")
```

This compiles to:

```html
<img src="image.jpg" alt="alt text" title="This is the tooltip" />
```

and creates a tooltip that appears when users hover over the image.

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
