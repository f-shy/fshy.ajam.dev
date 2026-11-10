# Riza Code Interpreter

> riza.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/riza/ | JSON https://fshy.ajam.dev/api/v1/entity/riza.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Riza Code Interpreter

- `compute/riza` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:16.351Z (live) | stale on 2026-12-05
- url https://riza.io/pricing
- free tier: an execution runtime with hard per-invocation caps: 30 seconds, 128 MiB of memory, HTTP-only network access and one interpreter version | unit: seconds | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - request-rate (binding): execution is capped at 30 seconds per invocation [1]
  - per-object-cap: 128 MiB of memory per invocation [1]
  - per-ip-shaping: network access is limited to HTTP; no raw sockets, so no non-HTTP protocol [1]
- interface detail: HTTPS REST API at api.riza.io with Python, Node and Go SDKs; no CLI or SSH
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and its limits section states the four caps that decide usability. The page publishes no price or free allowance in the extracted body, so the free-tier field keeps its earlier source
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.ram: 0.125
  - shape.note: 128 MiB of memory per invocation
  - session_cap.wall_clock_min: 0.5
  - session_cap.restart_required: no
  - session_cap.note: 30 seconds per invocation, a hard cap rather than a reap
  - free_tier_kind: allowance
  - net.out: yes
  - net.in: no
  - net.ports: HTTP only
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Execution time is limited to 30 seconds per invocation', 'Memory consumption is limited to 128Mib per invocation', 'Network access is limited to HTTP' and 'No support for alternative interpreter versions', quoted
  - [2] 2026-11-03: the service is reached through a REST API | capture: sha256:e76dbdab1488b4a524964e4df57e6d7fed44ab6b309ed23cdaaed2710eef77e1 | quote: The Riza API accepts HTTPS requests at `api.riza.io`.
  - [1] 2026-11-03: the page states a network restriction and no egress allowance or egress price | capture: sha256:413b32ab1864b6ceb8d779a2c29ea9fbe859743cb52dec44d92b50f1a57bfc8a | quote: Network access is limited to HTTP.
- sources:
  - [1] https://riza.io/pricing
  - [2] https://docs.riza.io/api-reference/introduction
