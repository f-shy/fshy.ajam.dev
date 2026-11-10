# Zade_Servers

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zade-servers/ | JSON https://fshy.ajam.dev/api/v1/entity/zade-servers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zade_Servers

- `compute/zade-servers` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:00.739Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/Zade_Servers/vps
- price parsed USD 3.5/mo
- free tier: DE-MEM-KVM-NVMe-2 at USD 3.50 per month at every billing term the cart prints (1, 3, 6 and 12 months all USD 3.50): 1 vCore @ 3.40+ GHz, 2 GB DDR4, 20 GB NVMe, unmetered bandwidth @ 1 Gbit/s (shared), 1 IPv4, in Germany. Cart read 2026-11-07: setup fee USD 0.00, total due today USD 3.50, item accepted ('Added to Cart'); renewal price not published. The category page prices the memory line from USD 3.50 upward; the tracker's prices for the sibling plans sit inside that range. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Unmetered bandwidth @ 1 Gbit/s (shared) on the entry memory plan, stated by the vendor's cart page read 2026-11-07; the tracker's monthly quota figure (2026-10-22) appears on no vendor page read. | metered: yes | free allowance: unmetered @ 1 Gbit/s shared (vendor cart, read 2026-11-07) | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): The vendor's cart states 'Unmetered Bandwidth @ 1 Gbit/s (shared)' for the entry memory plan; the tracker's monthly quota figure contradicts it and appears on no vendor page. The vendor documents no byte quota; the shared port is the wall its pages name. [1]
- limits note: The vendor's cart states 'Unmetered Bandwidth @ 1 Gbit/s (shared)' for the entry memory plan; the tracker's monthly quota figure contradicts it and appears on no vendor page. The vendor documents no byte quota; the shared port is the wall its pages name.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: WHMCS portal at my.zadeservers.net: the store category pages print specs and prices (read 2026-11-07) and the cart flow renders billing cycles, an order summary and a total; no API is documented.
- composes with: Unmetered bandwidth on a shared 1 Gbit/s with 2 GB of RAM at USD 3.50 a month in Germany is a strong bandwidth-to-price ratio; the plan suits a mirror or a caching node, and long-lived state belongs elsewhere.
- reliability: no reliability event recorded
- notes: The reads of 2026-10-22 hit a JavaScript portal home with no plan table; the store host my.zadeservers.net is readable without it: as of 2026-11-07 the memory-optimized category page prints the memory line's full price ladder and the entry plan's cart renders every billing term at USD 3.50 with setup USD 0.00 and the item accepted. The entry price is first-party now; renewal is not published.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 20
  - price_on_page: USD 3.50/month for DE-MEM-KVM-NVMe-2
  - renewal_usd: not published: the cart prints every billing term at USD 3.50 and no separate renewal figure
- evidence:
  - [1] 2026-10-22: 'These are the cheapest VPSs currently offered by Zade Servers, starting at $3.50 per month' and the row '$3.50 / month 1 Ryzen Cores (shared) 2,048 MB RAM 20 GB NVMe 51,200 GB/month bandwidth 1 Gbps port speed IPv4 Germany' as plan DE_MEM_KVM_NVMe_2
  - [1] 2026-10-22: sibling rows: '$5.50 / month 1 Ryzen Cores (shared) 2,048 MB RAM 50 GB NVMe 51,200 GB/month bandwidth 10 Gbps' as DE_COMPUTE_KVM_NVMe_2, and '$6.00 / month 1 Ryzen Cores (shared) 4,096 MB RAM 40 GB NVMe' as DE_MEM_KVM_NVMe_4
  - [2] 2026-11-07: the cart prints USD 3.50 for every billing term of DE-MEM-KVM-NVMe-2 | capture: sha256:89294eb37bb16dd05987c40f3f8ff144eefe0ac45fda7afcd3aef8d2edbeb291 | quote: 1 Month Price - $3.50 USD 3 Month Price - $3.50 USD 6 Month Price - $3.50 USD 12 Month Price - $3.50 USD
  - [3] 2026-11-07: the vendor's category page prices the entry memory plan from $3.50 USD monthly | capture: sha256:141cb9fab626076de5979ccab216d2c895debdc9631f90f4ca0cd56975ca140b | quote: <span class="price">$3.50 USD</span>
  - [2] 2026-11-07: the cart's order summary prices the plan monthly at USD 3.50 | capture: sha256:89294eb37bb16dd05987c40f3f8ff144eefe0ac45fda7afcd3aef8d2edbeb291 | quote: Monthly: $3.50 USD
  - [2] 2026-11-07: the cart totals USD 3.50 due today | capture: sha256:89294eb37bb16dd05987c40f3f8ff144eefe0ac45fda7afcd3aef8d2edbeb291 | quote: $3.50 USD Total Due Today
  - [2] 2026-11-07: the cart accepts the plan, no out-of-stock marker | capture: sha256:89294eb37bb16dd05987c40f3f8ff144eefe0ac45fda7afcd3aef8d2edbeb291 | quote: Added to Cart
  - [2] 2026-11-07: the vendor's cart states unmetered bandwidth on a shared 1 Gbit/s port | capture: sha256:89294eb37bb16dd05987c40f3f8ff144eefe0ac45fda7afcd3aef8d2edbeb291 | quote: Unmetered Bandwidth @ 1 Gbit/s (shared)
  - [2] 2026-11-07: the vendor's own cart states the bandwidth term | capture: sha256:89294eb37bb16dd05987c40f3f8ff144eefe0ac45fda7afcd3aef8d2edbeb291 | quote: Unmetered Bandwidth @ 1 Gbit/s (shared)
  - [2] 2026-11-07: the quota the old text relied on is contradicted by the vendor's own cart | capture: sha256:89294eb37bb16dd05987c40f3f8ff144eefe0ac45fda7afcd3aef8d2edbeb291 | quote: Unmetered Bandwidth @ 1 Gbit/s (shared)
  - [3] 2026-11-07: the store pages render specs and prices | capture: sha256:141cb9fab626076de5979ccab216d2c895debdc9631f90f4ca0cd56975ca140b | quote: <span class="price">$3.50 USD</span>
  - [2] 2026-11-07: the cart read supersedes the earlier wall note | capture: sha256:89294eb37bb16dd05987c40f3f8ff144eefe0ac45fda7afcd3aef8d2edbeb291 | quote: Added to Cart
  - [2] 2026-11-07: the entry plan price is unchanged in the cart | capture: sha256:89294eb37bb16dd05987c40f3f8ff144eefe0ac45fda7afcd3aef8d2edbeb291 | quote: 1 Month Price - $3.50 USD 3 Month Price - $3.50 USD 6 Month Price - $3.50 USD 12 Month Price - $3.50 USD
  - [2] 2026-11-07: the vendor's own cart prices the entry memory plan at USD 3.50 monthly | capture: sha256:89294eb37bb16dd05987c40f3f8ff144eefe0ac45fda7afcd3aef8d2edbeb291 | quote: Monthly: $3.50 USD
  - [2] 2026-11-07: the cart prints the same USD 3.50 for every billing term and no renewal figure | capture: sha256:89294eb37bb16dd05987c40f3f8ff144eefe0ac45fda7afcd3aef8d2edbeb291 | quote: 1 Month Price - $3.50 USD 3 Month Price - $3.50 USD 6 Month Price - $3.50 USD 12 Month Price - $3.50 USD
- sources:
  - [1] https://vpspricetracker.com/provider/Zade_Servers/vps
  - [2] https://my.zadeservers.net/cart.php?a=add&pid=84
  - [3] https://my.zadeservers.net/store/memory-optimized-nvme-kvm-de
