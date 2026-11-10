# Declaw

> declaw.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/declaw/ | JSON https://fshy.ajam.dev/api/v1/entity/declaw.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Declaw

- `compute/declaw` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T15:51:59.407Z (live) | stale on 2026-12-05
- url https://docs.declaw.ai/platform/billing
- free tier: $100 of sandbox compute credit and a separate $200 of guardrails credit, both one-time and never refilled; compute meters every 30 seconds at $0.0504 a vCPU-hour | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the archived billing and plans pages state no traffic allowance or per-GB overage; the plans table caps egress connections per sandbox at 50 on Free and 200 on Pro | metered: no | source: [1]
- identity: email | detail: Email: a cloud account is created at declaw.ai or console.declaw.ai before an API key exists ('A Declaw Cloud account — sign up at declaw.ai to get an API key'), and the account record carries an email address. No card is needed for the free credits, and no phone or identity document is named.
- interface: rest, cli
- limits:
  - request-rate (binding): $0.0504 a vCPU-hour, $0.0162 a GB-hour of memory and $0.110 a GB-month of disk [1]
  - retention-clamped: metering ticks every 30 seconds and a delayed tick is capped at 90 seconds of billable time, so a stop is noticed within 90 seconds [1]
  - per-object-cap: the two grants are one-time: $100 for sandbox compute and $200 for guardrails, never refilled [1]
- interface detail: REST API with an X-API-Key header, the declaw CLI, and Python, TypeScript and Go SDKs (archived docs index of 2026-10-13)
- tooling: not stated
- composes with: not established
- reliability: unverified: docs.declaw.ai answered DNS status 3 (NXDOMAIN) on 2026-11-04 and declaw.ai has no address record, so the billing page is readable only in archived copies of 2026-05-26 and 2026-10-13
- evidence note: the billing page was read on 2026-10-22 and states both grants, the microdollar metering and the 30-second tick with its 90-second cap. The record carried only the $100; the $200 is a second wallet with its own meter
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 2
  - shape.ram: 4
  - shape.disk: 10
  - shape.note: the page's own worked example: 2 vCPU, 4 GB and 10 GB for an hour costs 100,800 + 64,800 + 1,526 microdollars
  - session_cap.restart_required: no
  - session_cap.note: metered every 30 seconds against provisioned resources; a lagging tick bills at most 90 seconds
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
  - ps.gib: 10
  - ps.price: $0.110 a GB-month of overlay disk
  - ps.durability: overlay disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$100 grant at account creation' for sandbox compute and '$200 grant at account creation' for guardrails scans, both 'Never refilled by deposits', metered every 30 seconds at '14.0 microdollars / vCPU / sec = $0.0504 / vCPU / hour', with the metering tick capping at 90 seconds of billable time, quoted
  - probe:docs.declaw.ai 2026-11-04: the documentation host docs.declaw.ai answered NXDOMAIN to a DNS query | capture: sha256:c8e7e6245efc53e60e33ad62c30308bf54d4a27ae1e6c4d8c336e7664954976f | quote: "Status":3
  - [2] 2026-11-04: a REST API exists | capture: sha256:3888ed81ba0d39f55f8fc300f0f686cb549e52e459e68496338802715076f379 | quote: [API Overview](https://docs.declaw.ai/api-reference/overview.md): Conventions, base URL, request/response format, and error handling for the Declaw REST API.
  - [2] 2026-11-04: a CLI exists | capture: sha256:3888ed81ba0d39f55f8fc300f0f686cb549e52e459e68496338802715076f379 | quote: [CLI](https://docs.declaw.ai/cli/overview.md): Install and configure the Declaw CLI to manage sandboxes, templates, volumes, vault secrets, and MCP servers from the command line.
  - [3] 2026-11-04: the plans table caps egress connections per sandbox and carries no traffic volume row | capture: sha256:c41f997b0f3ccc2fd57dfeefeb7b977010499abb91022331560e68ee141c892a | quote: | Max egress connections / sandbox | 50 | 200 | Custom |
  - [4] 2026-11-04: a Declaw account is a precondition of the API key, and it is created by signing up at the vendor site | capture: sha256:f0ea2b198883fd03817820120c7511b741565d356b53c51cb80550638ea3e8ee | quote: A Declaw Cloud account — sign up at declaw.ai to get an API key
  - [5] 2026-11-04: the managed cloud credits are granted without a card | capture: sha256:22984cb90fb6e2d1d28b04854d4f5a3476038737bab7ad1e6a9bead37204d9cc | quote: $300 in free credits — no credit card
  - [6] 2026-11-04: the account object carries an email address | capture: sha256:c0ce5c5a16bd6aff3f77e9bac88c547c3cb64f0ad67e4a80741a9824483f6437 | quote: Account email.
  - [7] 2026-11-04: sign-up happens on the console, and the API key is self-service from the dashboard | capture: sha256:036ca9a465fa99b32ba5ec15cf4d31f6c4958666858c44e701fd73e13cc3a968 | quote: Sign up at console.declaw.ai
- sources:
  - [1] https://docs.declaw.ai/platform/billing
  - [2] https://web.archive.org/web/2026/https://docs.declaw.ai/llms.txt
  - [3] https://web.archive.org/web/2026/https://docs.declaw.ai/platform/plans
  - [4] https://web.archive.org/web/2026/https://docs.declaw.ai/quickstart
  - [5] https://web.archive.org/web/2026/https://declaw.ai/
  - [6] https://web.archive.org/web/2026/https://docs.declaw.ai/platform/usage
  - [7] https://web.archive.org/web/2026/https://docs.declaw.ai/cli/overview
