# MacStadium

> macstadium.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/macstadium/ | JSON https://fshy.ajam.dev/api/v1/entity/macstadium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MacStadium

- `compute/macstadium` | paid-only | evidence documented | binding write-gated | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:20.427Z (live) | stale on 2026-11-22
- url https://www.macstadium.com/pricing
- free tier: no free tier: Mac hosting on fixed monthly or annual billing with unlimited bandwidth, purchased through a portal account | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: fixed monthly or annual billing with no published entry price on this page [1]
  - per-ip-shaping: 'Unlimited bandwidth', a claim about a missing limit rather than a number [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and describes fixed monthly or annual billing with no free tier. The record's free-tier claim is contradicted
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.gpu_class: Apple Silicon
  - shape.gpu_count: 1
  - shape.note: standard configurations, width not stated on this page
  - session_cap.restart_required: no
  - session_cap.note: a dedicated or hosted Mac on a monthly term; no session clock
  - free_tier_kind: none
  - granularity.min_billed_s: 2592000
  - ps.price: included in the monthly term
  - ps.durability: dedicated storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
  - net.allowance: unlimited bandwidth
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Unlimited bandwidth' and 'predictable, fixed monthly or annual billing' with 'Sign-up online', and a FAQ entry 'Do you offer free trials on individual hosted Macs?', quoted
- sources:
  - [1] https://www.macstadium.com/pricing
