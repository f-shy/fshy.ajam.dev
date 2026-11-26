# Nodion Sandboxes

> nodion.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nodion/ | JSON https://fshy.ajam.dev/api/v1/entity/nodion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nodion Sandboxes

- `compute/nodion-sandboxes` | qualifies-with-caveat | evidence documented | binding volume-quota | category container and VM sandbox | tier GP-G2-4GB sandbox package
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-25T02:12:34.630Z (live) | stale on 2026-12-26
- url https://www.nodion.com/en/ai-sandboxes/
- free tier: no standing free tier: a new account can earn up to EUR 15 in credit when signing up, and running time is capped by a package monthly price | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The EUR 15 sign-up credit is stated on the documentation index; the amount a given account earns is not stated there.
- per-object cap: not applicable: the unit is a microVM with a workspace disk, not an object; the GP-G2-4GB package carries 32 GB of workspace | source: [2] | note: The workspace sizes are stated per package, for example 32 GB on GP-G2-4GB.
- retention: a sandbox lives until the user deletes it; after 5 idle minutes it sleeps and only its workspace disk is billed; max_lifetime_sec sets automatic cleanup | source: [2]
- egress: not published for sandboxes on the page read: outbound internet over NAT in isolated mode, no access to the project private network unless overlay mode is opted in | metered: no | source: [2]
- identity: email | detail: the hosted sign-in page presents 'Log in or sign up' with a Google or GitHub provider button or an email and password; no phone number, ID document or card is shown at sign-in, and a card is not stated for the sign-up credit
- interface: rest, cli, browser
- limits:
  - volume-quota (binding): EUR 20,00 per month of running time at most on the GP-G2-4GB package (EUR 0,0278 per hour) [2]
  - retention-clamped: after 5 idle minutes the sandbox sleeps and only its workspace disk is billed; max_lifetime_sec sets automatic cleanup [2]
  - request-rate: a command over the API runs up to 15 minutes per call [2]
- limits note: Personal API keys can be limited to sandbox read, write or exec. Billing starts once the sandbox runs, and deleting it stops billing.
- binding note: The package's EUR 20,00 monthly ceiling on running time is the first hard cap; a sandbox that runs for the whole month cannot exceed it.
- interface detail: REST API at https://api.nodion.com, a hosted MCP server and a web terminal; the CLI page states sandboxes are not in the CLI yet
- endpoint: part of interface detail
- tooling: a personal API key (nodion_…) scoped to sandbox read, write or exec; REST, MCP and a dashboard web terminal; sandboxes are not in the CLI yet
- composes with: a hosted microVM for running untrusted agent code, with HTTPS previews and access to the same project's databases in overlay mode
- reliability: the sandbox sleeps after 5 idle minutes and is deleted only when the user deletes it or max_lifetime_sec elapses; no further reliability event is stated on the pages read
- notes: Not a standing free tier: the sign-up credit is up to EUR 15 and the package monthly price caps running time. The operator's list quotes USD 0.031 per hour at 2 vCPU and 4 GB, against the vendor's EUR 0,0278 per hour for the GP-G2-4GB package.
- evidence note: the sandbox page, the documentation index and the API page were read on 2026-11-25; the sign-in gate was read from the hosted app's own JavaScript bundle, and the pricing from the vendor's sandbox page
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 32
  - billing_model: per-second running time with a monthly running-time ceiling per package
  - session_cap.wall_clock_min: 15
  - session_cap.idle_reap_s: 300
  - session_cap.restart_required: no
  - session_cap.note: 15 minutes per API command call; 5 idle minutes before sleep; max_lifetime_sec can end a sandbox
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: HTTPS previews per port, token-gated or public
  - free_tier_kind: sign-up credit
  - term: per-second, capped at a package monthly running-time price
  - source_scope: the GP-G2-4GB package is priced here; the list rate is for a 2 vCPU / 4 GB machine
- evidence:
  - [2] 2026-11-25: the GP-G2-4GB sandbox package is EUR 0,0278 per hour with a EUR 20,00 monthly running-time ceiling and 2 vCPU, 4 GB RAM, 32 GB workspace | capture: sha256:e9db0e5818bf67a3fb56b8506786f099e0c9bb5e21d6b769c38be09f96f55a15 | quote: 20,00 € per month of running time at most. 2 vCPU, 4 GB RAM, 32 GB workspace
  - [2] 2026-11-25: the sandbox sleeps after 5 idle minutes and only its disk is billed | capture: sha256:e9db0e5818bf67a3fb56b8506786f099e0c9bb5e21d6b769c38be09f96f55a15 | quote: After 5 idle minutes the sandbox goes to sleep. Only its disk is billed.
  - [2] 2026-11-25: API commands run up to 15 minutes per call | capture: sha256:e9db0e5818bf67a3fb56b8506786f099e0c9bb5e21d6b769c38be09f96f55a15 | quote: Run any command over the API and get its output and exit code, up to 15 minutes per call.
  - [1] 2026-11-25: a new account can earn up to EUR 15 in credit at sign-up | capture: sha256:c3363f50a5c102fb9860a643e219fcf405b2f96e20773b486b436d8934275d6f | quote: New accounts can earn up to 15 € in credit when signing up.
  - [3] 2026-11-25: the API is reachable at https://api.nodion.com with a bearer token | capture: sha256:662b058d4bc568539ac56847349710d42acf6853758a2691cedb629ef1b049b0 | quote: Base: `https://api.nodion.com`
  - [4] 2026-11-25: the hosted sign-in offers a social provider or an email and password, with no phone, ID or card at sign-in | capture: sha256:08061cb6cca5653b20573c4db76b0e4bb83f34373f2cdd6c32b7c3329c7b6d51 | quote: Log in or sign up
  - withheld 2026-11-25: the operator's list prices Nodion Sandboxes at USD 0.031 per hour billed per second, a reported rate about a third party and not a reading of the vendor's own page | capture: sha256:4d220f8008ed2a6126e4b7f8bc4639bd9e625605ec428846fde2bdf593cc5c95 | quote: 25. Nodion Sandboxes → $0.031/h · billed per second (new)
  - [2] 2026-11-24: smallest sandbox package is EUR 0.0139 per hour with a EUR 10 monthly running-time ceiling and 1 vCPU, 2 GB RAM, 16 GB workspace | capture: sha256:e9db0e5818bf67a3fb56b8506786f099e0c9bb5e21d6b769c38be09f96f55a15 | quote: GP-G2-2GB 0,0139 € / hour For scripts, tests and a single coding agent. 10,00 € per month of running time at most. 1 vCPU, 2 GB RAM, 16 GB workspace
  - [2] 2026-11-24: largest listed sandbox package is EUR 0.1111 per hour with an EUR 80 monthly ceiling | capture: sha256:e9db0e5818bf67a3fb56b8506786f099e0c9bb5e21d6b769c38be09f96f55a15 | quote: GP-G2-16GB 0,1111 € / hour For heavy builds and several services at once. 80,00 € per month of running time at most. 8 vCPU, 16 GB RAM, 128 GB workspace
  - [2] 2026-11-24: sandboxes are created and driven over MCP, CLI and REST API | capture: sha256:e9db0e5818bf67a3fb56b8506786f099e0c9bb5e21d6b769c38be09f96f55a15 | quote: You or your agent create it from the dashboard, over MCP, the CLI or the REST API, and running time is billed per second.
  - [2] 2026-11-24: default network mode is internet over NAT with no project network access, and overlay mode opts in | capture: sha256:e9db0e5818bf67a3fb56b8506786f099e0c9bb5e21d6b769c38be09f96f55a15 | quote: Network ### Isolated by default. Outbound internet over NAT, no access to your project's private network. Overlay mode opts in when the code should reach your databases.
  - [2] 2026-11-24: a sandbox sleeps after 5 idle minutes and only its disk is billed | capture: sha256:e9db0e5818bf67a3fb56b8506786f099e0c9bb5e21d6b769c38be09f96f55a15 | quote: After 5 idle minutes the sandbox goes to sleep. Only its disk is billed.
  - [2] 2026-11-24: API commands take at most 15 minutes per call | capture: sha256:e9db0e5818bf67a3fb56b8506786f099e0c9bb5e21d6b769c38be09f96f55a15 | quote: Run any command over the API and get its output and exit code, up to 15 minutes per call.
  - [2] 2026-11-24: a sandbox lives until deleted and its disk is billed while it sleeps | capture: sha256:e9db0e5818bf67a3fb56b8506786f099e0c9bb5e21d6b769c38be09f96f55a15 | quote: A sandbox lives until you delete it. While it sleeps, only its workspace disk is billed.
  - [5] 2026-11-24: each application instance includes 1 TB outbound per month as fair use, and object storage and CDN egress are EUR 0.005 per GB | capture: sha256:ee27ed26d1dad37840b7bb8ca1574425ee8a046df3c451d4add9f9b73f3b2693 | quote: Outbound traffic from applications and databases is not billed per GB. Every instance includes 1 TB of outbound traffic per month as fair use; if an app regularly needs more, we get in touch with you first. Object storage and CDN egress are billed per GB at the outbound rate listed above. Inbound and internal traffic is always free.
  - [5] 2026-11-24: signup credit is one-time and there is no recurring monthly free tier | capture: sha256:ee27ed26d1dad37840b7bb8ca1574425ee8a046df3c451d4add9f9b73f3b2693 | quote: There is no recurring monthly free allowance. New accounts can earn up to 15 € in credit when signing up, then usage is billed as you go.
  - [6] 2026-11-24: signup credit is EUR 5 each for product updates, X and Discord, granted on email confirmation | capture: sha256:88ecc9c5eb0b1bc898f9037460721391357229729f35c44d1a9face0bcc6262f | quote: There is no monthly free tier. New accounts can earn up to 15 € in credit when signing up: 5 € each for subscribing to product updates, following Nodion on X and joining the Discord community. Claimed credit is granted once your email address is confirmed.
  - [6] 2026-11-24: the accepted payment methods are card, SEPA direct debit and PayPal, charged monthly for the previous month | capture: sha256:7bb452e648a3233db46cc05e789677bf379def70d4cc4e78ee36870bba270b0e | quote: Add a card, SEPA direct debit, or PayPal. The default method is charged monthly for the previous month. Usage is metered (apps and databases down to the second).
  - [5] 2026-11-24: creating services needs a positive balance or a chargeable payment method | capture: sha256:ee27ed26d1dad37840b7bb8ca1574425ee8a046df3c451d4add9f9b73f3b2693 | quote: To create services, your account needs a balance > 0 € or a payment method we can charge. New accounts can earn up to 15 € in credit when signing up.
  - [7] 2026-11-24: signup accepts GitHub OAuth or an email address | capture: sha256:8ec92e792670522dc73e02df74e1e08ea805fc834ec1b81690caaac51bde1562 | quote: Continue with GitHub or with email Email addressStart free
  - [3] 2026-11-24: API calls are rate limited per account and a 429 carries Retry-After | capture: sha256:a8e86c2bf0a82230d228d0d4e744988eae902808580b28365f595716662a16ce | quote: Key-authenticated calls are rate limited per account. Responses include `RateLimit-Limit`, `RateLimit-Remaining`, and `RateLimit-Reset`. A `429` also sends `Retry-After`. Every response has `X-Request-Id`.
- sources:
  - [1] https://www.nodion.com/en/docs/
  - [2] https://www.nodion.com/en/ai-sandboxes/
  - [3] https://www.nodion.com/en/docs/api/
  - [4] https://app.nodion.com/assets/index-CsJ_Rknj.js
  - [5] https://www.nodion.com/en/pricing/
  - [6] https://www.nodion.com/en/docs/billing/
  - [7] https://www.nodion.com/en/docs/getting-started/
