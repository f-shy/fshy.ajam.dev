# AIGROW

> aigrow.gg | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aigrow/ | JSON https://fshy.ajam.dev/api/v1/entity/aigrow.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AIGROW

- `inference/aigrow` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://aigrow.gg/ai-api/guide
- free tier: No standing free tier is stated; API credit is bought in packs or plans. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a dashboard account with any email address, then redeem a code or buy a credit pack
- interface: rest
- limits:
  - volume-quota (binding): prepaid API credit packs and plans; no free allowance is published [2]
- endpoint: https://aigrow.gg/v1
- tooling: an OpenAI- or Anthropic-compatible base URL with an ag_ key; no vendor SDK to install
- composes with: the discount API credit pack is the scarce link; no free allowance is published
- reliability: an unknown model or dated id is rejected with 404 before forwarding and is not billed; a 429 carries a retry-after header
- notes: no free inference allowance is published; the price page sells discounted credit packs and plans
- evidence:
  - [1] 2026-11-18: the endpoint is OpenAI- and Anthropic-compatible; API credit is bought in packs, with no standing free allowance stated | capture: sha256:5b64b1e9671d4707fbaad9ce4335ed9141655f0c0efec000480b877353f0293e | quote: The AIGROW API endpoint is a drop-in replacement for the OpenAI and Anthropic APIs.
- sources:
  - [1] https://aigrow.gg/ai-api/guide
  - [2] https://aigrow.gg/ai-api
