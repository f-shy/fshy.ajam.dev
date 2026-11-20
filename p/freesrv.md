# Jad AI

> freesrv.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freesrv/ | JSON https://fshy.ajam.dev/api/v1/entity/freesrv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jad AI

- `inference/jad-ai` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://jadai.freesrv.com/docs
- free tier: All three model IDs (jad-ai, jad-go, jad-code) are free at USD 0 per million input tokens and USD 0 per million output tokens, with no billing step, no paid tier and no per-request charge. | unit: tokens | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create a key in Settings to API keys, shown once; no card or payment step is described
- interface: rest
- limits:
  - volume-quota (binding): USD 0 per million input and output tokens on all three model IDs [1]
  - per-object-cap: jad-go and jad-code output clamped to 16,384 tokens; jad-ai capped at 32,000 tokens [1]
- endpoint: https://jadai.freesrv.com/v1
- tooling: an OpenAI-compatible Chat Completions endpoint with a jad_ key and a JAD_API_KEY environment variable for OpenCode
- composes with: the gateway routes only free-tier upstream models, so upstream availability is the scarce link
- reliability: requests with images return 503 vision_unavailable if no vision-capable provider is configured; the gateway never executes tools itself and rejects unknown model IDs with 400
- notes: a genuinely free USD 0 per-token gateway exists, but it depends on free-tier upstream models and the three IDs are routing aliases, so model availability can change
- evidence:
  - [1] 2026-11-18: all three model IDs are free at USD 0 per million input and output tokens, routing only free-tier upstream models | capture: sha256:97ff90edad1210f236b19ebb78e7a46f531a0021d089f93f957679aff83f79e3 | quote: All three model IDs are free: $0 per million input tokens and $0 per million output tokens. The gateway routes only free-tier upstream models.
- sources:
  - [1] https://jadai.freesrv.com/docs
