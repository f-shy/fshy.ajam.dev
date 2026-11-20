# ParsPack

> parspack.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/parspack/ | JSON https://fshy.ajam.dev/api/v1/entity/parspack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ParsPack

- `compute/parspack` | paid-only | evidence reported | binding none | category VPS | tier frVPS1-Linux (France location)
- identity a placeholder: card and phone unknown | verified 2026-10-24T02:05:00.000Z (live) | stale on 2026-11-08
- url https://parspack.com/vps
- free tier: no free tier; the entry Linux plan is 1,415,000 toman a month in the France location and 1,375,000 in the UK location | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: monthly; the server persists while paid | source: [1]
- egress: 1000 GB a month of traffic (1000 گیگابایت ترافیک ماهانه) on every Linux plan in the block | metered: yes | free allowance: 1000 GB | source: [1]
- identity: national-id | detail: unverified: the price page was read and the signup path was not. The checkout sits behind my.parspack.com and the site is Persian only; an Iranian vendor normally requires a national ID (کد ملی) and an Iranian mobile, but this record does not establish… | country: IR
- interface: ssh, rest
- limits:
  - volume-quota: 1000 GB a month [1]
- binding note: the price in toman is the open question, not the quota: with no market rate read, the row cannot be ranked against the line
- interface detail: root SSH; the vendor's web console; a REST API where documented
- tooling: any SSH client
- composes with: recorded to close a lead: an Iranian host selling European locations, priced in toman, with no rate read so no USD figure is claimed
- reliability: no reliability event recorded
- notes: The toman is quoted at roughly a tenth of the rial, and Iran runs an official rate and a market rate that differ by an order of magnitude. Converting with either without reading it today would invent a number, so m24h_usd is null. This is the one row in this category where the price is known in local currency and deliberately not converted.
- evidence note: the plan block is first party, but the price is in a currency with two rates (official and market) and neither was read, so the USD value is not claimed and the record is ranked as reported
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 25
  - billing_model: monthly
  - term: monthly
  - price_arithmetic: 1,415,000 toman a month as printed; no USD rate read for the toman, so no conversion
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS that bills whether it runs or not
  - english: no; Persian only
  - payment_methods: not read
- evidence:
  - [1] 2026-10-24: quoted: 'frVPS1-Linux 1000 گیگابایت ترافیک ماهانه ... ۱٬۴۱۵٬۰۰۰ تومان/ماهانه 25GB SSD 1 vCPU 1GB RAM'
  - [1] 2026-10-24: quoted: 'ukVPS1-Linux ... ۱٬۳۷۵٬۰۰۰ تومان/ماهانه 25GB SSD 1 vCPU 1GB RAM'
- sources:
  - [1] https://parspack.com/vps
