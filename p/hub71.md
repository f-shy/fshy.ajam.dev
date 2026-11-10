# Hub71

> hub71.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hub71/ | JSON https://fshy.ajam.dev/api/v1/entity/hub71.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hub71

- `compute/hub71` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.hub71.com/program/access-programme
- free tier: For the Access Programme: 'AED 250,000 worth of in-kind incentives in the form of support services, and AED 250,000 in cash for exchange for equity through a SAFE note', with a possible 'top-up of up to AED 250,000 in exchange for additional equity', so up to AED 750,000 per startup. The earlier-stage Initiate programme offers a 'Free licence and office space at Hub71 for one year' with no cash stated. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: in-kind-and-equity
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Onboarding requires registering an ADGM tech licence subsidiary in Abu Dhabi, and 'At least one founder is expected to commit to relocating long-term and building a team out of Abu Dhabi', so the cost is incorporation plus physical relocation rather than a fee. [1]
- limits note: Onboarding requires registering an ADGM tech licence subsidiary in Abu Dhabi, and 'At least one founder is expected to commit to relocating long-term and building a team out of Abu Dhabi', so the cost is incorporation plus physical relocation rather than a fee.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The AED 500,000 cash half is equity, not a grant, so the effective free capacity is the AED 250,000 in-kind tranche, which is spent with Hub71's service providers rather than on a cloud bill; that is what limits it as a compute resource even though the headline number is the largest in the MENA slice of evaluated providers.
- reliability: no reliability event recorded
- notes: The prose on two Hub71 pages has drifted apart: a 2023 press release describes 'up to AED 750,000 in cash and in-kind incentives' while the current Access page splits it into two AED 250,000 tranches plus a performance top-up, which happens to sum to the same figure. Whether the in-kind tranche includes cloud credits is unresolved: no page read names a cloud provider, and the ADGM page describes the in-kind as housing, office space and health insurance. The cash tranche is not free money: it is explicitly 'in exchange for equity through a SAFE note'. A foreign founder can plausibly hold 100 percent of the ADGM subsidiary: the FAQ says the entity is a subsidiary of the holding entity 'regardless of the holding entity's location', which is the cheapest incorporation gate among the programmes read, after Malaysia's. The relocation clause is the real cost and it is not priced on any page read.
- extras:
  - facets.class: accelerator-credit
  - facets.free_tier_kind: in-kind-and-equity
- evidence:
  - [1] 2026-10-22: 'AED 250,000 worth of in-kind incentives in the form of support services, and AED 250,000 in cash for exchange for equity through a SAFE note'; 'top-up of up to AED 250,000 in exchange for additional equity', quoted
  - [1] 2026-10-22: 'At least one founder is expected to commit to relocating long-term and building a team out of Abu Dhabi'; Cohort 21 deadline 'February 2027' with the programme starting 'September 2027', quoted
  - [2] 2026-10-22: 'as part of the onboarding process, startups are required to register for an ADGM tech license. The newly formed entity will be set up as a subsidiary of your holding entity, regardless of the holding entity's location', quoted
  - [3] 2026-10-22: 'Free licence and office space at Hub71 for one year'; 'Access to venture builder partner programmes, mentorship and tools', quoted
  - [4] 2026-10-22: the ADGM Tech Startup Licence is 'incentivised for up three years' and the Hub71 Incentive Program 'provides up to 100% subsidies on housing, office space and health insurance for up to 25 employees, for up to three years', quoted
- sources:
  - [1] https://www.hub71.com/program/access-programme
  - [2] https://www.hub71.com/faqs
  - [3] https://www.hub71.com/program/initiate
  - [4] https://www.adgm.com/business-areas/tech-startup
