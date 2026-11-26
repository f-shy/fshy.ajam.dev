# slab

> slab.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/slab/ | JSON https://fshy.ajam.dev/api/v1/entity/slab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## slab

- `storage/slab` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:26.831Z (live) | stale on 2026-12-04
- url https://slab.com/pricing/
- free tier: none reachable: Free plan caps attachments at 10 MB and the API (the only programmatic route) is 'only available to customers on the Business or Enterprise plan'. 10 MB x 90-day version history is not a… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Free plan caps attachments at 10 MB and the API (the only programmatic route) is 'only available to customers on the Business or Enterprise plan'. 10 MB x 90-day version history is not a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free plan caps attachments at 10 MB and the API (the only programmatic route) is 'only available to customers on the Business or Enterprise plan'. 10 MB x 90-day version history is not a…
  - [2] 2026-10-21: cited as the basis of the rejection: Free plan caps attachments at 10 MB and the API (the only programmatic route) is 'only available to customers on the Business or Enterprise plan'. 10 MB x 90-day version history is not a sto
  - [1] 2026-11-19: Slab's live pricing page caps Free-plan attachments at 10 MB | capture: sha256:8e95dd47aa679774b2214af64be494b793147e6a6335f0c605feff67e3b4af9a | quote: | Attachments | 10MB | 25MB | 100MB | Custom |
  - [1] 2026-11-19: Slab's API is listed only on the Business and Enterprise plans, not Free | capture: sha256:8e95dd47aa679774b2214af64be494b793147e6a6335f0c605feff67e3b4af9a | quote: | API | | | GraphQL | GraphQL |
  - [1] 2026-11-19: Slab's free plan requires no card | capture: sha256:8e95dd47aa679774b2214af64be494b793147e6a6335f0c605feff67e3b4af9a | quote: Use Slab free forever. No credit card required.
- sources:
  - [1] https://slab.com/pricing/
  - [2] https://help.slab.com/en/articles/6545629-developer-tools-api-webhooks
