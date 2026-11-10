# hetzner object storage

> aeroftp.app | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aeroftp/ | JSON https://fshy.ajam.dev/api/v1/entity/aeroftp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## hetzner object storage (as the kms alternative to storage box)

- `storage/hetzner-object-storage-2` | paid-only | evidence documented | binding none | category rejected-provider
- needs card yes, phone no, ID no, institution no | verified 2026-10-30T18:30:36.688Z (inherited) | stale on 2026-11-30
- url https://docs.aeroftp.app/providers/hetzner-storage-box
- price EUR 6.49 a month base price, billed at EUR 0.0104 an hour for every hour at least one bucket exists, including 1 TB of storage (up to 744 TB-hours) and 1 TB of egress; storage beyond it EUR 0.0087 per TB-hour, about EUR 6.47 per TB in a 744-hour month; egress beyond it EUR 1.0000 per TB; prices exclude VAT | parsed USD 7.25/TB-mo
- duplicate of `storage/hetzner-object-storage`
- free tier: no free allowance: a EUR 6.49 a month base price (excl. VAT) includes 1 TB of storage and 1 TB of egress; storage and egress beyond it are billed pay-as-you-go | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: the base price includes 1 TB of egress a month for the whole account, accumulated hourly (at most 1.1160 TB in a 31-day month) and not carried over to the next month; ingress, internal traffic within the eu-central network zone and S3 operations such as PUT, GET and DELETE are free, but the egress those operations cause is billed | metered: yes | free allowance: 1 TB per month | price per TB: EUR 1.0000 per TB beyond the included quota, excl. VAT
- identity: card | detail: before an order is processed the account may have to be verified with a copy of a valid government-issued ID (ID card or passport) or with an advance payment from the holder's own credit card; registrants are asked not to use a free email address or a VPN service
- interface: s3-compatible
- interface detail: S3-compatible API at the fsn1, nbg1 and hel1 your-objectstorage.com endpoints
- tooling: not documented
- composes with: not recorded
- reliability: Pricing is €6.49/TB with 1 TB traffic included, compared to €3.20/TB with unmetered traffic on the Storage Box product.
- notes: the same as reliability
- evidence note: the price, the included quota and the locations are quoted from the first-party product page, the egress rules and endpoints from the first-party documentation, and the verification gate from the first-party fraud prevention FAQ
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: The guide that surfaced it states the comparison directly.
  - dead_end.retry_when: if a free allowance is added
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The guide that surfaced it states the comparison directly.
  - [2] 2026-10-30: the EUR 6.49 base price (EUR 0.0104 an hour) includes 1 TB of storage and 1 TB of egress; overage is EUR 0.0087 per TB-hour stored and EUR 1.0000 per TB of egress, excl. VAT | capture: sha256:d8ae06105caf52381149c3e0cc3781e2fbd75a3f6d7a9e468525aa90ab3e747f | quote: This base price includes 1 TB of storage (up to 744 TB-hours) and 1 TB of egress traffic.
  - [3] 2026-10-30: the included egress accrues hourly to at most 1.1160 TB in a 31-day month; unused quota expires at month end; ingress, eu-central internal traffic and S3 operations are free, the egress they cause is not | capture: sha256:15eabf26181806275b1779b8a7658fcc0e4073391b5a34d9f4db4590a4bd141c | quote: | Month with 31 days | max. 744 TB-hour | max. 1.1160 TB |
  - [3] 2026-10-30: egress beyond the included quota has a price, so traffic out is metered | capture: sha256:15eabf26181806275b1779b8a7658fcc0e4073391b5a34d9f4db4590a4bd141c | quote: Storage and traffic in excess of the quota included in the base price are billed separately on a pay-as-you-go basis based on your total account usage.
  - [2] 2026-10-30: the egress overage rate is EUR 1.0000, printed under Egress traffic with the unit per TB on the next line | capture: sha256:d8ae06105caf52381149c3e0cc3781e2fbd75a3f6d7a9e468525aa90ab3e747f | quote: € 1.0000 per hour, excl. VAT
  - [4] 2026-10-30: the account may have to be verified before an order with an ID document or a prepayment from the holder's own credit card; the page asks registrants not to use free email addresses or VPNs | capture: sha256:8f8bb169af727cac3b39ab390075e8c31bae86ecf6e3e05a15d69005c929ca83 | quote: Alternatively, you can verify your account by making an advance payment with your own credit card.
  - [3] 2026-10-30: the interface is the S3 API at the fsn1, nbg1 and hel1 your-objectstorage.com endpoints | capture: sha256:15eabf26181806275b1779b8a7658fcc0e4073391b5a34d9f4db4590a4bd141c | quote: - Amazon S3 API with the Hetzner S3 endpoint
- sources:
  - [1] https://docs.aeroftp.app/providers/hetzner-storage-box
  - [2] https://www.hetzner.com/storage/object-storage/
  - [3] https://docs.hetzner.com/storage/object-storage/overview/
  - [4] https://docs.hetzner.com/general/security-and-identify/fraud-prevention-faq/
