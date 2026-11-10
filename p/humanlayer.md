# HumanLayer

> humanlayer.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/humanlayer/ | JSON https://fshy.ajam.dev/api/v1/entity/humanlayer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HumanLayer

- `compute/humanlayer` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:08.888Z (live) | stale on 2026-11-22
- url https://humanlayer.com
- free tier: Free for small teams with up to 200 sessions a month; a local daemon runs sessions on the user's own machine. | unit: objects | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): up to 200 sessions a month on the free tier [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the free tier's 200-session bound and that a local daemon is the default execution path. The unit is a session count, not a second
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 200 sessions a month; the compute is a user's own laptop unless a cloud daemon is started
  - free_tier_kind: allowance
  - ps.price: a user's own storage
  - ps.durability: a user's own machine, or a cloud daemon
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: as long as the task exists
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free for small teams' with 'Up to 200 sessions / month', and 'A local daemon runs many Agent sessions in parallel on your laptop. Spin up cloud daemons for long-running work.' quoted
- sources:
  - [1] https://humanlayer.com
