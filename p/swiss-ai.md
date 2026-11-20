# Swiss AI Initiative

> swiss-ai.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/swiss-ai/ | JSON https://fshy.ajam.dev/api/v1/entity/swiss-ai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Swiss AI Initiative

- `compute/swiss-ai-initiative` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.swiss-ai.org/compute-grants
- free tier: Small project grants of 'typically ... between 20k and 32k compute hours' for 'a period of six months' on the CSCS Alps infrastructure (over 10,000 GH200 GPUs), plus a large-project call for 'projects requesting more than 500k GPU hours'. The initiative aims to distribute '10-20M GPU hours' across 2026. Eligibility, quoted: 'Every individual or team is eligible to apply as long as at least one team member is employed at a recognized research institution in Switzerland, at a minimum 50% FTE research function as permanent or Professor tenure-track for the whole duration of the project.' The proposal must carry 'signature of at least 1 supporting Swiss PI'. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Swiss research-institution employment at 50% FTE for the project's whole duration plus a co-signing Swiss PI is a condition no outsider can meet, and the application is a signed 2-page PDF. [1]
- limits note: Swiss research-institution employment at 50% FTE for the project's whole duration plus a co-signing Swiss PI is a condition no outsider can meet, and the application is a signed 2-page PDF.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None. The allocation is node-hours on a named national supercomputer, reachable only through the project, so it cannot be combined with a commercial allowance.
- reliability: no reliability event recorded
- notes: The national-HPC class in one record, and the cleanest illustration of why this class is closed: the quota is real and enormous (10-20M GPU hours across 2026, on GH200), and the eligibility sentence is a Swiss employment contract. The Swiss AI Initiative is co-founded by ETH Zurich and EPFL and runs on CSCS Alps. A reader who sees '10-20 million GPU hours' without the eligibility line will plan a year of training; the two belong in one sentence. On promotion, pair it with the same document's line that private companies, NGOs, SMEs and startups 'can not request nor directly access any computing resource', which closes the industry-partner route too.
- extras:
  - facets.class: research-credit
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_class: GH200
- evidence:
  - [1] 2026-10-22: 'For 2026, the 10-20 million GPU hours should be distributed'; 'The large compute call - targeted at projects requesting more than 500k GPU hours - is held twice a year'; 'Call for Small Projects (up to 32k GPU hours), rolling reviews', quoted; page…
  - [2] 2026-10-22: the small-grant call document: 'Every individual or team is eligible to apply as long as at least one team member is employed at a recognized research institution in Switzerland, at a minimum 50% FTE research function as permanent or Professor tenure-track for the whole duration of the project', 'signature of at least 1 supporting Swiss PI', 'Typically, the compute amount requested might be between 20k and 32k compute hours', quoted
  - [2] 2026-10-22: the call also requires 'Provide evidence of experience with GPU multi-GPU/node training', so the gate is an employment contract plus a demonstrated track record, not a proposal alone
- sources:
  - [1] https://www.swiss-ai.org/compute-grants
  - [2] https://docs.google.com/document/d/1o8x3Ow-3kYx0FZXQrXsFwT-rwDqR747wZcZHxQIWXKw/export?format=txt
