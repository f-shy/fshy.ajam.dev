# Enterprise

> eis.ee | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eis/ | JSON https://fshy.ajam.dev/api/v1/entity/eis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Enterprise

- `compute/enterprise` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://eis.ee/en/services/start-up-grant/
- free tier: A Start-up Grant of EUR 20,000 at 80 percent support intensity with 20 percent self-financing, for companies under three years old with fewer than 10 employees and turnover at or under EUR 40,000, plus an Innovation and Development Grant of EUR 75,000 to EUR 350,000 covering up to 80 percent of project costs and an Applied Research Grant of up to EUR 2 million. The EUR 20,000 round is closed: 'The budget of the Start-up Grant 5 021 428 has been fulfilled as of 11.08.2026'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): An Estonian registered company is necessary and not sufficient: the e-Residency guidance states 'Fully remote operations with no connections to Estonia (except the fact that the business is incorporated in Estonia) are usually not sufficient for receiving grants', so substance in Estonia is the binding test. [1]
- limits note: An Estonian registered company is necessary and not sufficient: the e-Residency guidance states 'Fully remote operations with no connections to Estonia (except the fact that the business is incorporated in Estonia) are usually not sufficient for receiving grants', so substance in Estonia is the binding test.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the chain evaluated providers was looking for and it fails at the last step: e-Residency gives a non-resident a 100 percent-owned Estonian company without travel, the company clears the incorporation test, and then the substance rule asks for Estonian payroll, tax or R&D presence, which is the same relocation cost Hub71 charges in a different currency. The EUR 75,000 to EUR 350,000 development grant has no published closure and is the larger target once substance exists.
- reliability: no reliability event recorded
- notes: The 5,000 euro tranche paid only at project end is a cash-flow fact that changes the usable value: the founder must fund the work before the final fifth arrives. e-Residency alone does not make the grants reachable: the e-Residency programme's own page is unusually candid that incorporation alone is not enough. The Start-up Grant is closed: the budget was fulfilled on 11 August 2026 and applications closed 14 August 2026. The Innovation and Development Grant publishes its size with no closure notice, and the substance rule is general to EIS grants. Only its article on amount and intensity was read.
- extras:
  - facets.class: government-grant
  - facets.free_tier_kind: grant
- evidence:
  - [1] 2026-10-22: 'Maximum grant 20 000', 'Self-financing 20%', and 'The budget of the Start-up Grant 5 021 428 has been fulfilled as of 11.08.2026. We closed the acceptance of applications on 14.08.2026', quoted
  - [1] 2026-10-22: 'For starting entrepreneurs (companies up to 3 years old)'; 'the company employs fewer than 10 people under employment contracts'; 'The turnover in the financial year immediately preceding the year of application was EUR40,000 or less', quoted
  - [2] 2026-10-22: 'Fully remote operations with no connections to Estonia (except the fact that the business is incorporated in Estonia) are usually not sufficient for receiving grants for startups', quoted
  - [2] 2026-10-22: 'Innovation and Development Grant - EUR 75,000-EUR 350,000, covering up to 80% of project costs for R&D, prototyping, testing, and certification'; 'Applied Research Grant - Up to EUR 2M', quoted
  - [3] 2026-10-22: 'The amount of the support per project is 20,000 euros'; 'The intensity of the support is 80 per cent of the eligible costs', quoted from the grant regulation
  - [4] 2026-10-22: 'Most of the support, 15,000 euros, is paid after the funding decision and the creation of a job, while ... 5,000 euros is paid at the end of the project', reported by a third party
- sources:
  - [1] https://eis.ee/en/services/start-up-grant/
  - [2] https://www.e-resident.gov.ee/blog/posts/funding-and-grants-for-startups/
  - [3] https://eis.ee/wp-content/uploads/2026/02/grant_regulation-1.pdf
  - [4] https://visitek.ee/en/business-plans/new-start-up-grant-round-opens-as-starditoetus-ee-helps-applicants-assess-readiness/
