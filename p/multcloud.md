# multi-cloud manager

> multcloud.com | Debrid, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/multcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/multcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MultCloud

- `debrid/multcloud` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud-to-cloud transfer service (not a file host) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://www.multcloud.com/price.html
- price USD 19.99 per 100 GB per month (about USD 199.90 per TB); USD 119/year unlimited | parsed USD 199.9/TB-mo
- free tier: Free: '5GB / Month' of data transfer, across 30+ cloud services, with 5 one-way/two-way sync modes and offline transfer. | unit: GB | metered on: uploaded-bytes | read on: 2026-10-23 | source: [1] | note: The 5 GB is transfer volume through MultCloud, not storage; MultCloud stores nothing of its own.
- per-object cap: not stated on the page read | source: [1]
- retention: not applicable: MultCloud moves bytes between accounts the user already owns and keeps no copy | source: [1]
- egress: Transfer is metered by volume through the service: free 5 GB/month, then 100 GB/month at $19.99. 'Offline transfer/sync/backup' is included even on free. | metered: yes | free allowance: 5 GB per month | price per TB: USD 19.99 per 100 GB per month, or USD 119 per year for unlimited | source: [1]
- identity: email | detail: A MultCloud account, then OAuth authorisation of each connected cloud. Payment by card, bank/wire transfer, check or invoice through CleverBridge.
- interface: rest, webdav
- limits:
  - volume-quota (binding): 5 GB per month free; 100 GB per month at $19.99; unlimited at $119/year [1]
- limits note: Offline transfer (a URL source rather than a cloud endpoint) is included on the free tier, which is the feature that overlaps the debrid topic.
- binding note: 5 GB a month free fails at 1 TiB by a factor of 200. The unlimited annual plan at $119 removes the byte counter, and the remaining limit is the provider list rather than a number.
- interface detail: A web console over 30+ providers, and it accepts WebDAV and FTP as endpoints among them. The 30+ list on the page includes Google Drive, Google Photos, Google Workspace, Dropbox, OneDrive, MEGA, Amazon S3, Box, pCloud, MediaFire, Putio, Backblaze, Yandex, Baidu, NAS, MySQL and Egnyte.
- tooling: Browser console plus scheduled sync jobs; no rclone backend and no public API was read. rclone covers the same ground for free with a local binary, which is the comparison this record exists to make.
- composes with: The only service in tested services that moves bytes between two clouds not administered here. The 'Putio' endpoint entry is the debrid-adjacent one: it can pull from a put.io account into another drive without a local machine in the path.
- reliability: Transfers run inside MultCloud's session, so each connected cloud's own rate limits and re-authorisation requirements break jobs silently; a revoked OAuth token stops a scheduled sync without an error the user sees.
- notes: At $19.99 per 100 GB the metered plan is one of the most expensive per byte in tested services; the $119 annual unlimited plan is the only sensible tier and it is still above a debrid subscription. rclone does the same job for nothing on a rented box, which is why this record is a comparison rather than a recommendation.
- evidence note: Every figure read from the vendor's own price page. An actual transfer would raise this to measured and would establish the real throughput.
- extras:
  - plans: 5 GB/month free; 100 GB/month $19.99; 1200 GB/year $59.99; Yearly Unlimited $119; Lifetime Unlimited $249
  - providers_supported: 30+
  - debrid_adjacent_endpoint: Putio
- evidence:
  - [1] 2026-10-23: '5GB / Month' free, '100GB / Month $19.99', '1200GB / Year $59.99', 'Yearly Unlimited $119', 'Lifetime Unlimited $249', and the 30+ service list including Putio, WebDav and Amazon S3
  - [2] 2026-10-23: the four products: cloud transfer, cloud sync, cloud backup, and remote/offline transfer
- sources:
  - [1] https://www.multcloud.com/price.html
  - [2] https://www.multcloud.com/

## multi-cloud manager guis (multcloud, and air cluster's own docs) as stripin

- `storage/multi-cloud-manager-guis-as-stripin` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:49.636Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/multcloud.md
- free tier: None reachable: They are transfer/copy schedulers between clouds, not capacity pools. MultCloud's own framing of the user request is telling — it answers 'how do I merge my cloud accounts' with a file-manag. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the first-party page states no per-object size cap; the product is a cloud-to-cloud transfer scheduler | note: not applicable
- retention: stated-absent: the first-party page states no a retention period; it is a transfer scheduler over cloud drives it does not itself hold
- egress: stated-absent: the first-party page states no egress terms for bytes it does not itself host | metered: no
- identity: email
- interface: browser
- interface detail: Web-based multi-cloud manager GUI; transfer, sync and schedule tasks across connected cloud drives
- tooling: not documented
- composes with: Chains existing cloud drives: integrates multiple cloud storage accounts into one platform and transfers or synchronizes files between them without downloading.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: They are transfer/copy schedulers between clouds, not capacity pools. MultCloud's own framing of the user request is telling — it answers 'how do I merge my cloud accounts' with a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: They are transfer/copy schedulers between clouds, not capacity pools. MultCloud's own framing of the user request is telling — it answers 'how do I merge my cloud accounts' with a…
  - [1] 2026-11-19: MultCloud is a transfer/management channel with no storage space of its own, not a capacity pool | capture: sha256:002823a6f603d1d9b887d4638ea5dd631f0f390f613cdb6c4e5dede603e3f755 | quote: MultCloud is like a cloud management channel and it does not have any storage space.
  - [2] 2026-11-19: the MultCloud first-party product page describes a cloud-to-cloud transfer and sync service | capture: sha256:a7c9cc115c90181ae02d0e46f04bb7cebe8f319da61e35301c5bbb3523d8318a | quote: Integrate all your cloud storage into a single platform and transfer and synchronize files seamlessly between cloud drives.
  - [2] 2026-11-19: the MultCloud first-party product page describes chaining between existing cloud drives | capture: sha256:a7c9cc115c90181ae02d0e46f04bb7cebe8f319da61e35301c5bbb3523d8318a | quote: Transfer files from one cloud to another without downloading
- sources:
  - [1] https://www.multcloud.com/helps.html
  - [2] https://www.multcloud.com/product
