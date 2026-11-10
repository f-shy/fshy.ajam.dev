# MIOSA

> miosa.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/miosa/ | JSON https://fshy.ajam.dev/api/v1/entity/miosa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MIOSA

- `compute/miosa` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T06:29:27.324Z (live) | stale on 2026-12-05
- url https://miosa.ai/pricing
- free tier: $1 of usage every month with no monthly charge, 1 computer with machines up to 4 vCPU and 8 GB, 5 sandboxes at once, and no overage: machines pause at a $0 balance | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Egress is billed at $0.054 per GB from the first GB, with no free tier; plans cap egress per month: Free 5 GB, Developer 100 GB, Business 1 TB, Enterprise 5 TB | metered: yes | free allowance: none: egress is billed from the first GB (the Free plan caps egress at 5 GB a month) | price per TB: $54 per TB ($0.054 per GB) | source: [1]
- identity: email
- interface: cli, ssh, rest
- limits:
  - request-rate (binding): $10 of credit, one time; machines up to 4 vCPU and 8 GiB [1]
  - retention-clamped: at a zero balance without a card, machines pause or stop and nothing is deleted [1]
- interface detail: CLI (miosa create, ssh, files cp, exec), SSH into a sandbox, REST API and a TypeScript SDK
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the credit, the shape ceiling and the no-overage behaviour. That last clause is the state answer: exhaustion pauses rather than deletes
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 4
  - shape.ram: 8
  - shape.note: the ceiling per machine on the free tier; the paid tiers go to 16 vCPU and 64 GiB
  - session_cap.restart_required: no
  - session_cap.note: no overage: exhaustion pauses or stops the machine rather than deleting it, so the state survives the credit running out
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
  - ps.price: not stated on this page
  - ps.durability: the machine survives a pause
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Start free with $10 of credits. Add a card to auto-reload and keep going.' with '$0 no monthly charge', 'Up to 4 vCPU / 8 GiB per machine', 'Sandboxes up to 4 vCPU / 8 GiB', and 'No overage: without a card at a $0 balance, machines pause or stop; nothing is deleted', quoted
  - [1] 2026-11-03: egress price per GB | capture: sha256:a5925dceec18de9c2b7704b80f9da33b5fb1804f004833a2586005d390996a20 | quote: | Egress | $0.054 | / GB | Data leaving MIOSA, from the first GB |
  - [1] 2026-11-03: CLI and SSH access | capture: sha256:a5925dceec18de9c2b7704b80f9da33b5fb1804f004833a2586005d390996a20 | quote: - `$ miosa ssh / files cp`Shell in, copy files
  - [1] 2026-11-03: the Free plan includes 5 GB of egress a month | capture: sha256:a5925dceec18de9c2b7704b80f9da33b5fb1804f004833a2586005d390996a20 | quote: - *✓* Egress a month: 5 GB
  - [1] 2026-11-03: a REST API, a TypeScript SDK and a CLI exist | capture: sha256:a5925dceec18de9c2b7704b80f9da33b5fb1804f004833a2586005d390996a20 | quote: For programs, see the [API](https://miosa.ai/docs/api-reference/), the [TypeScript SDK](https://miosa.ai/docs/sdks/typescript/) and the [CLI docs](https://miosa.ai/docs/cli/).
  - [1] 2026-11-03: the Free plan credit is $1 a month, not $10 one time | capture: sha256:a5925dceec18de9c2b7704b80f9da33b5fb1804f004833a2586005d390996a20 | quote: Start free with $1 of usage every month.
  - [1] 2026-11-04: monthly egress caps per plan: Free 5 GB, Developer 100 GB, Business 1 TB, Enterprise 5 TB | capture: sha256:a5925dceec18de9c2b7704b80f9da33b5fb1804f004833a2586005d390996a20 | quote: | Egress per month | 5 GB | 100 GB | 1 TB | 5 TB |
  - [1] 2026-11-04: egress is billed from the first GB with no free tier | capture: sha256:a5925dceec18de9c2b7704b80f9da33b5fb1804f004833a2586005d390996a20 | quote: Egress is billed from the first GB; there is no free tier.
- sources:
  - [1] https://miosa.ai/pricing
