# AbliteratedLLM

> abliteratedllm.dev | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/abliteratedllm/ | JSON https://fshy.ajam.dev/api/v1/entity/abliteratedllm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AbliteratedLLM

- `inference/abliteratedllm` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://abliteratedllm.dev/pricing
- free tier: USD 0.50 of free credit per new account, claimed in a separate step with a heavier proof-of-work check; one grant per IPv4 /24 or IPv6 /48 every 30 days; not from datacenter, VPN or Tor addresses. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: anonymous 16-digit account number at signup; no email and no KYC; the free credit is claimed in a separate step with a heavier browser proof-of-work check
- interface: rest
- limits:
  - volume-quota (binding): USD 0.50 free credit per IPv4 /24 or IPv6 /48 every 30 days [1]
  - request-rate: trial accounts get 10 requests a minute, one at a time, up to 4,096 output tokens each [1]
- endpoint: https://api.abliteratedllm.dev/v1
- tooling: an OpenAI-compatible base URL plus the vendor console; an Anthropic /v1/messages endpoint also exists
- composes with: the $0.50 credit and the IPv4 /24 gate bind before the per-token price
- reliability: trial accounts are limited to 10 requests a minute and one at a time until a credited deposit lifts the limits; credit claims are unavailable from datacenter, VPN or Tor addresses
- notes: the free credit expires never itself but is a one-off grant capped by network and proof of work, so it is a trial rather than a standing allowance
- evidence:
  - [1] 2026-11-18: a new account receives $0.50 of free credit; minimum top-up $5; credit never expires | capture: sha256:00538bd7d7a2c173b7273cb602f0b174b9ca86a92cf311525811e61c34721b41 | quote: No subscription and no minimum spend beyond a $5 top-up. Credit never expires, and every new account can try it with $0.50 of free credit.
- sources:
  - [1] https://abliteratedllm.dev/pricing
