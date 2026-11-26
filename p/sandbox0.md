# Sandbox0

> sandbox0.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sandbox0/ | JSON https://fshy.ajam.dev/api/v1/entity/sandbox0.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sandbox0

- `compute/sandbox0` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T13:21:03.998Z (live) | stale on 2026-12-25
- url https://sandbox0.ai/pricing
- free tier: one-time $5 usage credit for eligible new users after Stripe confirms a saved credit card; no one-hour compute minimum | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Network ingress is free and network egress is free for now (the page marks egress as temporary); no allowance in bytes and no overage price is published. | metered: no | source: [1]
- identity: card | detail: a saved credit card confirmed by Stripe is required for the one-time $5 welcome credit; a Sandbox0 account and an s0 CLI sign-in or team API key are the access path
- interface: rest, cli, ssh
- limits:
  - request-rate (binding): $5 of free credit for new users, one time [1]
  - per-object-cap: unlimited paused sandboxes per team; retained storage is billed [1]
- interface detail: HTTP API at /api/v1/sandboxes, open-source SDKs, the s0 CLI, and SSH to a sandbox
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The free credit is one-time; the durable facts are the absence of a one-hour minimum and the 2,000 paused-sandbox cap
- extras:
  - keep_rate: 0.0
  - keep_rate_basis: first-party: pply to Sandbox. The example uses a custom 2 vCPU / 6 GiB instance: Cloudflare requires at least 3 GiB per vCP
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no wall clock or idle reap published; ttl and hard_ttl default to 0, which disables them
  - persistent_storage.price_gib_month: billed by time and effective incremental data
  - persistent_storage.durability: paused sandboxes retain state
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: the 2,000-paused-sandbox cap bounds how many, not how long
  - free_tier_kind: one-time-credit
  - granularity.min_billed_s: 0
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$5 free credit for new users. No credit card required.' and 'No one-hour compute minimum. Paused sandboxes incur storage charges only. Keep up to 2,000 paused sandboxes per team by default', quoted
  - [2] 2026-11-03: REST API, SDKs and the s0 CLI exist | capture: sha256:dce8fcae7e9c06df67d1f1b0c990713f58d58225cb25945903faacfc165d74a1 | quote: Use the APIs, open-source SDKs, templates, and s0 CLI to build on a managed runtime with persistent workspaces and on-demand compute.
  - [3] 2026-11-03: SSH is an access path to a sandbox | capture: sha256:e39a37162efd3a0a89d0997afea489b06ca4342ee5a10bdf646fe1bc12709a7b | quote: Auto-resume on supported runtime API, SSH, and service access paths (default: true).
  - [3] 2026-11-18:  | capture: sha256:90cf4de59eb5635340b768a7c3dbcf53f930c6037bc5d562c33aeeb5f3d1397c | quote: | `hard_ttl` | integer | Hard sandbox lifetime in seconds (deletes identity and durable state; default: `0`, disabled) |
  - [1] 2026-11-24: the welcome credit is one-time and requires a saved credit card | capture: sha256:cea331f5489b9406879e75fd143528be69be9c40435bcd116006b1a1e5d89a72 | quote: Yes. Eligible new users receive a one-time $5 usage credit after Stripe confirms a saved credit card. Each user and team can receive the welcome credit once.
  - [1] 2026-11-24: a saved credit card is a gate for the welcome credit | capture: sha256:cea331f5489b9406879e75fd143528be69be9c40435bcd116006b1a1e5d89a72 | quote: Yes. Eligible new users receive a one-time $5 usage credit after Stripe confirms a saved credit card. Each user and team can receive the welcome credit once.
  - [1] 2026-11-24: the card gate for the welcome credit | capture: sha256:cea331f5489b9406879e75fd143528be69be9c40435bcd116006b1a1e5d89a72 | quote: Yes. Eligible new users receive a one-time $5 usage credit after Stripe confirms a saved credit card.
  - [1] 2026-11-24: the paused-sandbox cap was removed | capture: sha256:cea331f5489b9406879e75fd143528be69be9c40435bcd116006b1a1e5d89a72 | quote: No one-hour compute minimum. Paused sandboxes incur storage charges only. Keep unlimited paused sandboxes per team; retained storage is billed.
  - [1] 2026-11-24: egress remains free for now with no allowance or per-request meter | capture: sha256:cea331f5489b9406879e75fd143528be69be9c40435bcd116006b1a1e5d89a72 | quote: Ingress is free, egress is temporarily free, and object-store GET and PUT requests have no per-request charge.
  - [1] 2026-11-24: the current free egress terms | capture: sha256:cea331f5489b9406879e75fd143528be69be9c40435bcd116006b1a1e5d89a72 | quote: Ingress is free, egress is temporarily free, and object-store GET and PUT requests have no per-request charge.
  - [1] 2026-11-24: the API request-rate ceiling and burst | capture: sha256:cea331f5489b9406879e75fd143528be69be9c40435bcd116006b1a1e5d89a72 | quote: | | API requests | 100per second | Per team | Burst up to 200 requests. |
- sources:
  - [1] https://sandbox0.ai/pricing
  - [2] https://sandbox0.ai
  - [3] https://sandbox0.ai/docs
