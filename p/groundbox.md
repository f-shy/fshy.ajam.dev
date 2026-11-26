# Groundbox

> groundbox.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/groundbox/ | JSON https://fshy.ajam.dev/api/v1/entity/groundbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Groundbox

- `compute/groundbox` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding volume-quota | category sandbox | tier Free plan / Pro
- needs card no, phone no, ID no, institution no | verified 2026-11-25T16:38:10.902Z (live) | stale on 2026-12-26
- url https://groundbox.dev/pricing
- free tier: Free plan: 3,000 CI minutes a month, $5 of usage to start and small sandboxes until a card is added; an agent can sign itself up with $5.00 of free usage and no card. Billed by the second. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1]
- per-object cap: not applicable: the unit is a 20 GB sandbox disk, not a stored object; retained disks and volumes are billed per GB-month
- retention: On the free plan each sandbox lives at most 60 minutes from its start and pausing does not stop that clock; a link nobody claims stops working after a month. | source: [2]
- egress: not published for sandboxes: the pricing page names previews and public URLs but states no egress allowance or per-GB price | metered: no | source: [1]
- identity: anonymous | detail: An agent can sign itself up with POST /signup and no person and no card, getting an API key and a claim link for a person; a person signs up in the dashboard with GitHub, Google, GitLab or email and a verified email, and the free credit comes once per person. A card is needed only for full-size sandboxes, CI installation and auto top-up.
- interface: rest, cli, ssh
- limits:
  - volume-quota (binding): $5.00 of free usage on the free plan, then $0.04 per vCPU-hour running and $0.05 per GB-month paused or stopped [1]
  - retention-clamped: on the free plan each sandbox lives at most 60 minutes from its start, including while paused; a paid sandbox can run up to 720 hours [2]
  - request-rate: 2 sandboxes at a time until a card is on file; one more gets 429 concurrency_limit [3]
- limits note: No numeric quota, rate or object cap is published on the public site; the binding constraint is that the reader installs and operates the server, not a meter.
- binding note: The $5.00 of usage is what runs out first at $0.04 per vCPU-hour; the 60-minute free life and the two-sandbox cap bound a session, not the account balance.
- interface detail: REST API at https://api.groundbox.dev/v1, a Node CLI, SDKs and a hosted MCP server; a sandbox is a Linux VM with exec and file endpoints.
- endpoint: part of interface detail
- tooling: curl against the REST API, the groundbox CLI, Python and TypeScript SDKs, and MCP clients; a sandbox command runs with sh -c and a WebSocket streams output.
- composes with: $0.04 per vCPU-hour running and $0.05 per GB-month paused make a two-vCPU sandbox about $0.08 an hour, which can hand off to S3-compatible buckets and an image registry on the same account.
- reliability: At a spend cap, creating or starting a sandbox is refused and running sandboxes are stopped; a sandbox older than 60 minutes on the free plan is deleted with its save points, and a team may be suspended.
- notes: The free plan's $5 of usage covers the per-second sandbox meter; at $0.04 per vCPU-hour a two-vCPU box costs $0.08 an hour. A card is not needed to start but is needed for full-size or long-running sandboxes, and the 60-minute free life is a hard session ceiling. A separate file-sync product on groundbox.io is not this offer.
- evidence note: Prices, the free credit, the sign-up gates and the session caps are quoted from the vendor's own pricing page, API reference and sandbox guide read on 2026-11-25.
- self hosted: yes
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gb: 20
  - shape.note: free-plan limits before a card: 2 vCPU, 4 GB memory, a 20 GB disk and at most 2 sandboxes
  - billing_model: per-second usage against a $5 free credit, then per-vCPU-hour while running and per-GB-month while stopped
  - free_tier_kind: one-time-credit
  - term: free until the $5 credit is spent or the sandbox reaches 60 minutes
  - price_arithmetic: $5 of usage to start; $0.04 per vCPU-hour running; $0.05 per GB-month paused; $20 Pro plan with $20 included
  - derived: $0.04 per vCPU-hour x 2 vCPU = $0.08 per hour for the two-vCPU sandbox in the operator list; $5 / $0.08 per hour = 62.5 hours of usage
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: previews and public URLs are documented; no per-GB egress price is stated
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: no
  - session_cap.note: a free sandbox is deleted 60 minutes after its start, paused or not; a paid one can be set up to 720 hours
- evidence:
  - [1] 2026-11-25: the free plan gives 3,000 CI minutes a month and $5 of usage to start, and the $20 Pro plan includes $20 of usage | capture: sha256:93a40e92e6791bf17b654132dfdb0089164b5b596fe77a0ff67b0ff7e66d9d58 | quote: Free to start: 3,000 CI minutes a month and $5 of usage to start.
  - [1] 2026-11-25: a running sandbox is $0.04 per vCPU-hour and a paused or stopped one is $0.05 per GB-month | capture: sha256:93a40e92e6791bf17b654132dfdb0089164b5b596fe77a0ff67b0ff7e66d9d58 | quote: | Running | $0.04 / vCPU-hour |
  - [1] 2026-11-25: paused or stopped sandboxes are billed per GB of disk per month | capture: sha256:93a40e92e6791bf17b654132dfdb0089164b5b596fe77a0ff67b0ff7e66d9d58 | quote: | Paused or stopped | $0.05 / GB-month |
  - [1] 2026-11-25: a young GitHub account gets only 4 jobs at once and 30-minute jobs on the free plan | capture: sha256:93a40e92e6791bf17b654132dfdb0089164b5b596fe77a0ff67b0ff7e66d9d58 | quote: A GitHub account that is under 7 days old or has no public repositories gets 4 jobs at once and 30-minute jobs on the free plan.
  - [2] 2026-11-25: an agent can obtain a trial key without a person or a card | capture: sha256:efd9f4acffac10f5e56454f16cbdebcf597a1fb8298120fe3821294b4ae400a0 | quote: An agent can sign itself up and test Groundbox with no person and no card.
  - [2] 2026-11-25: the trial key starts with $5 of free usage and returns a claim link | capture: sha256:efd9f4acffac10f5e56454f16cbdebcf597a1fb8298120fe3821294b4ae400a0 | quote: The answer has `api_key` (shown once), `status: "trial"`, `trial` (credit and limits), `claim_url` and `message_for_human`.
  - [2] 2026-11-25: before a card a team runs two sandboxes with up to 2 vCPU, 4 GB and a 20 GB disk | capture: sha256:efd9f4acffac10f5e56454f16cbdebcf597a1fb8298120fe3821294b4ae400a0 | quote: 2 sandboxes at a time, forks and fork group copies included, up to 2 vCPU, 4 GB of memory and a 20 GB disk.
  - [2] 2026-11-25: a free sandbox is deleted after 60 minutes even if paused | capture: sha256:efd9f4acffac10f5e56454f16cbdebcf597a1fb8298120fe3821294b4ae400a0 | quote: Each sandbox lives at most 60 minutes from its start. Pausing does not stop that clock: a paused sandbox is deleted at the same mark, with its save points.
  - [2] 2026-11-25: a person can sign up with GitHub, Google, GitLab or a verified email and gets the credit once per person | capture: sha256:efd9f4acffac10f5e56454f16cbdebcf597a1fb8298120fe3821294b4ae400a0 | quote: Someone who signs up in the dashboard (GitHub, Google, GitLab or email) has it on their first team, once per person, with a verified email
  - [3] 2026-11-25: the sandbox is a Linux VM reached through a REST API | capture: sha256:fe84a974fdec9ad568cf0d3a66c578204831cadc43b8027a6af457b9915de070 | quote: A sandbox is a Linux VM of its own, with its own kernel, memory and disk. The API lives at `https://api.groundbox.dev/v1`.
  - [3] 2026-11-25: a third concurrent sandbox is refused with 429 concurrency_limit | capture: sha256:fe84a974fdec9ad568cf0d3a66c578204831cadc43b8027a6af457b9915de070 | quote: A team runs 2 of them at once; one more gets `429 concurrency_limit`.
  - [4] 2026-11-24: the MIT distribution is free and runs on the user's own machine and server | capture: sha256:da203e2b63088537ffd65beb024e995e3cb99dce2a3c90f2d4a8e013320928a2 | quote: Open source · MIT · your machine · your server · export by copying a folder
  - [4] 2026-11-24: the enterprise edition is licensed per organization with no published price | capture: sha256:da203e2b63088537ffd65beb024e995e3cb99dce2a3c90f2d4a8e013320928a2 | quote: licensed per organization, never per seat · terms on request
  - [4] 2026-11-24: what the user installs and runs | capture: sha256:da203e2b63088537ffd65beb024e995e3cb99dce2a3c90f2d4a8e013320928a2 | quote: One Go binary, Postgres and an object store, all of it MIT.
  - [4] 2026-11-24: the seven MCP tools are the full agent interface | capture: sha256:da203e2b63088537ffd65beb024e995e3cb99dce2a3c90f2d4a8e013320928a2 | quote: Seven MCP tools and no more. No database identifiers, no raw SQL, no admin mode.
  - [4] 2026-11-24: a user and server build and the platform requirement | capture: sha256:da203e2b63088537ffd65beb024e995e3cb99dce2a3c90f2d4a8e013320928a2 | quote: MIT · macOS client · self-hosted server · 0.1 (43), 18 MiB, macOS 14+
  - [4] 2026-11-24: an agent's writes are scoped to the person's grants | capture: sha256:da203e2b63088537ffd65beb024e995e3cb99dce2a3c90f2d4a8e013320928a2 | quote: An agent has no permissions of its own
  - [4] 2026-11-24: the open-source tier includes the whole product and is run by the user | capture: sha256:da203e2b63088537ffd65beb024e995e3cb99dce2a3c90f2d4a8e013320928a2 | quote: The complete product: server, macOS client, BRAIN, the seven MCP tools. Clone it, run it on your own hardware and never talk to us.
  - [5] 2026-11-24: the pricing URL returns a JavaScript shell with no rates in its body; the SPA needs JavaScript | capture: sha256:06a326caeab8773968b57397dea532bcf51c35cd3e5f98b59a343eefd24172bf | quote: Groundbox needs JavaScript to be enabled.
  - probe:https://groundbox.io/pricing 2026-11-24: the pricing URL answered HTTP 200 with a 1,988-byte HTML shell and no challenge under the direct probe | capture: sha256:e4611dce9f1a6d4a790c4e7888f4d7e6ecd74c160b7ce0f4ba5caf55163ae33e | quote: "status": 200
  - [2] 2026-11-25: the agent sign-up uses the anonymous identity flow, so no email, phone, card or person is required for the cheapest identity | capture: sha256:65bd43eb1efb3fe69571ef043225ba0cc7356d1fead3a28e692eacf1b631d546 | quote: Groundbox supports its `anonymous` flow: it is the sign-up above, with the same account, credit and limits.
  - [2] 2026-11-25: the agent identity route is anonymous, confirming identity_cost.kind is anonymous | capture: sha256:65bd43eb1efb3fe69571ef043225ba0cc7356d1fead3a28e692eacf1b631d546 | quote: Groundbox supports its `anonymous` flow: it is the sign-up above, with the same account, credit and limits.
- sources:
  - [1] https://groundbox.dev/pricing
  - [2] https://groundbox.dev/docs/api
  - [3] https://groundbox.dev/docs/sandboxes
  - [4] https://groundbox.io/
  - [5] https://groundbox.io/pricing
