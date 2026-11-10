# Loom

> loom.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/loom/ | JSON https://fshy.ajam.dev/api/v1/entity/loom.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Loom (Atlassian)

- `storage/loom` | fails-quota | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.loom.com
- free tier: Free Starter: up to 25 recordings per person, 5 minutes per video, 50 members. Not a storage quota. A recording-count quota. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free playback; no egress meter. | metered: no
- identity: email
- interface: rest
- limits note: 25 videos and 5 minutes are the ceiling; both are product limits on recording, not storage, and the web uploader enforces the same shape.
- interface detail: rest
- tooling: yt-dlp `loom` extractor (verified present; `loom:folder` marked CURRENTLY BROKEN). Loom has no public upload API.
- composes with: Free accounts are limited to 25 videos of up to 5 minutes each, yielding approximately 375 MB per account at standard bitrates.
- reliability: Deletion of old recordings is the norm on free tiers; 25 slots means you must delete to re-record, so it can never accumulate.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free Starter: up to 25 recordings per person, 5 minutes per video, 50 members. Not a storage quota — a recording-count quota.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: table: 'Recordings per person | Up to 25', 'Screen recording length | 5 min per video', 'Members | Up to 50' on the $0 Starter plan
- sources:
  - [1] https://www.loom.com/pricing

## loom / vidyard free tiers

- `storage/loom-vidyard-free-tiers` | fails-quota | evidence documented | binding volume-quota | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:35:00.101Z (live) | stale on 2026-12-04
- url https://www.loom.com/pricing
- free tier: Loom Starter (free): up to 25 recordings per person, 5 min per screen recording, up to 720p; Loom Business is $18 per user / month with unlimited recordings. Vidyard Free: 5 recorded videos a month and 30 minutes per recording; stored videos never expire and the library size is not limited. Neither page states a byte allowance. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): Loom Starter: up to 25 recordings per person, 5 min per video, up to 720p [1]
  - volume-quota (binding): Vidyard Free: 5 recorded videos a month, 30 min per recording, no limit on the number of stored videos [2]
- limits note: Both plans cap by recording count and length, not bytes: Loom Starter 25 recordings per person of 5 min each, Vidyard Free 5 recorded videos a month of 30 min each.
- binding note: recording count and length bound growth rather than bytes: Loom Starter 25 recordings per person of 5 min, Vidyard Free 5 recordings a month of 30 min
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Loom Starter caps recordings at 25 per person and 5 min each; Vidyard Free caps recorded videos at 5 a month and 30 min each, with no limit on the number of stored videos and no expiry. Neither page states a byte allowance.
- notes: the same as reliability
- evidence note: documented: Loom Starter's recordings per person, length per video and quality, and the Business price, are quoted from https://www.loom.com/pricing; Vidyard Free's recordings a month, length limit and library size are quoted from https://knowledge.vidyard.com/hc/en-us/articles/360009875374 (both vendor pages read 2026-11-03); neither page states a byte allowance
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Both cap by recording COUNT and clip LENGTH rather than bytes (Loom 25 videos x 5 min; Vidyard 5/month, 25-slot library). Ceiling is a few hundred MB per account, unreachable toward 500 GB…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Both cap by recording COUNT and clip LENGTH rather than bytes (Loom 25 videos x 5 min; Vidyard 5/month, 25-slot library). Ceiling is a few hundred MB per account, unreachable toward 500 GB…
  - [2] 2026-10-21: cited as the basis of the rejection: Both cap by recording COUNT and clip LENGTH rather than bytes (Loom 25 videos x 5 min; Vidyard 5/month, 25-slot library). Ceiling is a few hundred MB per account, unreachable toward 500 GB w
  - [1] 2026-11-03: Loom Starter allows up to 25 recordings per person | capture: sha256:2e696410ca8288b65e460a7eafe21cf2a1025b9abaecf8b31894ef057314e8b9 | quote: | Recordings per person | Up to 25 | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-03: Loom Starter records 5 min per video | capture: sha256:2e696410ca8288b65e460a7eafe21cf2a1025b9abaecf8b31894ef057314e8b9 | quote: | Screen recording length | 5 min per video | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-03: Loom Starter records up to 720p | capture: sha256:2e696410ca8288b65e460a7eafe21cf2a1025b9abaecf8b31894ef057314e8b9 | quote: | Video quality | Up to 720p | High-definition up to 4k | High-definition up to 4k | High-definition up to 4k |
  - [1] 2026-11-03: Loom Business is priced $18 per user / month with unlimited videos | capture: sha256:2e696410ca8288b65e460a7eafe21cf2a1025b9abaecf8b31894ef057314e8b9 | quote: $18
  - [2] 2026-11-03: Vidyard Free allows 5 recorded videos a month | capture: sha256:8cec421e31c5612a653c904cfffaaf71f3db836e97234e620f65c5a89d7c2f1c | quote: | Free (individual or workspace) | 5/mo | 5 |
  - [2] 2026-11-03: Vidyard Free recordings stop at 30 minutes | capture: sha256:8cec421e31c5612a653c904cfffaaf71f3db836e97234e620f65c5a89d7c2f1c | quote: Vidyard Free plans include a 30-minute length limit on new recordings.
  - [2] 2026-11-03: Vidyard has no limit on the number of videos in the library | capture: sha256:8cec421e31c5612a653c904cfffaaf71f3db836e97234e620f65c5a89d7c2f1c | quote: there is no limit to the number of videos you can have in your library at once.
  - [1] 2026-11-03: Loom Starter caps recordings per person | capture: sha256:2e696410ca8288b65e460a7eafe21cf2a1025b9abaecf8b31894ef057314e8b9 | quote: | Recordings per person | Up to 25 | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-03: Loom Starter is still capped at 25 recordings per person | capture: sha256:2e696410ca8288b65e460a7eafe21cf2a1025b9abaecf8b31894ef057314e8b9 | quote: | Recordings per person | Up to 25 | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-03: Loom Starter is capped at 25 recordings per person; the page gives a count, not a byte allowance | capture: sha256:2e696410ca8288b65e460a7eafe21cf2a1025b9abaecf8b31894ef057314e8b9 | quote: | Recordings per person | Up to 25 | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-03: the vendor page was read and quoted on 2026-11-03: Loom Starter allows up to 25 recordings per person | capture: sha256:2e696410ca8288b65e460a7eafe21cf2a1025b9abaecf8b31894ef057314e8b9 | quote: | Recordings per person | Up to 25 | Unlimited | Unlimited | Unlimited |
- sources:
  - [1] https://www.loom.com/pricing
  - [2] https://knowledge.vidyard.com/hc/en-us/articles/360009875374
