# AspireHosting

> aspirehosting.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aspirehosting/ | JSON https://fshy.ajam.dev/api/v1/entity/aspirehosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AspireHosting

- `compute/aspirehosting` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:27.360Z (live) | stale on 2026-11-22
- url https://billing.aspirehosting.net/store/cloud-standard-miami-fl-xeon
- price parsed USD 3.3/mo
- free tier: Cloud_Standard_Miami_2GB at USD 3.30 per month (dollar sign on the page, read as USD): 2 Intel cores (shared), 2,048 MB RAM, 30 GB NVMe, 1,024 GB/month bandwidth, 1 Gbps port, 1 IPv4 only, Miami, Florida, U.S.A. Second row 4.50 per month for 2 Epyc cores, 2,048 MB, 30 GB NVMe, 2,048 GB/month. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: metered: 1,024 GB/month on the cheapest row; no overage rate printed | metered: yes | free allowance: 1 TB/month per the vendor's store row (Cloud Standard Miami 2GB: '1TB Bandwidth (1GBPS)') | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1,024 GB a month on a 1 Gbps port; 2 GB of RAM and 30 GB of NVMe with 1 TB of transfer makes the counter, not the disk, the first limit. [1]
- limits note: 1,024 GB a month on a 1 Gbps port; 2 GB of RAM and 30 GB of NVMe with 1 TB of transfer makes the counter, not the disk, the first limit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read; no panel, API or client is documented on the pages that answered
- composes with: 2 cores and 2 GB for USD 3.30 is one of the better core-per-dollar rows among evaluated providers, but the 1 TB counter and the single IPv4 without IPv6 keep it to a scheduler or a small service rather than a crawler egress point.
- reliability: no reliability event recorded
- notes: Three vendor paths were tried and none published a price: https://aspirehosting.net/ (200, marketing and testimonials), /vps (200, feature copy only) and /vps-hosting (404). The number stays third-party at confidence reported. The homepage advertises a 26 percent discount on production servers but the extraction carried no code, so no discounted price is asserted. verification criteria: the checkout price for Cloud_Standard_Miami_2GB and whether the 26 percent code applies to it.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 30
  - monthly_usd: 3.3
  - annual_usd: not published: the store row prints a monthly cycle only and the cart refuses the order (out of stock), so no annual figure is reachable; read at https://billing.aspirehosting.net/store/cloud-standard-miami-fl-xeon
  - renewal_usd: not published: no renewal price is printed on the store row and the cart refuses the order (out of stock); read at https://billing.aspirehosting.net/store/cloud-standard-miami-fl-xeon
  - term: monthly; the store row prints a monthly cycle only
  - in_stock: no: the row's availability badge reads '0 Available' and the cart answers 'Out of Stock' with orders suspended
  - cart_url: https://billing.aspirehosting.net/store/cloud-standard-miami-fl-xeon/cloud-standard-miami-2gb
  - cart_note: the cart answers WHMCS's out-of-stock page and prices nothing: 'We are currently out of stock on this item so orders for it have been suspended until more stock is available. For further information, please contact us.'
- evidence:
  - [1] 2026-10-22: row quoted: 'AspireHosting - 3.30 / month', 'cpu 2 Intel Cores (shared)', 'ram 2,048 MB RAM', 'disk 30 GB NVMe', 'bandwidth 1,024 GB/month bandwidth', 'rj45 1 Gbps port speed', 'inet IPv4', 'city Miami Florida U.S.A.'
  - [1] 2026-10-22: second row '4.50 / month' with 'cpu 2 Epyc Cores (shared)', 'ram 2,048 MB RAM', 'disk 30 GB NVMe', 'bandwidth 2,048 GB/month bandwidth', 'rj45 1 Gbps port speed'
  - [2] 2026-10-22: homepage returns 200 and carries a promo banner 'Avail 26% OFF on all production servers - Use code at checkout!' but no plan table or price; /vps returns marketing copy only and /vps-hosting returned 404
  - [3] 2026-11-07: the vendor's own store prices the Cloud Standard Miami 2GB row at USD 3.30 monthly, 0 available | capture: sha256:70b2e5d4674bd4785992ba247565a45c730ce1eb32a41dd218cfd9b49f145bf0 | quote: Cloud Standard Miami 2GB 0 Available 2GB Ram DDR4 2vCores 30GB NVMe 1TB Bandwidth (1GBPS) DDoS Protection 1 IPv4 Intel Xeon 2nd Gen Scalable Starting from $3.30USD Monthly Order Now
  - [3] 2026-11-07: the vendor's store prices the Cloud Standard Miami 2GB row at USD 3.30 | capture: sha256:2bf3750f6ec7de5be174d198bd83717c3d71c6e1ef4894e91be346f716c7fd61 | quote: $3.30USD
  - [4] 2026-11-07: the Cloud Standard Miami 2GB cart prices nothing and suspends orders | capture: sha256:95c03ac84bd7789fe39c23edda5e4070a2e338d17b50c17724b030c8babcd590 | quote: We are currently out of stock on this item so orders for it have been suspended until more stock is available. For further information, please contact us.
  - [4] 2026-11-07: the cart prints no price beside the suspension notice | capture: sha256:95c03ac84bd7789fe39c23edda5e4070a2e338d17b50c17724b030c8babcd590 | quote: We are currently out of stock on this item so orders for it have been suspended until more stock is available. For further information, please contact us.
  - [3] 2026-11-07: the cycle line under the Cloud Standard Miami 2GB price reads Monthly; the row prints no other cycle | capture: sha256:2bf3750f6ec7de5be174d198bd83717c3d71c6e1ef4894e91be346f716c7fd61 | quote: Monthly
  - [3] 2026-11-07: the Cloud Standard Miami 2GB row's availability badge reads 0 Available | capture: sha256:2bf3750f6ec7de5be174d198bd83717c3d71c6e1ef4894e91be346f716c7fd61 | quote: 0 Available
  - [3] 2026-11-07: the Cloud Standard Miami 2GB row's Order Now button links the cart at /store/cloud-standard-miami-fl-xeon/cloud-standard-miami-2gb | capture: sha256:4ebf831e4c0eea7b1d274d7e314e3927c7e94831d0cec6b09f74ee1003f2950c | quote: id="product203-order-button"
  - [4] 2026-11-07: the Cloud Standard Miami 2GB cart suspends orders and prices nothing | capture: sha256:95c03ac84bd7789fe39c23edda5e4070a2e338d17b50c17724b030c8babcd590 | quote: We are currently out of stock on this item so orders for it have been suspended until more stock is available. For further information, please contact us.
  - probe:https://billing.aspirehosting.net/store/cloud-standard-miami-fl-xeon/cloud-standard-miami-2gb 2026-11-07: the warmed-session cart read agrees: the cart carries the out-of-stock phrase and no price | capture: sha256:9e9e343a87f18b2059ca71ada72c39f55766a4ea40653011f97c21540f811ca3 | quote: "out of stock"
  - [3] 2026-11-07: the vendor's store row lists 1TB Bandwidth (1GBPS) | capture: sha256:2bf3750f6ec7de5be174d198bd83717c3d71c6e1ef4894e91be346f716c7fd61 | quote: 1TB Bandwidth (1GBPS)
  - [3] 2026-11-07: the store page read prices Cloud Standard Miami 2GB at USD 3.30 monthly with 2 vCores, 30 GB NVMe and 1 TB bandwidth, 0 available | capture: sha256:2bf3750f6ec7de5be174d198bd83717c3d71c6e1ef4894e91be346f716c7fd61 | quote: $3.30USD
- sources:
  - [1] https://vpspricetracker.com/provider/AspireHosting/vps
  - [2] https://aspirehosting.net/
  - [3] https://billing.aspirehosting.net/store/cloud-standard-miami-fl-xeon
  - [4] https://billing.aspirehosting.net/store/cloud-standard-miami-fl-xeon/cloud-standard-miami-2gb
