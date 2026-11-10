# ServaRica

> servarica.com | Storage, Compute; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/servarica/ | JSON https://fshy.ajam.dev/api/v1/entity/servarica.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ServaRICA Polar Bear / Killer Whale / Mammoth storage

- `storage/servarica-polar-bear-killer-whale-mammoth-storage` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category storage VPS (HDD RAIDZ2, Montreal)
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://servarica.com/storage-servers-2/
- price $2.50/TB/mo at 2 TB ($5/mo) and at 8 TB ($20/mo); $2.43/TB/mo at 3.5 TB. On yearly: Polar Bear $48/yr = $2.00/TB/mo; Mammoth $220/yr = $2.29/TB/mo. at 5 TB: 8 TB plan at $2.50/TB/mo (or 3x Polar Bear at $2.00/TB/mo). at 20 TB: 2.5x Mammoth = $2.29/TB/mo. Caveat: active billing outage… | parsed USD 2/TB-mo
- free tier: Opossum 1 1 TB $29/yr · Polar Bear 2 TB $5/mo or $48/yr · Killer Whale 3.5 TB $8.50/mo or $84/yr · Mammoth 8 TB $20/mo or $220/yr | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Quoted as a hard monthly transfer figure per plan: 4 TB / 12 TB / 18 TB / 24 TB on a 1 Gbps port. So 2-3x storage per month. ServaRICA's separate 'unlimited' offer is a different product line: unlimited transfer starting at 250 Mbps and growing +1 Mbps/day up to 1 Gbps. | metered: no
- identity: email | detail: email
- interface: s3, webdav, sftp, rsync, nfs, rclone, webdav-proxy
- limits:
  - per-ip-shaping (binding): 1 GB/day [1]
- limits note: Bandwidth is a hard counter on these plans. Capacity grows 1 GB per day on the expanding plan series. Billing and ordering systems were offline during testing on 2026-10-21.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: KVM/Xen + root, so anything: SFTP, rsync, NFS, rclone serve s3, MinIO, WebDAV via container
- tooling: Root access makes this the most chainable option among the storage providers compared: AList, MinIO or a Cloudflare tunnel endpoint can run on the box itself.
- composes with: Composition with external storage pools is unestablished.
- reliability: Canadian provider since 2010, RAIDZ2. Treat as a real but currently-wobbly vendor.
- notes: the same as the free tier
- extras:
  - price_verbatim: $2.50/TB/mo at 2 TB ($5/mo) and at 8 TB ($20/mo); $2.43/TB/mo at 3.5 TB. On yearly: Polar Bear $48/yr = $2.00/TB/mo; Mammoth $220/yr = $2.29/TB/mo. at 5 TB: 8 TB plan at $2.50/TB/mo (or 3x Polar Bear at $2.00/TB/mo). at 20 TB: 2.5x Mammoth = $2.29/TB/mo. Caveat: active billing outage, bandwidth capped at 2-3x storage.
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 
  - [3] 2026-10-21: 
  - [4] 2026-10-21: 
- sources:
  - [1] https://servarica.com/storage-servers-2/
  - [2] https://servarica.com/unlimited-storage-vps/
  - [3] https://servarica.com/
  - [4] https://servarica.com/black-friday-2025/

## ServaRica storage VPS

- `storage/servarica-storage-vps` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category storage-vps
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://servarica.com/storage-servers-2/
- price $2.00-2.50/TB/mo. At 5 TB: Killer Whale 3.5 TB ($8.50) + Polar Bear 2 TB ($5) = $13.50/mo for 5.5 TB = $2.45/TB. At 20 TB: 2x Mammoth 8 TB ($40) + Penguin 4 TB ($11.11) = $51.11/mo for 20 TB = $2.56/TB; annual billing on the Mammoths drops it to $2.49/TB. Cheapest per-TB is Polar Bear at $2.00/TB… | parsed USD 2/TB-mo
- free tier: Opossum 1 1 TB, Opossum 2 1 TB, Polar Bear 2 TB, Killer Whale 3.5 TB, Horse 3 TB, Penguin 4 TB, Mammoth 8 TB; the 4-20 TB tier adds Chimera Hybrid 4 TB / 8 TB / 16 TB at 4-16 TB of HDD plus NVMe. RAIDZ2 on HDD, Montreal CA. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Two options per plan, switchable in the control panel. Option 1 (the one that matters): 'Unlimited transfer — 250 Mbps port, grows +1 Mbps/day up to 1 Gbps'. Option 2: '10 Gbps port — 12TB 1Gbps monthly cap (throttled to ~10 Mbps after cap)'. So the truly unmetered option is speed-clamped at 250 Mbps and slowly ramps, and the fast option is a 12 TB cap that degrades to ~10 Mbps rather than billing overage. The provider states traffic is counted on BOTH directions (LET thread 199994 p9: 'We count traffic from both d[irections]'). | metered: no
- identity: card | detail: card
- interface: rest, sftp, rsync, nfs, rclone
- limits:
  - per-ip-shaping (binding): 15 GB/day [1]
- limits note: per-object-cap: none. 'Unlimited Expanding Storage' plans add +1 to +15 GB/day of disk rather than granting it up front. Xen on the older storage line.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: sftp, rsync, nfs, rest (self-hosted)
- tooling: rclone SFTP, any backup tool, Xen/KVM root
- composes with: Root virtual private server supporting AList or MinIO installation. The 250 Mbps unmetered network option provides continuous throughput without monthly byte quotas.
- reliability: Long-standing CA provider with a strong LowEndTalk record — 'Have been using servarica for close a year now. Absolutely no issues' (thread 180949), 'I just renewed my storage vps with servarica for the 2nd year never had issue'.
- notes: the same as the free tier
- extras:
  - price_verbatim: $2.00-2.50/TB/mo. At 5 TB: Killer Whale 3.5 TB ($8.50) + Polar Bear 2 TB ($5) = $13.50/mo for 5.5 TB = $2.45/TB. At 20 TB: 2x Mammoth 8 TB ($40) + Penguin 4 TB ($11.11) = $51.11/mo for 20 TB = $2.56/TB; annual billing on the Mammoths drops it to $2.49/TB. Cheapest per-TB is Polar Bear at $2.00/TB on annual ($48/yr). Caveat: out of stock across the entire storage catalogue.
- evidence:
  - [2] 2026-10-21: Polar Bear 2 TB $5/mo or $48/yr, Killer Whale 3.5 TB $8.50/mo, Penguin 4 TB $11.11/mo, Mammoth 8 TB $20/mo or $220/yr
  - [3] 2026-10-21: Polar Bear detail page with BOTH bandwidth options quoted verbatim, plus a published YABS (1,090 GB6 single, 149-657 MB/s disk)
  - [1] 2026-10-21: and https://servarica.com/storage/4-20tb/ — every storage row marked 'Out of stock' at time of reading
  - [4] 2026-10-21: provider announcing 'unlimited bandwidth starting at 250 Mbps, with an extra 1 Mbps added daily'
- sources:
  - [1] https://servarica.com/storage/0-5-4tb/
  - [2] https://servarica.com/storage-servers-2/
  - [3] https://servarica.com/plan/588/
  - [4] https://lowendtalk.com/discussion/196219/

## Servarica

- `compute/servarica` | paid-only | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://servarica.com/dedicated-servers/
- free tier: The dedicated list, in USD with a CAD figure beside it: a Xen Dedicated with 2 x Xeon E5-2650 v2, 256 GB DDR3 ECC, a 500 GB SSD and a 500 Mbps uplink at USD 49 a month or USD 539 a year; a Baboon with the same CPUs and 256 GB but 2 x 12 TB of disk and a 1 Gbps uplink at USD 69; a Baboon E5-2697 v2 at 24 cores / 48 threads with 256 GB, 2 x 120 GB SSD and 2 x 12 TB at USD 79; an Epyc Greyhound with an EPYC 7551P at 32 cores / 64 threads, 128 GB DDR4 ECC, 3.2 TB NVMe and 100 TB a month on 10 Gbps at USD 112; and an Elephant Storage with 24 x 8 TB, 256 GB RAM and 200 TB a month on 10 Gbps at USD 448.50. Every one of those order links resolves to 'Out of Stock'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: category page carries full configuration text ('2x Intel Xeon E5-2630L V2, 64GB DDR3 ECC RAM, 1x 1TB SSD, 2x 16TB enterprise SATA disks, 500mbps unmetered Bandwidth') and no prices | metered: no | source: [2]
- identity: email
- interface: unknown
- limits note: no binding constraint identified
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: no open question recorded
- evidence:
  - [1] 2026-10-22: table rows 'Xen Dedicated | 256GB DDR3 ECC | 2x Xeon E5-2650 v2 | 500mbps UL | 1x 500GB SSD | $49 CA$66.15 | $539 CA$727.65', 'Baboon Dedicated | 256GB DDR3 | 2x Xeon E5-2650 v2 | 1Gbps UL | 2x 12TB | $69', 'Epyc Greyhound | 128GB DDR4 ECC | AMD EPYC 7551P | 100TB/M 10Gbps | 3.2TB NVMe | $112', 'Elephant Storage | 256GB DDR4 ECC | Xeon E5-2640 v4 | 200TB/M 10Gbps | 24x 8TB | $448.50'
  - [3] 2026-10-22: the order link for the USD 49 machine returns 'Out of Stock - We are currently out of stock on this item'
  - [4] 2026-10-22: the newer 2026 category lists eight configurations including 'EPYC 7551p or EPYC 7601 32 cores 64 threads, 128GB DDR4 ECC RAM, 3.2TB Enterprise NVMe, 150TB/m transfer on 10gbps' and 'Intel E5-2580v2 ... Fully dedicated (pci-passthrough) Nvidia Tesla P40, 100TB/m transfer on 10gbps', all without a readable price
  - [2] 2026-10-22: category page carries full configuration text ('2x Intel Xeon E5-2630L V2, 64GB DDR3 ECC RAM, 1x 1TB SSD, 2x 16TB enterprise SATA disks, 500mbps unmetered Bandwidth') and no prices
- sources:
  - [1] https://servarica.com/dedicated-servers/
  - [2] https://clients.servarica.com/store/dedicated-servers
  - [3] https://clients.servarica.com/store/black-friday-2024/xen-dedicated-server-2024
  - [4] https://clients.servarica.com/store/bf-2025-dedicated-servers

## ServaRica — 'Unlimited Expanding Storage' (500 GB + 1 GB/day, $5/mo)

- `storage/servarica-unlimited-expanding-storage` | paid-only | evidence documented | binding volume-quota | category iaas
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:10:58.430Z (live) | stale on 2026-12-04
- url https://servarica.com/unlimited-storage-vps/
- price USD 2.00 per TB-month at Polar Bear Storage (2 TB, USD 48 per year); USD 2.29 per TB-month at Mammoth Storage (8 TB, USD 220 per year) | parsed USD 2/TB-mo
- free tier: Shrimp 1: 500 GB base + 1 GB/day automatic growth, $5/mo. I.e. it crosses 1 TB at ~day 500 and 1.87 TB at 4 years, on a fixed price. Shrimp 2: 500 GB + 2 GB/day, $7/mo. Lobster: 2 TB + 3 GB/day, $10/mo. Separate fixed line: Opossum 1 = 1 TB for $29/YEAR, Polar Bear 2 TB $48/yr, Killer Whale 3.5 TB $84/yr. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Includes 12 TB per month (Shrimp) or 18 TB per month (Lobster) on 1 Gbps ports, with metered traffic beyond allowances. | metered: yes | free allowance: 12 TB per month
- identity: email | detail: email
- interface: sftp, rsync, ssh, rclone
- limits:
  - volume-quota (binding): 1 GB/day [1]
  - volume-quota (binding): 2 GB/day [1]
- limits note: Bandwidth is the real cap (12–18 TB/mo). Growth is 1–3 GB/day, so it is unusable for a 20 TB cold archive in year one. It is a decade instrument. Montreal location.
- binding note: the expanding plans start at 500 GB (Shrimp) or 2 TB (Lobster) and grow 1 to 3 GB per day
- interface detail: sftp
- tooling: KVM with root. SSH/SFTP/rsync/rclone-sftp. RaidZ2 HDD backend on the fixed line.
- composes with: The genuinely interesting mechanic: this is 'free storage over time' priced as a subscription. Capacity is a function of tenure, so the chaining move is tenure, not accounts. A $29/year Opossum is 1 TB now and the expanding plans add 365 GB/year for free at fixed price. No free tier.
- reliability: Long-running Canadian host with a heavy Black Friday presence on LET/NodeSeek; NodeSeek threads name it among the 'highly trusted' big-disk providers. RaidZ2 on the fixed line.
- notes: the same as the free tier
- evidence note: The 2026-11-03 evidence rows read https://servarica.com/unlimited-storage-vps/ (Shrimp 1, Shrimp 2 and Lobster base sizes, daily growth, bandwidth and monthly and yearly prices) and https://servarica.com/storage-servers-2/ (the fixed-size yearly prices). Price and growth that decide the paid-only verdict cite vendor captures; identity is not read from a sign-up page.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Shrimp 1: 500 GB base + 1 GB/day automatic growth, $5/mo — i.e. it crosses 1 TB at ~day 500 and 1.87 TB at 4 years, on a fixed price. Shrimp 2: 500 GB + 2 GB/day, $7/mo. Lobster: 2 TB + 3 GB/day, $10/mo. Separate fixed line: Opossum 1 = 1 TB for $29/YEAR, Polar Bear 2 TB $48/yr, Killer Whale 3.5 TB $84/yr.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Shrimp 1 | 2 GB | 2 | 12TB 1Gbps | 500 GB +1GB/day | $5'; 'Lobster … 2 TB +3GB/day … $10'; page subtitle 'Daily-expanding storage VPS from $5/mo. Grows automatically over time.'
  - [2] 2026-10-21: 'Opossum 1 Storage … 1 TB … $29/yr'; 'Mammoth Storage … 8 TB … $220/yr'
  - [1] 2026-11-03: Shrimp 1 is 500 GB plus 1 GB per day with 12TB of bandwidth at USD 5 per month, a paid plan | capture: sha256:36cc46bc792ddbce0a5a375f723609166b41e209a9b43c97c8916780f75463e1 | quote: | Shrimp 1 | 2 GB | 2 | 12TB 1Gbps | 500 GB +1GB/day | $5CA$6.75 | $55CA$74.25 |
  - [1] 2026-11-03: Shrimp 2 is 500 GB plus 2 GB per day at USD 7 per month | capture: sha256:36cc46bc792ddbce0a5a375f723609166b41e209a9b43c97c8916780f75463e1 | quote: | Shrimp 2 | 2 GB | 2 | 12TB 1Gbps | 500 GB +2GB/day | $7CA$9.45 | $77CA$103.95 |
  - [2] 2026-11-03: Polar Bear Storage is 2 TB at USD 48 per year; Mammoth Storage (8 TB, USD 220 per year) is on the same table | capture: sha256:797fe9bde7424d4d89bf09b5837b91c0c6c53f6e2458bf4fcadcba1b9daa4a0e | quote: | Polar Bear Storage | 2 GB | 2 | 12TB 1Gbps | 2 TB | $5CA$6.75 | $48CA$64.80 |
  - [1] 2026-11-03: Lobster starts at 2 TB and grows 3 GB per day; the Shrimp rows start at 500 GB and grow 1 or 2 GB per day | capture: sha256:36cc46bc792ddbce0a5a375f723609166b41e209a9b43c97c8916780f75463e1 | quote: | Lobster | 3 GB | 4 | 18TB 1Gbps | 2 TB +3GB/day | $10CA$13.50 | $110CA$148.50 |
  - [1] 2026-11-03: Shrimp 1 grows 1 GB per day from a 500 GB base | capture: sha256:36cc46bc792ddbce0a5a375f723609166b41e209a9b43c97c8916780f75463e1 | quote: | Shrimp 1 | 2 GB | 2 | 12TB 1Gbps | 500 GB +1GB/day | $5CA$6.75 | $55CA$74.25 |
- sources:
  - [1] https://servarica.com/unlimited-storage-vps/
  - [2] https://servarica.com/storage-servers-2/
