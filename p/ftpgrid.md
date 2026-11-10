# crawl-scale free-host ftp hosts

> ftpgrid.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ftpgrid/ | JSON https://fshy.ajam.dev/api/v1/entity/ftpgrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## crawl-scale free-host ftp hosts (storage share, cloudtb, fbipool, octopusft

- `storage/crawl-scale-free-host-ftp-hosts-storage-share-cloudtb-fb` | paid-only | evidence documented | binding volume-quota | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:04:35.453Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/ftpgrid.md
- free tier: The only free allowance among these hosts is ftpGrid's 100 MB of FTP/SFTP/FTPS/SCP cloud storage; the others are priced plans. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | note: not applicable
- retention: not recorded
- egress: not recorded | metered: no
- identity: email | detail: ftpGrid free account: no credit card required, sign-up at its dashboard. Identity for the priced plans of the other hosts is unverified: behind a sign-up.
- interface: unknown
- limits:
  - volume-quota (binding): 100 MB free storage on the ftpGrid free account; plans that reach the need are priced [1]
- binding note: the only free allowance is 100 MB; every plan that reaches the need is a priced plan
- interface detail: not documented
- tooling: the same as interface detail
- composes with: Priced plans only; no free route to a multi-TB allowance. Hosted offers that reach 10 TB: Hetzner Storage Share NX31 and CloudTB Enterprise.
- reliability: unverified: no uptime, suspension or data-loss reports were read for these hosts
- notes: Priced plans: Hetzner Storage Share NX31 10 TB at EUR 27.39 per month excl. VAT; CloudTB Basic 100 GB $2 Per Month, Standard 1 TB $10 Per Month, Enterprise 10 TB $99 Per Month (billed quarterly, no file size limit); FBIPool Cloud Drive 10GB from Rs.24 per month, 1000 GB from Rs.897 per month; ftpGrid Enterprise 1000 Gb at EUR 299 / Month; Octopus FTP 3 UK 1 TB at GBP 150 /month. Free: ftpGrid 100 MB.
- evidence note: the vendor pages of the 2026-11-03 evidence rows were read and captured (https://ftpgrid.com/tutorials/ftpgrid-free-tier-overview/, https://www.cloudtb.com/us/, https://www.hetzner.com/storage/storage-share/, https://hosting.fbipool.com/cloud-drive.php, https://ftpgrid.com/pricing/, https://www.octopusftp.co.uk/); every field that decides the verdict cites one of those captures
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Every one is paid. Storage Share 1 TB is a paid Nextcloud plan; CloudTB is '100 GB / $2 per month'; FBIPool 'Starts at Only Rs.24 Per Month' for 10 GB; ftpgrid is usage-based. The 'free FTP
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: Every one is paid. Storage Share 1 TB is a paid Nextcloud plan; CloudTB is '100 GB / $2 per month'; FBIPool 'Starts at Only Rs.24 Per Month' for 10 GB; ftpgrid is usage-based. The 'free FTP
  - [1] 2026-11-03: the ftpGrid free account has 100 MB of storage | capture: sha256:b46e53b29912994243d0f49cb05c4511b6a3e3772ba75f2472237330465fef98 | quote: 100 MB free FTP/SFTP/FTPS/SCP cloud storage
  - [2] 2026-11-03: CloudTB prices its 10 TB Enterprise plan at $99 a month | capture: sha256:f8f2ffb96275875738bf4dd522fcd8fe2369aee207d6a0daa337eccc25c8bcfb | quote: ## $99 Per Month
  - [1] 2026-11-03: the ftpGrid free account needs no card | capture: sha256:b46e53b29912994243d0f49cb05c4511b6a3e3772ba75f2472237330465fef98 | quote: No credit card required
  - [3] 2026-11-03: Hetzner Storage Share NX31 is a 10 TB plan at EUR 27.39 a month excl. VAT | capture: sha256:be4e5b04b01c3bb3b41475bea75fb4630dacd1c4ca477560d38145b7c0f4fc19 | quote: NX31 max/mo. € 27.39 per month, excl. VAT € 0.0439 per hour, excl. VAT /hr Storage 10 TB
  - [4] 2026-11-03: FBIPool Cloud Drive 10GB starts at Rs.24 per month | capture: sha256:9564075df73db86e4d0fcbf8583fc0b2a20b5d464d25c2d8c474d9bc4053f423 | quote: Starts at ₹24 per month
  - [4] 2026-11-03: FBIPool Cloud Drive 1000GB starts at Rs.897 per month | capture: sha256:9564075df73db86e4d0fcbf8583fc0b2a20b5d464d25c2d8c474d9bc4053f423 | quote: Starts at ₹897 per month
  - [2] 2026-11-03: CloudTB Basic 100 GB is $2 per month | capture: sha256:f8f2ffb96275875738bf4dd522fcd8fe2369aee207d6a0daa337eccc25c8bcfb | quote: ## $2 Per Month
  - [5] 2026-11-03: ftpGrid Enterprise (1000 Gb storage) is EUR 299 per month | capture: sha256:6648efbb878fb02cba3e64769afe89660c77374cdfb84e43127ed30562cac7fb | quote: €299 / Month
  - [6] 2026-11-03: Octopus FTP 3 UK, 1 TB storage, is GBP 150 per month | capture: sha256:01c5f764f91004d66dec67a1dc96aea98c21158276fcc05c2f1c2edf9bb1f284 | quote: £ 150 /month
- sources:
  - [1] https://ftpgrid.com/tutorials/ftpgrid-free-tier-overview/
  - [2] https://www.cloudtb.com/us/
  - [3] https://www.hetzner.com/storage/storage-share/
  - [4] https://hosting.fbipool.com/cloud-drive.php
  - [5] https://ftpgrid.com/pricing/
  - [6] https://www.octopusftp.co.uk/
