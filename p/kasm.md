# Kasm Workspaces

> kasm.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kasm/ | JSON https://fshy.ajam.dev/api/v1/entity/kasm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kasm Workspaces

- `compute/kasm-workspaces` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category dev environment
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:12.386Z (live) | stale on 2026-12-05
- url https://kasm.com/community-edition
- free tier: Community Edition is free for individuals and non-profit organisations, with 5 concurrent sessions | unit: users | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the Community Edition page lists no egress allowance and no overage price; Managed Egress is a separate feature marked For Purchase in the Enterprise column only | metered: no | source: [1]
- identity: email | detail: 'Individuals and non-profit organizations are free to use Kasm Workspaces Community Edition' with no account requirement stated; the licence is the gate, not an email
- interface: rest
- limits:
  - request-rate: 5 concurrent sessions on Community Edition [1]
  - write-gated (binding): the free edition is restricted to individuals and non-profit organisations [1]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: the Developer API, an HTTP API of POST endpoints under /api/public with an API key and secret (Community Edition includes it); the web console in the browser; the user installs and runs the server on a rented or free machine
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the Community Edition page was read on 2026-10-22 and states both the licence grant and the 5-session cap. The free product is self-hosted software, not hosted compute, and the record says so
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 5 concurrent sessions; the page states no wall-clock or idle cap
  - free_tier_kind: allowance
  - ps.price: a user supplies the storage
  - ps.durability: a user's own host
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: as long as a user's host exists
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Individuals and non-profit organizations are free to use Kasm Workspaces Community Edition for free' and '5 Concurrent Sessions' on the free edition, quoted
  - [1] 2026-11-03: the comparison table has a Managed Egress row that is a purchasable Enterprise feature; no bandwidth allowance or price appears | capture: sha256:e93aa062d5e6b84044d9a2707b051340150779d4e4ad201492a24f89918002ab | quote: Managed Egress
  - [2] 2026-11-03: the Developer API is a set of HTTP POST endpoints | capture: sha256:f04e166d2e9b2f1e7c498a893eb2bfc441f0831a86df9c36f111694a1e3122ef | quote: POST /api/public/create_user
  - [2] 2026-11-03: the API is for integration | capture: sha256:f04e166d2e9b2f1e7c498a893eb2bfc441f0831a86df9c36f111694a1e3122ef | quote: The Kasm Workspaces Developer API can be leveraged to extend the systems functionality and/or integrate with an exiting platform.
- sources:
  - [1] https://kasm.com/community-edition
  - [2] https://kasm.com/docs/latest/developers/developer_api/
