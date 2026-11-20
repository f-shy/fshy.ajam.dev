# Mondoze

> mondoze.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mondoze/ | JSON https://fshy.ajam.dev/api/v1/entity/mondoze.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mondoze

- `compute/mondoze` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:57.717Z (live) | stale on 2026-12-08
- url https://www.mondoze.com/vps
- price parsed USD 8.33/mo
- free tier: 2GB LINUX VPS ('2 GB Linux VPS (MY) V2') at USD 8.33/month on the billing portal's cart ('Starting from USD 8.33 Monthly'): 2 vCPU, 2 GB RAM, 60 GB disk, 'Unmetered' bandwidth, 1 IPv4, Malaysia; in stock (Order Now; the store prints per-plan stock counters, e.g. '2 Available' on the 12 GB plan). Annual: USD 99.95 on the cart's configure page ('Annually:USD 99.95', 'USD 99.95 Total Due Today'). Renewal: not published. Term: monthly and annually (the cart's cycle dropdown does not render its other options). The vendor page's struck-through list price is in the record's earlier evidence. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the vendor page says 'Unmetered Bandwidth'; the tracker row states 31,641 GB/month on a 0.1 Gbps port; no overage price was published on either page | metered: yes | free allowance: 31,641 GB/month as stated by the tracker; 'Unmetered' as stated by the vendor | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): The tracker row states 31,641 GB/month on a 0.1 Gbps port; the vendor page says 'Unmetered'. 31,641 GB is within 3 percent of the 32,400 GB a 100 Mbps port moves in 30 days, so the tracker figure restates the port ceiling rather than an independent quota. Derived by arithmetic, not published by the vendor. [1]
- limits note: The tracker row states 31,641 GB/month on a 0.1 Gbps port; the vendor page says 'Unmetered'. 31,641 GB is within 3 percent of the 32,400 GB a 100 Mbps port moves in 30 days, so the tracker figure restates the port ceiling rather than an independent quota. Derived by arithmetic, not published by the vendor.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: full root access; the Order Now button points at a WHMCS-style cart at billing.mondoze.com (billing.mondoze.com/cart.php?a=add&pid=122 for this plan); no API was stated on the page read
- composes with: 2 GB of RAM and 60 GB of disk at USD 8.33/month in Malaysia is a small always-on scheduler or DNS box for an APAC-facing crawl. The 100 Mbps port rules it out as a transfer host: the port, not the byte count, is what limits it.
- reliability: no reliability event observed; no uptime guarantee was stated on the page read.
- notes: The billing term behind '$8.33 as low as' is read on the vendor's own billing portal: 'Starting from USD 8.33 Monthly' on the Linux VPS V2 store page, with the plan in stock. The FAQ answers the earlier per-VM-versus-shared question: 'No, all our vps is shared bandwidth'.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 60
  - price_on_page: USD 8.33/month, 2 GB Linux VPS (MY) V2
  - renewal_usd: not published: the cart's configure page prints the annual term price and no renewal price
- evidence:
  - [1] 2026-10-22: 2GB LINUX VPS card, quoted: 'As Low As $8.33/month', '$9.99/month' struck through, '2GB Memory', '2 vCPU', '60GB Disk Space', 'Unmetered Bandwidth', '1 IP Address', 'Located in Malaysia'
  - [1] 2026-10-22: starter LINUX VPS at USD 11.00/month from USD 13.20 with 1.5 GB memory and 1 vCPU, so the smaller plan costs more than the 2 GB plan on the same page
  - [2] 2026-10-22: cheapest row: '$8.33 / month', 'yearly Service', '2 Intel Cores (shared)', '2,048 MB RAM', '60 GB NVMe', '31,641 GB/month bandwidth', '0.1 Gbps port speed', 'Malaysia'; header 'starting at $99.96 per year'
  - [3] 2026-11-07: the billing portal's Linux VPS V2 store lists the 2 GB plan at USD 8.33, monthly term, with an Order Now button | capture: sha256:b65d654c3399c67c31c6722906d0873b924dfa83383460a6e3d686f7a277d9ee | quote: 2 GB Linux VPS (MY) V2 2 GB RAM 2 vCPU 60 GB NVME SSD Storage 1 IP Address Unmetered Bandwidth Starting from USD 8.33 Monthly Order Now
  - [1] 2026-11-07: the vendor FAQ states VPS bandwidth is shared, not per-VM | capture: sha256:5f1a92837b9bd8f17e48dae0c1502f666b2dd1f90d96b896dacaae684a4a7411 | quote: No, all our vps is shared bandwidth if you want to add exclusive bandwidth you need to contact our
  - [4] 2026-11-07: the cart's configure page prints the annual term of the 2 GB Linux VPS (MY) V2 at USD 99.95 with USD 99.95 total due today | capture: sha256:d4036efc5762bf8bedd3e09d9a468e242c9c3ac2c3e333fa0aec4ffcab711979 | quote: Annually:USD 99.95 USD 99.95 Total Due Today
  - [3] 2026-11-07: the billing store lists the 2 GB Linux VPS (MY) V2 starting at USD 8.33 on the Monthly term with an Order Now button (product1, no stock badge; the 12 GB plan shows 2 Available) | capture: sha256:70c6fb5a7e77c0c5fc926834f79a54e0fe25e02e350201ec529006f63742e709 | quote: <span class="price">USD 8.33</span>
  - [3] 2026-11-07: the billing store prices the 2 GB Linux VPS (MY) V2 at USD 8.33 on the monthly term | capture: sha256:b65d654c3399c67c31c6722906d0873b924dfa83383460a6e3d686f7a277d9ee | quote: 2 GB Linux VPS (MY) V2 2 GB RAM 2 vCPU 60 GB NVME SSD Storage 1 IP Address Unmetered Bandwidth Starting from USD 8.33 Monthly Order Now
  - [4] 2026-11-07: the configure page prints the annual term price and the total due today; no renewal price appears | capture: sha256:d4036efc5762bf8bedd3e09d9a468e242c9c3ac2c3e333fa0aec4ffcab711979 | quote: Annually:USD 99.95 USD 99.95 Total Due Today
  - [3] 2026-11-07: the billing store lists the 2 GB Linux VPS (MY) V2 at USD 8.33 monthly with its 2 vCPU / 2 GB / 60 GB shape | capture: sha256:b65d654c3399c67c31c6722906d0873b924dfa83383460a6e3d686f7a277d9ee | quote: 2 GB Linux VPS (MY) V2 2 GB RAM 2 vCPU 60 GB NVME SSD Storage 1 IP Address Unmetered Bandwidth Starting from USD 8.33 Monthly Order Now
- sources:
  - [1] https://www.mondoze.com/vps
  - [2] https://vpspricetracker.com/provider/Mondoze/vps
  - [3] https://billing.mondoze.com/index.php/store/linux-vps-v2
  - [4] https://billing.mondoze.com/cart.php?a=add&pid=122
