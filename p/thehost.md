# TheHost.ua KeepData

> thehost.ua | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thehost/ | JSON https://fshy.ajam.dev/api/v1/entity/thehost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TheHost.ua KeepData — 10 TB flat with traffic included, WebDAV/SFTP/Samba

- `storage/thehost-ua-keepdata-10-tb-flat-with-traffic-included-web` | qualifies | evidence reported | binding per-ip-shaping | category storage-vps-managed-nas
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.thehost.ua/en/hosting/cloud-storage
- price $5.95/TB/mo at 10 TB ($59.48/mo) and identically at 50 TB ($297.48/mo) — flat rate, unmetered traffic, no volume discount at either end. Tier ladder is 25 GB / 100 GB / 500 GB / 1 TB / 10 TB / 50 TB, so there is NO 5 TB SKU: 5 TB means buying 5× the 1 TB plan ($64.15/mo = $12.83/TB/mo, poor) or… | parsed USD 5.95/TB-mo
- free tier: 25 GB / 100 GB / 500 GB / 1 TB / 10 TB / 50 TB. 10 TB = $59.48/mo, or $642.34/yr (10 % discount), or $1,141.90 for 2 years (20 %). Also sold in UAH and EUR on the same table (2,499 ₴ / €49.98 / $59.48 per month for 10 TB). Inodes: 1,000 K at 10 TB. 7-day free trial on every tier. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Included and unmetered. The traffic row reads simply «Traffic», with access speed «10 Gbit/s», and there is no meter, overage rate or traffic pack anywhere on the page. This is a dedicated-rail storage product, not metered object storage. | metered: no
- identity: card | detail: card
- interface: webdav, sftp, ftps, ftp, rsync, rclone
- limits:
  - per-ip-shaping (binding): 10 Gbit/s [1]
- limits note: Not S3. No bucket API, no presigned URLs, so CDN/CF fronting has to go through WebDAV or an rclone `serve` layer. Inode ceilings matter for a 20 TiB corpus of small files: 1,000 K inodes at 10 TB is 1 M files, which a dataset archive of many small parquet/JSON shards will exhaust long before 10 TB. Per-file size not published on the pricing page.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: webdav + sftp + ftp
- tooling: FTP, FTPS, SFTP, WebDAV (mounts as a network drive on Windows/macOS), plus BorgBackup / Restic / rsync / rclone over SFTP. Double redundancy across two physical datacentres in different cities. Auto-delete rules for camera/stream ingest.
- composes with: Sizing is by purchased volume, so 5 TB → 2× and 20 TB → 2× the 10 TB plan, both at the same per-TB rate. No account multiplication needed.
- reliability: Ukrainian operator (Kyiv), billing in UAH/EUR/USD with card. The 10 Gbit/s claim and the double-redundancy claim are the vendor's own and were not independently benchmarked here. Treat throughput as unverified. The 7-day trial is real and is the right way to test before committing 20 TiB.
- notes: the same as the free tier
- extras:
  - price_verbatim: $5.95/TB/mo at 10 TB ($59.48/mo) and identically at 50 TB ($297.48/mo) — flat rate, unmetered traffic, no volume discount at either end. Tier ladder is 25 GB / 100 GB / 500 GB / 1 TB / 10 TB / 50 TB, so there is NO 5 TB SKU: 5 TB means buying 5× the 1 TB plan ($64.15/mo = $12.83/TB/mo, poor) or 1× the 10 TB plan and using half of it ($5.95/TB/mo paid, $11.90/TB/mo effectively). 20 TB = 2× the 10 TB plan at $119/mo (derived; confirm they allow a second unit). At 1 TB the rate is $12.83/TB/mo, so buying the 10 TB tier is 2.16× cheaper per terabyte than buying the 1 TB tier.
- evidence:
  - [1] 2026-10-21: word count 3399. 10 T tier: «10000» GB, «1000» K inodes, traffic «Traffic», «10 Gbit/s», cost «1 month 2499 49.98 59.48»; «1 year 26989 539.78 642.34 Discount 10 %»; «2 years 47979 959.58 1141.9 Discount 20 %»
  - withheld 2026-10-21: same page, 1 T tier: «1 month 539 10.78 12.83» USD; 50 T tier «12499 249.98 297.48» — confirming the per-TB rate is flat at $5.95 from 10 TB upward and $12.83 at 1 TB
  - withheld 2026-10-21: same page — «Support for popular access protocols … SFTP, FTP, FTPS and WebDav», «double redundancy at the storage server level», «data is stored in two copies, located in different physical data centers in various cities», «Free trial period» / «Try for free for 7 days»
- sources:
  - [1] https://www.thehost.ua/en/hosting/cloud-storage
