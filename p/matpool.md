# Matpool

> matpool.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/matpool/ | JSON https://fshy.ajam.dev/api/v1/entity/matpool.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Matpool

- `compute/matpool` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T08:50:51.585Z (live) | stale on 2026-12-04
- url https://matpool.com/host-market/gpu
- free tier: Chinese GPU cloud (JuChiYun) publishing per-hour rates per zone with visible card availability: RTX 5090 32GB CNY 2.99/hr on 16 cores, 60 GB RAM and 300 GB SSD; RTX A6000 48GB CNY 2.85/hr on 12 cores, 86 GB RAM and 350 GB SSD; A100 40GB CNY 2.80/hr; RTX 4090 24GB CNY 2.20/hr; A30 24GB CNY 2.19/hr. At USD 1 = CNY 6.6743 that is USD 0.448, USD 0.427, USD 0.420, USD 0.330 and USD 0.328 per GPU-hour. Each row states the zone and how many cards that zone has free, for example a zone labelled as having at most two cards available. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: signup-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: country-phone | detail: Registration is documented as a mobile number plus an SMS code: the register page shows the steps translated as 'verify mobile number', then the mobile number field and the SMS code field. | country: CN
- interface: unknown
- limits:
  - write-gated (binding): The SMS registration step fails first: no account exists without a Chinese mobile number, and the new-user credit is only claimable after that step. [1]
- limits note: The SMS registration step fails first: no account exists without a Chinese mobile number, and the new-user credit is only claimable after that step.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The trial credit is unquantified, so it composes with nothing until an account exists; the A100 40GB row at USD 0.42/hr is the cheapest 40 GB A100 hour seen among evaluated providers, below Jarvislabs at USD 0.89.
- reliability: no reliability event recorded
- notes: Rates sit above AutoDL and Featurize for the same cards, so this is a supply-and-zone story rather than a price story: the zone labels and per-zone card counts are the part that other Chinese retailers do not publish. The size of the new-user credit is not stated on the page and was not established; it would need an account. Conversion uses the same 2026-10-22 rate as the other Chinese records in this batch.
- extras:
  - facets.class: regional-gpu-retailer
  - facets.free_tier_kind: signup-credit
  - facets.shape.vcpu: 10
  - facets.shape.ram_gib: 50
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 24
  - facets.shape.disk_gib: 300
- evidence:
  - [1] 2026-10-22: translated from the Chinese page, each rate marked as billed by the hour: RTX 5090 32GB CNY 2.99 on 16 cores and 60GB RAM; RTX A6000 48GB CNY 2.85; A100 40GB CNY 2.80; RTX 4090 24GB CNY 2.20; A30 24GB CNY 2.19
  - [1] 2026-10-22: each row carries a per-zone free-card count, translated as at most one card available and at most two cards available, which is a supply figure rather than an account cap
  - [2] 2026-10-22: translated from the register page: a new-user trial credit is given on registering, and the form steps are verify mobile number, mobile number, SMS code, set password
  - [3] 2026-10-22: USD 1 = CNY 6.6743 on 2026-10-22
  - [1] 2026-11-03: RTX 4090 24GB is CNY 2.20 per hour, marked as billed by the hour; the page lists no H100, L40S or L4 and no A100 other than the 40GB card, and states no minimum bill | capture: sha256:a922362ad142c975ea22ab201e5a168b9360ef859480b4366e52e131ba043c5b | quote: ¥2.20/小时按时计费
  - [1] 2026-11-03: A100 40GB is CNY 2.80 per hour, billed by the hour | capture: sha256:a922362ad142c975ea22ab201e5a168b9360ef859480b4366e52e131ba043c5b | quote: ¥2.80/小时按时计费
  - [1] 2026-11-03: RTX 5090 32GB is CNY 2.99 per hour, billed by the hour | capture: sha256:a922362ad142c975ea22ab201e5a168b9360ef859480b4366e52e131ba043c5b | quote: ¥2.99/小时按时计费
  - [1] 2026-11-03: RTX 4090 is CNY 2.20 per hour, marked as billed by the hour | capture: sha256:a922362ad142c975ea22ab201e5a168b9360ef859480b4366e52e131ba043c5b | quote: ¥2.20/小时按时计费
- sources:
  - [1] https://matpool.com/host-market/gpu
  - [2] https://matpool.com/register
  - [3] https://api.frankfurter.app/latest?from=USD&to=CNY
