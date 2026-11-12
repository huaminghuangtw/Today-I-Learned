---
title: "AppleScript’s Quit Waits Until the App Is Really Gone"
created: 2026-11-11
modified: 2026-11-11
draft: true
sources: []
---

Today I learned that `tell application "Something" to quit` does not mean “ask it to quit and carry on” — the command does not return until the app has actually closed.

# The Simple Version

Imagine you tell your little brother, “Time to leave the playground.” One way to do it is to stand next to him and wait until he walks out of the gate. The other way is to say it and go back to your own game.

AppleScript’s `quit` is the first way. Your script stops at that line and waits. `killall` is the second way. It taps the app on the shoulder and returns right away.

# Why It Matters

I was cutting a long job into 5-minute pieces: start it, wait 5 minutes, stop it, start again. The stopping line was:

```applescript
tell application id "com.apple.shortcuts" to quit
```

If the app is busy — say it is in the middle of a two-hour job — it may not close until that job finishes. So the script sat on that line for two hours, and the “5-minute piece” quietly became “the whole thing”. The safety net I wrote _after_ that line never got a turn.

There is a second trap: an Apple Event can time out after a couple of minutes and throw an error, so the same line can fail instead of waiting.

# The Fix

Send a signal instead. It returns immediately, and the app cannot argue:

```sh
killall Shortcuts
for _ in {1..25}; do
    pgrep -x Shortcuts >/dev/null || exit 0
    sleep 0.2
done
```

Now the timing is mine: the loop above gives the app about five seconds, and then I move on regardless. If it is still alive, the next round tries again.

The trade-off is honest: a signal does not let the app finish a file it was halfway through writing. That is why the job needs to be able to resume — mine re-reads a progress file and redoes the one item that was interrupted.

# Key takeaway

`quit` is a handshake, not a signal — AppleScript waits for the app to close, while `killall` returns at once, so use the signal whenever your script needs to keep moving.
