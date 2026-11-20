# SchnellNode

> schnellno.de | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/schnellno/ | JSON https://fshy.ajam.dev/api/v1/entity/schnellno.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SchnellNode

- `compute/schnellnode` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:58.956Z (live) | stale on 2026-12-08
- url https://schnellno.de/cart.php?gid=1
- price parsed USD 4.51/mo
- free tier: 15GB-R10SSD at EUR 4.00/month: 1 vCPU access, 256 MB RAM, 15 GB SSD (RAID 10), 1 Gbps port, 1,000 GB monthly bandwidth, 1 IPv4 and 16 IPv6, Germany. The next plan, 30GB-R10SSD, is EUR 7.00/month with 512 MB RAM, 2 vCPU and 2,000 GB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1,000 GB monthly bandwidth included on the entry plan; overage is not priced on the page read | metered: yes | free allowance: 1,000 GB per month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1,000 GB a month on a 1 Gbps port; the 256 MB of RAM is the tighter wall for anything but a relay or a scheduled job [1]
- limits note: 1,000 GB a month on a 1 Gbps port; the 256 MB of RAM is the tighter wall for anything but a relay or a scheduled job
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: control panel with OS reinstall, ISO and remote console documented; no API mentioned on the page read
- composes with: EUR 4 a month including 16 IPv6 addresses makes this an IPv6 egress relay or a cron runner, with the bulk bytes left on an unmetered host
- reliability: no reliability event observed; the site states shared CPU is split across no more than 5 VPS per node and that the clock can burst to 99 percent
- notes: The vendor cart page and the tracker agree on EUR 4.00, 256 MB and 1,000 GB. A site-wide code 30%OFF is advertised in the header; it is a coupon, not a price, and no discounted figure is recorded. Unverified: a probe of the order form to see whether the 1 vCPU is a fair-share core and whether 256 MB runs a current Debian image.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.25
  - facets.shape.disk_gib: 15
  - price_on_page: EUR 4.00/month (15GB-R10SSD); renewal: not published
- evidence:
  - [1] 2026-10-22: 15GB-R10SSD row: 'Starting from EUR 4.00EUR Monthly, 256MB RAM, 1 vCPU Access, 15GB SSD Space, 1Gbps Network Port, 1000GB Monthly Bandwidth, 1 IPv4 Address, 16 IPv6 Addresses'; the page prints the euro sign and it is spelled EUR here
  - [1] 2026-10-22: 30GB-R10SSD at EUR 7.00 with 512MB RAM and 2 vCPU; 60GB-R10SSD at EUR 14.00 with 1024MB and 4 vCPU; 80GB-R10SSD at EUR 20.00 with 2048MB
  - [2] 2026-10-22: tracker row 'EUR 4.00 / month, 1 Intel Cores (shared), 256 MB RAM, 15 GB SSD, 1,024 GB/month bandwidth, 1 Gbps port speed, IPv4 + IPv6, Germany'
  - [1] 2026-11-07: the 15GB-R10SSD plan's cart row prices it at 4.00 EUR a month | capture: sha256:399abbee5ed349d5ad8cafad742299d8551be4738c1d5eed48bcd21a526c5df0 | quote: | 15GB-R10SSD | Starting from €4.00EUR Monthly |
- sources:
  - [1] https://schnellno.de/cart.php?gid=1
  - [2] https://vpspricetracker.com/provider/SchnellNode/vps
