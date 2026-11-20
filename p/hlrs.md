# HLRS test access

> hlrs.de | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hlrs/ | JSON https://fshy.ajam.dev/api/v1/entity/hlrs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HLRS test access

- `compute/hlrs-test-access` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.hlrs.de/apply-for-computing-time
- free tier: A test account on HLRS systems carries a contingent of 100 Hunter node hours for up to six months, granted on a one to three page application that is explicitly not peer-reviewed; GCS Preparatory Access gives a larger contingent plus HLRS user-support assistance for up to one year. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: exploratory / test allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Test access is offered to potential applicants for GCS Large-Scale and rolling regular projects, which are German national calls for investigators at German research institutions, so the account presumes an eligible German home organisation. [1]
- limits note: Test access is offered to potential applicants for GCS Large-Scale and rolling regular projects, which are German national calls for investigators at German research institutions, so the account presumes an eligible German home organisation.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The un-peer-reviewed test account is the cheapest entry in the German stack, and it exists specifically to generate the scaling data a GCS regular or large-scale proposal needs.
- reliability: no reliability event recorded
- notes: HLRS is the only centre found that states outright that the test application is not peer-reviewed, which makes 100 Hunter node hours the most accessible German allocation; the eligibility section heading still ties it to German research institutions. Hunter carries AMD MI300A APUs, so 100 node hours is a small but real GPU allocation. GCS large-scale thresholds are useful as earlier clearest definition of what 'large' means in core hours versus GPU hours on the same programme.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: exploratory / test allocation
  - facets.shape.gpu_class: AMD MI300A (Hunter), NVIDIA A100 (Hawk)
- evidence:
  - [1] 2026-10-22: 'Within your test account you can consume a resource contingent of 100 Hunter node hours on the granted hardware platforms. The project time is limited to six months'; 'This short proposal will not be peer-reviewed', quoted
  - [1] 2026-10-22: page section heading 'For investigators at German research institutions'; GCS Preparatory Access 'may last a maximum of one year' and provides 'a higher resource contingent than ordinary GCS test projects', quoted
  - [2] 2026-10-22: GCS large-scale threshold 'at least 25,000 node-h on Hunter', '5,250 EFLOP on JUWELS Cluster', '140,000 GPU hours on SuperMUC-NG Phase 2', equal to 2% of each system's annual production, quoted
- sources:
  - [1] https://www.hlrs.de/apply-for-computing-time
  - [2] https://www.gauss-centre.eu/for-users/hpc-access/allocation-pgms
