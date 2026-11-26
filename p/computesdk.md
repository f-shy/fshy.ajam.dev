# Sandbox Router

> computesdk.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/computesdk/ | JSON https://fshy.ajam.dev/api/v1/entity/computesdk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sandbox Router

- `compute/sandbox-router` | qualifies-with-caveat | evidence documented | binding volume-quota | category sandbox (hosted router over multiple sandbox providers) | tier Pay as you go, USD 5 free credit
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.793Z (live) | stale on 2026-12-26
- url https://www.computesdk.com/sandbox-router
- free tier: USD 5 in free compute credit to start, with no provider account needed; credit is spent at the listed per-provider compute rates and a 5% platform fee applies when buying more credit | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: the free credit is USD 5 and the bill is drawn from the organization's ComputeSDK balance at the provider's rate; the router does not set a single price of its own, the per-provider table does
- per-object cap: not applicable: the unit is a sandbox session, not a stored object
- retention: a sandbox keeps running until the user destroys it or its lifetime expires; closing the terminal or disconnecting a preview does not destroy it, and sandbox and Actions rates may differ | source: [2]
- egress: no egress price is published on the read pages; a quote through the routing endpoint reports the provider, region and prepaid credit balance before a sandbox is created | metered: no | source: [1]
- identity: email | detail: the signup page asks for a name, an organization, an email address and a password, and offers Continue with Google or Continue with GitHub; the CLI browser login opens the same flow and saves the session locally. The free credit needs no provider account and no payment method is shown before credit is used.
- interface: rest, cli, chat
- limits:
  - volume-quota (binding): USD 5 free compute credit at signup, then credits bought with a 5% platform fee, spent at per-provider hourly rates [1]
  - request-rate: a sandbox runs until destroyed or its lifetime expires; the rate table lists per-hour prices and billing increments where the provider publishes them [3]
- limits note: Rates in the table are normalized to USD per hour for comparison; each row lists a billing increment when available, and most rows read 'Not specified'. A quote does not reserve capacity, and being listed in the catalog or benchmarks does not grant access to a provider account.
- binding note: the USD 5 credit is what a new user spends first; there is no router-wide concurrency or request ceiling on the read pages, and the per-provider rates determine how long the credit lasts
- interface detail: a REST API at https://platform.computesdk.com/api/v1 with an organization API key or OAuth token, a TypeScript SDK that includes the router, the compute CLI, and a remote MCP server
- endpoint: part of interface detail
- tooling: npm install computesdk for the SDK, npm install @computesdk/cli or curl -fsSL https://computesdk.com/install | sh for the CLI, an org API key from Settings, or the remote MCP server with OAuth
- composes with: one integration routes across many sandbox providers, with a fallback order and a choice of provider per run; managed compute spends ComputeSDK credit with no provider account, while BYOK lets a provider bill its own usage directly
- reliability: the platform does not charge the 5% fee again on each usage charge; the displayed rate is normalized per hour for comparison and the billing increment is listed separately where the provider publishes one, so short-lived sandboxes can cost a different effective rate
- notes: A hosted router over many sandbox providers rather than a single sandbox vendor: USD 5 of free compute credit at signup, a 5% fee only when buying more credit, and per-provider rates charged from the organization's balance. The per-provider table lists a 2 vCPU and 4 GB sandbox from USD 0.00604 per hour (agent37) to USD 0.3408 per hour (vercel medium); the operator list's USD 0.31 per hour for 'Sandbox Router' is not a router-wide rate on any page read, so the record states the published per-provider rates instead. The self-hosted SDK libraries are optional clients of this hosted service and come after it, not in its place.
- evidence note: the free credit, fee, rate table and signup fields are quoted from first-party pages read on 2026-11-25; the signup and console are behind a login wall, so the signup fields were read from a direct fetch of the public signup page, and no sandbox was created
- extras:
  - shape.note: the router offers many provider sizes; the per-provider rate table is the source of shape and price
  - billing_model: prepaid credits spent at per-provider rates, 5% fee on credit purchases
  - free_tier_kind: one-time credit
  - term: on demand; a sandbox runs until destroyed or its lifetime expires
  - price_arithmetic: USD 5 free credit; 5% fee on purchases; example 2 vCPU / 4 GB rates in the published table are USD 0.00604/h (agent37) and USD 0.3408/h (vercel medium)
  - network_out.allow_outbound: yes
  - session_cap.restart_required: no
  - session_cap.note: lifetime is set per sandbox; billing increment is listed per provider where available
- evidence:
  - [1] 2026-11-25: the router starts with USD 5 in free credit and charges a 5% fee only when credits are bought | capture: sha256:db6acf79818dc9d11a95337e3c4115b0e6d5af92a5079ac79309459cb9208d0f | quote: Pay for compute as you go. Start with $5 in free credit. A 5% platform fee applies when you buy credits.
  - [4] 2026-11-25: the Sandbox Router runs code and agents in isolated sandboxes with a routed or chosen provider | capture: sha256:18fe3a1b76398bc4450439730cb07f897d7d6e6df62f122f2874e23706473e8b | quote: Run code and agents in isolated sandboxes. Let us route, or choose a provider.
  - [3] 2026-11-25: the router is an available hosted product billed at provider rates from credits or from the user's own keys | capture: sha256:3a8884cef2c670c4bfa7c353ffef2eb59432b0cdd81dc37cba552d869305c525 | quote: - Pricing: Compute at the listed rates, paid from credits (5% platform fee on credit purchases), or billed by the provider with your own keys.
  - [3] 2026-11-25: the USD 5 free credit needs no provider account | capture: sha256:3a8884cef2c670c4bfa7c353ffef2eb59432b0cdd81dc37cba552d869305c525 | quote: Free credit: $5 in free compute credit to start; no provider account needed.
  - [3] 2026-11-25: the rate table is published per provider and normalized to USD per hour before the platform fee | capture: sha256:3a8884cef2c670c4bfa7c353ffef2eb59432b0cdd81dc37cba552d869305c525 | quote: Rates as published on https://www.computesdk.com/pricing (updated 2026-11-21T03:05:16.260Z), normalized to USD per hour, before the platform fee.
  - [5] 2026-11-25: the signup form asks for an email address | capture: sha256:ef4f65749ef34e40e434dd7bc9ed0adaa15a7df5e1513013ca7f38444ecb4f32 | quote: for="email">Email</label>
  - [5] 2026-11-25: the signup form asks for a password | capture: sha256:ef4f65749ef34e40e434dd7bc9ed0adaa15a7df5e1513013ca7f38444ecb4f32 | quote: for="password">Password</label>
  - [5] 2026-11-25: the signup form also offers Google social login | capture: sha256:ef4f65749ef34e40e434dd7bc9ed0adaa15a7df5e1513013ca7f38444ecb4f32 | quote: Continue with Google
  - [6] 2026-11-25: hosted sandboxes and keys belong to an organization created at the console | capture: sha256:66f7188131594616bb2d1ad945a0129836e88b61cbd0e941a0b18d9348695fa9 | quote: Every hosted sandbox, provider credential, API key and Actions run belongs to an organization.
  - [2] 2026-11-25: managed compute draws from the organization's credits with no provider account, and a sandbox runs until destroyed or its lifetime expires | capture: sha256:9a8adca49aa80eddbe074624ad77a00e4811f13325d36b1c75650b4f0a0a66b7 | quote: Start with $5 in free compute credit. Managed compute uses your organization's ComputeSDK credits; you do not need a provider account.
  - [3] 2026-11-24: the free credit is USD 5, one-time, and no provider account is needed | capture: sha256:1d3c8a637d90c1451993b0bb0809ae1a5c2158ed5fb7702a5232dc00b0e71b55 | quote: Free credit: $5 in free compute credit to start; no provider account needed.
  - [3] 2026-11-24: the platform fee is 5% on credit purchases and is not charged on each sandbox run | capture: sha256:1d3c8a637d90c1451993b0bb0809ae1a5c2158ed5fb7702a5232dc00b0e71b55 | quote: Platform fee: 5% on credit purchases. It is not charged again on each sandbox or workflow run.
  - [3] 2026-11-24: the lowest published sandbox rate is USD 0.03 an hour on sandbox0 small | capture: sha256:1d3c8a637d90c1451993b0bb0809ae1a5c2158ed5fb7702a5232dc00b0e71b55 | quote: | sandbox0 | small | 1 vCPU · 2 GB | sandbox | $0.03 | Not specified |
  - [3] 2026-11-24: the highest published sandbox rate is USD 5.4528 an hour on vercel 3xlarge | capture: sha256:1d3c8a637d90c1451993b0bb0809ae1a5c2158ed5fb7702a5232dc00b0e71b55 | quote: | vercel | 3xlarge | 32 vCPU · 64 GB · 64 GB disk | sandbox | $5.4528 | Not specified |
  - [3] 2026-11-24: the API rate limit is 240 requests per minute per connection | capture: sha256:1d3c8a637d90c1451993b0bb0809ae1a5c2158ed5fb7702a5232dc00b0e71b55 | quote: Rate limit: 240 requests per minute per connection. Past that, the server returns HTTP `429` with `{"error":"rate_limited"}`; wait and retry.
  - [3] 2026-11-24: sandboxes expire after 30 minutes by default and bill until destroyed or expired | capture: sha256:1d3c8a637d90c1451993b0bb0809ae1a5c2158ed5fb7702a5232dc00b0e71b55 | quote: Billing: sandboxes on managed accounts bill your org's prepaid credit while they run; sandboxes on your own provider keys are billed by that provider. Sandboxes expire on their own (30 minutes by default); destroying them sooner stops billing.
  - [3] 2026-11-24: code in a sandbox reaches the internet and a hosted port can be made public | capture: sha256:1d3c8a637d90c1451993b0bb0809ae1a5c2158ed5fb7702a5232dc00b0e71b55 | quote: Tool calls carry only what the assistant sends for that action, such as a command, a file, or a run id. Sandboxes run on third-party compute providers, and code running in a sandbox can reach the internet.
  - [3] 2026-11-24: the REST base URL, SDK, CLI and MCP endpoint are published | capture: sha256:1d3c8a637d90c1451993b0bb0809ae1a5c2158ed5fb7702a5232dc00b0e71b55 | quote: REST API: base URL `https://platform.computesdk.com/api/v1`. Send `Authorization: Bearer <org API key>` (minted in the console) or an OAuth 2.0 access token.
  - [7] 2026-11-24: every hosted sandbox and API key belongs to an organization and browser login opens a browser | capture: sha256:66f7188131594616bb2d1ad945a0129836e88b61cbd0e941a0b18d9348695fa9 | quote: Every hosted sandbox, provider credential, API key and Actions run belongs to an organization. Start at [platform.computesdk.com](https://platform.computesdk.com). Owners and admins manage keys and provider credentials in Settings.
  - [5] 2026-11-24: the sign-up form shows a workspace address, a password of at least 8 characters and a Terms acceptance | capture: sha256:aa5990e5e14b4ea9d3a7b1c26a19897becc6dc0b0020bc54132bf936ff19754a | quote: Its address: /your-name (numbered if taken). You can rename it later.
  - [8] 2026-11-24: the terms state no uptime commitment | capture: sha256:81abd443185cb56df3c3b37beed349cc0fbde38d90d6970054f92dfdba3d43f7 | quote: SLA: None.
- sources:
  - [1] https://www.computesdk.com/pricing
  - [2] https://docs.computesdk.com/platform/billing
  - [3] https://www.computesdk.com/llms-full.txt
  - [4] https://www.computesdk.com/sandbox-router
  - [5] https://platform.computesdk.com/signup
  - [6] https://docs.computesdk.com/platform/authentication
  - [7] https://docs.computesdk.com/platform/authentication.md
  - [8] https://www.computesdk.com/terms
