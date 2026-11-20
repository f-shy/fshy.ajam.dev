# TransferCloud.io

> transfercloud.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/transfercloud/ | JSON https://fshy.ajam.dev/api/v1/entity/transfercloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TransferCloud.io

- `debrid/transfercloud` | fails-quota | evidence documented | binding per-object-cap | category torrent/NZB/URL fetcher that writes into the user's own cloud drive | tier free
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T01:56:00.000Z (live) | stale on 2026-11-23
- url https://www.transfercloud.io/
- price USD 0 free; from USD 3.99/month paid | parsed USD 3.99/mo
- free tier: Free account: 'You can download any amount of files less than 1.5 GB!' with 'Unlimited Speed/Transfers'. | unit: requests | metered on: object-count | read on: 2026-10-23 | source: [1] | note: unlimited count with a 1.5 GB per-file ceiling
- per-object cap: 1.5 GB per file on the free account; paid caps are not stated on the page read. | bytes: 1500000000 | source: [1]
- retention: The retrieved file is written into the user's own cloud account (Google Drive, Dropbox, OneDrive, Mega, pCloud, Amazon S3 and '25+ more'), so retention follows that account. No server-side retention figure is published. | source: [1] | note: the vendor's own copy is transient; the durable copy is the destination account
- egress: 'Unlimited Speed/Transfers' on the free account; no byte allowance is published on any plan. Egress to the user happens from the destination cloud, not from TransferCloud. | metered: no | free allowance: not applicable: egress is billed by the destination cloud | source: [1]
- identity: card | detail: free account is an email plus a connected cloud account; paid plans from $3.99/month need a card.
- interface: rest
- limits:
  - per-object-cap (binding): 1.5 GB per file on the free account [1]
- limits note: plans start at $3.99/month but the paid per-file cap, job count and speed are not published on the landing page; the only numbers are the free 1.5 GB and the entry price.
- binding note: 1.5 GB rejects the 20 GiB case at the free tier, and the paid cap that would allow it is unpublished, so the record cannot say what the paid ceiling is.
- interface detail: web UI plus OAuth connections to 25+ cloud destinations; native FTP/SFTP/WebDAV pulls are also supported. No public API is documented on the page read.
- tooling: browser; the destination cloud supplies the programmatic path (rclone, Drive API).
- composes with: one hop that lands a torrent in an existing free drive, so the storage problem is solved by a service already held; it also takes NZB, which makes it the cheapest way to move a usenet download into Drive.
- reliability: the service inherits every failure of the destination cloud's OAuth and quota, and a 1.5 GB free cap means large torrents are impossible without paying.
- notes: The strongest 'writes into your own drive' option read in the sector, because it covers 25+ destinations and NZB as well as torrents. The free tier is capped at 1.5 GB per file, which is the same wall as every other free tier here.
- evidence note: the free-account sentence and the destination list were read. Paid limits and retention are unpublished.
- extras:
  - destinations: 25+ including Google Drive, Dropbox, OneDrive, Mega, pCloud, S3
  - usenet: NZB accepted
- evidence:
  - [1] 2026-10-23: 'Get a FREE account! - You can download any amount of files less than 1.5 GB!', 'Unlimited Speed/Transfers', destinations including Google Drive, Dropbox, OneDrive, Mega, pCloud and S3, NZB support, and 'Plans from $3.99/mo'
- sources:
  - [1] https://www.transfercloud.io/
