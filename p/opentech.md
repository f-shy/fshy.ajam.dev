# Open Technology Fund

> opentech.fund | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opentech/ | JSON https://fshy.ajam.dev/api/v1/entity/opentech.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Open Technology Fund

- `compute/open-technology-fund` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.opentech.fund/funds/internet-freedom-fund/
- free tier: 'Awards are between $10,000 and $900,000 for up to 24 months. Ideal applicants seek funding between $50,000 and $200,000 for efforts between 6 and 12 months.' And the sentence that makes it an individual lane: 'Funding awards are performance-based contracts signed directly with the applicant or applicants.' Applications are 'accepted on a rolling basis'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: cash-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - write-gated (binding): A two-stage written application and a program-manager review come before any contract, so there is no capacity until a proposal is accepted, but there is no fixed deadline. [1]
- limits note: A two-stage written application and a program-manager review come before any contract, so there is no capacity until a proposal is accepted, but there is no fixed deadline.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 50,000 is 50,000 hours at USD 1 an hour or 5,000 hours at USD 10 an hour, and the contract pays on deliverables rather than reimbursing receipts, so an accelerator can be rented month by month inside the grant period.
- reliability: no reliability event recorded
- notes: Scope is the gate, not the money: the work must serve internet-freedom users facing censorship or surveillance, so a data-science project qualifies only if that population uses it. The FOSS Sustainability Fund, the closest fit for plain maintenance work, is closed and was last run with GitHub contributing; its eligibility sentence is the clearest first-party statement that OTF contracts individuals.
- extras:
  - facets.class: grant-individual
  - facets.free_tier_kind: cash-grant
- evidence:
  - [1] 2026-10-22: quoted the USD 10,000 to USD 900,000 range, the 24-month ceiling, the rolling intake, and 'contracts signed directly with the applicant or applicants'
  - [2] 2026-10-22: quoted 'Individuals or organizations (for-profit or nonprofit) ages 18 or older - irrespective of nationality, creed, or sex - are encouraged to apply'; that fund states 'Not currently accepting applications'
  - [3] 2026-10-22: the live fund list: Internet Freedom Fund, Rapid Response Fund, Surge and Sustain Fund, FOSS Sustainability Fund, all behind one 'Apply for Support' entry
  - [4] 2026-10-22: the application portal answered HTTP 200 with an open form, so is live rather than archived
- sources:
  - [1] https://www.opentech.fund/funds/internet-freedom-fund/
  - [2] https://www.opentech.fund/funds/free-and-open-source-software-sustainability-fund/
  - [3] https://www.opentech.fund/
  - [4] https://apply.opentech.fund/
