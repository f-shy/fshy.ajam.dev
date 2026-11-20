# UniHost

> unihost.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unihost/ | JSON https://fshy.ajam.dev/api/v1/entity/unihost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UniHost

- `compute/unihost` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://unihost.com/vps/germany/
- free tier: LVP-G1 at EUR 6.90 per month excluding VAT, sold in Germany or the Netherlands: 4 AMD EPYC vCores (shared), 6 GB RAM, 100 GB SSD, 10 Gbps port, 30 TB* a month of traffic. The same row carries USD 7.74 and GBP 5.80 a month on the page. LVP-G2 is 6 vCore, 16 GB RAM, 200 GB SSD at EUR 12 a month in the same two countries. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 30 TB* a month of traffic on a 10 Gbps port; no per-GB rate and no overage price stated on the page read | metered: yes | free allowance: 30 TB a month, printed as '30 TB*' | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 30 TB a month, printed as '30 TB*', on a 10 Gbps port. The asterisk is not explained on the page read, so the allowance may carry a fair-use term that was not read. [1]
- limits note: 30 TB a month, printed as '30 TB*', on a 10 Gbps port. The asterisk is not explained on the page read, so the allowance may carry a fair-use term that was not read.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read; the vendor documents a dashboard cart and no client or API in the material read
- composes with: 4 vCores and 6 GB for EUR 6.90 with a 30 TB allowance is the cheapest per-core shape among documented hosts; it suits a scheduler or a scraper front end that bursts, with bulk bytes pushed to an unmetered host
- reliability: no reliability event recorded
- notes: The tracker's row and the vendor's row agree on price and shape, so this is one of the few lane entries where a third-party table and the first-party page can be checked against each other and both hold. The vendor row is 'ex.VAT' and the buyer's VAT position was not read. Unverified: whether the '30 TB*' asterisk hides a fair-use throttle, and whether the Germany and Netherlands rows are the same product.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 6
  - facets.shape.disk_gib: 100
- evidence:
  - [1] 2026-10-22: LVP-G1 row: '4 vCore / AMD EPYC / Shared', '6 GB RAM', '100 GB SSD', '10 Gbps 30 TB*', with data-prices_for_filter="{USD:7.74, EUR:6.90, GBP:5.80}" and the EUR column headed 'Price, EUR / mo.ex.VAT'
  - [1] 2026-10-22: 'LVP-G2 / DE NL / 6 vCore AMD EPYC / Shared / 16 GB RAM / 200 GB SSD / 10 Gbps 30 TB*' at EUR 12 a month in the same table
  - [2] 2026-10-22: tracker agrees: 'These are the cheapest VPSs currently offered by UniHost, starting at EUR 6.90 per month' with 4 Epyc cores (shared), 6,144 MB RAM, 100 GB SSD, 30,720 GB/month, 10 Gbps, Germany
- sources:
  - [1] https://unihost.com/vps/germany/
  - [2] https://vpspricetracker.com/provider/UniHost/vps
