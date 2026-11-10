# AgentComputer

> agentcomputer.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/agentcomputer/ | JSON https://fshy.ajam.dev/api/v1/entity/agentcomputer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AgentComputer

- `compute/agentcomputer` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:45:39.847Z (live) | stale on 2026-11-22
- url https://agentcomputer.ai/pricing
- free tier: no free tier: pay-as-you-go at $0.07 a CPU-hour, $0.04375 a GB-hour of memory, and storage at $0.000683 a GB-hour running or $0.000027 stopped | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $0.07 a CPU-hour and $0.04375 a GB-hour of memory while the machine runs [1]
  - retention-clamped: storage is billed at $0.000683 a GB-hour running and $0.000027 stopped, so a stopped machine still costs 4% of its running storage rate [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes a full usage ladder with no free tier. The record claimed a free tier from the card, which the page contradicts, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the page prices a stopped state separately, so stopping is supported and is not a reap
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.price: $0.000683 a GiB-hour running, $0.000027 stopped
  - ps.durability: billed storage in both states
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the storage is billed
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'CPU Time $0.07 per CPU-hour · Memory $0.04375 per GB-hour · Hot Storage $0.000683 per GB-hour (running) · Cold Storage $0.000027 per GB-hour (stopped)', quoted; the page publishes no free tier
- sources:
  - [1] https://agentcomputer.ai/pricing
