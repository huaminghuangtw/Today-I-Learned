---
title: Git Reset
description: 
created: 2025-07-24T05:38:30
modified: 2025-07-31T13:52:23
draft: false
tags:
  - Today-I-Learned/git
sources:
  - https://git-scm.com/docs/git-reset
---

## Introduction

`git reset` is used to **undo** changes in your Git repository. It allows you to move the current branch to a specific commit and control what happens to your staging area and working directory. `git reset` is especially useful when you want to undo commits that have not been pushed to a remote repository.

## When to Use

* Use `git reset --soft <commit>` to move the branch pointer back and keep your changes staged for a new commit.
* Use `git reset --mixed <commit>` (or simply `git reset <commit>`, since `--mixed` is the default) to remove files from the staging area but keep changes in your working directory.
* Use `git reset --hard <commit>` to completely discard all changes in both the staging area and working directory.
	* ⚠️ Dangerous! This will delete all uncommitted changes and is irreversible!

## Overview

| Mode      | Affects Commit History | Affects Staging Area | Affects Working Directory |
| --------- | --------------------- | -------------------- | ------------------------ |
| `--soft`  | ✅ Yes                 | ❌ No                | ❌ No                    |
| `--mixed` | ✅ Yes                 | ✅ Yes               | ❌ No                    |
| `--hard`  | ✅ Yes                 | ✅ Yes               | ✅ Yes                   |

> Summary:
>
> * `--soft`: Only resets commit history, keeps staging area and working directory unchanged.
> * `--mixed`: Resets commit history and staging area, keeps working directory unchanged.
> * `--hard`: Resets everything, including working directory.
