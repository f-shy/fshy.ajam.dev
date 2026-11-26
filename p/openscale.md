# OpenScale Sandboxes

> openscale.so | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openscale/ | JSON https://fshy.ajam.dev/api/v1/entity/openscale.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenScale Sandboxes

- `compute/openscale-sandboxes` | qualifies-with-caveat | evidence documented | binding volume-quota | category microVM sandbox | tier Pay-as-you-go sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-25T11:55:06.271Z (live) | stale on 2026-12-26
- url https://openscale.so/sandboxes
- free tier: New accounts get free credit to try the API; the first top-up within 7 days adds up to USD 100 more: USD 10 gets USD 2, USD 50 gets USD 15, USD 250 gets USD 100. Paused sandboxes cost nothing. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The size of the starting free credit is not stated on either page, so it is unverified: behind a sign-up. No recurring sandbox allowance is published. Credits bought never expire; card top-ups add a processing fee.
- per-object cap: Each sandbox has 25 GB of disk included and supports 1-8 vCPU and up to 16 GB of memory; no larger disk option is published. | source: [2]
- retention: A sandbox lives until the user deletes it, with no session time limit; after 5 idle minutes it pauses itself with memory and files intact, and paused sandboxes are free and kept. No maximum paused duration is published. | source: [2]
- egress: The sandbox page states no egress allowance or per-GB price; preview URLs are published per port and the sandbox has a network of its own. | metered: no | source: [2]
- identity: email | detail: unverified: no captured or fresh first-party page states what the sign-up requires; the pricing page says only 'Create an account' to get an API key and the sandbox page says 'Sign in and copy it', while app.openscale.so/signup renders a startups marketing page with no form. The sign-up fields are unverified: behind a sign-up. Card top-ups from USD 5 with a processing fee are stated on the pricing page, but no card is shown at registration.
- interface: rest, cli
- limits:
  - volume-quota (binding): one-time free credit of unstated size for new accounts, plus up to USD 100 of top-up matching credit [1]
  - volume-quota (binding): USD 0.0065 per vCPU-hour plus USD 0.001 per GiB-hour; USD 0.034 an hour for 4 vCPU and 8 GB [2]
  - volume-quota (binding): 100 sandboxes running at once by default, raised on request [2]
- limits note: No platform fee, no minimum and no session time limit; a sandbox sleeps after 5 idle minutes. Volumes, secrets, fork and the snapshots API are not supported yet, and there is no GPU.
- binding note: The free credit is the first limit a new account meets, since there is no session cap and no platform fee; its size is not published, so the number of free hours is unverified.
- interface detail: E2B-compatible JS and Python SDKs and CLI work unchanged after setting E2B_DOMAIN=sandbox.openscale.so and E2B_API_KEY to the OpenScale key; commands, streaming, stdin, an interactive terminal, files, preview URLs and a headless browser are listed.
- endpoint: https://api.openscale.so/v1
- tooling: E2B SDKs for JavaScript and Python and an E2B-style CLI, with two environment variables changed; REST access is implied by the SDK compatibility.
- composes with: The same API key works for models and sandboxes, so an agent can switch between inference and compute without a second credential; files and memory survive pause and resume.
- reliability: Sandboxes run in Singapore only; volumes, secrets, fork and the snapshots API are not supported, no GPU is offered, the free credit's amount is not published, and no page read states the registration identity.
- notes: The rate card gives USD 0.0065 per vCPU-hour plus USD 0.001 per GiB-hour, so a 4 vCPU / 8 GB sandbox is USD 0.034 an hour and 100 for one hour is USD 3.40, matching the page's comparison table. The headline free credit has no published size, so the number of free hours is unverified: behind a sign-up. The hosted sandbox is the offer; no self-hosted variant is priced here.
- evidence note: The per-second rate, shape, concurrency, pause behaviour and lack of session cap were read from the first-party sandbox page. No page read states the sign-up identity, so identity_cost.kind is a defaulted placeholder with an unverified detail; the free credit amount and signup fields are also unverified.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 8
  - shape.disk_gib: 25
  - billing_model: per-second, prepaid credit
  - free_tier_kind: one-time-credit
  - term: no minimum, no session limit
  - price_arithmetic: 4 x USD 0.0065 + 8 x USD 0.001 = USD 0.034/hour; 100 x 1 h = USD 3.40
  - status: live hosted service
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: a preview URL per port
  - session_cap.idle_reap_s: 300
  - session_cap.restart_required: no
  - session_cap.note: auto-pause after 5 idle minutes, resume with memory and files intact; no session time limit
- evidence:
  - [2] 2026-11-25: the sandbox price is USD 0.0065 per vCPU-hour plus USD 0.001 per GiB-hour with no platform fee or minimum and paused sandboxes free | capture: sha256:9a1db03456a3e77908a783c9b515b35c828510a27440f301ba61ac18f3b0c367 | quote: Per second while a sandbox runs, on its allocated size: $0.0065 per vCPU-hour plus $0.001 per GiB-hour of memory. No platform fee, no minimum. Paused sandboxes cost nothing.
  - [2] 2026-11-25: a sandbox pauses itself after 5 idle minutes | capture: sha256:9a1db03456a3e77908a783c9b515b35c828510a27440f301ba61ac18f3b0c367 | quote: After 5 idle minutes it pauses itself.
  - [2] 2026-11-25: 100 sandboxes run at once by default | capture: sha256:9a1db03456a3e77908a783c9b515b35c828510a27440f301ba61ac18f3b0c367 | quote: 100 by default.
  - [2] 2026-11-25: the shape is 1-8 vCPU, up to 16 GB memory and 25 GB disk included | capture: sha256:9a1db03456a3e77908a783c9b515b35c828510a27440f301ba61ac18f3b0c367 | quote: 1–8 vCPU and up to 16 GB of memory, with 25 GB of disk included.
  - [2] 2026-11-25: there is no session time limit and a sandbox lives until deleted | capture: sha256:9a1db03456a3e77908a783c9b515b35c828510a27440f301ba61ac18f3b0c367 | quote: No session time limit
  - [1] 2026-11-25: new accounts get free credit to try the API | capture: sha256:d34ee3fabb84ecbc41552f1397bcc3f25732e29128eae5baa4587a291cb367dd | quote: New accounts get free credit to try the API.
  - [1] 2026-11-25: an account is created at app.openscale.so/signup to get an API key | capture: sha256:d34ee3fabb84ecbc41552f1397bcc3f25732e29128eae5baa4587a291cb367dd | quote: Create an account
  - [2] 2026-11-25: the sandbox is reached by setting two E2B environment variables and runs SDK code unchanged | capture: sha256:9a1db03456a3e77908a783c9b515b35c828510a27440f301ba61ac18f3b0c367 | quote: E2B_DOMAIN=sandbox.openscale.so
  - [3] 2026-11-25: the sign-up URL renders a startups marketing page with no account form text | capture: sha256:226b0fde9802d317d08b463e5ffab2eddec6dda09a4e3b4dc828ebb4c5c270de | quote: OpenScale gives early stage startups up to $5,000 in free credits to build things.
  - [2] 2026-11-24: a 4-vCPU 8-GB sandbox costs $0.034 an hour with no platform fee and no minimum | capture: sha256:9a1db03456a3e77908a783c9b515b35c828510a27440f301ba61ac18f3b0c367 | quote: 4 vCPU and 8 GB for $0.034 an hour. No platform fee, no minimum.
  - [2] 2026-11-24: billing is $0.0065 per vCPU-hour plus $0.001 per GiB-hour of memory, per second, with paused sandboxes free | capture: sha256:9a1db03456a3e77908a783c9b515b35c828510a27440f301ba61ac18f3b0c367 | quote: Per second while a sandbox runs, on its allocated size: $0.0065 per vCPU-hour plus $0.001 per GiB-hour of memory. No platform fee, no minimum. Paused sandboxes cost nothing.
  - [2] 2026-11-24: 100 sandboxes run at once by default, with 1-8 vCPU, up to 16 GB memory and 25 GB disk included and no GPU | capture: sha256:9a1db03456a3e77908a783c9b515b35c828510a27440f301ba61ac18f3b0c367 | quote: 1–8 vCPU and up to 16 GB of memory, with 25 GB of disk included. No GPU.
  - [2] 2026-11-24: a sandbox has no time limit and lives until deleted, with auto-pause after 5 idle minutes | capture: sha256:9a1db03456a3e77908a783c9b515b35c828510a27440f301ba61ac18f3b0c367 | quote: After 5 idle minutes it pauses itself. The next call wakes it, memory and files intact.
  - [2] 2026-11-24: existing E2B SDKs switch with two environment variables | capture: sha256:9a1db03456a3e77908a783c9b515b35c828510a27440f301ba61ac18f3b0c367 | quote: E2B_DOMAIN=sandbox.openscale.so
  - [1] 2026-11-24: a first top-up within 7 days of signing up adds up to $100 in credit, and add credit starts from $5 | capture: sha256:9f8b3d6f77e5944e789d20e84903dfd54a778c338e2637a9d4ec132d335ced68 | quote: New accounts get free credit to try the API. Your first top-up within 7 days of signing up adds up to $100 in credit on top: $10 gets $2, $50 gets $15, $250 gets $100.
  - [1] 2026-11-24: card top-ups carry a processing fee and an account and API key are needed to buy credit | capture: sha256:9f8b3d6f77e5944e789d20e84903dfd54a778c338e2637a9d4ec132d335ced68 | quote: Card top-ups add a processing fee that covers the card network's cost, shown before you pay: $10 in credits costs $11.05 by card.
  - [4] 2026-11-24: the landing page advertises up to $100 in free credits and 100 sandboxes at 4 vCPU 8 GB for $3.40 per 100 running hours | capture: sha256:1f7087149611d885a477a06648f28e8dffdbc37dc91bed9329b8428b5ac198f4 | quote: Get up to $100 in free creditsView Pricing
  - [4] 2026-11-24: Chat and Messages bodies are never stored and Responses API responses are kept 30 days unless zero data retention is enabled | capture: sha256:1f7087149611d885a477a06648f28e8dffdbc37dc91bed9329b8428b5ac198f4 | quote: Chat and Messages requests are processed in memory and never stored. Responses API responses are kept 30 days for multi-turn state, and one switch turns that off.
  - [5] 2026-11-24: the account-wide rate budgets are 100 requests and 10,000,000 tokens per minute | capture: sha256:0b91a29b39d4451cb8789af813b0742619c260d67ac14373097cf829324ea8bd | quote: | Requests | 100 | | Tokens (prompt, cached prompt and completion combined) | 10,000,000 |
  - [6] 2026-11-24: an API key is created in the dashboard after signup and a missing or revoked key returns 401 | capture: sha256:4fe22305d1ac4321a56eb563013d7d6ab72b947d01e8c2cae94f708e42c1b76f | quote: Create a key in the dashboard ([sign up](https://app.openscale.so/signup?utm_source=api_reference&utm_medium=docs) if you have no account yet) and send it on every request: ``` Authorization: Bearer sk-openscale-... ``` Keys are shown once when created. A missing or revoked key returns `401`.
- sources:
  - [1] https://openscale.so/pricing
  - [2] https://openscale.so/sandboxes
  - [3] https://app.openscale.so/signup
  - [4] https://openscale.so/
  - [5] https://openscale.so/docs/rate-limits
  - [6] https://openscale.so/docs
