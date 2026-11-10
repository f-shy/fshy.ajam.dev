# GitHub Models inference

> github.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-2/ | JSON https://fshy.ajam.dev/api/v1/entity/github-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GitHub Models inference

- `inference/github-models-inference` | dead | evidence measured | binding none | category inference endpoint, dead shell
- needs card no, phone no, ID no, institution no | verified 2026-10-28T09:47:54.948Z (live) | stale on 2026-11-28
- url https://models.github.ai/inference
- free tier: no completion is returned; the endpoint answers 200 with a 4-byte body 'OK' | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no key was sent; the endpoint did not ask for one
- interface: rest
- limits note: no rate or quota binds: the gate is access, not allowance
- endpoint: https://models.github.ai/inference/chat/completions
- tooling: any OpenAI-compatible client; curl against POST {base}/chat/completions
- composes with: no chain exists: the service was retired on 2026-07-30 and every caller must move to Azure AI Foundry or Copilot
- reliability: returns HTTP 200 with Content-Type text/plain and a 4-byte body, which a status-only probe scores as a success
- notes: This is the control row for the never-trust-200 rule: the status is a success, the body is not a completion, and the body hash is identical across three runs. The verdict is dead, and it now rests on the vendor's own retirement notice at docs.github.com/en/github-models ('fully retired as of July 30, 2026'), not only on the empty body. The distinction matters: an endpoint that gates on a key also returns 402 or 401 rather than 200 with 'OK', and this one returns 200 with 'OK' because the service is gone rather than because it wants a credential.
- evidence note: Repeated test requests returned identical 4-byte response bodies consistently across runs on 2026-10-28.
- probe:
  - records[0].probe_id: github-models
  - records[0].requested_model: openai/gpt-4o-mini
  - records[0].http_run1: 200
  - records[0].http_run2: 200
  - records[0].answered_run1: no
  - records[0].answered_run2: no
  - records[0].echo_match: yes
  - records[0].latency_ms_run1: 1126
  - records[0].latency_ms_run2: 914
  - records[0].completion_tokens_run1: 0
  - records[0].needle_echoed_run1: no
  - records[0].body_bytes_run1: 4
  - records[0].body_sha256_16_run1: 19d8c9921b99c82d
  - records[0].reasoning_only: no
  - records[0].error_run1: OK
  - records[0].error_run2: OK
  - runs: probes-w.json; probes-w-run2.json
- extras:
  - death.on: 2026-07-30
  - death.cause: dead-service
- evidence:
  - probe:https://models.github.ai/inference/chat/completions 2026-10-22: HTTP 200, 4 bytes, body 'OK', identical sha256 19d8c9921b99c82d in three separate runs
  - [2] 2026-10-22: 'GitHub Models has been retired. As of July 30, 2026, GitHub Models has been fully retired. The playground, model catalog, inference API, and bring your own key (BYOK) are no longer available to any customer.' That is the vendor's own statement of death, which the 4-byte body alone could not establish
  - [2] 2026-10-28: the vendor states GitHub Models, including the inference API, was fully retired on July 30, 2026 | capture: sha256:a7ac45358c4db70999c6f9945215c9a440091ada92f391b410e267c8a85f602f | quote: As of July 30, 2026, GitHub Models has been fully retired. The playground, model catalog, inference API, and bring your own key (BYOK) are no longer available to any customer.
  - probe:https://models.github.ai/inference/chat/completions 2026-10-28: a GET to https://models.github.ai/inference/chat/completions returned HTTP 200, 4 bytes, text/plain, body 'OK', sha256 19d8c9921b99c82d78c985136a5e28f6382011641fb6160c0c1a7573a402ea66, the digest recorded for the earlier POST probes
- sources:
  - [1] https://models.github.ai/inference
  - [2] https://docs.github.com/en/github-models
