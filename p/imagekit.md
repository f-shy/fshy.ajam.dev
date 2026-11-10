# ImageKit

> imagekit.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/imagekit/ | JSON https://fshy.ajam.dev/api/v1/entity/imagekit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## imagekit

- `storage/imagekit-2` | fails-egress | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:23.415Z (live) | stale on 2026-12-04
- url https://imagekit.io/plans/
- disagrees on verdict: `storage/imagekit` says fails-quota, `storage/imagekit-2` says fails-egress
- free tier: none reachable: Free plan: 3 GB DAM storage (fixed limit) and 20 GB bandwidth/month; 225 GB storage costs $89/mo | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Free plan: 20 GB bandwidth, monthly limit. Lite (USD 9/mo): 40 GB bandwidth, then USD 0.5/GB. Pro (USD 89/mo): 225 GB bandwidth, then USD 0.45/GB. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: the 2026-11-03 evidence rows read the vendor page https://imagekit.io/plans/ (20 GB bandwidth on the free plan; 225 GB bandwidth then $0.45/GB); the free-plan storage figure and the Lite plan price were not quoted from it, and the sign-up fields were not read
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free plan: 3 GB DAM storage (fixed limit) and 20 GB bandwidth/month; 225 GB storage costs $89/mo
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free plan: 3 GB DAM storage (fixed limit) and 20 GB bandwidth/month; 225 GB storage costs $89/mo
  - [1] 2026-11-03: Pro plan includes 225 GB bandwidth then USD 0.45/GB | capture: sha256:9950d07fbb3949ffe96ba339cfaf86cc4a3b498a319ed1668980657ad56d7f0e | quote: 225 GB bandwidth $0.45/GB after that
  - [1] 2026-11-03: Free plan includes 20 GB bandwidth | capture: sha256:9950d07fbb3949ffe96ba339cfaf86cc4a3b498a319ed1668980657ad56d7f0e | quote: 20 GB bandwidth
- sources:
  - [1] https://imagekit.io/plans/

## ImageKit (free plan)

- `storage/imagekit` | fails-quota | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://imagekit.io
- disagrees on verdict: `storage/imagekit` says fails-quota, `storage/imagekit-2` says fails-egress
- free tier: 3 GB DAM storage, fixed. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 20 GB/month bandwidth on free, then $0.50/GB. Metered. | metered: yes | free allowance: 20 GB per month
- identity: email
- interface: rest
- limits note: 3 GB DAM storage is a fixed limit (their word), 20 GB/mo bandwidth. Originals are stored and served via the original/raw path; transformations are separate derivatives, so byte fidelity is good. Volume is what fails.
- interface detail: rest
- tooling: REST upload API, URL-based transformations, media-library endpoints, SDKs for JS/Python/PHP.
- composes with: Unlimited free accounts x 3 GB. Fixed limit, not a soft cap.
- reliability: Over-quota blocks uploads and eventually delivery; stored originals are not deleted on plan exhaustion.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 3 GB DAM storage, fixed.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '3 GB DAM storage' / 'Fixed limit'; '20 GB bandwidth' / 'Monthly limit'
  - [1] 2026-10-21: Lite $9/mo = 10 GB DAM storage, showing 3 GB is the free ceiling
- sources:
  - [1] https://imagekit.io/plans/
