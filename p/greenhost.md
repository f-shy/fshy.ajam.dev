# greenhost

> greenhost.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/greenhost/ | JSON https://fshy.ajam.dev/api/v1/entity/greenhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## greenhost

- `storage/greenhost` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:42.832Z (live) | stale on 2026-12-04
- url https://greenhost.net/products/vps/
- free tier: none reachable: VPS-only, paid from EUR 7.89/month for 1 vCPU/1 GiB/10 GiB disk/1 TiB traffic; the 4 GiB/40 GiB tier is EUR 31.54/month with 4 TiB traffic, and extra disks are sold in increments. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: VPS-only from EUR 7.89/month; account creation requires a 1-cent payment for verification, so it is paid, not free storage.
- notes: VPS-only: smallest plan EUR 7.89/month (1 GiB RAM, 10 GiB disk, 1 TiB traffic); the 40 GiB disk tier is EUR 31.54/month. No free tier; disk is small and paid, so it is not a storage offer.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: VPS-shaped: €6.95 for 2 vCPU/4 GB/40 GB disk/10 TB traffic. The 10 TB traffic allowance is generous but 40 GB of disk makes it irrelevant as storage.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: VPS-shaped: €6.95 for 2 vCPU/4 GB/40 GB disk/10 TB traffic. The 10 TB traffic allowance is generous but 40 GB of disk makes it irrelevant as storage.
  - [1] 2026-11-19: the first-party VPS page lists the 40 GiB disk tier alongside a EUR 31.54/month price and 4 TiB/month data limit | capture: sha256:6829fcdc74cd129ce1fac2f42cdb34708d74036e3e521e917bfb58cfcb9df925 | quote: | Disk Storage | 40 GiB |
  - [1] 2026-11-19: the 40 GiB VPS tier costs EUR 31.54 per month | capture: sha256:6829fcdc74cd129ce1fac2f42cdb34708d74036e3e521e917bfb58cfcb9df925 | quote: | € 31.54 / month | |
  - [1] 2026-11-19: Greenhost requires a payment of 1 cent to verify an account, so it is not free | capture: sha256:6829fcdc74cd129ce1fac2f42cdb34708d74036e3e521e917bfb58cfcb9df925 | quote: On ordering you will first need to create an account and make a payment of 1 cent for verification purposes.
  - [1] 2026-11-19: the VPS page still lists data limits in TiB per month, consistent with a paid VPS rather than a storage offer | capture: sha256:6829fcdc74cd129ce1fac2f42cdb34708d74036e3e521e917bfb58cfcb9df925 | quote: | Data limit | 4 TiB / month |
- sources:
  - [1] https://greenhost.net/products/vps/
