# Sandock

> sandock.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sandock/ | JSON https://fshy.ajam.dev/api/v1/entity/sandock.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sandock

- `compute/sandock` | paid-only | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://sandock.ai/pricing
- free tier: Plus is USD 5 per month for 5 sandboxes, 2 GB of storage, a 4-hour session timeout and up to 4 vCPU. Pro runs from USD 15 per month (10 sandboxes, 2 GB) through USD 30 (25 sandboxes, 10 GB, 8-hour timeout, up to 8 vCPU), USD 60 (60 sandboxes) to USD 100 (150 sandboxes). Code executions are not limited by plan: plans differ on sandbox count, storage, session timeout, compute capacity and support. There is no free plan. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
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
- sources:
  - [1] https://sandock.ai/pricing
