# Mastra

> mastra.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mastra/ | JSON https://fshy.ajam.dev/api/v1/entity/mastra.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mastra

- `compute/mastra` | qualifies-with-caveat | evidence documented | binding volume-quota | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-24T13:20:56.538Z (live) | stale on 2026-12-25
- url https://mastra.ai
- free tier: Mastra Platform Free, USD 0 a month: 40 vCPU-hours, 360 GB-hours of memory, 100K observability events, 10 GB shared egress, 5 connections and 15-day trace retention; then USD 0.25 per vCPU-hour, USD 0.25 per GB-hour and USD 10 per 100K events. Starter is USD 25 a month. The open-source framework is free to self-host | unit: mixed | metered on: wall-clock | read on: 2026-10-29 | source: [1] | note: read from the vendor pricing page; the plan is priced a month, and whether the allowance resets monthly is not stated
- per-object cap: not stated | source: [2]
- retention: not stated | source: [2]
- egress: Shared egress allowance per workspace: Free 10 GB, Starter 25 GB, Team 50 GB, then USD 0.10 per GB; each dedicated project uses its own egress first | metered: yes | free allowance: 10 GB (Free plan) | price per TB: USD 100 per TB | source: [2]
- identity: email
- interface: cli
- limits:
  - volume-quota (binding): the hosted Free plan includes 40 vCPU-hours, 360 GB-hours of memory and 100K events; usage past them is billed at USD 0.25 per vCPU-hour, USD 0.25 per GB-hour and USD 10 per 100K events [1]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: the mastra CLI starts a local server exposing REST endpoints and Studio; the hosted platform is managed in the Mastra console at projects.mastra.ai
- tooling: the mastra CLI with mastra deploy to the hosted platform
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-29: the hosted Mastra Platform has a Starter plan at $0 a month with 100K events and 24 CPU hours, above Teams at $250 a month. The site read on 2026-10-22 described only the open-source framework
- self hosted: no
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the harness manages sessions inside a user's own deployment
  - persistent_storage.price: a user's own storage
  - persistent_storage.durability: thread storage in a user's database
  - persistent_storage.on_stop: yes
  - persistent_storage.on_destroy: no
  - persistent_storage.max_retention: as long as a user keeps it
  - free_tier_kind: none
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: the site was read on 2026-10-22 and describes an open-source TypeScript agent framework with workflows, memory and a harness; it publishes no plan, price or free tier
  - [3] 2026-11-03: the mastra CLI deploys to the hosted platform | capture: sha256:ed35f882359bbafecac74947b56b1cf0f171b0d728d6192abf362fb8808a8f66 | quote: Builds and deploys your project to the Mastra platform environment selected by `--env`.
  - [1] 2026-11-24: the Free plan includes 40 vCPU-hours then USD 0.25 per vCPU-hour; Starter is a separate USD 25 plan | capture: sha256:5ef1bd76b247fd9e47942abad2885dc1f345034a6c704b1312d8c967cc50075f | quote: Compute | vCPU | 40 vCPU-hours, then $0.25 / vCPU-hour | 100 vCPU-hours, then $0.25 / vCPU-hour | 400 vCPU-hours, then $0.25 / vCPU-hour | Custom
  - [1] 2026-11-24: the Free allowance is denominated in both vCPU-hours and GB-hours, so the nearest unit term is mixed | capture: sha256:5ef1bd76b247fd9e47942abad2885dc1f345034a6c704b1312d8c967cc50075f | quote: Compute | Memory | 360 GB-hours, then $0.25 / GB-hour | 720 GB-hours, then $0.25 / GB-hour | 3.6K GB-hours, then $0.25 / GB-hour | Custom
  - [1] 2026-11-24: the egress allowance is 10 GB on Free, 25 GB on Starter and 50 GB on Team, at USD 0.10 per GB overage | capture: sha256:5ef1bd76b247fd9e47942abad2885dc1f345034a6c704b1312d8c967cc50075f | quote: Data | Egress | 10 GB, then $0.10 / GB | 25 GB, then $0.10 / GB | 50 GB, then $0.10 / GB | Custom
  - [1] 2026-11-24: the 10 GB egress allowance belongs to the Free plan, not to Starter | capture: sha256:5ef1bd76b247fd9e47942abad2885dc1f345034a6c704b1312d8c967cc50075f | quote: Data | Egress | 10 GB, then $0.10 / GB | 25 GB, then $0.10 / GB | 50 GB, then $0.10 / GB | Custom
  - [1] 2026-11-24: the Free plan's compute allowance and overage rate are written in the pricing table | capture: sha256:5ef1bd76b247fd9e47942abad2885dc1f345034a6c704b1312d8c967cc50075f | quote: Compute | vCPU | 40 vCPU-hours, then $0.25 / vCPU-hour | 100 vCPU-hours, then $0.25 / vCPU-hour | 400 vCPU-hours, then $0.25 / vCPU-hour | Custom
  - [1] 2026-11-24: the hosted platform's management interface is a web console | capture: sha256:5ef1bd76b247fd9e47942abad2885dc1f345034a6c704b1312d8c967cc50075f | quote: Start on the Free plan in the [Mastra console](https://projects.mastra.ai).
  - [4] 2026-11-24: a full name field is shown on the signup page | capture: sha256:50bc2fd7199ca365b970cc02c3bc89ef33253484f1364197ef54ffc1e97613a4 | quote: Full name
  - [1] 2026-11-24: the current plans table starts with a Free plan at USD 0 a month | capture: sha256:5ef1bd76b247fd9e47942abad2885dc1f345034a6c704b1312d8c967cc50075f | quote: Free | $0 / month | Build and test your first agents.
  - [3] 2026-11-24: the current CLI docs describe a REST-exposing local server; the old deploy-only quote is no longer on that page | capture: sha256:6e3b98474a2caf8c31f7ec443a21dc1356817d70c66f689b4e9dc5357493c34a | quote: Starts a server which exposes [Studio](https://mastra.ai/docs/studio/overview) and REST endpoints for your agents, tools, and workflows.
- sources:
  - [1] https://mastra.ai/pricing
  - [2] https://mastra.ai
  - [3] https://mastra.ai/reference/cli/mastra
  - [4] https://miosa.ai/register
