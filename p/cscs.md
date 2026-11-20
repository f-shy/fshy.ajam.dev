# CSCS Small

> cscs.ch | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cscs/ | JSON https://fshy.ajam.dev/api/v1/entity/cscs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CSCS Small

- `compute/cscs-small` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.cscs.ch/user-lab/allocation-schemes/small-projects
- free tier: "Small projects may request up to 8'000 node hours on Alps. Such projects may not exceed the granted allocation and are limited to a one-year duration." A Preparatory Project is the entry step and "is allocated a total of 250 node hours over 3 months on the HPC vCluster on Alps". Small proposals are assessed by technical evaluation only, with acceptance "within two months from submission", and no fixed deadline. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: continuous-small-allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): "Small projects are intended for applicants from the Swiss user community" and every proposer "must hold at least a postdoctoral position at an academic institution", so the 8,000 Alps node-hours need a Swiss academic appointment before any technical review begins. [1]
- limits note: "Small projects are intended for applicants from the Swiss user community" and every proposer "must hold at least a postdoctoral position at an academic institution", so the 8,000 Alps node-hours need a Swiss academic appointment before any technical review begins.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The quarterly reset is what makes this record useful beyond a simple rejection: a 8,000 node-hour annual allocation arrives in three-month windows and expires unused, so a workload that needs a continuous month of GPU time does not fit the shape even inside the institution.
- reliability: no reliability event recorded
- notes: A node on Alps is a GH200 Grace Hopper node (one node-hour corresponds to one GH200 hour rather than one core-hour).
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: continuous-small-allocation
  - facets.shape.gpu_class: NVIDIA GH200 (Alps)
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: "Small projects may request up to 8'000 node hours on Alps"; "limited to a one-year duration"; "A maximum of five accounts is allowed per small project", quoted
  - [1] 2026-10-22: "Small projects are intended for applicants from the Swiss user community"; "Proposers must hold at least a postdoctoral position at an academic institution. PhD students cannot apply independently", quoted
  - [2] 2026-10-22: "Preparatory Projects are allocated a total of 250 node hours over 3 months on the HPC vCluster on Alps", quoted
  - [3] 2026-10-22: "resources at CSCS are assigned over three-months windows"; unused resources "are forever lost", quoted
  - [4] 2026-10-22: "International applications (and collaborations) will be accepted only if proposers and their teams are affiliated with academic institutions", quoted
- sources:
  - [1] https://www.cscs.ch/user-lab/allocation-schemes/small-projects
  - [2] https://www.cscs.ch/user-lab/allocation-schemes/preparatory-projects
  - [3] https://docs.cscs.ch/policies/
  - [4] https://www.cscs.ch/user-lab/allocation-schemes/production-projects
