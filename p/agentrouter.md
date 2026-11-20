# AgentRouter

> agentrouter.org | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/agentrouter/ | JSON https://fshy.ajam.dev/api/v1/entity/agentrouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AgentRouter

- `inference/agentrouter` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://pro.agentrouter.org/docs/wallet
- free tier: New users automatically receive a $1.00 welcome bonus after registration; after that each API call deducts its cost from a prepaid wallet (pay-as-you-go). | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: email or GitHub/Google registration; a $1.00 welcome bonus is granted at registration
- interface: rest
- limits:
  - volume-quota (binding): $1.00 one-time welcome credit; per-token wallet deduction thereafter [1]
- endpoint: https://agentrouter.org/v1
- tooling: an OpenAI-compatible or Anthropic-compatible key (sk-ar- prefix) against the wallet-backed gateway
- composes with: the non-expiring one-dollar welcome credit is the only free allowance, spent per token afterward
- reliability: the free allowance is finite and one-time; top-ups are needed after it is spent
- evidence:
  - [1] 2026-11-18: new users get a $1.00 welcome bonus at registration | capture: sha256:38f10c2e4efa88289e9c56cda02509b0ba7ea1a9f1c425ec6a55f5e7789b5a65 | quote: New users automatically receive a $1.00 welcome bonus after registration
- sources:
  - [1] https://pro.agentrouter.org/docs/wallet
