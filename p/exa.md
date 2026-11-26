# Exa

> exa.ai | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/exa/ | JSON https://fshy.ajam.dev/api/v1/entity/exa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Exa

- `crawler-scraper/exa` | qualifies-with-caveat | evidence documented | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://exa.ai/pricing
- free tier: USD 10 in credits on signup, reset to USD 10 on the first of each month, no payment method; a one-time USD 10 bonus after onboarding | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a search request | source: [1]
- retention: credit balance resets monthly, so unused credit does not accumulate | source: [1]
- egress: not applicable: results are JSON, no bytes are stored | metered: no | source: [1]
- identity: email | detail: signup states no payment method required
- interface: rest
- limits:
  - request-rate (binding): USD 10 a month buys about 2,500 lite searches at USD 4 per 1,000 [1]
  - request-rate (binding): a base price covers 10 results; each result above 10 is USD 1 per 1,000 [1]
- interface detail: REST at api.exa.ai, bearer key; exa-py and exa-js SDKs; hosted MCP at mcp.exa.ai
- tooling: exa-py, exa-js, hosted MCP
- composes with: Serves as a primary web search provider. The /contents endpoint acts as a retrieval route billed per page and content type.
- reliability: no reliability event recorded
- notes: The top position reflects the Artificial Analysis search quality benchmark index rather than local evaluation.
- evidence:
  - [1] 2026-10-22: free tier is USD 10 of credit a month, reset monthly, no payment method; lite search USD 4 per 1,000 requests, auto and fast USD 7, contents USD 1 per 1,000 pages, answer USD 5, monitors USD 15
  - withheld 2026-10-22: 
- sources:
  - [1] https://exa.ai/pricing
