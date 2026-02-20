---
title: How to Remove Markdown Frontmatter Programmatically
description: Detect if the file starts with `---`, then strip out everything up to the next `---`.
created: 2025-08-24T09:29:13
modified: 2026-02-20T08:35:37
canonicalPath: 2025/8/24/how-to-remove-markdown-frontmatter-programmatically
draft: false
featured: false
tags:
  - Today-I-Learned/markdown
sources:
  - https://stackoverflow.com/questions/28221779/how-to-remove-yaml-frontmatter-from-markdown-files
---

Today I learned how to strip out YAML frontmatter (--- … ---) from Markdown files using either Python or a shell script.

✼ Python approach

```python
def remove_frontmatter(md_content):
	if md_content.startswith("---"):
		# Split the Markdown content into three parts
		# parts[0] = "" (before first ---)
		# parts[1] = YAML frontmatter
		# parts[2] = rest of the markdown
		parts = md_content.split("---", 2)
		if len(parts) > 2:
			return parts[2].lstrip("\n")
	return md_content
```

✼ Shell script approach

```sh
#!/bin/sh

if [ -f "$file" ] && head -n1 "$file" | grep -q '^---$'; then
	sed '1,/^---$/d' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
fi
```

**Key takeaway:** Whether in Python or shell, the idea is the same—detect if the file starts with `---`, then strip out everything up to the next `---`.
