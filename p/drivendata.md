# DrivenData

> drivendata.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/drivendata/ | JSON https://fshy.ajam.dev/api/v1/entity/drivendata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DrivenData / DOE

- `compute/drivendata-doe` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.drivendata.org/competitions/306/competition-doe-gems/
- free tier: 'Total Prize Pool: $300,000', split as 'Initial Prize Round - $50,000 Top 5 participants on private test set 1st - 5th Place (each) $10,000' and 'Final Prize Round - $250,000 1st $100,000 2nd $70,000 3rd $40,000 4th $25,000 5th $15,000'. Close date, quoted: 'Dec. 3, 2026, 11:59 p.m. UTC'. Entry route, quoted: 'Click the "Compete!" button in the sidebar on the competition homepage to enroll'. The award is cash, and the official rules supply no compute allowance: the prize is 'presented by the U.S. Department of Energy's Office of Geothermal'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: prize
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: country-phone | country: US
- interface: unknown
- limits:
  - write-gated (binding): nationality decides it before anything else: the official rules require a solo competitor to be a U.S. citizen or permanent resident, so the largest prize on the platform is closed regardless of skill or compute. [1]
- limits note: nationality decides it before anything else: the official rules require a solo competitor to be a U.S. citizen or permanent resident, so the largest prize on the platform is closed regardless of skill or compute.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nil for a non-US entrant. The record's value is the ratio it exposes: the biggest cash prize on a competition platform is gated on nationality rather than on compute, and a reader who sees '$300,000' on the listing page has no way to know that from the listing.
- reliability: no reliability event recorded
- notes: A refutation, not a discovery, but the most useful one: DrivenData is the platform a budget-conscious entrant would try first, and its flagship prize is closed on nationality. Three explanations for the gate were considered, since a domestic-only rule can come from the sponsor, the platform, or the prize's statutory basis. The rules PDF attributes it to the DOE prize programme itself ('Eligibility is subject to verification before prizes are awarded'), and the certification language about 18 U.S.C. 1001 in the DrivenData pre-registration form supports a federal prize rather than a platform policy.
- extras:
  - facets.class: prize
  - facets.free_tier_kind: prize
- evidence:
  - [1] 2026-10-22: 'Total Prize Pool: $300,000'; 'Initial Prize Round - $50,000'; 'Final Prize Round - $250,000 1st $100,000 2nd $70,000 3rd $40,000 4th $25,000 5th $15,000'; 'Dec. 3, 2026, 11:59 p.m. UTC'; page 200
  - [2] 2026-10-22: 'Institutions, companies, nonprofit organizations, and individuals based in the United States (U.S.) are eligible to compete'; 'An individual prize competitor (who is not competing as a member of a group) must be a U.S. citizen or permanent resident'; 'A group of individuals competing as one team may win, provided the designated team captain is a U.S. citizen or permanent resident'; PDF read as text, 200
  - [3] 2026-10-22: the listing shows 'The Geologic Enhanced Mapping System (GEMS) Prize Challenge' at '$300,000 in prizes' with '695 joined', alongside a benchmark and practice competitions with no prize; page 200
- sources:
  - [1] https://www.drivendata.org/competitions/306/competition-doe-gems/
  - [2] https://www.nlr.gov/docs/fy26osti/96647.pdf
  - [3] https://www.drivendata.org/competitions/
