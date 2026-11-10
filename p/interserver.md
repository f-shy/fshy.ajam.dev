# InterServer Storage

> interserver.net | Storage, Compute; 6 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/interserver/ | JSON https://fshy.ajam.dev/api/v1/entity/interserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## InterServer Storage ST 600 (20 TB)

- `storage/interserver-storage-st-600` | qualifies-with-caveat | evidence reported | binding none | category shared storage hosting
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.interserver.net/storage/
- price $2.10/TB/mo at 20 TB ($42). At 5 TB interpolating the 4 TB plan ($10, 10 TB transfer) → $2.50/TB/mo. Egress is metered 1:1, which is the difference from Hetzner at the same price. | parsed USD 2.1/TB-mo
- free tier: 20 TB space, 20 TB transfer/month, 60 domains, DirectAdmin | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'Transfer 20 TB' per month on the 20 TB plan (1:1 ratio with storage capacity). The plan provides Space 20TB and Transfer 20TB for $42 per month. | metered: yes
- identity: card | detail: card
- interface: sftp, ftps, ftp, scp, rsync, ssh, rclone
- limits note: 1:1 transfer ratio; no root; ZFS/RAID-Z2 backing
- interface detail: FTP/FTPS, SFTP, SCP, rsync over SSH, DirectAdmin, web delivery; 'Object Storage Beta' API
- tooling: rclone over SFTP; rsync
- composes with: rsync target; DirectAdmin file manager; beta object API
- reliability: Transfer cap at 1:1 is the binding constraint. A 20 TB restore consumes the entire month's allowance. Fine for backup-in, poor for serving.
- notes: the same as the free tier
- extras:
  - price_verbatim: $2.10/TB/mo at 20 TB ($42). At 5 TB interpolating the 4 TB plan ($10, 10 TB transfer) → $2.50/TB/mo. Egress is metered 1:1, which is the difference from Hetzner at the same price.
- evidence:
  - [1] 2026-10-21: 'ST 600 — 20 TB storage — $42/month — Transfer 20TB — Domains 60 — Control Panel DirectAdmin'; 'ST 500 — 10 TB — $25/month — Transfer 15TB'; 'ST 400 — 4 TB — $10/month — Transfer 10TB'
- sources:
  - [1] https://www.interserver.net/storage/

## InterServer Storage VPS (1 TB slices)

- `storage/interserver-storage-vps` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category storage VPS, composable slices
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.interserver.net/vps/storage.html
- price $3.00/TB/mo flat at 1, 5, 10, 20 TB — genuinely linear, no tier discount. Caveat: 2 TB transfer per TB stored does not cover 30 TB/mo serving at 20 TB stored (40 TB included, so it does at 20 TB; it fails at 10 TB stored where only 20 TB is included). | parsed USD 3/TB-mo
- free tier: 1 TB per slice, 1–20+ slices stacked | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Metered per slice: 'Each storage VPS slice adds 1TB SATA storage, 2GB memory, 2TB transfer'. A 2:1 ratio. At 10 slices = 10 TB storage and only 20 TB/mo transfer. Below the 30 TB/mo serving requirement. Overage rate not published on the page. | metered: yes | free allowance: 20 TB per month
- identity: card | detail: card
- interface: sftp, nfs
- limits:
  - per-ip-shaping (binding): 10 Gbps [1]
- limits note: Slice count adds RAM and cores linearly, which is wasted spend for pure storage. 10 Gbps shared port. The traffic ratio is the binding constraint, not the price.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: full root; run MinIO/SFTP/NFS yourself
- tooling: unrestricted
- composes with: MinIO + Cloudflare; or rsync target
- reliability: Long-established US host (Secaucus/LA). The $3/TB headline is genuine and linear — 10 slices is $30 for 10 TB, no discount, no cliff. Page served a 403 and was retrieved via the provider renderer.
- notes: the same as the free tier
- extras:
  - price_verbatim: $3.00/TB/mo flat at 1, 5, 10, 20 TB — genuinely linear, no tier discount. Caveat: 2 TB transfer per TB stored does not cover 30 TB/mo serving at 20 TB stored (40 TB included, so it does at 20 TB; it fails at 10 TB stored where only 20 TB is included).
- evidence:
  - [1] 2026-10-21: 'Starts at $3.00 per TB per month'; 1 Slice $3/mo (1TB SATA, 2TB transfer, 10Gbps shared); 10 Slices $30/mo (10TB SATA, 20TB transfer); 20 Slices listed
  - withheld 2026-10-21: same page — 'Use storage-optimized cloud compute for backups, archives, and high-volume file hosting when capacity matters more than raw application I/O'
- sources:
  - [1] https://www.interserver.net/vps/storage.html

## InterServer (compute/interserver)

- `compute/interserver` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:07.273Z (live) | stale on 2026-12-08
- url https://www.interserver.net/vps/
- price parsed USD 3/mo
- disagrees on identity_kind: `compute/interserver` says email, `compute/interserver-windows` says card
- free tier: USD 3.00/month for 1 slice: 1 core, 2 GB memory, 40 GB SSD, 2 TB transfer, 10 Gbps shared port, root access, in New Jersey. Slices stack: the page states 'The full order flow lets you choose any size from 1 to 32 slices' and that managed support is included from 8 slices. Windows Cloud Compute starts at USD 10.00/month and the Storage VPS line also starts at USD 3.00/month. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2 TB of transfer per slice, stated on the slice card; no overage price or throttle is stated on the page read | metered: yes | free allowance: 2 TB per month per slice | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2 TB of transfer per slice is the stated allowance and it scales with the slice count rather than sitting at the account level; no overage price and no post-allowance throttle are stated on the page read. The port is published as '10Gbps Shared', so the shared fabric rather than the named speed is the physical ceiling. [1]
- limits note: 2 TB of transfer per slice is the stated allowance and it scales with the slice count rather than sitting at the account level; no overage price and no post-allowance throttle are stated on the page read. The port is published as '10Gbps Shared', so the shared fabric rather than the named speed is the physical ceiling.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: full root access is stated on the slice card; the order flow is described as choosing a slice count from 1 to 32. No API or panel name appears in the extract
- composes with: USD 3.00 for 2 GB and 40 GB of SSD with 2 TB of transfer is the cheapest RAM among evaluated providers, and because the product is a stackable slice it grows from a cron host to a large box without changing provider or tooling; 40 GB of SSD per slice also makes 1-2 slices a usable small database host.
- reliability: no reliability event recorded
- notes: Wall: the direct fetch of the vendor page returned upstream 403 and the text was served through automated retrieval's exa reader, so the vendor figures here were read from an extraction rather than from a raw HTML fetch, and the page came back with no extraction step. The tracker and the vendor disagree on port speed for the same slice, 2 Gbps against '10Gbps Shared'; the vendor figure is recorded and the disagreement is left visible rather than reconciled. Rows above one slice were not read, so the per-slice price ladder is unverified. json covers the 1 TB-per-slice storage line. verification criteria: the price at 8 and 32 slices, and whether transfer pools per account or per slice.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 40
  - price_on_page: USD 3.00/month for 1 slice
  - renewal_note: not published; no renewal price is printed on the vendor's VPS page
- evidence:
  - [2] 2026-10-22: cheapest row, quoted: 'InterServer - $3.00 / month', '1 Intel Cores (shared)', '2,048 MB RAM', '40 GB SSD', '2,000 GB/month bandwidth', '2 Gbps port speed', 'IPv4 + IPv6', 'New Jersey U.S.A.'; product slug KVM_Machine_with_1_vCore_1_slice
  - [1] 2026-10-22: slice card, quoted: '1 Slice', '3/mo', '1 core 2GB memory', '40GB SSD 2TB transfer', '10Gbps Shared port', 'Root access Full server control'. The page's lead states 'Cloud compute that scales from $3/month VPS slices.'
  - [1] 2026-10-22: 'Each VPS hosting slice adds a predictable amount of CPU, memory, SSD storage, and transfer. The full order flow lets you choose any size from 1 to 32 slices.' and 'Managed eligible ... 8+ slices'; the style list reads 'Linux Cloud Compute ... from $3/mo', 'Windows Cloud Compute ... from $10/mo', 'Storage VPS ... from $3/mo'
  - [1] 2026-11-07: the vendor page prices 1 slice at $3.00 per month today, with the starter card reading 1 core, 2GB memory, 40GB SSD; the order flow at my.interserver.net bounced to a login page (login.php?queue=none.order_vps), so the cart price sits behind a sign-up | capture: sha256:c94cfe3423ba23d7298cc425e1f9a27287cb7a306ba6ff007f6807a1c08a519f | quote: Cloud compute starts at $3.00 per month. ... $3/mo with 1 core, 2GB memory, 40GB SSD
  - [1] 2026-11-07: the vendor page prices 1 slice at $3.00 per month today, with the starter card reading 1 core, 2GB memory, 40GB SSD | capture: sha256:c94cfe3423ba23d7298cc425e1f9a27287cb7a306ba6ff007f6807a1c08a519f | quote: Cloud compute starts at $3.00 per month. ... $3/mo with 1 core, 2GB memory, 40GB SSD
  - [1] 2026-11-07: the vendor's VPS page prices the monthly plan and prints no renewal price | capture: sha256:c94cfe3423ba23d7298cc425e1f9a27287cb7a306ba6ff007f6807a1c08a519f | quote: Cloud compute starts at $3.00 per month. ... $3/mo with 1 core, 2GB memory, 40GB SSD
- sources:
  - [1] https://www.interserver.net/vps/
  - [2] https://vpspricetracker.com/provider/InterServer/vps

## InterServer (Windows Cloud Compute, 8 slices)

- `compute/interserver-windows` | paid-only | evidence documented | binding volume-quota | category Windows VPS | tier Windows Cloud Compute, 8 slices
- needs card yes, phone no, ID no, institution no | verified 2026-10-26T11:33:32.317Z (live) | stale on 2026-11-26
- url https://www.interserver.net/vps/windows-vps.html
- price parsed USD 40/mo
- disagrees on identity_kind: `compute/interserver` says email, `compute/interserver-windows` says card
- free tier: no free tier; the Windows product starts at USD 10.00/month for 2 slices, and the 8-slice shape is USD 40.00/month | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the slice plan is paid; the page states no deletion clock
- egress: 16 TB of transfer a month on 8 slices, on a 10 Gbps shared port; no overage price or post-allowance throttle is stated | metered: yes | free allowance: 16 TB per month | source: [1]
- identity: card | detail: an account and a payment method at order; the order page returned a sign-in form, so the accepted instrument and any hold are unverified
- interface: unknown
- limits:
  - volume-quota (binding): 16 TB of transfer a month on 8 slices [1]
  - per-ip-shaping: 10 Gbps shared port, so the shared fabric is the physical ceiling rather than the named speed [1]
- limits note: the Windows page states no public IPv4 line and no session clock; the Linux slice card states IPv4 + IPv6, and the Windows slice ladder carries RDP
- binding note: 16 TB a month is the only published byte ceiling, and it is the first limit a high-transfer workload reaches; the shared 10 Gbps port is second.
- interface detail: RDP over the provider's network, with administrator control stated on the Windows page; no public API is documented for this product
- tooling: any RDP client; the provider's Hyper-V panel; no API read on 2026-10-26.
- composes with: a 4 vCPU / 16 GiB Windows desktop for USD 40 a month, which is the cheapest shape found that meets the four minimums; it grows by adding slices without changing provider
- reliability: no reliability event observed; the product is Hyper-V with a 10 Gbps shared port.
- notes: If the Windows SKU excludes a Microsoft license, license compliance requirements are not met.
- evidence note: the shape and the USD 40.00 price are printed on the Windows page read. The Windows SKU is USD 16.00 a month above the identical Linux 8-slice SKU at USD 24.00, which is consistent with a bundled licence, but no sentence on either page says 'licence included'.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 16
  - shape.disk_gib: 320
  - billing_model: monthly
  - term: monthly
  - monthly_usd: 40.0
  - first_month_usd: 40.0
  - setup_fee_usd: 0.0
  - renewal_usd: 40.0
  - windows_licence: supplied as part of the Windows Cloud Compute SKU; the page does not print the word licence
  - licence_delta_usd: 16.0
  - ipv4: not stated on the Windows page; the Linux slice card states IPv4 + IPv6
  - port_mbps: 10000
  - port_note: 10 Gbps shared
  - traffic: 16 TB/month
  - stock: orderable; the order page requires a login
  - cart_url: https://www.interserver.net/vps/windows-vps.html
  - payment_methods: not read; the order page returned a sign-in form
- evidence:
  - [1] 2026-10-26: quoted: '8 Slices ... $ 40 / mo ... 4 cores ... 16GB memory ... 320GB SSD ... 16TB transfer', and 'Run Windows Server workloads on Hyper-V cloud compute with Remote Desktop access, administrator control'
  - [1] 2026-10-26: the slice ladder runs from 2 slices at USD 10.00 to 20 slices at USD 100.00, and every rung carries 'Windows VPS platform | Remote Desktop | RDP access included'
  - [2] 2026-10-26: the identical Linux 8-slice shape is USD 24.00 a month for 4 cores, 16GB memory, 320GB SSD and 16TB transfer; the Windows 8-slice is USD 40.00, a USD 16.00 delta
- sources:
  - [1] https://www.interserver.net/vps/windows-vps.html
  - [2] https://www.interserver.net/vps/

## InterServer Storage Cloud Compute — 1 TB slices at $3/mo, recurring 'buy 1 get 2 free months'

- `storage/interserver-storage-cloud-compute-1-tb-slices-at-3-mo-re` | paid-only | evidence documented | binding none | category iaas
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T01:24:26.449Z (live) | stale on 2026-12-05
- url https://www.interserver.net/vps/storage.html
- free tier: No free tier. Storage VPS costs $3 per month per 1 TB SATA slice (2 GB memory and 2 TB transfer per slice), from 1 slice to 32 slices (32 TB SATA, 64 TB transfer). 11 slices are 11 TB SATA with 22 TB transfer for $33 per month; 22 slices are 22 TB SATA with 44 TB transfer for $66 per month. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 2 TB transfer per 1 TB slice (22 TB with 11 slices, 44 TB with 22 slices) on a 10 Gbps shared port; the page does not state the transfer period. | metered: yes | free allowance: 2 TB transfer per slice (period not stated on the page)
- identity: card | detail: card
- interface: sftp, rsync, ssh, scp, ftps, rclone
- limits note: No trial and no money-back guarantee: 'There is no trial period or money-back guarantee on Storage VPS hosting.' Transfer is 2 TB per 1 TB slice.
- binding note: priced offer: capacity is bought in 1 TB slices at $3 each and transfer scales at 2 TB per slice
- interface detail: sftp
- tooling: KVM root, full SSH/SFTP/rsync/rclone.
- composes with: The only quasi-repeatable discount here: LET runs 'Buy 1 Get 2 Free' on VPS/Storage VPS roughly quarterly, and the promo is claimed by replying with an order number in the thread. So it recurs on the promo calendar rather than per account. NodeSeek users also report a $2.40/mo 1 TB uncapped variant.
- reliability: Three U.S. regions: Secaucus NJ, Richardson TX and El Segundo CA. Month-to-month billing with no trial and no money-back guarantee. unverified: operating since 1998 and the NodeSeek recommendation counts.
- notes: 1 TB SATA per slice at $3.00/TB/month, stackable up to multi-TB (32 TB ladder). 2 GB RAM, 1 core, 30 GB SSD boot per slice, 2 TB transfer.
- evidence note: documented from the vendor page read on 2026-11-03 (https://www.interserver.net/vps/storage.html): the 1 TB slice with 2 TB transfer at 3 USD per month and the absence of a trial. Card as the payment identity, the transfer period, retention and per-object cap were not read.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 TB SATA per slice at $3.00/TB/month, stackable up to multi-TB (32 TB ladder). 2 GB RAM, 1 core, 30 GB SSD boot per slice, 2 TB transfer.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Starts at $3.00 per TB per month'; 'There is no trial period or money-back guarantee on Storage VPS hosting.'
  - [2] 2026-10-21: 'You can get 2 additional months free when you pay for just 1 month of VPS, Storage VPS, or Dedicated servers'
  - [1] 2026-11-03: each slice is 1 TB SATA with 2 TB transfer at $3 per month | capture: sha256:fdded16799f2e14e2ff691c577f4baa492e517e4c90112d3d3e0b8acd11bd9af | quote: Each storage VPS slice adds 1TB SATA storage, 2GB memory, 2TB transfer, and a predictable $3 monthly cost.
  - [1] 2026-11-03: the 11-slice plan has 11 TB SATA and 22 TB transfer | capture: sha256:fdded16799f2e14e2ff691c577f4baa492e517e4c90112d3d3e0b8acd11bd9af | quote: - 11TB SATA 22TB transfer
  - [1] 2026-11-03: transfer protocols offered | capture: sha256:fdded16799f2e14e2ff691c577f4baa492e517e4c90112d3d3e0b8acd11bd9af | quote: Transfer data with rsync over SSH, SFTP, SCP, FTP over TLS, or a custom LiteSpeed and PHP workflow.
  - [1] 2026-11-03: no trial, no money-back, month-to-month billing | capture: sha256:fdded16799f2e14e2ff691c577f4baa492e517e4c90112d3d3e0b8acd11bd9af | quote: There is no trial period or money-back guarantee on Storage VPS hosting. Billing is month to month, and you can cancel from your account if the service is no longer needed.
  - [1] 2026-11-03: three U.S. regions | capture: sha256:fdded16799f2e14e2ff691c577f4baa492e517e4c90112d3d3e0b8acd11bd9af | quote: Deploy VPS services near the New York City area in Secaucus, NJ, near Dallas in Richardson, TX, or in the Los Angeles area at El Segundo, CA.
  - [1] 2026-11-03: the 22-slice plan has 22 TB SATA and 44 TB transfer | capture: sha256:fdded16799f2e14e2ff691c577f4baa492e517e4c90112d3d3e0b8acd11bd9af | quote: - 22TB SATA 44TB transfer
  - [1] 2026-11-04: each slice is 1 TB SATA with 2 TB transfer at 3 USD per month | capture: sha256:fdded16799f2e14e2ff691c577f4baa492e517e4c90112d3d3e0b8acd11bd9af | quote: Each storage VPS slice adds 1TB SATA storage, 2GB memory, 2TB transfer, and a predictable $3 monthly cost.
  - [1] 2026-11-04: no free tier or trial; month-to-month billing | capture: sha256:fdded16799f2e14e2ff691c577f4baa492e517e4c90112d3d3e0b8acd11bd9af | quote: There is no trial period or money-back guarantee on Storage VPS hosting. Billing is month to month, and you can cancel from your account if the service is no longer needed.
- sources:
  - [1] https://www.interserver.net/vps/storage.html
  - [2] https://lowendtalk.com/discussion/203663/interserver-buy-1-get-2-free-wh-vps-updated-plans

## InterServer Storage Hosting ST 600 (20 TB)

- `storage/interserver-storage-hosting-st-600` | fails-egress | evidence reported | binding none | category shared storage hosting (ZFS / RAID-Z2, DirectAdmin)
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.interserver.net/storage/
- price $2.10/TB/mo at the 20 TB tier ($42) but with only 20 TB/mo of transfer. $2.50/TB/mo at the 10 TB tier with 15 TB transfer. at 5 TB: buy the 10 TB tier = $2.50/TB/mo. at 20 TB: $2.10/TB/mo. | parsed USD 2.1/TB-mo
- free tier: 200 GB $3 · 1 TB $5 · 2 TB $8 · 4 TB $10 · 10 TB $25 · 20 TB $42, all per month | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: VERBATIM per-tier transfer caps: 1 TB plan gets "Transfer 2 TB"; 4 TB gets 10 TB; 10 TB gets 15 TB; 20 TB gets only 20 TB of transfer. So egress is ~1x storage at the top tier, decaying to 0.5x at the 200 GB tier. This is a metered product wearing an 'unlimited hosting' costume. | metered: yes
- identity: card | detail: card
- interface: s3, webdav, sftp, ftps, ftp, scp, rsync, ssh
- limits note: No root access on the shared storage product ("Shared storage does not include root access"). Transfer caps are the binding constraint, not capacity.
- interface detail: FTP/FTPS, SFTP, SCP, rsync over non-root SSH, DirectAdmin, Apache/PHP/MySQL, Nextcloud, web file delivery
- tooling: Rsync/SFTP. "Object Storage Beta" exists but is beta. Treat as unavailable. No S3, no WebDAV stated.
- composes with: DirectAdmin + Apache means you CAN serve HTTP directly from it, which is unusual and useful for a Cloudflare origin. But the 20 TB transfer cap at the 20 TB tier means one full re-sync exhausts the month.
- reliability: Long-established (InterServer, since 1999), ZFS + RAID-Z2, 99.9% uptime claim, 24/7 support. Very stable operator. The product is priced to make capacity cheap and bandwidth expensive, which is the opposite of the requirement.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 200 GB $3 · 1 TB $5 · 2 TB $8 · 4 TB $10 · 10 TB $25 · 20 TB $42, all per month
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $2.10/TB/mo at the 20 TB tier ($42) but with only 20 TB/mo of transfer. $2.50/TB/mo at the 10 TB tier with 15 TB transfer. at 5 TB: buy the 10 TB tier = $2.50/TB/mo. at 20 TB: $2.10/TB/mo.
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 
- sources:
  - [1] https://www.interserver.net/storage/
  - [2] https://www.interserver.net/vps/storage.html
