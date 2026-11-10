# Vidyard

> vidyard.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vidyard/ | JSON https://fshy.ajam.dev/api/v1/entity/vidyard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vidyard (Free)

- `storage/vidyard` | fails-quota | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.vidyard.com
- free tier: Free: 5 recorded videos per month, 25 videos in the library at once, 30 minutes max length. AI video generation capped separately. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free sharing links; hosting of video is effectively a paid feature. | metered: no
- identity: email
- interface: rest
- limits note: 5 new videos/month and a 25-video rolling library. Deleting is mandatory to keep uploading; it cannot accumulate.
- interface detail: rest
- tooling: No yt-dlp extractor (absent from `--list-extractors`). No public upload API on Free.
- composes with: 5/month x unlimited accounts. But 25-slot library means each account tops out at 25 videos.
- reliability: The 25-video library cap plus monthly creation limit means capacity never grows. Retrieval has no supported automation path.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free: 5 recorded videos per month, 25 videos in the library at once, 30 minutes max length. AI video generation capped separately.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Recorded videos - 5 per month'
  - [2] 2026-10-21: 'You can have up to 25 videos in your Library at once ... delete old ones to make space'
  - withheld 2026-10-21: probe: `yt-dlp --list-extractors | grep -i vidyard` -> no match
- sources:
  - [1] https://knowledge.vidyard.com/hc/en-us/articles/360009875374-Video-usage-and-length-limits-in-Vidyard-Free
  - [2] https://www.vidyard.com/free-screen-record/
