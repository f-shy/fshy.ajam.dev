# CDN77 Object Storage

> cdn77.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cdn77/ | JSON https://fshy.ajam.dev/api/v1/entity/cdn77.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CDN77 Object Storage

- `storage/cdn77-object-storage` | qualifies-with-caveat | evidence reported | binding none | category object-storage
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:54:57.891Z (live) | stale on 2026-12-10
- url https://www.cdn77.com/pricing
- price USD 20/TB stored; USD 90/TB egress outside CDN77; USD 0 egress through CDN77. Growth plan USD 990/mo for 250 TB delivered (USD 3.96/TB). | parsed USD 20/TB-mo
- free tier: S3-compatible object storage with a slider up to 50 TB; priced at USD 100/month (USD 0.02/GB) for 5 TB stored; USD 20/TB at that tier. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: the object-storage limits page publishes a 1,000,000-object account cap and 50 buckets per account; no per-object byte cap is stated
- retention: source: [1] | note: no retention or expiry clause is published on the object-storage pricing page; the page lists storage prices per TB and per GB without a period
- egress: Egress traffic* charges only apply to traffic outside of our CDN; USD 0.09/GB, initial 50 GB free. Requests USD 0.03 per 10k, initial 1M free. No egress fees between the storage and CDN77 delivery platform. | metered: yes
- identity: card | detail: card
- interface: s3-compatible
- limits note: per-object-cap: none published. Storage at $0.03/10k requests after 1M free. Request pricing exists, unlike Bunny/CacheFly.
- interface detail: s3
- tooling: S3 API; 'Seamless integration with CDN77 delivery platform'. Growth plan is $990/mo for 250 TB traffic with $3.96/TB overage.
- composes with: Origin storage integrates with CDN77 without separate origin egress charges. Storage at rest is priced at $20 per TB monthly.
- reliability: 330 Tbps, enterprise-oriented; sales-gated plans ('Talk to sales') rather than self-serve checkout. Also one of the few CDNs that explicitly sponsors OSS (Blender, GNOME, Let's Encrypt, Fedora, Manjaro). See the Fast Forward note.
- notes: S3-compatible storage, slider up to 50 TB on the page; priced at '$100/month ($0.02/GB)' i.e. $20/TB.
- extras:
  - price_verbatim: $20/TB stored; $90/TB egress outside CDN77; $0 egress through CDN77. Growth plan $990/mo for 250 TB delivered (= $3.96/TB).
- evidence:
  - [1] 2026-10-21: 'CDN77 Object Storage … S3-compatible API … No egress fees between the storage and CDN77 delivery platform', 'Egress traffic* $0.09/GB', '$100/month ($0.02/GB)', Growth plan '$990/month $3.96/TB overages'
  - [1] 2026-11-19: the pricing page states the object-storage price and stored-data slider | capture: sha256:c14d2c7da132c15f1836fbeafe41a24d2f2482edf0e90b742b5e8dad99248d9f | quote: $100/month($0.02/GB)
  - [1] 2026-11-19: the pricing page states the egress rate and its free allowance | capture: sha256:c14d2c7da132c15f1836fbeafe41a24d2f2482edf0e90b742b5e8dad99248d9f | quote: Egress traffic* $0.09/GB Initial 50 GB: Free * Charges only apply to traffic outside of our CDN.
  - [1] 2026-11-19: the pricing page states the Growth plan price and overage rate | capture: sha256:c14d2c7da132c15f1836fbeafe41a24d2f2482edf0e90b742b5e8dad99248d9f | quote: $990/month$3.96/TB overages
  - [1] 2026-11-19: the object-storage slider is denominated in TB | capture: sha256:c14d2c7da132c15f1836fbeafe41a24d2f2482edf0e90b742b5e8dad99248d9f | quote: Stored data:5 TB on
  - [1] 2026-11-19: the object-storage page lists the S3-compatible API | capture: sha256:c14d2c7da132c15f1836fbeafe41a24d2f2482edf0e90b742b5e8dad99248d9f | quote: S3-compatible API
  - [2] 2026-11-25: the published limit is on account object count, not per-object bytes | capture: sha256:d53d16d4e2dbf6461d1d1b7c79e7fd9aaa9b2951414769712c7d932d57d6a822 | quote: - You can have up to 1,000,000 objects per account
  - [3] 2026-11-25: the pricing page states storage prices without a retention term or a month period | capture: sha256:42352e1ab666db200d905d9dacd63da42092e8972b28d4e095513cb8c456278e | quote: - First 1 TB: $20 - Beyond 1 TB: $0.02 per GB
  - [4] 2026-11-25: the introduction states the S3-compatible interface | capture: sha256:e5bc41de946d1be52ea5aeb8576b7279f7effce6f01f22c14921070dc1c17e1f | quote: CDN77 Object Storage is an S3-compatible service that lets you store large amounts of data.
  - [3] 2026-11-25: the pricing page states a 50 GB free egress allowance and $0.09 per GB outside the CDN | capture: sha256:42352e1ab666db200d905d9dacd63da42092e8972b28d4e095513cb8c456278e | quote: Egress Traffic: - First 50 GB: Free - Beyond 50 GB: $0.09 per GB (charges apply only to traffic outside of our CDN)
- sources:
  - [1] https://www.cdn77.com/pricing
  - [2] https://client.cdn77.com/support/knowledgebase/cdn77-object-storage/object-storage-limits
  - [3] https://client.cdn77.com/support/knowledgebase/cdn77-object-storage/object-storage-pricing
  - [4] https://client.cdn77.com/support/knowledgebase/cdn77-object-storage/cdn77-object-storage-introduction
