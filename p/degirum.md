# DeGirum AI Hub

> degirum.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/degirum/ | JSON https://fshy.ajam.dev/api/v1/entity/degirum.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DeGirum AI Hub

- `compute/degirum-ai-hub` | dead | evidence documented | binding retention-clamped | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://degirum.com/
- free tier: Withdrawn. The company states: 'Effective August 1, 2026, DeGirum has ceased operations. Its assets have been acquired by LatticeWork... AI Hub is being discontinued in full, including the Pro tier. Pro users get a free grace period of Pro access through September 30, 2026, after which AI Hub will no longer be available publicly. Cloud Compiler is being sunset on September 30, 2026.' The discontinued free plan was '20k AI Hub inferences per month, 1 included user, and 1 local device license', which was the only free cloud lane for running models on several edge accelerators without owning the hardware. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: monthly-inference-allowance
- per-object cap: not applicable | source: [1]
- retention: the allowance did not bind: the service stopped existing on 2026-09-30, which is 22 days before this reading. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - retention-clamped (binding): the allowance did not bind: the service stopped existing on 2026-09-30, which is 22 days before this reading. [1]
- limits note: the allowance did not bind: the service stopped existing on 2026-09-30, which is 22 days before this reading.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: It was the free half of a chain with Hailo's and other vendors' compilers, which produce hardware-specific binaries that the caller cannot execute without the silicon. That chain is now broken at the execution step.
- reliability: no reliability event recorded
- notes: Reopening criteria: relaunch of AI Hub under an active domain.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: monthly-inference-allowance
- evidence:
  - [1] 2026-10-22: 'Effective August 1, 2026, DeGirum has ceased operations' and 'after September 30, 2026 AI Hub will no longer be available publicly', quoted from the live homepage
  - [2] 2026-10-22: the retired plan table: 'Free is for individuals exploring. It includes 20k AI Hub inferences per month, 1 included user, and 1 local device license', quoted
- sources:
  - [1] https://degirum.com/
  - [2] https://docs.degirum.com/ai-hub/workspace-plans
