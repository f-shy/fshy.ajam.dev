# Arker

> arker.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arker/ | JSON https://fshy.ajam.dev/api/v1/entity/arker.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Arker

- `compute/arker` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-25T05:18:26.643Z (live) | stale on 2026-12-26
- url https://arker.ai/docs/pricing
- free tier: Cost to run one VM (1 vCPU, 2GiB RAM) for an hour, on public on-demand list prices as of 6/11/2026 Using c7gd.metal on AWS and AX162-S on Hetzner. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): 14x to 20x the public on-demand rate: $0.0828 to $0.1193 an hour for a 1 vCPU and 2 GiB VM [1]
  - retention-clamped: the multiplier is quoted against list prices as of 2026-06-11, so the underlying rate moving changes the price [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing documentation was read on 2026-10-22 and states the rate as a multiple of AWS and Hetzner list prices. There is no free tier, so the verdict moves to paid-only, and the multiplier is the fact a reader needs
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.ram: 2
  - shape.note: the page's reference shape, on c7gd.metal at AWS and AX162-S at Hetzner
  - session_cap.restart_required: no
  - session_cap.note: the page states no clock; the product is a priced wrapper on a user's own cloud
  - free_tier_kind: none
  - burst_x: 1.0
  - net.out: yes
  - net.in: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$0.0828/hr 14x' and '$0.1193/hr 20x', with 'Cost to run one VM (1 vCPU, 2GiB RAM) for an hour, on public on-demand list prices as of 6/11/2026 Using c7gd.metal on AWS and AX162-S on Hetzner', quoted
  - [1] 2026-11-25: the vendor's pricing page states the 1 vCPU and 2GiB reference VM and the on-demand list-price basis as of 2026-06-11 | capture: sha256:f58688de24a41d60486b71371155c20b80835f4e99d523c97a5612b3aa131381 | quote: Cost to run one VM (1 vCPU, 2GiB RAM) for an hour, on public on-demand list prices as of 6/11/2026 Using c7gd.metal on AWS and AX162-S on Hetzner.
- sources:
  - [1] https://arker.ai/docs/pricing
