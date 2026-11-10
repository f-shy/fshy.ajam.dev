# Agent Relay

> agentrelay.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/agentrelay/ | JSON https://fshy.ajam.dev/api/v1/entity/agentrelay.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Agent Relay

- `compute/agent-relay` | qualifies-with-caveat | evidence documented | binding request-rate | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:26.172Z (live) | stale on 2026-12-05
- url https://agentrelay.com
- free tier: free to start and free to connect agents, with no paid tier priced on the page | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the home page and the getting-started page state no egress allowance or price, and the /pricing path was not found | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - request-rate (binding): no metered limit is published; the free tier is a message relay between agents, not a machine to run code on [1]
- interface detail: agent-relay CLI run through npx (Node.js 22 or later); no REST API, SSH or SDK read; no pricing page was found at /pricing
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22. It offers a free tier and publishes no paid price, which contradicts the record's paid-only verdict. The product relays messages between agents rather than renting compute, so the free tier is not usable capacity and the caveat says so
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the unit is a message handoff between agents; there is no session to reap
  - free_tier_kind: allowance
  - reclassified_from: dead
  - net.out: yes
  - net.in: no
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Sign up and go. Free to start.' and 'Connect your agents for free' with 'Sign up for free', quoted; the page prices nothing above free
  - [2] 2026-11-03: a CLI exists | capture: sha256:523380596f0f148350e8ee31e22e8339bb8af99afc2e8f6e84c01b243d2078f4 | quote: Connect your agents with the CLI: try Agent Relay on one machine or set up a shared workspace for your team.
- sources:
  - [1] https://agentrelay.com
  - [2] https://agentrelay.com/docs/getting-started
