# proton

> proton.me | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proton/ | JSON https://fshy.ajam.dev/api/v1/entity/proton.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## proton drive paid

- `storage/proton-drive-paid` | paid-only | evidence reported | binding volume-quota | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:22:27.191Z (live) | stale on 2026-11-19
- url https://proton.me/drive/pricing
- price USD 10.00 per TB per month at Proton Family (3 TB, USD 29.99 per month); Proton Duo (2 TB + VPN) is USD 19.99 per month | parsed USD 10/TB-mo
- free tier: 5 GB of storage, photos and documents on Proton Free, no credit card required | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): 3 TB on the largest consumer plan (Proton Family); 2 TB on Proton Duo [1]
- binding note: the largest consumer plan holds 3 TB; Drive Professional is 1 TB per user at USD 9.99 per month; a 10 TiB set needs several plans or seats
- interface detail: not documented
- tooling: the same as interface detail
- composes with: capacity is sold per plan: Drive Plus 200 GB, Proton Unlimited 500 GB + VPN, Proton Duo 2 TB + VPN; the page states capacity up to 3TB on a paid consumer plan, beyond which Proton for Business sets the size
- reliability: Priced tiers on the page: Drive Plus 200 GB at USD 4.99 per month, Proton Unlimited 500 GB + VPN at USD 12.99 per month, Proton Duo 2 TB + VPN at USD 19.99 per month, Proton Family 3 TB at USD 29.99 per month.
- notes: Free: 5 GB. Paid consumer tiers: 200 GB, 500 GB, 2 TB and 3 TB.
- evidence note: plan names, sizes and the 5 GB free tier re-read on https://proton.me/drive/pricing on 2026-11-04; the paid-only verdict rests on that page
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Fails quota. No 2 TB+ consumer SKU published, no lifetime plan, no WebDAV/rclone/S3 path that would m
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Fails quota. No 2 TB+ consumer SKU published, no lifetime plan, no WebDAV/rclone/S3 path that would m
  - [1] 2026-11-03: Proton Free includes 5 GB of storage | capture: sha256:4edf6aa0f6091eb5937fb08be4ec5685494382ba3ae52ba326a44ef35113ea8e | quote: - 5 GB of storage, photos and documents
  - [1] 2026-11-03: the free allowance is stated in GB | capture: sha256:4edf6aa0f6091eb5937fb08be4ec5685494382ba3ae52ba326a44ef35113ea8e | quote: - 5 GB of storage, photos and documents
  - [1] 2026-11-03: the allowance is a stored volume | capture: sha256:4edf6aa0f6091eb5937fb08be4ec5685494382ba3ae52ba326a44ef35113ea8e | quote: - 5 GB of storage, photos and documents
  - [1] 2026-11-03: Proton Family is 3 TB at 29.99 USD per month | capture: sha256:a036253f2cba6c299f223126387ed014bd3b59d419584c124d0d2e4630634549 | quote: Proton Family 3 TB $29.99 /month
  - [1] 2026-11-03: the largest consumer plan on the page is 3 TB | capture: sha256:a036253f2cba6c299f223126387ed014bd3b59d419584c124d0d2e4630634549 | quote: Proton Family 3 TB $29.99 /month
  - [1] 2026-11-03: the largest consumer plan is 3 TB | capture: sha256:a036253f2cba6c299f223126387ed014bd3b59d419584c124d0d2e4630634549 | quote: Proton Family 3 TB $29.99 /month
  - [1] 2026-11-03: Drive Professional is 1 TB per user at 9.99 USD per month | capture: sha256:a036253f2cba6c299f223126387ed014bd3b59d419584c124d0d2e4630634549 | quote: Drive Professional 1 TB per user $9.99 /month
  - [1] 2026-11-03: Proton Duo is 2 TB + VPN at 19.99 USD per month | capture: sha256:a036253f2cba6c299f223126387ed014bd3b59d419584c124d0d2e4630634549 | quote: Proton Duo 2 TB + VPN $19.99 /month
  - [1] 2026-11-03: the plans that exceed the free 5 GB are priced | capture: sha256:a036253f2cba6c299f223126387ed014bd3b59d419584c124d0d2e4630634549 | quote: Proton Family 3 TB $29.99 /month
  - [1] 2026-11-03: the Proton Duo tier is 2 TB + VPN | capture: sha256:4edf6aa0f6091eb5937fb08be4ec5685494382ba3ae52ba326a44ef35113ea8e | quote: 2 TB + VPN
  - [1] 2026-11-04: Proton Drive plans sell file, photo and document storage: a cloud drive | capture: sha256:4edf6aa0f6091eb5937fb08be4ec5685494382ba3ae52ba326a44ef35113ea8e | quote: - 5 GB of storage, photos and documents
  - [1] 2026-11-04: paid Proton Drive plans raise the capacity to 3 TB | capture: sha256:ed512ba6d2345351da6e20a63b0b83bacdbfc70a5adef2dcc479226db86b1b6e | quote: If you upgrade to a paid Proton Drive plan, you will be able to take advantage of additional storage, increasing your drive capacity up to 3TB.
  - [1] 2026-11-04: the Proton Duo tier is 2 TB + VPN | capture: sha256:4edf6aa0f6091eb5937fb08be4ec5685494382ba3ae52ba326a44ef35113ea8e | quote: 2 TB + VPN
- sources:
  - [1] https://proton.me/drive/pricing

## Proton Drive

- `storage/proton-drive` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://proton.me/drive
- free tier: 5 GB free (starts at 2 GB, +3 GB welcome checklist within 30 days) | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No published per-GB egress meter on free; end-to-end encrypted so no CDN in front is possible. | metered: no
- identity: email
- interface: rest, rclone
- limits note: 5 GB; beta backend documented to break when Proton changes the protocol; E2E encryption means download cannot be CDN-offloaded to Cloudflare.
- interface detail: rest
- tooling: rclone backend 'protondrive' (Tier 4, added v1.64.0, self-described 'currently in Beta'; implemented by reverse-engineering the open-source client because Proton publishes no API docs).
- composes with: 5 GB x unlimited free Proton accounts. Bonus storage programs are separate and mostly paid-tier.
- reliability: Rclone backend is Beta and stated to have accounts it does not work with. Treat as best-effort, not infrastructure.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB free (starts at 2 GB, +3 GB welcome checklist within 30 days)
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Proton Free - Proton Drive - Proton Docs - Proton Sheets - 5 GB'
  - [2] 2026-10-21: 'unlock an extra 3 GB of Drive storage... we'll upgrade your storage from 2 GB to 5 GB' within 30 days
  - [3] 2026-10-21: 'added in v1.64.0 [Tier 4]... This backend is currently in Beta'
- sources:
  - [1] https://proton.me/drive/pricing
  - [2] https://proton.me/support/more-storage-proton-drive
  - [3] https://rclone.org/protondrive/

## proton mail free

- `storage/proton-mail-free` | fails-quota | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:26.604Z (live) | stale on 2026-12-04
- url https://proton.me/mail/pricing
- free tier: None reachable: 1 GB storage only ("Proton Free. 1 GB storage"), and the programmatic path is paywalled: "Proton Mail Bridge is currently available only with a paid Proton Mail plan." Zero-access encryptio. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: unverified: the pricing page lists no egress allowance or price; Proton Free caps storage at 1 GB | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: vendor pages captured 2026-11-03: https://proton.me/mail/pricing; every field that decides the verdict cites one of these captures
- extras:
  - dead_end.failure_class: read-gated
  - dead_end.why: 1 GB storage only ("Proton Free — 1 GB storage"), and the programmatic path is paywalled: "Proton Mail Bridge is currently available only with a paid Proton Mail plan." Zero-access…
  - dead_end.retry_when: if the read path opens anonymously
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 1 GB storage only ("Proton Free — 1 GB storage"), and the programmatic path is paywalled: "Proton Mail Bridge is currently available only with a paid Proton Mail plan." Zero-access…
  - [2] 2026-10-21: cited as the basis of the rejection: 1 GB storage only ("Proton Free — 1 GB storage"), and the programmatic path is paywalled: "Proton Mail Bridge is currently available only with a paid Proton Mail plan." Zero-access encryptio
  - [1] 2026-11-03: Proton Free has up to 1 GB of storage; the pricing page lists no egress allowance or price | capture: sha256:ec55f6d26f60feaa19349d15415314960ce78be0296bc3e570b75267ebbb5636 | quote: | Storage | Up to 1 GB | 15 GB | 500 GB |
- sources:
  - [1] https://proton.me/mail/pricing
  - [2] https://proton.me/support/imap-smtp-and-pop3-setup
