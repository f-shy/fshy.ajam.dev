# ReadyDedis

> readydedis.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/readydedis/ | JSON https://fshy.ajam.dev/api/v1/entity/readydedis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ReadyDedis

- `compute/readydedis` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:16:58.956Z (live) | stale on 2026-12-08
- url https://readydedis.com/cloud-vps
- price parsed USD 5/mo
- free tier: AMD-1 at USD 5.00/month: 1 core, 1 GB RAM, 20 GB NVMe SSD, 1.00 TB bandwidth on a 1 Gbps port per the tracker (the vendor table shows no port column), in New Jersey or Los Angeles. The table continues AMD-2 USD 10.00 (2 cores, 2 GB, 30 GB, 1.5 TB), AMD-3 USD 15.00 (2 cores, 4 GB, 40 GB, 3 TB), AMD-4 USD 20.00 (4 cores, 6 GB, 60 GB, 4 TB), AMD-5 USD 25.00 (4 cores, 8 GB, 75 GB, 5 TB) and AMD-6 USD 45.00 (4 cores, 12 GB, 100 GB, 6 TB). | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: monthly allowance stated per plan from 1.00 TB to 6.00 TB; no overage price was published on the page read | metered: yes | free allowance: 1.00 TB/month on AMD-1 | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1.00 TB a month on AMD-1, rising to 6.00 TB on AMD-6. On a 1 Gbps port that is under three hours of full-rate transfer by arithmetic, so the allowance and not the port is the limit. [1]
- limits note: 1.00 TB a month on AMD-1, rising to 6.00 TB on AMD-6. On a 1 Gbps port that is under three hours of full-rate transfer by arithmetic, so the allowance and not the port is the limit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with full root and a VNC console, Docker Manager with one-click apps, 24/7 monitoring; no API was stated on the page read
- composes with: USD 5.00 for 1 GB and 20 GB of NVMe with 1 TB in New Jersey or Los Angeles is mid-market among documented hosts. The better unit price on the same table is AMD-2 at USD 10.00 for 2 GB and 1.5 TB, or AMD-3 at USD 15.00 for 4 GB and 3 TB, which is where a crawler worker would sit.
- reliability: the vendor states a 99.9 percent uptime SLA backed by 24/7 monitoring; no reliability incident observed
- notes: or docs/ (searched both trees for readydedis, no hit). The page carries a second plan table below the AMD one that extracted empty, presumably for the Intel Xeon line the copy mentions, so no Intel row was read. The tracker says '20 GB SSD' where the vendor says '20 GB NVMe SSD'. Unverified: whether the 'Cores' column means shared or dedicated cores, since the page does not say and the tracker labels them shared.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
  - price_on_page: USD 5.00/month for AMD-1; renewal: not published
- evidence:
  - [1] 2026-10-22: plan table row quoted: 'AMD-1', '1 Cores', '1 GB', '20 GB NVMe SSD', '1.00 TB', '$5.00/mo'; the table runs to 'AMD-6', '4 Cores', '12 GB', '100 GB NVMe SSD', '6.00 TB', '$45.00/mo'
  - [1] 2026-10-22: page states 'Enterprise-grade KVM virtual servers powered by AMD EPYC and Intel Xeon processors', 'Up to 7GB/s read speeds', '99.9% Uptime SLA', 'Full Root Access ... VNC console', 'Docker Manager'
  - [2] 2026-10-22: cheapest row: '$5.00 / month', '1 Epyc Cores (shared)', '1,024 MB RAM', '20 GB SSD', '1,024 GB/month bandwidth', '1 Gbps port speed', 'IPv4', New Jersey; the same plan is listed for Los Angeles
  - [3] 2026-11-07: the cart's cycle selector prices cloud.1g (AMD-1) at USD 5.00 monthly or USD 50.00 annually with a USD 0.00 setup fee | capture: sha256:d637d8bfe2987b1cd0a224bb94091df8cb8d4fa537de0488015d2d097fbd24bb | quote: <option value="m" selected="selected">$5.00 USD Monthly</option><option value="a" >$50.00 USD Annually</option>
  - [3] 2026-11-07: the cart prices AMD-1 at 5.00 USD a month or 50.00 USD a year | capture: sha256:d637d8bfe2987b1cd0a224bb94091df8cb8d4fa537de0488015d2d097fbd24bb | quote: <option value="m" selected="selected">$5.00 USD Monthly</option><option value="a" >$50.00 USD Annually</option>
- sources:
  - [1] https://readydedis.com/cloud-vps
  - [2] https://vpspricetracker.com/provider/ReadyDedis/vps
  - [3] https://service.readydedis.com/?cmd=cart&action=add&id=222
