# outline

> getoutline.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getoutline/ | JSON https://fshy.ajam.dev/api/v1/entity/getoutline.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## outline (cloud)

- `storage/outline-2` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:38.527Z (live) | stale on 2026-12-04
- url https://www.getoutline.com/pricing
- disagrees on verdict: `storage/outline` says fails-quota, `storage/outline-2` says paid-only
- free tier: None reachable: No free cloud tier at all. 'your first 30 days are free. Once this trial period elapses your knowledge base becomes read-only until a payment method is added'. Trial, not free. Self-hosted. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: No free cloud tier at all — 'your first 30 days are free. Once this trial period elapses your knowledge base becomes read-only until a payment method is added'. Trial, not free. Self-hosted
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No free cloud tier at all — 'your first 30 days are free. Once this trial period elapses your knowledge base becomes read-only until a payment method is added'. Trial, not free. Self-hosted
  - [1] 2026-11-19: the pricing page still states a 30-day trial after which the knowledge base becomes read-only until payment | capture: sha256:e889443dce17692f2dfa153858707d0a802adbeee0d00fc0fe104b61c37d8b41 | quote: When you create a team your first 30 days are free. Once this trial period elapses your knowledge base becomes read-only until a payment method is added.
- sources:
  - [1] https://www.getoutline.com/pricing

## outline

- `storage/outline` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:55.865Z (live) | stale on 2026-12-04
- url https://www.getoutline.com/pricing
- disagrees on verdict: `storage/outline` says fails-quota, `storage/outline-2` says paid-only
- free tier: none reachable: the Cloud plan is a 30-day trial, after which the knowledge base becomes read-only until a payment method is added; the cheapest paid plan is USD 3/user/month, and the unlimited-storage route is self-hosting | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Cloud is trial-only: $10/mo minimum, and 'your first 30 days are free. Once this trial period elapses your knowledge base becomes read-only'. The only unlimited-storage route is…
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Cloud is trial-only: $10/mo minimum, and 'your first 30 days are free. Once this trial period elapses your knowledge base becomes read-only'. The only unlimited-storage route is…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Cloud is trial-only: $10/mo minimum, and 'your first 30 days are free. Once this trial period elapses your knowledge base becomes read-only'. The only unlimited-storage route is…
  - [2] 2026-10-21: cited as the basis of the rejection: Cloud is trial-only: $10/mo minimum, and 'your first 30 days are free. Once this trial period elapses your knowledge base becomes read-only'. The only unlimited-storage route is self-hosting
  - [1] 2026-11-19: the first-party pricing page confirms Cloud is a 30-day trial then read-only until payment, so no free hosted tier exists | capture: sha256:e889443dce17692f2dfa153858707d0a802adbeee0d00fc0fe104b61c37d8b41 | quote: When you create a team your first 30 days are free. Once this trial period elapses your knowledge base becomes read-only until a payment method is added.
  - [1] 2026-11-19: the pricing page confirms the 30-day trial and read-only after expiry | capture: sha256:e889443dce17692f2dfa153858707d0a802adbeee0d00fc0fe104b61c37d8b41 | quote: When you create a team your first 30 days are free. Once this trial period elapses your knowledge base becomes read-only until a payment method is added.
- sources:
  - [1] https://www.getoutline.com/pricing
  - [2] https://docs.getoutline.com/s/hosting/doc/file-storage-N4M0T6Ypu7
