# LowHosting

> lowhosting.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lowhosting/ | JSON https://fshy.ajam.dev/api/v1/entity/lowhosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LowHosting

- `compute/lowhosting` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:57.716Z (live) | stale on 2026-12-08
- url https://lowhosting.com/kvm-vps.php?gid=23
- price parsed USD 3.38/mo
- free tier: EUR 3.00/month (RKVMProtected, 1 GB): 1 Ryzen 9 5950X core (shared), 1,024 MB RAM, 20 GB NVMe, traffic stated as 'Unlimited*2' with a footnote, 0.2 Gbps port, IPv4 and IPv6, Germany. The tracker states 51,200 GB/month for the same plan. The EUR 2.00 OpenVZ plan the tracker lists first has no order link, and the EUR 4.00 plan is also without one. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: the cart (lowhosting.org/clientarea, WHMCS) prices RKVMPROTECTED1 at EUR 3.00 monthly, EUR 9.00 quarterly, EUR 18.00 semi-annually and EUR 36.00 annually, with no biennial or triennial term, EUR 0.00 setup and EUR 3.00 total due today on the monthly term; the cart's product description states Bandwidth Unlimited without the footnote marker the vendor table carries; no renewal price is printed and the cart shows no stock marker
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the vendor table says 'Unlimited*2' with a footnote that did not render in the extracted table; the tracker states 51,200 GB a month (free_allowance is in GB a month). Neither page states an overage price | metered: yes | free allowance: 51200 | source: [2]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): the vendor table says 'Unlimited*2' and the footnote text did not render, while the tracker states 51,200 GB a month; take 51.2 TB as the allowance until the footnote is read. The 200 Mbps port is the tighter limit for bulk transfer, and the 20 GB NVMe caps local caching [1]
- limits note: the vendor table says 'Unlimited*2' and the footnote text did not render, while the tracker states 51,200 GB a month; take 51.2 TB as the allowance until the footnote is read. The 200 Mbps port is the tighter limit for bulk transfer, and the 20 GB NVMe caps local caching
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: WHMCS cart at lowhosting.org/clientarea while the marketing site is lowhosting.com, so the order domain differs from the site domain; three product families chosen before the plan table; anti-DDoS included on every plan
- composes with: EUR 3 for 1 GB and 20 GB NVMe is the lowest euro price among evaluated providers, and the 200 Mbps port plus a 20 GB disk make it a control node or a proxy exit rather than a store; the same table's 12 GB plan at EUR 16 carries a lower price per GB of RAM than the entry plan, so the entry plan is not where the value is if the workload is memory-bound.
- reliability: no reliability event recorded
- notes: LowHosting provides budget VPS hosting.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
  - price_on_page: EUR 3.00/month for RKVMPROTECTED1
  - renewal_usd: not published: the cart prints the four billing-cycle prices and no renewal price; read at https://lowhosting.org/clientarea/index.php?rp=/store/rkvmprotected/rkvmprotected1
- evidence:
  - [1] 2026-10-22: row quoted with the euro sign written EUR: 'Germany | 1 GB | 1 (Ryzen 9 5950X*1) | Unlimited*2 | 20 GB | Included | EUR 3/mo', with an order link to lowhosting.org/clientarea/cart.php?a=add&pid=128; the same table runs to 48 GB at EUR 64/mo
  - [1] 2026-10-22: the vendor's page is one of three product families listed on /kvm-vps: IKVMProtected (Intel i9), RKVMProtected (AMD Ryzen) and XKVMProtected (Intel Xeon), each described as including 'advanced Anti-DDoS protection'
  - [2] 2026-10-22: card quoted at 'EUR 3.00 / month' with the euro sign written EUR, '1 Ryzen Cores (shared)', '1,024 MB RAM', '20 GB NVMe', '51,200 GB/month bandwidth', '0.2 Gbps port speed', 'Germany'; the EUR 2.00 OpenVZ card above it renders Go as a disabled span with no order link
  - [3] 2026-11-07: the cart prices RKVMPROTECTED1 across four billing cycles | capture: sha256:f4cc7b4a15361e6eff1391b97e169256e3a08a8243733ccae269979b71c88b48 | quote: €3,00 EUR Monthly ... €9,00 EUR Quarterly ... €18,00 EUR Semi-Annually ... €36,00 EUR Annually
  - [3] 2026-11-07: the cart lists RKVMPROTECTED1 with 1 core, 1 GB RAM, 20 GB NVMe, 200 Mbps at EUR 3.00 monthly | capture: sha256:f4cc7b4a15361e6eff1391b97e169256e3a08a8243733ccae269979b71c88b48 | quote: RKVMPROTECTED1 ... 1 Core (Ryzen 9 5950X) ... RAM 1 GB ... 20 GB NVMe ... 200 Mbps ... €3,00 EUR Monthly
  - [4] 2026-11-07: the cart prices the annual term of RKVMPROTECTED1 at EUR 36.00 with EUR 0.00 setup and no out-of-stock marker | capture: sha256:0c0f494c32421161f07cd2c384af7be090105fa128d9a936b9f21ed11979fddd | quote: Annually: €36,00 EUR €36,00 EUR Total Due Today
  - [3] 2026-11-07: the cart prices RKVMPROTECTED1 at EUR 3.00 on the monthly term | capture: sha256:f4cc7b4a15361e6eff1391b97e169256e3a08a8243733ccae269979b71c88b48 | quote: RKVMPROTECTED1 ... 1 Core (Ryzen 9 5950X) ... RAM 1 GB ... 20 GB NVMe ... 200 Mbps ... €3,00 EUR Monthly
  - [3] 2026-11-07: the cart's printed prices are the four billing-cycle prices; no renewal price appears among them | capture: sha256:f4cc7b4a15361e6eff1391b97e169256e3a08a8243733ccae269979b71c88b48 | quote: €3,00 EUR Monthly ... €9,00 EUR Quarterly ... €18,00 EUR Semi-Annually ... €36,00 EUR Annually
  - [3] 2026-11-07: the cart prices RKVMPROTECTED1 at EUR 3.00 monthly with the 1 core / 1 GB / 20 GB NVMe shape | capture: sha256:f4cc7b4a15361e6eff1391b97e169256e3a08a8243733ccae269979b71c88b48 | quote: RKVMPROTECTED1 ... 1 Core (Ryzen 9 5950X) ... RAM 1 GB ... 20 GB NVMe ... 200 Mbps ... €3,00 EUR Monthly
- sources:
  - [1] https://lowhosting.com/kvm-vps.php?gid=23
  - [2] https://vpspricetracker.com/provider/LowHosting/vps
  - [3] https://lowhosting.org/clientarea/index.php?rp=/store/rkvmprotected/rkvmprotected1
  - [4] https://lowhosting.org/clientarea/index.php?rp=/store/rkvmprotected/rkvmprotected1&billingcycle=annually
