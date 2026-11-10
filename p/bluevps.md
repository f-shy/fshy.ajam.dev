# BlueVPS

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bluevps/ | JSON https://fshy.ajam.dev/api/v1/entity/bluevps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BlueVPS

- `compute/bluevps` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:28.415Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/BlueVPS/vps
- price parsed USD 3.67/mo
- free tier: 1 vCPU (shared), 512 MB RAM, 6 GB HDD, 51,200 GB/month bandwidth on a 1 Gbps port, IPv4 + IPv6, Tel Aviv Israel, at USD 3.67/month, which the page states as USD 11.00 per quarter on quarterly billing. The tracker calls this the provider's cheapest currently offered VPS and the offer's info page marks it 'In stock now'. The same plan is also listed at the same price in Tallinn Estonia and Palermo Italy. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: contradicted between the two sources: the vendor homepage says 'Unlimited traffic' and states no egress term, the tracker lists 51,200 GB/month; nothing beyond the 51,200 GB figure is asserted here | metered: no | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 51,200 GB/month at 1 Gbps is the tracker's figure for this plan; the vendor's own homepage says 'Unlimited traffic' and publishes no cap, so the two sources contradict each other on whether an allowance exists at all and the explicit figure is the one recorded [1]
- limits note: 51,200 GB/month at 1 Gbps is the tracker's figure for this plan; the vendor's own homepage says 'Unlimited traffic' and publishes no cap, so the two sources contradict each other on whether an allowance exists at all and the explicit figure is the one recorded
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read: the vendor homepage advertises KVM with full root or RDP administrator access and names no API or client; it says '20 locations for KVM VPS deployment'
- composes with: a 512 MB / 6 GB box at USD 3.67 is only a scheduler or a proxy hop; it cannot hold a crawl frontier and it is the wrong shape for the storage or inference workloads
- reliability: no reliability event recorded
- notes: Confidence stays reported because no vendor price table was read. The location list on the tracker is three city rows at the same price, so the cheapest row is not one city.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.disk_gib: 6
  - monthly_usd: 3.67
  - annual_derived_usd: 39.96
  - renewal_usd: not published: neither the order page nor the cart prints a renewal or month-13 sentence
  - billing_term: quarterly
  - in_stock: yes
- evidence:
  - [1] 2026-10-22: card row quoted: 'BlueVPS - $3.67 / month', 'quarterly Service', '1 Intel Cores (shared)', '512 MB RAM', '6 GB HDD', '51,200 GB/month bandwidth', '1 Gbps port speed', 'IPv4 + IPv6', 'Tel Aviv Israel'; intro line 'These are the cheapest VPSs currently offered by BlueVPS, starting at $11.00 per quarter'
  - [3] 2026-10-22: properties block: 'In stock now', KVM, port 25 'Closed by default', IPv4 and IPv6 both present, and 'The latest yearly price was $40.00, collected on October 22'
  - [2] 2026-10-22: vendor homepage read as text: 'Unlimited traffic', '20 locations for KVM VPS deployment', 'KVM virtualization guarantee 100% dedicated resources per VPS'; no price table and no plan specs are published on the page
  - [4] 2026-11-07: the vendor cart renders bKVM 512 at USD 11.00 per quarter | capture: sha256:9aefeac7fe8ad7d8b608b3a3a96823202dc839c6a0928ecfd270e7a15ee3eacb | quote: "displayPrice": "$11.00 USD"
  - [5] 2026-11-07: the vendor's plan JSON states a best price of 3.33 on annual billing | capture: sha256:9a86cabb9a645b005e0a07da2d8cff0925d3eaa56ded1ed1fc42053045eb7772 | quote: best_price&quot;:3.33
  - [3] 2026-11-07: the tracker's info page marks the bKVM_512 offer in stock and states the latest yearly price as $40.00 | capture: sha256:7708206dfaae2fbdb685375a32a46888bab2e86ce08f568dac7c8889642a4e79 | quote: In stock now
- sources:
  - [1] https://vpspricetracker.com/provider/BlueVPS/vps
  - [2] https://bluevps.com/
  - [3] https://vpspricetracker.com/info/121935/BlueVPS/bKVM_512
  - [4] https://my.bluevps.com/cart.php?a=add&pid=2&language=english&currency=1
  - [5] https://bluevps.com/vps-1gb
