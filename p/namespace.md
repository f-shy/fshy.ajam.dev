# Namespace

> namespace.so | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/namespace/ | JSON https://fshy.ajam.dev/api/v1/entity/namespace.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Namespace

- `compute/namespace` | trial-only | evidence documented | binding retention-clamped | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:16.615Z (inherited) | stale on 2026-12-05
- url https://namespace.so/pricing
- free tier: a 30-day free trial of Compute, Devboxes, GitHub Runners and more; the plans themselves start at USD 0 for a limited tier and are billed per minute above it | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: '30-day free trial of Compute, Devboxes, Github Runners, and more'
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: no egress allowance or overage price on https://namespace.so/pricing and https://namespace.so/docs/workspaces/billing-and-limits.md | metered: no | source: [1]
- identity: email
- interface: cli, ssh, rest
- limits:
  - retention-clamped (binding): the trial runs 30 days [1]
- binding note: the 30-day clock ends the offer
- interface detail: nsc CLI and devbox CLI with SSH into instances; a public API served over gRPC and Connect (listed as rest: no grpc term); TypeScript and Go SDKs
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- extras:
  - keep_rate: 0.0
  - keep_rate_basis: suspends on idle (auto_stop_idle)
  - billing_model: unclassified
  - free_tier_kind: trial
  - burst_x: 1.0159
- evidence:
  - [1] 2026-10-22: '30-day free trial of Compute, Devboxes, Github Runners, and more'; a 2 vCPU / 4 GB shape is $0.002/min
  - [1] 2026-11-03: the pricing page prices compute minutes with an overage rate and prints no egress allowance or overage price | capture: sha256:73b0d2398fe288585f9cb989eb37dba7cbf1c7f88bf5e15fdf82afe4234f754b | quote: Prepaid cost is the effective cost of minutes in your plan, overage is the cost of any usage that exceeds your plan.
  - [2] 2026-11-03: the nsc CLI opens an SSH shell in an instance | capture: sha256:2daaeb58d172f8b07481b2951c46722fb45928653b3f57327f6df050b75a3ca3 | quote: nsc ssh <instance-id>
  - [3] 2026-11-03: a public gRPC/Connect API and SDKs (TypeScript, Go) exist | capture: sha256:4d53aebc82d06b96fc457b07b6bb042f0c4dac301379fc3a759ff289829db026 | quote: The same API the SDKs use is public. It is defined in Protocol Buffers, published at [buf.build/namespace/cloud](https://buf.build/namespace/cloud), and served over gRPC and Connect.
- sources:
  - [1] https://namespace.so/pricing
  - [2] https://namespace.so/docs
  - [3] https://namespace.so/docs/reference/sdk.md
