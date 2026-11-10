# European Innovation Council

> eic.ec.europa.eu | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eic-ec-europa-eu/ | JSON https://fshy.ajam.dev/api/v1/entity/eic-ec-europa-eu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## European Innovation Council

- `compute/european-innovation-council` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://eic.ec.europa.eu/eic-funding-opportunities/eic-2026-work-programme_en
- free tier: Grants below EUR 2.5 million combined with equity investment from EUR 0.5 million to EUR 10 million, from a EUR 634 million Accelerator budget in the 2026 work programme. The applicant guide states 'For grant only the maximum grant amount you can request is EUR 2 499 999'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Eligibility runs through 'a single company classified as a SME, and established within a Member State or an Associated Country', or through natural persons who intend to establish that SME, because 'Your company must prove its effective establishment in a Member State or an Associated Country at the time of submission of the full proposal'. [1]
- limits note: Eligibility runs through 'a single company classified as a SME, and established within a Member State or an Associated Country', or through natural persons who intend to establish that SME, because 'Your company must prove its effective establishment in a Member State or an Associated Country at the time of submission of the full proposal'.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the one programme among evaluated providers where the identity position is not the obstacle: the natural-person clause lets somebody without a company submit a short proposal, and the incorporation obligation lands only at full-proposal stage. What it composes with is a vendor's GPU lane, because a EUR 2.5 million grant converts a pay-as-you-go training budget into a funded line item rather than a credit balance.
- reliability: no reliability event recorded
- notes: The natural-person route is the only one that survives. A company is not required at submission: the call conditions admit 'natural persons ... intending to establish an SME', and the eic.ec.europa.eu page lists 'Natural persons or legal entities willing to set up an SMEs'. A company is required at full proposal: the applicant 'must prove its effective establishment ... at the time of submission of the full proposal', so the short proposal is the free step and incorporation is the price of the second. Whether a non-associated third-country national is excluded is unresolved: the conditions allow applicants 'from a non-associated third country intending to establish an SME ... or to relocate an existing SME to a Member State', which reads as open but is a relocation commitment. The verdict is qualifies-with-caveat rather than qualifies because the grant is competitive against deep-tech proposals with a published success rate near single digits, and because EUR 2.5 million is an R&D budget that has to be spent against an approved work programme, not a credit balance.
- extras:
  - facets.class: government-grant
  - facets.free_tier_kind: grant
- evidence:
  - [1] 2026-10-22: 'EIC Accelerator (EUR 634 million) for start-ups and SMEs'; 'grants below EUR 2.5 million, investments from EUR 0.5 to EUR 10 million', quoted
  - [2] 2026-10-22: 'For grant only the maximum grant amount you can request is EUR 2 499 999. For blended applications and ONLY in exceptional cases, you may request EUR 2 500 000 or more', quoted
  - [3] 2026-10-22: 'one or more natural persons (including individual entrepreneurs) or legal entities ... from a Member State or an Associated Country intending to establish an SME', and 'Your company must prove its effective establishment in a Member State or an Associated Country at the time of submission of the full proposal', quoted from the call conditions
  - [4] 2026-10-22: eligible applicants are 'Single start-up or SME (including spin-outs)' or 'Natural persons or legal entities willing to set up an SMEs or a mid-cap', quoted
- sources:
  - [1] https://eic.ec.europa.eu/eic-funding-opportunities/eic-2026-work-programme_en
  - [2] https://eic.ec.europa.eu/document/download/9d96fbf3-4d85-4ad0-9483-c77ce348111d_en?filename=EIC+Accelerator+guide+for+applicants_WP26.pdf
  - [3] https://www.euacc.ai/calls/HORIZON-EIC-2026-ACCELERATOR-01
  - [4] https://eic.ec.europa.eu/eic-funding-opportunities/eic-accelerator_en
