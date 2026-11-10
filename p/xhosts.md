# xHosts

> xhosts.uk | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xhosts/ | JSON https://fshy.ajam.dev/api/v1/entity/xhosts.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## xHosts

- `compute/xhosts` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:00.739Z (live) | stale on 2026-12-08
- url https://xhosts.uk/budget-vps-uk
- price parsed USD 4.68/mo
- free tier: Budget 1G at GBP 3.50 a month in the cart ('Monthly£3.50 GBP'), setup fee GBP 0.00, cart subtotal GBP 3.50, in stock (the cart accepts the item): 1 vCPU Intel Xeon E5-2630v4, 1 GB dedicated RAM, 30 GB SSD, 1 Gbps, 5 TB bandwidth, 1 IPv4 + /64 IPv6, in Maidenhead, Manchester or Glasgow. Annual and renewal prices not published on the pages read 2026-11-07 (the cart's billing-cycle dropdown options did not render). Higher Budget tiers sit above it; their prices are quoted in the record's evidence rows. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB a month on Budget 1G, stated by the vendor's cart page read 2026-11-07 ('5 TB Bandwidth'), at a 1 Gbps port; the marketing page prints no bandwidth for this plan and the next tier up prints a larger allowance. The tracker's monthly figure agrees to GB/TB rounding. No overage price is stated | metered: yes | free allowance: 5 TB a month (vendor cart, read 2026-11-07) | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 5 TB a month on Budget 1G, now stated by the vendor's own cart ('5 TB Bandwidth' with a 1 Gbps connection); the tracker's monthly figure agrees to rounding. The next tier up prints a larger allowance, so the allowance rises with the plan. No overage price is stated. [1]
- limits note: 5 TB a month on Budget 1G, now stated by the vendor's own cart ('5 TB Bandwidth' with a 1 Gbps connection); the tracker's monthly figure agrees to rounding. The next tier up prints a larger allowance, so the allowance rises with the plan. No overage price is stated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: order links go to my.xhosts.uk; the site carries a knowledgebase, a looking glass at /lg/ and a ticket form. No API appears on the page read
- composes with: GBP 3.50 for 1 GB with 5 TB of transfer in three UK cities is a cheap UK presence for a latency-sensitive front end or a mail relay near its users; the 2 GB row at GBP 5.50 is the better buy because it is the first plan the vendor actually specifies, at 8 TB, and the 1G plan's specs rest on the tracker alone
- reliability: no reliability event recorded
- notes: Wall: https://xhosts.uk/vps/ returns a 404 'That route reached a dead end. /vps/' and the real plan page is /budget-vps-uk, found from the homepage link. The vendor page confirms the price and the three locations but prints no cores, RAM, disk or bandwidth for Budget 1G, so the shape fields in this record come from the tracker and the record is documented only for the price; that split is deliberate and is the one weakness here. The homepage's third block 'From GBP 3.00 /month' has no heading in the extract, so it is not attributed to a product. Unverified: the Budget 1G specification from the vendor's order form, and whether the GBP 3.50 is a from-price that a location surcharge moves.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 30
  - price_on_page: GBP 3.50/month for Budget 1G VPS
  - renewal_usd: not published: the cart prints the monthly price and no renewal figure; the billing-cycle dropdown options did not render
- evidence:
  - [2] 2026-10-22: cheapest row, quoted: 'xHosts - GBP 3.50 / month', '1 Intel Cores (shared)', '1,024 MB RAM', '30 GB SSD', '5,120 GB/month bandwidth', '1 Gbps port speed', 'IPv4 + IPv6', 'Maidenhead United Kingdom'; product slug Budget_1G_VPS. The page states 'These are the cheapest VPSs currently offered by xHosts, starting at GBP 3.50 per month'.
  - [1] 2026-10-22: plan block, quoted: 'Budget 1G', 'Lightweight websites and development projects.', 'From', 'GBP 3.50/month', 'Maidenhead - Manchester - Glasgow'. The specification bullets that follow belong to the next card, 'Budget 2G', and no bullets sit under the 1G block.
  - [1] 2026-10-22: 'Budget 2G' at 'GBP 5.50/month' with '- 1 vCPU Intel Xeon - 2GB dedicated RAM - 50GB SSD storage - 1Gbps network - 8TB bandwidth - 1 IPv4 address'; 'Budget 4G' at 'GBP 10.00/month' with '4GB dedicated RAM' and '75GB SSD storage'; 'Budget 128G' at 'GBP 100.00/month' with '128GB dedicated RAM' and '1000GB SSD storage'
  - [3] 2026-10-22: homepage blocks, quoted: 'Budget VPS From GBP 3.50 /month ... View VPS plans', 'AMD EPYC VPS From GBP 4.00 /month', and a third block 'From GBP 3.00 /month' whose heading is not in the extract
  - [4] 2026-11-07: the cart prices Budget 1G VPS at GBP 3.50 monthly | capture: sha256:6d15bd15693dd4b393ab51d7ebab16e7a3b02cb230b6801ef42aaf146380d02d | quote: Monthly£3.50 GBP
  - [4] 2026-11-07: no setup fee in the cart | capture: sha256:6d15bd15693dd4b393ab51d7ebab16e7a3b02cb230b6801ef42aaf146380d02d | quote: Setup Fee£0.00 GBP
  - [4] 2026-11-07: the cart names a subtotal line, GBP 3.50, for Budget 1G VPS | capture: sha256:6d15bd15693dd4b393ab51d7ebab16e7a3b02cb230b6801ef42aaf146380d02d | quote: Cart subtotal today:
  - [4] 2026-11-07: the vendor's own cart states the bandwidth for Budget 1G VPS | capture: sha256:6d15bd15693dd4b393ab51d7ebab16e7a3b02cb230b6801ef42aaf146380d02d | quote: 5 TB Bandwidth
  - [4] 2026-11-07: the vendor's own cart states the Budget 1G CPU | capture: sha256:6d15bd15693dd4b393ab51d7ebab16e7a3b02cb230b6801ef42aaf146380d02d | quote: 1 vCPU Intel Xeon E5-2630v4
  - [1] 2026-11-07: the marketing page still prints Budget 1G from GBP 3.50/month | capture: sha256:217e341b96cf637ef19f3a28f2d37fa1be5c2d96c8c719acacad0b9d11e3f901 | quote: £3.50/month
  - [4] 2026-11-07: the vendor's own cart states the allowance | capture: sha256:6d15bd15693dd4b393ab51d7ebab16e7a3b02cb230b6801ef42aaf146380d02d | quote: 5 TB Bandwidth
  - [4] 2026-11-07: the entry plan price is unchanged in the cart | capture: sha256:6d15bd15693dd4b393ab51d7ebab16e7a3b02cb230b6801ef42aaf146380d02d | quote: Monthly£3.50 GBP
  - [4] 2026-11-07: the vendor's own cart prices Budget 1G VPS at GBP 3.50 monthly | capture: sha256:6d15bd15693dd4b393ab51d7ebab16e7a3b02cb230b6801ef42aaf146380d02d | quote: Monthly£3.50 GBP
- sources:
  - [1] https://xhosts.uk/budget-vps-uk
  - [2] https://vpspricetracker.com/provider/xHosts/vps
  - [3] https://xhosts.uk/
  - [4] https://my.xhosts.uk/?cmd=cart&action=add&id=680
