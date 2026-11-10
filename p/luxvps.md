# Luxvps

> luxvps.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/luxvps/ | JSON https://fshy.ajam.dev/api/v1/entity/luxvps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Luxvps

- `compute/luxvps` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:57.716Z (live) | stale on 2026-12-08
- url https://luxvps.net/
- price parsed USD 5.07/mo
- free tier: EUR 4.50/month (KVM Rootserver Tiny): 1 Intel Xeon vCore, 4,096 MB RAM, 30 GB NVMe, 5,120 GB (5 TB) bandwidth, 1 Gbps uplink, IPv4 + /64 IPv6, Frankfurt Germany. The vendor table row reads KVM Rootserver Tiny, Intel Xeon, 1 vCore, 4 GB, 30 GB, 5 TB, at 4.50 euros a month (pipes added here to render the row inline, the euro sign written EUR). The next steps are KVM Rootserver Starter at EUR 5.50 (2 vCores, 6 GB, 40 GB) and EPYC Tiny at EUR 6.95 (2 vCores, 8 GB, 60 GB, 10 TB). | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: the cart (billing.luxvps.net, WHMCS) prices KVM Rootserver Tiny at EUR 4.50 for 1 Month, EUR 4.28 per month for 3 Months, EUR 4.05 per month for 6 Months and EUR 3.83 per month for 12 Months, with EUR 0.00 setup and EUR 4.50 total due today on the monthly term; no renewal price is printed and the cart shows no stock marker
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB a month included per the vendor plan table (free_allowance is in GB a month); the overage price is not stated on the page read | metered: yes | free allowance: 5120 | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 5 TB a month on a shared 1 Gbps uplink; the overage price is not stated on the page read, and the 30 GB NVMe is the second wall. Quarterly to annual terms are discounted up to 15% at checkout [1]
- limits note: 5 TB a month on a shared 1 Gbps uplink; the overage price is not stated on the page read, and the 30 GB NVMe is the second wall. Quarterly to annual terms are discounted up to 15% at checkout
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: billing.luxvps.net runs the WHMCS store; the vendor documents a custom VPS panel with NoVNC console, Windows templates at no extra charge, custom ISO mount, four daily backups and a 48 hour money-back window
- composes with: EUR 4.50 buys 4 GB of RAM, 30 GB NVMe and a plan whose page states Windows Server is included at no extra charge, which is the only such statement among evaluated providers; the EPYC Tiny plan doubles the RAM to 8 GB for EUR 2.45 more, and 5 TB a month with a 30 GB disk keep either to control-plane and build work, not to the 20 TB dataset.
- reliability: no reliability event observed; the vendor claims 99.99% average uptime from 400 days of its own data and runs a public status page at status.luxvps.net, neither of which was checked.
- notes: LuxVPS provides VPS hosting in Luxembourg and Germany.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 30
  - price_on_page: EUR 4.50/month for KVM Rootserver Tiny
  - renewal_usd: not published: the cart prints the four term prices and no renewal price; read at https://billing.luxvps.net/index.php?rp=/store/kvm-rootservers/kvm-rootserver-tiny
- evidence:
  - [2] 2026-10-22: card priced at 4.50 a month (euro sign written EUR for ASCII) and quoted verbatim as '1 Intel Cores (shared)', '4,096 MB RAM', '30 GB NVMe', '5,120 GB/month bandwidth', '1 Gbps port speed', 'IPv4 + IPv6', 'Frankfurt Germany'; all 12 cards on the page carry an order link
  - [1] 2026-10-22: plan card quoted with the euro sign written EUR: 'KVM Rootserver Tiny', 'Intel Xeon', '1 vCore 4 GB RAM 30 GB NVMe 5 TB BW', 'EUR 4.50/mo', with a link to billing.luxvps.net/index.php?rp=/store/kvm-rootservers/kvm-rootserver-tiny&billingcycle=monthly
  - [1] 2026-10-22: the full KVM Rootserver table quoted with the euro sign written EUR, from 'KVM Rootserver Tiny | Intel Xeon | 1 | 4 GB | 30 GB | 5 TB | EUR 4.50/mo' to 'KVM Rootserver Ultimate | Intel Xeon | 10 | 64 GB | 350 GB | 45 TB | EUR 38.45/mo', plus the EPYC table from 'EPYC Tiny | EPYC 7763 | 2 | 8 GB | 60 GB | 10 TB | EUR 6.95/mo' to 'EPYC Elite | ... | 10 | 64 GB | 500 GB | 80 TB | EUR 59.95/mo'
  - [1] 2026-10-22: inclusions listed under 'All plans include': 1 Gbit Uplink, IPv4 + /64 IPv6, 3.2 Tbit/s Premium DDoS Protection, 4 Daily Backups, Free Setup, NVMe RAID-1, 48-hr Refund Policy; and quoted verbatim, 'quarterly, 6-month and annual terms are discounted at checkout (up to 15% off)'
  - [3] 2026-11-07: the cart prices KVM Rootserver Tiny across four billing cycles | capture: sha256:f44aceed9d6865d8f62a8eba7191e14e8426d27b8ddc2c63602f6fad9548aa6c | quote: 1 Month Price - €4.50 EUR ... 3 Month Price - €4.28 EUR ... 6 Month Price - €4.05 EUR ... 12 Month Price - €3.83 EUR
  - [3] 2026-11-07: the cart prices KVM Rootserver Tiny at EUR 4.50 on the monthly term | capture: sha256:f44aceed9d6865d8f62a8eba7191e14e8426d27b8ddc2c63602f6fad9548aa6c | quote: 1 Month Price - €4.50 EUR
  - [3] 2026-11-07: the cart prices KVM Rootserver Tiny across four terms, the 12-month term at EUR 3.83 per month, with no out-of-stock marker | capture: sha256:4db0693cf91326ae27ae45b1e8b32e2cc51008eb5de0dfd40d5e63b2fda18fb8 | quote: 1 Month Price - €4.50 EUR 3 Month Price - €4.28 EUR 6 Month Price - €4.05 EUR 12 Month Price - €3.83 EUR
  - [3] 2026-11-07: the cart prices the KVM Rootserver Tiny plan at EUR 4.50 on the monthly term | capture: sha256:f44aceed9d6865d8f62a8eba7191e14e8426d27b8ddc2c63602f6fad9548aa6c | quote: 1 Month Price - €4.50 EUR
  - [3] 2026-11-07: the cart's printed prices are the four term prices; no renewal price appears among them | capture: sha256:f44aceed9d6865d8f62a8eba7191e14e8426d27b8ddc2c63602f6fad9548aa6c | quote: 1 Month Price - €4.50 EUR ... 3 Month Price - €4.28 EUR ... 6 Month Price - €4.05 EUR ... 12 Month Price - €3.83 EUR
- sources:
  - [1] https://luxvps.net/
  - [2] https://vpspricetracker.com/provider/Luxvps/vps
  - [3] https://billing.luxvps.net/index.php?rp=/store/kvm-rootservers/kvm-rootserver-tiny
