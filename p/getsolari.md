# Solari

> getsolari.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getsolari/ | JSON https://fshy.ajam.dev/api/v1/entity/getsolari.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Solari

- `compute/solari` | qualifies-with-caveat | evidence documented | binding retention-clamped | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:18.816Z (live) | stale on 2026-12-05
- url https://docs.getsolari.com/pricing
- free tier: $3 of credits a month on a $0 plan, sessions capped at 1 hour, 3 concurrent browsers, 3 profiles and 1 day of replay retention | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page (https://docs.getsolari.com/pricing) lists credits, hourly rate, session time, concurrency and replay retention, and no transfer allowance or per-GB price; a hardened sandbox has no outbound network at all | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - request-rate: $3 of monthly credits on Free, drawn at $0.15 an hour [1]
  - retention-clamped (binding): a free session is capped at 1 hour and replay is kept 1 day [1]
  - request-rate: 3 concurrent browsers and 3 profiles on Free; human-verification handling and proxies are not available [1]
- interface detail: HTTP API (api.getsolari.com) and SDKs for TypeScript, Python, Go, Rust and C++; VMs are also viewed and controlled over VNC; no CLI or SSH found in the docs read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The pricing page read on 2026-10-22 documents tier pricing, the 1-hour session cap on the Free tier, and replay retention periods.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.note: a VM adds $0.02 an hour for the live screen and bills per vCPU-hour at $0.0525 on Free
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: no
  - session_cap.note: a hard 1-hour maximum session time on Free, 5 hours on Starter and 24 on Professional
  - free_tier_kind: recurring-credit
  - burst_x: 1.0
  - ps.price: profiles and replay storage are capped per plan
  - ps.durability: profile and replay
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: 1 day of replay on Free
  - net.out: yes
  - net.in: no
  - net.static_ip: no
  - net.allowance: proxies are not available on the free tier
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '| Monthly fee | $0 | $20 | $200 | Custom |' with '| Monthly credits | $3 | $20 | $200 | Custom |', '| Max session time | 1 hour | 5 hours | 24 hours | Unlimited |', '| Rate | $0.15 / hour', '| Concurrent browsers | 3', and 'Replay retention 1 day' on Free, quoted
  - [1] 2026-11-03: the plan table prices hours and sessions; no transfer allowance or per-GB price in it | capture: sha256:cfa41effcf4cbd6c48ffd4f8d1c774a5e148d53cd58ee63096f4bc17d8beb2b4 | quote: | Rate | $0.15 / hour | $0.10 / hour | $0.07 / hour | $0.05 / hour | $0.005 / hour |
  - [2] 2026-11-03: a REST HTTP API is documented | capture: sha256:f77ce8c5d0fc97013858b054d44e4f3c330f0591f046a2d2ffa3cf25376d22af | quote: The raw HTTP surface: every endpoint, every status code, every body shape, callable with `curl` or any HTTP client.
  - [3] 2026-11-03: SDKs exist in several languages | capture: sha256:b811b079f2992f43de140ed113e6c1bb2d865345627b24ae79d807f939f64274 | quote: TypeScript and Python are at full parity
- sources:
  - [1] https://docs.getsolari.com/pricing
  - [2] https://docs.getsolari.com/api-reference
  - [3] https://docs.getsolari.com/languages
