# inis.run

> inis.run | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inis/ | JSON https://fshy.ajam.dev/api/v1/entity/inis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## inis.run

- `compute/inis-run` | trial-only | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:07.841Z (live) | stale on 2026-12-05
- url https://inis.run/pricing
- free tier: New accounts get EUR 1.00 in credit, no card required, and prepaid credit does not expire. Three fixed sizes metered by the millisecond while a session runs: small 1 vCPU / 1 GB at EUR 0.0144 per hour, medium 2 vCPU / 4 GB at EUR 0.036 per hour, large 4 vCPU / 8 GB at EUR 0.072 per hour. A paused session is billed storage only, about EUR 0.07 per GB per month. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: The continuous-live backstop force-pauses any session after 24 hours live, and after 6 hours on an unverified trial account; a session paused by its own max_lifetime_ms can never be resumed (HTTP 410). | source: [1]
- egress: Outbound access is open to the public internet by default, with an optional per-session domain allowlist; no egress allowance or overage price is published on the pricing or networking pages. | metered: no | source: [1]
- identity: email | detail: no card and no payment method: the pricing page states EUR 1.00 of starting credit with no card required, and prepaid credit does not expire, so no hold exists. The account does begin as an 'unverified trial' with tighter caps (1 live session, 5 GB disk, 6-hour continuous-live backstop), so a verification step exists, but what it asks for is not stated in the evidence
- interface: rest, cli
- limits:
  - retention-clamped (binding): The continuous-live backstop force-pauses any session after 24 hours live, and after 6 hours on an unverified trial account; a session paused by its own max_lifetime_ms can never be resumed (HTTP 410). [1]
- limits note: The continuous-live backstop force-pauses any session after 24 hours live, and after 6 hours on an unverified trial account; a session paused by its own max_lifetime_ms can never be resumed (HTTP 410).
- binding note: the same as limits note
- interface detail: REST API at https://api.inis.run (versioned under /v1, bearer authentication) and the inis CLI, whose inis ssh command opens an interactive shell
- tooling: the inis command-line tool, installed with the inis.run install script (static binary); it wraps the HTTP API and needs no SDK
- composes with: Prepaid credit that never expires plus millisecond billing makes this the cheapest place to park a long-lived 1 vCPU agent that idles; the paused tier (hot, warm, cold) is what lets it wake in tens of milliseconds without paying for the wait.
- reliability: no reliability event recorded
- notes: Considered as floor candidate. EUR 0.036 per hour for 2 vCPU / 4 GiB is EUR 26.28 for 730 hours, a full month of a 2 vCPU machine, and it undercuts every provider on the boat.dev and boxyard comparison tables except the ones that bill active CPU only. The unverified-trial limits (1 live session, 5 GB disk, 6 hour backstop) are the part a new account actually meets. Isolation technology was not read. GPU: none, every size is CPU only.
- extras:
  - facets.class: prepaid-sandbox
  - facets.free_tier_kind: one-time-credit
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
- evidence:
  - [1] 2026-10-22: EUR 0.0144/hr small 1 vCPU 1 GB, EUR 0.036/hr medium 2 vCPU 4 GB, EUR 0.072/hr large 4 vCPU 8 GB, millisecond metering, EUR 1 free credit, no card required, credit does not expire, paused storage about EUR 0.07 per GB per month
  - [2] 2026-10-22: defaults and hard caps on the managed cloud: no default idle timeout, max_lifetime_ms hard cap 24 hours, always-on 24 hour continuous-live backstop (6 hours on a new unverified trial), paused_ttl 30 days, one exec 30 s default and 1 hour cap, 10 concurrent live sessions (1 on trial), 50 GB cumulative disk (5 GB on trial)
  - [2] 2026-10-22: a session paused by its own max_lifetime_ms firing cannot wake again; resume is refused with 410
  - [1] 2026-10-22: 
  - [3] 2026-11-03: default egress is open; no allowance or price stated | capture: sha256:fc17e60928561fc4d4b99e4d6fd6df7a4ca29a8a08bf80a924c848ef830a7624 | quote: By default a session has full public outbound network access.
  - [4] 2026-11-03: the CLI provides an SSH-style shell | capture: sha256:05762abf44b7bc441b2cac9cec75ed64ee5a506a11e7f952a93db01436a886c5 | quote: `inis ssh` attaches a raw interactive shell to a session
  - [5] 2026-11-03: a REST API exists | capture: sha256:32a54b24b8b7e6bd8c7f4895a409039c0511cac8a9e645f4999ac1d264562d05 | quote: REST API for sandbox execution and session management.
  - [3] 2026-11-03: default egress is open | capture: sha256:fc17e60928561fc4d4b99e4d6fd6df7a4ca29a8a08bf80a924c848ef830a7624 | quote: By default a session has full public outbound network access.
  - [4] 2026-11-04: the CLI, including its inis ssh subcommand, is a wrapper over the HTTP API; no SSH protocol endpoint is documented | capture: sha256:05762abf44b7bc441b2cac9cec75ed64ee5a506a11e7f952a93db01436a886c5 | quote: The `inis` CLI is the fastest way to run sandboxes from a terminal or CI pipeline. It wraps the HTTP API — no SDK required.
  - [5] 2026-11-04: the REST API is documented | capture: sha256:32a54b24b8b7e6bd8c7f4895a409039c0511cac8a9e645f4999ac1d264562d05 | quote: REST API for sandbox execution and session management.
  - [4] 2026-11-04: the documented client is the inis CLI | capture: sha256:05762abf44b7bc441b2cac9cec75ed64ee5a506a11e7f952a93db01436a886c5 | quote: The `inis` CLI is the fastest way to run sandboxes from a terminal or CI pipeline. It wraps the HTTP API — no SDK required.
- sources:
  - [1] https://inis.run/pricing
  - [2] https://inis.run/docs/session-lifecycle
  - [3] https://inis.run/docs/networking
  - [4] https://inis.run/docs/integrations/cli
  - [5] https://inis.run/docs/api/overview
