# Token Harbor

> tokenharbor.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tokenharbor/ | JSON https://fshy.ajam.dev/api/v1/entity/tokenharbor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Token Harbor

- `inference/token-harbor` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway, free plan with a rolling 7-day allowance on :free model ids
- needs card no, phone no, ID no, institution no | verified 2026-11-18T05:36:13.257Z (live) | stale on 2026-12-19
- url https://tokenharbor.ai/pricing
- free tier: a $0 Free plan with a free allowance that resets on a rolling 7-day period, spent on :free model ids (DeepSeek V4.1 Flash, MiMo V2.6 Flash, TH-Rudder at the time read); the allowance amount is not printed on the pages read | unit: mixed | metered on: unstated | read on: 2026-11-04 | source: [1] | note: TH-Rudder text chat in Webchat is free and unlimited during a limited-time campaign and does not draw on the allowance; the allowance size is unverified: not printed
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: the sign-in page offers Continue with GitHub and Continue with Google; the pricing page says no card is required for the Free plan
- interface: rest
- limits:
  - volume-quota (binding): free allowance resetting on a rolling 7-day period; the amount is not printed on the pages read; unverified: behind a sign-up [1]
  - request-rate: unverified: no free-plan request rate is printed on the pages read [2]
- binding note: the rolling 7-day free allowance is the stated bound; its size is unpublished
- interface detail: OpenAI- and Anthropic-compatible inference gateway. OpenAI shape is POST https://tokenharbor.ai/v1/chat/completions under base URL https://tokenharbor.ai/v1; Anthropic shape is POST https://tokenharbor.ai/v1/messages under base URL https://tokenharbor.ai; the model catalog is GET https://tokenharbor.ai/v1/models and needs a key. Other first-party routes are /v1/responses and /v1/images/generations.
- endpoint: https://tokenharbor.ai/v1 (OpenAI-compatible base URL); https://tokenharbor.ai (Anthropic-compatible base URL)
- tooling: any OpenAI-compatible client with a custom base URL, or an Anthropic SDK with base_url="https://tokenharbor.ai"; official Connect CLI at https://tokenharbor.ai/connect.sh. No client tool is missing.
- composes with: Free plan, then wallet top-ups per token, or an optional Pass from $1.99 a month
- reliability: free models are promotional and the set changes as models are added or retired; free-route conversations may be read by staff and used by the serving providers
- notes: the allowance amount needs the dashboard, which is behind a sign-up. Keyless GET /v1/models and keyless POST to both chat routes returned HTTP 401 on 2026-11-18, and HEAD /v1 returned 404; no first-party OpenAPI document is published and /openapi.json returned HTML under HTTP 200. On 2026-11-18 two keyless POSTs returned HTTP 403 stating that API access from your region is not available, so the route exists and the host refuses this network.
- evidence note: endpoint, route, method and auth are from first-party llms.txt, /docs, the Chat APIs page and the live API error body, and keyless probes returned 401 as expected. The key and any per-account allowance were not disclosed without an account.
- probe:
  - records[0].probe_id: token-harbor-20261118
  - records[0].target: https://tokenharbor.ai/v1/chat/completions
  - records[0].runs[0].label: run1
  - records[0].runs[0].probed_at: 2026-11-18T05:26:25.264Z
  - records[0].runs[0].status: 403
  - records[0].runs[0].completion: no
  - records[0].runs[0].capture: sha256:c0f7a8dc0ace475329cb297ff01c17620a4f74336e308778258f0333d808e762
  - records[0].runs[1].label: run2
  - records[0].runs[1].probed_at: 2026-11-18T05:36:13.257Z
  - records[0].runs[1].status: 403
  - records[0].runs[1].completion: no
  - records[0].runs[1].capture: sha256:454a1a37cb1cec68f3507086037661470ca28f27198caa9af6eb79c05a2b00e9
- evidence:
  - [1] 2026-11-04: the free allowance resets on a rolling 7-day period | capture: sha256:5f4a90d2e133a69f267690ca6ffb89c461500de64b50488c279fa14a76593d0e | quote: Resets on a rolling 7-day period
  - [1] 2026-11-04: the Free plan needs no card | capture: sha256:5f4a90d2e133a69f267690ca6ffb89c461500de64b50488c279fa14a76593d0e | quote: No card required.
  - [2] 2026-11-04: free models are promotional | capture: sha256:c5bc035959d8c3f60ceddc27ec0a1a7a9cfa831b4eb3ea01678dc68dcaba7a3b | quote: Yes. Token Harbor may provide free access to selected frontier models as part of promotional programs and community initiatives.
  - [3] 2026-11-04: free model ids draw on the free allowance and are never billed | capture: sha256:f7ee59688b7dcd00fb6e986d79b9bc3e7f542ac602509f95f082d313d2fa94df | quote: Each :free model ID uses Token Harbor's free allowance and is never billed
  - [4] 2026-11-04: the sign-in page offers GitHub sign-in | capture: sha256:31a93f3ca257c26356b2a04e55aea3f4d5b291c3f9fc481447109ee586a6c79e | quote: Continue with GitHub
  - [4] 2026-11-04: the sign-in page offers Google sign-in | capture: sha256:31a93f3ca257c26356b2a04e55aea3f4d5b291c3f9fc481447109ee586a6c79e | quote: Continue with Google
  - [1] 2026-11-04: the allowance resets on a rolling 7-day period; its size is not on the public pages | capture: sha256:5f4a90d2e133a69f267690ca6ffb89c461500de64b50488c279fa14a76593d0e | quote: Resets on a rolling 7-day period
  - [5] 2026-11-18: both first-party base URLs stated in the first-party catalog | capture: sha256:3a4897d1e0e6877c7e8b829ecbef6df116b2389cf23d6e358e95cd9c7c786394 | quote: One key, every model. The OpenAI-compatible base URL is https://tokenharbor.ai/v1 and the Anthropic-compatible base URL is https://tokenharbor.ai.
  - [6] 2026-11-18: model catalog route and its key requirement | capture: sha256:3b231e5350f079c871659321417af4898be15446252249a1b30ecf9a295ac27f | quote: run `GET https://tokenharbor.ai/v1/models` with your key as the Bearer token (without one it answers `401`).
  - [7] 2026-11-18: bearer auth header on the OpenAI-compatible route | capture: sha256:da61eecbf6b07bfaeb75bac10e7829684bd560ccef05fe3240a5dde40be7a560 | quote: Auth header is `Authorization: Bearer thk_…`.
  - [7] 2026-11-18: full first-party POST route for OpenAI Chat Completions | capture: sha256:da61eecbf6b07bfaeb75bac10e7829684bd560ccef05fe3240a5dde40be7a560 | quote: url="https://tokenharbor.ai/v1/chat/completions",
  - [7] 2026-11-18: auth headers on the Anthropic-compatible route | capture: sha256:da61eecbf6b07bfaeb75bac10e7829684bd560ccef05fe3240a5dde40be7a560 | quote: Auth accepts either `x-api-key` (Anthropic default) or `Authorization: Bearer` — pass your `thk_live_` key in either header.
  - [8] 2026-11-18: the single base URL a client is told to paste | capture: sha256:082d36dbfbc2cdadabe001a337ceefbbf3a5e21753c53bc0421caf822b25b62f | quote: | Base URL | `https://tokenharbor.ai/v1` |
  - [9] 2026-11-18: auth scope of the Universal Key across both route families | capture: sha256:a64d3a247ec0538e7ecf71c128c63486054026375e26b76880755b730d65ba89 | quote: A Universal Key is an OpenAI-shaped bearer token that authenticates every call to `/v1/chat/completions` and the Anthropic-compatible `/v1/messages`.
  - probe:https://tokenharbor.ai/v1/chat/completions 2026-11-18: a keyless POST to https://tokenharbor.ai/v1/chat/completions for deepseek-v4.1-flash:free returned HTTP 403 with body {'error':{'message':'API access from your region is not available. Token Harbor can't serve regions under sanc and no completion in 879 ms Probe start 2026-11-18T05:26:25.264Z. | capture: sha256:c0f7a8dc0ace475329cb297ff01c17620a4f74336e308778258f0333d808e762 | quote: a keyless POST to https://tokenharbor.ai/v1/chat/completions for deepseek-v4.1-flash:free returned HTTP 403 with body {'error':{'message':'API access from your region is not available. Token Harbor can't serve regions under sanc and no completion in 879 ms
  - probe:https://tokenharbor.ai/v1/chat/completions 2026-11-18: a keyless POST to https://tokenharbor.ai/v1/chat/completions for deepseek-v4.1-flash:free returned HTTP 403 with body {'error':{'message':'API access from your region is not available. Token Harbor can't serve regions under sanc and no completion in 960 ms Probe start 2026-11-18T05:36:13.257Z. | capture: sha256:454a1a37cb1cec68f3507086037661470ca28f27198caa9af6eb79c05a2b00e9 | quote: a keyless POST to https://tokenharbor.ai/v1/chat/completions for deepseek-v4.1-flash:free returned HTTP 403 with body {'error':{'message':'API access from your region is not available. Token Harbor can't serve regions under sanc and no completion in 960 ms
- sources:
  - [1] https://tokenharbor.ai/pricing
  - [2] https://tokenharbor.ai/faq
  - [3] https://tokenharbor.ai/blog/3-best-free-ai-apis-for-coding-and-agents-in-2026
  - [4] https://tokenharbor.ai/signup
  - [5] https://tokenharbor.ai/llms.txt
  - [6] https://tokenharbor.ai/docs/integrations
  - [7] https://tokenharbor.ai/docs/api/curl
  - [8] https://tokenharbor.ai/docs/getting-started/quickstart
  - [9] https://tokenharbor.ai/docs/getting-started/universal-key
