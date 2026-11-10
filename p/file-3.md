# File.AL

> file.al | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/file-3/ | JSON https://fshy.ajam.dev/api/v1/entity/file-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## File.AL

- `debrid/file-al` | qualifies-with-caveat | evidence documented | binding volume-quota | category file host (premium one-time, XFileSharing script) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://file.al/premium.html
- price USD 29.95 per month for 4 TB stored and 30 GB/day | parsed USD 7.49/TB-mo
- free tier: Registered free account: max upload 20 Gb, storage 1 TB, download volume '5 GB in 1 days', files deleted '30 days after last download'. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: Anonymous upload is weaker still: 1 GB/day of download volume against the registered 5 GB.
- per-object cap: Premium 100 Gb; Registered 20 Gb | bytes: 107374182400 | source: [1] | note: Quoted as 'Max upload file size' - the largest single file a client may upload.
- retention: Premium: 'Never'. Registered: '30 days after last download'. | days: 30 | source: [1] | note: The 30 days applies to the free registered tier; premium files are never deleted for inactivity.
- egress: Premium: 'Download volume 30 GB in 1 days'. Registered: 5 GB in 1 days. Anonymous: 1 GB in 1 days. Premium also adds download-accelerator support and resumable downloads. | metered: yes | free allowance: 5 GB/day registered, 1 GB/day anonymous | source: [1]
- identity: card | detail: Premium bought at $29.95 for 30 days. The page shows no payment-method list beyond the checkout button; 'Purchase Extra Traffic' is offered as a separate item.
- interface: unknown
- limits:
  - volume-quota (binding): 30 GB per day of download volume on premium [1]
  - per-object-cap: 100 GB per file premium, 20 GB registered [1]
  - volume-quota (binding): 1 TB storage registered, 4 TB premium [1]
- limits note: The three columns (Anon / Premium / Registered) are printed out of order in the vendor's table; the numbers above are read from the column labels.
- binding note: 30 GB/day is 900 GB in a 30-day month against the 1,024 GB 1 TiB of monthly transfer needs, so it fails by 12% before storage matters. The 4 TB archive can be filled but not drained.
- interface detail: Web upload with remote URL upload on premium. No API endpoint is published on the page read.
- tooling: Browser only as read; the host is on the PrimeLeech generator list at generator/fileal.html. No rclone backend found.
- composes with: 4 TB of storage with files kept forever is the largest archive-shaped offer in tested services, but 30 GB/day caps a month at about 900 GB, so it is an archive that cannot be emptied at speed.
- reliability: Anonymous downloads are capped at 1 GB a day, so an unregistered pull of a large file fails on volume rather than on a wait; a test file (100 Mb) is published for checking speed before paying.
- notes: The $99.95 year is $8.33 a month. 4 TB stored for $8.33 is the cheapest storage per euro in tested services, and the 30 GB/day drain is what makes it an archive rather than a workspace.
- evidence note: The three-column feature table and the three prices were read on the vendor premium page. The table's columns are unlabelled in the extracted text and were mapped by order; a second read of the rendered page would confirm the mapping.
- extras:
  - plans: 30 days $29.95; 90 days $59.95; 365 days $99.95
  - annual_effective_monthly: USD 8.33
  - supports_: download accelerators and resume on premium only
- evidence:
  - [1] 2026-10-23: the prices (30 days $29.95, 90 days $59.95, 365 days $99.95) and the feature table: Premium 100 Gb upload / 4 TB / 30 GB/day / never deleted; Registered 20 Gb / 1 TB / 5 GB/day / 30 days
- sources:
  - [1] https://file.al/premium.html
