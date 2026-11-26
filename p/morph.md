# Morph Cloud

> morph.so | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/morph/ | JSON https://fshy.ajam.dev/api/v1/entity/morph.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Morph Cloud

- `compute/morph-cloud` | paid-only | evidence documented | binding volume-quota | category container and VM sandbox | tier Free Developer
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:03:52.933Z (live) | stale on 2026-12-26
- url https://cloud.morph.so/web/subscribe
- free tier: The $0 tier starts with '| Starting credit allocation | 0 MCUs | 1000 MCUs | 7500 MCUs |'; the same table prices it '| Pricing | $0 / monthPurchase MCUs to use compute | $40 / month20% Discount ($50 value) | $250 / month33% Discount ($375 value) |'. | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: A zero-credit tier: compute cannot start until MCUs are bought, so there is no free machine at all.
- per-object cap: Instances 'Up to 64 vCPU', RAM 'Up to 256 GB', storage 'Up to 1024 GB' on Free Developer; GitHub Actions runner sizes are 'Small 3 MCU/hr 2 vCPU / 4 GB RAM / 40 GB disk', 'Medium 5 MCU/hr 4 vCPU / 8 GB RAM / 80 GB disk', 'Large 10 MCU/hr 8 vCPU / 16 GB RAM / 160 GB disk'. | source: [1] | note: The shape limits are generous; the balance is zero.
- retention: No retention term is stated on the subscribe page; storage is sold per GB up to the tier cap. | source: [1]
- egress: No egress charge or allowance is stated on the subscribe page. | metered: no | source: [1]
- identity: email | detail: Free signup with no card mentioned; a card is needed for the first MCU purchase. No hold amount is stated.
- interface: cli, ssh, rest
- limits:
  - volume-quota (binding): 0 MCUs of starting credit on the free tier [1]
  - volume-quota (binding): 1000 MCUs for USD 40 a month on Team [1]
- limits note: The MCU price per unit is not stated on the subscribe page, so a per-hour cost cannot be derived without a further page.
- binding note: Zero credit is the constraint: no machine exists on the free tier, whatever the shape limits say.
- interface detail: Python and TypeScript SDKs and the morphcloud CLI; devbox access over SSH and HTTP services exposed to the public internet
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
  - [1] 2026-11-25: the subscribe table still shows 0 MCUs of starting credit on the USD 0 tier and 1000 MCUs on the USD 40 tier | capture: sha256:26665673e6b91e2a9299b2bf3cb95108300edff972f6619faa701d2975ac4ba2 | quote: | Starting credit allocation | 0 MCUs | 1000 MCUs | 7500 MCUs |
  - [1] 2026-11-24: the subscribe page lists 0 MCUs of starting credit on the $0 Developer tier and 1000/7500 MCUs on the paid tiers | capture: sha256:26665673e6b91e2a9299b2bf3cb95108300edff972f6619faa701d2975ac4ba2 | quote: | Starting credit allocation | 0 MCUs | 1000 MCUs | 7500 MCUs |
  - [1] 2026-11-24: the $0 tier requires buying MCUs while the $40 and $250 tiers bundle 1000 and 7500 MCUs | capture: sha256:26665673e6b91e2a9299b2bf3cb95108300edff972f6619faa701d2975ac4ba2 | quote: | Pricing | $0 / monthPurchase MCUs to use compute | $40 / month20% Discount ($50 value) | $250 / month33% Discount ($375 value) |
  - [2] 2026-11-24: Morph documents a CLI that starts devboxes and runs commands over SSH | capture: sha256:87170a9eff405511f4d734196e1eecc62217e74568caad333e059a1d7aaf3e73 | quote: morphcloud devbox ssh "$DEVBOX_ID" echo "Hello from a Morph Devbox!"
  - [3] 2026-11-24: Morph documents SSH access and SDK/CLI clients | capture: sha256:d4cda99c9254fba1e3fb95d9c82f98238b21b6bfef3f5ccd6a527643d090291b | quote: MorphCloud provides SSH access to your instances. You'll need to configure SSH keys and connect using the provided connection details.
  - [4] 2026-11-24: the sign-up doc claims 300 free compute hours a month on the $0 Developer Plan once the user has an invite | capture: sha256:4950c8be6f5d8d1e90409247145c69b269e363713cc8c9a5865867340b97b88b | quote: Once you have your invite, our $0/month Developer Plan provides 300 free compute hours per month
  - [3] 2026-11-24: the FAQ repeats the 300 free compute hours per month claim for the Developer Plan | capture: sha256:d4cda99c9254fba1e3fb95d9c82f98238b21b6bfef3f5ccd6a527643d090291b | quote: Yes! The Developer Plan provides 300 free compute hours per month with pay-as-you-go pricing after that.
- sources:
  - [1] https://cloud.morph.so/web/subscribe
  - [2] https://cloud.morph.so/docs/developers
  - [3] https://cloud.morph.so/docs/faq
  - [4] https://cloud.morph.so/docs/documentation/setup/signing-up
