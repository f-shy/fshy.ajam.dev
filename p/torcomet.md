# Torcomet

> torcomet.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/torcomet/ | JSON https://fshy.ajam.dev/api/v1/entity/torcomet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Torcomet

- `debrid/torcomet` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud torrent (HTTPS retrieval) | tier Limited (free)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:13.292Z (live) | stale on 2026-12-04
- url https://torcomet.com/
- free tier: Free plan 'Limited': 2 GB disk space, no file expiry, unlimited download speed; the page shows the slot count as 1 active slot in one tab and unlimited in the others. | unit: GB | metered on: stored-bytes | read on: 2026-11-03 | source: [1]
- per-object cap: The 2 GB disk bounds what one torrent can hold on the free plan; paid plans 100 GB and 500 GB. | source: [1]
- retention: No file expiry on any plan per the pricing page. | source: [1]
- egress: Unlimited download speed on every plan per the pricing page; the home page states a maximum of 1 Gbps. | metered: no | free allowance: 2 GB of disk, no expiry | source: [1]
- identity: email | detail: An account is required (JOIN NOW leads to a registration form); The registration form fields were not readable, so the email requirement is unverified.
- interface: unknown
- limits:
  - volume-quota (binding): free plan 2 GB disk; Standard 100 GB; Premium 500 GB [1]
  - request-rate: active slots: 1 on the free plan in one tab, 5 on Standard, 20 on Premium [1]
- binding note: Disk size is the metered limit on every plan; speed is stated as unlimited.
- interface detail: Web upload of a .torrent or magnet link, then an HTTPS download of the fetched files; no API is documented on the pages read.
- tooling: Browser only on the pages read.
- composes with: Fetch a torrent into the 2 GB free disk, download over HTTPS, delete, repeat; paid plans raise the disk to 100 GB or 500 GB.
- reliability: A third-party list reports the same free 2 GB and a $5.99 and $9.99 pair for the paid plans.
- notes: Billing period of the $5.99 Standard price is unverified; a third-party list gives it per month.
- evidence note: First-party pricing page; the three tabs on it are not labelled with their billing periods in the capture, so the period of each price is unverified.
- evidence:
  - [1] 2026-11-03: the free plan has 2 GB disk and no file expiry | capture: sha256:7b48d94995c57a17f6abe377fde0bb94febf111519ca3cfcaf31f4a0d14191b7 | quote: ### Limited Free - 2 GB Disk Space - No file Expiry - Unlimited Slots - Unlimited Download Speed
  - [1] 2026-11-03: the Standard plan shows a struck-out 9.99 and a current 5.99 | capture: sha256:7b48d94995c57a17f6abe377fde0bb94febf111519ca3cfcaf31f4a0d14191b7 | quote: ### Standard $9.99 $ 5 99
  - [1] 2026-11-03: the Standard plan has 100 GB disk and 5 active slots | capture: sha256:7b48d94995c57a17f6abe377fde0bb94febf111519ca3cfcaf31f4a0d14191b7 | quote: - 100 GB Disk Space - No file Expiry - 5 Active Slots
  - [2] 2026-11-03: the home page states a 1 Gbps maximum download speed | capture: sha256:60a651e1264d8a2e704dcb2d304ec3fa01045064ab3673b5eab5b4fc0ed6b182 | quote: Download your torrent file to your device like a normal file at a maximum speed upto 1GBPS
  - [3] 2026-11-03: the terms mention blocking an email address and an IP address on a closed account | capture: sha256:b719a8c688da8e1e0fdba9fb5962541fca7c7c1b20bd56813b7363c89e010997 | quote: We may block your email address and Internet protocol address to prevent further registration.
- sources:
  - [1] https://torcomet.com/pricing
  - [2] https://torcomet.com/
  - [3] https://torcomet.com/terms
