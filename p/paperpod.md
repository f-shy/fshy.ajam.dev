# PaperPod

> paperpod.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/paperpod/ | JSON https://fshy.ajam.dev/api/v1/entity/paperpod.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PaperPod

- `compute/paperpod` | qualifies-with-caveat | evidence reported | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:16.349Z (live) | stale on 2026-11-19
- url https://www.paperpod.dev/
- free tier: USD 5.0 of one-time credit, from catalog records; unverified against live endpoints | unit: mixed | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: cli, rest
- limits:
  - write-gated (binding): access is a CLI; the page publishes no plan and no price [1]
- interface detail: ppod CLI (npm package @paperpod/cli) and an HTTP API (POST /execute with a bearer token); no SDK
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and demonstrates the CLI and persistent context but publishes no plan or price, so the USD 5 credit still rests on documented records card
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 'Persistent context across sessions' is the state claim; the page states no clock
  - persistent_storage.price: not stated
  - persistent_storage.durability: context persists across sessions
  - persistent_storage.on_stop: yes
  - persistent_storage.on_destroy: no
  - persistent_storage.max_retention: not stated
  - free_tier_kind: one-time-credit
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the site was read on 2026-10-22 and shows CLI usage (`ppod exec`, `ppod interpret`) with 'Persistent context across sessions'; it publishes no plan and no price
  - [2] 2026-11-03: the vendor documents a CLI (ppod) and an HTTP API | capture: sha256:90075d756692af1039302e4a6f61b821b92c44016f51a6a31435de9939172012 | quote: all via CLI or HTTP, no SDK or API keys required
  - [3] 2026-11-03: the pricing line lists compute per second, AI per 1K neurons and a $5 credit, with no egress allowance or overage price | capture: sha256:6ea385b7fcfd45ed11e52312e6db0556026937dff876042d5bb289bda06b9bdf | quote: Pricing: $0.0001/sec compute, $0.02/1K neurons AI. $5 free.
- sources:
  - [1] https://www.paperpod.dev/
  - [2] https://paperpod.dev/SKILL.md
  - [3] https://www.paperpod.dev/docs
