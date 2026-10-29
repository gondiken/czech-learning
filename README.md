# Česky za 10

A 10-minute-a-day Czech course for a Turkish speaker living in Czechia.

- **App (phone):** https://claude.ai/artifact/49jET6PDeyUZhUw95zHbxX
- **Daily coach:** a scheduled Claude task that runs every day, prepares the next lesson and sends a phone notification.

## How a day works (≈10 min)

| Step | Time | What happens |
|---|---|---|
| Warm-up review | 2 min | Flashcards of earlier words that are due (spaced repetition: 1, 3, 7, 14, 30, 60 days) |
| Sounds & tricks | 2 min | One "Turkish bridge": a Czech sound or grammar idea mapped onto Turkish |
| New words | 3 min | 6–10 picture cards with Czech audio, English and Turkish |
| Real scene | 2 min | A short dialogue from daily life in Czechia, played aloud |
| Quick check | 1–2 min | 5 questions: listen, pick the word, pick the picture |

## Where things live

- `app/index.html`: the app page, published as a claude.ai artifact.
- `lessons/NNN.json`: lesson source files (also stored in the artifact's database, which is what the app reads).
- `CURRICULUM.md`: the roadmap the coach uses to write new lessons.
- `COACH.md`: the exact instructions the daily scheduled task follows.

## Artifact database layout

| Path | Written by | Contents |
|---|---|---|
| `lessons/NNN` | coach | one lesson (schema below) |
| `progress/main` | app | `done{n:{date,score,of}}`, `days[]`, `cards{cz:{box,due,n}}`, `log[]` (incl. missed words) |
| `notes/today` | coach | `{date, text}` shown as "Your coach" on top of the app |

Lesson schema:

```json
{
  "n": 15, "title": "…", "line": "A|B|C", "why": "one sentence",
  "bridge": {"title": "…", "rows": [{"cz":"…","tr":"…","ex":"…","note":"…"}], "note": "…"},
  "words": [{"cz":"…","en":"…","tr":"…","emoji":"…","say":"optional pronunciation"}],
  "dialog": [{"who":"Ty|<role in Czech>","cz":"…","en":"…"}],
  "pattern": {"cz":"…","en":"…"}
}
```
`who: "Ty"` is the learner (shown as blue "You" bubbles).
