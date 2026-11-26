# boxd

> boxd.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boxd/ | JSON https://fshy.ajam.dev/api/v1/entity/boxd.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## boxd

- `compute/boxd` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T11:38:11.103Z (live) | stale on 2026-12-25
- url https://boxd.sh/pricing
- free tier: €30 of free credits to start; RAM is billed on use rather than on provisioned size, and machines suspend, resume and hibernate | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the rate card prices vCPU-hours, RAM and disk only and states no egress allowance or overage | metered: no | source: [1]
- identity: card | detail: a person signs in with GitHub or Google, then a new organization needs a payment method before its first machine; '€30 of credits when you add a payment method. Nothing is charged when you add the card'.
- interface: ssh, cli, rest
- limits:
  - request-rate (binding): €30 of credits at signup, one time [1]
- interface detail: SSH, the boxd CLI with --json output, and an API with API keys
- tooling: The hosted service is reached with the boxd CLI (--json output), the Python and TypeScript SDKs, SSH, each machine's HTTPS URL and the web console, or an API key; self-hosted last: the user installs and runs the boxd Rust binary on a rented or free machine.
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The credit is one-time and denominated in euro, so the unit is mixed
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.idle_reap_s: 14400
  - session_cap.restart_required: no
  - session_cap.note: a machine hibernates after 4 hours with no traffic; the timeout is configurable and 0 means off
  - persistent_storage.price_gib_month: disk bills on bytes written, not on provisioned size
  - persistent_storage.durability: suspend and hibernate keep the machine
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: not stated
  - free_tier_kind: one-time-credit
  - granularity.min_billed_s: 0
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Credit-based. RAM bills on what is in use and disk on what you have written to, not on what you provisioned. Start with €30 of free credits.' and 'Suspend, resume, and hibernate', quoted
  - [2] 2026-11-04: SSH access | capture: sha256:f2977ff6094b108ba94c023e412248af6fa14d826cfacc3d89bcb18583a9b3ca | quote: boxd gives developers and AI agents their own persistent Linux machines accessible via SSH.
  - [3] 2026-11-04: a CLI and an API exist | capture: sha256:6a586153d84017a98d02690b47ac917b63211d8fb724fa3118c462298b18e096 | quote: Drive all of it from the CLI, the API, or your CI job.
  - [1] 2026-11-04: the full rate card has three rows and no network row | capture: sha256:ac88294b02feeec834235d9bceaf5dc07020c0a6ca61b63a4a6e365ebf0fe0cd | quote: €0.039 per vCPU-hour, €0.012 per GiB-hour of RAM, and €0.00008 per GiB-hour of disk.
  - [1] 2026-11-04: the €30 credit is released by adding a payment method | capture: sha256:ac88294b02feeec834235d9bceaf5dc07020c0a6ca61b63a4a6e365ebf0fe0cd | quote: €30 of credits when you add a payment method.
  - [4] 2026-11-18:  | capture: sha256:056b9eea20750da17f0f781f2828b605c79107cb9f82c79929c59e9e247ffbb2 | quote: After 4 hours with no traffic a machine hibernates and pays for disk only, then wakes with its processes intact.
  - [2] 2026-11-24: the hosted service is driven by a CLI, SDKs, SSH and an HTTPS URL | capture: sha256:e95c5af76b8d5e9c7d7a5885ecb43b885255786cac0c5567b701c8565f82c085 | quote: You use boxd through the `boxd` CLI (`--json` gives machine-readable output), the Python SDK (`pip install boxd`) and the TypeScript SDK (`npm install @boxd-sh/sdk`), SSH into any machine, each machine's own HTTPS URL, and the web console at https://app.boxd.sh.
  - [1] 2026-11-24: a payment method is required to receive the EUR 30 credit and nothing is charged when it is added | capture: sha256:ac88294b02feeec834235d9bceaf5dc07020c0a6ca61b63a4a6e365ebf0fe0cd | quote: €30 of credits when you add a payment method. Nothing is charged when you add the card
  - [1] 2026-11-24: the per-second rate card is unchanged: EUR 0.039 per vCPU-hour, 0.012 per GiB-hour RAM, 0.00008 per GiB-hour disk | capture: sha256:ac88294b02feeec834235d9bceaf5dc07020c0a6ca61b63a4a6e365ebf0fe0cd | quote: €0.039 per vCPU-hour, €0.012 per GiB-hour of RAM, and €0.00008 per GiB-hour of disk.
  - [2] 2026-11-24: a payment method is required before the first machine and the credit arrives with it | capture: sha256:e95c5af76b8d5e9c7d7a5885ecb43b885255786cac0c5567b701c8565f82c085 | quote: A new organization also needs a payment method before its first machine: right after sign-in they are asked to connect one (nothing is charged, and the free credits arrive with it).
- sources:
  - [1] https://boxd.sh/pricing
  - [2] https://boxd.sh/llms.txt
  - [3] https://boxd.sh
  - [4] https://boxd.sh/
