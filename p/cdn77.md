# CDN77 Object Storage

> cdn77.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cdn77/ | JSON https://fshy.ajam.dev/api/v1/entity/cdn77.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CDN77 Object Storage

- `storage/cdn77-object-storage` | qualifies-with-caveat | evidence reported | binding none | category object-storage
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.cdn77.com/pricing
- price $20/TB stored; $90/TB egress outside CDN77; $0 egress through CDN77. Growth plan $990/mo for 250 TB delivered (= $3.96/TB). | parsed USD 20/TB-mo
- free tier: S3-compatible storage, slider up to 50 TB on the page; priced at '$100/month ($0.02/GB)' i.e. $20/TB. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'Egress traffic* $0.09/GB — *Charges only apply to traffic outside of our CDN.' So delivery through CDN77's own CDN is free; only pulling straight from storage costs. Initial 50 GB egress free, initial 1M requests free. | metered: yes
- identity: card | detail: card
- interface: s3-compatible
- limits note: per-object-cap: none published. Storage at $0.03/10k requests after 1M free. Request pricing exists, unlike Bunny/CacheFly.
- interface detail: s3
- tooling: S3 API; 'Seamless integration with CDN77 delivery platform'. Growth plan is $990/mo for 250 TB traffic with $3.96/TB overage.
- composes with: Origin storage integrates with CDN77 without separate origin egress charges. Storage at rest is priced at $20 per TB monthly.
- reliability: 330 Tbps, enterprise-oriented; sales-gated plans ('Talk to sales') rather than self-serve checkout. Also one of the few CDNs that explicitly sponsors OSS (Blender, GNOME, Let's Encrypt, Fedora, Manjaro). See the Fast Forward note.
- notes: the same as the free tier
- extras:
  - price_verbatim: $20/TB stored; $90/TB egress outside CDN77; $0 egress through CDN77. Growth plan $990/mo for 250 TB delivered (= $3.96/TB).
- evidence:
  - [1] 2026-10-21: 'CDN77 Object Storage … S3-compatible API … No egress fees between the storage and CDN77 delivery platform', 'Egress traffic* $0.09/GB', '$100/month ($0.02/GB)', Growth plan '$990/month $3.96/TB overages'
- sources:
  - [1] https://www.cdn77.com/pricing
