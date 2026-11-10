# Cloudinary

> cloudinary.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudinary/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudinary.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cloudinary

- `storage/cloudinary-2` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://cloudinary.com/documentation/pricing.md
  - [2] https://cloudinary.com/pricing/compare-plans

## Cloudinary (free plan)

- `storage/cloudinary` | fails-quota | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://cloudinary.com/pricing/compare-plans
  - [2] https://cloudinary.com/pricing
