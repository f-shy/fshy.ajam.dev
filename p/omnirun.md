# OmniRun

> omnirun.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/omnirun/ | JSON https://fshy.ajam.dev/api/v1/entity/omnirun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OmniRun

- `compute/omnirun` | paid-only | evidence documented | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:36.911Z (live) | stale on 2026-11-22
- url https://omnirun.io/pricing
- free tier: no free tier and no price list: capacity is arranged per client with an agreed sandbox-hour quota, shown on the page as an example of 600 hours a month | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no self-serve plan and no price list: limits and price are agreed per client [1]
  - request-rate: capacity is quoted in sandbox-hours a month against an agreed quota [1]
  - retention-clamped: the page describes per-sandbox lifetimes from seconds to hours as a term to be agreed [1]
- limits note: Session cap, idle-reap and network policy are not documented. Ranked partial.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states in as many words that there is no public price list and no self-serve plan. The verdict moves to fails-identity only if access needs an institution; it needs a contract, which is a sales gate
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: sandbox lifetime is a term of the agreement, 'seconds, minutes or hours per sandbox'
  - free_tier_kind: none
  - ps.price: part of the agreed terms
  - ps.durability: bare-metal hosts with KVM and Firecracker
  - ps.retention: the agreed quota
  - net.out: yes
  - net.in: yes
  - net.ports: preview URLs for ports
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Managed OmniRun is arranged per client or team. There is no public price list and no self-serve plan: we size limits with you.' and 'Sandbox-hours this month 412.6 h of 600 h agreed quota', quoted
- sources:
  - [1] https://omnirun.io/pricing
