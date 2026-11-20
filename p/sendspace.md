# SendSpace

> sendspace.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sendspace/ | JSON https://fshy.ajam.dev/api/v1/entity/sendspace.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SendSpace

- `debrid/sendspace` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file host (free Lite, paid Pro plans) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://www.sendspace.com/
- free tier: Free sendspace Lite: files up to 300 MB (split files allowed), no registration needed, ad-supported, kept while downloaded at least once every 30 days. | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 300 MB per file on Lite; 5 GB on Pro Base; 10 GB on Pro Plus and Business | source: [1]
- retention: a file becomes inactive when not downloaded at least once in a 30 day period; Premium files are not deleted when inactive | days: 30 | source: [1]
- egress: Pro Base includes 100 GB of recipient bandwidth a month; Pro Plus 300 GB; Business 500 GB. No free recipient bandwidth figure is published on the pages read. | metered: yes | free allowance: not published | source: [2]
- identity: anonymous | detail: No registration and no email address are needed to upload; registration is optional and free.
- interface: rest
- limits:
  - per-object-cap (binding): 300 MB per file on Lite, split files allowed; 5 GB on Pro Base [1]
  - retention-clamped: a file becomes inactive after 30 days without a download [1]
  - volume-quota: 100 GB of recipient bandwidth a month on Pro Base [2]
- binding note: The 300 MB per-file ceiling on the free tier is the first limit; it only moves with a paid plan.
- interface detail: Web upload; a PDF user guide is linked from the FAQ. No API page was read.
- tooling: Browser upload; no API or client documented on the pages read.
- composes with: Pro Base is $9 for 1 month (5 GB per file, 100 GB of recipient bandwidth a month); a 12-month Pro Base is $89.
- reliability: Long-running host; no status page was read.
- notes: Cheapest paid tier is Pro Base at $9 for one month.
- evidence note: Limits and prices read on the vendor FAQ and upgrade pages.
- evidence:
  - [1] 2026-11-03: the free per-file limit is 300 MB | capture: sha256:7f39131a4bacc279fc7767fd160c5a31cdc9c1fa054c4e5d438e9c0206e31feb | quote: As long as the file size is less than the file size limit (300MB - split files allowed)
  - [1] 2026-11-03: upload needs no account | capture: sha256:7f39131a4bacc279fc7767fd160c5a31cdc9c1fa054c4e5d438e9c0206e31feb | quote: You do not need to register to use ***send*space**.
  - [1] 2026-11-03: inactivity is 30 days without a download | capture: sha256:7f39131a4bacc279fc7767fd160c5a31cdc9c1fa054c4e5d438e9c0206e31feb | quote: A file becomes inactive if it has not been downloaded at least once during a 30 day period.
  - [2] 2026-11-03: the cheapest paid plan is $9 for one month with 100 GB of recipient bandwidth | capture: sha256:d7eb5b102bed4d298caeef80519948ae9d1ec3699b7eb27b27a3ca1133208c13 | quote: Pro Base 1 Month @ $9 includes 100GB recipient bandwidth a month.
  - [2] 2026-11-03: Pro Base allows 5 GB per file | capture: sha256:d7eb5b102bed4d298caeef80519948ae9d1ec3699b7eb27b27a3ca1133208c13 | quote: Upload and send files up to 5 GB each
- sources:
  - [1] https://www.sendspace.com/faqs.html
  - [2] https://www.sendspace.com/premium_upgrade.html
