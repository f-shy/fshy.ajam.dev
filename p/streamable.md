# Streamable

> streamable.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/streamable/ | JSON https://fshy.ajam.dev/api/v1/entity/streamable.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Streamable

- `storage/streamable` | fails-quota | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://streamable.com
- free tier: 250 MB per file, 10 minutes per video on the free plan. No storage pool. The unit is the individual clip. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 250 MB per file | bytes: 250000000 | source: [1] | note: not stated
- retention: Videos are auto-deleted after 90 days even on a free account ('archived after 24 hours' when anonymous). | days: 1 | source: [1] | note: not stated
- egress: Free, unlimited playback; no egress meter. | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): 250 MB per file [1]
  - retention-clamped: deleted after 90 days [1]
- limits note: 250 MB AND 10 minutes, both hard. Videos are auto-deleted after 90 days even on a free account ('archived after 24 hours' when anonymous).
- interface detail: rest
- tooling: yt-dlp `Streamable` extractor (verified present). Undocumented upload endpoint only.
- composes with: Unlimited clips at 250 MB. Mathematically unbounded but practically useless: 500 GB would need 2,000 separate uploads, each expiring in 90 days.
- reliability: Systematic 90-day deletion makes it a transfer service, not storage. Data disappears on a timer by design.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 250 MB per file, 10 minutes per video on the free plan. No storage pool — the unit is the individual clip.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'maximum file size of 250 MB and a duration of 10 minutes'; 'Videos uploaded by free users are automatically deleted after 3 months (90 days)'
  - [2] 2026-10-21: '250 MB' free tier
- sources:
  - [1] https://streamable-support.zendesk.com/hc/en-us/articles/35415717293204-Free-Plan-Limits
  - [2] https://streamable.com/pricing
