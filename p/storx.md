# storx

> storx.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/storx/ | JSON https://fshy.ajam.dev/api/v1/entity/storx.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## storx

- `storage/storx` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:43.355Z (live) | stale on 2026-11-19
- url https://www.storx.io/pricing
- free tier: None reachable: Every route lands on a sign-in wall; the only quotable copy is 'S3-Compatible Offsite Backup Storage — No Egress Fees'. No free allowance was visible after two attempts, so nothing is claime. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: No egress fees (vendor home page); the free allowance and paid prices are not readable on the pricing page, which renders no plan values to a page reader. | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: re-read on 2026-11-03: the vendor home page https://www.storx.io/; it states no egress fees and also lists a Free plan with 2 GB of encrypted storage and email account creation, which free_tier.stated does not reflect; confidence stays reported
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Every route lands on a sign-in wall; the only quotable copy is 'S3-Compatible Offsite Backup Storage — No Egress Fees'. No free allowance was visible after two attempts, so nothing is…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Every route lands on a sign-in wall; the only quotable copy is 'S3-Compatible Offsite Backup Storage — No Egress Fees'. No free allowance was visible after two attempts, so nothing is…
  - [2] 2026-10-21: cited as the basis of the rejection: Every route lands on a sign-in wall; the only quotable copy is 'S3-Compatible Offsite Backup Storage — No Egress Fees'. No free allowance was visible after two attempts, so nothing is claime
  - [3] 2026-11-03: the vendor states there are no egress fees | capture: sha256:fee2d6c49ea8754c1c1d69034b75c86668bf4f449ba6165591f931f10a092126 | quote: No single point of failure. No egress fees.
  - [3] 2026-11-04: the vendor states there are no egress fees | capture: sha256:6316994828f362ec6edae3c2791dce46289c57074e76beb11d9b440c4532595a | quote: No single point of failure. No egress fees.
- sources:
  - [1] https://www.storx.io/pricing
  - [2] https://www.storx.io/login
  - [3] https://www.storx.io/
