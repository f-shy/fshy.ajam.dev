# PSC Neocortex

> psc.edu | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/psc-edu/ | JSON https://fshy.ajam.dev/api/v1/entity/psc-edu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PSC Neocortex

- `compute/psc-neocortex` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.psc.edu/resources/neocortex/allocations/
- free tier: Free wafer-scale accelerator time on Cerebras CS-3 systems, allocated through the NSF ACCESS programme: 'There is no cost to use Neocortex for non-proprietary research.' Eligibility is explicit and institutional: 'Projects must be non-proprietary. Applicants must be a researcher or educator at a US academic or non-profit research institution. A principal investigator (PI) is required. PIs may not be a high school, undergraduate or graduate student; a qualified advisor must serve in this capacity.' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): a PI at a US academic or non-profit institution plus a reviewed ACCESS allocation request, so identity fails before any quota does. [1]
- limits note: a PI at a US academic or non-profit institution plus a reviewed ACCESS allocation request, so identity fails before any quota does.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The allocation is the only route to a CS-3 that does not involve a purchase, and it chains with publishing the result. It breaks at the PI requirement, which no amount of preparation substitutes for.
- reliability: no reliability event recorded
- notes: Neocortex at Pittsburgh Supercomputing Center provides access to Cerebras CS-3 systems via ACCESS allocation requests. Allocations require academic peer-review approval.
- extras:
  - facets.class: national-programme
  - facets.free_tier_kind: allocation
  - facets.shape.gpu_class: Cerebras CS-3 wafer-scale engine, 2 nodes
  - facets.shape.gpu_count: 2
- evidence:
  - [1] 2026-10-22: 'Applicants must be a researcher or educator at a US academic or non-profit research institution. A principal investigator (PI) is required. PIs may not be a high school, undergraduate or graduate student', quoted
  - [2] 2026-10-22: 'There is no cost to use Neocortex for non-proprietary research', quoted, with proprietary work routed to a Corporate Affiliates programme
  - [3] 2026-10-22: the same accelerator appears at Argonne as a Cerebras CS-3 with 24 nodes, 'Available through an allocation request'
- sources:
  - [1] https://www.psc.edu/resources/neocortex/allocations/
  - [2] https://www.psc.edu/resources/neocortex/
  - [3] https://www.alcf.anl.gov/alcf-ai-testbed
