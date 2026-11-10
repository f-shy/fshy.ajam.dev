# SixtyNet

> sixtynet.net | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sixtynet/ | JSON https://fshy.ajam.dev/api/v1/entity/sixtynet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SixtyNet (sixtynet.net)

- `ip-proxy/sixtynet-residential-vps` | paid-only | evidence reported | binding none | category ISP-registered VPS | tier Residential VPS, 2 to 8 core, US Los Angeles (AT&T network, Cox or Astound double-ISP option)
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:35:32.672Z (live) | stale on 2026-11-18
- url https://sixtynet.net/
- free tier: No free tier. A trade site's 2025-10-22 reading of the vendor's offer lists four residential plans on a 10 Gbps port with one IPv4: 2 core, 2 GB, 40 GB NVMe, 5 TB a month at 15 USD a month; 4 core, 4 GB, 80 GB, 10 TB at 35 USD; 8 core, 8 GB, 160 GB, 20 TB at 75 USD; 8 core, 16 GB, 320 GB, 40 TB at 155 USD. The default network is a single-ISP AT&T line and 5 USD more selects a Cox Residential or Astound double-ISP address. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: unverified on the vendor's own pages: the vendor's home page at sixtynet.net renders no plan or price text, and its residential page paths returned 404. The figures are the trade site's reading dated 2025-10-22.
- per-object cap: not applicable | source: [1]
- retention: not applicable: a rented machine and its address, not stored bytes | source: [1]
- egress: A monthly allowance of 5 TB, 10 TB, 20 TB or 40 TB by plan on a 10 Gbps port, per the trade site's reading. No overage price was read. | metered: yes | free allowance: 5 TB per month on the 15 USD plan, per a trade site's reading | source: [1]
- identity: email | detail: unverified: the sign-up and checkout pages were not read. The kind records an email as the floor.
- interface: unknown
- limits:
  - volume-quota: 5 TB per month on the 15 USD plan, up to 40 TB on the 155 USD plan, per a trade site [1]
- limits note: The address class is the live question. The trade site's own postscript says readers report the addresses are no longer AT&T residential, and a forum review list says the vendor lost its residential property after an ASN change. The vendor's home page names a single region, US East (Los Angeles).
- binding note: No byte limit binds a low-volume exit. What decides the record is whether the addresses are still residential, and the vendor's pages do not say.
- interface detail: A KVM virtual machine with one IPv4 (the vendor's FAQ states KVM virtualization and a free 24/7 ticket support). The access method for the residential line is not stated on the pages read.
- tooling: An SSH or RDP client plus a proxy or tunnel daemon the user installs on the machine. The vendor publishes no proxy endpoint on the pages read.
- composes with: A Worker opens an outbound connection to the machine's IPv4 and the machine makes the upstream request, so the upstream sees an address on the AT&T, Cox or Astound network the plan names instead of AS13335. The trade site says the residential line does not open ports 80 and 443 and blocks ping.
- reliability: A trade site warns readers to check with the vendor before buying because some say the addresses are no longer AT&T residential. A forum review list marks the vendor as formerly the best value, with its residential property lost after an ASN change.
- notes: The vendor domain is sixtynet.net. The record names the contested address class, not a verdict on it: two third-party sources say the AT&T residential line changed, and no registry lookup was possible because no test address is published.
- evidence note: Reported. Prices and plan rows come from one trade-site post dated 2025-10-22, the residential property is contested by two third-party sources, and the vendor's own pages gave no plan text. Nothing was measured and no test address is published.
- extras:
  - rung: 5
  - rung_note: The offer is a claim about the address class and the class is contested by third parties.
- evidence:
  - [1] 2026-11-03: the default line is a single-ISP AT&T residential VPS and 5 USD more selects a Cox or Astound double-ISP address | capture: sha256:62c58dc7f1b6c69a4232cd2fc9bd3a75e8ad63427b07fe7ea6f1f443e63170af | quote: SixtyNet美国ATT线路住宅VPS，默认是单ISP，加5美元可升级成Cox或者Astound双ISP住宅IP
  - [1] 2026-11-03: the four plan prices are 15, 35, 75 and 155 USD a month | capture: sha256:62c58dc7f1b6c69a4232cd2fc9bd3a75e8ad63427b07fe7ea6f1f443e63170af | quote: | 15美元/月 | 35美元/月 | 75美元/月 | 155美元/月 |
  - [1] 2026-11-03: the monthly allowances are 5, 10, 20 and 40 TB | capture: sha256:62c58dc7f1b6c69a4232cd2fc9bd3a75e8ad63427b07fe7ea6f1f443e63170af | quote: | 5TB月流量 | 10TB月流量 | 20TB月流量 | 40TB月流量 |
  - [1] 2026-11-03:  | capture: sha256:62c58dc7f1b6c69a4232cd2fc9bd3a75e8ad63427b07fe7ea6f1f443e63170af | quote: 由于IP风险控制原因，住宅IP产品不开放80和443端口，并且禁止ping
  - [1] 2026-11-03: readers report the addresses are no longer AT&T residential | capture: sha256:62c58dc7f1b6c69a4232cd2fc9bd3a75e8ad63427b07fe7ea6f1f443e63170af | quote: 有读者反应现在不是ATT的住宅IP了，大家入手前请发工单和商家确认
  - [2] 2026-11-03: a forum review list says the residential property was lost after an ASN change | capture: sha256:d87221c7a0ade538abdee839d90e04a75a376eb9e055f9afce7daeb8a53a2416 | quote: ASN 改动后家宽属性丧失
  - [3] 2026-11-03: the vendor's home page advertises residential-IP VPS and dedicated servers | capture: sha256:88e68c14060e32a40b4e079a67a24539baca4558d05562210b0d5664c0cab32d | quote: Order VPS or dedicated servers with Residential IPs and boost trust due to their linkage to real homes and avoid potential web restrictions.
  - [3] 2026-11-03: the vendor names a single region | capture: sha256:88e68c14060e32a40b4e079a67a24539baca4558d05562210b0d5664c0cab32d | quote: SixtyNet infrastructure has been launched in US East (Los Angeles).
- sources:
  - [1] https://www.vpsxxs.com/sixtynet20251022/
  - [2] https://www.nodeseek.com/post-321780-1
  - [3] https://sixtynet.net/
