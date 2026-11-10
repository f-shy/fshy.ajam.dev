# Reddit native media

> reddit.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/reddit/ | JSON https://fshy.ajam.dev/api/v1/entity/reddit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Reddit native media (i.redd.it)

- `storage/reddit-native-media` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://reddit.com
- free tier: 20 MB per image post, ~1 GB per video post, no stated total | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free, direct image URLs on Fastly (probe headers show 'Fastly-Restarts' and a versioned S3-style origin); no auth on i.redd.it GETs | metered: no
- identity: institution
- interface: rest
- limits note: 20 MB/image; media must go through the subreddit's native uploader (no arbitrary file types at all. Images and video only); spam filters and per-subreddit karma gates bite long before any byte cap.
- interface detail: rest
- tooling: official Reddit API has a /api/submit image path (submit_image + image_path / upload lease); PRAW and Late/Zernio wrappers expose it
- composes with: 20 MB x unlimited posts x unlimited subreddits x N accounts. 500 GB = 25,000 image posts; OAuth rate limits (100 QPM) make that ~4 hours of posting, far faster than a human, which is exactly what gets flagged
- reliability: i.redd.it is Fastly-backed and 404s cleanly (probe returned a 2016-dated 404 with x-amz-version-id), i.e. real object storage behind CDN; but media is tied to the post lifecycle and API-scoped uploads are heavily moderated
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Reddit accepts images up to 20 MB' / 'Reddit accepts videos up to 1 GB'
  - [2] 2026-10-21: probe: HEAD -> 404 with 'Fastly-Restarts' and 'x-amz-version-id' headers (Fastly + S3-style origin, image/png content-type on 404)
  - [3] 2026-10-21: /api/submit documented; submit_image present in PRAW (github.com/praw-dev/praw issue 1359 shows the API path in use)
- sources:
  - [1] https://help.postpone.app/platforms/reddit/media-limits
  - [2] https://i.redd.it/
  - [3] https://www.reddit.com/dev/api/
