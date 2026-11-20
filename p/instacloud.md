# InsForge

> instacloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/instacloud/ | JSON https://fshy.ajam.dev/api/v1/entity/instacloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## InsForge (InstaCloud)

- `compute/insforge-instacloud` | qualifies-with-caveat | evidence documented | binding request-rate | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:32.967Z (live) | stale on 2026-12-05
- url https://www.instacloud.com/pricing
- free tier: $10 of usage credit a month that refreshes, with up to 4 vCPU, 4 GB of RAM and 1 GB of volume per service; a project pauses when the credit runs out and resumes next cycle | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: egress is priced at USD 0.05 per GB as a usage cost; no free egress allowance is listed on the pricing page | metered: yes | price per TB: USD 50 per TB | source: [1]
- identity: email
- interface: cli, rest
- limits:
  - request-rate (binding): $10 of usage credit a month, refreshing; $0.00000772 a vCPU-second [1]
  - per-object-cap: up to 4 vCPU, 4 GB of RAM and 1 GB of volume per service [1]
  - retention-clamped: a project pauses when the credit runs out and resumes in the next cycle, so exhaustion is a pause rather than a delete [1]
- interface detail: the insta CLI (interactive login or an API token) and the InstaCloud REST API authenticated with an insta_ token
- tooling: the insta CLI, which a coding agent can also drive
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the monthly credit, the per-service caps and the pause-on-exhaustion behaviour. The credit recurs, which makes it a tier, and the pause is the state answer
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 4
  - shape.ram: 4
  - shape.disk: 1
  - shape.note: the ceiling per service on the free tier
  - session_cap.restart_required: no
  - session_cap.note: billed only on active CPU and memory; a project pauses on exhaustion and resumes next cycle
  - free_tier_kind: recurring-credit
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.gib: 1
  - ps.price: $0.000000057833 a GB-second of volume, $0.000000005783 a GB-second of object storage
  - ps.durability: volume and object storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$10 of usage credit per month. Refreshes every month' with 'Up to 4 vCPU / 4 GB RAM / 1 GB volume per service', 'Projects pause when credit runs out, and resume next cycle', and '$0.00000772 per vCPU/sec', quoted
  - [1] 2026-11-03: egress is priced at $0.05 per GB | capture: sha256:9813aed5a2c5cb4b87f7c7c70dacd635dc3ecd2e4e33b7946509739b451800a5 | quote: Egress $0.05 per GB
  - [2] 2026-11-03: a CLI manages services | capture: sha256:ecc89f4c6e79d3fc2dcf56c57db235e4c2143d22b555122c43c417a17558770d | quote: The `insta` CLI manages projects, branches, services, secrets, and deploys from a terminal
  - [3] 2026-11-03: a REST API exists | capture: sha256:060a35f1e487bf5ab156c66cf117d3afea67c5637e0715bd65a1f90abd26888a | quote: Authenticate to the InstaCloud REST API with an insta_ token
- sources:
  - [1] https://www.instacloud.com/pricing
  - [2] https://docs.instacloud.com/reference/cli/overview.md
  - [3] https://docs.instacloud.com/llms.txt
