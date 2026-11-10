# True Digital Park

> truedigitalpark.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/truedigitalpark/ | JSON https://fshy.ajam.dev/api/v1/entity/truedigitalpark.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## True Digital Park

- `compute/true-digital-park` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-30T11:09:07.777Z (live) | stale on 2026-11-30
- url https://www.truedigitalpark.com/startup-support/tdpk-startup-booster
- free tier: USD 25,000 of Google Cloud credit for verified startups, a benefit of the THB 100,000 Global Startup Program package; the page states no period for the credit: "Free 25,000USD Google Cloud Credits for verified startups." | unit: credits | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: paid-incubator-package
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: a registered Thai company plus a capital test, before any payment: the joining checklist requires "Registered company in Thailand in targeted industries", "Hold at least 25% share of the company" and "Personal Saving in Bank Account exceeding 600k Baht", and the package itself is THB 100,000, "less than $3,000", so the fee is the smallest of the three costs; the USD 25,000 of Google Cloud credits is listed as a benefit for "verified startups". The record does not state the payment rail for the THB 100,000, any hold, or debit or prepaid acceptance
- interface: rest
- limits:
  - write-gated (binding): The joining checklist requires 'Registered company in Thailand in targeted industries', 'Hold at least 25% share of the company' and 'Personal Saving in Bank Account exceeding 600k Baht', so the THB 100,000 fee is the smallest of three costs and the credit is only for 'verified startups'. [1]
- limits note: The joining checklist requires 'Registered company in Thailand in targeted industries', 'Hold at least 25% share of the company' and 'Personal Saving in Bank Account exceeding 600k Baht', so the THB 100,000 fee is the smallest of three costs and the credit is only for 'verified startups'.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the cleanest chain among documented hosts: THB 100,000 buys the Thai company registration and the two-year visa that the Google credit requires, so the package converts a visa problem into a procurement problem. It composes with Google's own startup tiers because the credit lands on a billing account the founder controls, and it breaks if the 600,000 baht balance cannot be shown, which is roughly USD 18,000 parked in a bank.
- reliability: no reliability event recorded
- notes: THB 100,000 does not buy the credits: they are listed as a package benefit 'for verified startups' and verification is a separate step. Whether the fee is annual is unresolved: the page says '1 Year co-working space' and '2-Year' visa without stating a renewal price. The USD 25,000 is plausibly Google's standard startup tier rather than a True Digital Park grant, because Google's own Start tier is USD 2,000 and its Scale tier USD 100,000, so USD 25,000 sits between them and may be a partner-negotiated figure; the Google page was not read. The 25 percent shareholding rule is what stops a founder holding the company entirely through a nominee, and the 600,000 baht savings rule is a capital test rather than an identity test.
- extras:
  - facets.class: incubator-package
  - facets.free_tier_kind: paid-incubator-package
  - facets.shape.gpu_class: provider-dependent (Google Cloud)
- evidence:
  - [1] 2026-10-22: 'Individual Package for an entrepreneur or anyone whose company has registered in Thailand : THB 100,000 (It's less than $3,000)'; 'Free 25,000USD Google Cloud Credits for verified startups', quoted
  - [1] 2026-10-22: '2-Year smart S visa (No work Permit Required)'; '1 Year co-working space at True Digital Park and True Space in 6 Locations', quoted
  - [1] 2026-10-22: Joining checklist: 'Technology-based startup', 'Hold at least 25% share of the company', 'Registered company in Thailand in targeted industries', 'Personal Saving in Bank Account exceeding 600k Baht (Any Bank and any currency)', quoted
  - [2] 2026-10-22: the same package is repeated on the business-service page, which also names True Digital Park as an ecosystem partner in the Google for Startups Cloud Program
  - [1] 2026-10-30: the package lists USD 25,000 of Google Cloud credits for verified startups, with no period stated | capture: sha256:4f62003219be1c0636cd4b497490e666fe4b139b1bd0bb8a1dfdaa241fedab96 | quote: Free 25,000USD Google Cloud Credits for verified startups.
- sources:
  - [1] https://www.truedigitalpark.com/startup-support/tdpk-startup-booster
  - [2] https://www.truedigitalpark.com/business-service/global-startup-program
