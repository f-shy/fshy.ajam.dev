# YepCode Run

> yepcode.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yepcode/ | JSON https://fshy.ajam.dev/api/v1/entity/yepcode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## YepCode Run

- `compute/yepcode` | qualifies-with-caveat | evidence documented | binding request-rate | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:26.169Z (live) | stale on 2026-12-05
- url https://yepcode.io/pricing/
- free tier: 50,000 Yeps, which are seconds of execution time, with 300 executions a day, a 30-second cap per execution, 1 concurrent execution, 5 storage files of 5 MB each and 5 MB of local disk | unit: seconds | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page meters execution seconds (Yeps) and lists no egress allowance or overage price; docs.yepcode.io states none | metered: no | source: [1]
- identity: email | detail: 'FREE, no credit card required', quoted from yepcode.io/pricing read 2026-10-22
- interface: rest
- limits:
  - request-rate (binding): 50,000 seconds of execution time on Free, with 300 executions a day and 1 concurrent execution [1]
  - request-rate (binding): a single execution is capped at 30 seconds on Free, 1 hour on the paid tier [1]
  - per-object-cap: 5 storage files at 5 MB each and 5 MB of local disk on Free [1]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: REST API at https://cloud.yepcode.io/api/{team}/rest (schedules, executions); also webhooks and cron schedules; no CLI, SSH or SDK read on the pages
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the free tier in Yeps, which the page defines as seconds of execution time, plus five separate caps. That is the most complete free-tier statement in the tail
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.disk: 0.005
  - shape.note: 'Sandboxes with limited CPU and memory' and 5 MB of local disk, with no figure for CPU
  - session_cap.wall_clock_min: 0.5
  - session_cap.restart_required: no
  - session_cap.note: 30 seconds per execution on Free, 1 hour on the paid tier; 50,000 seconds in total a month
  - free_tier_kind: allowance
  - ps.gib: 0.005
  - ps.price: 5 storage files at 5 MB each on Free
  - ps.durability: storage files and local disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the account exists
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'FREE, no credit card required' with 'Includes 50K Yeps (seconds of execution time)', 'Max 300 executions per day', 'Max 30 seconds execution time', 'Max 1 concurrent execution', 'Up to 5 storage files (5Mb max per file)' and '5Mb local disk space', quoted
  - [1] 2026-11-03: the free plan includes the REST API | capture: sha256:90ba6ebd94f612a5d09e678fa8e827b5911ee3cb2b042a1915b46f378c2508c9 | quote: - YepCode Rest API
  - [1] 2026-11-03: usage is metered in Yeps (seconds), not bytes | capture: sha256:90ba6ebd94f612a5d09e678fa8e827b5911ee3cb2b042a1915b46f378c2508c9 | quote: - Includes 50K Yeps (seconds of execution time)
- sources:
  - [1] https://yepcode.io/pricing/
