# AI Singapore

> aisingapore.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aisingapore/ | JSON https://fshy.ajam.dev/api/v1/entity/aisingapore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AI Singapore

- `compute/ai-singapore` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://aisingapore.org/innovation/100e/
- free tier: Co-funding of up to SGD 150,000 per project, with a dedicated AI Engineering Hub of full-time AI, data and platform engineers building and deploying an AI minimum viable product over 6 months; a newer 100E 3-month proof-of-concept path runs with 2 to 3 AI engineers. Organisations must match the funding with in-kind manpower and cash. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: co-funding
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The award is co-funding against a Singapore organisation's own cash and manpower contribution, delivered by an AI Singapore engineering team, so an applicant has to be an established organisation with staff to second and money to match. [1]
- limits note: The award is co-funding against a Singapore organisation's own cash and manpower contribution, delivered by an AI Singapore engineering team, so an applicant has to be an established organisation with staff to second and money to match.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Because the deliverable is engineers rather than credits, 100E does not compose with a cloud free tier in the usual way: the compute sits inside AI Singapore's own environment, so the only thing taken away is the model and the code, not a billing account.
- reliability: no reliability event recorded
- notes: The SGD 150,000 is a co-funding ceiling, not a grant, and the cash share is invoiced up front against a signed Research Collaboration Agreement, which inverts the cash flow a grant applicant expects.
- extras:
  - facets.class: national-programme
  - facets.free_tier_kind: co-funding
- evidence:
  - [1] 2026-10-22: the 100E programme 'provides co-funding of up to SGD$150,000 per project'; 'Organisations are required to match this funding with in-kind contribution (manpower) and cash', quoted
  - [1] 2026-10-22: the MVP path runs 'over 6 months' with 'a dedicated AI Engineering Hub (AIEH), comprising full-time AI, data, and platform engineers'; the 3-month POC path uses '2 - 3 AI Engineers & Project Manager', quoted
  - [2] 2026-10-22: 'The total cash (including the Indirect Research Costs and GST) to be paid will be invoiced to the organisation upon the endorsement of the Research Collaboration Agreement (RCA) for the project', quoted
- sources:
  - [1] https://aisingapore.org/innovation/100e/
  - [2] https://aisingapore.org/faq/when-is-the-cash-contribution-required/
