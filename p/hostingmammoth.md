# Hosting Mammoth Object Storage

> hostingmammoth.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostingmammoth/ | JSON https://fshy.ajam.dev/api/v1/entity/hostingmammoth.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hosting Mammoth Object Storage

- `storage/hosting-mammoth-object-storage` | qualifies | evidence reported | binding none | category S3-compatible object storage (EU)
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T01:28:32.687Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://hostingmammoth.com/object-storage
- price $5.62/TB at 5 TB (EUR 24.99 = $28.07) and $5.62/TB at 20 TB (EUR 99.99 = $112.33), before the EUR 1/TB egress overage. | parsed USD 5.62/TB-mo
- free tier: Base plan EUR 4.99/mo = 1 TB storage + 1 TB egress; 100 buckets, 50M objects/bucket, 100 TB/bucket, 5 TB max object | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 TB maximum single object (via multipart upload) | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: "The base plan includes 1 TB storage and 1 TB egress. Overages are billed at EUR 0.005/GB/month for storage and EUR 1.00/TB for egress. Ingress (uploads) and API calls are always free." | metered: yes | price per TB: EUR 1.00/TB
- identity: card | detail: card
- interface: s3-compatible, rclone, cli
- limits note: Single-provider small host; static website hosting explicitly not supported; no per-TB graduated tier. The overage rate is a derived per-GB rate, not a published block price.
- interface detail: S3 API, AWS Signature V4
- tooling: AWS CLI, rclone, Cyberduck, s3cmd, MinIO client, Node/Python(boto3)/Go SDKs. All named.
- composes with: S3 origin; versioning, object lock/WORM, lifecycle, presigned URLs, SSE-C all supported.
- reliability: unverified: https://hostingmammoth.com/object-storage answered HTTP 403 to a direct request on 2026-11-03; the page text was read only through an undated search-index copy (provider exa), which carries the egress and limit text but not the monthly base price or any order availability; routes tried: a direct request, a page reader, every pinned page reader (one returned the index copy, the rest refused or failed), a raw fetch with headers (HTTP 403 from the origin), the Wayback Machine (no capture)
- notes: the same as the free tier
- extras:
  - price_verbatim: $5.62/TB at 5 TB (EUR 24.99 = $28.07) and $5.62/TB at 20 TB (EUR 99.99 = $112.33), before the EUR 1/TB egress overage.
- evidence:
  - [1] 2026-10-21: meta: "Starting at EUR4.99/month with 1 TB storage and 1 TB egress included"; FAQ: "Overages are billed at EUR0.005/GB/month for storage and EUR1.00/TB for egress. Ingress (uploads) and API calls are always free."; "Maximum single object size is 5 TB"; "Static website hosting is not currently supported"
  - [2] 2026-10-21: separate storage-VPS product line (not S3)
  - probe:https://hostingmammoth.com/object-storage 2026-10-30: the product page answered HTTP 403 to a direct request on 2026-10-30 | capture: sha256:b8dbc67c9a965821dd81c65912aa23f9ee5c52f81c86a68adfb1fcd11c127e89 | quote: "status": 403
  - probe:https://hostingmammoth.com/ 2026-10-30: the home page answered HTTP 403 to a direct request on 2026-10-30 | capture: sha256:e4156e0802a88d8af7dd3a70c72487f74d14bc17b590b63791448ef7c204a232 | quote: "status": 403
  - [1] 2026-11-03: bucket, object and size limits, including a 5 TB maximum single object | capture: sha256:5c18d430f7a604a6de9a2ba92e17598b9d6925cc6d4fcb1fc90adb630f457be9 | quote: Up to 100 buckets per account, 50 million objects per bucket, and 100 TB per bucket. Maximum single object size is 5 TB (via multipart upload).
  - probe:https://hostingmammoth.com/object-storage 2026-11-03: the origin answered HTTP 403 to a direct request on 2026-11-03 | capture: sha256:51faf4d7ea903087c73f558859f330049ddb1fc99a342d41625c3ec66bfe6d35 | quote: "status": 403
  - [1] 2026-11-03: the page copy states the base plan includes 1 TB storage and 1 TB egress and bills egress overage at 1.00 euro per TB | capture: sha256:5c18d430f7a604a6de9a2ba92e17598b9d6925cc6d4fcb1fc90adb630f457be9 | quote: The base plan includes 1 TB storage and 1 TB egress. Overages are billed at €0.005/GB/month for storage and €1.00/TB for egress. Ingress (uploads) and API calls are always free.
- sources:
  - [1] https://hostingmammoth.com/object-storage
  - [2] https://hostingmammoth.com/storage-vps
