# Millenial

> mlnl.host | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mlnl/ | JSON https://fshy.ajam.dev/api/v1/entity/mlnl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Millenial

- `compute/millenial` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:57.716Z (live) | stale on 2026-12-08
- url https://mlnl.host/
- price parsed USD 4/mo
- free tier: HK KVM NAT 512M at USD 4.00/month on the cart ('Starting from $4.00USD Monthly'): 1 vCPU, 512 MB RAM, 5 GB storage, 1 TB bandwidth, 1 Gbps, NAT IPv6-only with no IPv4, Hong Kong; in stock (Order Now, no stock badge, on a cart page that marks sold-out plans '0 Available ... Out of Stock'). Annual: not published. Renewal: not published. Term: monthly. The 1 GB NAT plan is USD 5.00/month on the cart and in stock; the 20 GB NAT unmetered plan is USD 15.00/month on the cart; HK-KVM-DDoS-1G (USD 7.00), HK-KVM-512M (USD 4.00) and HK-KVM-1G-v2 (USD 5.00) show '0 Available' and 'Out of Stock' on the same cart page. The UK line's cart price and the storefront's promo rows are in the evidence rows. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month included per the vendor plan table (free_allowance is in GB a month); the overage price is not stated on the page read | metered: yes | free allowance: 1000 | source: [1]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): 1 TB a month, and the plan has no IPv4 address at all, so it cannot serve inbound traffic without a relay; the 5 GB SSD is the tightest disk among evaluated providers. [1]
- limits note: 1 TB a month, and the plan has no IPv4 address at all, so it cannot serve inbound traffic without a relay; the 5 GB SSD is the tightest disk among evaluated providers.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the storefront is a single page with a tab per location and a promo code per plan; NAT plans come with no IPv4, so a public service needs the non-NAT, UK or Netherlands lines; nothing is documented about an API or CLI on the page read
- composes with: USD 4 for 512 MB and 5 GB behind NAT is a throwaway runner, a tunnel endpoint or a probe target, not a host with a public address; there is no US location on the list at all, and the only interesting shape is the UK 2 GB unmetered plan at USD 8.00 on promo
- reliability: no reliability event recorded
- notes: The storefront shows the recorded plan at USD 5 struck to USD 4 a month with code MILLENIAL40, and the cart prices it at the same USD 4 without a code, so the cart price already includes the discount; whether a renewal re-prices to the list USD 5 is not published. The storefront's 20 GB NAT unmetered row reads USD 12 struck to USD 7 with MILLENIAL40; the cart prices that shape higher (see the free-tier text). The order button for the recorded plan is cart.php?a=add&pid=18 on both the storefront and the cart page. Whether the unmetered plans have a fair-use cap in the terms is not published on the pages read. The page header now reads 'UP TO 55% OFF'; the header's earlier 'Starting at' figure is gone from the page as read.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.disk_gib: 5
  - price_on_page: USD 4.00/month for HK-KVM-NAT-512M
  - renewal_usd: not published: the cart prices USD 4.00 on the monthly term and prints no renewal price; read at https://www.millenial.host/portal/store/promos
- evidence:
  - [1] 2026-10-22: row quoted: '1 vCPU | 512 MB | 1 core | 5GB | NAT | 1 TB (1000 GB) - 1 Gbps | $5 | $4 /month | On sale - Save 20% | Promo code - MILLENIAL40', with an order button in the Hong Kong tab
  - [1] 2026-10-22: the Hong Kong tab's other rows: 1 vCPU / 1 GB / 10 GB NAT / 3 TB at 8.5 down to 5, and 1 vCPU / 1 GB / 20 GB NAT / unmetered at 12 down to 7, in the same currency per month; the UK tab's first row is quoted as '2 vCPU | 2GB | 1 core | 50GB | Unmetered | 1 Gbps | $10 | $8 /month ... Promo code - MLNL-UK-20'
  - [2] 2026-10-22: card quoted: '$4.00 / month', '1 Intel Cores (shared)', '512 MB RAM', '5 GB SSD', '1,000 GB/month bandwidth', '1 Gbps port speed', '(NAT) IPv6', 'Hong Kong'; the page lists five locations: Hong Kong, Lithuania, Netherlands, Switzerland and the United Kingdom
  - [3] 2026-11-07: the cart's Promotions (HK) page prices HK-KVM-NAT-512M at USD 4.00 a month, monthly term, with no stock badge | capture: sha256:74ad2e1b1f3bd54462734ef798933fdcdea55c751140a4a403e64d99bce60bd5 | quote: HK-KVM-NAT-512M Starting from $4.00USD Monthly 1 vCPU Cores 5 GB Storage 512 MB RAM 1TB Bandwidth 1 Gbps Network No Public IPv4 (NAT Only)
  - [1] 2026-11-07: the storefront's recorded row reads list USD 5 struck to USD 4 a month with promo code MILLENIAL40 | capture: sha256:c1d97c88f2b6bb13e18cdc51d2f1c8b189129762d5cc367d9f182933e258cdb6 | quote: $5 $4/month On sale - Save 20% Promo code - MILLENIAL40
  - [4] 2026-11-07: the cart's UK page prices UK-2G at USD 10.00 a month, in stock | capture: sha256:3346b90a0551cd5ad096669c7017f2ae3673a13868e2f53847950cc3b8fe74ae | quote: UK-2G $10.00USD Monthly 3.0 GHz+ Intel Core i9 2 vCPU Cores 50 GB NVMe SSD 2 GB DDR4 RAM Unmetered* Bandwidth 10 Gbps Network
  - [3] 2026-11-07: the cart's Promotions (HK) page prices HK-KVM-NAT-512M (product1) starting at USD 4.00 on the Monthly term; the same page prices the 1 GB NAT plan at USD 5.00 and the 20 GB NAT unmetered plan at USD 15.00 | capture: sha256:a5eddb7157ec1852d224b2bcc5f1c852029844f62f6f2b5f7a406b0ca1c89936 | quote: <span class="price">$4.00USD</span>
  - [3] 2026-11-07: the cart page renders an Order Now button for HK-KVM-NAT-512M (pid=18) with no out-of-stock marker on the plan; the three sold-out HK plans show 0 Available and Out of Stock | capture: sha256:a5eddb7157ec1852d224b2bcc5f1c852029844f62f6f2b5f7a406b0ca1c89936 | quote: <a href="/portal/cart.php?a=add&amp;pid=18" class="btn outline-btn" id="product1-order-button"> Order Now </a>
  - [3] 2026-11-07: the cart prices HK-KVM-NAT-512M at USD 4.00 on the monthly term | capture: sha256:74ad2e1b1f3bd54462734ef798933fdcdea55c751140a4a403e64d99bce60bd5 | quote: HK-KVM-NAT-512M Starting from $4.00USD Monthly 1 vCPU Cores 5 GB Storage 512 MB RAM 1TB Bandwidth 1 Gbps Network No Public IPv4 (NAT Only)
  - [3] 2026-11-07: the cart's printed price for the plan is the monthly USD 4.00; no renewal price appears | capture: sha256:74ad2e1b1f3bd54462734ef798933fdcdea55c751140a4a403e64d99bce60bd5 | quote: HK-KVM-NAT-512M Starting from $4.00USD Monthly 1 vCPU Cores 5 GB Storage 512 MB RAM 1TB Bandwidth 1 Gbps Network No Public IPv4 (NAT Only)
  - [3] 2026-11-07: the cart prices HK-KVM-NAT-512M at USD 4.00 monthly with the 1 vCPU / 512 MB RAM / 5 GB shape | capture: sha256:74ad2e1b1f3bd54462734ef798933fdcdea55c751140a4a403e64d99bce60bd5 | quote: HK-KVM-NAT-512M Starting from $4.00USD Monthly 1 vCPU Cores 5 GB Storage 512 MB RAM 1TB Bandwidth 1 Gbps Network No Public IPv4 (NAT Only)
- sources:
  - [1] https://mlnl.host/
  - [2] https://vpspricetracker.com/provider/Millenial/vps
  - [3] https://www.millenial.host/portal/store/promos
  - [4] https://www.millenial.host/portal/store/virtual-private-servers-united-kingdom-uk
