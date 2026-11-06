---
title: Git Pre-Push Hooks Cannot Add to the Push in Flight
created: 2026-11-06
modified: 2026-11-06
draft: true
sources: []
---

Today I learned that a `pre-push` hook cannot add its own changes to the push that triggered it.

# The Simple Version

Imagine you seal a letter in an envelope and hand it to the postman. Then you remember one more sentence you wanted to say. Can you slip it in? No. The envelope is already sealed. You have to write a new letter and mail it again.

`git push` works the same way. Git decides which commits to send **before** it runs your `pre-push` hook. If the hook creates a new commit, that commit missed the envelope.

# What People Usually Write

A hook that refreshes a generated file and commits it looks like this:

```sh
#!/bin/sh
python3 .scripts/generate.py

if ! git diff --quiet generated.json; then
  git add generated.json
  git commit -m "chore: refresh generated.json"
fi
```

This runs, the commit is created locally, and the push carries on — with the **old** commit. The new one waits for your next push.

# Two Ways to Behave

| Hook ending | What you see | When the file actually ships |
|---|---|---|
| `exit 0` | silent success | your next push, whenever that is |
| `exit 1` + a message | push fails loudly | the retry you do right away |

The silent version is the dangerous one: nothing tells you the remote is missing the file.

# Where the Work Belongs Instead

If the goal is “the file must travel with my commit”, generate it in a `pre-commit` hook. There the commit does not exist yet, so `git add` inside the hook goes into the very commit being created.

If you prefer to keep things explicit, just run the generator before you commit — one command, then a normal commit and push.

**Key takeaway:** `pre-push` runs after git has already picked the commits to send, so anything it commits ships on the _next_ push — generate in `pre-commit`, or run the generator yourself before committing.
