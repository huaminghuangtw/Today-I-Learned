---
title: Handling Case-Sensitive File Renames in Git
description: Always use `git mv` for file renames in git-tracked folders.
created: 2025-08-08T17:10:17
modified: 2025-08-29T08:30:45
draft: false
featured: true
tags:
  - Today-I-Learned/git
sources: []
---

# The Problem

Today I ran into a frustrating Git issue that I’d never encountered before. I had renamed several image files in my Obsidian vault’s `_attachments` folder, changing their extensions from uppercase (`.PNG`, `.JPG`, `.WEBP`) to lowercase (`.png`, `.jpg`, `.webp`).

However, when I tried the usual workflow:

```bash
git add .
git commit -m "Fix file extensions"
git push
```

Git didn’t detect any changes, even though I could clearly see the files had different extensions on my filesystem.

# The Root Cause

The issue stems from macOS having a **case-insensitive filesystem** while Git is **case-sensitive**.

From the filesystem’s point of view, `image.PNG` and `image.png` are the same file, but Git sees them as different files.

This caused a mismatch where Git was still tracking the old uppercase extensions in its index, even though the filesystem only showed the lowercase files.

As a result, Git doesn’t realize the file has been renamed because the filesystem treats both names as identical.

# The Solution: `git mv`

The solution is to use `git mv` to explicitly tell Git about the change. The `git mv` command renames the file both in your filesystem and Git’s index, so Git can track the rename as a single operation:

```bash
# Instead of manually renaming files, use git mv
git mv oldfile.PNG newfile.png
git mv image.JPG image.jpg
git mv photo.WEBP photo.webp
```

# What I Did

I had to rename several files that Git was tracking with uppercase extensions:

```bash
cd "/path/to/my/repo"

# First, find out which files with uppercase extensions Git is tracking
git ls-files _attachments/ | grep -E "\.(PNG|JPG|WEBP)$"

# Then rename each one using git mv
git mv _attachments/2b3a6c702b5b01cf12507cc029630bf3.JPG _attachments/2b3a6c702b5b01cf12507cc029630bf3.jpg
git mv _attachments/316d587a5c95f54ea7a4f86fbb986d63.PNG _attachments/316d587a5c95f54ea7a4f86fbb986d63.png
git mv _attachments/33fabea8972383bcb4bbeea50437f690.PNG _attachments/33fabea8972383bcb4bbeea50437f690.png
# more attachments...

# Commit the changes
git commit -m "Rename image file extensions from uppercase to lowercase"
git push
```

# Alternative Solutions

Other approaches I could have used (but `git mv` is cleanest and simplest):

1. **Configure Git to ignore case** (_not recommended_):

   ```bash
   git config core.ignorecase false
   ```

2. **Remove and re-add** (_loses history_):

   ```bash
   git rm file.PNG
   git add file.png
   ```

   In contrast, when you use `git mv`, Git properly records the change as a **rename**:

	```bash
	# Git status showed:
	renamed: _attachments/image.PNG -> _attachments/image.png
	```
