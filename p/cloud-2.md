# cloud.mu

> cloud.mu | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloud-2/ | JSON https://fshy.ajam.dev/api/v1/entity/cloud-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cloud.mu

- `compute/cloud-mu` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:30.075Z (live) | stale on 2026-12-08
- url https://cloud.mu/linux-virtual-servers/
- free tier: Rs279/month for 1 CPU vCore, 1 GB, 32 GB SSD, 500 GB/month bandwidth, printed as 'Rs299 Rs279' with the first figure struck through. Second row Rs549 (from Rs569) for 1 vCore, 2 GB, 64 GB SSD, 700 GB/month. From the third row the bandwidth column reads 'Unmetered': Rs819 for 2 vCores, 3 GB, 128 GB SSD; Rs1,369 for 4 vCores, 6 GB, 256 GB; Rs3,279 for 8 vCores, 16 GB, 512 GB; Rs8,189 for 16 vCores, 64 GB, 1,024 GB. All servers in Mauritius, all limited to a 100 Mbps port. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 500 GB/month on the entry plan and 700 GB/month on the second; every plan from 3 GB of RAM upward prints 'Unmetered', subject to the FAQ's port-speed clause and a 100 Mbps port on all servers | metered: yes | free allowance: 500 GB per month on the entry plan | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 500 GB a month on the entry plan is the first wall, and it is the tightest transfer allowance among evaluated providers. The FAQ states no overage price and no suspension rule, only that abuse may lead to a port-speed limit, so what happens at 500 GB is unverified. Every plan also sits behind a 100 Mbps port, so throughput caps the 'Unmetered' rows before the word means much. [1]
- limits note: 500 GB a month on the entry plan is the first wall, and it is the tightest transfer allowance among evaluated providers. The FAQ states no overage price and no suspension rule, only that abuse may lead to a port-speed limit, so what happens at 500 GB is unverified. Every plan also sits behind a 100 Mbps port, so throughput caps the 'Unmetered' rows before the word means much.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM is stated in the FAQ ('As we use KVM to power our virtual hosting platform'), full admin/root access is stated on the homepage, and the buy links go to a WHMCS store at my.cloud.mu. No API appears on the page read
- composes with: Rs279 a month for 1 GB and 32 GB of SSD in Mauritius is the only host among evaluated providers with a footprint in the Indian Ocean, which makes it a low-latency front end for an audience there; 500 GB of transfer and a 100 Mbps port on every plan make it a small-site and control-plane host rather than a mover.
- reliability: no reliability event recorded
- notes: The tracker generated no page for this provider, so the record is single-sourced from the vendor. The page prints 'Rs' with no ISO currency code and no conversion is done here. One row is internally inconsistent: '| 6 CPU vCores | 8 GB | 384 GB SSD | Unmetered | Rs1,900 Rs1,909 |' prints a struck figure below the current one, which reads as a bad edit rather than a discount. The entry row's two order routes disagree: index.php?rp=/store/linux-virtual-servers/mu-lin1 answers the WHMCS out-of-stock template, while the /store/linux-vps group lists the same shape at Rs299.00 full price with a working order link, and the store's NVMe group lists the same shape at Rs299.00 hosted in South Africa. The page states 'Get up to 10% discount when ordering for 1 year or more' and prints no annual figure. Open: which product the /store/linux-vps order link configures, and whether the Rs279 promotional price applies at checkout.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 32
  - monthly_mur: 279
  - annual_mur: not published: the price table prints monthly figures only
  - renewal_mur: not published: no page read prints a renewal or month-13 sentence
  - billing_term: monthly
  - in_stock: true on the /store/linux-vps order route, whose cart resolves to the product configurator with no out-of-stock phrase; the index.php?rp=/store/linux-virtual-servers/mu-lin1 route answers the WHMCS out-of-stock template
- evidence:
  - [2] 2026-10-22: wall, quoted from the returned document: 'HTTP 404 - Provider not found.' The tracker has no page for this provider under that name, so the tracker step of the method could not run and every figure here comes from the vendor.
  - [1] 2026-10-22: table header '| CPU | Memory | Storage | Bandwidth | Price/month |' and first row '| 1 CPU vCore | 1 GB | 32 GB SSD | 500 GB/Month | Rs299 Rs279 |', second row '| 1 CPU vCore | 2 GB | 64 GB SSD | 700 GB/Month | Rs569 Rs549 |'
  - [1] 2026-10-22: rows three and up carry 'Unmetered' in the bandwidth column: '| 2 CPU vCores | 3 GB | 128 GB SSD | Unmetered | Rs839 Rs819 |', '| 4 CPU vCores | 6 GB | 256 GB SSD | Unmetered | Rs1,399 Rs1,369 |', '| 8 CPU vCores | 16 GB | 512 GB SSD | Unmetered | Rs3,299 Rs3,279 |', '| 16 CPU vCores | 64 GB | 1024 GB SSD | Unmetered | Rs8,299 Rs8,189 |'
  - [1] 2026-10-22: FAQ, quoted: 'We do not limit the amount of traffic to and from your Virtual Server. You could use 1GB or 10TB - but if we suspect abuse, we may be in touch or limit your port speed. Play fair! All servers are limited to 100Mbps port speed.'
  - [1] 2026-11-07: the vendor's price table prints the entry row at Rs299 (Mauritius) and Rs279 (South Africa) a month | capture: sha256:8276abc01fb785bbb065f2c3ea0fde36945c01c16df902c79a8545922806c448 | quote: Rs299
  - [1] 2026-11-07: the entry row's Buy Now button links the vendor's own store page for the plan | capture: sha256:8276abc01fb785bbb065f2c3ea0fde36945c01c16df902c79a8545922806c448 | quote: href="https://my.cloud.mu/store/linux-vps/1-vcpu1gb-ram32gb-nvme">Buy Now
  - [1] 2026-11-07: the vendor's price table prints the same rows: the entry row at Rs299 (Mauritius) and Rs279 (South Africa) a month | capture: sha256:8276abc01fb785bbb065f2c3ea0fde36945c01c16df902c79a8545922806c448 | quote: Rs299
  - [1] 2026-11-07: the page prints the list price and no renewal sentence | capture: sha256:8276abc01fb785bbb065f2c3ea0fde36945c01c16df902c79a8545922806c448 | quote: Rs299
  - [1] 2026-11-07: the price table still prints the entry row at Rs299 struck to Rs279 a month | capture: sha256:27f433a0667bb85a2299b879094a45708d57e06f1f17a2ac8851a80f90eb3ba4 | quote: | 1 CPU vCore | 1 GB | 32 GB SSD | 500 GB/Month | Rs299 Rs279 |
  - [1] 2026-11-07: the page states an annual discount of up to 10% but prints no annual price | capture: sha256:27f433a0667bb85a2299b879094a45708d57e06f1f17a2ac8851a80f90eb3ba4 | quote: Get up to 10% discount when ordering for 1 year or more
  - [1] 2026-11-07: the page states the billing term as monthly or annually with discounts | capture: sha256:27f433a0667bb85a2299b879094a45708d57e06f1f17a2ac8851a80f90eb3ba4 | quote: Billed monthly or annually with discounts and no hidden fees. Cancel or Upgrade at any time!
  - [3] 2026-11-07: the mu-lin1 order route answers the WHMCS out-of-stock template | capture: sha256:a65d1c5a39dc7677a11fa38d6ff7a69c43763c7dd71e95a7642e7dd17e56d8d4 | quote: We are currently out of stock on this item so orders for it have been suspended until more stock is available. For further information, please contact us.
  - [4] 2026-11-07: the store's NVMe group lists the same 1 vCPU / 1 GB / 32 GB shape at Rs299.00 a month | capture: sha256:94a5caeaea31e52a67b83ab6e91e29d0994320ef21f6696de1a3aff51a6c88b3 | quote: ### 1 vCPU/1GB RAM/32GB NVMe Starting from Rs299.00
  - [1] 2026-11-07: the price table still prints the internally inconsistent row this note describes | capture: sha256:27f433a0667bb85a2299b879094a45708d57e06f1f17a2ac8851a80f90eb3ba4 | quote: | 6 CPU vCores | 8 GB | 384 GB SSD | Unmetered | Rs1,900 Rs1,909 |
- sources:
  - [1] https://cloud.mu/linux-virtual-servers/
  - [2] https://vpspricetracker.com/provider/cloud.mu/vps
  - [3] https://my.cloud.mu/index.php?rp=/store/linux-virtual-servers/mu-lin1
  - [4] https://my.cloud.mu/store/nvme-vps-mauritius
