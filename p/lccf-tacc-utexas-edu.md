# LCCF Horizon Leadership

> lccf.tacc.utexas.edu | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lccf-tacc-utexas-edu/ | JSON https://fshy.ajam.dev/api/v1/entity/lccf-tacc-utexas-edu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LCCF Horizon Leadership

- `compute/lccf-horizon-leadership` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://lccf.tacc.utexas.edu/allocations/
- free tier: Large allocations from 125,000 to 500,000 SUs on Horizon and up to 50,000 SUs on Vista for six months, with submissions opening 15 April 2026 and rolling review from 15 May 2026, on a system carrying 4,750 Vera CPU nodes and 2,000 Grace-Blackwell GPU nodes. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: merit-reviewed allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Horizon is open to US researchers working in open research and the PI is typically faculty or a research scientist at a US academic institution; the page also requires current peer-reviewed research funding to support the allocated work. [1]
- limits note: Horizon is open to US researchers working in open research and the PI is typically faculty or a research scientist at a US academic institution; the page also requires current peer-reviewed research funding to support the allocated work.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The non-US route is as a collaborator with substantive intellectual participation by the US partner, which is the same shape as the ACCESS escape hatch and equally dependent on a US collaborator existing.
- reliability: no reliability event recorded
- notes: The largest US number found after INCITE: 500,000 SUs on the newest NSF leadership system. SUs are a site-defined service unit, not GPU-hours or core-hours, so converting them would be invention. Classified as a refutation of the idea that the newest NSF hardware is open to anyone: it requires a US base and existing peer-reviewed funding.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: merit-reviewed allocation
  - facets.shape.gpu_class: NVIDIA Grace-Blackwell
- evidence:
  - [1] 2026-10-22: 'Large allocations from 125,000 to 500,000 SUs (Horizon) and up to 50,000 (Vista) for six months duration'; 'must demonstrate readiness ... as well as current peer-reviewed research funding', quoted
  - [1] 2026-10-22: 'Horizon is broadly available to any U.S. researcher working in open research'; 'Collaborative projects involving non-U.S. researchers are allowed provided they include substantive intellectual participation by the U.S. researchers', quoted
  - [1] 2026-10-22: system composition '4,750 Dell/NVIDIA Vera CPU nodes, and 2,000 Dell/NVIDIA Grace-Blackwell nodes'; submissions 15 April 2026 to 15 June 2026
- sources:
  - [1] https://lccf.tacc.utexas.edu/allocations/
