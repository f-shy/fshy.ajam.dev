# unity

> unity.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unity/ | JSON https://fshy.ajam.dev/api/v1/entity/unity.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Unity Cloud Content Delivery (CCD)

- `storage/unity-cloud-content-delivery` | fails-egress | evidence inferred | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://unity.com/products/gaming-services/pricing
- free tier: Conflicting. The live UGS pricing page lists Cloud Content Delivery 'Cloud Storage — Free'. A third-party writeup of the same product reports 5 GB/month included. Unresolved; treat as small until an account test settles it. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Per-object-cap: entry upload bounded by the storage allowance; request-rate: API requests currently unlimited/free; per-ip-shaping: none documented. Retention: releases are immutable snapshots, kept until deleted. Good archive semantics if the quota is real. | source: [1] | note: not stated
- egress: Metered after a free tier allowance: 'Bandwidth (CCD) 50 GB / month. After 50 GB: $0.08 per GB, After 50 TB: $0.06 per GB'. | metered: yes | free allowance: 50 GB per month
- identity: national-id
- interface: rest, cli
- limits note: Per-object-cap: entry upload bounded by the storage allowance; request-rate: API requests currently unlimited/free; per-ip-shaping: none documented. Retention: releases are immutable snapshots, kept until deleted. Good archive semantics if the quota is real.
- interface detail: rest
- tooling: UGS CLI (`ugs ccd ...`), Content Delivery Management API and Client API, plus the CCD Management SDK. Releases are content-addressed: entries carry an md5 content hash and size that must match on upload.
- composes with: Buckets per environment x releases per bucket x promotion between buckets. Note: 'Creating or promoting a new release does not create copies of the entries in a bucket'. Promotion is a pointer, not a copy, so it does NOT multiply storage.
- reliability: The old CCD API-key auth and UCD CLI were deprecated in 2024 with no planned sunset after community pushback, so the write path still works but is on a deprecated auth path. Public read URLs are of the form https://{projectId}.client-api.unity3dusercontent.com/client_api/v1/buckets/{bucketId}/releases/{releaseId}/entry_by_path/content/?path=<path>.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Conflicting. The live UGS pricing page lists Cloud Content Delivery 'Cloud Storage — Free'. A third-party writeup of the same product reports 5 GB/month included. Unresolved; treat as small until an account test settles it.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Cloud Content Delivery: 'Cloud Storage — Free — Free'; 'Bandwidth (CCD) 50 GB / month; After 50 GB: $0.08 per GB'
  - [2] 2026-10-21: 'ストレージ容量 5 GB/月' (5 GB/month storage, ~$0.08/GB/mo overage) — direct contradiction of the 'Free' line
  - [3] 2026-10-21: read URL format, md5+size content hash requirement, 'Creating or promoting a new release does not create copies of the entries in a bucket'
  - [4] 2026-10-21: probe: GET -> 404 {"code":5,"details":["not found"],"reason":"Not found"} — API is live and gated on a project/org token
- sources:
  - [1] https://unity.com/products/gaming-services/pricing
  - [2] https://garnetcode.jp/blog/2025/08/ugs_ccd/
  - [3] https://docs.unity.com/en-us/ccd/faq
  - [4] https://content-api.cloud.unity3d.com/api/v1/buckets

## unity asset manager org storage (unity personal)

- `storage/unity-asset-manager-org-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.unity.com/en-us/cloud/billing/storage-pricing
- free tier: none reachable: Explicitly a hard cap: 'The plan has a non-extensible cap of 10 GB of storage ... At any given time, the total size of the assets that are currently stored in Unity Cloud can't exceed the… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Explicitly a hard cap: 'The plan has a non-extensible cap of 10 GB of storage ... At any given time, the total size of the assets that are currently stored in Unity Cloud can't exceed the…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Explicitly a hard cap: 'The plan has a non-extensible cap of 10 GB of storage ... At any given time, the total size of the assets that are currently stored in Unity Cloud can't exceed the…
- sources:
  - [1] https://docs.unity.com/en-us/cloud/billing/storage-pricing

## unity cloud save (the cloud save product, not ccd)

- `storage/unity-cloud-save` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://unity.com/products/gaming-services/pricing
- free tier: none reachable: Free tier includes 5 GiB per month storage, 1M write operations, and 1M read operations per month. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 5 GiB/month stored on the free tier, with 1M writes and 1M reads per month.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 GiB/month stored on the free tier, with 1M writes and 1M reads per month.
- sources:
  - [1] https://unity.com/products/gaming-services/pricing
