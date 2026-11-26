# Maritime

> maritime.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/maritime/ | JSON https://fshy.ajam.dev/api/v1/entity/maritime.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Maritime

- `compute/maritime` | qualifies-with-caveat | evidence documented | binding write-gated | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T13:20:56.540Z (live) | stale on 2026-12-25
- url https://maritime.sh/pricing
- free tier: new accounts get a 7-day free trial with up to USD 20 of usage on Starter terms; a card is required to start the first machine and is not charged if cancelled within the week. Plans start at USD 20 a month and each plan fee becomes that month's usage credit | unit: credits | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: no egress allowance or overage price is on the pricing page; the plan credit covers machine time and disk. Network policy allows all, an allowlist or no internet, with optional residential exits billed separately per GB | metered: no | source: [1]
- identity: card | detail: a card is needed to start the first machine and is not charged during the 7-day trial; the signup form also offers Continue with Google and Continue with GitHub alongside email and password. One free trial per card and per email
- interface: rest, cli
- limits:
  - write-gated (binding): the free offer is a 7-day trial capped at USD 20 of usage; at the cap machines stop until the paid plan starts and one free trial is allowed per card and per email [1]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: REST API and CLI, per maritime.sh/llms.txt: "one REST API" and "the maritime CLI"
- tooling: the provider documents TypeScript SDK (npm maritime-sdk), Python SDK (pip maritime) and the maritime CLI (npm maritime-cli), per maritime.sh/llms.txt
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-11-24 and states a 7-day free trial with up to USD 20 of usage on Starter terms, then plans from USD 20 a month
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.note: no wall clock published; an idle sandbox ends and its disk is deleted with no published interval
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [2] 2026-11-03: REST API and CLI exist | capture: sha256:15ede80b02234716172021235d9ed4ee95eb00eb7c66d30ad73a5255ea226df1 | quote: Interfaces: one REST API (bearer mk_ key), TypeScript SDK (npm maritime-sdk), Python SDK (pip maritime), the maritime CLI (npm maritime-cli), an MCP server for desktops and phones, and the dashboard.
  - [1] 2026-11-03: plan credit covers machine time and disk; no egress line | capture: sha256:4db5ed2e401eba55e14432fc58656cff99fa43cb4fc2cc98540857e0fe5ce135 | quote: The credit covers machine time and disk.
  - [2] 2026-11-04: the provider lists a REST API and the maritime CLI | capture: sha256:c6c087926fcf03c7e2def30d3be4513f5353ea46d5b12f52e238a68794ca49ab | quote: Interfaces: one REST API (bearer mk_ key), TypeScript SDK (npm maritime-sdk), Python SDK (pip maritime), the maritime CLI (npm maritime-cli), an MCP server (https://mcp.maritime.sh/mcp) for desktops, phones, sandboxes, swarms and agents, and the dashboard.
  - [2] 2026-11-04: the provider lists its SDKs and CLI | capture: sha256:c6c087926fcf03c7e2def30d3be4513f5353ea46d5b12f52e238a68794ca49ab | quote: Interfaces: one REST API (bearer mk_ key), TypeScript SDK (npm maritime-sdk), Python SDK (pip maritime), the maritime CLI (npm maritime-cli), an MCP server (https://mcp.maritime.sh/mcp) for desktops, phones, sandboxes, swarms and agents, and the dashboard.
  - [1] 2026-11-18:  | capture: sha256:05e5cbc8e1fd91fff119f46685aacdd5021174f53bbd48ffa1743e51462fe530 | quote: Sleeps when idle, wakes in about a second Unlimited awake hours / Asleep Only if you set it to pause when idle; by default an idle sandbox ends and its disk is deleted
  - [1] 2026-11-24: the free offer is a 7-day trial capped at USD 20, not an ongoing USD 0 plan | capture: sha256:c53c9666214b20c2372af0ee8c5b68315c0b409c918943e5e4faef3ed5f67b3b | quote: 7-day free trial, up to $20 of usage
  - [1] 2026-11-24: the trial allowance is denominated in USD of usage | capture: sha256:c53c9666214b20c2372af0ee8c5b68315c0b409c918943e5e4faef3ed5f67b3b | quote: 7-day free trial, up to $20 of usage
  - [1] 2026-11-24: the trial is limited to one per card and email and ends at USD 20 of usage | capture: sha256:c53c9666214b20c2372af0ee8c5b68315c0b409c918943e5e4faef3ed5f67b3b | quote: One free trial per card and per email.
  - [1] 2026-11-24: a card is required to start the first machine even during the free trial | capture: sha256:c53c9666214b20c2372af0ee8c5b68315c0b409c918943e5e4faef3ed5f67b3b | quote: Yes. A card is needed to start your first machine, and it is not charged then. The first 7 days are free, with up to $20 of usage on Starter terms.
  - [1] 2026-11-24: the card requirement applies before the first machine starts | capture: sha256:c53c9666214b20c2372af0ee8c5b68315c0b409c918943e5e4faef3ed5f67b3b | quote: Yes. A card is needed to start your first machine, and it is not charged then.
  - [1] 2026-11-24: the plan credit covers machine time and disk, with no egress line | capture: sha256:c53c9666214b20c2372af0ee8c5b68315c0b409c918943e5e4faef3ed5f67b3b | quote: The credit covers machine time and disk. Usage past the credit is billed at the same rates on the same invoice.
  - [2] 2026-11-24: the REST API, SDKs, CLI, MCP server and dashboard are published | capture: sha256:4203bb146acb42aba99ec565e9c7f0376e0b4e764fdc703f9ae1d4b434263858 | quote: Interfaces: one REST API (bearer mk_ key), TypeScript SDK (npm maritime-sdk), Python SDK (pip maritime), the maritime CLI (npm maritime-cli), an MCP server (https://mcp.maritime.sh/mcp) for desktops, phones, virtual machines, swarms and agents, and the dashboard.
- sources:
  - [1] https://maritime.sh/pricing
  - [2] https://maritime.sh/llms.txt
