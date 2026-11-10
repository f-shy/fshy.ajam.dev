# Freestyle

> freestyle.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freestyle/ | JSON https://fshy.ajam.dev/api/v1/entity/freestyle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Freestyle

- `compute/freestyle` | qualifies-with-caveat | evidence documented | binding volume-quota | category container and VM sandbox | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:52:56.000Z (live) | stale on 2026-11-24
- url https://www.freestyle.sh/pricing
- price parsed USD 13.32/mo
- free tier: No cash credit. The Free plan includes 'Hour of vCPU ... 200 per month', 'Hour of GiB Memory ... 400 per month', 'Hour of GiB Storage ... 60,000 per month' and 'GB of Data Transfer ... 50 free'. 'On Free, allowances are hard stops rather than paid overage.' | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: An allowance that resets monthly, worth about USD 13.22 at the vendor's own rates, and a hard stop when it runs out. This is not a USD 100 credit.
- per-object cap: Free plan limits: 'Max vCPUs per VM | 4 vCPUs', 'Max Memory per VM | 8 GiB', 'Max Disk per VM | 32 GiB', 'Concurrent VMs | 10', 'Saved VMs | 10'. | source: [1] | note: 'Persistent VMs | ✗' and 'Custom Sizing | ✗' on Free: a Free VM cannot pick its shape and is not persistent.
- retention: Free has no persistent VMs and no persistent snapshots ('Persistent Snapshots | ✗'); saved VMs are capped at 10. | source: [1]
- egress: 'GB of Data Transfer | $0.02 | 50 free, 500 on paid'; Free includes 50 GB a month. | metered: yes | free allowance: 50 GB a month | price per TB: USD 20 per TB | source: [1]
- identity: email | detail: No card is mentioned for the Free plan; the pricing page lists Free, Hobby and Pro with no payment requirement for Free. No hold exists because no payment method is taken on Free.
- interface: rest, cli
- limits:
  - volume-quota (binding): 200 vCPU-hours, 400 GiB-hours of memory and 60,000 GiB-hours of storage a month [1]
  - volume-quota (binding): 50 GB of data transfer a month on Free [1]
  - per-object-cap: 4 vCPU, 8 GiB and 32 GiB disk per VM on Free [1]
- limits note: Allowances are hard stops: the VM does not throttle, it stops.
- binding note: 200 vCPU-hours is 27% of the 730 vCPU-hours a single 1 vCPU box needs for a month, so the monthly allowance is the constraint, not the shape.
- interface detail: API and CLI; a fixed set of VM sizes on Free
- tooling: SDK and CLI; saved VMs and snapshots on paid plans only
- composes with: the only free allowance here stated in vCPU-hours with a hard stop, which makes the monthly ceiling arithmetic exact
- reliability: A Free VM that hits the monthly allowance stops with no overage path, and Free has no persistent VM, so state has to be snapshotted or rebuilt.
- notes: The free allowance is real, but the useful comparison is against a month of uptime: 730 hours of a 1 vCPU box needs 730 vCPU-hours and 730 GiB-hours of memory, against 200 and 400 included. A 4 vCPU box lasts 50 hours. The allowance is worth USD 8.06 of vCPU plus USD 5.16 of memory at list, so about USD 13.22 a month, not USD 100.
- evidence note: Allowances, per-VM caps, the hard-stop rule and the transfer allowance are on the pricing page read. Not established: whether a Free VM is destroyed at the allowance or merely stopped.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 32
  - billing_model: per-second against a monthly allowance
  - granularity.min_billed_s: 1
  - granularity.rounding_s: 1
  - session_cap.restart_required: no
  - session_cap.note: no published wall-clock cap; the monthly vCPU-hour allowance caps total uptime at 200 h for a 1 vCPU box
  - keep_rate.basis: not stated; a saved VM exists on paid plans only
  - keep_rate.source: https://www.freestyle.sh/pricing
  - persistent_storage.included_gib: 32
  - persistent_storage.price_gib_month: USD 0.000086 per GiB-hour
  - persistent_storage.durability: none on Free
  - persistent_storage.survives_stop: no
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: the VM lifetime
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - free_tier_kind: monthly-allowance
  - m10h_usd: 5.55
  - m24h_usd: 13.32
  - price_arithmetic: 1 vCPU x 0.04032 + 1 GiB x 0.0129 = 0.05322/h; x 730 = 38.85 a month at list; allowance covers 200 h of that, i.e. 27.4%
  - allowance_arithmetic: 200 vCPU-h / 2 vCPU = 100 h of this shape a month, which is 3.3 h a day
  - price_note: gross rate before the 200 vCPU-hour and 400 GiB-hour monthly allowances.
  - price_basis: 10 h/day x 30 = 300 h; 24/7 x 30 = 730 h
  - burst_x: 1.0
  - crosscheck.boat_compare_2026-09-26: USD 0.264/h at 4 vCPU / 8 GB
  - shape_max.vcpu: 4
  - shape_max.ram_gib: 8
  - shape_max.disk_gib: 32
  - term: monthly
  - credit_usd: 0
  - allowance_value_usd: 13.22
  - credit_months_at_shape: 0.27
  - credit_hours_at_shape: 200
  - credit_expiry: resets monthly; unused hours do not carry
- evidence:
  - [1] 2026-10-22: USD 0.04032 per vCPU-hour with 200 a month included; USD 0.0129 per GiB-hour with 400 included; USD 0.02/GB with 50 free
  - [1] 2026-10-22: Free column: 10 concurrent VMs, Persistent VMs forbidden, Persistent Snapshots forbidden, custom sizing forbidden, 4 vCPU and 32 GiB disk maximum
  - [1] 2026-10-22: on Free the allowances are hard stops rather than paid overage
  - [2] 2026-10-22: a competitor's comparison table lists Freestyle at USD 0.264 per hour for a 4 vCPU / 8 GB / 50 GB machine, with list prices dated 2026-09-26; this is a reported rate about a third party and not a reading of the vendor's own page
  - [1] 2026-10-24: quoted: 'Hour of vCPU | $0.04032 | 200 per month', 'Hour of GiB Memory | $0.0129 | 400 per month', 'Hour of GiB Storage | $0.000086 | 60,000 per month', 'GB of Data Transfer | $0.02 | 50 free, 500 on paid', 'On Free, allowances are hard stops rather than paid overage.', 'Persistent VMs | ✗', 'Max vCPUs per VM | 4 vCPUs', 'Max Memory per VM | 8 GiB'.
- sources:
  - [1] https://www.freestyle.sh/pricing
  - [2] https://boat.dev/compare
