# Molted

> molted.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/molted/ | JSON https://fshy.ajam.dev/api/v1/entity/molted.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Molted

- `compute/molted` | paid-only | evidence documented | binding volume-quota | category hosted agent sandbox | tier Small (always-on agent)
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T01:20:00.639Z (live) | stale on 2026-12-26
- url https://www.molted.net/pricing
- free tier: No free tier: the Service is prepaid, credit is bought by card and there is no free trial. The first Small or Large instance running Mue receives a one-time promotional credit worth 5 days of its running price. Mue on Small or Large credits the first 5 days of hosting to the wallet. | unit: none | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The 5-day credit is a one-time new-account promotion, not a recurring allowance, and requires buying credit by card. Mue must be chosen on Small or Large.
- per-object cap: not applicable: the unit is a machine, not an object; the Small size has 5 GB of NVMe storage and a versioned workspace with a file explorer | source: [2]
- retention: An agent whose balance stays at zero or below for 3 days is stopped, not deleted, and restarts after adding credit; instances keep being charged while they exist. Deleting the agent ends the charge. | source: [1]
- egress: $0 network fees, in or out; a public HTTPS address is included with every agent | metered: no | source: [2]
- identity: card | detail: The Terms require email confirmation and state that credit is bought by card through Stripe with no free trial.
- interface: ssh, rest, browser, cli
- limits:
  - volume-quota (binding): Small $2.88 per month, billed by the day and prorated to the time the agent exists; stopped workspace about 10x cheaper; $0 once the agent is deleted [2]
  - per-object-cap: Small: up to 1.5 vCPU, up to 1.5 GB RAM, 5 GB NVMe storage [2]
- limits note: Billing is prepaid by card; when the balance reaches zero, tools stop, and after 3 days at zero or below instances are stopped but keep being charged until deleted.
- binding note: The prepaid balance and the $2.88 a month running price are what run out first; the 5 GB disk and 1.5 GB RAM of the Small tier cap a job before any count-based limit does.
- interface detail: A terminal in the browser, SSH access, the API and a public HTTPS address for every agent.
- tooling: Console, SSH, API and a public HTTPS address; the instance runs the vendor's agent runtime with automatic repair and a versioned workspace.
- composes with: An always-on hosted agent with its own public HTTPS URL; a job that must survive instance deletion needs its output copied to a separate object-storage record.
- reliability: No service level applies unless a separate signed agreement says so; tools stop when prepaid credit reaches zero, and instances are stopped after 3 days at zero or below.
- notes: Paid-only: a card buys prepaid credit and there is no recurring free allowance. Hosted, always-on agent runtime, not software the user installs.
- evidence note: The price, included resources, no-fee egress and signup fields come from the vendor's pricing and signup pages read 2026-11-25; the prepaid card requirement, the one-time 5-day credit and the stop behaviour come from the vendor's terms page read the same day.
- extras:
  - shape.vcpu: 1.5
  - shape.ram_gib: 1.5
  - shape.disk_gib: 5
  - shape.note: up to 1.5 vCPU and 1.5 GB RAM with 5 GB NVMe on the Small tier
  - billing_model: prepaid credit, by the day, prorated to agent lifetime
  - free_tier_kind: one-time promotional credit
  - term: monthly, no commitment
  - price_arithmetic: Small $2.88 per month; no network fees in or out; $0 once the agent is deleted
  - status: live
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: a public HTTPS address for every agent
  - session_cap.restart_required: no
  - session_cap.note: always on until the balance runs out; after 3 days at zero or below the instance is stopped but keeps being charged until deleted
- evidence:
  - [2] 2026-11-25: the Small tier is $2.88 per month | capture: sha256:b48ecb795ec182caa608f0c6f4830dcadf3f32c26ff8476b34d59fde2ebac158 | quote: Small $2.88per month
  - [2] 2026-11-25: the Small tier has 5 GB of NVMe storage | capture: sha256:b48ecb795ec182caa608f0c6f4830dcadf3f32c26ff8476b34d59fde2ebac158 | quote: 5 GB of NVMe storage
  - [2] 2026-11-25: no network fees are charged in or out | capture: sha256:b48ecb795ec182caa608f0c6f4830dcadf3f32c26ff8476b34d59fde2ebac158 | quote: $0 network fees, in or out
  - [2] 2026-11-25: each agent has a browser console, SSH, the API and a public HTTPS address | capture: sha256:b48ecb795ec182caa608f0c6f4830dcadf3f32c26ff8476b34d59fde2ebac158 | quote: Console, SSH, API and URL
  - [2] 2026-11-25: Mue on Small or Large credits the first five days of hosting to the wallet | capture: sha256:b48ecb795ec182caa608f0c6f4830dcadf3f32c26ff8476b34d59fde2ebac158 | quote: Choose Mue on Small or Large and your first 5 days are credited to your wallet
  - [1] 2026-11-25: the service is prepaid by card through Stripe and has no free trial | capture: sha256:8c2d9a8514888f49957a244b305d6260cf4ae53bf53a5fcde253ae28df173350 | quote: The Service is prepaid. You buy credit by card, and a balance is kept on your account. There is no free trial. Card payments are processed by Stripe.
  - [1] 2026-11-25: registration requires confirming an email address and keeping sign-in methods secure | capture: sha256:8c2d9a8514888f49957a244b305d6260cf4ae53bf53a5fcde253ae28df173350 | quote: You must give accurate information, confirm your email address and keep your sign-in methods (passkeys and email) secure.
  - [3] 2026-11-25: the signup form asks for a work email, organization, name, website and region | capture: sha256:1b275b54e57fc5f51499e0bdc5feb1ab5219d423940fbfb54cf08e6208aad74c | quote: Work email
  - probe:https://molted.dev/ 2026-11-25: the live site is molted.net | capture: sha256:8b98e91d8dd1c81fcd036cc4b295109d42acde0a4df9140db90ed86963179e55 | quote: "status": null
  - [2] 2026-11-24: the 5-day free hosting credit is a Mue-only trial on Small or Large, once per account, excluding XLarge and other runtimes | capture: sha256:2e964b9ecdd5c83ff97b8b50248a84f6599195b1dcba961285afedf9b801f39c | quote: Pick Mue as your runtime on a Small or Large instance and your first 5 days of hosting are credited to your wallet, once per account. The offer is for Mue only and does not apply to XLarge. OpenClaw and Hermes are billed from the first day, prorated.
  - [2] 2026-11-24: network traffic is not billed in or out | capture: sha256:2e964b9ecdd5c83ff97b8b50248a84f6599195b1dcba961285afedf9b801f39c | quote: $0 network fees, in or out
  - [2] 2026-11-24: the paid always-on Large instance costs USD 5.25 a month | capture: sha256:2e964b9ecdd5c83ff97b8b50248a84f6599195b1dcba961285afedf9b801f39c | quote: $5.25 per month
  - [3] 2026-11-24: account creation asks for a work email and names, with no card, phone or ID field on the signup page | capture: sha256:1b275b54e57fc5f51499e0bdc5feb1ab5219d423940fbfb54cf08e6208aad74c | quote: Create your account
  - [3] 2026-11-24: the signup form asks for a work email | capture: sha256:1b275b54e57fc5f51499e0bdc5feb1ab5219d423940fbfb54cf08e6208aad74c | quote: Work email
- sources:
  - [1] https://www.molted.net/legal/terms
  - [2] https://www.molted.net/pricing
  - [3] https://www.molted.net/signup
