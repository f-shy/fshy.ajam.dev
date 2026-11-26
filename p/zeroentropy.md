# ZeroEntropy zerank reranker and zembed-1 embeddings API

> zeroentropy.dev | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zeroentropy/ | JSON https://fshy.ajam.dev/api/v1/entity/zeroentropy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZeroEntropy zerank reranker and zembed-1 embeddings API

- `inference/zeroentropy-rerank-embeddings` | dead | evidence measured | binding none | category rerank and embedding API, sunset | tier Pay-as-you-go
- needs card no, phone no, ID no, institution no | verified 2026-11-03T09:59:11.542Z (live) | stale on 2026-12-04
- url https://zeroentropy.dev/pricing/
- free tier: none: the vendor sunset its hosted products after September 4th, 2026 and disabled new signups; the FAQ still advertises a free tier of unstated size. The models are released as open weights under Apache 2.0 | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: new signups are disabled; unverified: the former sign-up fields, because the dashboard page shows a marketing shell only
- interface: rest
- limits:
  - request-rate: while the API served: 500,000 bytes and 1,000 requests per minute by default per the rerank reference, 2,500,000 UTF-8 bytes per minute per the pricing page; the endpoint now answers HTTP 503 [2]
- binding note: the service no longer answers
- endpoint: https://api.zeroentropy.dev/v1/models/rerank
- tooling: Python and TypeScript SDKs and a REST API that no longer serve; the open weights of zerank-1, zerank-2 and zembed-1 are on Hugging Face
- composes with: none: the hosted API is down
- reliability: the hosted rerank endpoint answered HTTP 503 with the body 'ZeroEntropy inference is unavailable.' on 2026-11-03, after the vendor's announced sunset of 2026-09-04; the docs, FAQ and pricing pages still list prices and a free tier
- notes: the pricing and docs pages still show USD 0.025 per million tokens for zerank-2 and USD 0.05 for zembed-1; those prices describe the sunset service
- evidence note: the sunset notice is quoted from the vendor and the 503 is a stored probe of the endpoint.
- evidence:
  - [1] 2026-11-03: the vendor announced the sunset of every product after 2026-09-04 | capture: sha256:ac92c6889d72d16e5b2169ebd8125df5b79dfbf2d0f3a0fd6bf3b5c8862c8679 | quote: All ZeroEntropy products will remain fully supported until September 4th, 2026 with no degradation, after which they will be sunset.
  - [1] 2026-11-03: new signups are disabled | capture: sha256:ac92c6889d72d16e5b2169ebd8125df5b79dfbf2d0f3a0fd6bf3b5c8862c8679 | quote: We have disabled new signups, and encourage existing customers to migrate away from ZeroEntropy products using the following resources.
  - probe:api.zeroentropy.dev 2026-11-03: the hosted rerank endpoint answers HTTP 503 on 2026-11-03 | capture: sha256:73fd0329b27ad52246503d40a5e7201d9c426b292020755c8c4675bf3303eab6 | quote: "status": 503
  - probe:api.zeroentropy.dev/body 2026-11-03: the endpoint body states that inference is unavailable | capture: sha256:78fee608fc0ad5bade4536c57b19df4317b0c8c94f504b382a5ea12124f57632 | quote: {"detail":"ZeroEntropy inference is unavailable."}
  - [3] 2026-11-03: the FAQ still advertises a free tier, with no amount, after the sunset notice | capture: sha256:67eddb0731537d3906bc37ee505a4a8d5773655581b9d7955c93956719649ffd | quote: Yes — every account starts with a free tier sufficient to evaluate the API end-to-end on your own data.
  - [4] 2026-11-03: the pricing page still lists zerank-2 at $0.025 per million tokens and a rate limit | capture: sha256:9c3178e729860281a8b318af9b51e5a3c02e9e533bf91b2935921c8240535813 | quote: Ratelimits: 2,500,000 UTF-8 bytes per minute
  - [5] 2026-11-03: a new account started on the free tier, so an account was the entry | capture: sha256:cbbf479aaa8cb0368796fafe1064845d938cb5bb8de0acc9a2d64d7dad5ec863 | quote: New accounts start on the free tier with rate limits sufficient for prototyping.
- sources:
  - [1] https://www.zeroentropy.dev/articles/zeroentropy-is-joining-notion/
  - [2] https://docs.zeroentropy.dev/api-reference/models/rerank
  - [3] https://zeroentropy.dev/faq/
  - [4] https://zeroentropy.dev/pricing/
  - [5] https://docs.zeroentropy.dev/quickstart
