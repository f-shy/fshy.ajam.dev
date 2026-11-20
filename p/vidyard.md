# Vidyard

> vidyard.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vidyard/ | JSON https://fshy.ajam.dev/api/v1/entity/vidyard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vidyard (Free)

- `storage/vidyard` | fails-quota | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:31.692Z (live) | stale on 2026-12-04
- url https://www.vidyard.com
- free tier: Free: 5 recorded videos per month, 15 AI videos total (lifetime), and a 30-minute maximum on new recordings. Existing videos never expire and there is no limit to library size. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free sharing links with ad-free playback and no bandwidth limits on shared videos. | metered: no
- identity: email
- interface: rest
- limits note: 5 new recorded videos per month and 15 AI videos lifetime; new recordings cap at 30 minutes. Videos never expire and there is no library-size limit, so capacity accumulates.
- interface detail: rest
- tooling: No yt-dlp extractor (absent from `--list-extractors`). No public upload API on Free.
- composes with: 5 recorded videos per month per account; recordings never expire and the library has no stated size limit, so capacity accumulates across accounts.
- reliability: Recordings never expire and there is no library-size cap, so capacity grows by 5 recorded videos per month; retrieval has no supported automation path (no yt-dlp extractor, no public upload API on Free).
- notes: Free: 5 recorded videos per month, 25 videos in the library at once, 30 minutes max length. AI video generation capped separately.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free: 5 recorded videos per month, 25 videos in the library at once, 30 minutes max length. AI video generation capped separately.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Recorded videos - 5 per month'
  - [2] 2026-10-21: 'You can have up to 25 videos in your Library at once ... delete old ones to make space'
  - withheld 2026-10-21: probe: `yt-dlp --list-extractors | grep -i vidyard` -> no match
  - [1] 2026-11-19: Vidyard Free allows 5 recorded videos per month | capture: sha256:24fea1250ee5d48449d920b83af4bf07656774743ce402b5fcaf833b26b0556c | quote: Recorded videos** - 5 per month
  - [1] 2026-11-19: AI videos are capped at 15 lifetime and the same article states the library has no size limit | capture: sha256:24fea1250ee5d48449d920b83af4bf07656774743ce402b5fcaf833b26b0556c | quote: AI videos** - 15 total (lifetime)
  - [1] 2026-11-19: there is no library-size cap and videos do not expire | capture: sha256:24fea1250ee5d48449d920b83af4bf07656774743ce402b5fcaf833b26b0556c | quote: Just so you know, your existing videos never expire, and there is no limit to the number of videos you can have in your library at once.
  - [1] 2026-11-19: no per-account library ceiling is stated, so the former 25-slot cap is gone | capture: sha256:24fea1250ee5d48449d920b83af4bf07656774743ce402b5fcaf833b26b0556c | quote: Just so you know, your existing videos never expire, and there is no limit to the number of videos you can have in your library at once.
  - [1] 2026-11-19: recordings accumulate at 5 per month with no stated library ceiling | capture: sha256:24fea1250ee5d48449d920b83af4bf07656774743ce402b5fcaf833b26b0556c | quote: Recorded videos** - 5 per month
  - [2] 2026-11-19: Vidyard states ad-free playback with no bandwidth limit on shared videos | capture: sha256:25cc90ef5c6a0fb88342faac19482f3ce2ef7c5bdaf3c8e9bea92a3dd21c815a | quote: ad-free playback with no bandwidth limits
- sources:
  - [1] https://knowledge.vidyard.com/hc/en-us/articles/360009875374-Video-usage-and-length-limits-in-Vidyard-Free
  - [2] https://www.vidyard.com/free-screen-record/
