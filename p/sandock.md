# Sandock

> sandock.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sandock/ | JSON https://fshy.ajam.dev/api/v1/entity/sandock.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sandock

- `compute/sandock` | paid-only | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T15:03:47.061Z (live) | stale on 2026-12-26
- url https://sandock.ai/pricing
- free tier: Plus is $5/month with 5 sandboxes and 2 GB storage. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: The FAQ says Sandock is a paid product and no free plan is offered; Pro plans run from $15/month to $100/month, code executions are not limited by plan, and session timeouts are 4 hours on Plus and 8 hours on Pro.
- per-object cap: not applicable | source: [1]
- retention: The session timeout is the binding term: 4 hours on Plus and 8 hours on Pro, so a sandbox cannot hold a job longer than that no matter how much CPU it has. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - retention-clamped (binding): The session timeout is the binding term: 4 hours on Plus and 8 hours on Pro, so a sandbox cannot hold a job longer than that no matter how much CPU it has. [1]
- limits note: The session timeout is the binding term: 4 hours on Plus and 8 hours on Pro, so a sandbox cannot hold a job longer than that no matter how much CPU it has.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 5 a month for five sandboxes with no per-execution charge is the cheapest flat subscription documented; it suits a fixed small fleet of long-lived Docker environments where the count is known, and it does not suit fan-out because every sandbox beyond five needs a plan change.
- reliability: no reliability event recorded
- notes: The cheapest paid shape recorded among documented hosts by subscription, and the honest floor for a Docker sandbox that must not be rebuilt from scratch. It is recorded as paid-only because the vendor states plainly that there is no free plan, which refutes the 'start free' line in the page description that the page itself then contradicts in its own FAQ. The RAM per sandbox is not stated on the pricing page, so shape carries null for RAM; 'up to 4 vCPU' is the only compute number published. Session timeouts of 4 and 8 hours are short for an agent that runs overnight.
- extras:
  - facets.class: cheap-flat-sandbox
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 4
  - facets.shape.disk_gib: 2
- evidence:
  - [1] 2026-10-22: 'Sandock is a paid product - an active subscription is required to use the platform'; Plus USD 5 per month with 5 sandboxes, 2 GB storage, a 4 hour session timeout and up to 4 vCPU
  - [1] 2026-10-22: Pro tiers: Starter USD 15 (10 sandboxes, 2 GB), Growth USD 30 (25 sandboxes, 10 GB), Scale USD 60 (60 sandboxes, 30 GB), Business USD 100 (150 sandboxes, 100 GB); 'Sandock does not limit plans by the number of code executions'
  - [1] 2026-10-22: a 14-day money-back guarantee on paid plans and billing through Creem
  - [1] 2026-11-25: the pricing FAQ states the cheapest paid plan, Plus, at $5 per month with 5 sandboxes and 2 GB storage | capture: sha256:bdfb0445022f0d884679a02e098b1912a06f9ee5b73c0defb3a342a92a6ac0b0 | quote: Plus is $5/month with 5 sandboxes and 2 GB storage.
  - [1] 2026-11-25: the FAQ describes paid plans starting at $5 and $15 per month | capture: sha256:bdfb0445022f0d884679a02e098b1912a06f9ee5b73c0defb3a342a92a6ac0b0 | quote: We offer a Plus plan at $5/month and Pro plans from $15/month, so you can start small and scale as your needs grow.
- sources:
  - [1] https://sandock.ai/pricing
