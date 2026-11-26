# Sirv

> sirv.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sirv/ | JSON https://fshy.ajam.dev/api/v1/entity/sirv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sirv (free plan)

- `storage/sirv` | fails-quota | evidence documented | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:26.831Z (live) | stale on 2026-12-20
- url https://www.sirv.com
- free tier: 0.5 GB storage. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 2 GB/month on free. Effectively a demo. | metered: no | free allowance: 2 GB per month
- identity: email
- interface: s3-compatible, rest
- limits note: 0.5 GB storage, 2 GB bandwidth, 5,000 processing requests/month. Soft limits allow 2x allowance for 30 days.
- interface detail: rest
- tooling: REST/S3-compatible upload, URL image transformations, spin/360 tooling.
- composes with: Unlimited free accounts x 0.5 GB. 2,000 accounts for 1 TB, which is not trivial.
- reliability: Over-allowance degrades to soft-limit warnings then blocking. Originals are retained (Sirv keeps the source file and generates derivatives).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 0.5 GB storage, 2 GB bandwidth, 5,000 processing requests/month. Soft limits allow 2x allowance for 30 days.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Storage limit... 0.5 GB storage'; 'Bandwidth (monthly)... 2 GB'; 'Soft limits... you'll get double your allowance for 30 days'
  - [1] 2026-11-19: Sirv's first-party pricing page was read and captured | capture: sha256:a337e0c1c3518972cb1110743108e13cc06f7b91aa2be8913215ea0995d23a8a | quote: 0.5 GB storage
  - [1] 2026-11-19: Sirv's live pricing page still lists 0.5 GB storage on the Free plan | capture: sha256:a337e0c1c3518972cb1110743108e13cc06f7b91aa2be8913215ea0995d23a8a | quote: 0.5 GB storage
  - [1] 2026-11-19: Sirv's free plan still lists 2 GB monthly bandwidth | capture: sha256:a337e0c1c3518972cb1110743108e13cc06f7b91aa2be8913215ea0995d23a8a | quote: Bandwidth (monthly) Total size of all optimized files served to your visitors in one month (bandwidth). File uploads don't count towards transfer usage. | 2 GB | 20 GB | Custom |
- sources:
  - [1] https://www.sirv.com/pricing/
