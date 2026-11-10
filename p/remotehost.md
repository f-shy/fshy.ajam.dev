# RemoteHost

> remotehost.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/remotehost/ | JSON https://fshy.ajam.dev/api/v1/entity/remotehost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RemoteHost

- `compute/remotehost` | trial-only | evidence documented | binding volume-quota | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T02:24:16.350Z (live) | stale on 2026-12-05
- url https://docs.remotehost.ai/docs/pricing
- free tier: Starter is USD 20 per month and includes 610 machine-hours, 35 concurrent sandboxes rising to 1,200, and 24-hour sessions, self-serve with a 7-day free trial. A small machine (2 vCPU / 4 GB) counts 0.5 machine-hours per hour and a default machine (4 vCPU / 8 GB) counts 1, so the Starter allowance is 1,220 hours at 2 vCPU / 4 GB. Overage is USD 0.64 per standard machine-hour, metered by the second. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: rest, cli, ssh
- limits:
  - volume-quota (binding): The 610 machine-hour allowance is the binding term: a 4 vCPU / 8 GB sandbox running continuously needs 730 machine-hours a month and spends 120 hours of overage at USD 0.64, while a 2 vCPU / 4 GB box fits 24/7 inside the allowance. [1]
- limits note: The 610 machine-hour allowance is the binding term: a 4 vCPU / 8 GB sandbox running continuously needs 730 machine-hours a month and spends 120 hours of overage at USD 0.64, while a 2 vCPU / 4 GB box fits 24/7 inside the allowance.
- binding note: the same as limits note
- interface detail: REST API (OpenAPI), remote CLI, SSH via the RemoteHost gateway, TypeScript SDK @remotehost/sdk and a web console
- tooling: the `remote` CLI (alias `rh`), the TypeScript SDK `@remotehost/sdk`, and the REST API
- composes with: At 0.5 machine-hours per hour for a 2 vCPU / 4 GB box, USD 20 a month covers 1,220 hours, which is a 24/7 sandbox plus 490 spare hours for a second box part-time; that turns a per-hour sandbox into a fixed monthly cost, which is the shape a persistent agent service needs.
- reliability: no reliability event recorded
- notes: This is the cheapest way found to keep a 2 vCPU / 4 GB sandbox alive every hour of the month: USD 20 buys 1,220 machine-hours at the 0.5x multiplier against a 730-hour month. It is recorded as trial-only because the free lane is a 7-day trial and the plan itself needs a card at checkout. The 24-hour session cap on Starter is the term that matters for a long-running service, since a session has to be recreated daily. Disk is not priced separately on the page; the repo-large and long-running profiles carry 80 GB and 160 GB disks. Checkout requires acknowledging that usage is measured from allocated resource-time.
- extras:
  - facets.class: flat-monthly-sandbox
  - facets.free_tier_kind: trial
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
- evidence:
  - [1] 2026-10-22: Starter USD 20 per month, 610 included machine-hours, 35 concurrent sandboxes up to 1,200, 24 hour sessions, 7-day free trial, self-serve; overage USD 0.64 per standard machine-hour
  - [1] 2026-10-22: machine-time multipliers: small 2 vCPU / 4 GB is 0.5x, default 4 vCPU / 8 GB is 1x, large 8 vCPU / 16 GB is 2x, and sandboxes are metered by the second while running with billing stopping when one is stopped
  - [1] 2026-10-22: Max carries 72-hour sessions and custom base images; Business is USD 100 per seat per month with 200 machine-hours per seat and overage USD 4.712 per standard machine-hour
  - [2] 2026-11-03: the CLI opens SSH to a sandbox through a gateway | capture: sha256:1472e9d74124830f0c1f42fa78303bb01c90e35b08c5afec4688cb08d258b07f | quote: Hosted sandboxes route through the RemoteHost SSH gateway
  - [3] 2026-11-03: a TypeScript SDK exists | capture: sha256:cada2789f5a7ddfef695a11c33c49c9cbc704a211453025025e8dab1b90aad42 | quote: The official `@remotehost/sdk` package is the server-side TypeScript interface to RemoteHost.
  - [1] 2026-11-03: the pricing page names two costs, plan price and machine-hour overage; no egress allowance or egress price is listed | capture: sha256:bf50b2f1202829d408b67a853632e88f6976c4e8ca11a800818443f5628205c6 | quote: Remotehost has two costs: a plan's monthly price, and usage past the machine hours the plan includes.
  - [2] 2026-11-04: the documented CLI is remote, alias rh | capture: sha256:1472e9d74124830f0c1f42fa78303bb01c90e35b08c5afec4688cb08d258b07f | quote: The CLI is `remote`. `rh` is a shorter alias for the same binary
  - [3] 2026-11-04: the documented SDK is @remotehost/sdk | capture: sha256:cada2789f5a7ddfef695a11c33c49c9cbc704a211453025025e8dab1b90aad42 | quote: The official `@remotehost/sdk` package is the server-side TypeScript interface to RemoteHost.
- sources:
  - [1] https://docs.remotehost.ai/docs/pricing
  - [2] https://docs.remotehost.ai/docs/cli-reference
  - [3] https://docs.remotehost.ai/docs/sdk
