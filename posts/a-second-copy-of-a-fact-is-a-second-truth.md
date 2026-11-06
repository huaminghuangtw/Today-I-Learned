---
title: A Second Copy of a Fact Is a Second Truth
created: 2026-11-06
modified: 2026-11-06
draft: true
sources: []
---

Today I learned that if the same fact is written down in two places, you do not own a fact any more. You own a guess about which copy is still right.

Think of two clocks in a house: one on the kitchen wall, one by the bed. For a week they agree. Then the battery in one goes weak and it loses a minute a day. Now every time you leave the house you have to pick a clock to believe, and the clocks cannot tell you which one it is. Two clocks did not give you more time. They gave you one more decision every morning.

Two copies work the same way. They are free to disagree, and when they do, nothing in the code argues. You just get a page that says one thing in the header and another thing in the weather.

# Before: Three Clocks

The site knew my time zone in three separate places:

* `SITE.timeZone` in `src/consts.ts`
* a `fallbackTimeZone` argument handed to `fetchWeather()`
* `TAIPEI_OFFSET_MS` and `taipeiNow()` in `src/scripts/lifespan.ts`

All three said `Asia/Taipei`, and all three were true while I lived in Taipei. They agreed by luck, not by design. Once the page started saying “wherever my latest journal entry says”, the luck ran out: three places, three ways to be wrong, and the `timeZone` that Open-Meteo returned for the weather was a fourth.

# After: One Clock, and a Loud Failure

`src/lib/now-location.ts` reads `now.md` and exports `NOW_LOCATION`. Everything else — the header clock, the weather request, `todayISO`, `pickByDay`, the daily feeds, the Strava fetcher — asks it. No file holds a zone of its own.

If the key is missing, the build throws with the command that fixes it:

```text
now.md is missing `timeZone` — run `.scripts/update-now.py` in the Slash repo
```

That is the other half. A missing fact should stop the build, not quietly fall back to a guess. The old `fallbackTimeZone` was exactly such a guess, so it went away too.

# The Exception That Proves the Rule

The birthday stays hardcoded:

```ts
export const BIRTH_TIME_ZONE = "Asia/Taipei"
```

Not because the rule is soft, but because this is a different fact. My age should tick over at midnight where I was born, not at midnight wherever I happen to be standing. “Where I was born” does not move. It is written once, and nothing else claims to know it.

# Why Not Just Keep Them in Sync

Because syncing is a job, and jobs get skipped. Every copy you keep is a promise that somebody will update it later. One copy is a promise nobody has to keep.

**Key takeaway:** Keep one copy of a fact and let the build break when it is missing — the second copy is not redundancy, it is a second truth you will eventually have to choose between.
