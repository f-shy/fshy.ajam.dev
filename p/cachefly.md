# CacheFly Object Storage

> cachefly.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cachefly/ | JSON https://fshy.ajam.dev/api/v1/entity/cachefly.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CacheFly Object Storage ($25/TB with $0 egress)

- `storage/cachefly-object-storage` | qualifies-with-caveat | evidence reported | binding none | category object-storage
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T21:12:58.757Z (live) | stale on 2026-12-04
- url https://www.cachefly.com/object-storage/
- price $25/TB stored with $0 egress/ingress/requests (object storage). CDN separately: free developer 100 GB/mo; $0.05/GB overage. | parsed USD 25/TB-mo
- free tier: Unlimited S3-compatible object storage, USD 25 per TB per month with USD 0 request, ingress and egress fees. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: **$0 ingress, $0 egress, $0 request fees. Stated three ways on the same page** ('$25 per TB with $0 request, ingress or egress fees', 'Ingress and egress CacheFly is always free', 'no ingress or egress fees'). If the object storage is fronted by CacheFly's own CDN, delivery is included in the $25. | metered: yes | price per TB: $25 per TB
- identity: card | detail: card
- interface: s3-compatible
- limits note: per-object-cap: not stated on the page opened; no published cap. Request fees $0. Free developer account is 100 GB/month on one domain then $0.05/GB overage.
- interface detail: s3
- tooling: S3 API. Self-signup is at portal.cachefly.com/signup/developer100gb.
- composes with: For a serving-heavy workload this is the cheapest egress-free paid option found: 1 TB stored and 30 TB/mo delivered costs $25/mo total, because the only metre is bytes at rest. That inverts the usual model. Storage is the expensive line and egress is genuinely free. Pair with the free CDN tier (100 GB/mo) for the small hot set and put the 20 TiB cold archive elsewhere.
- reliability: Self-signup 'requires a credit card at registration … charged and refunded $1 to authenticate'. 65+ PoPs, 99.95% SLA. Object storage onboarding is sales-gated ('Sign Up' → contact-object-storage form), unlike the CDN developer account which is instant.
- notes: Unlimited, $25 per TB per month. S3-compatible.
- extras:
  - price_verbatim: $25/TB stored with $0 egress/ingress/requests (object storage). CDN separately: free developer 100 GB/mo; $0.05/GB overage.
- evidence:
  - [1] 2026-10-21: '$25 per TB with $0 request, ingress or egress fees'; 'Globally available starting at $25 per terabyte a month'; 'Ingress and egress CacheFly is always free'
  - [2] 2026-10-21: 'Self-signup plans require a credit card at registration … charged and refunded $1'; free developer account 100 GB/mo
  - [1] 2026-11-19: the object-storage page states the price and no request, ingress or egress fees | capture: sha256:20e069925b86007b12dea19f63202eb2af87e5212552497c882cf2e4fa32d2de | quote: $25 per TB with $0 request, ingress or egress fees
  - [1] 2026-11-19: the object-storage page states ingress and egress are always free | capture: sha256:20e069925b86007b12dea19f63202eb2af87e5212552497c882cf2e4fa32d2de | quote: Ingress and egress CacheFly is always free.
  - [2] 2026-11-19: self-signup requires a credit card at registration | capture: sha256:1128a77cd54fcca74928e6aa0b4c8bec122eadb35fa18dbaffe0e7d737fb707f | quote: Self-signup plans require a credit card at registration to streamline future billing.
- sources:
  - [1] https://www.cachefly.com/object-storage/
  - [2] https://www.cachefly.com/free/
