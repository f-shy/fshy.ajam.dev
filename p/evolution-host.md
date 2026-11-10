# Evolution Host

> evolution-host.com | Storage, Compute; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/evolution-host/ | JSON https://fshy.ajam.dev/api/v1/entity/evolution-host.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Evolution Host — $0.00 lifetime VDS, 1 TB NVMe, in exchange for a backlink

- `storage/evolution-host-0-00-lifetime-vds-1-tb-nvme-in-exchange-f` | qualifies-with-caveat | evidence reported | binding write-gated | category iaas
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://lowendtalk.com/discussion/211463/0-00-high-spec-vds-128gb-ram-16-cores-5ghz-1tb-nvme-backlink-required
- disagrees on verdict: `storage/evolution-host` says fails-egress, `storage/evolution-host-0-00-lifetime-vds-1-tb-nvme-in-exchange-f` says qualifies-with-caveat
- free tier: 1 TB NVMe, 128 GB DDR5 RAM, 16 cores @ 5 GHz, DDoS protected. $0.00 'lifetime', conditional on keeping a link to Evolution Host on a website you own. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not stated in the offer text. Unverified. Treat as unknown rather than unmetered. | metered: no
- identity: email | detail: email
- interface: sftp, rsync, ssh, rclone
- limits:
  - write-gated (binding): Application reviewed for SEO value [1]
- limits note: 1 TB per VDS; disqualification is losing the backlink. Application reviewed for SEO value.
- interface detail: sftp
- tooling: Full root VDS. SSH/SFTP/rsync/rclone.
- composes with: This is the write-gated archetype the round-2 brief names: the gate is not money or a card, it is an SEO asset. 'We're mainly looking for websites with good SEO value.' You cannot multiply it without multiplying indexed domains, which is a different resource than storage.
- reliability: 12+ year provider with a history of these barter offers. The failure mode is that the server is removed when the link is removed, not a technical fault.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '128GB DDR5 RAM / 1TB NVMe SSD / 16 CPU Cores @ 5GHz'; 'You get this high-spec DDoS Protected VDS at no cost. All we ask in return is a backlink to your website.'
- sources:
  - [1] https://lowendtalk.com/discussion/211463/0-00-high-spec-vds-128gb-ram-16-cores-5ghz-1tb-nvme-backlink-required

## Evolution Host (Compute)

- `compute/evolution-host` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:06.322Z (live) | stale on 2026-12-08
- url https://evolution-host.com/vps/
- price parsed USD 5.63/mo
- free tier: EUR 5.00/month for Starter: 1 CPU core at 4 GHz and above, 1 GB DDR5, 20 GB NVMe, 1 Gb/s port, 10 TB monthly transfer, Linux, in Europe, US and Asia. Footnoted: Dallas transfer is 10% of the printed value, so the Dallas Starter is 1 TB a month; Singapore, India and Australia ports are 200 Mbps and their base cost is twice the standard rate. Next plans: Developer EUR 10.00 (2 cores, 2 GB, 20 GB, 20 TB), Production EUR 20.00 (3 cores, 3 GB, 60 GB, 30 TB), Business EUR 40.00 (4 cores, 4 GB, 80 GB, 60 TB), Professional EUR 60.00 (8 cores, 8 GB, 120 GB, 70 TB), Enterprise EUR 80.00 (12 cores, 12 GB, 160 GB, 80 TB), Ultimate EUR 100.00 (16 cores, 16 GB, 200 GB, 100 TB). | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 10 TB a month on Starter, 20 TB on Developer and 30 TB on Production; Dallas is 10% of the printed value, so 1 TB on Starter. No overage price is stated | metered: yes | free allowance: 10 TB per month, 1 TB in Dallas | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 10 TB a month generally, but 1 TB in Dallas, which is the location the tracker's cheapest row names; the allowance therefore depends on which of the fifteen locations the order is placed in. Footnotes also cut Singapore, India and Australia to 200 Mbps and double their base cost, so the cheapest region and the fastest region are not the same one. [1]
- limits note: 10 TB a month generally, but 1 TB in Dallas, which is the location the tracker's cheapest row names; the allowance therefore depends on which of the fifteen locations the order is placed in. Footnotes also cut Singapore, India and Australia to 200 Mbps and double their base cost, so the cheapest region and the fastest region are not the same one.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the page documents a VPS control panel with 'unlimited OS reinstalls', real-time resource monitoring and off-site remote backups downloadable from the panel; no API is mentioned on the page read
- composes with: EUR 5.00 for 1 GB with 10 TB of transfer is the cheapest published transfer among evaluated providers, beating AlexHost's EUR 6.00 on a port a hundred times faster; the Dallas location drops to 1 TB, so this is a buy-transfer provider only outside Dallas, and it is the obvious host for a crawler whose cost is bandwidth rather than disk.
- reliability: no reliability event recorded
- notes: The tracker's Dallas row of 1,000 GB/month looked like a print error against the vendor's 10 TB until the vendor's footnote 2 explained it as 10% for wholesale cost; the two sources agree and the footnote is the reason, which is why this record states both numbers rather than one. No storage product line exists: storage/evolution-host already records fails-egress for that question on the same catalogue. json, a different provider. verification criteria: whether Dallas is the cheapest location once the 10% cut is applied, and whether the 4 GHz floor is a guarantee or a fleet description.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
  - price_on_page: EUR 5.00/month: Starter
  - renewal_note: not published: the vendor's own VPS page read on 2026-11-07 prints a monthly price per plan and no renewal price
- evidence:
  - [2] 2026-10-22: cheapest row, quoted: 'Evolution Host - EUR 5.00 / month', '1 Intel Cores (shared)', '1,024 MB RAM', '20 GB NVMe', '1,000 GB/month bandwidth', '1 Gbps port speed', 'IPv4 + IPv6', 'Dallas Texas U.S.A.'
  - [1] 2026-10-22: plan table, quoted: 'EUR 5 Starter Monthly VPS Plan 1 CPU Core at 4Ghz+ 1GB DDR5 RAM 20GB NVMe SSD 1Gb/s Port 10TB Monthly Transfer EvoShield Level 1 Linux Distributions Europe, US and Asian VPS'
  - [1] 2026-10-22: footnote 2, quoted: 'Monthly transfer limits in the Dallas, USA location are 10% of the values displayed above due to wholesale costs.' Footnote 1: 'The port speeds for VPS in Singapore, India and Australia are limited to 200Mbps'. Footnote 4: 'the base cost of Singapore, India and Australia VPS are charged at twice the standard rate of other locations'
  - [1] 2026-10-22: 'EUR 10 Developer ... 2 CPU Cores at 4Ghz+ 2GB DDR5 RAM 20GB NVMe SSD 1Gb/s Port 20TB Monthly Transfer', 'EUR 20 Production ... 3 CPU Cores at 4Ghz+ 3GB DDR5 RAM 60GB NVMe SSD 1Gb/s Port 30TB Monthly Transfer', and the range up to 'EUR 100 Ultimate ... 16 CPU Cores at 4Ghz+ 16GB DDR5 RAM 200GB NVMe SSD 1Gb/s Port 100TB Monthly Transfer'
  - [1] 2026-11-07: the vendor's own VPS page prices the Starter plan at EUR 5 a month | capture: sha256:c0fc2abff04aa1ced9ca688b7aef3da8b3079d914d3f690ab729fe054a0d2b47 | quote: €5 Starter Monthly VPS Plan 1 CPU Core at 4Ghz+ 1GB DDR5 RAM 20GB NVMe SSD 1Gb/s Port1 10TB Monthly Transfer2 EvoShield Level 1 Linux Distributions Europe, US and Asian VPS
- sources:
  - [1] https://evolution-host.com/vps/
  - [2] https://vpspricetracker.com/provider/Evolution_Host/vps

## evolution host (Storage)

- `storage/evolution-host` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://evolution-host.com/vps-hosting.php
- disagrees on verdict: `storage/evolution-host` says fails-egress, `storage/evolution-host-0-00-lifetime-vds-1-tb-nvme-in-exchange-f` says qualifies-with-caveat
- free tier: None reachable: Checked as named. No storage product line at all. The entire catalogue is NVMe VPS from 20 GB to 160 GB with generous transfer (10-80 TB). High bandwidth, no disk. Exactly inverted from wha. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: egress
  - dead_end.why: Checked as named. No storage product line at all — the entire catalogue is NVMe VPS from 20 GB to 160 GB with generous transfer (10-80 TB). High bandwidth, no disk. Exactly inverted from…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Checked as named. No storage product line at all — the entire catalogue is NVMe VPS from 20 GB to 160 GB with generous transfer (10-80 TB). High bandwidth, no disk. Exactly inverted from…
  - [2] 2026-10-21: cited as the basis of the rejection: Checked as named. No storage product line at all — the entire catalogue is NVMe VPS from 20 GB to 160 GB with generous transfer (10-80 TB). High bandwidth, no disk. Exactly inverted from wha
- sources:
  - [1] https://evolution-host.com/vps-hosting.php
  - [2] https://www.vpsbenchmarks.com/compare/evolution_host
