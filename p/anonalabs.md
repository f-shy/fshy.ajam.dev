# Anona Compute

> anonalabs.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anonalabs/ | JSON https://fshy.ajam.dev/api/v1/entity/anonalabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Anona Compute

- `compute/anona-compute` | qualifies-with-caveat | evidence documented | binding volume-quota | category sandbox (KVM microVM) | tier Free plan, USD 25 usage once
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.793Z (live) | stale on 2026-12-26
- url https://docs.anonalabs.com/compute/pricing
- free tier: the Free plan is USD 0 per month and includes USD 25 of usage once, about 500 typical agent hours; no card payments are taken during the preview, the usage is metered and shown in the dashboard and the invoices are drafts | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: the usage dollar credit is spent at the published per-meter rates; a typical agent sandbox is about USD 0.05 an hour. When the credit runs out, creates are refused until a plan is bought or credit is added
- per-object cap: not applicable: the unit is a microVM, not a stored object
- retention: a paused sandbox keeps its memory and filesystem and is charged only snapshot storage at USD 0.03 per GB-month; a running sandbox is sampled running and a quarter of an hour costs a quarter of a sandbox-hour | source: [1]
- egress: egress is metered at USD 0.12 per GB; on the Free plan public internet egress is off, while Starter, Pro and Scale have it on by default | metered: yes | price per TB: USD 0.12 per GB | source: [1]
- identity: email | detail: the sign-in page renders an Email label and input, a Sign in button and an "Email me a sign-in link" button, plus Google and GitHub options; access to a new account is by invitation and the waitlist
- interface: rest, cli, ssh, sftp
- limits:
  - volume-quota (binding): USD 25 of usage once on the Free plan, spent at the published per-meter rates; creates are refused when it runs out [1]
  - request-rate: 5 running sandboxes and 5 paused sandboxes at once on the Free plan; longest timeout 1 hour; 2 API keys and 20 templates [2]
- limits note: Per-sandbox size limits, per-minute create rates and request rates exist in the plans but are not enforced by the gateway yet. Cold starts wait up to 60 s and return 503 with Retry-After: 30 if a server does not start. Preview pricing is not charged.
- binding note: the one-time USD 25 credit stops creates first on the Free plan; the 5-sandbox and 1-hour timeout limits bound a single burst but do not end the plan
- interface detail: an E2B-compatible API, an anona-compute CLI with exec, connect, ssh, scp, preview and desktop commands, and an MCP server for agents
- endpoint: https://api.compute.anonalabs.com
- tooling: the stock E2B SDK pointed at compute.anonalabs.com with an e2b_ API key, the Anona SDK extras, the anona-compute binary installed with npm, or the MCP server
- composes with: a microVM that pauses and resumes with memory intact, so a long agent run can be suspended between turns and resumed without paying the running sandbox-hour or CPU and memory meters; a 2 vCPU and 4 GiB sandbox costs USD 0.284 per hour when the CPU is busy and about USD 0.048 per hour for a typical agent
- reliability: the Free plan has public internet egress off and a 1-hour longest timeout; creates are refused when the USD 25 credit is used up, and during the preview no card payments are taken and invoices are drafts
- notes: A hosted KVM microVM sandbox with an E2B-compatible API. The Free plan gives USD 25 of usage once with no card taken during the preview, 5 concurrent running sandboxes and a 1-hour timeout, and public internet egress is off; paid plans start at USD 20 a month with USD 20 of usage included. A 2 vCPU and 4 GiB sandbox is USD 0.284 per hour busy and about USD 0.048 per hour for a typical agent, and egress is USD 0.12 per GB. The public sign-in page shows an email field and email sign-in link, so the identity kind is email; a new account is by invitation and the waitlist.
- evidence note: the prices, rates, plan limits and sign-in flow are quoted from first-party documentation pages read on 2026-11-25; the prices are labelled preview by the vendor and no sandbox was created
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.note: a KVM microVM with its own kernel, filesystem and network policy; the example shape is 2 vCPU and 4 GiB
  - billing_model: usage in dollars spent at per-meter rates, included in a one-time credit or a monthly plan allowance
  - free_tier_kind: one-time credit
  - term: on demand, pause and resume with memory intact
  - price_arithmetic: USD 0.012 per running sandbox-hour plus USD 0.12 per active vCPU-hour plus USD 0.008 per GiB-hour resident memory; a 2 vCPU / 4 GiB busy sandbox is USD 0.284/h
  - derived: USD 0.012 + (2 x USD 0.12) + (4 x USD 0.008) = USD 0.284/h, matching the published busy example
  - network_out.allow_outbound: yes
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: no
  - session_cap.note: the Free plan longest timeout is 1 hour; paused sandboxes keep memory and cost only snapshot storage
- evidence:
  - [1] 2026-11-25: the Free plan is USD 0 a month with USD 25 of usage once and no card payments during the preview | capture: sha256:7cee11f076cf8525a0f771c112646676cf28981d4beb4715833fc14da9de9f7f | quote: Preview pricing.** These are the plans and rates the dashboard and metering use today. No card payments are taken during the preview
  - [1] 2026-11-25: the plan prices are USD 0, USD 20, USD 99 and USD 399 per month | capture: sha256:7cee11f076cf8525a0f771c112646676cf28981d4beb4715833fc14da9de9f7f | quote: | Price per month | \$0 | \$20 | \$99 | \$399 |
  - [1] 2026-11-25: the Free plan includes USD 25 of usage once, while paid plans include a monthly allowance | capture: sha256:7cee11f076cf8525a0f771c112646676cf28981d4beb4715833fc14da9de9f7f | quote: | Usage included | \$25 once | \$20 a month | \$110 a month | \$450 a month |
  - [1] 2026-11-25: a busy 2 vCPU / 4 GiB sandbox costs USD 0.284 per hour at the published meters | capture: sha256:7cee11f076cf8525a0f771c112646676cf28981d4beb4715833fc14da9de9f7f | quote: | Busy (CPU-bound work) | 2 active vCPU, 4 GiB | \$0.012 + \$0.24 + \$0.032 = \$0.284 |
  - [1] 2026-11-25: the running sandbox-hour rate is USD 0.012 and egress is USD 0.12 per GB | capture: sha256:7cee11f076cf8525a0f771c112646676cf28981d4beb4715833fc14da9de9f7f | quote: | Running sandbox-hour | \$0.012 |
  - [1] 2026-11-25: egress is USD 0.12 per GB | capture: sha256:7cee11f076cf8525a0f771c112646676cf28981d4beb4715833fc14da9de9f7f | quote: | Egress, GB | \$0.12 |
  - [1] 2026-11-25: creates are refused when the included usage runs out on the Free and Starter plans | capture: sha256:7cee11f076cf8525a0f771c112646676cf28981d4beb4715833fc14da9de9f7f | quote: Creates are refused
  - [2] 2026-11-25: public internet egress is off on the Free plan and the longest timeout is one hour | capture: sha256:579f947443aa824e3c90b1e28340b9ce66d1fd379b3329ee3b885be6e199c058 | quote: Public internet egress
  - [3] 2026-11-25: sign-in is a browser device flow in which the user picks an organization and approves | capture: sha256:eada59f1b065e1cc63e0679c4f5e9173efbb16fadb2706e51755ce29bce234da | quote: picks organization, approves
  - [3] 2026-11-25: the device-flow sign-in keeps the password and API key from the coding agent | capture: sha256:eada59f1b065e1cc63e0679c4f5e9173efbb16fadb2706e51755ce29bce234da | quote: The sign-in is a standard device flow (RFC 8628). The agent never sees your password or an API key.
  - [4] 2026-11-25: the public sign-in page asks for an email address and offers an email sign-in link, with Google and GitHub options; new access is by invitation | capture: sha256:49a6bd08eb330fcb9f05493960d1449b905cf3ef91419399ddfdaa1c7845177d | quote: <label for="email">Email</label>
  - [5] 2026-11-24: the four plan prices and that Free includes $25 of usage once | capture: sha256:7cee11f076cf8525a0f771c112646676cf28981d4beb4715833fc14da9de9f7f | quote: | Price per month | \$0 | \$20 | \$99 | \$399 | | Usage included | \$25 once | \$20 a month | \$110 a month | \$450 a month |
  - [5] 2026-11-24: the sandbox-hour, vCPU-hour, memory, snapshot storage and egress meter rates | capture: sha256:7cee11f076cf8525a0f771c112646676cf28981d4beb4715833fc14da9de9f7f | quote: | Running sandbox-hour | \$0.012 | | Active vCPU-hour | \$0.12 | | Resident memory, GiB-hour | \$0.008 | | Snapshot storage (paused sandboxes), GB-month | \$0.03 | | Egress, GB | \$0.12 |
  - [5] 2026-11-24: preview pricing is metered but no card payments are taken | capture: sha256:7cee11f076cf8525a0f771c112646676cf28981d4beb4715833fc14da9de9f7f | quote: No card payments are taken during the preview: usage is metered and shown in the dashboard, and invoices are drafts.
  - [6] 2026-11-24: the Free plan's concurrent sandbox count and one-hour timeout | capture: sha256:579f947443aa824e3c90b1e28340b9ce66d1fd379b3329ee3b885be6e199c058 | quote: | Running sandboxes at once | 5 | 20 | 100 | 500 | | Paused sandboxes kept | 5 | 50 | 200 | 800 | | Longest timeout | 1 hour | 24 hours | No maximum (`timeout=-1` allowed) | No maximum |
  - [7] 2026-11-24: the free plan has no public egress and paid plans allow it by default | capture: sha256:86435070572d46c9ce0899f80fc4dc0ec1ad0aa19346152ff3613c6e1244f69c | quote: 2. Your plan's limits. Paid plans allow the public internet by default; the free plan allows no public egress.
  - [8] 2026-11-24: sign-in requires an email magic link or GitHub, and the CLI uses a browser device flow | capture: sha256:de5d6c7adf61718ebef963ba3067b751d95bd2e3fe5791a03826b3d30a721eec | quote: | Sign in | Email magic link or GitHub |
  - [9] 2026-11-24: the REST gateway endpoint and that the API is E2B-compatible | capture: sha256:9d6bc084009817962097a55790197d89b6e4e77f06a63b711b6b7214d6ca70d2 | quote: | API | `https://api.compute.anonalabs.com`, the E2B-compatible gateway |
- sources:
  - [1] https://docs.anonalabs.com/compute/pricing
  - [2] https://docs.anonalabs.com/compute/concepts/limits
  - [3] https://docs.anonalabs.com/compute/agents/overview
  - [4] https://compute.anonalabs.com/
  - [5] https://docs.anonalabs.com/compute/pricing.md
  - [6] https://docs.anonalabs.com/compute/concepts/limits.md
  - [7] https://docs.anonalabs.com/compute/concepts/networking.md
  - [8] https://docs.anonalabs.com/compute/dashboard.md
  - [9] https://docs.anonalabs.com/compute/overview
