# Akamai Cloud

> linode.com | Storage, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linode/ | JSON https://fshy.ajam.dev/api/v1/entity/linode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Akamai / Linode Object Storage

- `storage/akamai-linode-object-storage` | qualifies-with-caveat | evidence documented | binding none | category object-storage
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T01:28:47.499Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://www.linode.com/products/object-storage/
- price USD 5 a month flat, prorated, including 250 GB of storage and 1 TB of outbound transfer added to the account's global transfer pool; storage beyond 250 GB USD 0.02 per GB a month (about USD 20 per TB), and overages may vary by data center; outbound overage USD 0.005 per GB (about USD 5 per TB), USD 0.015 per GB in Jakarta and USD 0.007 per GB in São Paulo | parsed USD 20/TB-mo
- free tier: USD 5 a month flat, prorated, for 250 GB of storage and 1 TB of outbound transfer added to the account's transfer pool; storage beyond 250 GB USD 0.02 per GB a month | unit: GB | metered on: unstated | read on: 2026-10-30 | source: [1]
- per-object cap: 5 TiB per object; a single upload is at most 5 GB, larger objects by multipart upload of up to 10,000 parts of 5 MiB to 5 GiB | bytes: 5497558138880 | source: [2] | note: Maximum Object Size under the multipart upload limits of the first-party quotas and limits page
- retention: source: [3] | note: not stated
- egress: enabling Object Storage adds 1 TB a month of transfer allowance, prorated by active hours, to the account's global network transfer pool and none to region-specific pools such as Jakarta and São Paulo; all outbound transfer from Object Storage is metered, over public IPv4 and IPv6, even to other services in the same data center; inbound transfer is free; transfer beyond the pools is billed at the end of the billing period at the rate of the service region | metered: yes | free allowance: 1 TB per month | price per TB: USD 0.005 per GB (about USD 5 per TB) beyond the pool; USD 0.015 per GB in Jakarta and USD 0.007 per GB in São Paulo
- identity: card | detail: a valid credit card on file is a requirement of the Master Services Agreement; Visa, Mastercard, American Express and Discover are accepted, and credit can be added from a PayPal account
- interface: s3-compatible, rclone
- limits:
  - per-object-cap: 5 TiB per object [2]
  - request-rate: 750 requests/s per bucket for all operations on E0 and E1 endpoints; on E2 and E3 by default 2,000 GET/HEAD, 500 PUT, 100 LIST and 200 DELETE requests/s per bucket; requests above the limit get HTTP 503 [2]
  - volume-quota: default capacity per account per endpoint 5 TB on E0, 100 TB on E1 and E2, 500 TB on E3; per bucket at most 1 TB on E0, 1 PB on E1 and E2, 5 PB on E3 [2]
- limits note: 5 GB per single upload; multipart parts of 5 MiB to 5 GiB, up to 10,000 parts; 1,000 buckets per account per endpoint by default; default ingress and egress throughput 2 Gbps per account per endpoint on E0 and E1 and 10 Gbps on E2 and E3; on E0 and E1 delete requests are capped at 100 per second per bucket within the 750 requests/s limit; quotas are account defaults, while product limits cannot be increased
- binding note: no named limit binds before the transfer price: the default capacity is 100 TB per account per endpoint on E1 and E2 and 500 TB on E3, objects reach 5 TiB, and a bucket takes at least 750 requests/s; the deciding terms are the storage and outbound transfer prices
- interface detail: s3
- tooling: S3 API, rclone s3 backend, any SDK. Cluster URL per region. The endpoint type (E0 to E3) is a property of the region and its endpoint hostname, chosen when a bucket is created, and is not an account-level default; most regions offer one type and a few offer several; new customers are directed to the standard E2 or E3 endpoints, and Limited Availability endpoints are opened by a support ticket.
- composes with: The 1 TB/month included egress is the free slice: enough for 33 GB/day, matching Gcore. Its real use is as a stable S3 origin behind one of the free CDNs, not as the delivery path. $5/TB egress is good but Bunny's Volume tier matches it and CacheFly/Telnyx beat it.
- reliability: requests above a bucket's rate limit are answered with HTTP 503; spreading data across buckets gives each bucket its own limit
- notes: Scales 250 GB → 5 PB per bucket, 10 billion objects, 20K RPS. Entry plan $5/mo = 250 GB + 1 TB outbound included.
- evidence note: the plan price, storage and transfer rates and the card requirement are quoted from the first-party pricing page, the transfer metering from the first-party network transfer page, and the object, request and capacity limits from the first-party quotas and limits page
- extras:
  - price_verbatim: $20/TB stored + $5/TB egress beyond the included 1 TB; entry $5/mo for 250 GB + 1 TB egress.
- evidence:
  - [4] 2026-10-21: → resolves to https://www.akamai.com/products/object-storage: 'Scale from 250 GB to 5 PB per bucket', 'up to 20K RPS', 'free inbound transfer and up to 1TB outbound is included'
  - withheld 2026-10-21: 
  - [1] 2026-10-30: USD 5 a month flat, prorated, for 250 GB; storage beyond it USD 0.02 per GB and may vary by data center; 1 TB of transfer is added to the global pool; overage USD 0.005 per GB, Jakarta USD 0.015, Sao Paulo USD 0.007 | capture: sha256:404db7a35989f79f9cf6a42f8f9e86379810802cfe8f7ad9d4f66c831bcaa365 | quote: Object Storage costs a flat rate of $5 a month, and includes 250 GB of storage.
  - [5] 2026-10-30: all Object Storage egress is metered, even within the data center; Object Storage adds 1 TB a month to the global pool and none to Jakarta or Sao Paulo pools; inbound is free | capture: sha256:fe9ae768d30ec941b0492ccf8138ec90573ed7daede9e19727e716b3e83857f7 | quote: * Outbound transfer from Object Storage (over both public IPv6 and public IPv4), even to other services within the same data center.
  - [1] 2026-10-30: outbound overage is USD 0.005 per GB, USD 0.015 in Jakarta and USD 0.007 in Sao Paulo | capture: sha256:404db7a35989f79f9cf6a42f8f9e86379810802cfe8f7ad9d4f66c831bcaa365 | quote: Any outbound network transfer overages are billed at the rate $0.005/GB for all data centers except for Jakarta ($0.015/GB) and São Paulo ($0.007/GB).
  - [1] 2026-10-30: a valid credit card on file is required by the Master Services Agreement; Visa, Mastercard, American Express and Discover are accepted and PayPal can add credit | capture: sha256:404db7a35989f79f9cf6a42f8f9e86379810802cfe8f7ad9d4f66c831bcaa365 | quote: Maintaining a valid credit card on file with your account is a requirement of our
  - [2] 2026-10-30: the per-object cap is 5 TiB; a single upload is at most 5 GB and multipart allows 10,000 parts of 5 MiB to 5 GiB | capture: sha256:b56ca5428388138f0deb8eb4e6d65f61f89142ba36c16ccb18b5bd6455d8ac13 | quote: * Maximum Object Size. 5 TiB
  - [2] 2026-10-30: E0 and E1 buckets take 750 requests/s for all operations; E2 and E3 default to 2,000 GET/HEAD, 500 PUT, 100 LIST and 200 DELETE requests/s per bucket | capture: sha256:b56ca5428388138f0deb8eb4e6d65f61f89142ba36c16ccb18b5bd6455d8ac13 | quote: For E0 and E1 endpoints all operations count towards one rate limit for the bucket.
  - [2] 2026-10-30: default capacity per account per endpoint is 5 TB on E0, 100 TB on E1 and E2 and 500 TB on E3; per bucket 1 TB on E0, 1 PB on E1 and E2, 5 PB on E3 | capture: sha256:b56ca5428388138f0deb8eb4e6d65f61f89142ba36c16ccb18b5bd6455d8ac13 | quote: Quotas are account-level limits placed on usage for Object Storage.
  - [2] 2026-10-30: product limits are fixed while quotas are defaults; the page gives the upload, part, bucket-count and delete-rate limits | capture: sha256:b56ca5428388138f0deb8eb4e6d65f61f89142ba36c16ccb18b5bd6455d8ac13 | quote: Unlike account-level quotas, these product limits cannot be increased.
  - [2] 2026-10-30: rate-limited requests receive HTTP 503, and each bucket has its own limit | capture: sha256:b56ca5428388138f0deb8eb4e6d65f61f89142ba36c16ccb18b5bd6455d8ac13 | quote: Any requests that are rate limited will receive a 503 response.
  - [1] 2026-10-30: USD 0.02 per GB stored and USD 0.005 per GB out after the first 1 TB each month; the same page requires a credit card on file and calls the service S3-compatible | capture: sha256:404db7a35989f79f9cf6a42f8f9e86379810802cfe8f7ad9d4f66c831bcaa365 | quote: | $0.02/GB | $0.005/GB with the first 1TB free each month. | [Sign up](https://login.linode.com/signup) |
  - [6] 2026-10-30: the sign-up form asks for an email address, a username and a password, or a Google or GitHub sign-in | capture: sha256:55fb90e5f7d6a2b77dbcebb92a5939794cf885b051f85889d285346a5239c504 | quote: Sign up with email
  - [7] 2026-11-03: the vendor directs new customers to the standard E2 or E3 endpoints; no account-level default type is stated | capture: sha256:578962703b575a00524082618a0222408df59edb1e6392c9b2ae0d4bdf83c192 | quote: All new customers or projects should start with the standard endpoints (E2 or E3) to take advantage of increased performance and new features.
  - [8] 2026-11-03: the endpoint type is shown at bucket creation and follows the chosen region, not an account setting | capture: sha256:af54b206fd3aae6bf6607b1eccdc4c44aa01fd4588c7176e6e7c958e82f02cb1 | quote: Most regions only support one endpoint type
- sources:
  - [1] https://www.akamai.com/cloud/pricing/object-storage
  - [2] https://techdocs.akamai.com/cloud-computing/docs/object-storage-product-limits
  - [3] https://www.akamai.com/products/object-storage
  - [4] https://www.linode.com/products/object-storage/
  - [5] https://techdocs.akamai.com/cloud-computing/docs/network-transfer-usage-and-costs
  - [6] https://login.linode.com/signup
  - [7] https://techdocs.akamai.com/cloud-computing/docs/endpoint-types
  - [8] https://techdocs.akamai.com/cloud-computing/docs/create-and-manage-buckets

## Akamai Cloud (Linode)

- `egress/akamai-cloud-linode` | trial-only | evidence reported | binding volume-quota | category trial credit (provider VM) | tier free
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://www.linode.com/pricing/
- price USD 100 of credit
- free tier: Create an account to try this guide with a $100 credit. This credit will be applied to any valid services used during your first 60 days. | unit: mixed | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: $100 of credit at $0.005 per GB is 18.2 TiB, or 9.1 TiB a month across the 60-day window, plus the plan's included transfer of 0 to 20 TB a month; ingress: udp | metered: yes | free allowance: $100 of credit at $0.005 per GB is 18.2 TiB, or 9.1 TiB a month across the 60-day window, plus the plan's included transfer of 0 to 20 TB a month | source: [1]
- identity: card | detail: Maintaining a valid credit card on file with your account is a requirement of our Master Services Agreement. | country: None
- interface: cli, rest
- limits:
  - volume-quota (binding): $100 of egress at $0.005 per GB is 18.2 TiB, and the credit expires at 60 days [1]
- binding note: the 60-day expiry binds, not the volume: at 1 TiB a month the 60 days spend 2 TiB of an 18.2 TiB credit. At this volume the credit is nine times larger than the window it lives in.
- interface detail: the Linode CLI and API, and the Cloud Manager
- tooling: wg-quick on the instance; the Linode CLI or API
- composes with: one instance for 60 days with 18.2 TiB of metered egress behind it, or a plan with a 20 TB bundle and no credit needed
- reliability: unused promo credit expires at 60 days; plans that bundle no transfer bill every outbound byte
- notes: A USD 100 promotional credit at USD 0.005 per GB provides 20,000 GB (18.19 TiB) across 60 days, or 9.09 TiB monthly. At USD 0.01 per GB, the credit provides 10,000 GB (9.09 TiB total, 4.55 TiB monthly). Bundled plans include 0 TB to 20 TB per month of transfer.
- evidence note: the $100 and 60 days come from an archived copy of Linode's own documentation; the current /lp/free-credit/ path returns 404 and the pricing page renders no credit line. The $0.005 overage rate is third-party. A current first-party page carrying both would raise this to documented
- extras:
  - wg_path: native-conf
  - wg_detail: a Compute Instance with a public IPv4; wg-quick binds UDP with no vendor component in the path
  - ingress: udp
  - volume_tib_month: 9.09
  - volume_stated: $100 of credit at $0.005 per GB is 18.2 TiB, or 9.1 TiB a month across the 60-day window, plus the plan's included transfer of 0 to 20 TB a month
  - bytes_transit: yes
  - transit_note: outbound bytes cross Akamai's network and draw on a global transfer pool before any overage is billed
- evidence:
  - [1] 2026-10-23: 'Older plans include transfer that scales based on plan family and size, from 0 TB to 20 TB per month. G8 and GPU accelerated plans do not include bundled transfer or egress with the plan' and 'Maintaining a valid credit card on file with your account is a requirement'
  - [2] 2026-10-23: 'You are only billed for additional network transfer if your usage exceeds the global or data center-specific pools during a billing period'
  - [3] 2026-10-23: archived Linode documentation: 'Create an account to try this guide with a $100 credit. This credit will be applied to any valid services used during your first 60 days.'
  - [4] 2026-10-23: third party: 'In North America the overage price is US$0.005 per GB', with pooled transfer and only outbound metered
- sources:
  - [1] https://www.linode.com/pricing/
  - [2] https://techdocs.akamai.com/cloud-computing/docs/network-transfer-usage-and-costs
  - [3] https://archive.ph/4yiBQ
  - [4] https://wiki.licenseware.io/wiki/akamai-cloud-pricing-and-billing/
