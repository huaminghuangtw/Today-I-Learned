---
title: Git Pre-Commit Hooks Run Once per Commit, Not per File
description: Git pre-commit hooks run once per commit (not per file), so you can filter by file to keep the commits efficient.
created: 2025-08-25T08:39:02
modified: 2026-02-20T08:35:33
canonicalPath: 2025/8/25/git-pre-commit-hooks-run-once-per-commit-not-per-file
draft: false
featured: false
tags:
  - Today-I-Learned/git
sources: []
---

Today I learned that Git’s `pre-commit` hook is executed/triggered **once per commit, not once per file included in the commit**.

If you want to restrict its behavior to certain files, you need to implement that logic inside your pre-commit script (for example, by checking [`git diff --cached --name-only`](https://git-scm.com/docs/git-diff) to see which files are staged).

✼ Example 1: Strip YAML front matter from `README.md`

```sh
#!/bin/sh

if git diff --cached --name-only | grep -q '^README.md$'; then
    if head -n1 README.md | grep -q '^---$'; then
        sed '1,/^---$/d' README.md > README.md.tmp && mv README.md.tmp README.md
        git add README.md
    fi
fi
```

✼ Example 2: Run a Python script to update `README.md`

```sh
#!/bin/sh

if git diff --cached --name-only | grep -q '^README.md$'; then
    python3 .scripts/update_readme.py
    git add README.md
fi
```

By adding file-based checks, you can avoid unnecessary work and speed up commit performance, _especially in large projects_.
