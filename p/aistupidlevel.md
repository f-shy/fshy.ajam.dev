# AI Stupid Level

> aistupidlevel.info | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aistupidlevel/ | JSON https://fshy.ajam.dev/api/v1/entity/aistupidlevel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AI Stupid Level

- `inference/aistupidlevel` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference router
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://aistupidlevel.info
- free tier: Free plan at USD 0 forever with no card required: 1,000 Smart Router requests a month, Data API at 10 requests a day, 3 tracked models and 30 days of history. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a free account with no card; signup is through the auth/signup page
- interface: rest
- limits:
  - volume-quota (binding): Smart Router 1,000 requests a month on Free; Data API 10 requests a day [1]
- endpoint: https://aistupidlevel.info/v1
- tooling: an OpenAI-compatible base URL and an aism_ router key; the Smart Router also speaks Anthropic /v1/messages
- composes with: the 1,000 routed requests a month is the scarce link, and the caller must supply their own provider keys
- reliability: the router bills tokens directly to the caller at the upstream list price with zero markup; a circuit opens after five straight failures and probes again after 60 seconds
- notes: the free tier grants routed requests but the caller must hold OpenAI, Anthropic, Google, DeepSeek, Moonshot and Z.ai keys, so inference tokens are not free
- evidence:
  - [1] 2026-11-18: the free plan includes 1,000 Smart Router requests a month and 10 Data API requests a day, with no card required | capture: sha256:4a1f6b2238ed42bcd3833b8b37090fe12f0ccbdbb5fed952546223f8050fed67 | quote: - Smart Router: 1,000 requests a month - Data API: 10 requests a day
- sources:
  - [1] https://aistupidlevel.info
