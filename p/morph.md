# Morph Cloud

> morph.so | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/morph/ | JSON https://fshy.ajam.dev/api/v1/entity/morph.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Morph Cloud

- `compute/morph-cloud` | paid-only | evidence documented | binding volume-quota | category container and VM sandbox | tier Free Developer
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:52:56.000Z (live) | stale on 2026-11-24
- url https://cloud.morph.so/web/subscribe
- free tier: 'Starting credit allocation | 0 MCUs' on the Free Developer tier, with 'Pricing | $0 / month Purchase MCUs to use compute'. The Popular Team tier is '$40 / month' with '1000 MCUs'. | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: A zero-credit tier: compute cannot start until MCUs are bought, so there is no free machine at all.
- per-object cap: Instances 'Up to 64 vCPU', RAM 'Up to 256 GB', storage 'Up to 1024 GB' on Free Developer; GitHub Actions runner sizes are 'Small 3 MCU/hr 2 vCPU / 4 GB RAM / 40 GB disk', 'Medium 5 MCU/hr 4 vCPU / 8 GB RAM / 80 GB disk', 'Large 10 MCU/hr 8 vCPU / 16 GB RAM / 160 GB disk'. | source: [1] | note: The shape limits are generous; the balance is zero.
- retention: No retention term is stated on the subscribe page; storage is sold per GB up to the tier cap. | source: [1]
- egress: No egress charge or allowance is stated on the subscribe page. | metered: no | source: [1]
- identity: email | detail: Free signup with no card mentioned; a card is needed for the first MCU purchase. No hold amount is stated.
- interface: unknown
- limits:
  - volume-quota (binding): 0 MCUs of starting credit on the free tier [1]
  - volume-quota (binding): 1000 MCUs for USD 40 a month on Team [1]
- limits note: The MCU price per unit is not stated on the subscribe page, so a per-hour cost cannot be derived without a further page.
- binding note: Zero credit is the constraint: no machine exists on the free tier, whatever the shape limits say.
- interface detail: Access interface not documented in published terms.
- tooling: part of limits note
- composes with: not established
- reliability: no reliability event recorded
- notes: This corrects any reading of Morph as a credit provider: the free tier starts at zero MCUs, so the USD 40 Team tier is a purchase of 1000 MCUs, not a grant. The MCU-to-dollar rate is on a different page and was not read, so this record claims no hourly price; 1000 MCUs at USD 40 would make a Medium runner 5 MCU an hour, i.e. USD 0.20, which is arithmetic on an unverified unit price and is not used in the ranking.
- evidence note: The zero starting allocation and the tier prices are on the subscribe page read. The per-MCU dollar rate is not on that page, so no hourly price is claimed.
- extras:
  - keep_rate: 1.0
  - billing_model: prepaid MCUs
  - shape.vcpu: 4
  - shape.ram_gib: 8
  - shape.disk_gib: 80
  - session_cap.restart_required: no
  - session_cap.note: instances persist while paid; devboxes are ephemeral
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.gib: 40
  - ps.price: included in the runner size
  - ps.durability: runner disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the runner exists
  - term: monthly or prepaid
  - price_arithmetic: not computable from the page read: MCU unit price unstated
  - credit_usd: 0
  - credit_hours_at_shape: 0
  - credit_expiry: not applicable
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '| Starting credit allocation | 0 MCUs | 1000 MCUs | 7500 MCUs |' with 'Pricing $0/month. Purchase MCUs to use compute', 'Concurrency 8', and the runner sizes '2 vCPU / 4 GB / 40 GB disk' upward, quoted
  - [1] 2026-10-24: quoted: 'Starting credit allocation | 0 MCUs'; '$0 / month Purchase MCUs to use compute'; 'PopularTeam ... $40 / month 20% Discount ($50 value)' with '1000 MCUs'; 'Medium 5 MCU/hr 4 vCPU / 8 GB RAM / 80 GB disk'.
- sources:
  - [1] https://cloud.morph.so/web/subscribe
