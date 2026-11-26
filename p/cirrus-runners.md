# Cirrus Runners

> cirrus-runners.app | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cirrus-runners/ | JSON https://fshy.ajam.dev/api/v1/entity/cirrus-runners.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cirrus Runners

- `compute/cirrus-runners` | dead | evidence documented | binding write-gated | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-11-24T11:38:11.670Z (live) | stale on 2026-12-25
- url https://cirrus-runners.app/pricing/
- free tier: none: Cirrus Runners is a subscription of $150 a month per runner with no limit on minutes, and it no longer accepts new customers | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: subscription for dedicated runners; the page prices against GitHub's managed rates rather than per minute [1]
  - per-object-cap: a vCPU is a single physical core, so the machine's core count is the real concurrency ceiling [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. It sells dedicated physical cores by subscription and publishes no free tier, which confirms paid-only and gives the shape axis: one vCPU is one physical core, not a hyperthread
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.gpu_class: paravirtualized GPU on the Linux GPU runner
  - shape.note: shapes run to 16 dedicated vCPU cores and 4 M4 Pro cores; each vCPU is one physical core
  - session_cap.restart_required: no
  - session_cap.note: a runner is allocated while a job needs it; the page states no idle reap
  - free_tier_kind: none
  - death.on: 2026-11-03
  - death.cause: registration-closed
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Each vCPU is backed by a single physical core' and 'Linux x86: High-frequency x86 CPUs (2x faster)' with per-machine comparisons against GitHub-managed runners, quoted; the page publishes no free tier
  - [1] 2026-11-03: Cirrus Runners is a $150 a month subscription per runner with unlimited minutes and no free tier | capture: sha256:a130c9b78fd972ab4c37f6cfe2f4591f20dca2af4066ae0c4cc4e9738553255f | quote: Each Cirrus Runner costs $150 a month and there is no limit on the amount of minutes for your actions.
  - [2] 2026-11-03: Cirrus Runners, a separate product from Cirrus CI, is closed to new customers by the same announcement | capture: sha256:2fcf1b3d8ce8a9ca14f6b6c131587adcce7033c13e5d145d570d384b1a974542 | quote: We are no longer accepting new customers for Cirrus Runners but will continue supporting the service for existing customers through their existing contract periods.
  - [1] 2026-11-24: the subscription price and unlimited minutes are unchanged and no free tier is published | capture: sha256:963dbd1e3fc4c6dfe5418ebf637635d5307f383f7d423ad8cd8ff89c3d5f0a03 | quote: Each Cirrus Runner costs $150 a month and there is no limit on the amount of minutes for your actions.
  - [2] 2026-11-24: Cirrus Runners is still closed to new customers | capture: sha256:92970fa6b767e1deffc6bf4929753e693717d79ee9360c6def05fbb968ba855b | quote: We are no longer accepting new customers for Cirrus Runners but will continue supporting the service for existing customers through their existing contract periods.
- sources:
  - [1] https://cirrus-runners.app/pricing/
  - [2] https://cirruslabs.org/
