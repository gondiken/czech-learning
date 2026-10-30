# Česky za 10

A 10-minute-a-day Czech course for a Turkish speaker living in Czechia.

- **App (phone):** https://claude.ai/artifact/49jET6PDeyUZhUw95zHbxX
- **Daily coach:** a scheduled Claude task that runs every day, prepares the next lesson and sends a phone notification.

## How it works

- **Placement test** (first open): 5 questions per unit, starting from Unit 1. ≥ 80% tests you out of the unit
  (its lessons are marked done and its words go into the review deck). Retake any time from Practice.
- **Path**: units → stations (lessons) → a checkpoint test (15 questions, 80% to pass). Passing raises your level.
- **A lesson** (~10 min): warm-up on fading words → Turkish bridge → new words (teach card + exercise) →
  match pairs → real scene (dialogue) → sentence exercises → typing. Wrong answers come back at the end.
- **Exercise types**: pick picture, pick meaning, pick Czech, listen & pick, listen & type, write in Czech
  (accent-tolerant, with an accent keyboard), match pairs, build Czech from tiles, translate with tiles,
  tap what you hear, fill the gap.
- **XP & goal**: 1 XP per first-try correct answer, +10 per lesson, +20 per passed checkpoint. Goal 20/30/50 XP a day.
  Reaching it ends the day ("Done for today"); extra practice is optional. No hearts, no leagues.
- **Streak**: days with the goal met; one missed day per 7 is a rest day (☾) and doesn't break it.
- **Memory model**: half-life regression (simplified). Each word has a half-life `h` in days; recall = 2^(-days/h).
  Right answers grow `h` (more for typing/production), wrong answers halve it. Strong = `h` ≥ 7 days.
- **Adapting**: each word climbs exercise stages (recognise → recall → type); the weakest skill gets more exercises;
  a session under 70% or 15+ fading words turns the next session into a "Strengthen day"; the coach's `plan/today`
  can set mode, focus skill/words and new-word cap.
- **Level**: Unit n passed = Level n, labelled with its CEFR band (Pre-A1 → A1.2 → A2). An estimate, not an exam.

## The fun layer (no stress mechanics)

- **Knedlík**, a dumpling mascot, reacts to answers, cheers combos ("Tři v řadě!") and naps when you're done for the day.
- **Silly sentences** (2 per lesson) star recurring characters: pan Medvěd (a bear who never has a tram ticket),
  a cat, and a talking rohlík. They're translated with word tiles.
- **Postcards**: each finished station gives a Czech culture card (fact + phrase with audio), collected in the Album tab.
- **Speed round** (Practice): match pairs for 60 seconds and race only your own best.

## Where things live

- `app/index.html`: the app page, published as a claude.ai artifact.
- `lessons/NNN.json`: lesson source files (also stored in the artifact's database, which is what the app reads).
- `CURRICULUM.md`: the roadmap the coach uses to write new lessons.
- `COACH.md`: the exact instructions the daily scheduled task follows.

## Artifact database layout

| Path | Written by | Contents |
|---|---|---|
| `lessons/NNN` | coach | one lesson (schema below) |
| `units/N` | coach | `{n, title, cefr, can, lessons[]}` |
| `progress/main` | app | `v:2`, `goal`, `placement`, `done{n}`, `units{n:{passed,score}}`, `cards{cz:{h,last,stage,seen,right,wrong}}`, `days{date:{xp,ex,right,min,sk{skill:[right,total]}}}`, `skill{skill:[last 50 bools]}`, `history{date:{learned,strong,xp}}`, `lastSession` |
| `answers/<date>-<time>` | app | one finished session: `{date, mode, lesson, unit, acc, xp, mins, items[{ex,skill,item,ok,first,ms}]}` |
| `plan/today` | coach | today's plan (see `COACH.md`) |
| `reports/latest` | coach | `{date, text}` shown on the Progress tab |

Lesson schema:

```json
{
  "n": 15, "unit": 4, "short": "Tab label", "title": "…", "why": "one sentence",
  "bridge": {"title": "…", "rows": [{"cz":"…","tr":"…","ex":"…","note":"…"}], "note": "…"},
  "words": [{"cz":"…","en":"…","tr":"…","emoji":"…","say":"optional pronunciation"}],
  "dialog": [{"who":"Ty|<role in Czech>","cz":"…","en":"…"}],
  "pattern": {"cz":"…","en":"…"},
  "silly": [{"cz":"Medvěd nemá jízdenku.","en":"The bear doesn't have a ticket.","emoji":"🐻🎫"}],
  "postcard": {"emoji":"🏰","title":"…","text":"one true, surprising fact about Czechia","cz":"phrase","en":"meaning"}
}
```
`who: "Ty"` is the learner (shown as blue "You" bubbles).
