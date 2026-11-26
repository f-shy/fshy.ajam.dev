# Datalix S3-compatible Object Storage

> datalix.eu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datalix-2/ | JSON https://fshy.ajam.dev/api/v1/entity/datalix-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Datalix S3-compatible Object Storage (Frankfurt)

- `storage/datalix-s3-compatible-object-storage` | qualifies | evidence documented | binding volume-quota | category S3-compatible object storage, TB-prepaid
- needs card no, phone no, ID no, institution no | verified 2026-11-01T22:11:43.693Z (live) | stale on 2026-12-02
- url https://datalix.eu/rent-s3-compatible-objectstorage
- price EUR 3.95 per TB per month, prepaid, at every booked size from 1 TB to 100 TB; the page publishes no volume discount and no other rate. | parsed USD 4.42/TB-mo
- free tier: 1 TB to 100 TB of booked storage per account, up to 30 million objects per bucket | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1] | note: 1 TB is the minimum of the page's booked-storage control (min 1, max 100, step 1) and the 100 TB ceiling is stated in the specification block; the smallest configuration the order page offers is 1 TB
- per-object cap: No largest single object is stated. The order page states a 100 TB maximum size per bucket and 30 million files per bucket; the product page states a 100 TB maximum capacity per account and up to 30 million objects per bucket. Neither page states a per-object size limit. | source: [1] | note: the product page states 100 TB of capacity per account and 30 million objects per bucket; the order page states a 100 TB maximum size per bucket and 30 million files per bucket; neither page states a largest-single-object figure
- retention: Data is kept for the paid term; on expiry the service is suspended and the associated data and content are permanently deleted after a grace period of three days. | source: [2] | note: the grace period runs from the end of the paid term, not from inactivity; the terms state no retention rule for data inside a running term
- egress: Ingress is free and unlimited; egress includes 10 TB per 1 TB of booked storage, so the included volume scales with the booking. Egress beyond that ratio has no published price. | metered: yes | free allowance: 10 TB per 1 TB of booked storage
- identity: email | detail: registration takes a username, an email address and a password; ordering needs a password-protected customer account and prepayment, and the terms allow card, PayPal, SEPA, bank transfer or cryptocurrency
- interface: s3-compatible, rclone, cli
- limits:
  - volume-quota (binding): 100 TB per account [1]
- limits note: Prepaid, TB-based: the booked capacity is paid for whether or not it is used. 100 TB per account and 30 million objects per bucket. The product page publishes no S3 endpoint hostname, so the endpoint comes from the customer panel.
- binding note: the 100 TB per account cap ends the booking; the per-bucket object count (30 million) is the other ceiling, and the page states no per-object size cap
- interface detail: S3 API, IAM, 30 M objects/bucket
- tooling: any S3 SDK, rclone, s3cmd, restic
- composes with: native S3 → Cloudflare in front → presigned URLs; no wrapper needed
- reliability: Small German host (AS203446), Equinix FRA-05/07/08. Payment methods verified on their KVM page: PayPal, credit card, Sofort, Giropay, EPS, Paysafecard, Przelewy24, Bitcoin, Litecoin, Alipay, Monero, bank transfer. Best payment friction profile of any EU host here for a non-EU buyer.
- notes: the same as the free tier
- evidence note: the product page, its German edition, the terms and the order configuration were read and quoted; free tier, limits, egress, identity, retention and interface each cite a capture
- extras:
  - price_verbatim: €3.95/TB/mo flat at every tier (5 TB = €19.75, 20 TB = €79.00) ≈ $4.58/TB. No volume discount. Cheapest genuine S3-API option in the EU with a sane egress ratio.
  - verified[0].url: https://datalix.de/object-storage
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 404
  - verified[0].bytes: 64382
  - verified[0].sha256: 87c09ce4fc67418f8a32d85ec9d8ffbdaeefa87e6bd0e60c1a571d516372b6f7
  - verified[0].pattern_found: yes
  - verified[0].what_changed: no change: the page still states the claim
- evidence:
  - [1] 2026-10-21: '€3.95 per TB · prepaid', '100 TB max. per account', '30M objects per bucket', '∞ ingress · free', 'Egress includes 10 TB per 1 TB of storage', Frankfurt am Main EQ datacenter
  - withheld 2026-10-21: same page — comparison table claims Wasabi €6.40, IONOS €15.00, Azure/Google/DO €20.00, AWS €23.00 per TB (their figures, standard/hot list price)
  - [3] 2026-10-21: payment method list including Bitcoin/Monero/Alipay; 'When the traffic limit of your server is reached, the speed of your server will be limited to 10 MB/s (80Mbit/s)' (KVM products only — soft throttle, not a hard cut)
  - [1] 2026-11-01: the booked-storage price is EUR 3.95 per TB, capped at 100 TB | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Price: 3.95 EUR per TB, up to 100 TB.
  - [1] 2026-11-01: the account-level capacity ceiling is 100 TB | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Up to 100 TB per account
  - [1] 2026-11-01: the per-bucket object count ceiling is 30 million | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Up to 30 million objects per bucket.
  - [1] 2026-11-01: the included egress is a 10:1 ratio to booked storage, not a fixed volume | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Egress includes 10 TB per 1 TB of storage.
  - [2] 2026-11-01: an order cannot be placed without an account, and the registration form asks only for username, email and password | capture: sha256:7090e5757058c430d97659d2e5c780a6f1aa53ba6690e6650337c99c7a392b31 | quote: The conclusion of a contract requires the creation of a password-protected customer account.
  - [1] 2026-11-01: ingress is free and unlimited, so only egress is metered | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Ingress is free and unlimited.
  - [1] 2026-11-01: the interface is an S3-compatible API | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: S3 compatible API
  - [1] 2026-11-01: the booked-storage control runs from 1 TB to 100 TB in 1 TB steps, so the 1 TB lower bound is published and not inferred | capture: sha256:37cf83ae87e4b34a6499c74d7695278bc1f0533da72f113208343e695944e444 | quote: <input type="range" id="objectstorage-storage-range" min="1" max="100" step="1" value="1" class="dx-range" oninput="updateObjectStorageCalculator()">
  - [4] 2026-11-01: the smallest configuration the order page presents is one terabyte | capture: sha256:072b3d29bc17b3071b31767395209fa30688e8d456b6bffd12f1aab4cb93256e | quote: Storage - 1 TB
  - [1] 2026-11-01: the account-level capacity ceiling is 100 TB, the upper bound of the range | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Up to 100 TB per account
  - [2] 2026-11-01: the terms state the deletion timeline after the paid term ends, so retention is stated and not a gap | capture: sha256:7090e5757058c430d97659d2e5c780a6f1aa53ba6690e6650337c99c7a392b31 | quote: If the service is not actively renewed in time, it ends upon expiry of the period paid for. The Provider suspends the service upon expiry of the period; the associated data and content are subsequently permanently deleted after the expiry of a grace period of three days.
  - [2] 2026-11-01: the retention clause is in the terms, so the field names that page as its source | capture: sha256:7090e5757058c430d97659d2e5c780a6f1aa53ba6690e6650337c99c7a392b31 | quote: the associated data and content are subsequently permanently deleted after the expiry of a grace period of three days
  - [2] 2026-11-01: the deletion timeline is triggered by the end of the paid term | capture: sha256:7090e5757058c430d97659d2e5c780a6f1aa53ba6690e6650337c99c7a392b31 | quote: If the service is not actively renewed in time, it ends upon expiry of the period paid for.
  - [1] 2026-11-01:  | capture: sha256:37cf83ae87e4b34a6499c74d7695278bc1f0533da72f113208343e695944e444 | quote: <input type="range" id="objectstorage-storage-range" min="1" max="100" step="1" value="1" class="dx-range" oninput="updateObjectStorageCalculator()">
  - [4] 2026-11-01: the order page states the per-bucket object count the two readings share | capture: sha256:072b3d29bc17b3071b31767395209fa30688e8d456b6bffd12f1aab4cb93256e | quote: 30 million files max. per bucket
  - [1] 2026-11-01: the product page was served and read, so the earlier note about a 404 no longer describes the source | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: You only pay for booked storage.
  - [1] 2026-11-01:  | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Price: 3.95 EUR per TB, up to 100 TB.
  - [1] 2026-11-01: the product page still states the booked-storage price and the 100 TB account ceiling the record carries | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Price: 3.95 EUR per TB, up to 100 TB.
  - [5] 2026-11-01: the German edition carries the same booked-storage control, 1 TB to 100 TB, so the lower bound is published in both languages | capture: sha256:89e244e88f5c1ddb033ad4217f411e3dfeb4ed23345f89bda0741d2930d422f6 | quote: <input type="range" id="objectstorage-storage-range" min="1" max="100" step="1" value="1" class="dx-range" oninput="updateObjectStorageCalculator()">
  - [5] 2026-11-01: the German edition states the same 100 TB per account ceiling | capture: sha256:89e244e88f5c1ddb033ad4217f411e3dfeb4ed23345f89bda0741d2930d422f6 | quote: Bis zu 100 TB pro Account
  - [4] 2026-11-01: the order page states the per-bucket capacity ceiling as 100 TB alongside the 30 million object count | capture: sha256:072b3d29bc17b3071b31767395209fa30688e8d456b6bffd12f1aab4cb93256e | quote: 100 TB Maximum size per Bucket
  - [4] 2026-11-01: the cap the order page states is a per-bucket capacity, not a per-object size | capture: sha256:072b3d29bc17b3071b31767395209fa30688e8d456b6bffd12f1aab4cb93256e | quote: 100 TB Maximum size per Bucket
  - [1] 2026-11-01: the page gives an object count per bucket and no per-object size | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Up to 30 million objects per bucket.
  - [1] 2026-11-01: the pricing page states the prepaid booked-capacity model the field describes | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: You only pay for booked storage.
  - [4] 2026-11-01: the order page states a 100 TB ceiling on the size of a bucket, which is a bucket capacity and not an object size | capture: sha256:072b3d29bc17b3071b31767395209fa30688e8d456b6bffd12f1aab4cb93256e | quote: 100 TB Maximum size per Bucket
  - [1] 2026-11-01: the product page states the 100 TB capacity ceiling per account, not per bucket, so it does not carry the per-bucket figure the order page states | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Up to 100 TB per account
  - [4] 2026-11-01: the order page states the per-bucket file count that the field names | capture: sha256:072b3d29bc17b3071b31767395209fa30688e8d456b6bffd12f1aab4cb93256e | quote: 30 million files max. per bucket
  - [1] 2026-11-01: the product page states the per-bucket object count and states its 100 TB ceiling per account, so the note no longer attributes a per-bucket capacity to both pages | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Up to 30 million objects per bucket.
  - [1] 2026-11-01: the product page is live and still states the 100 TB account ceiling, the 30 million objects per bucket, free ingress and the 10 TB egress per 1 TB of booked storage | capture: sha256:e5bbd3fed3a9c2d4c13b50efc6b7ee7178302b19fe1a41a3e4332cc6fc86d313 | quote: Up to 100 TB per account
- sources:
  - [1] https://datalix.eu/rent-s3-compatible-objectstorage
  - [2] https://datalix.eu/tos
  - [3] https://datalix.eu/rent-storage-kvm-server
  - [4] https://datalix.eu/cp/order/config/7/5be0094e-d0ff-43ab-baf6-3fa4f7155fef
  - [5] https://datalix.de/s3-kompatibler-objectstorage-mieten
