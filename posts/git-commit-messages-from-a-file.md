---
title: Git Commit Messages from a File
description: You can specify a file to use as a commit message in Git. This is a clean approach for writing longer or more detailed commit messages.
created: 2025-07-20T15:08:42
modified: 2025-08-07T05:39:10
draft: false
tags:
  - Today-I-Learned/git
sources:
  - https://git-scm.com/docs/git-commit
---

There are two main ways to provide a commit message in Git:

1. `-m <msg>` or `--message=<msg>`: This is the most common way, where you provide the message directly on the command line. You can use multiple `-m` options, and their values will be concatenated as separate paragraphs.
2. `-F <file>` or `--file=<file>`: This option allows you to take the commit message from a given file. If you use `-` as the filename, the message is read from the standard input. This is particularly useful for multi-line messages as it avoids potential issues with shell character escaping.

It's important to note that the `-m` and `-F` options are mutually exclusive. You can only use one of them for a single commit.

✱ Example using `-F`

1. Create a file named `commit-message.txt`:

   ```txt
   feat: Add new login feature

   This commit introduces a new login system with email and password authentication.
   It also includes basic validation and error handling.
   ```

2. Use the file in your commit command:

   ```bash
   git commit -F commit-message.txt
   ```
