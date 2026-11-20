# MassiveGRID

> massivegrid.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/massivegrid/ | JSON https://fshy.ajam.dev/api/v1/entity/massivegrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MassiveGRID

- `egress/massivegrid-cloud-vps-starter` | paid-only | evidence documented | binding volume-quota | category vps (hosted, New York, London, Frankfurt, Singapore, Proxmox HA) | tier Cloud VPS Starter
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:42.856Z (live) | stale on 2026-12-04
- url https://massivegrid.com/
- price USD 3.99 per month with 1 TB Premium Traffic included | parsed USD 3.99/TB-mo
- free tier: No free tier. Cloud VPS Starter is USD 3.99 a month: 1 vCPU, 1 GB RAM, 32 GB NVMe SSD, 1 TB Premium Traffic, 1 dedicated IPv4, 2 Gbps dedicated uplink, in New York, London, Frankfurt or Singapore. The Dedicated VPS tier starts at USD 8.30 a month. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: a virtual server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 1 TB of Premium Traffic on a 2 Gbps dedicated uplink; no overage rate is published on the page read. | metered: yes | free allowance: 1 TB/month included in Starter | source: [1]
- identity: email | detail: unverified: the sign-up fields were not read. The page lists Visa, Mastercard, Amex, PayPal, Bitcoin, Bitcoin Cash and USDT as accepted payment methods.
- interface: ssh
- limits:
  - volume-quota (binding): 1 TB Premium Traffic on Starter [1]
- binding note: 1 TB of Premium Traffic is the ceiling on the cheapest plan; a 2 Gbps uplink can move that allowance in hours, so the allowance fails first.
- interface detail: Root SSH on a Proxmox-hosted guest with a root password chosen at order and mailed after provisioning.
- tooling: ssh; any daemon the guest supports.
- composes with: One dedicated IPv4 and a 2 Gbps uplink at USD 3.99 a month; IPv6 and inbound policy are not stated on the page read.
- reliability: Plans of the 2025 LowEndTalk offer are retired and migrate to the 2026 product line on 1 December 2026 at a new recurring price (third-party post quoting the vendor notice).
- notes: The 2026 product line replaces the 2025 offer plans; the Starter row is the 2026 entry price.
- evidence note: The Starter price, resources, traffic, dedicated IPv4 and uplink are vendor page lines read on 2026-11-03. IPv6, NAT and inbound policy and identity are not stated.
- extras:
  - nat: not stated; a dedicated IPv4 is listed
  - ipv6: not stated
  - inbound: not stated
  - udp: not stated
- evidence:
  - [1] 2026-11-03: the Cloud VPS tier starts at USD 3.99 a month | capture: sha256:432bea94625c08182f048ac7f09cae2be3581bdfd6853756bf12c4fe0b0fd7fc | quote: Cloud VPS*Shared resources, from $3.99/mo*
  - [1] 2026-11-03: the Starter preset is 1 vCPU, 1 GB RAM, 32 GB NVMe | capture: sha256:432bea94625c08182f048ac7f09cae2be3581bdfd6853756bf12c4fe0b0fd7fc | quote: 1 vCPU • 1 GB RAM • 32 GB NVMe SSD
  - [1] 2026-11-03: Starter lists 1 TB of Premium Traffic | capture: sha256:432bea94625c08182f048ac7f09cae2be3581bdfd6853756bf12c4fe0b0fd7fc | quote: Premium Traffic 1 TB
  - [1] 2026-11-03: Starter lists one dedicated IPv4 | capture: sha256:432bea94625c08182f048ac7f09cae2be3581bdfd6853756bf12c4fe0b0fd7fc | quote: Dedicated IPv4 1
  - [1] 2026-11-03: Starter lists a 2 Gbps dedicated uplink | capture: sha256:432bea94625c08182f048ac7f09cae2be3581bdfd6853756bf12c4fe0b0fd7fc | quote: Dedicated Uplink 2 Gbps
  - [1] 2026-11-03: the page lists card payment methods | capture: sha256:432bea94625c08182f048ac7f09cae2be3581bdfd6853756bf12c4fe0b0fd7fc | quote: Visa Mastercard Amex
  - [1] 2026-11-03: the page lists cryptocurrency payment methods | capture: sha256:432bea94625c08182f048ac7f09cae2be3581bdfd6853756bf12c4fe0b0fd7fc | quote: Bitcoin Bitcoin Cash USDT
  - [2] 2026-11-03: the plans of the 2025 LowEndTalk offer migrate to the 2026 product line on 1 December 2026 | capture: sha256:6532041ec0f217c7d8522ccd81488fe5200dd493aed530f79d02d82ad3b29bd1 | quote: Migration date: 1 December 2026.
- sources:
  - [1] https://massivegrid.com/vps/
  - [2] https://lowendbox.com/blog/massivegrid-when-the-lifetime-price-guarantee-turns-out-to-not-be-quite-so-lifetime/
