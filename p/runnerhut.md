# RunnerHut

> runnerhut.com | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runnerhut/ | JSON https://fshy.ajam.dev/api/v1/entity/runnerhut.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RunnerHut

- `ci-cd-runners/runnerhut` | qualifies-with-caveat | evidence documented | binding request-rate | category CI runner (hosted, GitHub Actions-compatible)
- needs card no, phone no, ID no, institution no | verified 2026-11-10T02:39:57.384Z (live) | stale on 2026-12-11
- url https://runnerhut.com/pricing
- free tier: 3,000 Linux minutes a month on the free plan, with unlimited cache, every runner family and full analytics; per-second billing with a one-minute minimum beyond it. The 2 vCPU Linux x64 runner is USD 0.0040 a minute, the 2 vCPU ARM64 runner USD 0.0032, Windows USD 0.0080, macOS USD 0.0400 and an L4 GPU runner USD 0.0900. | unit: minutes | metered on: wall-clock | read on: 2026-11-10 | source: [1]
- per-object cap: not applicable: a job is bounded by the runner size, and the page prices a 2 vCPU tier and scales linearly with size
- retention: not applicable: a job runs and is destroyed; the page publishes no artifact or cache retention window
- egress: no egress charge is published: the page says it bills per-second compute with no per-developer fee, no cache charges and no egress surprises | metered: no
- identity: email | detail: an email address and a GitHub account to connect a repository: the homepage states "No credit card required · 3,000 free minutes", and no signup was performed
- interface: git
- limits:
  - request-rate (binding): 3,000 Linux minutes a month on the free plan [1]
  - request-rate (binding): USD 0.0040 a minute for the 2 vCPU Linux x64 runner, USD 0.0032 for ARM64, USD 0.0900 for an L4 GPU runner [1]
  - request-rate (binding): per-second billing with a one-minute minimum, so a 20-second job is billed as a full minute [1]
- limits note: no concurrency cap, queue charge, cache charge or egress charge is published; the free pool is Linux only and every runner family is available on the paid meter
- binding note: 3,000 minutes is the first thing to fail: on a 2 vCPU runner it is 50 hours of wall-clock time a month, and nothing else on the free plan is capped.
- interface detail: a GitHub Actions workflow points its runs-on label at a RunnerHut runner; the homepage calls them drop-in runners and says there is no agent to install
- tooling: a one-line change to an existing GitHub Actions workflow; no agent, CLI or self-hosted runner is needed
- composes with: GitHub Actions on a public repository stays free and comes first; RunnerHut buys private-repository minutes at USD 0.0040 for 2 vCPU against GitHub list price of USD 0.0060, and the 3,000 free minutes cover a small private pipeline before any card is needed
- reliability: the page publishes no job wall clock, no concurrency cap and no queue limit; per-second billing with a one-minute minimum rounds a short job up to a full minute
- notes: A hosted GitHub Actions runner with a free pool large enough for a small private pipeline: 3,000 Linux minutes a month, no cache charge and no egress charge. The rates undercut GitHub list price on every family the page lists, and the one-minute minimum is the only rounding. The free pool is Linux only, and the runners are EU-hosted with data residency in six regions.
- evidence note: The free pool, the five runner rates and the billing granularity are read from the vendor own pricing page, and the no-card and drop-in claims from its homepage. Raise by running one job on the free plan and reading the minute counter and the first invoice line.
- evidence:
  - [1] 2026-11-10: the free plan is 3,000 Linux minutes a month with unlimited cache | capture: sha256:aa23425588cf89ddc6c343f85aeeabe26ec367de3d97fdcf6c709a1ff83b809a | quote: 3,000 Linux minutes a month. Everything included
  - [1] 2026-11-10: prices are per minute for the 2 vCPU tier and scale linearly with size | capture: sha256:aa23425588cf89ddc6c343f85aeeabe26ec367de3d97fdcf6c709a1ff83b809a | quote: Prices are per minute for the 2 vCPU tier and scale linearly with size.
  - [1] 2026-11-10: cache is unlimited and no retention window is stated | capture: sha256:aa23425588cf89ddc6c343f85aeeabe26ec367de3d97fdcf6c709a1ff83b809a | quote: Unlimited cache
  - [1] 2026-11-10: no egress charge is published | capture: sha256:aa23425588cf89ddc6c343f85aeeabe26ec367de3d97fdcf6c709a1ff83b809a | quote: No per-developer fee, no cache charges, no egress surprises.
  - [2] 2026-11-10: a workflow targets the runners by changing one line | capture: sha256:17ebf4716a6100de57ef86cab4fea0dd4de16d8ed4e67114d8d85be5c5cce903 | quote: Change one line in your workflow.
  - [2] 2026-11-10: the runners are drop-in and need no agent | capture: sha256:17ebf4716a6100de57ef86cab4fea0dd4de16d8ed4e67114d8d85be5c5cce903 | quote: There is no agent to install
  - [1] 2026-11-10: the 2 vCPU Linux rate is USD 0.0040 a minute against GitHub list price of USD 0.0060 | capture: sha256:aa23425588cf89ddc6c343f85aeeabe26ec367de3d97fdcf6c709a1ff83b809a | quote: | Linux x64 | $0.0040 | $0.0060 | 33% |
  - [1] 2026-11-10: per-second billing with a one-minute minimum | capture: sha256:aa23425588cf89ddc6c343f85aeeabe26ec367de3d97fdcf6c709a1ff83b809a | quote: Per-second billing with a one-minute minimum.
  - [1] 2026-11-10: the free pool is Linux minutes | capture: sha256:aa23425588cf89ddc6c343f85aeeabe26ec367de3d97fdcf6c709a1ff83b809a | quote: 3,000 Linux minutes a month. Everything included
  - [2] 2026-11-10: no credit card is required for the free minutes | capture: sha256:17ebf4716a6100de57ef86cab4fea0dd4de16d8ed4e67114d8d85be5c5cce903 | quote: No credit card required · 3,000 free minutes
- sources:
  - [1] https://runnerhut.com/pricing
  - [2] https://runnerhut.com/
