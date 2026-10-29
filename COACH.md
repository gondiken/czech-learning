# Daily coach routine

This is the prompt of the scheduled task "Czech daily lesson". It runs once a day in a fresh cloud session.

App artifact: https://claude.ai/artifact/49jET6PDeyUZhUw95zHbxX

1. Read with the ArtifactData tool (load it with ToolSearch if needed):
   `progress/main` (may not exist yet), `notes/today`, and all of `lessons` (page with cursor).
2. Work out: next lesson = lowest `n` not in `progress.done`; streak; words missed in the last 7 days
   (`progress.log[].missed`); whether the learner skipped yesterday.
3. If fewer than 5 unfinished lessons remain, write the next 7 following `CURRICULUM.md` and the
   schema in `README.md`, recycling recently missed words. Double-check every Czech and Turkish line.
   Save them with one ArtifactData `batch` (`set` on `lessons/NNN`, zero-padded), and also as
   `lessons/NNN.json` in this repo; commit and push them to the session branch.
4. Write `notes/today` (`set`, pin `if_version`) with `{date, text}`: 1–3 short friendly sentences.
   Mention the streak or gently welcome them back after a gap; add one tiny real-life tip
   (a word they'll see today on a sign, a seasonal word, a missed word to watch for).
   Mix in a little Czech. No guilt-tripping.
5. Finish with a single short message (it becomes the phone notification), e.g.
   `🚋 Station 5 ready: Paying at the till (~10 min). Tip: "Sbíráte body?" → "Ne." https://claude.ai/artifact/49jET6PDeyUZhUw95zHbxX`
