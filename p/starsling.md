# StarSling

> starsling.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/starsling/ | JSON https://fshy.ajam.dev/api/v1/entity/starsling.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## StarSling

- `compute/starsling` | paid-only | evidence documented | binding request-rate | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-25T15:03:52.090Z (live) | stale on 2026-12-26
- url https://starsling.dev/pricing
- free tier: New accounts get 2,000 free minutes in their first month. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $0.004 a minute for 2 vCPU and 8 GB, $0.008 for 4 vCPU and 16 GB [1]
  - request-rate (binding): unlimited concurrency, with no job queue limit stated [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes the per-minute CPU and GPU ladder with unlimited concurrency. There is no free tier, so the verdict moves to paid-only; the free items are open-source audit skills
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 4
  - shape.ram: 16
  - shape.note: the default runner at 4 vCPU and 16 GB; CPU shapes run from 2 to 64 vCPU
  - session_cap.restart_required: no
  - session_cap.note: a runner is allocated per job and billed per minute
  - free_tier_kind: none
  - granularity.min_billed_s: 60
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Per-minute CPU and GPU pricing, with unlimited concurrency' with '| 2 vCPU / 8 GB | $0.004 | $0.006 | 33% |' and '4 vCPU / 16 GB default $0.008 | $0.012 | 33%' against GitHub's $0.012 a minute, quoted
  - [1] 2026-11-25: new accounts receive 2,000 free minutes in their first month | capture: sha256:680f1099499f73f39aa042ca2069e1bc2f4e2df3adee9332d7c004adde729f2c | quote: New accounts get 2,000 free minutes in their first month.
- sources:
  - [1] https://starsling.dev/pricing
