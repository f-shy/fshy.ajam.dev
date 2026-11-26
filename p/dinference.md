# DInference

> dinference.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dinference/ | JSON https://fshy.ajam.dev/api/v1/entity/dinference.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DInference

- `inference/dinference` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://dinference.com
- free tier: No free allowance is stated on the apex page. OpenAI-compatible endpoints are priced up to 30% lower per token than OpenRouter; GLM-5.3-Flash is USD 0.084 per million input tokens. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create an account at panel.dinference.com; an OpenRouter route is listed as coming soon
- interface: rest
- limits:
  - volume-quota (binding): per-token pricing, for example GLM-5.3-Flash at USD 0.084 per million input tokens [1]
- endpoint: https://api.dinference.com/v1
- tooling: an OpenAI-compatible base URL; built-in provider on OpenCode and Kilo Code
- composes with: the per-token charge and the account signup are the scarce links; no free allowance is stated on the apex page
- reliability: zero-retention policy is stated; a 99.9% uptime SLA is claimed; high-volume usage of USD 1,000 a month or more uses a direct API form
- notes: no standing free inference allowance is stated on the apex page; endpoints are per-token paid and a signup is required
- evidence:
  - [1] 2026-11-18: the service offers OpenAI-compatible endpoints priced up to 30% below OpenRouter; no free allowance is stated on the apex page | capture: sha256:815d67aefe855839b97b2090ad97a95f4c73e6e5d92e6f5f9967a098f174bf1e | quote: Drop-in OpenAI-compatible endpoints, up to 30% lower cost per token.
- sources:
  - [1] https://dinference.com
