# directus cloud

> directus.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/directus/ | JSON https://fshy.ajam.dev/api/v1/entity/directus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## directus cloud (core)

- `storage/directus-cloud` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:34.058Z (live) | stale on 2026-12-04
- url https://directus.io/pricing
- free tier: None reachable: Core is now $89/mo billed yearly ($99 monthly), with a 14-day free trial and no commitment; it is capped at 3 user seats, 25 collections and 5 flows and advertises no free storage allowance. Assets go to a storage adapter the deployment configures. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Core is $0/mo but is capped on seats/collections (3 seats, 25 collections, 5 flows) and provides no advertised free storage allowance. Assets go to a storage adapter the deployment configures. Self-h.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Core is $0/mo but is capped on seats/collections (3 seats, 25 collections, 5 flows) and provides no advertised free storage allowance — assets go to a storage adapter the deployment configures. Self-h
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Core is $0/mo but is capped on seats/collections (3 seats, 25 collections, 5 flows) and provides no advertised free storage allowance — assets go to a storage adapter the deployment configures. Self-h
  - [1] 2026-11-19: Core now costs $89/mo, with a 14-day free trial and 3 seats, 25 collections, 5 flows | capture: sha256:a5a7e3b6e001ae3ab6081d539a8e99ce28ab13c383d384873370eeb0d5e09278 | quote: # Core Evaluate Directus or power small, individual builds within the seat and collection limits. # $89 / mo Billed yearly, or $99 monthly [Start Free Trial](https://directus.cloud/account/register/) 14-day free trial · No commitment 3 user seats, 25 Collections, 5 Flows, AI Assistant, Advanced RBAC, Community Support
  - [1] 2026-11-19: Directus Core now costs $89/mo with a 14-day free trial, not a $0/mo free tier | capture: sha256:a5a7e3b6e001ae3ab6081d539a8e99ce28ab13c383d384873370eeb0d5e09278 | quote: # Core Evaluate Directus or power small, individual builds within the seat and collection limits. # $89 / mo Billed yearly, or $99 monthly [Start Free Trial](https://directus.cloud/account/register/) 14-day free trial · No commitment 3 user seats, 25 Collections, 5 Flows, AI Assistant, Advanced RBAC, Community Support
- sources:
  - [1] https://directus.io/pricing
