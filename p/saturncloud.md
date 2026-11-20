# saturn cloud

> saturncloud.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/saturncloud/ | JSON https://fshy.ajam.dev/api/v1/entity/saturncloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## saturn cloud

- `storage/saturn-cloud` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:23.338Z (live) | stale on 2026-12-04
- url https://saturncloud.io/plans/saturn_cloud_plans/
- free tier: No free tier on the current plans page. It opens into paid GPU inference: dedicated endpoints from USD 1.10 per GPU-hour and serverless tokens from USD 0.0125 per 1M input tokens. No storage allowance stated. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The current plans page sells paid GPU inference endpoints; no free storage allowance is stated.
- notes: No free tier on the current plans page. It opens directly into a paid GPU/CPU rate table (cheapest listed is a 4 GB / 2 vCPU t3.medium at $0.15/hr, then nebius boxes). No storage allowance.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: No free tier on the current plans page — it opens directly into a paid GPU/CPU rate table (cheapest listed is a 4 GB / 2 vCPU t3.medium at $0.15/hr, then nebius boxes). No storage allowance
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No free tier on the current plans page — it opens directly into a paid GPU/CPU rate table (cheapest listed is a 4 GB / 2 vCPU t3.medium at $0.15/hr, then nebius boxes). No storage allowance
  - [1] 2026-11-19: the current plans page lists dedicated GPU endpoints from USD 1.10 per GPU-hour and serverless tokens from USD 0.0125 per 1M input tokens | capture: sha256:c99e0600e92bf1ce15aab00651597d50d62e7152753e069b7efcb5b538c67a68 | quote: From$1.10per GPU-hour ... From$0.0125per 1M input tokens
  - [1] 2026-11-19: the current plans page is a paid GPU inference rate card | capture: sha256:c99e0600e92bf1ce15aab00651597d50d62e7152753e069b7efcb5b538c67a68 | quote: From$1.10per GPU-hour ... From$0.0125per 1M input tokens
  - [1] 2026-11-19: the platform still has a free signup to try it, with no free storage allowance stated | capture: sha256:c99e0600e92bf1ce15aab00651597d50d62e7152753e069b7efcb5b538c67a68 | quote: Yes. Sign up for a free account to try the platform.
- sources:
  - [1] https://saturncloud.io/plans/saturn_cloud_plans/
