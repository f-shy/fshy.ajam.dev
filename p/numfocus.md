# NumFOCUS Small Development

> numfocus.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/numfocus/ | JSON https://fshy.ajam.dev/api/v1/entity/numfocus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NumFOCUS Small Development

- `compute/numfocus-small-development` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://numfocus.org/programs/small-development-grants
- free tier: 'Up to $10,000 can be awarded for each proposal'. Eligibility: 'Any NumFOCUS Fiscally Sponsored or Affiliated project is eligible to submit 1 proposal per grant cycle. Each project may receive a maximum of 2 grants per calendar year', and 'Proposals may be submitted by residents of any country'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: cash-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The applicant must be an existing NumFOCUS fiscally sponsored or affiliated project before the grant exists, which is the whole gate; a person with a useful repository and no affiliation cannot submit. [1]
- limits note: The applicant must be an existing NumFOCUS fiscally sponsored or affiliated project before the grant exists, which is the whole gate; a person with a useful repository and no affiliation cannot submit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Suitable for scientific-computing tools: affiliated projects can receive grants of USD 10,000 up to three times a year to fund compute infrastructure.
- reliability: no reliability event recorded
- notes: The honest alternative is the same money via NLnet, MOSS or the Google patch tiers, none of which need an affiliation. The October 17 2026 deadline has passed two cycles into the year, so even an affiliated applicant is looking at 2027.
- extras:
  - facets.class: grant-project-affiliated
  - facets.free_tier_kind: cash-grant
- evidence:
  - [1] 2026-10-22: quoted the USD 10,000 ceiling, the affiliation eligibility sentence, the any-country sentence, the three cycles per year, and the 2026 deadlines of June 6 and October 17
  - [2] 2026-10-22: quoted 'Eligibility is limited to our fiscally sponsored and affiliated projects, and calls for proposals are run 3 times per year'
- sources:
  - [1] https://numfocus.org/programs/small-development-grants
  - [2] https://numfocus.org/projects-overview
