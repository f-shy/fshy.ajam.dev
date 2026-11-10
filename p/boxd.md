# boxd

> boxd.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boxd/ | JSON https://fshy.ajam.dev/api/v1/entity/boxd.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## boxd

- `compute/boxd` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:24:08.724Z (live) | stale on 2026-12-05
- url https://boxd.sh/pricing
- free tier: €30 of free credits to start; RAM is billed on use rather than on provisioned size, and machines suspend, resume and hibernate | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the rate card prices vCPU-hours, RAM and disk only and states no egress allowance or overage | metered: no | source: [1]
- identity: card | detail: a payment method is added to receive the €30 of credits; the page states nothing is charged when it is added
- interface: ssh, cli, rest
- limits:
  - request-rate (binding): €30 of credits at signup, one time [1]
- interface detail: SSH, the boxd CLI with --json output, and an API with API keys
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The credit is one-time and denominated in euro, so the unit is mixed
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: suspend, resume and hibernate are offered; the page states no automatic reap interval
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
- sources:
  - [1] https://boxd.sh/pricing
  - [2] https://boxd.sh/llms.txt
  - [3] https://boxd.sh
