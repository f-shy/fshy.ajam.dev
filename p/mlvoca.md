# mlvoca.com free LLM API

> mlvoca.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mlvoca/ | JSON https://fshy.ajam.dev/api/v1/entity/mlvoca.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mlvoca.com free LLM API

- `inference/mlvoca` | dead | evidence measured | binding none | category inference endpoint, keyless, Ollama format (not OpenAI-compatible), not answering
- needs card no, phone no, ID no, institution no | verified 2026-10-28T04:36:18.974Z (live) | stale on 2026-11-28
- url https://mlvoca.com/api/generate
- free tier: documented as POST /api/generate on tinyllama and deepseek-r1:1.5b with no API key and no rate limit; when read, GET /api/generate answered 502 Bad Gateway from nginx | unit: none | metered on: none | read on: 2026-10-28 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no API key and no rate limit per the project page when it was working
- interface: rest
- limits note: no rate or quota binds: the endpoint is not answering
- endpoint: https://mlvoca.com/api/generate
- tooling: Ollama-format POST /api/generate with {"model", "prompt", "stream"}; not an OpenAI chat route
- composes with: no chain exists while the endpoint is not answering
- reliability: GET /api/generate answered 502 Bad Gateway from nginx on four reads over about 10 minutes, and GET / and /api/tags answered 403 Forbidden; a third-party prober recorded 0 of 336 chat calls answered in 14 days
- notes: dead cause: dead-service, not confirmed by a POST; revisit with a POST-capable probe
- evidence note: the 502 was read by GET; no POST was sent because probe issues GET and HEAD only, so a POST that answers while the GET fails cannot be excluded
- probe:
  - records[0].probe_id: mlvoca-generate-get
  - records[0].method: GET
  - records[0].url: https://mlvoca.com/api/generate
  - records[0].http: 502
  - records[0].server: nginx/1.22.1
  - records[0].probed_at: 2026-10-28T04:48:45.156Z
  - records[1].probe_id: mlvoca-tags-get
  - records[1].method: GET
  - records[1].url: https://mlvoca.com/api/tags
  - records[1].http: 403
  - records[1].probed_at: 2026-10-28T04:45:32.339Z
- evidence:
  - [1] 2026-10-28: the project page states no rate limit and no API key | capture: sha256:3af9f46cc6901d91489242212b23e0c5b801d851c4b35d165c7b06583eff69eb | quote: - The endpoint of the free llm api currently works without any kind of rate limit or API key. Therefore, it can be used for free without token/call limits.
  - [2] 2026-10-28: GET /api/generate answered a 502 Bad Gateway page from nginx | capture: sha256:63e384c14fa5327de0db932d60f2ded2e889028eb50e74dcde35c721fe2ce0ee | quote: <center><h1>502 Bad Gateway</h1></center>
  - [3] 2026-10-28: a third-party prober got no answer from the endpoint in 14 days | capture: sha256:34aa29edf68cc49c49bdcf1119b702b0c338ae9d71d2a58db4b4586122b9a223 | quote: | [mlvoca.com](https://stillworks.supercapybara.com/llm/mlvoca) (Ollama-shaped, not OpenAI-compatible) | 0 of 0 models answering | 0 of 336 (0%) | — | no model answering |
- sources:
  - [1] https://mlvoca.github.io/free-llm-api/
  - [2] https://mlvoca.com/api/generate
  - [3] https://stillworks.supercapybara.com/free-llm-api-no-key
