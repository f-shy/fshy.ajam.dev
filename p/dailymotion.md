# Dailymotion

> dailymotion.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dailymotion/ | JSON https://fshy.ajam.dev/api/v1/entity/dailymotion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dailymotion

- `storage/dailymotion` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.dailymotion.com
- free tier: No total storage cap stated. Per-account upload policy: 4 GB per file, 2 hours per file, 15 videos per 24 hours, 10 hours of content per 24 hours (standard creators). Premium/Edge lifts to 64 GB/file and unlimited duration. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 4 GB per file | bytes: 4000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, ad-supported CDN playback. No egress meter on standard accounts. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 4 GB per file [1]
  - per-object-cap (binding): 64 GB/file [1]
- limits note: 4 GB per file is small for bulk. 15 videos/24h and 10 h/24h are enforced by suspension of upload privileges for 24 hours, which makes it a bad target for automated batch loading.
- interface detail: rest
- tooling: yt-dlp `dailymotion` extractor (verified present) plus `dailymotion:playlist|search|user`. Official Data API with resumable upload.
- composes with: 10 hours of content per 24 h per account x unlimited accounts. At a 4 GB/2 h ceiling that is ~20 GB/day ceiling per account, ~7 TB/year, if you fill every slot.
- reliability: Exceeding either the count or duration limit suspends uploads for 24 hours; the platform is also ad-driven and aggressively deletes non-video content, so it is not a general blob store.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: table: '4 GB per file maximum', '2 hours per file maximum', '15 videos uploaded per 24 hours', '10 hours of content uploaded per 24 hours'
  - [2] 2026-10-21: 
- sources:
  - [1] https://faq.dailymotion.com/hc/en-us/articles/115009030568-Upload-policies-technical-specifications
  - [2] https://www.dailymotion.com/video/x8j8n7k`
