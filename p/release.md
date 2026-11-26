# Release

> release.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/release/ | JSON https://fshy.ajam.dev/api/v1/entity/release.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Release

- `compute/release` | paid-only | evidence documented | binding write-gated | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-25T15:03:50.982Z (live) | stale on 2026-12-26
- url https://release.com/pricing
- free tier: Enterprise pricing is based on your specific needs and usage patterns. | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no free plan: the page lists enterprise plans only, and the environments deploy into self-hosted cloud account [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and lists enterprise features with no free plan, which confirms paid-only. The compute runs in self-hosted cloud account
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a user's own cloud sets the clocks
  - network_out.out: yes
  - network_out.in: yes
  - network_out.ports: a user's own cloud account
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the pricing page was read on 2026-10-22 and describes enterprise plans with SSO, RBAC, Helm and Terraform support and 'Unlimited clusters'; it publishes no free tier
  - [1] 2026-11-25: the page states pricing is custom enterprise pricing and states no free tier | capture: sha256:5f33372f2445872be444a6086795ef15afe91e1a998d18c857dc95040b38e599 | quote: Enterprise pricing is based on your specific needs and usage patterns.
  - [1] 2026-11-25: pricing remains custom enterprise pricing with no free tier stated | capture: sha256:5f33372f2445872be444a6086795ef15afe91e1a998d18c857dc95040b38e599 | quote: Enterprise pricing is based on your specific needs and usage patterns.
- sources:
  - [1] https://release.com/pricing
