# Pipeshift

> pipeshift.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pipeshift/ | JSON https://fshy.ajam.dev/api/v1/entity/pipeshift.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pipeshift

- `compute/pipeshift` | paid-only | evidence documented | binding write-gated | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-10-30T00:03:23.259Z (live) | stale on 2026-11-30
- url https://pipeshift.com
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1] | note: unverified: https://pipeshift.com/pricing answered HTTP 404 on 2026-11-03. No H100, A100, L40S, RTX 4090 or L4 price is listed on the site.
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no plan, price or self-serve path: engagement is through forward-deployed engineers [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Paid-only rather than dead: the product is sold and reachable. Pipeshift sells managed, single-tenant inference clusters on Pipeshift Cloud, with a self-hosted deployment in the user's VPC as the other option; no plan or price is published.
- evidence note: the site was read on 2026-10-22 and again on 2026-10-29. It sells managed, single-tenant inference clusters on Pipeshift Cloud, or self-hosted in the user's VPC, with no plan, price or self-serve path, which confirms paid-only
- self hosted: no
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the site was read on 2026-10-22 and sells inference infrastructure orchestration: 'Pipeshift's custom-built infrastructure orchestration - load balancers, schedulers and auto scalers', with a 'Modular Architecture for GPU Inference Clusters (MAGIC)'. No plan and no price
  - [1] 2026-10-29: Pipeshift sells managed, single-tenant inference clusters on Pipeshift Cloud; a self-hosted deployment in a user's VPC is the other option | capture: sha256:71db6bbda8c0b3ac75fde5372357f7d51f1be1a6f6260bbe6b635c3ff1f064d7 | quote: Rapidly scale workloads globally with our single-tenant deployments on Pipeshift Cloud or self-hosted ones in your VPC.
  - probe:https://pipeshift.com/pricing 2026-11-03: the pricing page answers HTTP 404 | capture: sha256:305c9dfdc7231de3ed68f27d98fff01b58a29d4e2332c1aca186af9d66878166 | quote: "status": 404
- sources:
  - [1] https://pipeshift.com
