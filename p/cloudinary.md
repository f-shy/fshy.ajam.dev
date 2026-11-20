# Cloudinary

> cloudinary.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudinary/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudinary.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cloudinary

- `storage/cloudinary-2` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:00.657Z (live) | stale on 2026-12-04
- url https://cloudinary.com/documentation/pricing.md
- disagrees on verdict: `storage/cloudinary` says fails-quota, `storage/cloudinary-2` says fails-egress
- free tier: None reachable: Free plan is 25 credits/month where 1 credit = 1 GB storage OR 1 GB CDN bandwidth OR 1,000 transformations. I.e. 25 GB total across storage+delivery combined, and max raw file size is 10 MB. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: egress
  - dead_end.why: Free plan is 25 credits/month where 1 credit = 1 GB storage OR 1 GB CDN bandwidth OR 1,000 transformations — i.e. 25 GB total across storage+delivery combined, and max raw file size is 10…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free plan is 25 credits/month where 1 credit = 1 GB storage OR 1 GB CDN bandwidth OR 1,000 transformations — i.e. 25 GB total across storage+delivery combined, and max raw file size is 10…
  - [2] 2026-10-21: cited as the basis of the rejection: Free plan is 25 credits/month where 1 credit = 1 GB storage OR 1 GB CDN bandwidth OR 1,000 transformations — i.e. 25 GB total across storage+delivery combined, and max raw file size is 10 MB
  - [1] 2026-11-19: one Cloudinary credit equals 1 GB of CDN bandwidth | capture: sha256:1a858f48d8d9c8df750ee3128a9afae4b18b291de6262979dbbae4b664db0792 | quote: 1 GB of viewing (CDN) bandwidth, OR
- sources:
  - [1] https://cloudinary.com/documentation/pricing.md
  - [2] https://cloudinary.com/pricing/compare-plans

## Cloudinary (free plan)

- `storage/cloudinary` | fails-quota | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:08.377Z (live) | stale on 2026-12-04
- url https://cloudinary.com
- disagrees on verdict: `storage/cloudinary` says fails-quota, `storage/cloudinary-2` says fails-egress
- free tier: 25 monthly credits. 1 credit = 1 GB managed storage OR 1 GB CDN bandwidth OR 1,000 transformations, mixable. So max 25 GB if every credit is spent on storage and nothing is served. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB per file | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Metered from the same credit pool: every GB of viewing bandwidth burns 1 credit. Delivering 25 GB empties the account. Fails the free-egress filter. | metered: yes
- identity: email
- interface: s3, rest
- limits:
  - per-object-cap (binding): 100 MB per file [1]
- limits note: 25 credits/mo; 100 MB per file on free; the original is retained and retrievable (raw delivery of the original is supported); transformations are what burn credits. Credit exhaustion blocks delivery.
- interface detail: rest
- tooling: Excellent: REST plus SDKs for every language, signed/unsigned upload presets, remote fetch, auto-backup to S3/GCS.
- composes with: Unlimited free accounts (3 users / 1 account per free plan) x 25 credits. But credits reset monthly, so stored data does not survive if you stop paying attention. One cloud_name per account.
- reliability: Credit exhaustion is silent until delivery 401s; assets are not deleted but become undeliverable. Effectively a metered trial that renews.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 25 monthly credits. 1 credit = 1 GB managed storage OR 1 GB CDN bandwidth OR 1,000 transformations, mixable. So max 25 GB if every credit is spent on storage and nothing is served.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '1 Credit equals 1000 transformations or 1GB of managed storage or 1GB of viewing bandwidth or 500 SD video seconds or 250 HD video processing seconds'
  - [2] 2026-10-21: '25 monthly credits'; '3 Users / 1 Account'; the same free column also lists '25 Gigabytes (GB) of Storage'
  - [2] 2026-11-19: the free plan includes 25 monthly credits, the binding monthly allowance | capture: sha256:2408ca4619e369a9d35f05b2f92bb4a2c5b0c503e0af65f60949f95df363394a | quote: 25 monthly credits
  - [1] 2026-11-19: one credit is interchangeable across storage, bandwidth and transformations, so any serving burns the storage budget | capture: sha256:2cf95239c620bf44f99131e8880062b2288cb4dbbcb54f771c163757684935f2 | quote: 1 Credit equals 1000 transformations or 1GB of managed storage or 1GB of viewing bandwidth or 500 SD video seconds or 250 HD video processing seconds.
- sources:
  - [1] https://cloudinary.com/pricing/compare-plans
  - [2] https://cloudinary.com/pricing
