# SystemFreaks S3-Compatible Object Storage

> systemfreaks.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/systemfreaks/ | JSON https://fshy.ajam.dev/api/v1/entity/systemfreaks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SystemFreaks S3-Compatible Object Storage

- `storage/systemfreaks-s3-compatible-object-storage-250-gb-free-du` | paid-only | evidence documented | binding none | category iaas
- needs card unknown, phone yes, ID no, institution no | verified 2026-10-30T12:21:42.672Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://systemfreaks.com/object-storage
- price USD 6.00/TB/month on Standard (egress free up to 3x storage, then USD 1.00 per TB); USD 8.00/TB/month on Unmetered (no egress fees) | parsed USD 1/TB-mo
- free tier: No free allowance is offered. Standard USD 6.00/TB/month with free egress up to 3x storage, then USD 1.00 per TB; Unmetered USD 8.00/TB/month with no egress fees. | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: the beta that carried the free allowance ended in January 2025; no free plan is listed now
- per-object cap: unverified: the vendor page states no per-object cap | source: [1] | note: the earlier value was the beta's free storage allowance, not a per-object cap
- retention: source: [2] | note: not stated
- egress: Standard: egress free up to 3x the storage quota, then USD 1.00 per TB. Unmetered: no egress fees. Ingress is free on both plans. | metered: no | price per TB: USD 1.00/TB above 3x storage on Standard; none on Unmetered
- identity: email | detail: the order signup form has fields for name, postal address, country, phone, email and a password; which fields are required, and the payment methods for the paid plans, are unverified: behind a sign-up
- interface: s3-compatible, rclone, cli
- limits note: Capacity is bought per TB and is individually expandable; no API request fees; Standard bills egress above 3x storage at USD 1.00 per TB. The vendor page publishes no per-object, request-rate or bucket cap.
- binding note: no limit of a vocabulary kind is published: capacity is bought per TB and is expandable, and the only other meter is Standard's egress above 3x storage
- interface detail: s3
- tooling: S3-compatible API with an access key per app, created and rotated in the web console; rclone, backup tools and any AWS SDK; a browser file manager with expiring share links. A custom-domain endpoint is listed as coming soon.
- composes with: No free allowance exists to multiply across accounts; every TB is billed. Objects are served through pre-signed URLs, public links or static website hosting, and the vendor page names CDN delivery.
- reliability: The beta that carried the free allowance ended in January 2025; beta buckets were invoiced for disk usage from their next renewal date. The provider runs colocated hardware and rented dedicated servers.
- notes: Two paid plans, no free allowance: Standard USD 6.00/TB/month with egress free up to 3x storage, then USD 1.00 per TB; Unmetered USD 8.00/TB/month with no egress fees. No API request fees; locations in Canada, the USA and France.
- evidence note: the vendor page, its order cart and the signup form were read on 2026-10-30: two plans priced per TB and no free plan
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 250 GB free during beta, 'and bandwidth is free'. Post-beta: $0.0050/GB storage ($5/TB/mo) with 1 TB bandwidth included then $1.00/TB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'During the beta, it's free for up to 250 GB of storage with the coupon STRBETA, and bandwidth is free. After the beta … Storage: $0.0050/GB … Bandwidth: 1 TB included then $1.00/TB'
  - [3] 2026-10-21: probe: GET -> HTTP 302 (redirect to login; site alive, beta status unverified)
  - [1] 2026-10-30: the vendor page lists two paid plans, Standard at USD 6.00/TB/month and Unmetered at USD 8.00/TB/month, and no free plan | capture: sha256:c6106c55b9efb168e7cf88128cc2b581b2919e02cf84dc6c1c51739c5dbe847c | quote: Store backups, media and app files from $6.00 per TB per month, with free egress up to 3× your storage. Choose Unmetered at $8.00 per TB and pay no egress fees.
  - [1] 2026-10-30: the offer is two paid plans priced per TB, with no free plan | capture: sha256:c6106c55b9efb168e7cf88128cc2b581b2919e02cf84dc6c1c51739c5dbe847c | quote: Two plans, priced per TB
  - [4] 2026-10-30: the provider's own account announced in January 2025 that the beta, which carried the free allowance, had ended | capture: sha256:ac8d43648220bb2a6668d0d2a96cb66cbcfc8d943e8f0ea133cd46a96f75691d | quote: The beta phase of our S3-compatible object storage has officially concluded.
  - probe:https://manager.systemfreaks.com/order/config/index/S3-Compatible-Object-storage/?group_id=33&pricing_id=3598&coupon=STRBETA 2026-10-30: the beta order link with coupon STRBETA no longer opens the beta package; it lands on the current paid package list | capture: sha256:651c0d4c2374a29724dc6b82fce68c318b1dcbc080c48128f417360e8dfb4fb4 | quote: "final_url": "https://manager.systemfreaks.com/order/main/packages/S3-Compatible-Object-storage/?group_id=38"
  - [1] 2026-10-30: the product name the vendor page uses | capture: sha256:c6106c55b9efb168e7cf88128cc2b581b2919e02cf84dc6c1c51739c5dbe847c | quote: S3-Compatible Object Storage
  - [1] 2026-10-30: Standard egress is free up to 3x the storage quota, then USD 1.00/TB; Unmetered has no egress fees; ingress is free | capture: sha256:c6106c55b9efb168e7cf88128cc2b581b2919e02cf84dc6c1c51739c5dbe847c | quote: Standard includes free egress up to 3× your storage quota. Above that, egress costs $1.00 per TB. Unmetered has no egress fees, and ingress is always free.
  - [1] 2026-10-30: capacity is bought per TB and is expandable; the page names no per-object, request or bucket cap | capture: sha256:c6106c55b9efb168e7cf88128cc2b581b2919e02cf84dc6c1c51739c5dbe847c | quote: Scalable, individually expandable storage capacity
  - [1] 2026-10-30: both plans include static website hosting | capture: sha256:c6106c55b9efb168e7cf88128cc2b581b2919e02cf84dc6c1c51739c5dbe847c | quote: Static website hosting
  - [1] 2026-10-30: rclone, backup tools and AWS SDKs work with per-app access keys | capture: sha256:c6106c55b9efb168e7cf88128cc2b581b2919e02cf84dc6c1c51739c5dbe847c | quote: Use rclone, your backup software or any AWS SDK with your access keys.
  - [4] 2026-10-30: after the beta ended, beta buckets were invoiced for disk usage from their next renewal date | capture: sha256:ac8d43648220bb2a6668d0d2a96cb66cbcfc8d943e8f0ea133cd46a96f75691d | quote: You can continue using your buckets; however, starting on your next renewal date, an invoice reflecting your disk usage will be issued.
  - [2] 2026-10-30: the provider's own account states it runs colocated hardware and rented dedicated servers | capture: sha256:3da83533a66141fe778442d623ee0cfae39a6759059cca06ef39684b0441b985 | quote: Our infrastructure combines colocated hardware and rented dedicated servers to ensure reliable service.
  - probe:https://manager.systemfreaks.com/order/config/index/S3-Compatible-Object-storage/?group_id=38&pricing_id=3741 2026-10-30: the Unmetered order configurator renders a price (USD 8.00), so new customers can order | capture: sha256:aaddff33d019d6bcbf034447f59b0d89bb2de90e761b026c94830000a289b71e | quote: "verdict": "priced"
  - [5] 2026-10-30: the order signup form has fields for a postal address, phone and email | capture: sha256:c4d13e7ee57faa2402439333770677877bdf7ea9eb4c419160a1b8d34c55f3e6 | quote: Zip/Postal Code Phone Fax Email
  - [1] 2026-10-30: the two plans and their egress terms, restated at the foot of the vendor page | capture: sha256:c6106c55b9efb168e7cf88128cc2b581b2919e02cf84dc6c1c51739c5dbe847c | quote: Choose Standard from $6.00 per TB with free egress up to 3× storage, or Unmetered at $8.00 per TB with no egress fees.
- sources:
  - [1] https://systemfreaks.com/object-storage
  - [2] https://lowendtalk.com/discussion/201922/systemfreaks-com-early-access-to-our-object-storage
  - [3] https://manager.systemfreaks.com/
  - [4] https://lowendtalk.com/discussion/201922/systemfreaks-com-early-access-to-our-object-storage/p3
  - [5] https://manager.systemfreaks.com/order/signup/index/S3-Compatible-Object-storage/
