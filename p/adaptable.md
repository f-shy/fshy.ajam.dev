# Adaptable

> adaptable.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/adaptable/ | JSON https://fshy.ajam.dev/api/v1/entity/adaptable.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Adaptable

- `compute/adaptable` | dead | evidence documented | binding retention-clamped | category platform host | tier none
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:55:00.000Z (live) | stale on 2026-11-24
- url https://adaptable.io/
- free tier: nothing reachable: every path on adaptable.io returned a Cloudflare 530 from the origin on 2026-10-24, which is a DNS or origin failure rather than a page | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable: the service does not answer
- retention: the free Starter plan ended on 2024-09-23 and all apps were paused on 2025-02-15
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: not applicable: no signup page is served
- interface: unknown
- limits:
  - retention-clamped (binding): origin answers 530 on the root path [1]
- limits note: there is no allowance to bind: the product is gone.
- binding note: there is no service to bind.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: none: Service is inactive.
- reliability: Cloudflare error 530 means the origin DNS entry is missing or the origin refused; it is not a challenge page
- notes: One route tried today: HTTP request to https://adaptable.io/, which returned 530. The earlier routes tried on this record (direct fetch, /docs/free-app-hosting, search) are not repeated here.
- evidence note: the 530 was observed today on the root path; the shutdown history is carried from earlier readings and remains unverified against live endpoints.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: none
  - billing_model: none
  - term: none
  - price_arithmetic: none
  - free_tier_kind: none
  - session_cap.restart_required: no
  - session_cap.note: dead
- evidence:
  - [2] 2026-10-22: via the search index of the page: 'We have made the very difficult decision to end our free Starter Plan on September 23, 2024'; apps paused 2024-09-23 and permanently deleted 2024-10-07 including database data, quoted
  - [3] 2026-10-22: via the search index of the page: 'Adaptable is shutting down. All apps will be paused on February 15, 2025', quoted
  - [1] 2026-10-22: 
  - [1] 2026-10-24: 
- sources:
  - [1] https://adaptable.io/
  - [2] https://adaptable.io/docs/free-app-hosting
  - [3] https://adaptable.io/terms
