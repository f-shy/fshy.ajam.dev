# Mozilla Foundation Human-Scale

> mozillafoundation.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mozillafoundation/ | JSON https://fshy.ajam.dev/api/v1/entity/mozillafoundation.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mozilla Foundation Human-Scale

- `compute/mozilla-foundation-human-scale` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.mozillafoundation.org/en/what-we-do/grantmaking/incubator/human-scale-ai/call-for-proposals/
- free tier: 'Applicants to this cohort will be eligible to receive up to $500,000 USD in funding over three years - without giving up equity.' The base award, quoted: 'Selected projects will receive $300,000 USD and 12 months of intensive support beginning in April 2027', and the follow-on, quoted: 'Projects that demonstrate strong progress may be eligible for up to $200,000 USD in additional funding and two more years of bespoke support'. Deadline, quoted: 'The deadline to apply is Friday, November 20, 2026 at 11:59 p.m. Pacific Standard Time (UTC-8)'. Selection, quoted: 'Applications are reviewed through a multi-stage process. The primary review occurs at the Initial Project Proposal stage, with only a small number of shortlisted applicants invited to submit a full application.' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): a multi-stage competitive review with a small shortlist decides the money, and the payment is a 12 month runway rather than a compute balance, so the award buys capacity only after it is won. [1]
- limits note: a multi-stage competitive review with a small shortlist decides the money, and the payment is a 12 month runway rather than a compute balance, so the award buys capacity only after it is won.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Cash with no equity and no spending restriction, so it composes with every compute record in earlier readings: USD 300,000 at Lambda's documented on-demand rate of USD 3.99 per H100 GPU-hour (compute/lambda) is about 75,000 H100-hours. It is the largest live, entity-agnostic award found among evaluated providers and the only one whose deadline falls after on 2026-10-22.
- reliability: no reliability event recorded
- notes: Eligibility terms address builders, while distribution of USD 300,000 grants typically involves a registered entity.
- extras:
  - facets.class: grant
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: 'Applicants to this cohort will be eligible to receive up to $500,000 USD in funding over three years - without giving up equity'; 'Selected projects will receive $300,000 USD and 12 months of intensive support beginning in April 2027'; 'up to $200,000 USD in additional funding and two more years'; 'The deadline to apply is Friday, November 20, 2026'; 'with only a small number of shortlisted applicants invited to submit a full application'; page 200
  - [2] 2026-10-22: 'It offers seven projects up to $500,000 each over three years. We fund, you build, and you keep ownership.'; 'This cohort is seeded with three teams'; 'Applications for the Human-Scale AI Incubator cohort are open now'; page 200
- sources:
  - [1] https://www.mozillafoundation.org/en/what-we-do/grantmaking/incubator/human-scale-ai/call-for-proposals/
  - [2] https://www.mozillafoundation.org/en/what-we-do/grantmaking/incubator/human-scale-ai/
