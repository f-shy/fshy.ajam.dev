# Yotta Labs Academic

> yottalabs.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yottalabs/ | JSON https://fshy.ajam.dev/api/v1/entity/yottalabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Yotta Labs Academic

- `compute/yotta-labs-academic` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.yottalabs.ai/research-credit
- free tier: '$1000 Credits' plus 'Discounted Compute Usage for 6 Months' and 1-on-1 engineering support. Its eligibility list is the interesting part, because it ends with a lane for people with no institution: after 'Researchers ... From accredited academic or non-profit organizations', 'Faculty Members', and 'Graduate & Postdoctoral Researchers', it lists 'Other Independent Researchers - Anyone conducting their own research projects'. The vendor's own follow-up post repeats the framing: 'If you're an academic or independent researcher working on GPU-intensive AI or data-driven research, we're still actively reviewing applications.' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an email-gated application rather than a signup: the eligibility list names 'Other Independent Researchers' and 'Anyone conducting their own research projects', so an unaffiliated applicant is not excluded, but admission is an editorial review ('we're still actively reviewing applications'), not an automatic grant. Up to USD 1,000 in GPU compute credits plus six months of discounted usage. No card is stated, so no hold and no debit question.
- interface: unknown
- limits:
  - write-gated (binding): the credit is USD 1,000, which at GPU list prices is tens of hours, so the amount and a review cycle bind before any technical limit does. [1]
- limits note: the credit is USD 1,000, which at GPU list prices is tens of hours, so the amount and a review cycle bind before any technical limit does.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Small enough that it composes rather than substitutes: USD 1,000 of GPU time plus six months of discounted pricing is a supplement to a larger allowance, not a base.
- reliability: no reliability event recorded
- notes: The fourth independent-researcher door found, and the smallest: USD 1,000 is roughly tens of GPU-hours, so on its own it funds an experiment rather than a project. The evidence that it pays out is thin and one-sided: the vendor names three sponsorships, all at university labs, so the 'Other Independent Researchers' lane is published but not yet demonstrated.
- extras:
  - facets.class: research-credit
  - facets.free_tier_kind: one-time-credit
- evidence:
  - [1] 2026-10-22: the eligibility list names 'Other Independent Researchers' and 'Anyone conducting their own research projects'; '$1000 Credits'; 'Discounted Compute Usage for 6 Months'; page 200
  - [2] 2026-10-22: 'If you're an academic or independent researcher working on GPU-intensive AI or data-driven research, we're still actively reviewing applications'; 'Up to $1,000 in GPU compute credits'; page 200
  - [2] 2026-10-22: the program is new and small: 'approximately half a dozen qualified inquiries from top academic institutions', and the three named sponsorships are all university labs (UCSD Z-Lab, UC Berkeley, UT Austin VITA Group)
- sources:
  - [1] https://www.yottalabs.ai/research-credit
  - [2] https://www.yottalabs.ai/post/research-credits-update
