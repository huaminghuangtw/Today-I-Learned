---
title: Using Media Fragments for Video Thumbnails on iOS Safari
created: 2026-10-14
modified: 2026-10-14
sources:
  - https://stackoverflow.com/questions/56428378/no-way-to-preload-first-video-frame-on-ios-safari
---

Today I learned a one-line fix for the [video](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video) that shows up as a black rectangle on an iPhone: append a **[media fragment](https://www.w3.org/TR/media-frags/)** `#t=0.5` to its URL. Safari will use that frame as the thumbnail.

```html
<video src="clip.mp4#t=0.5" controls playsinline preload="metadata"></video>
```

Rules of thumb:

* The fragment goes **after** the query string (`clip.mp4?cache=1#t=0.5`), and never append a second fragment to a URL that already has one.

	```js
  const THUMBNAIL_TIME = 0.5

  function withThumbnail(src) {
    return src.includes('#') ? src : `${src}#t=${THUMBNAIL_TIME}`
  }
  ```

* Keep the offset small (`0.5`, not `5`).
* Pick a frame that isn’t black: a clip that fades in from black at `t=0` looks like a broken player.
