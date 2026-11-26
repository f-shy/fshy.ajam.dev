# naïve

> usenaive.ai | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenaive/ | JSON https://fshy.ajam.dev/api/v1/entity/usenaive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## naïve (naive)

- `compute/naive` | qualifies-with-caveat | evidence documented | binding volume-quota | category microVM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.732Z (live) | stale on 2026-12-26
- url https://usenaive.ai/blogs/introducing-sandbox
- free tier: Start free with 5,000 credits (USD 1) and no card to start; the Standard 7-day trial grants 50,000 credits (USD 10) but requires adding a card, and converts to USD 20 a month unless cancelled before day 7. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: 5,000 credits are the free starting balance, not a recurring monthly allowance. A computer is billed per second on provisioned vCPU and memory; a session's 1 vCPU / 1 GiB computer costs 333 credits (USD 0.0666) per running hour, and a 2 vCPU / 4 GiB computer costs USD 0.1656 an hour at published rates.
- per-object cap: The unit is a microVM, not an object. A session's computer is 1 vCPU / 1 GiB; one created directly defaults to 2 vCPU / 4096 MiB, with a range of 1 to 16 vCPU and 128 to 65536 MiB, disk up to 100 GiB. | source: [2]
- retention: A computer is disposable: state is ephemeral by default and a destroy tears it down. A snapshot is a durable checkpoint that survives destroy, a persistent volume keeps disk and paused memory across park and sleep but not destroy, and files that must outlive the sandbox are published to Files. | source: [2]
- egress: A computer has general outbound access by default with cloud metadata and internal ranges filtered; allow_outbound: false is an immutable kill-switch for all outbound traffic. Nothing reaches in: there is no port-preview surface. No egress price or volume allowance is published. | metered: no | source: [2]
- identity: email | detail: The register page at app.usenaive.ai/register renders an Email field and a terms agreement; the onboarding manifest documents 'naive auth register --email ... --password ...' with a confirmation mail, and states an account starts at 0 credits until a plan is chosen. No card is needed to start free, but the 7-day Standard trial and any paid plan require a card.
- interface: rest, cli
- limits:
  - volume-quota (binding): 5,000 free credits (USD 1) at start; vCPU USD 0.000014 per second and memory USD 0.0000045 per GiB-second, with no creation fee [2]
  - write-gated: the Standard 7-day trial requires a card and grants 50,000 credits; every route outside billing needs an active plan, and a paused computer resumes only if the balance covers one 10-minute block [1]
  - retention-clamped: 12-hour maximum runtime from create to destroy, fixed with no per-computer override; the computer is auto-destroyed at the ceiling [3]
- limits note: A computer you create is billed in advance in 10-minute blocks; a session's computer is billed per running second. The browser is capped at 360 minutes per session. Automatic destroy at zero balance and per-organization concurrency caps are not enforced yet.
- binding note: The USD 1 starting credit runs out first: it buys about 15 hours of a session's 1 vCPU / 1 GiB computer or about 6 hours of the 2 vCPU / 4 GiB default, both shorter than the 12-hour runtime ceiling.
- interface detail: A TypeScript SDK (@usenaive-sdk/managed-agents) and a CLI (naive computer create/exec/fs/snapshot/pause/delete) against the API base URL https://api.vetta.sh with an API key.
- tooling: The naive CLI and TypeScript SDK create and drive computers; a session's agent reaches the same machine through built-in shell, filesystem and browser tools.
- composes with: A computer pauses between agent turns and wakes on the next operation, so a multi-hour task pays only for running seconds; publish_file moves artifacts out to organization-scoped Files that outlive the sandbox.
- reliability: Automatic destroy at zero balance and after the maximum runtime is not enforced yet, so a user must delete a computer when finished; cloud metadata, 10.0.0.0/8 and 172.16.0.0/12 are blocked but 192.168.0.0/16 is not reliably blocked, so private-range blocking is not a security boundary for the shell.
- notes: naïve sells a hosted disposable Linux microVM ('computer') as part of Naive Managed Agents, either provisioned by a session or created directly through the CLI or SDK. A session computer is 1 vCPU / 1 GiB at USD 0.0666 per running hour; the directly created default 2 vCPU / 4 GiB is USD 0.1656 an hour. Idle between turns costs nothing because the machine sleeps. The account starts with 5,000 free credits and no card; a card is required for the 7-day trial and any paid plan. The 12-hour lifetime cap and unenforced failsafes are the caveats.
- evidence note: The computer price, egress behaviour and lifecycle are quoted from the vendor's launch post read on 2026-11-25; the free credits, trial card gate and 12-hour ceiling are from the vendor pricing and limits pages on the same date.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.note: the directly created default; a session computer is 1 vCPU / 1 GiB
  - billing_model: per-second running time, 10-minute blocks for a directly created computer
  - free_tier_kind: one-time-credit
  - status: hosted, available
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: no port-preview surface; nothing reaches in
  - session_cap.wall_clock_min: 720
  - session_cap.restart_required: no
  - session_cap.note: 12-hour maximum runtime from create to destroy, with auto-destroy not enforced yet
- evidence:
  - [2] 2026-11-25: the per-second price with no creation fee and the USD 0.0666 session computer hour | capture: sha256:c69753df518886449435af547b73f1ae589ffda7a4a75363598e2454a780af85 | quote: There is no creation fee. Running time is metered per second on provisioned vCPU and memory; a full hour of a session's 1 vCPU / 1 GiB computer is $0.0666.
  - [2] 2026-11-25: outbound network access is available by default | capture: sha256:c69753df518886449435af547b73f1ae589ffda7a4a75363598e2454a780af85 | quote: A computer has general outbound access by default, so the agent can install packages, call APIs, and fetch data without configuration.
  - [2] 2026-11-25: an immutable outbound kill-switch is available at create time | capture: sha256:c69753df518886449435af547b73f1ae589ffda7a4a75363598e2454a780af85 | quote: The one control that is a boundary is `allow_outbound: false` at create time: a complete, verified kill-switch for all outbound traffic, immutable for the life of the computer.
  - [2] 2026-11-25: the advertised zero-balance and max-runtime destruction failsafes are not enforced | capture: sha256:c69753df518886449435af547b73f1ae589ffda7a4a75363598e2454a780af85 | quote: Automatic destroy at a zero balance or after a max runtime is not enforced yet, so delete a computer when you are done with it.
  - [1] 2026-11-25: 5,000 free starting credits and the USD 20 monthly plan with 100,000 credits | capture: sha256:4c4416f7c3b773e99cbd618c70a21b5fbdbb733dbda03331fd5d79ddcf17a8a5 | quote: Your AI team does the work. Start free with 5,000 credits. Then $20 a month, with 100,000 credits your agents spend as they work.
  - [1] 2026-11-25: the 7-day trial requires a card and grants 50,000 credits | capture: sha256:4c4416f7c3b773e99cbd618c70a21b5fbdbb733dbda03331fd5d79ddcf17a8a5 | quote: Standard starts with 7 days free and 50,000 credits. You add a card to start, and if you cancel before day 7 you pay nothing.
  - [3] 2026-11-25: the fixed 12-hour runtime ceiling | capture: sha256:0daac77756b6abddb52662e46d39738ad7ce93f30523f3470072f78e6c122b4b | quote: Max runtime | 12 hours, fixed | A computer exceeding it is auto-destroyed. There is no per-computer override.
  - [4] 2026-11-25: the registration form asks for an email address | capture: sha256:c9d2cf3a7473b25be66d303a3e9ad617465265fa5558916c49f379678dc3aff9 | quote: Email
- sources:
  - [1] https://usenaive.ai/pricing
  - [2] https://usenaive.ai/blogs/introducing-sandbox
  - [3] https://usenaive.ai/docs/computer/limits-and-billing
  - [4] https://app.usenaive.ai/register

## naïve (Free)

- `compute/naive-free` | qualifies-with-caveat | evidence documented | binding retention-clamped | category managed AI agent platform with hosted computers | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-24T10:11:14.932Z (live) | stale on 2026-12-25
- url https://usenaive.ai/pricing
- free tier: Start free with 5,000 credits to try the whole team; no card to start. Standard then costs $20 a month with 100,000 credits a month; a separate Standard 7-day trial requires a card. | unit: credits | metered on: wall-clock | read on: 2026-11-24 | source: [1] | note: The hosted computer is charged 252 credits per vCPU-hour and 81 credits per GiB-hour, so 5,000 credits pays for about 15 hours of the 1 vCPU / 1 GiB session computer at 333 credits an hour, within its 12-hour cap. Credits roll over and do not expire.
- per-object cap: not applicable: the unit is an agent's computer, not an object; a file read or write is 4 MiB per call, publish_file or fetch_file moves up to 5 GiB per file, and shell output is 262,144 characters per stream
- retention: Included credit rolls over and never expires; a computer is auto-destroyed at 12 hours from create, and when its balance cannot pay the next 10-minute block it is paused with its disk kept. | source: [2]
- egress: The hosted computer runs on the platform; no outbound data volume allowance or per-TB price is published. Agent email is 4 credits per send however many recipients, web_fetch about 4 credits per page and web_search about 8 credits, and each phone-minute includes the residential network the traffic exits through. | metered: no | source: [3]
- identity: email | detail: Registration is by email and starts with 5,000 credits and no card; a Google or other social option is not shown on the signup page. A card is required only for the 7-day Standard trial, and one trial is allowed per organization and per person.
- interface: rest, cli, chat
- limits:
  - retention-clamped (binding): 12 hours maximum computer runtime from create to destroy; no per-computer override [2]
  - volume-quota: 5,000 credits to start, at 333 credits per hour for the 1 vCPU / 1 GiB session computer [2]
  - per-object-cap: 4 MiB per file read or write call; 5 GiB per publish_file or fetch_file; 262,144 characters per shell output stream [2]
- limits note: A computer you create yourself is billed ahead in 10-minute blocks and needs a balance covering one block to create or resume; a session's computer is metered per running second. There is no count limit on computers, only the balance.
- binding note: The 12-hour fixed lifetime with no override ends a long-running job whatever the balance, before the free credit or the per-call file cap is spent.
- interface detail: Agents are driven from the studio chat and a REST API such as POST /v1/agents and /v1/computers, with a naive command line tool; computer files and shell are reached through the API's file and shell routes.
- endpoint: https://app.usenaive.ai/register
- tooling: the studio, the REST API and the naive CLI; an agent's computer runs commands and files through the API and a browser, phone and mobile device can be attached to it
- composes with: One company plan covers all agents with no per-person fee, and the same credit balance pays model inference, the hosted computer, web tools, media and phone minutes; files must be published off the computer with publish_file before its 12-hour auto-destroy.
- reliability: A computer is paused when its balance cannot cover the next 10-minute block and is auto-destroyed at 12 hours; an unfunded mobile device is ended with termination_reason unfunded, and a data or social data run past two minutes is stopped.
- notes: The free tier is 5,000 credits, no card at signup, for a hosted AI agent platform whose agents run a hosted computer billed in credits; the Standard plan is $20 per month with 100,000 credits and Pro is $200 with 1,000,000. Compute is capped at 12 hours per computer, and the documentation is served from a separate domain at vetta.sh. Hosted service; the user runs only the CLI against it.
- evidence note: The free grant, credit rate, card-free signup and paid prices are quoted from the vendor's pricing and registration pages read on 2026-11-24; the runtime ceiling, metering and per-object caps are quoted from its own documentation.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.note: the session computer is 1 vCPU and 1 GiB; custom sizes are not published on the pricing page
  - billing_model: free credits, then a per-organization monthly plan with metered compute, tools and models
  - free_tier_kind: recurring-allowance
  - term: no expiry on credits; 12-hour hard ceiling per computer
  - price_arithmetic: 5,000 credits at 5,000 per USD is USD 1; 333 credits an hour gives about 15 hours of the session computer, capped at 12 hours
  - status: published free and paid tiers
  - network_out.allow_outbound: yes
  - network_out.note: web_fetch and web_search are priced per call; no host egress volume price is published
  - session_cap.wall_clock_min: 720
  - session_cap.restart_required: no
  - session_cap.note: a computer is auto-destroyed at 12 hours; an unfunded one is paused with its disk kept
- evidence:
  - [1] 2026-11-24: the free tier gives 5,000 credits to try the whole team | capture: sha256:4c4416f7c3b773e99cbd618c70a21b5fbdbb733dbda03331fd5d79ddcf17a8a5 | quote: 5,000 creditsto try it
  - [1] 2026-11-24: no card is needed to start the free tier | capture: sha256:4c4416f7c3b773e99cbd618c70a21b5fbdbb733dbda03331fd5d79ddcf17a8a5 | quote: No card to start
  - [1] 2026-11-24: one US dollar is 5,000 credits and Standard costs $20 a month | capture: sha256:4c4416f7c3b773e99cbd618c70a21b5fbdbb733dbda03331fd5d79ddcf17a8a5 | quote: Then $20/mo on Standard
  - [3] 2026-11-24: a 15-second Mira edit costs 2,250 credits and an email 4 credits | capture: sha256:c538ae3b9e8f2f3088ef2826d9462953e5a043d60e42595f2360229abb549f78 | quote: A 15-second edit with Mira costs 2,250 credits.
  - [2] 2026-11-24: create and resume need a balance covering one full 10-minute block at the computer's size | capture: sha256:0daac77756b6abddb52662e46d39738ad7ce93f30523f3470072f78e6c122b4b | quote: Create and resume** need a balance that covers one full block
  - [2] 2026-11-24: a session computer at 1 vCPU and 1 GiB costs 333 credits for a full running hour | capture: sha256:0daac77756b6abddb52662e46d39738ad7ce93f30523f3470072f78e6c122b4b | quote: A session's computer is `1 vCPU / 1 GiB`, so a full hour of running time is 252 + 81 = 333 credits.
  - [4] 2026-11-24: the signup page offers email registration and no social or phone option | capture: sha256:c9d2cf3a7473b25be66d303a3e9ad617465265fa5558916c49f379678dc3aff9 | quote: Email
  - [5] 2026-11-24: the 7-day Standard trial requires a card and one trial is allowed per organization and per person | capture: sha256:2e952ffd542cc34d6066615407f40fe8f45deed0063b73b2c53364d2a823b36f | quote: a card is required
- sources:
  - [1] https://usenaive.ai/pricing
  - [2] https://vetta.sh/docs/computer/limits-and-billing.md
  - [3] https://vetta.sh/docs/platform/pricing.md
  - [4] https://app.usenaive.ai/register
  - [5] https://vetta.sh/docs/cli/billing.md
