# Omnara

> omnara.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/omnara/ | JSON https://fshy.ajam.dev/api/v1/entity/omnara.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Omnara

- `compute/omnara` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:14.181Z (live) | stale on 2026-12-05
- url https://www.omnara.com/pricing
- free tier: no platform fee: the software is free and users bring models and machines, or pays $0.0414 a GiB-hour of memory for an Omnara-managed machine, which auto-sleeps when idle | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page bills Omnara-managed machines for memory runtime and retention and states no egress allowance or price | metered: no | source: [1]
- identity: email
- interface: rest, cli
- limits:
  - request-rate (binding): $0.0414 a GiB of memory an hour while a managed machine is online [1]
  - retention-clamped: an idle machine auto-sleeps, preserving data and pausing runtime charges; a retention charge continues [1]
- interface detail: web dashboard, CLI, REST API and TypeScript SDK
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the zero platform fee, the per-GiB-hour rate and the auto-sleep behaviour. The free half is the software; the managed machines are metered
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.ram: 4
  - shape.note: the page's worked example is a 4 GiB machine an hour a day
  - session_cap.restart_required: no
  - session_cap.note: idle machines auto-sleep and keep their data; the page states no fixed interval
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.price: a retention charge continues while a machine is asleep
  - ps.durability: sleep preserves data
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'The full platform is free. Bring your own models and machines, or pay as you go for Omnara-managed resources.' with ' $0 platform fee', '$0.0414 per GiB of memory per hour online', and 'Idle machines auto-sleep, preserving data and pausing runtime charges', quoted
  - [1] 2026-11-03: machine charges are runtime and retention only; no egress line | capture: sha256:8e7d8a21339f16a0eda255a54ab5a5095ce6cbc7242721e53a0c1a84c750fed6 | quote: Omnara-managed machines, billed for storage and active time
  - [2] 2026-11-03: REST API and CLI exist | capture: sha256:4eee030d6b66aed445bb0c38432dc430eb1b7f0894a3b02ad12ddb66ae79027d | quote: Omnara exposes a web interface, CLI, and REST API to enable these use cases.
- sources:
  - [1] https://www.omnara.com/pricing
  - [2] https://docs.omnara.com
