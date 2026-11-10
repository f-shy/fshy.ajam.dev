# BlockRun

> blockrun.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/blockrun/ | JSON https://fshy.ajam.dev/api/v1/entity/blockrun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BlockRun

- `inference/blockrun` | qualifies-with-caveat | evidence measured | binding request-rate | category inference relay
- needs card no, phone no, ID no, institution no | verified 2026-11-10T01:21:20.150Z (live) | stale on 2026-12-11
- url https://blockrun.ai/api/v1
- free tier: on 2026-11-10, 9 of 117 model ids on /v1/models carried billing_mode free; on 2026-10-22, 7 of 117 carried an input price of 0 (the two counts use different markers); the rest carry list prices spanning openai, google, anthropic, xai, zai, bytedance, deepseek, qwen, nvidia and eleven other families | unit: tokens | metered on: request-count | read on: 2026-11-10 | source: [1] | note: on 2026-11-10 the nine free ids were nvidia/nemotron-3-super-120b, nvidia/nemotron-3-nano-omni-30b-a3b-reasoning, nvidia/nemotron-3.5-lightning, nvidia/nemotron-3-ultra-550b, cohere/north-mini-code, poolside/laguna-xs-2.1, nvidia/muse-glimmer-30b, nvidia/nemotron-3.5-bolt and nvidia/minimax-m3.1-flash; on 2026-10-22 the seven zero-priced ids were nvidia/nemotron-3-nano-omni-30b-a3b-reasoning, nvidia/nemotron-3.5-lightning, nvidia/llama-3.2-11b-vision, nvidia/nemotron-3-ultra-550b, cohere/north-mini-code, poolside/laguna-xs-2.1 and nvidia/muse-glimmer-30b
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no Authorization header sent and none required for the free route
- interface: rest
- limits:
  - request-rate (binding): unpublished at BlockRun. The free route fails with FREE_MODEL_FAILED carrying debug 'NVIDIA API error: 429 Too Many Requests', so the observed ceiling belongs to BlockRun's own upstream key probe:https://blockrun.ai/api/v1/chat/completions, 2026-10-22
  - request-rate (binding): 30 requests per minute (burst) and 300 requests per hour (sustained) per source IP on free chat models; over the limit the answer is 429 FREE_TIER_RATE_LIMITED [2]
- binding note: the upstream NVIDIA 429 binds, and it arrives inside a 200-style error body rather than as a 429 status, so a client cannot see it by status code
- endpoint: https://blockrun.ai/api/v1/chat/completions
- tooling: any OpenAI-compatible client; curl against POST {base}/chat/completions
- composes with: pairs with a free-standing agent as a relay of last resort; the scarce link is BlockRun's own upstream key, because its 429 arrives as FREE_MODEL_FAILED inside a 200
- reliability: a keyless POST on 2026-11-10 for nvidia/nemotron-3.5-lightning answered 200 twice and echoed the model; on 2026-10-22, 5 sequential identical calls answered 2 and refused 3 with FREE_MODEL_FAILED and a debug field naming 'NVIDIA API error: 429 Too Many Requests'
- notes: The relay category's clearest instance. An error body that names a different vendor's API is the cheapest available tell, and the echoed model string is the second. A caller that does not compare the echoed model receives a plausible answer from a model it did not choose.
- evidence note: the relay is proved by its own error body naming NVIDIA, and the substitution by the echoed model string. Both are measured; the upstream arrangement is inferred from them.
- probe:
  - records[0].probe_id: blockrun-gptoss20b
  - records[0].requested_model: nvidia/gpt-oss-20b
  - records[0].http_run1: 200
  - records[0].http_run2: 200
  - records[0].answered_run1: yes
  - records[0].answered_run2: yes
  - records[0].model_echoed: nvidia/gpt-oss-20b
  - records[0].echo_match: yes
  - records[0].latency_ms_run1: 2091
  - records[0].latency_ms_run2: 2543
  - records[0].ttft_ms_run1: 822
  - records[0].completion_tokens_run1: 51
  - records[0].tps_run1: 12.92
  - records[0].tps_run2: 13.23
  - records[0].needle_echoed_run1: yes
  - records[0].body_bytes_run1: 451
  - records[0].body_sha256_16_run1: 056f8f161ffbc029
  - records[0].reasoning_only: no
  - runs: probes-w.json; probes-w-run2.json
- evidence:
  - probe:https://blockrun.ai/api/v1/chat/completions 2026-10-22: nvidia/gpt-oss-20b answered 200 and echoed nvidia/gpt-oss-20b's two runs, 2091 ms and 2543 ms, 51 completion tokens each
  - probe:https://blockrun.ai/api/v1/chat/completions 2026-10-22: in the recon sweep eight minutes earlier, one of five sequential calls echoed nvidia/nemotron-3-super-120b for a nvidia/gpt-oss-20b request, and three returned FREE_MODEL_FAILED with debug 'NVIDIA API error: 429 Too Many Requests'
  - [1] 2026-10-22: 117 model ids across 13 or more vendor families including openai, anthropic, google, xai and elevenlabs, with per-model long_context price tiers
  - [2] 2026-10-28: the documented over-limit 429 carries Retry-After, X-RateLimit-Limit: 30, X-RateLimit-Remaining and X-RateLimit-Reset (unix milliseconds); a separate 429 with code FREE_MODEL_FAILED and Retry-After: 30 signals an exhausted free pool | capture: sha256:ba788bc524f7f0c096e6f5599a022a32f41226246bf61875c5f1a74226e5ca01 | quote: X-RateLimit-Limit: 30
  - [3] 2026-10-28: the vendor documents that a busy free model is answered by another free model and that the model field names the one that answered | capture: sha256:2a850de5e2d02ee8412c6ed4b4abf2f3b5a10fbd054ba091478c46dd19d15b7a | quote: When the one you named is, we answer with another free model instead of failing the request.
  - probe:https://blockrun.ai/api/v1/chat/completions 2026-10-28: one POST with no Authorization header for nvidia/nemotron-3.5-lightning answered 200 and echoed model nvidia/nemotron-3.5-lightning-nim; headers x-free-model: true, x-health-reroute: true, x-original-model: nvidia/nemotron-3.5-lightning, x-served-model: nvidia/nemotron-3.5-lightning-nim; no X-RateLimit header on the 200; content was a reasoning trace with finish_reason length at max_tokens 128
  - [4] 2026-10-28: the error catalogue lists FREE_TIER_RATE_LIMITED as the 429 per-IP free-tier limit of 30 per minute and 300 per hour | capture: sha256:b8ffbc5247355c81fa1087b9a13ef5dbf9a1f6be7d9bed386084eecbc1beafba | quote: | `FREE_TIER_RATE_LIMITED` | 429 | Per-IP free-tier limit (30/min, 300/hour) |
  - [2] 2026-10-28: free-model pool exhaustion surfaces as FREE_MODEL_FAILED (non-streaming) or STREAM_FAILED (streaming), published as 429 with Retry-After 30 | capture: sha256:ba788bc524f7f0c096e6f5599a022a32f41226246bf61875c5f1a74226e5ca01 | quote: Separately, when the free model pool itself is out of capacity (every free rung is throttled or unhealthy upstream), the response is `429` with `code: "STREAM_FAILED"` (streaming) or `"FREE_MODEL_FAILED"` (non-streaming) and `Retry-After: 30`.
  - [2] 2026-10-28: free chat models need no wallet and no payment | capture: sha256:ba788bc524f7f0c096e6f5599a022a32f41226246bf61875c5f1a74226e5ca01 | quote: Free chat models (the ones `GET /v1/models` lists with `"billing_mode": "free"`) need no wallet and no payment
  - [2] 2026-10-28: the free-route limit is a per-IP request-rate limit, so the limit kind request-rate stands | capture: sha256:ba788bc524f7f0c096e6f5599a022a32f41226246bf61875c5f1a74226e5ca01 | quote: 30 requests per minute (burst) and 300 requests per hour (sustained)
  - [2] 2026-11-04: the vendor publishes a per-IP free-tier limit of 30 per minute and 300 per hour | capture: sha256:041d612f47f75550fdcb581e18c7b754b72d150dc46f0ff7073de28565ae8475 | quote: 30 requests per minute (burst) and 300 requests per hour (sustained)
  - [4] 2026-11-04: the error catalogue names FREE_TIER_RATE_LIMITED as the per-IP free-tier 429 at 30 per minute and 300 per hour | capture: sha256:3c7ba5fc030c1986488e0129271d3177eeb4f22f11d31a819fb645f94124c807 | quote: | `FREE_TIER_RATE_LIMITED` | 429 | Per-IP free-tier limit (30/min, 300/hour) |
  - [2] 2026-11-04: the free route is still limited per source IP by request rate | capture: sha256:041d612f47f75550fdcb581e18c7b754b72d150dc46f0ff7073de28565ae8475 | quote: 30 requests per minute (burst) and 300 requests per hour (sustained)
  - probe:https://blockrun.ai/api/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 for nvidia/nemotron-3.5-lightning answered 200 twice and echoed nvidia/nemotron-3.5-lightning with 56 tokens (24 prompt, 32 completion) | capture: sha256:4fcea24310d308aa980892921873cfc8567e30e890a7862708b79add745fb6dd | quote: "status": 200
- sources:
  - [1] https://blockrun.ai/api/v1/models
  - [2] https://blockrun.ai/docs/api-reference/rate-limits
  - [3] https://blockrun.ai/free
  - [4] https://blockrun.ai/docs/api-reference/errors
