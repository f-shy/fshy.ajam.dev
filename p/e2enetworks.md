# e2e networks

> e2enetworks.com | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/e2enetworks/ | JSON https://fshy.ajam.dev/api/v1/entity/e2enetworks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## E2E Networks

- `compute/e2e-networks` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.e2enetworks.com/pricing
- price parsed USD 33.65/mo
- free tier: no recurring free tier: GPU resources bill per minute, and the only free path is a trial account with limited resources granted on application | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: institution | detail: the named credits require an incorporated company with 10 or fewer employees; the self-serve route requires an identity document, an address document and up to 3 business days of manual review | country: IN
- interface: unknown
- limits:
  - request-rate: per-minute GPU billing; the trial account's limits are not published [1]
  - retention-clamped: the trial is a limited-resource account granted on request, not a recurring allowance [1]
- binding note: the incorporation test fails first: without a registered company there is no route to the credits, and the self-serve route is a 20-credit bonus behind document review
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: A 20-infra-credit sign-up bonus requires phone OTP, billing details, and identity KYC verification.
- evidence note: the pricing page was read on 2026-10-22 and states per-minute GPU billing plus a trial account rather than a tier. The trial has no published limits, so the verdict is trial-only and the record says the limits are unstated
- extras:
  - keep_rate: 1.0
  - billing_model: flat-pool
  - session_cap.restart_required: no
  - session_cap.note: a trial account with unpublished limits; the paid path bills per minute
  - price_note: a VPS bills by the month with an hourly rate capped at the monthly figure, so the two columns answer two questions: destroying the box between runs versus keeping it up.
  - free_tier_kind: trial
  - m10h_usd: 13.2
  - m24h_usd: 33.65
  - price_basis: 10 h/day column = 300 h at the hourly rate, which is what a server destroyed between runs costs; 24/7 column = the monthly cap, because a VPS kept up all month stops at the cap.
  - burst_x: 1.0484
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'E2E Networks offers transparent, pay-as-you-go billing with per-minute granularity for GPU resources. You are billed only for the resources you use' and 'we offer trials and demonstrations for potential customers. You can sign up for a free trial account to test our services with limited resources', quoted
  - [2] 2026-10-22: the self-serve account FAQ requires 'Copy of any one identity proof document' and 'Copy of any one address proof', with activation that 'may take up to 3 business days'
- sources:
  - [1] https://www.e2enetworks.com/pricing
  - [2] https://www.e2enetworks.com/startup-program

## e2e networks object storage (in)

- `storage/e2e-networks-object-storage` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:13.492Z (live) | stale on 2026-11-19
- url https://docs.e2enetworks.com/docs/tir/object-storage/Pricing/
- disagrees on verdict: `storage/e2e-networks-object-storage` says fails-egress, `storage/e2e-networks-object-storage-2` says fails-quota
- free tier: none reachable: ₹2.5/GB/mo = $26.46/TB plus ₹3/GB egress = $31.77/TB of egress. Billed on PEAK monthly usage, so deleting early in the month does not help. Both dimensions are far above the floor, and INR… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Data that leaves the network for the public internet is charged per GB, on top of storage billed on peak monthly usage; the per-GB rate is not shown on the captured vendor pages (unverified: the page defers to a rate card). | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Re-read on 2026-11-04: https://docs.e2enetworks.com/docs/myaccount/storage/object_storage/faq/ (public-internet egress is billed per GB) and https://docs.e2enetworks.com/docs/tir/object-storage/Pricing/ (billing on peak monthly usage). The storage and egress rates sit on a separate pricing page that was not read, so the fails-egress verdict stays at reported.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: ₹2.5/GB/mo = $26.46/TB plus ₹3/GB egress = $31.77/TB of egress. Billed on PEAK monthly usage, so deleting early in the month does not help. Both dimensions are far above the floor, and INR…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: ₹2.5/GB/mo = $26.46/TB plus ₹3/GB egress = $31.77/TB of egress. Billed on PEAK monthly usage, so deleting early in the month does not help. Both dimensions are far above the floor, and INR…
  - [2] 2026-11-03: egress to the public internet is billed per GB | capture: sha256:c9e33a0a231c0971daa6bb30db8b3a51703e29770189b36d4c53debeaeeb93f0 | quote: Data that leaves E2E’s network for the public internet is charged per GB.
  - [2] 2026-11-04: egress to the public internet is billed per GB | capture: sha256:c9e33a0a231c0971daa6bb30db8b3a51703e29770189b36d4c53debeaeeb93f0 | quote: Data that leaves E2E’s network for the public internet is charged per GB.
- sources:
  - [1] https://docs.e2enetworks.com/docs/tir/object-storage/Pricing/
  - [2] https://docs.e2enetworks.com/docs/myaccount/storage/object_storage/faq/

## e2e networks object storage (india)

- `storage/e2e-networks-object-storage-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.e2enetworks.com/docs/tir/object-storage/Pricing/
- disagrees on verdict: `storage/e2e-networks-object-storage` says fails-egress, `storage/e2e-networks-object-storage-2` says fails-quota
- free tier: None reachable: ₹2.5/GB/month is $26.95/TB/mo. 6.6× Utho's archive tier and 17× its own archive. And data transfer is ₹3/GB, i.e. $32.24 per TB read. Worse, billing is on PEAK usage per calendar month: «T. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: ₹2.5/GB/month is $26.95/TB/mo — 6.6× Utho's archive tier and 17× its own archive — and data transfer is ₹3/GB, i.e. $32.24 per TB read. Worse, billing is on PEAK usage per calendar month…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: ₹2.5/GB/month is $26.95/TB/mo — 6.6× Utho's archive tier and 17× its own archive — and data transfer is ₹3/GB, i.e. $32.24 per TB read. Worse, billing is on PEAK usage per calendar month…
- sources:
  - [1] https://docs.e2enetworks.com/docs/tir/object-storage/Pricing/
