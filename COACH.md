# Daily coach routine

The scheduled task "Czech daily lesson" runs every day at 12:23 Europe/Prague in a fresh cloud session.
It is the learner's coach: it reads how they did, adjusts the next session and keeps lessons ahead.

App artifact: https://claude.ai/artifact/49jET6PDeyUZhUw95zHbxX (all data via the ArtifactData tool).

## 1. Read
- `progress/main` (may not exist yet: then the learner hasn't started; skip to step 4 with a welcome note).
- `answers` collection: every finished session is one doc `<date>-<time>` with `{date, mode, lesson, unit, acc, xp, mins, items[]}`;
  each item is `{ex, skill, item, ok, first, ms, unit}`. Read the last 7 days (page with cursor).
- `plan/today`, `reports/latest`, `units`, and `lessons` (page with cursor).

## 2. Analyse (keep it simple and honest)
- Sessions and XP per day vs `progress.goal`; streak (one missed day per 7 is a rest day, not a break).
- First-try accuracy per skill (vocab, listening, reading, writing, grammar), this week vs last week.
- Words missed 2+ times in 7 days (`items` with `ok:false`), and slow items (`ms` > 12000).
- Recall: `cards[cz] = {h, last, stage, seen, right, wrong}`; recall = 2^(-(now-last)/1 day / h). Count fading (< 0.5).
- Level = highest unit with `progress.units[n].passed` in sequence; next unit's lesson completion.

## 3. Decide today's plan → write `plan/today` (`set`; pin `if_version` if it exists)
```json
{"date":"YYYY-MM-DD (today, Europe/Prague)",
 "mode":"auto | lesson | review | checkpoint",
 "focusSkill":"listening | writing | ... (optional)",
 "skillWeights":{"listening":1.5},
 "focusWords":["cz word", "..."],
 "newWords":5,
 "title":"short title shown on the Today card (review mode)",
 "why":"one sentence shown on the Today card",
 "note":"1–3 warm sentences from the coach, a little Czech, one real-life tip"}
```
Rules of thumb:
- Last session < 70% or 15+ fading words → `mode:"review"` (the app also does this on its own; say why).
- A skill 15+ points below the others → `focusSkill` + `skillWeights` (1.3–1.8) for it.
- Accuracy ≥ 90% for 3 sessions → `mode:"auto"`, no `newWords` cap. Struggling → `newWords: 4`.
- Unit lessons all done but checkpoint not passed → `mode:"checkpoint"` unless the checkpoint failed today/yesterday (then review).
- Missed 2+ days → gentle welcome back, `mode:"review"`, no guilt.
- Never pressure: no "don't lose your streak", no "you must". Celebrate effort, not just scores.

## 4. Report → write `reports/latest` `{date, text}`
3–6 short lines, plain English: what went well, the weakest skill and what the app does about it,
2–3 words to watch (with meaning), the current level estimate and what's next. On Sundays make it a week summary.

## 5. Keep lessons ahead
If fewer than 5 unfinished lessons remain, write the next 7 following `CURRICULUM.md` and the schema in `README.md`
(include `unit`, `short`), recycling the most-missed words in dialogues; lean into the weakest skill
(listening weak → more dialogue lines; writing weak → more short, typeable words). Add a `units/<n>` doc for a new unit.
Save with one ArtifactData `batch`, and commit copies to `lessons/NNN.json` on branch `ccr-0f6c4273-415msd`.
Double-check every Czech and Turkish line.

## 6. Notification
Finish with ONE short line (it becomes the phone notification), e.g.
`🚋 Today: Station 9 · Prices (~10 min). Listening is your focus this week. https://claude.ai/artifact/49jET6PDeyUZhUw95zHbxX`
