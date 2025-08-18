---
title: How to write good Git commit messages
description: 
created: 2025-07-19T10:45:21
modified: 2025-08-18T06:36:11
draft: false
featured: false
tags:
  - Today-I-Learned/git
sources:
  - https://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html
---

# Why?

A clear, consistent commit message format helps:

1. Quickly understand project history
2. Filter and find specific changes (e.g. documentation vs. code)
3. Generate changelogs automatically (see below for details)

# Recommended Format

Use the [Conventional Commits](https://www.conventionalcommits.org/) standard:

```bash
<type>(<scope>): <description>

[optional body]

[optional footer]
```

* **Header/Subject** (`type` + `scope` + `description`) is _required_
  * Keep the subject line under 72 characters
* **Body** and **footer** are _optional_

# Common Types

| Type       | Description                                   |
| ---------- | --------------------------------------------- |
| `feat`     | New feature                                   |
| `fix`      | Bug fix                                       |
| `docs`     | Documentation changes                         |
| `style`    | Formatting, whitespace, etc. (no code change) |
| `refactor` | Code refactor (no bug fix or feature)         |
| `perf`     | Performance improvement                       |
| `test`     | Adding or updating tests                      |
| `chore`    | Routine tasks (build, dependencies, etc.)     |

# Writing Good Commit Messages

* Use _imperative, present tense_: “Fix bug” not “Fixed bug”
* Capitalize the subject line
* No period at the end of the subject

**Example commit messages:**

```bash
feat(auth): add login with Google OAuth
fix(api): handle token refresh errors
docs(readme): update setup instructions
```

# Helper Tools

| Tool                                                                                       | What It Does                                                                        | When It's Used              |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- | --------------------------- |
| [commitizen](https://github.com/commitizen/cz-cli)                                         | Interactive CLI that guides you through writing a commit message                    | **Before** writing commits  |
| [commitlint](https://github.com/conventional-changelog/commitlint)                         | Lints commit messages to ensure they meet the standard and enforce consistency [^1] | **After** writing commits   |
| [conventional-changelog](https://github.com/conventional-changelog/conventional-changelog) | Automatically generates changelogs from commit history                              | **After** merging/releasing |

**Example workflow:**

1. Write commits using the [Conventional Commits](https://www.conventionalcommits.org/) format.
2. Run `npx conventional-changelog -i CHANGELOG.md -s` to update your changelog.

   > This command scans your commit history for Conventional Commits, generates a changelog, writes it to `CHANGELOG.md` (`-i CHANGELOG.md`), and updates the file in place (`-s`). The default preset is Angular, but you can omit `-p angular` for most projects.

   > 💡 [To see all available command line parameters, run: `conventional-changelog --help`](https://github.com/conventional-changelog/conventional-changelog/tree/master/packages/conventional-changelog#usage)

3. Optionally, use [`standard-version`](https://github.com/conventional-changelog/standard-version) or [`release-it`](https://github.com/release-it/release-it) to bump versions and update changelogs automatically.

[^1]: You can add a Git hook ([`commit-msg`](https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks)) to validate your commit messages: `npx commitlint --edit $1`
