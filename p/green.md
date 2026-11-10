# GreenCloudVPS Storage

> green.cloud | Storage, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/green/ | JSON https://fshy.ajam.dev/api/v1/entity/green.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GreenCloudVPS Storage KVM

- `storage/greencloudvps-storage-kvm` | qualifies | evidence reported | binding per-ip-shaping | category storage-vps
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://green.cloud/storage-kvm-vps.php
- price $3.33/TB/mo at the 2 TB rung ($80/yr = $6.67/mo). At 5 TB: 2x Storage-2 + 1x Storage-1 = $13.33 + $3.75 = $17.08/mo = $3.42/TB. At 20 TB: 10x Storage-2 = $66.67/mo = $3.33/TB. Annual-only pricing; the per-TB rate is already the annual rate. | parsed USD 3.33/TB-mo
- free tier: US/EU: Storage-0.5TB 500 GB, Storage-1 1 TB, Storage-2 2 TB (SATA RAID-10, 10 Gbps port). APAC: same three sizes in Tokyo and Singapore but with a quarter of the bandwidth. No plan above 2 TB exists. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Metered annual-bundled allowance, no published overage rate. US/EU: 0.5 TB->3 TB, 1 TB->6 TB, 2 TB->10 TB per month. APAC: 0.5 TB->1 TB, 1 TB->2 TB, 2 TB->4 TB. I.e. APAC is 1/2.5 of the US figure. This is the Asia option's real trap: the Tokyo/Singapore plans cost the same as US/EU and give 40% of the traffic. | metered: yes | free allowance: 10 TB per month
- identity: card | detail: card
- interface: rest, sftp, rsync, rclone
- limits:
  - per-ip-shaping (binding): 10 Gbps [1]
- limits note: per-object-cap: none. Hard 2 TB per-VM ceiling. APAC bandwidth 40% of US/EU.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: sftp, rsync, rest (self-hosted)
- tooling: rclone SFTP, root KVM
- composes with: Root KVM on a 10 Gbps port, which is unusually fast for this price class. Ceiling of 2 TB per VM means 10 VMs for 20 TB. Workable for the chunk-and-replicate pattern but not for a single 10 TiB working set.
- reliability: '#1 Top Provider Award & #1 Most Stable Provider on LowEndTalk' is their own claim on their own page. Widely used in the LET storage-VPS recommendation threads with no data-loss reports surfaced.
- notes: the same as the free tier
- extras:
  - price_verbatim: $3.33/TB/mo at the 2 TB rung ($80/yr = $6.67/mo). At 5 TB: 2x Storage-2 + 1x Storage-1 = $13.33 + $3.75 = $17.08/mo = $3.42/TB. At 20 TB: 10x Storage-2 = $66.67/mo = $3.33/TB. Annual-only pricing; the per-TB rate is already the annual rate.
- evidence:
  - [1] 2026-10-21: APAC block identical pricing with 1/2/4 TB
  - [2] 2026-10-21: user citing GreenCloud 500 GB / 3 TB for '$2.08 / month'
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
  - [2] 2026-11-04: serverdeals lists GreenCloud 10GbpsStorage0.5TB at USD 25.0 a year with 3 TB | quote: #### USD 25.0 / year
- sources:
  - [1] https://green.cloud/storage-kvm-vps.php
  - [2] https://serverdeals.cc/
