# meraGPT

> meragpt.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/meragpt/ | JSON https://fshy.ajam.dev/api/v1/entity/meragpt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## meraGPT

- `inference/meragpt` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://meragpt.com/pricing
- free tier: USD 1 free credit for the first week, then prepaid credit from USD 0.04 per 1M tokens, with no subscription. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: signup at the login page; the page states no card requirement
- interface: rest
- limits:
  - volume-quota (binding): USD 1 free credit for the first week [1]
- endpoint: https://meragpt.com/v1
- tooling: an OpenAI-compatible base URL with a prepaid balance
- composes with: the first-week credit is the scarce link; prepaid top-up is the only continuation
- reliability: prepaid credit with no published rate limit
- evidence:
  - [1] 2026-11-18: a new account gets USD 1 free credit for its first week and later usage is prepaid from USD 0.04 per 1M tokens | capture: sha256:b4b44dbf5db3f6b3017a9f547d470919af1e21ceefb213a4c98244bb12a4662f | quote: [$1 free credit for your first week](https://meragpt.com/login?signup=true) · from $0.04 / 1M tokens · prepaid credit, no subscription
- sources:
  - [1] https://meragpt.com/pricing
