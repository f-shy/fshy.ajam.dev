# Inferris

> inferris.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inferris/ | JSON https://fshy.ajam.dev/api/v1/entity/inferris.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Inferris

- `inference/inferris` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://inferris.ai/developers.md
- free tier: New accounts get USD 3.00 of credit at sign-up. After that usage is prepaid in the wallet; glm-5.3-flash is USD 0.09 per million input tokens. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign in at inferris.ai and open API keys; the signup credit is added on account creation
- interface: rest
- limits:
  - volume-quota (binding): USD 3.00 signup credit, then prepaid wallet [1]
- endpoint: https://api.inferris.ai/v1
- tooling: OpenAI Chat Completions, Responses and Anthropic Messages endpoints with an sk- key
- composes with: the one-off USD 3 signup credit binds before the prepaid wallet and per-token prices
- reliability: a 403 with insufficient_user_quota means the balance or key quota is used up; a 429 means rate limit or capacity; a Cloudflare edge block can appear as a plain-text 403 with an error code
- notes: the only free allowance is a one-off USD 3 signup credit, after which usage is prepaid
- evidence:
  - [1] 2026-11-18: new accounts receive USD 3 of signup credit; later usage is prepaid in the wallet | capture: sha256:8e183358ff36cc142e45c4f0a4266c69a4bcaf98aaeb38e7265f7f1e1dab0a8e | quote: New accounts get $3.00 of credit at sign-up. After that you prepay in Wallet (https://inferris.ai/wallet).
- sources:
  - [1] https://inferris.ai/developers.md
