# Folder Fort

> folderfort.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/folderfort/ | JSON https://fshy.ajam.dev/api/v1/entity/folderfort.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FolderFort — free tier + 2.0 pricing

- `storage/folderfort-free-tier-2-0-pricing` | fails-egress | evidence reported | binding write-gated | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://folderfort.com
- free tier: Free plan with encrypted storage, no card; '+25GB free' if you post a social-media review. Paid Personal from 100 GB; Business up to 2x storage in bandwidth. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Monthly bandwidth ALLOWANCE, not free: 'up to 10GB on the Free plan', 'your chosen storage size on Personal', 'up to 2x your storage on Business'. Frequently-accessed files are cached so some traffic doesn't count. | metered: yes
- identity: email | detail: email
- interface: rest, rclone
- limits:
  - write-gated (binding): review [1]
- limits note: Bandwidth is limited to 10 GB per month on the free plan.
- interface detail: rest
- tooling: API use is explicitly covered by the bandwidth allowance, implying a REST API; no rclone backend.
- composes with: Free tier is ~10 GB bandwidth/month. The bandwidth allowance, not storage, is the binding constraint and it is tiny.
- reliability: The StackSocial 2 TB lifetime listing (f/18179782, $109.97) now 404s. The lifetime SKU line has been retired in favour of 'Folder Fort 2.0' subscriptions. Bandwidth-metered model is the opposite of the egress-free requirement.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: Free plan with encrypted storage, no card; '+25GB free' if you post a social-media review. Paid Personal from 100 GB; Business up to 2x storage in bandwidth.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'up to 10GB on the Free plan ... up to 2x your storage on Business ... refreshes automatically every month', fetched 2026-10-21
  - [2] 2026-10-21: > 'Page Not Found'
- sources:
  - [1] https://folderfort.com/pricing
  - [2] https://www.stacksocial.com/sales/folderfort-2tb-cloud-storage-pro-plan-lifetime-subscription

## Folder Fort 2.0

- `storage/folder-fort-2-0` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.folderfort.com/pricing
- free tier: Free plan exists with no credit card, size not published on the pricing page; free-plan bandwidth is 10 GB/month. Paid Personal starts at 100 GB, Business 1 TB. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Metered by monthly bandwidth allowance: 'up to 10GB on the Free plan, your chosen storage size on Personal (starting at 100GB), and up to 2x your storage on Business'. API/SFTP/WebDAV traffic counts against it. | metered: yes
- identity: institution
- interface: s3, rest, webdav, sftp, rclone
- limits note: per-ip-shaping/request-rate: 10 GB/month bandwidth on free (covers upload, download, streaming, embedding, share links and API use); API credits on Classic accounts are annual ('1 GB = up to 2 credits free annually'); free plan storage not stated; Classic access ends 2026-11-16.
- interface detail: sftp / webdav / rest (rclone) / s3-style via FF Connect
- tooling: Rclone backend (documented), SFTP, WebDAV. Folderfort.com/sftp-webdav-rclone.
- composes with: If the free storage number were large this would be a genuine finding because rclone/SFTP/WebDAV are all supported and 'all users, regardless of plan, receive free SFTP access'. But free bandwidth is 10 GB/month, so even a 500 GB free bucket could not be read out. Multiplication by accounts multiplies 10 GB/month each.
- reliability: Platform is mid-migration: 'Classic access ends November 16, 2026', free tier has already been re-scoped once this year; SFTP was still 'load testing' per its own docs.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free plan exists with no credit card, size not published on the pricing page; free-plan bandwidth is 10 GB/month. Paid Personal starts at 100 GB, Business 1 TB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Yes. Sign up and you get free encrypted storage to try the platform — no credit card required', 'Every plan includes a monthly bandwidth allowance — up to 10GB on the Free plan ... up to 2x your storage on Business', 'Classic access ends November 16, 2026'
  - [2] 2026-10-21: 'All users, regardless of plan, receive free SFTP access', 'We are currently load testing our new SFTP connection option'
- sources:
  - [1] https://www.folderfort.com/pricing
  - [2] https://www.folderfort.com/sftp-webdav-rclone
