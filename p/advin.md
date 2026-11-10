# Advin

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/advin/ | JSON https://fshy.ajam.dev/api/v1/entity/advin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Advin

- `compute/advin` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:23.467Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/Advin/vps
- price parsed USD 6/mo
- free tier: USD 6.00/month: 2 EPYC cores (shared), 4,000 MB RAM, 64 GB NVMe, 2,000 GB/month bandwidth on a 2.4 Gbps port, IPv4 + IPv6, Johor Malaysia; the tracker slug is KVM_Premium_1_Johor_Bahru_MY. The same USD 6.00 row in Kansas City states 32,000 GB/month on the same 2.4 Gbps port, and Los Angeles states 2,000 GB/month, so the allowance is set by location and not by plan. Separately, the storage line is USD 15.00/month for 5,120 GB HDD with 2,000 MB RAM and 16,000 GB/month, USD 25.00 for 10,240 GB and USD 50.00 for 20,480 GB, all Kansas City; the largest transfer row is USD 96.00/month for 14 cores, 64,000 MB, 1,024 GB NVMe and 200,000 GB/month. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2,000 GB a month in Johor Bahru and Los Angeles, 32,000 GB a month in Kansas City at the same price. No overage price and no post-allowance throttle are stated on the pages read | metered: yes | free allowance: 2 TB per month (Johor Bahru, Los Angeles); 32 TB per month (Kansas City) | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2,000 GB a month in Johor Bahru and in Los Angeles is the first wall, and the Kansas City row at the same USD 6.00 states 32,000 GB a month, so the allowance has to be read per region rather than per plan. No overage price and no post-allowance throttle are stated on either page read, so what happens at the cap is unverified. [1]
- limits note: 2,000 GB a month in Johor Bahru and in Los Angeles is the first wall, and the Kansas City row at the same USD 6.00 states 32,000 GB a month, so the allowance has to be read per region rather than per plan. No overage price and no post-allowance throttle are stated on either page read, so what happens at the cap is unverified.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: a JSON API is documented: the vendor page shows a GET against console.advinservers.com/api/v1/client/servers/<id> with a bearer token, and lists scoped API keys with IP restrictions, power actions, rebuild, backups and resource monitoring. The page read does not document a plan-creation or billing call
- composes with: USD 6.00 for 4 GB and 64 GB of NVMe with a 2.4 Gbps port is the cheapest 4 GB plan among evaluated providers, and the Kansas City variant's 32 TB of transfer at the same price makes it a candidate for moving bytes as well as for running a small always-on worker; the Johor variant carries 2 TB, so region choice is the whole difference between those two jobs.
- reliability: no reliability event recorded
- notes: The price rests on the tracker alone, so the record is reported: the vendor's /vps page was fetched on the same date and carries no plan table. That page disagrees with itself on uptime, stating '99.99% SLA guarantee' in the plan block and '99.9% uptime SLA policy by default' further down. json covers the storage line only and is a different product. verification criteria: the same plans read from the vendor's order form, and whether the Kansas City 32 TB row is the identical plan or a separately provisioned one. Rendering and provenance: currency written as USD, and a price the page prints on one line is joined as value/period.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 64
  - term: monthly, no contract: the vendor's VPS page states 'No contract, monthly billed.'
  - annual_usd: not published: the vendor sells monthly only ('No contract, monthly billed') and its page renders no plan table; the tracker's info page prints no annual price either, its chart plots the same figure for the monthly and the annual series
  - renewal_usd: not published: the vendor bills monthly with no contract and no page prints a renewal price
  - stock: per the tracker's per-plan info pages (collected 2026-11-06): KVM Premium 1 Johor Bahru out of stock, KVM Premium 1 Kansas City in stock, KVM Premium 1 Los Angeles out of stock; the vendor's own page renders no stock state
  - monthly_usd: 6.0
  - cart_url: https://advinservers.com/vps (the tracker's Go-to-Offer for every Advin row lands there; the page renders no plan table or cart to a non-JS reader)
  - price_on_page: the vendor's VPS page prints no plan table; the tracker prints '### Advin — $6.00 / month' for the three KVM Premium 1 rows (Johor Bahru, Kansas City, Los Angeles)
- evidence:
  - [1] 2026-10-22: cheapest row, quoted: 'Advin - $6.00 / month', '2 Epyc Cores (shared)', '4,000 MB RAM', '64 GB NVMe', '2,000 GB/month bandwidth', '2.4 Gbps port speed', 'IPv4 + IPv6', 'Johor Malaysia'. The page states 'These are the cheapest VPSs currently offered by Advin, starting at $6.00 per month'.
  - [1] 2026-10-22: the second USD 6.00 row is identical except for '32,000 GB/month bandwidth' and 'Kansas U.S.A.'; the third is '2,000 GB/month bandwidth' and 'Los Angeles California U.S.A.'
  - [1] 2026-10-22: largest-storage rows: '$15.00 / month' with '5,120 GB HDD' and '16,000 GB/month bandwidth', '$25.00' with '10,240 GB HDD', '$50.00' with '20,480 GB HDD' and '48,000 GB/month'; highest-bandwidth row '$96.00 / month' with '200,000 GB/month bandwidth'
  - [2] 2026-10-22: the vendor's own plan page was read and renders no plan table: the extracted body is marketing copy, a control-panel list, and a cURL example against console.advinservers.com/api/v1. Its meta description states 'Cloud VPS on AMD Ryzen and EPYC with NVMe storage, full root access and no setup fees. From $1/GB of RAM across 6 locations.', which is a per-gigabyte floor and not a plan price.
  - [1] 2026-11-07: the tracker still lists the USD 6.00 a month rows with the 2 Epyc cores, 4,000 MB RAM, 64 GB NVMe and 2,000 GB/month figures the record states | capture: sha256:7dbeb7af646245ae76be85b71e51b7ee9c4605ff66d999d45a180d1a6e9f70f9 | quote: ### Advin — $6.00 / month
  - [1] 2026-11-07: the tracker still prints the USD 6.00 a month row with the shape and the 2,000 GB a month allowance the record states | capture: sha256:7dbeb7af646245ae76be85b71e51b7ee9c4605ff66d999d45a180d1a6e9f70f9 | quote: ### Advin — $6.00 / month cpu 2 Epyc Cores (shared) ram 4,000 MB RAM disk 64 GB NVMe bandwidth 2,000 GB/month bandwidth rj45 2.4 Gbps port speed inet IPv4 + IPv6 city Johor Malaysia
  - [2] 2026-11-07: the vendor's own billing-term statement | capture: sha256:0ca1ace9b7dda46065c5261f6d10f529f50addd8e9079f2e1ee2a544ad0dff8c | quote: High performance cloud compute, powered by KVM. No contract, monthly billed.
  - [2] 2026-11-07: the vendor sells a monthly term and prints no annual rate | capture: sha256:0ca1ace9b7dda46065c5261f6d10f529f50addd8e9079f2e1ee2a544ad0dff8c | quote: High performance cloud compute, powered by KVM. No contract, monthly billed.
  - [2] 2026-11-07: a no-contract monthly plan prints no separate renewal price | capture: sha256:0ca1ace9b7dda46065c5261f6d10f529f50addd8e9079f2e1ee2a544ad0dff8c | quote: High performance cloud compute, powered by KVM. No contract, monthly billed.
  - [3] 2026-11-07: the tracker marks the Johor Bahru row out of stock | capture: sha256:879f1eadcbe549294d4e69ce49857f0266713d77bdcc590e4b245bf9f8e9d483 | quote: | In stock now | ✘ |
  - [1] 2026-11-07: the tracker's printed monthly price | capture: sha256:7dbeb7af646245ae76be85b71e51b7ee9c4605ff66d999d45a180d1a6e9f70f9 | quote: ### Advin — $6.00 / month
  - [4] 2026-11-07: the tracker's offer link resolves to the vendor's VPS page | capture: sha256:18492c2c516e754b330c263b22e35fe98fbd325beabd814ba575f33c4d9249b8 | quote: x-web-final-url: https://advinservers.com/vps
  - [1] 2026-11-07: the tracker's printed row | capture: sha256:7dbeb7af646245ae76be85b71e51b7ee9c4605ff66d999d45a180d1a6e9f70f9 | quote: ### Advin — $6.00 / month
- sources:
  - [1] https://vpspricetracker.com/provider/Advin/vps
  - [2] https://advinservers.com/vps
  - [3] https://vpspricetracker.com/info/1937378/Advin/KVM_Premium_1_Johor_Bahru_MY
  - [4] https://vpspricetracker.com/offer/1937378/Advin/KVM_Premium_1_Johor_Bahru_MY
