# Gologin Cloud Browser

> gologin.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gologin/ | JSON https://fshy.ajam.dev/api/v1/entity/gologin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gologin Cloud Browser

- `compute/gologin` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:43:13.247Z (live) | stale on 2026-12-05
- url https://gologin.com/cloud-browser/
- free tier: a free start with no card, browser hours billed flat with residential IPs included and $1 a GB past the traffic allowance; the first paid plan has no session-length cap | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Traffic is metered: each plan has a proxy traffic allowance and traffic past it is billed at USD 1 per GB; the allowance size per plan is not on the page read. | metered: yes | free allowance: a per-plan allowance, size not stated on the page read | source: [1]
- identity: email | detail: 'Sign up with Google and copy your key from the dashboard. Free, no card.', quoted from gologin.com read 2026-10-22
- interface: unknown
- limits:
  - per-ip-shaping (binding): traffic beyond the allowance is $1 a GB; residential IPs are included [1]
  - request-rate: browser hours bill flat per hour; the first paid plan has no session-length cap [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the cloud browser page was read on 2026-10-22 and states a free no-card start, the $1 a GB traffic rate and a no-limit session on the first paid plan. The record's paid-only verdict is contradicted by the free start
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no session cap on the first paid plan; the free start's cap is not published on this page
  - free_tier_kind: allowance
  - burst_x: 1.0
  - ps.price: profiles persist cookies, local storage and login state
  - ps.durability: saved profile
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until the profile is deleted
  - net.out: yes
  - net.in: no
  - net.ports: WebSocket connect endpoint
  - net.allowance: residential IPs included; $1 a GB past the allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Start free · Flat hourly · Residential IPs included · $1/GB after that' and 'Sign up with Google and copy your key from the dashboard. Free, no card.' and 'Longest session, first paid plan: No limit', quoted
  - [1] 2026-11-03: proxy traffic past the plan allowance is billed at $1 per GB | capture: sha256:2bc9dfc7997342ea80a539897c05f4ad0536b9c6243da3786b714c7eaed2ca12 | quote: proxy traffic past your allowance at $1/GB
- sources:
  - [1] https://gologin.com/cloud-browser/
