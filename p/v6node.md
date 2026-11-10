# v6Node

> v6node.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/v6node/ | JSON https://fshy.ajam.dev/api/v1/entity/v6node.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## v6Node (Karlsruhe)

- `compute/v6node-compute-node-1gb` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category IPv6-only VPS | tier Compute Node (entry rung)
- needs card no, phone no, ID no, institution no | verified 2026-11-09T13:13:24.633Z (live) | stale on 2026-11-24
- url https://v6node.com/
- free tier: No free tier. The vendor states compute nodes start at EUR 1 per month; the entry rung's shape is not shown on any first-party page reached. A tracker lists a Node 2GB at EUR 3.00 a month for 1 core, 2 GB, 20 GB SSD and 2 TB traffic. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the vendor's deploy page lists monthly prices with a struck-through higher figure beside each; no deletion grace period is printed | source: [2]
- egress: not published on the pages reached; a tracker lists 2 TB for the Node 2GB | metered: yes | free allowance: unverified | source: [3]
- identity: email | detail: an account on cloud.v6node.com, which returned a login wall to every read attempt. The vendor states payment by 'Apple/ Google Pay, all major credit/debit cards and SEPA direct debit', so a debit card is explicitly accepted. No card hold is stated. | country: DE
- interface: ssh
- limits:
  - volume-quota: not published on the pages reached; 2 TB per a tracker row for the Node 2GB [3]
  - per-ip-shaping (binding): one dedicated /64 per node; no IPv4 address, and NAT64 covers outbound only [4]
- binding note: no IPv4 at all and NAT64 is outbound-only, so nothing on the IPv4 internet can open a connection to the guest unless it goes through the reverse proxy.
- interface detail: KVM guests with a dedicated /64 IPv6 subnet and no IPv4; the vendor preconfigures a DNS64/NAT64 resolver so the guest can still reach IPv4-only destinations outbound. A free reverse proxy gives any domain a dual-stack HTTP endpoint.
- tooling: any SSH client over IPv6; the control panel is cloud.v6node.com and is behind a login
- composes with: the only row among documented hosts whose IPv4 problem is solved for outbound traffic by design (DNS64/NAT64) rather than by an add-on, which makes it the best fit for a monitor that has to poll IPv4-only targets
- reliability: no reliability event observed; a 2022 LowEndBox offer for the same provider advertised 4.5 EUR a year, so the entry price has risen since
- notes: The architecture is the most useful of the IPv6-only hosts, and the price is the least documented. DNS64/NAT64 is the answer to the caveat that governs every other row here: a guest on this host can reach IPv4-only destinations outbound without buying an IPv4 address, which is exactly what a health monitor polling IPv4 endpoints needs. What could not be established is what EUR 1 actually buys: the marketing site says 'starting at €1 per month', the deploy page starts at EUR 4.49, and the only shape figure is a tracker's Node 2GB at EUR 3.00. The control panel is login-walled, so the entry rung's RAM, disk and traffic are unverified. The entity is a sole trader with a German VAT ID, which is a weaker counterparty than a GmbH but is a real registered taxpayer.
- evidence note: the EUR 1 entry price, the IPv6-only statement, the DNS64/NAT64 statement, the /64 and the payment rails are quoted from first-party pages today, but the entry rung's shape and traffic allowance are not published on any page reached, and the control panel is login-walled. The shape in this record is a tracker's, not the vendor's.
- evidence:
  - [1] 2026-10-24: quoted: 'IPv6 only virtual machines in the cloud ... Compute Nodes General purpose compute instances Starting at €1 per month' and 'All of our nodes only come equipped with native IPv6 connectivity. But thanks to DNS64 and NAT64 you can still access IPv4-only resources on the Internet.'
  - [1] 2026-10-24: quoted payment answer: 'You can pay with Apple/ Google Pay, all major credit/debit cards and SEPA direct debit' and 'We currently only offer Germany as a datacenter location'
  - [2] 2026-10-24: quoted: 'Cloud servers, simple pricing ... From 4.49€/mo ... Node 4GB G2 ... 4.49€ /month ... 4.99€ /month ... 2 cores · 4GB · 40GB NVMe ... Amsterdam Spokane Frankfurt 2' - the deploy page starts at 4.49 EUR, so the EUR 1 rung is not on it
  - [5] 2026-10-24: the imprint (§ 5 TMG) gives a VAT ID and the register court Amtsgericht Karlsruhe for a sole trader in Karlsruhe, Germany, not a limited company
  - [3] 2026-10-24: third-party tracker, quoted: 'Monthly price € 3.00 EUR ... Virtualization type KVM ... 1 core ... 2 GB ... Total SSD Capacity 20 GB ... Uplink 10,000 Mbit ... Traffic 2 TB ... Germany ... Frankfurt' and the page's own warning 'This offer is invisible. It can only be reached by this direct link.'
  - [4] 2026-10-24: third-party offer writeup, quoted: 'Outgoing IPv4 still reachable thanks to preconfigured NAT64/DNS64 nameserver' and 'Dedicated /64 IPv6 subnet' and '2TB Traffic per Month' and 'Hosted at Hetzner, Germany'
  - [1] 2026-11-09: the page was read and states no traffic volume, bandwidth figure or port speed for the plan | capture: sha256:24b23efed5846800c78ff2295fdb1b81e9ec4d3e569ff4a7d2cb42f60cb10003 | quote: All of our nodes only come equipped with native IPv6 connectivity.
- sources:
  - [1] https://v6node.com/
  - [2] https://cloud.v6node.com/deploy
  - [3] https://www.serverhunter.com/offer/v6node-com-node-2gb/
  - [4] https://lowendbox.com/blog/v6node-vms-start-at-4-5e-year-in-germany/
  - [5] https://v6node.com/legal/
