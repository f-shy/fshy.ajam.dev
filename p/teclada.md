# Teclada

> teclada.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/teclada/ | JSON https://fshy.ajam.dev/api/v1/entity/teclada.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Teclada

- `compute/teclada` | qualifies-with-caveat | evidence documented | binding write-gated | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:18.388Z (live) | stale on 2026-12-05
- url https://www.teclada.com/
- free tier: a Free tier; paid plans are $100 a month and $500 a month | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://www.teclada.com/ lists plans by history days, systems and users and states no egress allowance or overage price | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding):  [1]
- interface detail: console only: a browser-based terminal (SSH client in the browser); the pages read state no REST API, CLI or SDK
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing table was read on 2026-10-22 and lists a Free plan. The record carried paid-only, which the page contradicts
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no session cap published; the product is a browser-based SSH client, so the server is a user's own
  - free_tier_kind: allowance
  - reclassified_from: dead
  - net.out: yes
  - net.in: no
  - net.ports: works without open ports or a static IP: the connection is outbound from the server
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free' in the plan table beside '$100/month' and '$500/month', and 'Worry-free 30 day money back guarantee', quoted
  - [1] 2026-11-03: the page describes no network cost; the plan list carries no egress line | capture: sha256:38b8e9e5f8c287424da5680765776759f55d6d03aa140630fa4fb851ff6d3f76 | quote: Teclada's turn-key platform works on any network without requiring your servers to have a static IP or custom firewall rules.
  - [1] 2026-11-03: access is through a browser | capture: sha256:38b8e9e5f8c287424da5680765776759f55d6d03aa140630fa4fb851ff6d3f76 | quote: Getting work done with Teclada is easy because all you need to get connected is a web browser.
- sources:
  - [1] https://www.teclada.com/
