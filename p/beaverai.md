# BeaverNet

> beaverai.org | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/beaverai/ | JSON https://fshy.ajam.dev/api/v1/entity/beaverai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BeaverNet

- `inference/beavernet` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway, community GPU pool, anonymous tier
- needs card no, phone no, ID no, institution no | verified 2026-11-10T02:44:00.000Z (live) | stale on 2026-12-11
- url https://net.beaverai.org/v1
- free tier: Works without a key, with limits; a free key gives more. /v1/models listed 9 ids on 2026-11-10; the one echo/ id probed answered with no key, and the one other id probed, blue/dealignai/DeepSeek-V4.1-Flash-1017-UNCENSORED-FP8, answered 401 and requires a key; the listing carries a per-model allow_anonymous flag. On 2026-10-28 the home page counted 4 models available | unit: requests | metered on: request-count | read on: 2026-11-10 | source: [1] | note: the limits are not stated as numbers on the page; models are served by volunteers sharing their own GPUs
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: the page says try it without an account, or sign up with just a name; a GET to /v1/usage, /v1/limits and /v1/chat/completions with no Authorization header answered 401 Missing or invalid Authorization header, so the anonymous route may need a header or token that the page does not show
- interface: rest
- limits:
  - request-rate (binding): unpublished: the page says works without a key, with limits, and gives no number; GET /v1/models returns no rate-limit header [1]
- binding note: the unpublished anonymous limit is the stated gate, and only some models allow anonymous calls
- endpoint: https://net.beaverai.org/v1/chat/completions
- tooling: any OpenAI-compatible client with base URL https://net.beaverai.org/v1
- composes with: pairs with prototypes that tolerate a changing set of volunteer-served models; the anonymous tier covers only models flagged allow_anonymous
- reliability: the model set is small and changes with volunteer availability: the home page counted 4 models available on 2026-10-28, and /v1/models listed 9 ids on 2026-11-10
- notes: whether a keyless POST to /v1/chat/completions answers is unverified
- evidence note: the claim is first-party and the listing was read by GET; the 401 on keyless GETs to the chat and usage routes conflicts with it, and no completion was sent because probe issues GET and HEAD only
- probe:
  - records[0].probe_id: beavernet-v1-models-get
  - records[0].method: GET
  - records[0].url: https://net.beaverai.org/v1/models
  - records[0].http: 200
  - records[0].authorization_sent: no
  - records[0].models.Quack/koboldcpp/Dumbstral-169B.i1-IQ4_XS.allow_anonymous: no
  - records[0].models.drummer/google/gemma-4-31b-it.allow_anonymous: no
  - records[0].models.bgg1996/melirrhoe.allow_anonymous: yes
  - records[0].models.blue/dealignai/DeepSeek-V4.1-Flash-1017-UNCENSORED-FP8.allow_anonymous: yes
  - records[0].probed_at: 2026-10-28T04:49:21.961Z
  - records[0].chat_completion_tested: no
  - records[1].probe_id: beavernet-chat-get
  - records[1].method: GET
  - records[1].url: https://net.beaverai.org/v1/chat/completions
  - records[1].http: 401
  - records[1].error_message: Missing or invalid Authorization header
  - records[1].probed_at: 2026-10-28T04:48:00.137Z
- evidence:
  - [1] 2026-10-28: the page states the API works without a key, with limits | capture: sha256:a9d2ed2ff3c265abfb8c59b35e3f0fea89502c289105c8493aed3db14ec77197 | quote: Works without a key, with limits. Get a free key for more.
  - [1] 2026-10-28: an account is optional and a signup needs just a name | capture: sha256:a9d2ed2ff3c265abfb8c59b35e3f0fea89502c289105c8493aed3db14ec77197 | quote: Try it without an account, or sign up with just a name.
  - [1] 2026-10-28: the home page lists the count of models available | capture: sha256:a9d2ed2ff3c265abfb8c59b35e3f0fea89502c289105c8493aed3db14ec77197 | quote: Models available
  - [2] 2026-10-28: a keyless GET /v1/models answered 200 and listed bgg1996/melirrhoe, whose allow_anonymous flag follows in the body | capture: sha256:7a673e698eb68662b0dab4bd4dbf7a5413cc5b2f8d94e1939e13cbe21d05aa71 | quote: "id":"bgg1996/melirrhoe"
  - probe:https://net.beaverai.org/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 for echo/huihui-qwen3.8-27b-abliterated answered 200 twice and echoed huihui-qwen3.8-27b-abliterated, the first call with empty content at 32 reasoning tokens and the second with content pong | capture: sha256:8b56fa04aaa7b6dd7231e56123dc75be6fdee9b0790b32bf2ccf274dc5b087eb | quote: "status": 200
  - probe:https://net.beaverai.org/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 for blue/dealignai/DeepSeek-V4.1-Flash-1017-UNCENSORED-FP8 answered 401 on both calls with the message that the model requires an API key, in the same probe in which echo/huihui-qwen3.8-27b-abliterated answered 200 twice | capture: sha256:49f461bf5fa016ea3acabeb8dc785d7f7c8093405af520fabb056d372e65c1f7 | quote: "status": 401
- sources:
  - [1] https://net.beaverai.org/
  - [2] https://net.beaverai.org/v1/models
