---
title: GitHub URL Schemes for Viewing, Editing, and Commit History
description: 
created: 2025-07-16T12:10:42
modified: 2025-08-09T16:15:51
draft: false
featured: false
tags:
  - Today-I-Learned/github
  - Today-I-Learned/url-schemes
sources:
  - https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files
---

GitHub provides several URL schemes for different file operations.

1. For **viewing files**, use: [^1]

	```
	https://github.com/{owner}/{repo}/blob/{branch}/{file_path}
	```

	Example: <https://github.com/huaminghuangtw/Today-I-Learned/blob/main/posts/github-url-schemes.md>

2. To **view raw content**, use:

	```
	https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}
	```

	Example: <https://raw.githubusercontent.com/huaminghuangtw/Today-I-Learned/main/posts/github-url-schemes.md>

3. When you need to **modify content**, use:

	```
	https://github.com/{owner}/{repo}/edit/{branch}/{file_path}
	```

	Example: <https://github.com/huaminghuangtw/Today-I-Learned/edit/main/posts/github-url-schemes.md>

	==Remark==: Both view and edit URLs support `#Lx` suffix for jumping to specific lines. Edit URLs require login to save changes, while view URLs are public. The key difference is that edit URLs are for proposing changes and editing content, while view URLs are for sharing lines and viewing raw files.

4. Finally, to explore **version history**, use:

	```
	https://github.com/{owner}/{repo}/commits/{branch}/{file_path}
	```

	Example: <https://github.com/huaminghuangtw/Today-I-Learned/commits/main/posts/github-url-schemes.md>

[^1]: With Markdown files (`.md`), GitHub automatically adds the `plain=1` query parameter when you go to **Code** view to get a line permalink, because Markdown files are rendered without line numbers in **Preview** mode. For code files (`.js`, `.py`, `.txt`, etc.), you get syntax highlighting without the `plain=1` parameter.
