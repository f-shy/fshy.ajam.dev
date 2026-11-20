# CDN77 Object Storage

> cdn77.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cdn77/ | JSON https://fshy.ajam.dev/api/v1/entity/cdn77.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CDN77 Object Storage

- `storage/cdn77-object-storage` | qualifies-with-caveat | evidence reported | binding none | category object-storage
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T21:12:58.758Z (live) | stale on 2026-12-04
- url https://www.cdn77.com/pricing
- price USD 20/TB stored; USD 90/TB egress outside CDN77; USD 0 egress through CDN77. Growth plan USD 990/mo for 250 TB delivered (USD 3.96/TB). | parsed USD 20/TB-mo
- free tier: S3-compatible object storage with a slider up to 50 TB; priced at USD 100/month (USD 0.02/GB) for 5 TB stored; USD 20/TB at that tier. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
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
- sources:
  - [1] https://www.cdn77.com/pricing
