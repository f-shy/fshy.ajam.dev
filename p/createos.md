# CreateOS Sandbox

> createos.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/createos/ | JSON https://fshy.ajam.dev/api/v1/entity/createos.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CreateOS Sandbox (NodeOps)

- `compute/createos` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-09T13:26:53.816Z (live) | stale on 2026-12-10
- url https://createos.sh/products/sandbox
- free tier: 500 free credits to start; a sandbox auto-pauses after 5 minutes idle with memory and disk preserved and compute billing stopped | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: egress is unmetered at $0 at any volume; outbound traffic is firewalled to an allowlist and there is no ingress by default | metered: no | free allowance: unlimited | price per TB: $0 | source: [1]
- identity: email | detail: email: the account documentation offers passwordless one-time codes by email, one-click Google sign-in and GitHub login ('Use passwordless OTP via email or one-click Google authentication for rapid entry.'), and names no phone and no identity document. The vendor's pricing page states the Free tier needs no card ('Start today, no credit card required.'). Whether the sign-up form asks for anything else is unverified.
- interface: rest, cli
- limits:
  - request-rate (binding): 500 free credits at signup [1]
  - retention-clamped: auto-pause after 5 minutes idle; memory and disk are snapshotted rather than lost [1]
- interface detail: REST API, CLI, a TypeScript SDK and MCP; no Python SDK
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the sandbox page was read on 2026-10-22. The 500-credit grant is one-time; the 5-minute auto-pause is the wall-clock axis and it preserves state, which is the unusual half
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: first-party: PAUSED sandboxes stop vCPU billing but KEEP billing RAM at $0.01159025/GB-h
  - billing_model: unclassified
  - session_cap.idle_reap_s: 300
  - session_cap.restart_required: no
  - session_cap.note: auto-pause after 300 idle seconds, as the page's own example sets auto_pause_after_seconds: the sandbox is checkpointed to a Firecracker snapshot, vCPU billing stops while memory and disk keep billing, and a resume restores the exact state. No maximum session lifetime is published
  - persistent_storage.price_gib_month: not published on this page
  - persistent_storage.durability: Firecracker snapshot on disk
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: until deleted
  - free_tier_kind: one-time-credit
  - granularity.min_billed_s: 0
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '500 free credits to start.' and 'Idle 5 min → paused, disk + memory preserved' with 'A paused sandbox is a Firecracker snapshot on disk: guest memory and device state are frozen, and compute billing stops', quoted
  - [1] 2026-11-04: SDK, CLI, MCP and REST API | capture: sha256:771920ef867e86ee0ae168d9e61c0e342467ca3822ac771b318eef5be94bd317 | quote: A TypeScript SDK, the CLI, MCP, or the REST API from any language, so an agent can provision its own compute through a tool call.
  - [1] 2026-11-04: egress is not charged | capture: sha256:771920ef867e86ee0ae168d9e61c0e342467ca3822ac771b318eef5be94bd317 | quote: Networking is unmetered, so egress is $0.
  - [2] 2026-11-04: the login methods are an emailed one-time code, Google or GitHub, so an email address is the identity | capture: sha256:e88d0ed4625d5ecfa237fb341f8c5415f6f5f6a9de16afa8743bd70abfa240cc | quote: Use passwordless OTP via email or one-click Google authentication for rapid entry.
  - [2] 2026-11-04: a GitHub account is the second accepted login | capture: sha256:e88d0ed4625d5ecfa237fb341f8c5415f6f5f6a9de16afa8743bd70abfa240cc | quote: GitHub Login The preferred method for developers, automatically preparing your identity for automated deployment flows.
  - [3] 2026-11-04: the Free tier is available at sign-up with no card, so the free credits are not behind a card | capture: sha256:c6c64c3fbb7e0feeb72b41218b96b7b0361dc2add88390742752b77369132968 | quote: Designed for every stage of your journey. Start today, no credit card required.
  - [1] 2026-11-09: the sandbox API takes an auto_pause_after_seconds of 300, so idling for five minutes pauses the sandbox | capture: sha256:771920ef867e86ee0ae168d9e61c0e342467ca3822ac771b318eef5be94bd317 | quote: // Idle 5 min → paused, disk + memory preserved. auto_pause_after_seconds: 300,
  - [1] 2026-11-09: the idle pause interval and the snapshot behaviour are both on the page | capture: sha256:771920ef867e86ee0ae168d9e61c0e342467ca3822ac771b318eef5be94bd317 | quote: // Idle 5 min → paused, disk + memory preserved. auto_pause_after_seconds: 300,
  - [1] 2026-11-09: the pause is a snapshot that stops vCPU billing and keeps memory and disk billed, and the example sets the idle interval to 300 seconds | capture: sha256:771920ef867e86ee0ae168d9e61c0e342467ca3822ac771b318eef5be94bd317 | quote: "A paused sandbox is a Firecracker snapshot on disk: guest memory and device state are frozen, and vCPU billing stops while memory and disk are still billed."
  - [1] 2026-11-09: the idle pause interval is 300 seconds | capture: sha256:771920ef867e86ee0ae168d9e61c0e342467ca3822ac771b318eef5be94bd317 | quote: // Idle 5 min → paused, disk + memory preserved. auto_pause_after_seconds: 300,
- sources:
  - [1] https://createos.sh/products/sandbox
  - [2] https://createos.sh/docs/Account-Billing/Account-Management
  - [3] https://nodeops.network/createos/pricing
