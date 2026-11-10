# MultCloud

> multcloud.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

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
