---
title: Array Every Stops at the First No
created: 2026-11-26
modified: 2026-11-26
draft: true
sources: []
---

Today I learned that `every()` on an array stops the moment the function says “no” — so if that function also *does* something, everything after the first “no” never happens.

Think of a teacher checking homework along a row of desks. The rule is “check every child”. But the moment she finds one unfinished page, she stops walking and heads to the principal. The children after that desk never get checked at all.

# Where it bit me

The contact form has four required fields. Each field needs its own error message in the page's language, written with `setCustomValidity()`. So the check function does two jobs: it writes a message onto the field, and it answers “is this field fine?”.

```js
const check = (field) => {
  if (!field.value.trim()) {
    field.setCustomValidity("請填寫這個欄位")
    return false
  }
  field.setCustomValidity("")
  return true
}

fields.every(check) // stops at the first empty field
```

If the name is empty and the message is empty too, `every` stops after the name. The message field never gets a message. Then `form.reportValidity()` walks the form and shows the *first* invalid field — which might be the one that was never checked, so the visitor sees the browser's own English bubble on a Chinese page.

# The fix

Visit every field first, then read the results:

```js
const allValid = fields.map(check).every(Boolean)
if (!allValid) form.reportValidity()
```

`map` has no early exit — it calls `check` on all four fields. `every` then only reads the four booleans, so stopping early costs nothing.

# The rule behind it

| Method | Stops early? |
| --- | --- |
| `every` | yes, at the first `false` |
| `some` | yes, at the first `true` |
| `find` / `findIndex` | yes, at the first match |
| `map` / `forEach` / `filter` | no, visits everything |

If the function handed to an early-exit method has a side effect, that side effect depends on position — which is almost never what you meant.

**Key takeaway:** when the callback does something (writes a message, logs, saves), use `map(...).every(...)` or a `for...of` loop instead of `every(...)`, because `every` stops at the first “no” and never runs the callback for the rest.
