# AKI.IO

> aki.io | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aki/ | JSON https://fshy.ajam.dev/api/v1/entity/aki.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AKI.IO

- `inference/aki-io` | paid-only | evidence documented | binding volume-quota | category inference endpoint, keyed paid credit
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://aki.io/docs/
- free tier: no free inference allowance stated: the docs say to create a free user account and then top up the credit balance; the API key is required for all requests | unit: none | metered on: none | read on: 2026-11-18 | source: [1] | note: the FAQ describes a free Company Account to explore models but no free inference credits; purchased prepaid credits never expire; payment methods include credit card, bank transfer and SEPA debit
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a free user account is created at aki.io/signup; no card or phone field is stated on the docs page
- interface: rest
- limits:
  - volume-quota (binding): credit balance must be topped up before use; an optional monthly budget cap can be set in the user profile [1]
- binding note: no free tokens are published, so a topped-up balance binds before any rate
- endpoint: https://aki.io/openai/v1
- tooling: an OpenAI- or Anthropic-compatible key; AKI.IO admin profile for keys and monthly budget caps
- composes with: pairs with an OpenAI-compatible agent only after topping up credit; the scarce link is the paid balance
- reliability: no reliability event recorded
- notes: the word free applies to the account, not to inference; no free token allowance is published.
- evidence:
  - [1] 2026-11-18: a free account is created and then the credit balance must be topped up | capture: sha256:25704f2b1a21d18a7bc862a464513633f4e3f9351ffa250988261143cfd1871c | quote: create a free user account at [https://aki.io/signup](https://aki.io/signup) and top-up your credit balance.
  - [2] 2026-11-18: a free Company Account is offered to explore models, but pricing is prepaid credit with no free inference allowance | capture: sha256:6e5042231f3be841dfde0efe5b8855d083b6c227864f2133d088eadd058f16d1 | quote: Create a free Company Account to explore available models and start integrating the API. For additional evaluation credits or assistance with model selection, Trust Levels, and production workloads, contact sales@aki.io.
- sources:
  - [1] https://aki.io/docs/
  - [2] https://aki.io/
