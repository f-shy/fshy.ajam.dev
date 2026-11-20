# MacinCloud

> macincloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/macincloud/ | JSON https://fshy.ajam.dev/api/v1/entity/macincloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MacinCloud

- `compute/macincloud` | paid-only | evidence documented | binding write-gated | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:20.656Z (live) | stale on 2026-11-22
- url https://www.macincloud.com/pages/dedicated.html
- free tier: no free tier and no trial on dedicated plans: Mac hosting from $59 a month for a 4-core Intel with 8 GB and 120 GB, up to $164 for an M4 with 16 GB and 250 GB | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: $59 to $164 a month depending on CPU, RAM and disk [1]
  - write-gated (binding): 'Dedicated Server Plans do not include a trial', quoted; a card is the only route in [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the dedicated server page was read on 2026-10-22 and prices four configurations. It states in as many words that dedicated plans carry no trial, which is the strongest form of the record's claim
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.vcpu: 4
  - shape.ram: 8
  - shape.disk: 120
  - shape.gpu_class: Intel or Apple Silicon
  - shape.gpu_count: 1
  - shape.note: the entry configuration is a 4-core Intel with 8 GB and 120 GB; the top is an M4 with 16 GB and 250 GB
  - session_cap.restart_required: no
  - session_cap.note: a monthly dedicated Mac; no session clock
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - ps.gib: 120
  - ps.price: included, customisable size
  - ps.durability: SSD
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
  - net.out: yes
  - net.in: yes
  - net.ports: RDP on some configurations
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$164/month' for macOS Sequoia or Tahoe on an M4 with 16 GB and 250 GB, down to '$59/month' for macOS Sonoma on a 4-core Intel with 8 GB and 120 GB, and 'Trial: Dedicated Server Plans do not include a trial', quoted
- sources:
  - [1] https://www.macincloud.com/pages/dedicated.html
