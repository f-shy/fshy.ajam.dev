# Nous Portal

> nousresearch.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nousresearch/ | JSON https://fshy.ajam.dev/api/v1/entity/nousresearch.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nous Portal

- `inference/nous-portal-free` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway, free plan with free models only | tier Free
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T05:36:05.774Z (live) | stale on 2026-12-19
- url https://portal.nousresearch.com/manage-subscription
- free tier: Free plan at $0 per month with $0 in monthly credits: access to the models marked FREE in the catalog only, at standard rate limits; a third-party plan table reads 50 RPM / 500K TPM | unit: mixed | metered on: request-count | read on: 2026-11-04 | source: [1] | note: the free model set rotates; the portal catalog page read on 2026-11-04 lists Reflection Beam 1.0 501B A23B, Crouton Alpha, StepFun Step 3.7 Flash and Upstage Solar Mini 4 as free; the true unit is a request and token rate with no volume cap, which no unit term names
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a Nous Portal account (email, Discord or wallet login); one first-hand third-party report states the Free plan is activated through a 0-yen payment screen that requires a credit card; another directory records no card requirement, so the card requirement is reported, not documented
- interface: rest
- limits:
  - request-rate (binding): 50 RPM / 500K TPM per a third-party plan table; unverified on the vendor page, which prints only 'standard rate limits' and no numbers; unverified: behind a sign-up [1]
  - request-rate (binding): 50 RPM, 500,000 TPM for the Free tier, stated in the first-party OpenAPI definition under API Key Rate Limits [2]
- binding note: the free tier is bounded by the 50 requests a minute and 500,000 tokens a minute limit, not by a credit balance
- interface detail: OpenAI-compatible REST. POST /chat/completions and POST /completions for inference; GET /models for the public model list. Auth is an API key as a bearer token in the Authorization header (BearerAuth, HTTP bearer scheme).
- endpoint: https://inference-api.nousresearch.com/v1
- tooling: OpenAI-compatible endpoint at https://inference-api.nousresearch.com/v1, stated in the first-party OpenAPI definition and API docs; Hermes Agent CLI logs in through OAuth. Routes: POST /chat/completions, POST /completions, GET /models.
- composes with: free models only; paid models and API keys draw on prepaid credits
- reliability: the free model list rotates and one report found only 6 of 10 listed free models answering
- notes: endpoint filled from first-party OpenAPI definition on 2026-11-18; the free tier uses the same host as paid tiers, distinguished by the 50 RPM / 500,000 TPM limit and FREE model tags. On 2026-11-18 two keyless POSTs to /v1/chat/completions returned HTTP 403 with a Cloudflare challenge page, so the host answered and refused the request at the edge.
- evidence note: Endpoint, routes, auth scheme and the Free 50 RPM / 500,000 TPM limit come from the first-party OpenAPI definition and API docs read on 2026-11-18; the host was probed live with an unkeyed GET /models that returned 200. Model access for a free account remains unverified: behind a sign-up.
- probe:
  - records[0].probe_id: nous-portal-free-20261118
  - records[0].target: https://inference-api.nousresearch.com/v1/chat/completions
  - records[0].runs[0].label: run1
  - records[0].runs[0].probed_at: 2026-11-18T05:26:14.804Z
  - records[0].runs[0].status: 403
  - records[0].runs[0].completion: no
  - records[0].runs[0].capture: sha256:3783a597dd1da2a95442118314b82a4951774a676658559a8df83969c85b1e40
  - records[0].runs[1].label: run2
  - records[0].runs[1].probed_at: 2026-11-18T05:36:05.774Z
  - records[0].runs[1].status: 403
  - records[0].runs[1].completion: no
  - records[0].runs[1].capture: sha256:1629f56e462a83f05d235b5b01e3f6defc756fb11834fef85b3c3ebce4dafd18
- evidence:
  - [1] 2026-11-04: third-party plan table: Free plan is $0 with no monthly credits, free models only, 50 RPM / 500K TPM | capture: sha256:8f9d6b027445de62dc3f9c132854e40413d5e212a4d7d33d2bb7da045e3c61c4 | quote: | Free | $0 | $0 (free models only) | — | 50 RPM / 500K TPM |
  - [3] 2026-11-04: first-hand third-party report: the Free plan needs a card at a 0-yen checkout | capture: sha256:36e06ee5c28832581a8e0e3029e2544d5c43a31890d88f86e604803472c72ba9 | quote: However, even for the free plan, you must register a credit card when signing up.
  - [4] 2026-11-04: the portal model catalog marks models FREE | capture: sha256:41c87bc8743004d617e2b6a11b5d642580338881efa8e5ffd2a1c0363bed9c7d | quote: | #1 | Upstage: Solar Mini 4 | Text | FREE | — | — |
  - [5] 2026-11-04: a directory says the public page no longer shows the 50 RPM / 500K TPM figures | capture: sha256:89cb975ec7b573a10b39bf5a40da54f68c786412898b79302a413ff6bb608553 | quote: The public free-plan page checked on 2026-10-06 no longer exposes the earlier observed 50 RPM and 500k TPM.
  - [6] 2026-11-04: API keys draw on prepaid credits, not on plan usage | capture: sha256:48de04e6871ea390bc7865b60a641978b91a02bfb5325711a4089adaf191d6d0 | quote: API keys always use your credits (pay-as-you-go), not included usage
  - [1] 2026-11-04: third-party plan table gives 50 RPM / 500K TPM | capture: sha256:8f9d6b027445de62dc3f9c132854e40413d5e212a4d7d33d2bb7da045e3c61c4 | quote: | Free | $0 | $0 (free models only) | — | 50 RPM / 500K TPM |
  - [2] 2026-11-18: first-party OpenAPI definition states the API base URL | capture: sha256:645775176ce197be1cd63943dd41198ed4c3eec272e334e88c7bb809e8ccd6ac | quote: - The API is available at [https://inference-api.nousresearch.com/v1](https://inference-api.nousresearch.com/v1).
  - [2] 2026-11-18: the OpenAPI server list names the production endpoint | capture: sha256:645775176ce197be1cd63943dd41198ed4c3eec272e334e88c7bb809e8ccd6ac | quote: "servers":[{"url":"https://inference-api.nousresearch.com/v1","description":"Production server"}]
  - [2] 2026-11-18: API authentication is a bearer token in the Authorization header | capture: sha256:645775176ce197be1cd63943dd41198ed4c3eec272e334e88c7bb809e8ccd6ac | quote: "securitySchemes":{"BearerAuth":{"type":"http","scheme":"bearer"}}
  - [2] 2026-11-18: the first-party OpenAPI definition states the Free tier rate limit | capture: sha256:645775176ce197be1cd63943dd41198ed4c3eec272e334e88c7bb809e8ccd6ac | quote: - Free: 50 RPM, 500,000 TPM
  - [7] 2026-11-18: the rendered first-party docs page repeats the API base URL | capture: sha256:d6c031aef80f92472ef7da1c441047d09c6f03bd43d0193497760630479de623 | quote: - The API is available at [https://inference-api.nousresearch.com/v1](https://inference-api.nousresearch.com/v1).
  - [8] 2026-11-18: the Hermes Agent integration guide sets the same base URL | capture: sha256:91ae43c3ede9832d5c07ff2ed3cb3396da8832e74f1ab06747790329fe045ede | quote: base_url: https://inference-api.nousresearch.com/v1
  - probe:https://inference-api.nousresearch.com/v1/chat/completions 2026-11-18: a keyless POST to https://inference-api.nousresearch.com/v1/chat/completions for NousResearch/Hermes-4-405B returned HTTP 403 with body <!DOCTYPE html> <!--[if lt IE 7]> <html class='no-js ie6 oldie' lang='en-US'> <![endif]--> <!--[if IE 7]> <htm and no completion in 549 ms Probe start 2026-11-18T05:26:14.804Z. | capture: sha256:3783a597dd1da2a95442118314b82a4951774a676658559a8df83969c85b1e40 | quote: a keyless POST to https://inference-api.nousresearch.com/v1/chat/completions for NousResearch/Hermes-4-405B returned HTTP 403 with body <!DOCTYPE html> <!--[if lt IE 7]> <html class='no-js ie6 oldie' lang='en-US'> <![endif]--> <!--[if IE 7]> <htm and no completion in 549 ms
  - probe:https://inference-api.nousresearch.com/v1/chat/completions 2026-11-18: a keyless POST to https://inference-api.nousresearch.com/v1/chat/completions for NousResearch/Hermes-4-405B returned HTTP 403 with body <!DOCTYPE html> <!--[if lt IE 7]> <html class='no-js ie6 oldie' lang='en-US'> <![endif]--> <!--[if IE 7]> <htm and no completion in 128 ms Probe start 2026-11-18T05:36:05.774Z. | capture: sha256:1629f56e462a83f05d235b5b01e3f6defc756fb11834fef85b3c3ebce4dafd18 | quote: a keyless POST to https://inference-api.nousresearch.com/v1/chat/completions for NousResearch/Hermes-4-405B returned HTTP 403 with body <!DOCTYPE html> <!--[if lt IE 7]> <html class='no-js ie6 oldie' lang='en-US'> <![endif]--> <!--[if IE 7]> <htm and no completion in 128 ms
- sources:
  - [1] https://openclawlaunch.com/guides/nous-portal
  - [2] https://portal.nousresearch.com/api/openapi
  - [3] https://note.com/hash_13/n/n4fe7799c48af?hl=en
  - [4] https://portal.nousresearch.com/models
  - [5] https://freeinferencing.com/provider/nous_portal/
  - [6] https://portal.nousresearch.com/manage-subscription
  - [7] https://portal.nousresearch.com/api-docs
  - [8] https://hermes-agent.nousresearch.com/docs/integrations/nous-portal
