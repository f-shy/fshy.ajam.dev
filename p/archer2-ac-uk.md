# ARCHER2 Pump Priming

> archer2.ac.uk | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archer2-ac-uk/ | JSON https://fshy.ajam.dev/api/v1/entity/archer2-ac-uk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ARCHER2 Pump Priming

- `compute/archer2-pump-priming` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T15:03:32.751Z (live) | stale on 2026-12-26
- url https://www.archer2.ac.uk/support-access/access
- free tier: The access page describes Pump Priming in the past tense: it awarded at most 4,000 CU for six months through a form sent to the service desk, with a decision usually in under two weeks, and a starter allocation of 800 CU, GPU nodes included, for new users; Director's Time for University of Edinburgh researchers is listed as Closed. | unit: users | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: exploratory / pump-priming allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Pump Priming is open only to researchers within the EPSRC remit, meaning eligibility for UKRI EPSRC funding and a UK research organisation, so the form is light but the applicant still needs a UK institutional base. [1]
- limits note: Pump Priming is open only to researchers within the EPSRC remit, meaning eligibility for UKRI EPSRC funding and a UK research organisation, so the form is light but the applicant still needs a UK institutional base.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The Driving Test gets a new user onto the GPU nodes for 800 CU, and Pump Priming then carries the same code to 4,000 CU, so the two compose into a single ramp inside one national system.
- reliability: no reliability event recorded
- notes: The always-open, form-only structure makes this the closest UK analogue to the trial tiers found in Germany and the US, and the sub-two-week decision is faster than any peer-reviewed call in evaluated benchmarks. The binding term is 'EPSRC remit', which is a funding-eligibility test rather than a nationality test, but it still resolves to a UK research organisation. CU means CPU-hour equivalent on ARCHER2 and is not a GPU-hour unit, so no conversion is offered.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: exploratory / pump-priming allocation
  - facets.shape.gpu_class: AMD MI210 (4 GPU nodes, 8 GPUs each)
- evidence:
  - [1] 2026-10-22: Pump-priming row: 'Always open', 'EPSRC remit only. Small amounts of time for testing and porting. Quick decision on access. Maximum of 4000 CU for 6 months', quoted
  - [1] 2026-10-22: 'We expect decisions to be made in less than 2 weeks (and usually much sooner). A maximum of 4000 CU for 6 months are currently available through Pump Priming', quoted
  - [1] 2026-10-22: 'A small allocation (800 CU) for new ARCHER2 users to get them started using the ARCHER2 Service ... Includes access to GPU nodes', quoted
  - [1] 2026-10-22: 'Director's Time ... Small amount of resource is available for University of Edinburgh researchers only', quoted
  - [1] 2026-11-25: the access page states a former maximum of 4000 CU for 6 months through Pump Priming | capture: sha256:86de1e55e688b53864b9a25fba21f2b113937a5cbd5054c63c7ea318832c2fcb | quote: A maximum of 4000 CU for 6 months were available through Pump Priming.
  - [1] 2026-11-25: the access page still states a former maximum of 4000 CU for 6 months through Pump Priming | capture: sha256:86de1e55e688b53864b9a25fba21f2b113937a5cbd5054c63c7ea318832c2fcb | quote: A maximum of 4000 CU for 6 months were available through Pump Priming.
  - [1] 2026-11-25: Pump Priming is described in the past tense, with a maximum of 4,000 CU for six months | capture: sha256:86de1e55e688b53864b9a25fba21f2b113937a5cbd5054c63c7ea318832c2fcb | quote: A maximum of 4000 CU for 6 months were available through Pump Priming.
- sources:
  - [1] https://www.archer2.ac.uk/support-access/access
