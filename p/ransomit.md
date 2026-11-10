# ransomIT

> ransomit.com.au | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ransomit/ | JSON https://fshy.ajam.dev/api/v1/entity/ransomit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ransomIT

- `compute/ransomit` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:58.956Z (live) | stale on 2026-12-08
- url https://ransomit.com.au/vps/
- free tier: KVM2GB at AUD 20 / month, on a page that states 'Prices in AUD, including GST': 2 CPU cores, 2 GB RAM, 30 GB SSD, 1 TB/month data, 1 IPv4 plus a routed /64 IPv6. The same plans and prices are offered in all eight locations: Perth, Adelaide, Melbourne, Sydney, Brisbane, Auckland, Singapore and Tokyo. KVM4GB is AUD 50 / month with 4 cores, 4 GB, 50 GB SSD and 1.5 TB; KVM8GB is AUD 95 with 4 cores, 8 GB, 100 GB and 2 TB. The store's category page in its AUD view prints 'Starting from $20.00 AUD Monthly' for KVM2GB, with $50.00 AUD on KVM4GB and $95.00 AUD on KVM8GB, each with an Order Now button and no stock badge; the same page in its USD view prints $20.00 USD, so both currency views carry the same number and the USD figure is the vendor's set price, not a market conversion. The product page redirects anonymous visits to the category, and no annual, quarterly or renewal price is published on any page reachable without an account. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month on KVM2GB, counted in both directions, with the plan speed-restricted on exhaustion rather than suspended; no per-TB overage price is published, only 'contact us' | metered: yes | free allowance: 1 TB a month, inbound and outbound counted equally | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1 TB a month, and the page states 'Inbound and outbound data count equally. When a VPS reaches its data limit, its speed is restricted.' The allowance therefore throttles rather than suspends, but it counts both directions, so a mirror or a serving node spends it twice as fast as a pull-only crawler. [1]
- limits note: 1 TB a month, and the page states 'Inbound and outbound data count equally. When a VPS reaches its data limit, its speed is restricted.' The allowance therefore throttles rather than suspends, but it counts both directions, so a mirror or a serving node spends it twice as fast as a pull-only crawler.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with a VPS control panel, self-service reverse DNS, custom ISO on request and resizing at any time; no API was read
- composes with: The only Australian and APAC presence among documented hosts, at one price across eight cities including Singapore and Tokyo, which makes it the node to place where latency to an Asia-Pacific target matters. At 1 TB counted both ways it is a front end with a presence, not a transfer or storage node.
- reliability: no reliability event observed; the provider states it has run since 2008 on hardware it owns
- notes: Ransom IT VPS hosting is priced in Australian Dollars (AUD), including GST for domestic customers. Entry plans provide Australian and Asia-Pacific datacenter locations.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 30
  - price_on_page: AUD 20/month for KVM2GB; renewal: not published
- evidence:
  - [1] 2026-10-22: KVM2GB plan card, quoted as label and value pairs: '$20' 'AUD/mo', 'CPU cores' '2', 'Memory' '2 GB', 'SSD storage' '30 GB', 'Data' '1 TB/mo', 'IP addresses' '1 IPv4, routed /64 IPv6'; the page states 'Prices in AUD, including GST' and 'KVM virtual servers in eight locations, with the same plans and prices everywhere'
  - [1] 2026-10-22: data policy, quoted verbatim: 'Inbound and outbound data count equally. When a VPS reaches its data limit, its speed is restricted. If you need more data, contact us and we'll set up a plan that fits.'
  - [2] 2026-10-22: location list quoted from the homepage: 'Perth Adelaide Melbourne Sydney Brisbane Auckland Singapore Tokyo', with VPS 'from $20 AUD/mo'
  - [3] 2026-10-22: tracker row, cells in page order: '2 Intel Cores (shared)', '2,048 MB RAM', '30 GB SSD', '1,024 GB/month bandwidth', '0.05 Gbps port speed', 'IPv4 + IPv6', 'Brisbane Australia', price '$20.00 / month'; repeated at the same price for Sydney and Melbourne
  - [4] 2026-11-07: the WHMCS store lists KVM2GB starting at USD 20.00 monthly, the plan and price free_tier.stated records | capture: sha256:bb07e52cf1378372952e4508563c617e7e129ab7c34ab65ee3a24a210bb95ac2 | quote: KVM2GB Starting from $20.00 USD Monthly
  - [5] 2026-11-07: the store's AUD view prices KVM2GB at 20.00 AUD monthly, with KVM4GB at 50 and KVM8GB at 95, each with an Order Now button and no stock badge | capture: sha256:ab8519f2beb8132f28741a96315983890c3e08f9a6025c0e44421af809150a5e | quote: <span class="price">$20.00 AUD</span>
  - [1] 2026-11-07: the vendor page states prices are in AUD including GST and lists KVM2GB at 20 AUD per month | capture: sha256:34e73470777aff4ea2f14eed7143b76dbb92cc7e394346ed8be5500ad130f505 | quote: Prices in AUD, including GST
  - [5] 2026-11-07: the store rendered its AUD currency view, the view the vendor's own order links request | capture: sha256:ab8519f2beb8132f28741a96315983890c3e08f9a6025c0e44421af809150a5e | quote: <option value="2" selected>AUD</option>
  - [4] 2026-11-07: the store's USD view prices KVM2GB at 20.00 USD, the same number the AUD view prints in AUD | capture: sha256:b83bfe35f480899a78d0418bed1a65e7e9b1c0919e63d80e85bf4e25e90452d4 | quote: <span class="price">$20.00 USD</span>
  - [5] 2026-11-07: the store's AUD view prices KVM2GB at 20.00 AUD on a monthly term | capture: sha256:ab8519f2beb8132f28741a96315983890c3e08f9a6025c0e44421af809150a5e | quote: <span class="price">$20.00 AUD</span>
- sources:
  - [1] https://ransomit.com.au/vps/
  - [2] https://ransomit.com.au/
  - [3] https://vpspricetracker.com/provider/ransomIT/vps
  - [4] https://secure.ransomit.com.au/index.php?rp=/store/vps/kvm2gb&currency=2
  - [5] https://secure.ransomit.com.au/index.php?rp=/store/vps&currency=2
