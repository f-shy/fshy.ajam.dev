# PulsedMedia

> pulsedmedia.com | Storage; 6 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pulsedmedia/ | JSON https://fshy.ajam.dev/api/v1/entity/pulsedmedia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PulsedMedia M10G Storage Box (16 TB)

- `storage/pulsedmedia-m10g-storage-box` | qualifies | evidence documented | binding per-ip-shaping | category storage VPS / storage box (HDD, RAID5)
- needs card no, phone no, ID no, institution no | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://pulsedmedia.com/storage-boxes.php
- price €1.69/TB/mo at the 16 TB tier (€26.99/16). at 5 TB: buy the 8 TB tier = €1.87/TB/mo. at 20 TB: buy the 32 TB tier = €2.00/TB/mo. ~$1.83 / $2.02 / $2.16 at 1.08 USD/EUR. Black Friday flash (8 TB, recurring, 15 units) = €1.02/TB/mo. | parsed USD 1.9/TB-mo
- free tier: 4 / 8 / 16 / 32 TB tiers. 16 TB = €26.99/month, monthly billing. 32 TB = €63.99/month. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: "Internet egress: Unlimited@100Mbps (~30TB/Month / ~1TB/Day)" + "Burst egress: 10Gbps 500GiB/month" + "DC internal: Unlimited at 10Gbps" + "Ingress: Unlimited at 10Gbps". This is the honest form of unmetered: the cap is a 100 Mbit/s port, not a byte counter, and the vendor states the implied monthly figure (~30 TB). The 10 Gbps burst allowance IS a real 500 GiB/month counter. | metered: no | free allowance: 30TB per month
- identity: email | detail: email
- interface: s3, webdav, sftp, ftp, scp, rsync, ssh, rclone
- limits:
  - per-ip-shaping (binding): 100 Mbps sustained internet egress; 10 Gbps burst capped at 500 GiB/month [1]
- limits note: CPU/IO fair-use (0.5-1 core, standard IO priority). RAID5 survives one drive. 25% burst quota above allocation; bonus disk grows with account age. Live fleet stats published (median 25.7 users/server, 37.1 ms disk response, 24.1% disks busy). Unusually honest disclosure.
- interface detail: SFTP, SCP, FTP(S), rsync, WebDAV, HTTP(S), SSHFS, SSH, Docker rootless, BorgBackup, Restic, rclone
- tooling: rclone as a plain SFTP/WebDAV destination; Borg and Restic preinstalled; full rclone serve s3 / MinIO possible via docker rootless
- composes with: Pools cleanly behind AList/OpenList (WebDAV) or rclone serve s3, then Cloudflare. Same-datacenter transfers to a PulsedMedia seedbox run 70-75 MB/s, so the hot/cold split (hot on seedbox NVMe, cold here) is a native pattern.
- reliability: Finnish own hardware (Helsinki Lauttasaari, Kerava). V-series is RAID0. Pick M-series. Not a hyperscaler; a one-shop provider.
- notes: the same as the free tier
- evidence note: The page states the number in the record; the claim is documented, not measured.
- extras:
  - price_verbatim: €1.69/TB/mo at the 16 TB tier (€26.99/16). at 5 TB: buy the 8 TB tier = €1.87/TB/mo. at 20 TB: buy the 32 TB tier = €2.00/TB/mo. ~$1.83 / $2.02 / $2.16 at 1.08 USD/EUR. Black Friday flash (8 TB, recurring, 15 units) = €1.02/TB/mo.
  - verified[0].url: https://pulsedmedia.com/storage-boxes.php
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 200
  - verified[0].bytes: 7273
  - verified[0].sha256: d54786f3b8bb4c9c28835ce0617bde66fe1948f33a2235ecee938a442d954fda
  - verified[0].pattern_found: yes
  - verified[0].what_changed: no change: the page still states the claim
- evidence:
  - [1] 2026-10-22: M10G is EUR 26.99 and the egress string is stated. Re-read https://pulsedmedia.com/storage-boxes.php: HTTP 200, 7273 bytes, sha256 d54786f3b8bb4c9c. Quoted: =1488 Available: 30 - [M10G STORAGE BOX 16TB](https://pulsedmedia.com/clients/cart.php?a=add&pid=309&billingcycle=annually&configoption[245]=1484&configoption[246]=1488) - 26.99€ monthly billing - 16TB Redundant RAID5 HDD Storage - 500MB RAM - 10Gbps Network - - SSH - SCP - SFTP - FTP(S) - HTTPS - HTTP - Public HTTP(S) - SSHFS - Rsync - Rclone - Restic - Borg backup -
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 
  - [3] 2026-10-21: 
- sources:
  - [1] https://pulsedmedia.com/storage-boxes.php
  - [2] https://wiki.pulsedmedia.com/wiki/Storage_Boxes
  - [3] https://lowendtalk.com/discussion/comment/4622106/

## PulsedMedia — M10G Storage Box 16TB

- `storage/pulsedmedia-m10g-storage-box-16tb` | qualifies | evidence reported | binding per-ip-shaping | category seedbox/storage-box hosting
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://pulsedmedia.com/storage-boxes.php
- price 16TB: €26.99 -> €1.69/TB/mo (~$1.94). 32TB: €63.99 -> €2.00/TB. 8TB: €14.99 -> €1.87/TB. 4TB: €8.99 -> €2.25/TB | parsed USD 1.9/TB-mo
- duplicate of `storage/pulsedmedia-m10g-storage-box`
- disagrees on verdict: `storage/pulsedmedia-eternal-v-in-m-inen-1-99-storage-tiers` says fails-egress, `storage/pulsedmedia-m10g-storage-box-16tb` says qualifies
- free tier: 16 TB HDD RAID5 (4/8/16/32 TB tiers) | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: "Internet egress: Unlimited@100Mbps (~30TB/Month / ~1TB/Day)" + "Burst egress: 10Gbps 500GiB/month" + "Ingress: Unlimited at 10Gbps". Genuinely unmetered, rate-shaped at 100 Mbps sustained (~1 TiB/day). Not a byte cap. | metered: no | free allowance: 30TB per month
- identity: email | detail: email
- interface: s3, sftp, ftp, scp, rsync, ssh, rclone
- limits:
  - per-ip-shaping (binding): 100 Mbps [1]
- limits note: 100 Mbps sustained egress; 500 MB RAM on storage boxes; RAID5 single-parity
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: SSH, SCP, SFTP, FTP(S), HTTPS, public HTTP(S), SSHFS, Rsync, Rclone, Restic, Borg, Docker (rootless), WireGuard/OpenVPN
- tooling: Rclone native, restic/borg native, plain SSHFS mount. No S3 endpoint.
- composes with: Supports SSHFS and rclone mounts, allowing integration with frontend distribution layers. A sustained 100 Mbps link provides up to approximately 1.08 TB per day.
- reliability: Own DC in Finland, 15+ yrs operating; storage-box tier is 500 MB RAM so Nextcloud-on-box is impractical. Use it as a filesystem only.
- notes: 16 TB HDD RAID5 configuration within the M10G Storage Box product line, offering 4, 8, 16, and 32 TB tiers.
- extras:
  - price_verbatim: 16TB: €26.99 -> €1.69/TB/mo (~$1.94). 32TB: €63.99 -> €2.00/TB. 8TB: €14.99 -> €1.87/TB. 4TB: €8.99 -> €2.25/TB
  - duplicate_of: pulsedmedia-m10g-storage-box
  - duplicate_note: The same 16 TB tier of one product line. The vendor page read 2026-10-22 lists four tiers under one name, 'M10G STORAGE BOX 4TB / 8TB / 16TB / 32TB', at EUR 8.99 / 14.99 / 26.99 / 63.99, all on the same 500 MB RAM, 10 Gbps, RAID5 platform. There is no second 16 TB SKU and no non-16 TB record of this product. The canonical record is pulsedmedia-m10g-storage-box: same product, rung documented rather than reported, and it carries the port limit this record also names.
  - count_note: this record duplicates pulsedmedia-m10g-storage-box; a count over the directory includes the one offer twice
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: M10G seedbox ladder for comparison (2TB 8.99€ ... 12TB 24.99€)
  - [3] 2026-10-21: ... — provider states "Payments are Paypal and Crypto", 14-day moneyback (campaign thread)
- sources:
  - [1] https://pulsedmedia.com/storage-boxes.php
  - [2] https://pulsedmedia.com/m10g-seedbox.php
  - [3] https://lowendspirit.com/discussion/10922/

## PulsedMedia Free Seedbox Trial (Helsinki)

- `storage/pulsedmedia-free-seedbox-trial` | trial-only | evidence reported | binding per-ip-shaping | category iaas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://pulsedmedia.com/free-seedbox.php
- free tier: 50 GiB storage, 250 MB RAM, 200 GiB torrent traffic, 1 Gbps, for 30 days, free. 'Free Seedbox Trial 30 Days — FREE!!!! Free like Free Speech! — 50 GiB Storage'. | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Retention: 30-day trial only. The binding clause. | days: 30 | source: [1] | note: not stated
- egress: Included in the 200 GiB torrent traffic allowance; no per-GB charge stated. | metered: yes
- identity: card | detail: inferred from the category 'iaas'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: sftp, ssh, rclone
- limits:
  - per-ip-shaping (binding): 1 Gbps [1]
- limits note: Per-object-cap: none stated. Request-rate: n/a (SSH). Retention: 30-day trial only. The binding clause. Traffic: 200 GiB/month.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: sftp
- tooling: RTorrent + ruTorrent/Deluge/qBittorrent web UI, SSH, SFTP, Docker rootless, Jellyfin media stack, WireGuard/OpenVPN. SFTP is the storage transport. Usable by rclone's `sftp` backend.
- composes with: Real but weak: 50 GiB x N accounts, and each trial is 30 days, so the chain has to be re-established monthly. Not a storage tier; a way to test throughput before buying the EUR 1.99/mo 230 GiB plan.
- reliability: Trial-only by construction, and the parallel paid 'M1000 SSD 230G' plan shows 'Available: 0', so capacity is genuinely constrained, not artificially so.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 50 GiB storage, 250 MB RAM, 200 GiB torrent traffic, 1 Gbps, for 30 days, free. 'Free Seedbox Trial 30 Days — FREE!!!! Free like Free Speech! — 50 GiB Storage'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free Seedbox Trial 30 Days ... 50 GiB Storage ... 200 GiB Torrent traffic'; paid 230 GiB SSD plan listed at 'Available: 0'
- sources:
  - [1] https://pulsedmedia.com/free-seedbox.php

## PulsedMedia Storage Boxes — 4 TB at €8.99/mo + a genuinely free 50 GiB/30-day box

- `storage/pulsedmedia-storage-boxes-4-tb-at-8-99-mo-a-genuinely-fr` | paid-only | evidence documented | binding per-ip-shaping | category iaas
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:04:13.394Z (live) | stale on 2026-12-04
- url https://pulsedmedia.com/storage-boxes.php
- free tier: A separate free seedbox lasts 30 days with 50 GiB storage and 200 GiB torrent traffic, one per customer, and showed 'Available: 0'. Storage Boxes are paid (see notes). | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Internet egress is unlimited at 100 Mbps (about 30 TB per month, 1 TB per day) plus 10 Gbps burst of 500 GiB per month; ingress is unlimited at 10 Gbps. | metered: no
- identity: email | detail: email
- interface: webdav, sftp, ftp, scp, ssh, rclone
- limits:
  - per-ip-shaping (binding): 100 Mbps (about 30 TB per month, 1 TB per day) [1]
- limits note: Free seedbox: 50 GiB storage, terminates after 30 days, 200 GiB torrent traffic, 'Available: 0' at read time. Paid boxes are shaped by internet egress (see limits).
- binding note: internet egress is shaped to 100 Mbps, about 30 TB per month or 1 TB per day, on every Storage Box size
- interface detail: sftp
- tooling: SSH, SCP, SFTP, FTP(S), HTTPS. Docker rootless means you can run rclone or a WebDAV server inside it.
- composes with: The free box is explicitly one-per-customer with a newsletter signup as the price ('Signing up for FREE Seedbox you enroll to marketing newsletter maximum twice per month'; 'Only 1 Seedbox per user!'). Not stackable. The provider says outright that the guardrails exist because 'a free seedbox is catnip for spammers and ratio-cheaters', which in plain terms means the free box attracts users who take more than it is meant for.
- reliability: Own hardware in Finland at two datacenters, Lauttasaari (Helsinki) and Kerava. The free seedbox is rationed to one per customer with limited slots. unverified: tenure of the host.
- notes: Paid Storage Boxes (RAID5 HDD): 4 TB 8.99 EUR per month, 8 TB 14.99 EUR, 16 TB 26.99 EUR, 32 TB 63.99 EUR; a separate free 30-day seedbox exists.
- evidence note: vendor pages captured 2026-11-03: https://pulsedmedia.com/storage-boxes.php, https://pulsedmedia.com/free-seedbox.php; every field that decides the verdict cites one of these captures
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Storage Boxes from 4 TB (€8.99/mo, RAID5) to 32 TB. Separately, a FREE 30-day seedbox: 50 GiB storage, 250 MB RAM, 200 GiB torrent traffic, SSH + SFTP + Docker rootless.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Free Seedbox Trial 30 Days … 50 GiB Storage … 200 GiB Torrent traffic … Terminates after 30 Days … Available: 0'; 'one per customer, limited slots, and you're signed up to our newsletter'
  - [1] 2026-10-21: 'M10G STORAGE BOX 4TB … 8.99€ … 4TB Redundant RAID5 HDD Storage … Unlimited bandwidth at 100Mbps plus 10Gbps burst'
  - [1] 2026-11-03: the 32 TB Storage Box (M10G STORAGE BOX 32TB card) costs 63.99 EUR per month | capture: sha256:b02b3f6960e56388e5200bb7c4e92a12f013b9686a0d5c6d44422cd6e3f15902 | quote: - 63.99€
  - [2] 2026-11-03: the free seedbox has 50 GiB storage | capture: sha256:6a736a46bfda2d8a49ddb431a9d107d6ee76d57f7180de4eb6f0a966915fb54b | quote: - 50 GiB Storage
  - [1] 2026-11-03: internet egress is unlimited at 100 Mbps, about 30 TB per month or 1 TB per day | capture: sha256:b02b3f6960e56388e5200bb7c4e92a12f013b9686a0d5c6d44422cd6e3f15902 | quote: - Internet egress: Unlimited@100Mbps (~30TB/Month / ~1TB/Day)
  - [2] 2026-11-03: the free seedbox has 200 GiB torrent traffic | capture: sha256:6a736a46bfda2d8a49ddb431a9d107d6ee76d57f7180de4eb6f0a966915fb54b | quote: - 200 GiB Torrent traffic
  - [1] 2026-11-03: own hardware in Finland at two datacenters | capture: sha256:b02b3f6960e56388e5200bb7c4e92a12f013b9686a0d5c6d44422cd6e3f15902 | quote: Your data lives on our own hardware in Finland, one of the strongest privacy jurisdictions in the world. Two datacenter locations: Lauttasaari (Helsinki) and Kerava.
  - [1] 2026-11-03: the 4 TB Storage Box (M10G STORAGE BOX 4TB card) costs 8.99 EUR per month | capture: sha256:b02b3f6960e56388e5200bb7c4e92a12f013b9686a0d5c6d44422cd6e3f15902 | quote: - 8.99€
  - [1] 2026-11-03: the 8 TB Storage Box costs 14.99 EUR per month | capture: sha256:b02b3f6960e56388e5200bb7c4e92a12f013b9686a0d5c6d44422cd6e3f15902 | quote: - 14.99€
  - [1] 2026-11-03: the 16 TB Storage Box costs 26.99 EUR per month | capture: sha256:b02b3f6960e56388e5200bb7c4e92a12f013b9686a0d5c6d44422cd6e3f15902 | quote: - 26.99€
  - [1] 2026-11-03: a Storage Box TB is 910 GiB | capture: sha256:b02b3f6960e56388e5200bb7c4e92a12f013b9686a0d5c6d44422cd6e3f15902 | quote: Diskspace in TB is multiples of 910 GiB.
  - [2] 2026-11-03: the free seedbox ends after 30 days | capture: sha256:6a736a46bfda2d8a49ddb431a9d107d6ee76d57f7180de4eb6f0a966915fb54b | quote: - Terminates after 30 Days
  - [2] 2026-11-03: no free seedbox slots were available at read time | capture: sha256:6a736a46bfda2d8a49ddb431a9d107d6ee76d57f7180de4eb6f0a966915fb54b | quote: Available: 0
  - [2] 2026-11-03: one free box per customer, limited slots, newsletter sign-up | capture: sha256:6a736a46bfda2d8a49ddb431a9d107d6ee76d57f7180de4eb6f0a966915fb54b | quote: one per customer**, limited slots, and you're signed up to our newsletter (max twice a month)
- sources:
  - [1] https://pulsedmedia.com/storage-boxes.php
  - [2] https://pulsedmedia.com/free-seedbox.php

## pulsedmedia — 'eternal väinämöinen' €1.99 storage tiers

- `storage/pulsedmedia-eternal-v-in-m-inen-1-99-storage-tiers` | fails-egress | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:39.699Z (live) | stale on 2026-12-04
- url https://pulsedmedia.com/eternal-vainamoinen.php
- disagrees on verdict: `storage/pulsedmedia-eternal-v-in-m-inen-1-99-storage-tiers` says fails-egress, `storage/pulsedmedia-m10g-storage-box-16tb` says qualifies
- free tier: none reachable: The headline €0.83-1.00/TB prices carry egress quotas an order of magnitude below storage: 'Storage 2TB R5 1G' is €1.99/mo for 2 TB with 268 GB/month traffic; 'Storage 4TB R5 10G' €3.99 for | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Storage 2TB R5 1G (1.99 EUR / month, 2 TB) includes 250 GiB traffic a month; Storage 4TB R5 10G (3.99 EUR / month, 4 TB) includes 500 GiB traffic a month. 1 TiB a day is not reachable. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: vendor pages captured 2026-11-03: https://pulsedmedia.com/eternal-vainamoinen.php; every field that decides the verdict cites one of these captures
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: The headline €0.83-1.00/TB prices carry egress quotas an order of magnitude below storage: 'Storage 2TB R5 1G' is €1.99/mo for 2 TB with 268 GB/month traffic; 'Storage 4TB R5 10G' €3.99 for
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The headline €0.83-1.00/TB prices carry egress quotas an order of magnitude below storage: 'Storage 2TB R5 1G' is €1.99/mo for 2 TB with 268 GB/month traffic; 'Storage 4TB R5 10G' €3.99 for
  - [1] 2026-11-03: the 2 TB storage tier (1.99 EUR / month) includes 250 GiB of traffic a month | capture: sha256:98d79f56e908ea2fdff07f7d75b794a8f83d079ac9f35b978624d48e7935f269 | quote: - 250 GiB traffic/mo
  - [1] 2026-11-03: the 4 TB storage tier (3.99 EUR / month) includes 500 GiB of traffic a month | capture: sha256:98d79f56e908ea2fdff07f7d75b794a8f83d079ac9f35b978624d48e7935f269 | quote: - 500 GiB traffic/mo
- sources:
  - [1] https://pulsedmedia.com/eternal-vainamoinen.php

## pulsedmedia free seedbox (50 gib / 30 days)

- `storage/pulsedmedia-free-seedbox` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://pulsedmedia.com/free-seedbox.php
- free tier: none reachable: 50 GiB and terminates at day 30; all slots taken ('Available: 0'). The provider itself calls it 'a blatant marketing gimmick'. Fails the quota floor by 10x and the retention test outright. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: 50 GiB and terminates at day 30; all slots taken ('Available: 0'). The provider itself calls it 'a blatant marketing gimmick'. Fails the quota floor by 10x and the retention test outright.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 50 GiB and terminates at day 30; all slots taken ('Available: 0'). The provider itself calls it 'a blatant marketing gimmick'. Fails the quota floor by 10x and the retention test outright.
- sources:
  - [1] https://pulsedmedia.com/free-seedbox.php
