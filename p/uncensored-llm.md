# uncensored-llm.sbs

> uncensored-llm.sbs | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uncensored-llm/ | JSON https://fshy.ajam.dev/api/v1/entity/uncensored-llm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## uncensored-llm.sbs

- `inference/uncensored-llm` | fails-quota | evidence measured | binding request-rate | category inference endpoint, keyless
- needs card no, phone no, ID no, institution no | verified 2026-10-28T05:28:44.471Z (live) | stale on 2026-11-28
- url https://uncensored-llm.sbs/v1
- free tier: 3 model ids, no key; no quota is published | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no key required
- interface: rest
- limits:
  - request-rate (binding): unpublished. One call was refused with Cloudflare Error 1010 on a Python User-Agent, and the rest returned filler rather than an answer probe:https://uncensored-llm.sbs/v1/chat/completions, 2026-10-22
- limits note: unpublished. One call was refused with Cloudflare Error 1010 on a Python User-Agent, and the rest returned filler rather than an answer; the filler reproduces on 2026-10-22T04:51:05Z with a 278-byte…
- binding note: the returned content binds before any rate does: the endpoint answers 200 with valid JSON and filler, so a caller meets a quality failure before a quota
- endpoint: https://uncensored-llm.sbs/v1/chat/completions
- tooling: any OpenAI-compatible client; curl against POST {base}/chat/completions
- composes with: pairs with nothing that needs a correct answer; the scarce link is content quality, because the endpoint returns filler inside a valid 200
- reliability: returns a well-formed completion whose content is filler rather than an answer, with finish_reason stop and no usage object
- notes: A 200, valid JSON, non-empty content and finish_reason stop, which is not an answer. The needle test declared it a failure and a does-content-exist test would have declared it a success.
- evidence note: five calls across three sessions. Two answered with content that did not contain the needle; one was refused by Cloudflare Error 1010 with the wrong User-Agent.
- probe:
  - records[0].probe_id: uncensored-llm-70b
  - records[0].requested_model: uncensored-llm-70b
  - records[0].http_run1: 403
  - records[0].http_run2: 200
  - records[0].answered_run1: no
  - records[0].answered_run2: yes
  - records[0].model_echoed: uncensored-llm-70b
  - records[0].echo_match: yes
  - records[0].latency_ms_run1: 203
  - records[0].latency_ms_run2: 861
  - records[0].completion_tokens_run1: 0
  - records[0].needle_echoed_run1: no
  - records[0].body_bytes_run1: 708
  - records[0].body_sha256_16_run1: 3334d60915892d60
  - records[0].reasoning_only: no
  - records[0].error_run1: {"type":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1010/","title":"Error 1010: Access denied","status":403,"detail":"The site owner has b
  - runs: probes-w.json; probes-w-run2.json
- evidence:
  - probe:https://uncensored-llm.sbs/v1/chat/completions 2026-10-22: a POST asking for the single token NEEDLE-9K2X returned 200 with a 278-byte body, finish_reason 'stop', model 'uncensored-llm-70b' echoed, and content "I can help with that. Could you provide more details about what you're looking for?" The needle is absent from the answer, so the endpoint answers with filler rather than with a completion
  - [2] 2026-10-28: the vendor publishes no rate number, only that heavy sustained use may be throttled; the same page states no signup and no credit card | capture: sha256:3312cbbf0207b5f0daa3a5ab46e8eaf7b944bc3a01439de81c1044e832c1020a | quote: The free tier is intentionally generous. Heavy sustained use may be throttled to keep the endpoint fast for everyone.
  - probe:https://uncensored-llm.sbs/v1/chat/completions 2026-10-28: one POST with no Authorization header for uncensored-llm-70b answered 200 with a 270-byte body, model uncensored-llm-70b echoed, finish_reason stop, no usage object, and content that does not contain the requested token NEEDLE-9K2X; no rate-limit header (headers: server cloudflare, cf-cache-status DYNAMIC)
- sources:
  - [1] https://uncensored-llm.sbs/v1/models
  - [2] https://uncensored-llm.sbs/
