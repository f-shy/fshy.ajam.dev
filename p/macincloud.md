# MacinCloud

> macincloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/macincloud/ | JSON https://fshy.ajam.dev/api/v1/entity/macincloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MacinCloud

- `compute/macincloud` | paid-only | evidence documented | binding write-gated | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-11-25T11:17:40.889Z (live) | stale on 2026-12-26
- url https://www.macincloud.com/pages/dedicated.html
- free tier: no free tier and no trial on dedicated plans: Mac hosting from $59 a month for the Intel package (macOS Sonoma, Intel 4-Core CPU, 8GB RAM, 120GB SSD storage), up to $165 a month for the M4 package (8/16GB RAM, 250GB SSD storage) | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: USD 59 to USD 165 per month depending on CPU, RAM and disk [1]
  - write-gated (binding): Dedicated Server Plans do not include a trial; the sign-up fields are not published on the dedicated page. [1]
- interface detail: RDP on the M4, M2 and M1 dedicated packages; a static IP address is included.
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
  - [1] 2026-11-25: the dedicated page lists an Intel 4-Core with 8GB RAM and 120GB SSD storage at $59/month | capture: sha256:0e89260d206a545fd07dbbe1f454ee77bbccdd35c7cc58ee49bbafdf43ef2e53 | quote: Intel macOS Sonoma, Intel 4-Core CPU, 8GB RAM, 120GB SSD Storage $59/month
  - [1] 2026-11-24: the current M4 dedicated plan price | capture: sha256:0e89260d206a545fd07dbbe1f454ee77bbccdd35c7cc58ee49bbafdf43ef2e53 | quote: $165/month
  - [1] 2026-11-24: the dedicated plans carry no trial | capture: sha256:0e89260d206a545fd07dbbe1f454ee77bbccdd35c7cc58ee49bbafdf43ef2e53 | quote: Trial: Dedicated Server Plans do not include a trial
  - [1] 2026-11-24: the M4 package includes RDP access | capture: sha256:0e89260d206a545fd07dbbe1f454ee77bbccdd35c7cc58ee49bbafdf43ef2e53 | quote: macOS Golden Gate/Tahoe, Silicon M4, 8/16GB RAM, 250GB SSD Storage, RDP
- sources:
  - [1] https://www.macincloud.com/pages/dedicated.html
