# LangSearch Rerank API

> langsearch.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/langsearch/ | JSON https://fshy.ajam.dev/api/v1/entity/langsearch.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LangSearch Rerank API

- `inference/langsearch-rerank-api` | dead | evidence documented | binding none | category rerank API, withdrawn | tier Free Plan
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:34:03.660Z (live) | stale on 2026-12-04
- url https://docs.langsearch.com/resources/faq
- free tier: none: the vendor states Rerank is no longer a documented product offering; the Free Plan covers web search with a daily token allowance | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an API key is created in the vendor dashboard; unverified: the dashboard sign-up fields, which are behind a login
- interface: rest
- limits:
  - request-rate: not applicable: the rerank endpoint is withdrawn; the web search Free Plan applies a daily token allowance that resets at 00:00 UTC [1]
- binding note: the rerank offer is withdrawn
- tooling: no rerank endpoint is documented; the vendor's web search API remains
- composes with: none for rerank
- reliability: third-party lists still describe a free Rerank API; the vendor's own documentation states it is no longer offered and its former reference page answers not found
- notes: the web search side of the product is separate and still free; it belongs to the crawler-scraper topic
- evidence note: the withdrawal is quoted from the vendor FAQ and the missing reference page is a stored capture; the exact date of withdrawal is unknown.
- evidence:
  - [1] 2026-11-03: the Rerank API is no longer offered | capture: sha256:6d35f2087d9c131494e6f35410eb5671f6bfbb257ce646afc8a9b3e1dc4b54b1 | quote: Our product now focuses on Web Search API. Rerank is no longer a documented product offering.
  - [2] 2026-11-03: the former Rerank API reference page no longer exists | capture: sha256:b9c07a31c2f48a7715dcb36a0dbf1bc55f46f03263f0ccfaef62662269456fbc | quote: The requested page could not be found.
  - [3] 2026-11-03: the free plan lists web search features only | capture: sha256:54e45c39adb9d6eab01a1da3abf26b1a1cb7c564da1341d9e220e92946d5b4e4 | quote: Web Search Free More context Free All supported features Free
- sources:
  - [1] https://docs.langsearch.com/resources/faq
  - [2] https://docs.langsearch.com/api/rerank-api
  - [3] https://langsearch.com/pricing
