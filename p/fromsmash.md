# fromsmash free

> fromsmash.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fromsmash/ | JSON https://fshy.ajam.dev/api/v1/entity/fromsmash.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## fromsmash free tier

- `storage/fromsmash-free-tier` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:30.232Z (live) | stale on 2026-12-04
- url https://fromsmash.com/pricing
- free tier: none reachable: 2 GB before queueing; the '100 GB free' claim is a 14-day developer TRIAL, not a free tier. API access requires a paid account. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: 2 GB before queueing; the '100 GB free' claim is a 14-day developer TRIAL, not a free tier. API access requires a paid account.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 2 GB before queueing; the '100 GB free' claim is a 14-day developer TRIAL, not a free tier. API access requires a paid account.
  - [2] 2026-10-21: cited as the basis of the rejection: 2 GB before queueing; the '100 GB free' claim is a 14-day developer TRIAL, not a free tier. API access requires a paid account.
  - [1] 2026-11-19: the free plan asks for no payment and no sign-up | capture: sha256:e643928df5f40d2f51abaf62755226ae7a7a6d94ac471c6f5f4c071e314cd909 | quote: Free $0.00 No payment required. No sign-up required.
  - [1] 2026-11-19: the free plan provides no storage; transfers are capped at 2 GB and valid 7 days | capture: sha256:e643928df5f40d2f51abaf62755226ae7a7a6d94ac471c6f5f4c071e314cd909 | quote: No storage
- sources:
  - [1] https://fromsmash.com/pricing
  - [2] https://api.fromsmash.com/docs/quick-start

## Smash (fromsmash.com) — Free web tier

- `storage/smash-free-web-tier` | fails-quota | evidence documented | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:26.833Z (live) | stale on 2026-12-20
- url https://fromsmash.com/discover-smash/everyone
- free tier: No file size limit and no limit on number of transfers on the free web tier; no account required. Transfers above 2 GB are queued behind paid traffic. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object behaviour beyond 2 GB | bytes: 2000000000 | source: [1] | note: not stated
- retention: Free transfers are valid for 7 days | source: [1] | note: not stated
- egress: Free and unmetered on the free tier (no per-GB line anywhere on the pricing page); free tier is ad-supported. | metered: no
- identity: institution
- interface: rest
- limits:
  - retention-clamped: retention 7 days [1]
  - retention-clamped: deleted at 7 days [1]
  - per-object-cap (binding): per-object behaviour beyond 2 GB [1]
- limits note: Retention 7 days on free (30 days paid). This is the binding constraint; no per-object-cap on the anonymous web tier; per-object behaviour beyond 2 GB is queue+deprioritisation not rejection; API keys are '100 GB, 14-day free trial (No credit card required)'. Trial, not free tier.
- interface detail: rest (official API + SDKs, but gated behind an API key) / web for the anonymous path
- tooling: Official SDKs: @smash-sdk/uploader (npm), @smash-sdk/downloader, github.com/fromsmash/smash-uploader-js, smash-sdk-js, smash-downloader-js; docs api.fromsmash.com/docs/quick-start
- composes with: Per-transfer model caps multiplication: unlimited transfers but each dies in 7 days. As storage it is a 7-day rolling window. N transfers/day x (size) x 7 days, nothing retained past 7. The API path (100 GB trial key x free accounts) is a 14-day trial, not perpetual.
- reliability: Free transfers are queued when >2 GB with no SLA on queue time; files are 'stored temporarily' on AWS regions and deleted at 7 days.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No file size limit and no limit on number of transfers on the free web tier; no account required. Transfers above 2 GB are queued behind paid traffic.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free '$0.00 ... - 2 GB per transfer* - Transfers valid for 7 days; *Beyond 2 GB, transfers join a queue behind Pro transfers'
  - [2] 2026-10-21: 'With the free version, there is no file size limit for the files you send. However ... transfers larger than 2 GB are not prioritized and are placed in a waiting queue' (dated February 27, 2026)
  - [3] 2026-10-21: 'You will have a 100 GB, 14-day free trial (No credit card required)'
  - [4] 2026-10-21: probe: GET -> 200 (660,946 bytes); POST https://api.fromsmash.com/transfer -> 404 text/plain (endpoint path differs, no anonymous write path found); GET https://transfer.fromsmash.com/<zero-uuid> -> 404 (27,204 bytes, real 404 not a 200 error page)
  - [1] 2026-11-19: Smash's first-party pricing page was read and captured | capture: sha256:e643928df5f40d2f51abaf62755226ae7a7a6d94ac471c6f5f4c071e314cd909 | quote: - 2 GB per transfer*
  - [1] 2026-11-19: Smash's live pricing page still lists 2 GB per transfer on the free tier | capture: sha256:e643928df5f40d2f51abaf62755226ae7a7a6d94ac471c6f5f4c071e314cd909 | quote: - 2 GB per transfer*
  - [1] 2026-11-19: Smash's pricing page states a 7-day validity for free transfers | capture: sha256:e643928df5f40d2f51abaf62755226ae7a7a6d94ac471c6f5f4c071e314cd909 | quote: - Transfers valid for 7 days
  - [5] 2026-11-19: Smash's free web tier needs no account | capture: sha256:33a3a913cd5b311f0b3b70709b634a96b8c51168eb9839fd26f04356d7133ce6 | quote: Your photos, videos, or work documents: send them in seconds, with no size limit and no account required.
  - [1] 2026-11-19: Smash queues free transfers above 2 GB behind paid traffic | capture: sha256:e643928df5f40d2f51abaf62755226ae7a7a6d94ac471c6f5f4c071e314cd909 | quote: *Beyond 2 GB, transfers join a queue behind Pro transfers.
- sources:
  - [1] https://fromsmash.com/pricing
  - [2] https://fromsmash.com/help/articles/13885610-what-is-the-file-size-limit-on-smash
  - [3] https://api.fromsmash.com/docs/quick-start
  - [4] https://api.fromsmash.com/
  - [5] https://fromsmash.com/discover-smash/everyone
