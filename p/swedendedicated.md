# SwedenDedi

> swedendedicated.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/swedendedicated/ | JSON https://fshy.ajam.dev/api/v1/entity/swedendedicated.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SwedenDedi

- `compute/swedendedi` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-07T11:15:41.616Z (live) | stale on 2026-12-08
- url https://swedendedicated.com/vps/
- price parsed USD 11.27/mo
- free tier: NVMe SSD VPS 2 GB at EUR 10.00 per month in the vendor cart: the order summary prints setup EUR 0.00, monthly EUR 10.00, EUR 10.00 due today, with 1 processor core, 2 GB memory, 40 GB NVMe or SSD disk, 2000 GB monthly data transfer, 1000 Mbit connection, 1 IPv4, KVM over VNC, at the Stockholm - Kista datacenter. The cart configurator rendered with prices and no out-of-stock notice; the cycle options rendered without labels, so no annual price is labeled on the pages read, and no renewal price is published. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2 TB a month is included; the page states no overage price and no throttle, so what happens past 2 TB is unverified | metered: yes | free allowance: 2 TB per month | source: [1]
- identity: email | detail: the cart requires an account: the cart page carries Login and Register links; the registration form's fields were not read
- interface: rest
- limits:
  - volume-quota (binding): 2 TB a month is the plan's stated bandwidth on a 1000 Mbit uplink; no overage rate is stated, so the allowance is the wall and its enforcement is unverified [1]
- limits note: 2 TB a month is the plan's stated bandwidth on a 1000 Mbit uplink; no overage rate is stated, so the allowance is the wall and its enforcement is unverified
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read beyond 'KVM' and the control-panel feature list ('Control panel, reboot, reinstall, monitor'); no API is documented on the page read
- composes with: 2 GB and 2 TB in Sweden for EUR 9.99 sits well above the EUR 2.50 two-gigabyte host among documented hosts, and its case is the stated 1 Gbit uplink with a free /64 IPv6 rather than the memory, so it fits a small proxy or an EU index node that needs IPv6
- reliability: The vendor domain answers with its VPS page and its WHMCS cart prices the 2 GB plan; the record's DNS-failure rows probe a misspelling of the vendor domain (swededicated.com in place of swedendedicated.com) and say nothing about the vendor.
- notes: The tracker's EUR 10.00 is a rounding of the vendor's EUR 9.99, so the two sources agree to the cent and the record carries the vendor figure. The page states a 99.9 percent uptime claim in prose, which is a stated term and not an observed event. Unverified: whether the 1000 Mbit uplink is shared or guaranteed per VM, and whether the 2 TB is enforced by shaping. Rendering and provenance: currency symbols are written out (EUR, GBP, RUB, VND), diacritics in place names are folded to ASCII, and a price the page splits across two lines is joined as value/period; the tracker page stated 'Database update: 7 hours ago' when it was read on 2026-10-22.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 40
  - price_on_page: EUR 10.00/month for NVMe SSD VPS 2 GB
- evidence:
  - [2] 2026-10-22: cheapest row: 'SwedenDedi - EUR 10.00 / month', '1 Intel Cores (shared)', '2,048 MB RAM', '40 GB NVMe', '2,000 GB/month bandwidth', '0.98 Gbps port speed', 'Stockholm Sweden'
  - [1] 2026-10-22: plan card, quoted: 'NVMe SSD VPS 2 GB', 'EUR 9.99 monthly', 'Memory: 2 GB', 'Storage: 40 GB SSD', 'Processor core: 1', 'Bandwidth: 2 TB', 'Ipv4 Address: 1', 'Uplink: 1000 Mbit', 'Virtualization: KVM'
  - [1] 2026-10-22: the ladder above it: 'NVMe SSD VPS 4 GB' at 'EUR 19.99 monthly' with 60 GB and 3 TB, '8 GB' at 'EUR 39.99' with 100 GB and 5 TB, '16 GB' at 'EUR 59.99', '32 GB' at 'EUR 79.99'
  - [1] 2026-10-22: 'Located in Sweden!', 'Ipv6 /64 subnet for free!', and 'all servers are connected to the internet through redundant 1000 Mbit connections'
  - probe:https://swededicated.com/vps/ 2026-11-07: the probe record of the vendor page ends at DNS resolution with no HTTP status | capture: sha256:61bf9184c7ac5893bb569a6cd5c8b76d0e9ad73f8bfa5cb1f23958bbe83573d2 | quote: "error": "dns"
  - [3] 2026-11-07: the probe record of the vendor page ends at DNS resolution with no HTTP status, so the prices stand as read on 2026-10-22 | capture: sha256:61bf9184c7ac5893bb569a6cd5c8b76d0e9ad73f8bfa5cb1f23958bbe83573d2 | quote: "error": "dns"
  - [4] 2026-11-07: the WHMCS cart configurator prices the 2 GB plan at EUR 10.00 monthly with EUR 0.00 setup and renders no out-of-stock notice | capture: sha256:90169ab71d82908e53bd33e29630d44c21ee8e9623cf228dd49fcd519a97c862 | quote: NVMe SSD VPS 2 GB€10,00 EUR » Data center location: Stockholm - Kista Data Center€0,00 EUR » IP Address (ipv4): 1 (included)€0,00 EUR Setup Fees:€0,00 EUR Monthly:€10,00 EUR €10,00 EUR Total Due Today
  - [1] 2026-11-07: the vendor domain swedendedicated.com answers with its VPS page, so the record's DNS-failure note does not describe the vendor | capture: sha256:5338b6c048a46cdaa7ef53fb1ad7986d6a40091779c95f33e4d3dbb526402a4a | quote: Our servers are located in separate datacenters across Sweden
  - [4] 2026-11-07: the cart page carries Login and Register links | capture: sha256:90169ab71d82908e53bd33e29630d44c21ee8e9623cf228dd49fcd519a97c862 | quote: [Register](https://billing.swedendedicated.com/register.php)
- sources:
  - [1] https://swedendedicated.com/vps/
  - [2] https://vpspricetracker.com/provider/SwedenDedi/vps
  - [3] https://swededicated.com/vps/
  - [4] https://billing.swedendedicated.com/cart.php?a=add&pid=66
