# Nomic

> nomic.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nomic/ | JSON https://fshy.ajam.dev/api/v1/entity/nomic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nomic

- `compute/nomic` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:40:26.615Z (live) | stale on 2026-12-05
- url https://www.nomic.ai/pricing
- free tier: a Free plan that needs no card: 'No credit card required', 'Limited agent requests', 'Access to core Platform surfaces'. Paid tiers are Individual at USD 20 a month and Business at USD 40 a user a month with a 25-seat minimum. The free allowance is not quantified on the page. | unit: users | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: product-tier
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no card: the pricing page's Free column reads 'No credit card required' with 'Start for free'. No hold exists because no payment method is taken. The signup form is not quoted, so the email requirement is inferred rather than read, and debit and prepaid acceptance are not stated.
- interface: rest
- limits:
  - request-rate (binding): the limit is a request count with no published number: 'Limited agent requests' is the only quantity on the pricing page, so the binding point is unknown until an account is exercised. [1]
- limits note: the limit is a request count with no published number: 'Limited agent requests' is the only quantity on the pricing page, so the binding point is unknown until an account is exercised.
- binding note: the same as limits note
- interface detail: HTTP (REST) API at https://<your-domain>.nomic.ai/api/v0, authenticated with a Bearer or Basic API key from the Developer Console; documented at docs.nomic.ai/api/overview for Business and Enterprise instances.
- tooling: HTTP API at https://<your-domain>.nomic.ai/api/v0 with API keys, on Business and Enterprise instances only; Individual plan accounts do not include the Agent API; an MCP server is also published.
- composes with: an account with no card that parses long documents composes with a free embedding tier elsewhere: Nomic does the parsing, another vendor does the vectors, and neither needs a payment method.
- reliability: no reliability event recorded
- notes: Nomic has moved from an embedding and atlas company to document parsing for architecture, engineering and construction data, so the free tier buys that product rather than a general inference quota. The record is kept because the free tier is real and card-free, and the missing number is the whole question: without a published request count it cannot be compared with the other lanes. Unverified: one account and a rate-limit response header.
- extras:
  - facets.class: product-tier
  - facets.free_tier_kind: product-tier
- evidence:
  - [1] 2026-10-22: the Free column reads 'Free', 'No credit card required', 'Limited agent requests', 'Access to core Platform surfaces', with 'Start for free'; Individual '$20 / mo.'; Business '25 seat minimum' at '$40 / user / mo.', quoted
  - [2] 2026-10-22: 'Agent API: APIs and models for internal AI teams building custom agents over complex AEC data: parse drawings, extract structured data, embed multimodal files', quoted
  - [3] 2026-11-04: the HTTP API is not part of the Individual plan; the Free plan has no API per the docs | capture: sha256:060a3b8101548211447639f5e734d0828b5dacc8e8de2f042d911500b02ebb30 | quote: Individual plan accounts do not include the Agent API.
  - [3] 2026-11-04: an HTTP API exists | capture: sha256:060a3b8101548211447639f5e734d0828b5dacc8e8de2f042d911500b02ebb30 | quote: The Nomic HTTP API connects your systems to the same platform capabilities you use in the product
  - [3] 2026-11-04: the provider documents an HTTP API | capture: sha256:060a3b8101548211447639f5e734d0828b5dacc8e8de2f042d911500b02ebb30 | quote: The Nomic HTTP API connects your systems to the same platform capabilities you use in the product
- sources:
  - [1] https://www.nomic.ai/pricing
  - [2] https://www.nomic.ai/
  - [3] https://docs.nomic.ai/api/overview
