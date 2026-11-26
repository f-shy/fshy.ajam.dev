# GEANT Testbeds Service

> geant.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/geant/ | JSON https://fshy.ajam.dev/api/v1/entity/geant.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GEANT Testbeds Service

- `compute/geant-testbeds-service` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://connect.geant.org/2020/04/21/amidst-the-covid-19-pandemic-do-you-miss-your-office-and-test-lab-environment-let-the-geant-testbeds-service-gts-help
- free tier: "GTS is currently available to researchers from the European network research community with an endorsement from their local NREN". Quoted on cost: "There are no costs, but there are quotas in place on how many resources you can use." | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): No cost, but entry needs an endorsement from a national research and education network plus a project description, and quotas are set by the operator, so a person with no NREN affiliation cannot request a VM. [1]
- limits note: No cost, but entry needs an endorsement from a national research and education network plus a project description, and quotas are set by the operator, so a person with no NREN affiliation cannot request a VM.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing for an unaffiliated individual. For someone with an NREN endorsement it would be free multi-node testbed compute, which the free public clouds do not offer at any price.
- reliability: no reliability event recorded
- notes: The GTS page read is dated 2020, so its current status is uncertain: the successor described on clouds.geant.org is a deploy-it-yourself platform for NRENs rather than a service that individuals request.
- extras:
  - facets.class: refutation-identity-gated
  - facets.free_tier_kind: grant
- evidence:
  - [1] 2026-10-22: FAQ states GTS is for researchers with an endorsement from their local NREN and that there are no costs but there are quotas, quoted
  - [2] 2026-10-22: the current GEANT community cloud product is software that NRENs and institutions deploy on their own infrastructure, with access through eduGAIN, so an individual cannot join directly
- sources:
  - [1] https://connect.geant.org/2020/04/21/amidst-the-covid-19-pandemic-do-you-miss-your-office-and-test-lab-environment-let-the-geant-testbeds-service-gts-help
  - [2] https://clouds.geant.org/news/community-cloud/
