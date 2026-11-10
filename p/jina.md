# Jina Reader

> jina.ai | Crawling, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jina/ | JSON https://fshy.ajam.dev/api/v1/entity/jina.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jina Reader

- `crawler-scraper/jina-reader` | qualifies | evidence measured | binding per-ip-shaping | category reader and extractor API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-12-22
- url https://jina.ai/reader/
- free tier: r.jina.ai is free at 20 requests a minute with no key; a free API key raises it to 500 RPM and carries 10M tokens | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a request, billed in output tokens once a key is used | source: [1]
- retention: 10M tokens per new key, one-time | source: [1]
- egress: not applicable: Markdown answers | metered: no | source: [1]
- identity: anonymous | detail: the keyless route needs nothing; a key is an account
- interface: rest
- limits:
  - request-rate: 20 RPM keyless, 500 RPM with a free key, 5,000 RPM premium [1]
  - request-rate: 10M free tokens per new key, counted on the output response [1]
  - per-object-cap: a per-request token budget header bounds the answer; the OCR path costs 40 times more tokens [1]
  - per-ip-shaping (binding): 20 requests a minute per IP keyless, reported in x-ratelimit-limit as `20, 20;w=60`; a domain can be blocked for a year or more after excess use [2]
- interface detail: GET https://r.jina.ai/<url>; search at s.jina.ai; token budget per request
- tooling: Apache-2.0 source; Readability over linkedom; pdfjs-dist
- composes with: Read step 2's ladder; the only keyless renderer found
- reliability: A domain can be blocked for years after excess use: nodeseek.com answered 403 with a block dated 2027-07-02. Page text arrives with the page's own instructions to models intact, so it must be treated as data.
- notes: It is not universal. It refused www.nodeseek.com with a 403 AbuseAlleviationError stating the domain is blocked until 2027-07-02 after suspected excess use, so a per-domain block is the failure mode and it outlasts any retry budget. Every answer is a third party's rendering, so a number read from it is reported, not documented, until the origin confirms it.
- evidence:
  - [1] 2026-10-22: Reader API free; 20 RPM without an API key, 500 RPM with a free key, 5000 with premium; 10M free tokens per new key; s.jina.ai 100 RPM with a free key
  - [3] 2026-10-22: 200, 460 bytes, 0.9 s, keyless, Markdown with a title and a published time; the body carried two warnings about the page maybe not being fully loaded
  - [4] 2026-10-22: x-ratelimit-limit reads `20, 20;w=60` and x-usage-tokens 28 on a small page
  - [5] 2026-10-22: 200, a whole 2024 thread with every post body, 19 posts with author and date; the answer also carries the forum's own all-caps instruction block addressed to language models, so the page text is untrusted input
- sources:
  - [1] https://jina.ai/reader/
  - [2] https://r.jina.ai/https://www.nodeseek.com/post-918318-1
  - [3] https://r.jina.ai/https://example.com/
  - [4] https://r.jina.ai/https://linux.do/
  - [5] https://r.jina.ai/https://linux.do/t/topic/49044

## Jina AI embeddings and reranker API

- `inference/jina-ai-embeddings-reranker` | trial-only | evidence documented | binding volume-quota | category embedding and rerank API, one-time free token balance on an auto-generated key | tier Free API key
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:34:03.660Z (live) | stale on 2026-12-04
- url https://jina.ai/embeddings/
- free tier: an auto-generated API key carries free tokens usable across every Jina model (embeddings, reranker, reader, classifier, segmenter). The first-party pages state no token amount; a third-party catalogue reports 10M tokens per new key, one-time. When the tokens are spent the key needs a purchased top-up | unit: tokens | metered on: request-count | read on: 2026-11-03 | source: [1] | note: unverified: the 10M figure rests on the third-party catalogue only; the vendor pages read say 'free tokens' with no number
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: a key is auto-generated for a new user and the vendor only recommends logging in to keep it; unverified: whether the key page asks for any field before it issues the key, and the key page is a browser app that the page reader returned empty
- interface: rest
- limits:
  - volume-quota (binding): free tokens on the key, shared by every Jina API on that key; amount unstated on the vendor pages read, a third-party catalogue reports 10M tokens one-time [1]
  - request-rate: Free key: 100 requests and 100,000 tokens per minute on /v1/embeddings and /v1/rerank per the product pages (https://jina.ai/embeddings/, https://jina.ai/reranker/); the API reference at https://docs.jina.ai/ states 500 requests and 1,000,000 tokens per minute for the same endpoints; both pages are current and disagree; a per-IP limit of 10,000 requests per 60 seconds also applies; excess answers HTTP 429 [1]
- binding note: the one-time free token balance runs out before any rate limit matters: at the lower rate (100,000 tokens per minute) 10M tokens would take 100 minutes
- endpoint: https://api.jina.ai/v1/embeddings
- tooling: any HTTP client or the OpenAI-schema-compatible /v1/embeddings call; /v1/rerank takes a query and a document list; /v1/batch/embeddings takes JSONL for large jobs
- composes with: the same key and balance also pay for Reader (r.jina.ai) and Search (s.jina.ai); embeddings from here pair with the rerank endpoint of the same key as a second stage
- reliability: the vendor's post-acquisition notice states the embeddings and reranker APIs continue to be developed and maintained; the free tokens do not renew
- notes: models on the keyless list include jina-embeddings-v5-text-small, v5-text-nano, v5-omni-small, v5-omni-nano, jina-embeddings-v4 and v3, jina-code-embeddings-0.5b and 1.5b, jina-clip-v2, jina-colbert-v2, and the rerankers jina-reranker-v3.5, v3, m0 and v2-base-multilingual
- evidence note: the free key, both rate-limit pairs and the model ids are quoted from vendor pages; the token amount is unverified at the vendor (third-party figure only) and the two rate-limit pairs disagree between vendor pages.
- evidence:
  - [1] 2026-11-03: a new user gets an auto-generated key carrying free tokens that work across every Jina model; the first-party page states no token amount | capture: sha256:16d0824ab71c0cd89aaa7776d67f33b355dbe2c6a31aa682f22c19e0fb042b5f | quote: Yes. New users get an auto-generated API key with free tokens usable across any of our models. Once the free tokens are consumed, you can purchase additional tokens for the key in the 'Buy tokens' tab.
  - [1] 2026-11-03: a free key is limited to 100 requests and 100,000 tokens per minute, with an additional per-IP limit of 10,000 requests per 60 seconds | capture: sha256:16d0824ab71c0cd89aaa7776d67f33b355dbe2c6a31aa682f22c19e0fb042b5f | quote: Rate limits depend on your API key type: Free: 100 RPM, 100K TPM Paid: 500 RPM, 2M TPM Premium: 5,000 RPM, 50M TPM There is an additional IP-based limit of 10,000 requests per 60 seconds to prevent abuse.
  - [2] 2026-11-03: the embeddings product page gives a free key 100 requests and 100,000 tokens per minute on /v1/embeddings | capture: sha256:c06b8bb0bd531a74d1812410326a8d12e4bc14eb632d3db29b184c700deee62c | quote: | Embedding API | `https://api.jina.ai/v1/embeddings` | Convert text/images to fixed-length vectors | | 100 RPM & 100,000 TPM |
  - [3] 2026-11-03: the reranker product page gives a free key 100 requests and 100,000 tokens per minute on /v1/rerank | capture: sha256:b2aed74caa12a4405b4ef2fa9593467f379bfcf67dae78889645ce4a09cda3c1 | quote: | Reranker API | `https://api.jina.ai/v1/rerank` | Rank documents by query | | 100 RPM & 100,000 TPM |
  - [4] 2026-11-03: the API reference gives the Free column 500 requests and 1,000,000 tokens per minute on /v1/embeddings, which differs from the product pages | capture: sha256:7d4e9bc1850b97d96874777a92289ca2c39aa010f1f57c1ffeefa6798ef576d3 | quote: | `/v1/embeddings` | 500 RPM · 1M TPM | 500 RPM · 10M TPM | 5,000 RPM · 100M TPM |
  - [4] 2026-11-03: the API reference gives the Free column 500 requests and 1,000,000 tokens per minute on /v1/rerank | capture: sha256:7d4e9bc1850b97d96874777a92289ca2c39aa010f1f57c1ffeefa6798ef576d3 | quote: | `/v1/rerank` | 500 RPM · 1M TPM | 500 RPM · 10M TPM | 5,000 RPM · 100M TPM |
  - [5] 2026-11-03: the keyless model list names jina-embeddings-v5-text-small among the embedding models | capture: sha256:4a7b9f90344ab85b83834202b1cb2f2ea3b013ad50d8a8e7480f052d19a917d0 | quote: "id":"jina-ai/jina-embeddings-v5-text-small","hugging_face_id":"jinaai/jina-embeddings-v5-text-small"
  - [5] 2026-11-03: the keyless model list names jina-reranker-v3.5 among the rerankers | capture: sha256:4a7b9f90344ab85b83834202b1cb2f2ea3b013ad50d8a8e7480f052d19a917d0 | quote: "id":"jina-ai/jina-reranker-v3.5","hugging_face_id":"jinaai/jina-reranker-v3.5"
  - [1] 2026-11-03: logging in is recommended and not stated as required to hold a key | capture: sha256:16d0824ab71c0cd89aaa7776d67f33b355dbe2c6a31aa682f22c19e0fb042b5f | quote: It's recommended to log in to keep your API key securely stored and easily accessible.
  - [4] 2026-11-03: every embeddings and rerank call needs a bearer key, obtained from the key page | capture: sha256:7d4e9bc1850b97d96874777a92289ca2c39aa010f1f57c1ffeefa6798ef576d3 | quote: Authentication. Send `Authorization: Bearer `. Get a key at https://jina.ai/?sui=apikey.
  - [6] 2026-11-03: a third-party catalogue reports the free allowance as 10M tokens per new key, one-time, with no card | capture: sha256:31a3a81929acb13229c013370fa33b7abe2a057991fadd279e773fe5909d7637 | quote: | [Jina AI](https://aifree.dev/offer/jina-ai-free-api-tokens) | 10M tokens per new API key, shared across Embeddings, Reranker, Reader, Classifier and Segmenter | jina-embeddings-v5-text-small and v5-omni-small (32K) | jina-reranker-v3.5 | No | One-time |
  - [1] 2026-11-03: the vendor states the embeddings and reranker APIs continue to be served after the acquisition | capture: sha256:16d0824ab71c0cd89aaa7776d67f33b355dbe2c6a31aa682f22c19e0fb042b5f | quote: Yes. The Reader API, Embeddings API, and Reranker API continue to be developed and maintained, and models continue to be published to cloud marketplace platforms.
  - probe:https://api.jina.ai/v1/embeddings 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:d658b90813e4980496b49f59bfc7a3809ef73830add47967993cae3dfcc4d575 | quote: "status": 401
- sources:
  - [1] https://jina.ai/contact-sales/
  - [2] https://jina.ai/embeddings/
  - [3] https://jina.ai/reranker/
  - [4] https://docs.jina.ai/
  - [5] https://api.jina.ai/v1/models
  - [6] https://aifree.dev/learn/free-embeddings-api
