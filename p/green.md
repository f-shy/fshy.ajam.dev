# GreenCloudVPS Storage

> green.cloud | Storage, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/green/ | JSON https://fshy.ajam.dev/api/v1/entity/green.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GreenCloudVPS Storage KVM

- `storage/greencloudvps-storage-kvm` | qualifies | evidence reported | binding per-ip-shaping | category storage-vps
- identity a placeholder: card and phone unknown | verified 2026-11-25T12:15:41.805Z (live) | stale on 2026-12-10
- url https://green.cloud/storage-kvm-vps.php
- price $3.33/TB/mo at the 2 TB rung ($80/yr = $6.67/mo). At 5 TB: 2x Storage-2 + 1x Storage-1 = $13.33 + $3.75 = $17.08/mo = $3.42/TB. At 20 TB: 10x Storage-2 = $66.67/mo = $3.33/TB. Annual-only pricing; the per-TB rate is already the annual rate. | parsed USD 3.33/TB-mo
- free tier: | Storage-2 | 2048GB SATA | 4 cores | 6 GB | 10 TB | 10Gbps Port | Linux | 24/7/365 | $80/year | Order | | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: The plan page lists storage, CPU, memory, bandwidth and port speed and states no per-object limit.
- retention: source: [1] | note: The plan page states no retention or deletion policy.
- egress: Each plan lists a bandwidth allowance (US/EU 3, 6 or 10 TB; APAC 1, 2 or 4 TB); the page gives no period for it. Additional bandwidth costs $3/TB/mo in the US/EU and $15/TB/mo in APAC. | metered: yes | free allowance: 10 TB on Storage-2 in the US/EU (the page states no period) | price per TB: $3/TB/mo in the US/EU; $15/TB/mo in APAC
- identity: card | detail: unverified: the cited pricing page states no payment method; the order flow was not entered
- interface: unknown
- limits:
  - per-ip-shaping (binding): 10Gbps Port [1]
- limits note: per-object-cap: none stated. Up to 20TB of additional storage per plan at $5/TB/mo, subject to server availability. APAC plans list 1, 2 or 4 TB of bandwidth against 3, 6 or 10 TB for US/EU.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: unverified: the plan page names no access protocol or client tool
- tooling: unverified: the plan page names no access protocol or client tool; it lists a KVM VPS with Linux
- composes with: Plans are KVM VPSes with 500GB, 1024GB or 2048GB of SATA storage. A plan can add up to 20TB of additional storage at $5/TB/mo, subject to server availability.
- reliability: '#1 Top Provider Award & #1 Most Stable Provider on LowEndTalk' is their own claim on their own page. Widely used in the LET storage-VPS recommendation threads with no data-loss reports surfaced.
- notes: US/EU: Storage-0.5TB 500 GB, Storage-1 1 TB, Storage-2 2 TB (SATA RAID-10, 10 Gbps port). APAC: same three sizes in Tokyo and Singapore but with a quarter of the bandwidth. No plan above 2 TB exists.
- evidence note: the same as the free tier
- extras:
  - price_verbatim: $3.33/TB/mo at the 2 TB rung ($80/yr = $6.67/mo). At 5 TB: 2x Storage-2 + 1x Storage-1 = $13.33 + $3.75 = $17.08/mo = $3.42/TB. At 20 TB: 10x Storage-2 = $66.67/mo = $3.33/TB. Annual-only pricing; the per-TB rate is already the annual rate.
- evidence:
  - [1] 2026-10-21: APAC block identical pricing with 1/2/4 TB
  - [2] 2026-10-21: user citing GreenCloud 500 GB / 3 TB for '$2.08 / month'
  - [1] 2026-11-09: The pricing table states the Storage-2 plan and its allowance. | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: | Storage-2 | 2048GB SATA | 4 cores | 6 GB | 10 TB | 10Gbps Port | Linux | 24/7/365 | $80/year | Order |
  - [1] 2026-11-09: The plan row states a 10Gbps port. | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: 10Gbps Port
  - [1] 2026-11-25: the page names a 10Gbps port and RAID-10 SATA drives and no access protocol | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: Connected to a 10Gbps port with Enterprise SATA drives in Hardware RAID-10 (NVMe boot drive available in some locations) for performance and reliability.
  - [1] 2026-11-25: no access protocol is named | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: Connected to a 10Gbps port with Enterprise SATA drives in Hardware RAID-10 (NVMe boot drive available in some locations) for performance and reliability.
  - [1] 2026-11-25: the plan row lists Linux and no access method | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: | Storage-2 | 2048GB SATA | 4 cores | 6 GB | 10 TB | 10Gbps Port | Linux | 24/7/365 | $80/year | Order |
  - [1] 2026-11-25: up to 20TB of additional storage can be added at $5/TB/mo | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: - You can add up to 20TB additional storage with the price of $5/TB/mo. RAM: $3/1GB RAM/mo, CPU: $3/CPU Core/mo. Subject to server availability.
  - [1] 2026-11-25: additional storage up to 20TB is sold | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: - You can add up to 20TB additional storage with the price of $5/TB/mo. RAM: $3/1GB RAM/mo, CPU: $3/CPU Core/mo. Subject to server availability.
  - [1] 2026-11-25: additional bandwidth is priced at $3/TB/mo US/EU and $15/TB/mo APAC | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: - Price for additional bandwidth: $3/TB/mo in the US/EU and $15/TB/mo in APAC
  - [1] 2026-11-25: the additional bandwidth price | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: - Price for additional bandwidth: $3/TB/mo in the US/EU and $15/TB/mo in APAC
  - [1] 2026-11-25: the BANDWIDTH column lists 10 TB for Storage-2, with no period | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: | Storage-2 | 2048GB SATA | 4 cores | 6 GB | 10 TB | 10Gbps Port | Linux | 24/7/365 | $80/year | Order |
  - [1] 2026-11-25: the plan columns include no per-object limit | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: | PLAN NAME | STORAGE | CPU | MEMORY | BANDWIDTH | GIG | OS | TECHNICAL SUPPORT | PRICE |
  - [1] 2026-11-25: the plan columns include no retention term | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: | PLAN NAME | STORAGE | CPU | MEMORY | BANDWIDTH | GIG | OS | TECHNICAL SUPPORT | PRICE |
  - [1] 2026-11-25: the Storage-2 row: 2048GB SATA, 10 TB bandwidth, 10Gbps Port, $80/year | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: | Storage-2 | 2048GB SATA | 4 cores | 6 GB | 10 TB | 10Gbps Port | Linux | 24/7/365 | $80/year | Order |
- sources:
  - [1] https://green.cloud/storage-kvm-vps.php
  - [2] https://lowendtalk.com/discussion/193376/

## GreenCloudVPS

- `egress/greencloud-storage-0-5tb` | paid-only | evidence documented | binding volume-quota | category cheap-egress VPS (storage KVM, 10 Gbps port) | tier Storage-0.5TB
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:17.777Z (live) | stale on 2026-12-05
- url https://green.cloud/storage-kvm-vps.php
- free tier: No free tier. Storage-0.5TB is USD 25 a year with 500GB SATA, 2 GB RAM, 3 TB bandwidth and a 10Gbps port. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The aggregator names the plan 10Gbps Storage 0.5TB and lists it at USD 25.0 a year.
- per-object cap: not applicable: a VPS, not an object store | source: [1]
- retention: not applicable | source: [1]
- egress: 3 TB bandwidth on a 10Gbps port; the period and the overage rule are not published on the page read. | metered: yes | free allowance: 3 TB, period not stated | source: [1]
- identity: email | detail: unverified: behind a sign-up. The plan page lists an Order button and no sign-up fields.
- interface: ssh
- limits:
  - volume-quota (binding): 3 TB bandwidth, period and overage not published [1]
- limits note: The vendor billing host answered HTTP 403 to the affiliate link; the vendor's own storage page was read instead.
- binding note: 3 TB is the only stated cap on the plan row.
- interface detail: KVM storage VPS on SATA hardware RAID-10; 1 IPv4 and a /112 or /64 IPv6 by default.
- tooling: Any SSH client.
- composes with: 1 IPv4 and /112 or /64 IPv6 assigned by default on a 10Gbps port; no port filter or protocol list is published on the page read.
- reliability: unverified: stock and location availability of the plan were not read.
- notes: A storage-topic record for the GreenCloudVPS storage line exists; this record is the plan an aggregator lists.
- evidence note: Plan row read on the vendor storage page on 2026-11-04; period, overage and sign-up fields are unverified.
- extras:
  - nat_ports: not applicable: dedicated IPv4
  - ipv6: /112 or /64
  - udp_forwarding: unverified: not stated
  - routed_ipv6_prefix: /112 or /64 by default
  - inbound_ipv4_ports: unverified
  - term: 12 months
  - virtualization: KVM
- evidence:
  - [1] 2026-11-04: the plan row lists 3 TB, a 10Gbps port and USD 25 a year | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: | Storage-0.5TB | 500GB SATA | 1 core | 2 GB | 3 TB | 10Gbps Port | Linux | 24/7/365 | $25/year | Order |
  - [1] 2026-11-04: the storage VPS gets 1 IPv4 and a /112 or /64 IPv6 | capture: sha256:50c7e7e87b19a90c27f470d68260ff48a85dad8b99c0100be2bc2713dd47a542 | quote: 1 IPv4 and /112 or /64 IPv6 are assigned to each VPS by default.
  - [2] 2026-11-04: serverdeals lists GreenCloud 10GbpsStorage0.5TB at USD 25.0 a year with 3 TB | capture: sha256:74205844fcd10df773b4c9dceb9f0293e9016e911c7fa802feb8a1b72c886965 | quote: #### USD 25.0 / year
- sources:
  - [1] https://green.cloud/storage-kvm-vps.php
  - [2] https://serverdeals.cc/
