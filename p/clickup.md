# clickup

> clickup.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clickup/ | JSON https://fshy.ajam.dev/api/v1/entity/clickup.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## clickup

- `storage/clickup` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://clickup.com/pricing
- free tier: None reachable: Free Forever Workspace gets 60 MB of total file storage. Not per file, total. Paid jumps straight to 'Unlimited', which confirms the free tier is deliberately useless for this. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Free Forever Workspace gets 60 MB of total file storage — not per file, total. Paid jumps straight to 'Unlimited', which confirms the free tier is deliberately useless for this.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free Forever Workspace gets 60 MB of total file storage — not per file, total. Paid jumps straight to 'Unlimited', which confirms the free tier is deliberately useless for this.
- sources:
  - [1] https://clickup.com/pricing

## clickup (free plan)

- `storage/clickup-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://clickup.com/pricing
- free tier: none reachable: 'File Storage / 60MB' on Free - and the paid tiers are the only route to 'Unlimited'. 60 MB is a rounding error; not chainable in any useful way. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: 'File Storage / 60MB' on Free - and the paid tiers are the only route to 'Unlimited'. 60 MB is a rounding error; not chainable in any useful way.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'File Storage / 60MB' on Free - and the paid tiers are the only route to 'Unlimited'. 60 MB is a rounding error; not chainable in any useful way.
- sources:
  - [1] https://clickup.com/pricing
