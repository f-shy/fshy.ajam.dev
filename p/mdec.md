# Malaysia Digital Acceleration

> mdec.my | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mdec/ | JSON https://fshy.ajam.dev/api/v1/entity/mdec.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Malaysia Digital Acceleration

- `compute/malaysia-digital-acceleration` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T08:50:51.587Z (live) | stale on 2026-12-04
- url https://www.mdec.my/grants/mdag-ai
- free tier: Up to RM 2 million in performance-based funding for Malaysia Digital companies that develop and commercialise AI solutions, aimed at the foundation, enabling and application layers, with the 2026 budget carrying an RM 53 million allocation for MDAG. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): The applicant must be 'Incorporated in Malaysia under Companies Act 1965 or the Companies Act 2016' and be, or have a live application for, a Malaysia Digital or MSC Malaysia status company, and the published application window closed on 18 July 2025. [1]
- limits note: The applicant must be 'Incorporated in Malaysia under Companies Act 1965 or the Companies Act 2016' and be, or have a live application for, a Malaysia Digital or MSC Malaysia status company, and the published application window closed on 18 July 2025.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The RM 1,000 minimum paid-up capital for Malaysia Digital status is the cheapest company gate evaluated providers found anywhere: a foreign founder can hold 100 percent of a Malaysian Sendirian Berhad, so unlike the Singapore 30 percent local-equity rule, this door opens with incorporation alone, provided a 2026 cycle reopens.
- reliability: no reliability event recorded
- notes: The grant is probably closed and the page stale: the page carries '18th July 2025' as a deadline while the site now runs 2026 content and the 2026 budget allocates RM 53 million to MDAG, so the allocation and the deadline disagree. It is not closed permanently, given the fresh allocation. Whether it reopened under a different call is unresolved, and the finding is recorded as fails-identity because the company gate binds regardless of the cycle. The RM 2 million is a performance-based ceiling rather than an upfront credit, so the amount a participant actually receives depends on milestone claims, which could not be priced from the pages read.
- extras:
  - facets.class: government-grant
  - facets.free_tier_kind: grant
- evidence:
  - [1] 2026-10-22: 'Fast-track your Artificial Intelligence growth with up to RM 2 million in performance-based funding', quoted
  - [1] 2026-10-22: 'Incorporated in Malaysia under Companies Act 1965 or the Companies Act 2016'; 'must be Malaysia Digital (MD) or MSC Malaysia status company', quoted from Eligibility Criteria
  - [1] 2026-10-22: 'Applications open until 18th July 2025', quoted twice on the page
  - [2] 2026-10-22: 'to be awarded MD Status, a company is required to meet the following criteria: (a) Incorporated under the ... (c) Has a minimum paid up capital of RM1,000.00', quoted from the MD status guidelines
  - [3] 2026-10-22: 'RM 53 million: Malaysia Digital Acceleration Grant (MDAG) by MDEC to accelerate the growth and adoption of new technologies such as blockchain, AI and quantum computing', quoted from the Budget 2026 snapshot
  - [1] 2026-11-03: the page states the application window as open until 18 July 2025 | capture: sha256:0781adaae24f243782553e88357df2eec07fa5ff507feec8ddf68a406b5a00ee | quote: Applications open until 18th July 2025
- sources:
  - [1] https://www.mdec.my/grants/mdag-ai
  - [2] https://www.mdec.my/api/media/file/20260701_GARIS-PANDUAN-STATUS-MD.pdf
  - [3] https://platform.mdec.com.my/cmscdn/v1.aspx?GUID=28b5a527-8d35-4b2d-92b5-1218779acb4a&file=Belanjawan+2026.pdf
