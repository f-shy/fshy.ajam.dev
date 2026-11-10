# Pollinations

> pollinations.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pollinations/ | JSON https://fshy.ajam.dev/api/v1/entity/pollinations.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pollinations

- `inference/pollinations` | qualifies-with-caveat | evidence measured | binding request-rate | category inference endpoint, keyless
- needs card no, phone no, ID no, institution no | verified 2026-11-10T01:21:21.471Z (live) | stale on 2026-12-11
- url https://text.pollinations.ai/openai
- free tier: the Classic API lists one model, openai-fast, described as 'GPT-OSS 20B Reasoning LLM (OVH)', with aliases openai, gpt-oss, gpt-oss-20b and ovh-reasoning | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1] | note: the served model is OVH-hosted gpt-oss-20b, so this endpoint is a relay of the OVH public tier rather than a separate allocation
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no key required, but the allowance is metered per IP and shared with everything else on that address
- interface: rest
- limits:
  - request-rate (binding): 1 reply every 30 seconds per IP on the anonymous tier 402 body: 'Free limit reached: 1 reply every 30 seconds per IP'
- endpoint: https://text.pollinations.ai/openai/chat/completions
- tooling: any OpenAI-compatible client; curl against POST {base}/chat/completions
- composes with: pairs with a lightweight interactive caller; the one-reply-per-30-seconds-per-IP floor is the scarce link and it is shared with every other caller on the address
- reliability: a keyless POST on 2026-11-10 for openai-fast answered 200 twice with content 'pong'; on 2026-10-22 gpt-5-nano returned 402 in run 1 and 404 in run 2, eight minutes apart. The record of 2026-10-28 said: the same model on the same base URL returned 402 and 404 responses intermittently across test runs on 2026-10-28
- notes: The 402 is the finding: a keyless endpoint exhausted by per-IP budget with no account in existence.
- evidence note: the per-IP 402 was observed. The advertised id openai-fast is listed by GET /models with the aliases openai, gpt-oss, gpt-oss-20b and ovh-reasoning, and a completion for openai-fast reports the served model as gpt-oss-20b, so the served model is the advertised one under one of its aliases.
- probe:
  - records[0].probe_id: pollinations-fast
  - records[0].requested_model: openai-fast
  - records[0].http_run1: 200
  - records[0].http_run2: 200
  - records[0].answered_run1: yes
  - records[0].answered_run2: yes
  - records[0].model_echoed: gpt-oss-20b
  - records[0].echo_match: SUBSTITUTED
  - records[0].latency_ms_run1: 3501
  - records[0].latency_ms_run2: 997
  - records[0].ttft_ms_run1: 2532
  - records[0].completion_tokens_run1: 51
  - records[0].tps_basis: streamed chars/4 / (time_total - time_starttransfer) on a second, streaming call, run 1 only
  - records[0].needle_echoed_run1: yes
  - records[0].body_bytes_run1: 475
  - records[0].body_sha256_16_run1: c904d7fb4b2362a8
  - records[0].reasoning_only: no
  - records[1].probe_id: pollinations-gpt5
  - records[1].requested_model: gpt-5-nano
  - records[1].http_run1: 402
  - records[1].http_run2: 404
  - records[1].answered_run1: no
  - records[1].answered_run2: no
  - records[1].echo_match: yes
  - records[1].latency_ms_run1: 595
  - records[1].latency_ms_run2: 490
  - records[1].completion_tokens_run1: 0
  - records[1].needle_echoed_run1: no
  - records[1].body_bytes_run1: 324
  - records[1].body_sha256_16_run1: 9af5216aca23af3a
  - records[1].reasoning_only: no
  - records[1].error_run1: {"code": "FREE_LIMIT", "message": "Free limit reached: 1 reply every 30 seconds per IP. Retry after 28s, or get unlimited replies with a pollen key at https://enter.pollinations.ai/?ref=classic", "tim
  - records[1].error_run2: {"code": "NOT_FOUND", "message": "Model \"gpt-5-nano\" isn't on the Classic API. Free models: https://text.pollinations.ai/models. Every model we offer is on https://enter.pollinations.ai/?ref=classic
  - runs: probes-w.json; probes-w-run2.json
  - timing_note: latency_ms and ttft_ms on a row came from two different requests in the original instrument, which is how five rows ended up with ttft_ms > latency_ms. They are corrected here from a re-probe on 2026-10-22T04:38:22Z with probe3.py, which takes both fields from one streaming request: 475 ms total and 475 ms to first byte. The earlier run-1 figures (3501 ms latency, 2532 ms ttft) are kept because both came from one request pair that was internally consistent.
- evidence:
  - probe:https://text.pollinations.ai/openai/chat/completions 2026-10-22: requesting openai-fast returned 200 with model gpt-oss-20b echoed, a substitution; 51 completion tokens in the written run, and re-probed at 2026-10-22T04:38:22Z at 475 ms total with 475 ms to first byte on one streaming request. The recon run's 289 ms figure is withdrawn: its ttft_ms on the same row was 499 ms, so the two fields describe two different calls and neither can be quoted as a latency
  - probe:https://text.pollinations.ai/openai/chat/completions 2026-10-22: requesting gpt-5-nano returned 402 'Free limit reached: 1 reply every 30 seconds per IP' in run 1 and 404 'isn't on the Classic API' in run 2, eight minutes apart
  - [1] 2026-10-22: the Classic API lists exactly one model, openai-fast, with alias gpt-oss-20b and the description 'GPT-OSS 20B Reasoning LLM (OVH)'
  - [2] 2026-10-28: text requests are limited to one at a time, at least 30 seconds apart, per IP address | capture: sha256:2f2ef50b3871573b61ad7b1eb7485560eb6bbfe3af4a368f7d2f6dc7851a3d46 | quote: | Text | One at a time, at least 30 seconds apart. A stream waits for the next slot |
  - probe:https://text.pollinations.ai/openai/chat/completions 2026-10-28: one POST with no Authorization header for openai-fast answered 200 with content NEEDLE-9K2X; body model gpt-oss-20b and user_tier anonymous; headers x-model-used: gpt-oss-20b, x-usage-prompt-text-tokens: 324, x-usage-completion-text-tokens: 51, x-usage-total-tokens: 375; no rate-limit header (Retry-After is exposed only on a refusal)
  - probe:https://text.pollinations.ai/models 2026-10-28: GET /models lists one model, openai-fast, described as GPT-OSS 20B Reasoning LLM (OVH), tier anonymous, with aliases openai, gpt-oss, gpt-oss-20b and ovh-reasoning
  - probe:https://text.pollinations.ai/openai/chat/completions 2026-11-10: a keyless POST on 2026-11-10 for openai-fast answered 200 twice and echoed gpt-oss-20b with content 'pong' and 344 tokens (315 prompt, 29 completion) | capture: sha256:3a67cc241ac2052d9216edc29069d0bc6b155252dd0869a45577c33b24a441a4 | quote: "status": 200
- sources:
  - [1] https://text.pollinations.ai/models
  - [2] https://github.com/pollinations/pollinations/blob/master/APIDOCS.md
