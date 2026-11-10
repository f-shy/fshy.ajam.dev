# Inet.ws

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inet-ws/ | JSON https://fshy.ajam.dev/api/v1/entity/inet-ws.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Inet.ws

- `compute/inet-ws` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:07.273Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/Inet_ws/vps
- price parsed USD 4/mo
- free tier: Linux VPS vCore 1 / RAM 2 / SSD 30 GB at USD 4.00/month: 1 Intel core shared, 2,048 MB RAM, 30 GB SSD, 10,240 GB/month bandwidth, 0.5 Gbps port, 1 IPv4, Ashburn Virginia. The tracker's line reads "starting at $4.00 per month", and the same plan at USD 4.00 is listed for Atlanta Georgia and Chicago Illinois. The vendor's FAQ states the post-quota behaviour in terms: for one and two vCPU plans the port falls to 5 Mbps. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 10,240 GB a month, then a port reduction to 5 Mbps on one and two vCPU plans and 10 Mbps on the rest, stated in the vendor's FAQ; no overage price is published, so the throttle is the only consequence | metered: yes | free allowance: 10240 GB per month | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 10,240 GB a month is 340 GB a day, then the port drops to 5 Mbps on this class of plan, which is about 54 GB a day at saturation; the drop is the harder wall and the vendor states it as policy, not as best effort. [1]
- limits note: 10,240 GB a month is 340 GB a day, then the port drops to 5 Mbps on this class of plan, which is about 54 GB a day at saturation; the drop is the harder wall and the vendor states it as policy, not as best effort.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with root, an IPv4 primary with extra addresses at a fee, a client-area portal and a documented API is not mentioned on the page read; ISO install is available by handing support a direct HTTP link. The company is INETCLOUD Inc.
- composes with: 2 GB, 30 GB and 10 TB a month for USD 4.00 is the best balance of RAM and bytes at the monthly floor of evaluated providers, which fits a crawler that keeps its queue in memory and writes little; once the allowance is spent the 5 Mbps throttle is a hard stop, so a crawl that might overshoot belongs on an unmetered host or on Hosting Int.
- reliability: no reliability event recorded
- notes: Price is tracker-only: inet.ws/pricing answered a 404 ("Page not found"), and inet.ws/vps/ answered 200 but rendered its FAQ without the plan table, so the USD 4.00 is reported. The FAQ facts are documented and are the useful part of this record: the throttle, the SMTP block on new accounts, and the free weekly backup.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 30
  - price_on_page: USD 4.00/month for the entry Linux VPS (2,048 MB RAM, 30 GB SSD)
  - renewal_note: not published; the vendor's own order path is walled (Cloudflare challenge on every route, read 2026-11-07)
- evidence:
  - [1] 2026-10-22: the cheapest row quoted: "Inet.ws - $4.00 / month" / "cpu 1 Intel Cores (shared)" / "ram 2,048 MB RAM" / "disk 30 GB SSD" / "bandwidth 10,240 GB/month bandwidth" / "rj45 0.5 Gbps port speed" / "inet IPv4" / "city Ashburn Virginia U.S.A.", under "starting at $4.00 per month", with the same row repeated for Atlanta and Chicago
  - [2] 2026-10-22: the post-quota rule quoted: "What will happen when the bandwidth volume runs out? - For the plan with one vCPU and two vCPU, the port speed will be reduced to 5Mbps. - For all other plans, the port speed will be set to 10Mbps."
  - [2] 2026-10-22: the account terms quoted: "In some instances, outbound traffic to the SMTP port may be blocked for new accounts"; "Weekly backup for free", automatic daily backups at "a 20% higher base monthly fee"; stopped instances "continue to reserve dedicated system resources (RAM, SSD storage, IP aliases, vCPU)"; "We utilize KVM virtualization on all of our infrastructure."
  - [1] 2026-11-07: the tracker's cheapest Inet.ws row is USD 4.00 a month | capture: sha256:7da801eb01bad24ca3efeb2522402c6f72e5d9caa80f2fbd8140691d0df9ecf7 | quote: starting at $4.00 per month
  - [1] 2026-11-07: the tracker's rows print monthly prices only, no renewal price | capture: sha256:7da801eb01bad24ca3efeb2522402c6f72e5d9caa80f2fbd8140691d0df9ecf7 | quote: starting at $4.00 per month
  - [1] 2026-11-07: the tracker's cheapest row is as the record states | capture: sha256:7da801eb01bad24ca3efeb2522402c6f72e5d9caa80f2fbd8140691d0df9ecf7 | quote: starting at $4.00 per month
- sources:
  - [1] https://vpspricetracker.com/provider/Inet_ws/vps
  - [2] https://inet.ws/vps/
