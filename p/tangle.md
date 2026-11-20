# Tangle Sandbox

> tangle.tools | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tangle/ | JSON https://fshy.ajam.dev/api/v1/entity/tangle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tangle Sandbox

- `compute/tangle-sandbox` | paid-only | evidence reported | binding volume-quota | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://sandbox.tangle.tools/pricing
- free tier: No free tier and no free credit: the vendor's own plans data says 'Sandbox has no free tier or free credit.' The entry plan is USD 0 a month with usage paid from prepaid credit, one concurrent sandbox, three snapshots per sandbox and 100 GiB of egress a month that is refused past the allowance and never charged. Usage is USD 0.0104 per allocated vCPU-hour and USD 0.0071 per GiB-hour of memory, billed per second with a USD 0.04 minimum charge. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the provider card records the plans API text 'Sandbox has no free tier or free credit.' and '100 GiB egress per account each month, refused beyond it, never charged', plus USD 0.010445613415710504 per vCPU-hour and a USD 0.04 minimum charge | metered: no | source: [2]
- identity: email | detail: self-serve signup for a prepaid account; the vendor documents no further gate
- interface: rest, cli
- limits:
  - volume-quota (binding): the entry plan refuses egress beyond 100 GiB a month and allows one concurrent sandbox, so a second parallel job waits rather than bills [1]
- limits note: the entry plan refuses egress beyond 100 GiB a month and allows one concurrent sandbox, so a second parallel job waits rather than bills
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: an SDK published as @tangle-network/sandbox with a CLI, driving shells, ports, desktop and trace
- composes with: a prepaid balance plus one concurrent sandbox makes this a single-job lane; parallelism needs a paid plan rather than more credit
- reliability: no reliability event recorded
- notes: the per-vCPU-hour figure is derived from a provider card rather than read on the vendor page; the open question is whether a stopped sandbox's disk is still billed
- extras:
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: the page returned a JavaScript shell with no price table when read on 2026-10-22, so no figure here is first-party from that fetch
  - [2] 2026-10-22: the provider card records the plans API text 'Sandbox has no free tier or free credit.' and '100 GiB egress per account each month, refused beyond it, never charged', plus USD 0.010445613415710504 per vCPU-hour and a USD 0.04 minimum charge
- sources:
  - [1] https://sandbox.tangle.tools/pricing
  - [2] https://github.com/ariana-dot-dev/battleships
