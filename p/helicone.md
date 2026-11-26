# Helicone

> helicone.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/helicone/ | JSON https://fshy.ajam.dev/api/v1/entity/helicone.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Helicone

- `inference/helicone` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference observability and gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://helicone.ai/pricing
- free tier: Hobby plan is Free and includes 10,000 free requests, 1 GB storage, 1 seat and 1 organization; the Pro plan carries a 7-day free trial. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: the response is the payload of the proxied call; no separate egress term is published | metered: no
- identity: email | detail: a free Hobby signup needs an email; no card is required for the Hobby plan
- interface: rest
- limits:
  - volume-quota (binding): 7-day trial on Pro, and 10,000 requests a month on the free tier [2]
- endpoint: https://ai-gateway.helicone.ai/v1
- tooling: a proxy base URL plus the vendor SDK
- composes with: the 10,000-request monthly ceiling on the Hobby plan is the scarce link
- reliability: the free figure is a request count on a proxied path, so the gateway sits in the failure path of every call
- notes: A standing free Hobby tier of 10,000 requests was read on 2026-11-18; the Pro plan also has a 7-day trial. The binding constraint is the 10,000-request monthly ceiling.
- evidence:
  - [2] 2026-11-18: the Pro plan carries a 7-day free trial and the free tier is priced at USD 0.00 for 10K requests | capture: sha256:6d276f7d533f7a88e8fd5b964cca31812d06c6abe8230fde2606be0ca0d2316b | quote: Pro[7-day free trial](https://us.helicone.ai/settings/billing)
  - [1] 2026-11-18: the Hobby plan is free and includes 10,000 free requests, 1 GB storage, 1 seat and 1 organization | capture: sha256:6d276f7d533f7a88e8fd5b964cca31812d06c6abe8230fde2606be0ca0d2316b | quote: 10,000 free requests
- sources:
  - [1] https://www.helicone.ai/pricing
  - [2] https://helicone.ai/pricing
