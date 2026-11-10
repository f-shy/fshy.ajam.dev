# lightnode 'storage

> lightnode.com | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lightnode/ | JSON https://fshy.ajam.dev/api/v1/entity/lightnode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LightNode

- `compute/lightnode-tokyo` | paid-only | evidence documented | binding volume-quota | category VPS | tier Start (Tokyo)
- identity a placeholder: card and phone unknown | verified 2026-10-24T02:05:00.000Z (live) | stale on 2026-11-24
- url https://go.lightnode.com/tokyo-vps
- price parsed USD 7.71/mo
- free tier: no free tier; the Tokyo Start plan is USD 7.71 a month and is billed hourly | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: hourly billing; the instance persists while the balance lasts | source: [1]
- egress: 1 TB of bandwidth a month on the Start plan, 2 TB on Agency | metered: yes | free allowance: 1 TB | source: [1]
- identity: email | detail: unverified: the price page was read and the console was not. LightNode advertises PayPal and Alipay on its Chinese-language mirror, which implies no card wall, but that page was not read first party here
- interface: ssh, rest
- limits:
  - volume-quota (binding): 1 TB a month of bandwidth on Start [1]
- binding note: the price binds before the bandwidth: USD 7.71 is above the line on the smallest plan, and hourly billing at USD 0.04 an hour would be worse for 24/7 use
- interface detail: root SSH; the vendor's web console; a REST API where documented
- tooling: any SSH client
- composes with: recorded to close a lead: the cheapest Tokyo shape is 1 vCPU / 2 GB / 50 GB NVMe at USD 7.71, so LightNode has nothing under the line
- reliability: no reliability event recorded
- notes: Hourly billing exists but the hourly rate for this shape was not read on this page, so no 10 h/day figure is recorded. Nothing here is under USD 5 in any region.
- evidence note: price and shape from the vendor's Tokyo page today; identity and payment unverified
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 2
  - shape.disk_gib: 50
  - billing_model: hourly, displayed as a monthly equivalent
  - term: hourly
  - m24h_usd: 7.71
  - price_arithmetic: USD 7.71 a month as printed; no hourly rate read, so the 10 h/day figure is left null rather than derived
  - renewal_usd: 7.71
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS that bills whether it runs or not
  - english: yes
  - payment_methods: not read
- evidence:
  - [1] 2026-10-24: quoted: 'Start $7.71/month Tokyo VPS - 2 GB DDR4 Memory - 1 vCPU High Frequency - 50 GB NVMe SSD Storage - 1 TB Bandwidth'
- sources:
  - [1] https://go.lightnode.com/tokyo-vps

## lightnode 'storage vps' line

- `storage/lightnode-storage-vps-line` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://go.lightnode.com/storage-vps
- free tier: none reachable: Storage VPS tiers include 50 GB NVMe across all pricing options. The maximum published disk allocation is 50 GB at $52.70 per month. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Marketed as a storage product but every rung ships 50 GB of NVMe regardless of price. There is no big-disk SKU at all — the largest is 50 GB for $52.70/mo.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Marketed as a storage product but every rung ships 50 GB of NVMe regardless of price. There is no big-disk SKU at all — the largest is 50 GB for $52.70/mo.
- sources:
  - [1] https://go.lightnode.com/storage-vps
