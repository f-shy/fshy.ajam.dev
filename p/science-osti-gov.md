# ALCC

> science.osti.gov | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/science-osti-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/science-osti-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ALCC

- `compute/alcc` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://science.osti.gov/ascr/Facilities/Accessing-ASCR-Facilities/ALCC/Call-for-Proposals
- free tier: ALCC allocates 10% to 30% of the allocatable time on Frontier, Aurora, Polaris and Perlmutter, which for the 2026-2027 cycle is published as 20,000,000 node-hours on Frontier and 16,000,000 node-hours on Aurora, with awards of one year extendable to three by renewal and proposals due 26 January 2026. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: merit-reviewed allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Available to researchers from universities, industry and government agencies with no DOE sponsorship required, but every participating institution must sign the ASCR facility user agreement, and the award is capped below INCITE size unless the request serves a DOE mission or national emergency. [1]
- limits note: Available to researchers from universities, industry and government agencies with no DOE sponsorship required, but every participating institution must sign the ASCR facility user agreement, and the award is capped below INCITE size unless the request serves a DOE mission or national emergency.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: ALCC is the second rung of the DOE ladder above Director's Discretionary and below INCITE, and it is the only DOE programme that explicitly requires a DOE-mission or national-emergency rationale, which is why it is the harder sell for a general data-science workload.
- reliability: no reliability event recorded
- notes: The largest absolute published pool in evaluated benchmarks: 37 million node-hours across Frontier and Aurora for one cycle, with roughly 120,000 to 160,000 GPU-hours per 15,000 to 20,000 Frontier node-hours at 8 GCDs each. Those totals are the programme pool, not a single award: the page says award size is 'Small-medium' and never states the per-project maximum, so a per-award figure would be invented. ALCC is the natural comparison for INCITE because both use the same machines and the same technical assessment, and the difference is the mission justification rather than the identity cost.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: merit-reviewed allocation
  - facets.shape.gpu_class: AMD MI300A (Frontier), Intel Data Center GPU Max (Aurora), NVIDIA A100 (Perlmutter, Polaris)
- evidence:
  - [1] 2026-10-22: '20,000,000 node-hours on Frontier at Oak Ridge Leadership Computing Facility, 16,000,000 node-hours on Aurora', 1,000,000 node-hours on Polaris, 2,250,000 CPU-node-hours and 1,250,000 GPU-accelerated node-hours on Perlmutter, quoted
  - [1] 2026-10-22: 'Available to researchers from universities, industry, and government agencies. DOE sponsorship is not required'; '10% to 30% of the allocatable computing time will be made available'; proposals due 26 January 2026; decision late May, quoted
  - [1] 2026-10-22: 'proposals seeking very large allocations are more appropriate for the INCITE allocation program. Projects that request more than the maximum request limit will be considered nonresponsive', quoted
  - [1] 2026-10-22: 'Proposals undergo an external peer-review and assessment by computational experts at ALCF, OLCF, and NERSC', quoted
- sources:
  - [1] https://science.osti.gov/ascr/Facilities/Accessing-ASCR-Facilities/ALCC/Call-for-Proposals

## ALCC (ASCR Leadership Computing Challenge)

- `storage/alcc` | fails-quota | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://science.osti.gov/ascr/Facilities/Accessing-ASCR-Facilities/ALCC
- free tier: 10-30% of ALCF/OLCF/NERSC resources each year, with associated project storage (e.g. OLCF 200 TB archive, 50 TB work). | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free to allocation holders. | metered: no
- identity: institution
- interface: ssh
- limits:
  - write-gated (binding): review [1]
- limits note: Requires 'Funded researchers affiliated with a university, lab, agency, or industry' AND a named DOE program manager/sponsor - 'you need to provide the name and email of your program manager/project sponsor... projects that do not have input from the sponsor program will not be competitive'. One-year allocation, renewable up to 3 with annual renewal. Proposals without a recognised funding source are rejected without review.
- interface detail: posix
- tooling: SSH, Globus, Lustre/HPSS.
- composes with: Larger per-project storage than most grants, but gated behind a DOE-relevant compute case.
- reliability: Effectively closed to an unaffiliated individual: two independent institutional gates (employer + DOE sponsor).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10-30% of ALCF/OLCF/NERSC resources each year, with associated project storage (e.g. OLCF 200 TB archive, 50 TB work).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Funded researchers affiliated with a university, lab, agency, or industry'; 'Proposals that lack a PI affiliated with a recognized entity...'; 'ALCC does NOT award any funding'
  - [2] 2026-10-21: 'allocation year runs from July 1 - June 30th... with a possibility of renewal for up to 2 years'
- sources:
  - [1] https://science.osti.gov/ascr/Facilities/Accessing-ASCR-Facilities/ALCC/FAQ-Detail
  - [2] https://science.osti.gov/ascr/Facilities/Accessing-ASCR-Facilities/ALCC
