# Dailymotion

> dailymotion.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dailymotion/ | JSON https://fshy.ajam.dev/api/v1/entity/dailymotion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dailymotion

- `storage/dailymotion` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T04:14:18.949Z (live) | stale on 2026-12-10
- url https://www.dailymotion.com
- free tier: No total storage cap stated. Per-account upload policy: 4 GB per file, 2 hours per file, 15 videos per 24 hours, 10 hours of content per 24 hours (standard creators). Premium/Edge lifts to 64 GB/file and unlimited duration. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 4 GB per file | bytes: 4000000000 | source: [1] | note: the upload policy table caps standard uploads at 4 GB per file and Premium or Edge uploads at 64 GB per file
- retention: source: [1] | note: unverified: the upload policies page states size, duration, volume and suspension limits but no file retention period
- egress: Free, ad-supported CDN playback. No egress meter on standard accounts. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 4 GB per file [1]
  - per-object-cap (binding): 64 GB/file [1]
- limits note: upload privileges may be suspended for 24 hours when the 15 videos per 24 hours or 10 hours of content per 24 hours limits are reached; the standard file cap is 4 GB
- interface detail: rest
- tooling: yt-dlp `dailymotion` extractor (verified present) plus `dailymotion:playlist|search|user`. Official Data API with resumable upload.
- composes with: 10 hours of content per 24 h per account x unlimited accounts. At a 4 GB/2 h ceiling that is ~20 GB/day ceiling per account, ~7 TB/year, if you fill every slot.
- reliability: Exceeding either the count or duration limit suspends uploads for 24 hours; the platform is also ad-driven and aggressively deletes non-video content, so it is not a general blob store.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: table: '4 GB per file maximum', '2 hours per file maximum', '15 videos uploaded per 24 hours', '10 hours of content uploaded per 24 hours'
  - [2] 2026-10-21: 
  - [3] 2026-11-11: the upload policy table caps a standard upload at 4 GB per file | capture: sha256:5f713af2bf0fda25a9d330186045989c3ea413be2fb6665a3f2953c6e9f1ed6c | quote: 4 GB per file maximum
  - [3] 2026-11-19: the upload policy table caps a standard-creator upload at 4 GB per file (64 GB for Premium/Edge), with 15 videos and 10 hours per 24 hours | capture: sha256:df942625918b51652b7304c8e348453b0c8acd235dab528bf6a317ec34e17d56 | quote: 4 GB per file maximum
  - [1] 2026-11-25: the upload policy table gives the standard and Premium or Edge per-file ceilings | capture: sha256:9ad44c54a5004bf0100b4aaf3906373cdab0904d12cf015ed57653e780152be9 | quote: | Video size | 4 GB per file maximum | 64 GB |
  - [1] 2026-11-25: the upload policies page states upload limits but publishes no retention period | capture: sha256:9ad44c54a5004bf0100b4aaf3906373cdab0904d12cf015ed57653e780152be9 | quote: | Video size | 4 GB per file maximum | 64 GB |
  - [1] 2026-11-25: the upload policies page states a 24-hour suspension for exceeding the stated volume limits | capture: sha256:9ad44c54a5004bf0100b4aaf3906373cdab0904d12cf015ed57653e780152be9 | quote: If you reach one of these limits, your upload privileges may be suspended for 24 hours and an error message will be displayed on your upload interface.
  - [1] 2026-11-25: the upload policy table still gives the standard 4 GB and Premium or Edge 64 GB ceilings | capture: sha256:9ad44c54a5004bf0100b4aaf3906373cdab0904d12cf015ed57653e780152be9 | quote: | Video size | 4 GB per file maximum | 64 GB |
  - [1] 2026-11-25: the upload policies page still states a 24-hour suspension on limit breach | capture: sha256:9ad44c54a5004bf0100b4aaf3906373cdab0904d12cf015ed57653e780152be9 | quote: If you reach one of these limits, your upload privileges may be suspended for 24 hours and an error message will be displayed on your upload interface.
- sources:
  - [1] https://faq.dailymotion.com/hc/en-us/articles/115009030568-Upload-policies-technical-specifications
  - [2] https://www.dailymotion.com/video/x8j8n7k`
  - [3] https://faq.dailymotion.com/api/v2/help_center/en-us/articles/115009030568.json
