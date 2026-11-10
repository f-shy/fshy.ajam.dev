# Coze

> coze.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coze/ | JSON https://fshy.ajam.dev/api/v1/entity/coze.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Coze

- `inference/coze` | trial-only | evidence documented | binding volume-quota | category agent platform API, one-time free API call quota, daily message credits in the app
- identity a placeholder: card and phone unknown | verified 2026-11-10T01:21:20.151Z (live) | stale on 2026-12-11
- url https://www.coze.com/open/docs/developer_guides/coze_api_overview
- free tier: a free quota of 30 Coze API calls for each registered account, counted over all APIs of all agents, then Coze tokens must be bought; separately 10 message credits a day in the app, valid only for the day | unit: requests | metered on: request-count | read on: 2026-11-04 | source: [1] | note: the 10 credits a day cover use in the Coze app and not API calls; the free API quota is 30 calls and is not stated to reset
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: unverified: the sign-up page renders only in a browser and was not readable; the docs say the free quota is for registered users
- interface: rest
- limits:
  - volume-quota (binding): 30 free Coze API calls per account, then Coze tokens are deducted [1]
  - request-rate: under 2M accumulated purchased Coze tokens: 5 requests per second, 300 per minute, 20,000 per day [1]
- binding note: 30 free calls is the whole free API allowance
- endpoint: https://api.coze.com/v3/chat
- tooling: HTTP API that chats with an agent published as an API service, authenticated with a personal access token; the model is the one configured in the agent
- composes with: buying Coze tokens raises the Chat API rate limit tier at 2M accumulated tokens
- reliability: not measured
- notes: the free API quota is a one-time 30 calls
- evidence:
  - [1] 2026-11-04: the free API quota is 30 calls | capture: sha256:0ea7eb5d6882b2a83cec0cdeb28f8ef51d5e0f0fc03fcda54f9cbcc13cd00655 | quote: The free quota for the API service is 30 Coze API calls
  - [1] 2026-11-04: the rate limit below 2M purchased tokens | capture: sha256:0ea7eb5d6882b2a83cec0cdeb28f8ef51d5e0f0fc03fcda54f9cbcc13cd00655 | quote: | Less than 2M (2,000,000)​ | 5​ | 300​ | 20,000​ |
  - [2] 2026-11-04: each account gets 30 free API calls | capture: sha256:2d83d4cee27809cc183e5ecf30fb6f8e6d230a2e83114ee3864b68327ee3a060 | quote: Each Coze account is granted 30 free API calls and 100 Web SDK calls.
  - [3] 2026-11-04: 10 message credits per day in the app | capture: sha256:a677e17bbeb762c93787f2305ab03005537aaef4f5a857967d33ee58a754fb73 | quote: Each account is granted 10 credits per day.
  - probe:https://api.coze.com/v3/chat 2026-11-10: a keyless POST on 2026-11-10 answered 200 with code 4101 'The token you entered is incorrect', so the endpoint gates on a token | capture: sha256:8638292092c535c247f204d05568f3077ef4b43bf7ae336d7bc57f170824ad01 | quote: "status": 200
- sources:
  - [1] https://www.coze.com/open/docs/developer_guides/coze_api_overview
  - [2] https://docs.coze.com/guides/billing
  - [3] https://www.coze.com/open/docs/guides/message_credits
