# NetDynamics24 Germany Backup SFTP

> netdynamics24.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/netdynamics24/ | JSON https://fshy.ajam.dev/api/v1/entity/netdynamics24.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NetDynamics24 Germany Backup SFTP (LET50% recurring)

- `storage/netdynamics24-germany-backup-sftp` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category backup storage / SFTP box (RAID-6, Enterprise HDD)
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.netdynamics24.com/client/order.php?step=1&productGroup=13
- price List: $6.00/TB/mo at 1 TB, $5.50/TB/mo at 2 TB. With LET50% on annual: 1 TB = $30/yr = $2.50/TB/mo; 2 TB = $55/yr = $2.29/TB/mo. at 5 TB: three 2 TB boxes = $2.29/TB/mo. at 20 TB: same $2.29/TB/mo but requires ten boxes. Unmetered 1 Gbit/s is the reason to care. | parsed USD 2.29/TB-mo
- free tier: 250 GB $3/mo · 500 GB $4/mo · 1 TB $6/mo · 2 TB $11/mo. Germany (Falkenstein) and Finland (Helsinki) sold as separate product groups. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: "Unmetered Traffic" with "1 GBit/s" port, on both the DE and FI product pages. This is the cleanest egress term among the records read. A port speed with no counter and no published fair-use threshold. | metered: no
- identity: email | detail: email
- interface: s3, webdav, ftp, rsync, ssh
- limits:
  - per-ip-shaping (binding): 1 Gbit/s [1]
- limits note: WebDAV and S3 protocols are not supported. Storage plans cap at 2 TB per server instance.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: (S)FTP, SSH, rsync, BorgBackup, control panel
- tooling: rsync/Borg/restic over SSH. No S3, no WebDAV.
- composes with: Archive/backup leg only. No object API means it cannot serve the hot set or back a Cloudflare origin directly.
- reliability: Hosting provider advertises 256 GB RAM Xeon E5-1650v3 storage nodes with RAID-6 arrays and unmetered 1 Gbit/s network links. Promotional discounts are reported on hosting forums but unverified at checkout without placing an order.
- notes: the same as the free tier
- extras:
  - price_verbatim: List: $6.00/TB/mo at 1 TB, $5.50/TB/mo at 2 TB. With LET50% on annual: 1 TB = $30/yr = $2.50/TB/mo; 2 TB = $55/yr = $2.29/TB/mo. at 5 TB: three 2 TB boxes = $2.29/TB/mo. at 20 TB: same $2.29/TB/mo but requires ten boxes. Unmetered 1 Gbit/s is the reason to care.
- evidence:
  - [2] 2026-10-21: 
  - [1] 2026-10-21: 
  - [3] 2026-10-21: "Please check our Storage plans: ... and use the coupon code: LET50% to get a recurring annual 50% discount" (NetDynamics24 Host Rep account)
- sources:
  - [1] https://www.netdynamics24.com/client/order.php?step=1&productGroup=13
  - [2] https://netdynamics24.com/backup-services.php
  - [3] https://lowendtalk.com/discussion/209856/looking-for-1tb-for-restic
