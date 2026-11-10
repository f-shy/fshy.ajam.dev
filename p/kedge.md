# Kedge

> kedge.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kedge/ | JSON https://fshy.ajam.dev/api/v1/entity/kedge.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kedge

- `compute/kedge` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:12.146Z (live) | stale on 2026-12-05
- url https://kedge.dev/docs/billing
- free tier: $5 of usage a month, recurring, consumed before paid credit; compute bills per second at $0.0205 a vCPU-hour on measured use, not on the configured limit | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: egress is metered at $0.01 / GiB; no byte allowance is published, and the account's $5 of monthly usage is consumed first | metered: yes | source: [1]
- identity: email
- interface: rest, cli, ssh
- limits:
  - request-rate (binding): $0.0205 a vCPU-hour measured on scheduled CPU time, and $5 a GiB-month of memory on resident pages [1]
  - per-object-cap: storage bills bytes written, not the logical volume size [1]
  - retention-clamped: a scaled-to-zero or idle-suspended app accrues only its stored-data cost [1]
- interface detail: REST API at https://kedge.dev/api (OpenAPI 3.1), the kedge CLI and SSH commands
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the billing page was read on 2026-10-22. The $5 recurs monthly, which makes it a tier rather than the one-time credit the record implied, and the page calls the rates estimates because the service is in public preview
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: `idle-suspend` pauses a machine and leaves it accruing storage only; scale-to-zero does the same
  - free_tier_kind: recurring-credit
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.price: $0.05 a GiB-month, billed on written bytes
  - ps.durability: volume
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: yes
  - net.allowance: $0.01 a GiB egress
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Every account includes $5 of monthly usage, consumed before paid credit.' with 'CPU $15 / vCPU-month ($0.0205 / vCPU-hour)', 'Memory $5 / GiB-month', and 'A scaled-to-zero app has no running CPU or memory usage, so it accrues only its stored-data cost.' quoted
  - [1] 2026-11-03: egress is metered at $0.01 per GiB | capture: sha256:fd7622a4df173cd579ec5ef541d1746ba48a78bbb2f0697b2fec28f3e0640708 | quote: | Egress | $0.01 / GiB |
  - [1] 2026-11-03: the free allowance is a dollar amount, not a byte volume | capture: sha256:fd7622a4df173cd579ec5ef541d1746ba48a78bbb2f0697b2fec28f3e0640708 | quote: Every account includes $5 of monthly usage, consumed before paid credit.
  - [2] 2026-11-03: a REST API and SSH commands exist | capture: sha256:757adab170c4e07542d59b20a897dd93288c1abb2ce9b4dd53479331c7886a0d | quote: The REST API backs the web console and SSH commands.
  - [2] 2026-11-03: a kedge CLI exists | capture: sha256:757adab170c4e07542d59b20a897dd93288c1abb2ce9b4dd53479331c7886a0d | quote: Mint a token with `kedge token`, then send it as a Bearer token:
  - [2] 2026-11-04: the service exposes a REST API and SSH commands, supporting interface rest and ssh | capture: sha256:757adab170c4e07542d59b20a897dd93288c1abb2ce9b4dd53479331c7886a0d | quote: The REST API backs the web console and SSH commands.
- sources:
  - [1] https://kedge.dev/docs/billing
  - [2] https://kedge.dev/docs/api
