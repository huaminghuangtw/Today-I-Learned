---
title: Temporarily Ignore Local Changes to a Tracked File in Git
description:
created: 2025-08-22
modified: 2026-04-30
canonicalPath: 2025/8/22/temporarily-ignore-local-changes-to-a-tracked-file-in-git
featured: false
sources:
  - https://git-scm.com/docs/git-update-index
tags:
  - Today-I-Learned/git
---

Today I learned that you can tell Git to temporarily ignore changes to a tracked file using:

```bash
git update-index --assume-unchanged <file>
```

After this, Git won’t show changes to the file in `git status`, `git add`, or `git commit`.

To start tracking changes again:

```bash
git update-index --no-assume-unchanged <file>
```

# Caution

* ❗️ If the file is modified in the remote branch and you pull, Git may overwrite your local changes.
* ❗️ This is only for temporary local changes; the file remains tracked in the repository.
This is mainly an optimization for large repositories, as Git will skip checking the file for changes, speeding up `status` and `diff`.

# Side Notes

* This is mainly an optimization for large repositories, as Git will skip checking the file for changes, speeding up `status` and `diff`.
