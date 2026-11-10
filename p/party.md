# Party

> party.build | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/party/ | JSON https://fshy.ajam.dev/api/v1/entity/party.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Party

- `compute/party` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-10-22T04:47:41.154Z (live) | stale on 2026-11-22
- url https://party.build
- free tier: $100 in credits, one time, with 2 concurrent active sessions and no card; the agent harness and model are chosen per agent | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: 'No card required', quoted from party.build read 2026-10-22
- interface: unknown
- limits:
  - request-rate (binding): $100 of credit, one time; 2 concurrent active sessions [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the credit, the concurrency cap and the no-card condition. The record's USD 100 was right and the two operational limits were missing
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 2 concurrent active sessions; the page states no wall-clock cap
  - free_tier_kind: one-time-credit
  - net.out: yes
  - net.in: no
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$100 in credits, one time' and '2 concurrent active sessions' with 'No card required' and 'Choose a harness and model for each agent. Use managed access or bring your team's own credentials and API keys', quoted
- sources:
  - [1] https://party.build
