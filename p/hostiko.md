# Hostiko

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostiko/ | JSON https://fshy.ajam.dev/api/v1/entity/hostiko.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hostiko

- `compute/hostiko` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:33.037Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/Hostiko/vps
- price parsed USD 3.77/mo
- free tier: XS at EUR 3.35/month: 1 Epyc core shared, 1,024 MB RAM, 25 GB NVMe, 5,120 GB/month bandwidth, 1.95 Gbps port, IPv6 only, Warsaw Poland. The tracker's line reads "starting at EUR 3.35 per month". The same XS plan is EUR 3.35 in Stockholm and EUR 4.10 in Warsaw with IPv4 + IPv6, which is the price of a public v4. The provider lists VPS in Poland and Sweden only. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5,120 GB a month counted on the sum of ingress and egress, then shaped to 10 Mbit/s with the counter reset every 30 days; no overage price is published | metered: yes | free allowance: 5120 GB per month | source: [2]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 5,120 GB a month is 170 GB a day, then the connection is throttled to 10 Mbit/s and the counter resets every 30 days from activation, both stated on the vendor page; the 25 GB NVMe disk and the single core are the tighter limit for anything but a relay. [1]
- limits note: 5,120 GB a month is 170 GB a day, then the connection is throttled to 10 Mbit/s and the counter resets every 30 days from activation, both stated on the vendor page; the 25 GB NVMe disk and the single core are the tighter limit for anything but a relay.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with root, own ISO images accepted, and a control panel that reinstalls the OS, powers the server and shows load and traffic; the vendor's price table is rendered client-side, so the HTML read carried the prose and not the numbers.
- composes with: EUR 3.35 for 5.1 TB a month and a 1.95 Gbps port is the cheapest per byte of transfer among evaluated providers, which makes it a relay or a tunnel endpoint in Europe; 1 GB of RAM and 25 GB of disk rule it out as a cache, and the IPv6-only floor means a v4 address costs EUR 0.75 more a month.
- reliability: no reliability event recorded
- notes: Price is tracker-only: the vendor's /vps page answered 200 and rendered its FAQ and plan prose, but the prices are templated client-side and no number reached the text extraction. A day-rate trial exists and is paid, so it is not a free tier. verification criteria: a JavaScript render of hostiko.com.ua/vps to lift EUR 3.35 to documented, and a read of the day-rate terms.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 25
  - term: monthly
  - price_on_page: EUR 3.35/mo (tracker; the vendor page renders prices client-side and none reached the read)
  - out_of_pocket_usd: 3.74
  - renewal_usd: not published: no page read prints a renewal price
  - cart_url: https://my.hstk.net/virtual/order#plan=f6abf4f7-d956-428b-a8a3-cf2023a7cbab&period=monthly&location=751da6ee-6673-4456-93af-7d85de20145c
  - stock: unverified: the vendor order page answers a JS app no read could render; the tracker carries no stock line
- evidence:
  - [1] 2026-10-22: the cheapest row quoted: "Hostiko - EUR 3.35 / month" / "cpu 1 Epyc Cores (shared)" / "ram 1,024 MB RAM" / "disk 25 GB NVMe" / "bandwidth 5,120 GB/month bandwidth" / "rj45 1.95 Gbps port speed" / "inet IPv6" / "city Warsaw Poland", under "starting at EUR 3.35 per month"; the Warsaw IPv4 + IPv6 row is EUR 4.10
  - [2] 2026-10-22: the post-quota rule translated from the Ukrainian page, not a verbatim quote: traffic is counted on the sum of ingress and egress, after the limit the connection speed is automatically reduced to 10 Mbit/s, and the counter resets every 30 days from server activation; the same page states KVM virtualisation on all VPS plans
  - [2] 2026-10-22: the page states it does not provide VPS for tests, transliterated from "My ne nadaiemo virtualni servery dlia testiv", but that any plan can be ordered for a day to check quality; Windows Server 2025, 2022 and 2019 are available on all plans except UA-XS and PL-XS
  - [1] 2026-11-07: the tracker still lists the XS plan at EUR 3.35 a month for Warsaw and Stockholm | capture: sha256:d7fb6bef51af071bcc28ae21c2406527613e3656aabd70c068c1796ab00bd43a | quote: These are the cheapest VPSs currently offered by Hostiko, starting at €3.35 per month:
  - [3] 2026-11-07: the vendor's own plan data for PL-XS (1 vCPU, 1 GB RAM, 25 GB NVMe, 5 TB @ 2Gbps) carries the order URL my.hstk.net/virtual/order#plan=f6abf4f7-d956-428b-a8a3-cf2023a7cbab&period=monthly&location=751da6ee-6673-4456-93af-7d85de20145c | capture: sha256:37319957d04c9ab8ad0aaaec210347e40a04015ba8ed4d91994afd6f915ec690 | quote: id\u0022:4007,\u0022name\u0022:\u0022PL-XS\u0022,\u0022price\u0022:{\u0022daily\u0022:0.87,\u0022monthly\u0022:210
  - [1] 2026-11-07: the tracker still lists the XS plan at EUR 3.35 a month | capture: sha256:d7fb6bef51af071bcc28ae21c2406527613e3656aabd70c068c1796ab00bd43a | quote: These are the cheapest VPSs currently offered by Hostiko, starting at €3.35 per month:
  - [1] 2026-11-07: the tracker lists the XS plan as currently offered and states no stock count | capture: sha256:d7fb6bef51af071bcc28ae21c2406527613e3656aabd70c068c1796ab00bd43a | quote: These are the cheapest VPSs currently offered by Hostiko, starting at €3.35 per month:
- sources:
  - [1] https://vpspricetracker.com/provider/Hostiko/vps
  - [2] https://hostiko.com.ua/vps
  - [3] https://hostiko.com.ua/en/vps?p=1050978
