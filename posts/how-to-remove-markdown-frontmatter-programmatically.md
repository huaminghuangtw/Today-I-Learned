---
title: How to Remove Markdown Frontmatter Programmatically
created: 2025-08-24
modified: 2026-10-19
sources:
  - https://stackoverflow.com/questions/28221779/how-to-remove-yaml-frontmatter-from-markdown-files
---

Today I learned how to strip out YAML frontmatter (`---` … `---`) from Markdown files using either Python or a shell script.

# The Python Approach

```python
def remove_frontmatter(md_content):
	if md_content.startswith("---"):
		parts = md_content.split("---", 2)
		if len(parts) > 2:
			return parts[2].lstrip("\n")
	return md_content
```

# The Shell Script Approach

```sh
#!/bin/sh

if [ -f "$file" ] && head -n1 "$file" | grep -q '^---$'; then
	sed '1,/^---$/d' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
fi
```

**Key takeaway:** Whether in Python or shell, the idea is the same—detect if the file starts with `---`, then strip out everything up to the next `---`.
