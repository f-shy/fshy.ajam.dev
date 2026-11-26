# Regolo AI

> regolo.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/regolo/ | JSON https://fshy.ajam.dev/api/v1/entity/regolo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Regolo AI

- `compute/regolo-ai` | trial-only | evidence documented | binding volume-quota | category inference API | tier 30-day Free Trial
- needs card no, phone unknown, ID no, institution no | verified 2026-11-24T10:11:15.041Z (live) | stale on 2026-12-25
- url https://regolo.ai/pricing/
- free tier: Get full access to all Core Models. No credit card required, no commitment. Sign up and start building. The trial lasts 1 month / 30 days with 1M tokens per day, daily token limit to explore all features, stricter rate limits with fair usage throttling, and all Core Models including chat and embedding. | unit: tokens | metered on: wall-clock | read on: 2026-11-24 | source: [1] | note: trial-credit: 30 days of full Core Model access with no card; after the trial the account moves to pay-as-you-go with no automatic charge. The FAQ says 'You get 30 days of full, unrestricted access to all Regolo core models — no credit card required.'
- per-object cap: not applicable: the unit is API tokens, not stored objects; Regolo states zero data retention and no disk persistence, so there is no per-object cap. | source: [2] | note: the unit is tokens, not bytes
- retention: Zero Data Retention means Regolo does not store, log, or retain any of the data you send through our APIs — including prompts, completions, and any attached files. | days: 0 | source: [2] | note: the data is discarded once the request is processed; no stored object to expire
- egress: No. Regolo does not charge data egress fees. We believe in open, fair pricing — not in building financial walls around your data. | metered: no | source: [2]
- identity: email | detail: The sign-up guide says 'Click Sign Up and complete the registration form' and 'Verify your email address'. The pricing page states no credit card is required for the 30-day trial. Whether a phone number is asked for is unverified: not stated on the sign-up or pricing page read.
- interface: rest
- limits:
  - volume-quota (binding): 1M tokens per day on the Free Trial, with a 30-day duration, stricter rate limits and fair-usage throttling; the subscribed Core plan raises this to 20 million tokens a day at EUR 39.00 per month. [1]
- limits note: The trial's 1M tokens per day is a daily pool; the FAQ states a 20-million-token daily cap by default on subscription plans, up to 50M on Boost, 100M on Pro and 200M on Scale.
- binding note: The 1M-tokens-per-day trial pool runs out before the 30-day window does under sustained use, and the trial adds stricter rate limits and fair-usage throttling on top.
- interface detail: OpenAI-compatible REST API at https://api.regolo.ai/v1, a chat completions endpoint, and a browser dashboard for virtual keys; the provider documents Python, Node.js and cURL clients.
- endpoint: part of interface detail
- tooling: the user installs an OpenAI-compatible client library (Python, Node.js) or uses cURL against the API; no server binary is run by the user and no hardware is owned.
- composes with: An OpenAI-compatible endpoint and key-scoped spend limits let an agent loop swap Regolo into an existing client; the paid Core plan adds a 20-million-token daily cap with per-model usage multipliers, so the free 1M daily allowance binds first.
- reliability: Fair-usage throttling and stricter rate limits apply on the trial; no contractual SLA on Pay-as-you-Go or Subscription plans, and the service disclaims uninterrupted or error-free access.
- notes: The 30-day trial is a time-boxed allowance, not a recurring free tier: 1M tokens a day, no card, verified email, and a switch to pay-as-you-go at trial end. The cheapest paid subscription is the Core plan at EUR 39.00 per month for up to 600M tokens a month with 70% discount on the first 3 months; pay-as-you-go prices start at EUR 0.10 per 1M input tokens on several models. The API model list is readable without a key (HTTP 200, 17 models returned with usage multipliers), while the trial itself requires sign-up.
- evidence note: The rate, free trial, identity gate, egress terms and daily token cap are quoted from the vendor's own pricing, FAQ, docs and sign-up pages read on 2026-11-24; the API endpoint was read without a key with a probe.
- extras:
  - shape.gpu_class: serverless autoscaling GPUs, not exposed per model
  - billing_model: 30-day free trial with no card, then pay-as-you-go or monthly subscription
  - free_tier_kind: time-boxed-trial
  - term: 30 days, then pay as you go
  - status: announced and published on the current pricing page
  - network_out.allow_outbound: yes
  - network_out.ports: not stated
  - session_cap.wall_clock_min: 43200
  - session_cap.restart_required: no
  - session_cap.note: 1M tokens per day, 30-day trial duration; stricter rate limits and fair-usage throttling on the trial
- evidence:
  - [1] 2026-11-24: the trial gives 1M tokens per day and stricter rate limits for one month with no credit card required | capture: sha256:a1f124c09515a3964531dab8ae94d984fc2d34a0c038b71721fd9527fed4611a | quote: Get full access to all Core Models. No credit card required, no commitment. Sign up and start building.
  - [1] 2026-11-24: the free trial allows 1M tokens per day | capture: sha256:a1f124c09515a3964531dab8ae94d984fc2d34a0c038b71721fd9527fed4611a | quote: 1M tokens per day
  - [1] 2026-11-24: fair-usage throttling and stricter rate limits apply on the trial | capture: sha256:a1f124c09515a3964531dab8ae94d984fc2d34a0c038b71721fd9527fed4611a | quote: Stricter rate limits
  - [2] 2026-11-24: Regolo charges no egress fees | capture: sha256:f14219fde36022cc108a385deac0c0615068fb5a9593c05d6dd664e914376bb7 | quote: No. Regolo does not charge data egress fees. We believe in open, fair pricing — not in building financial walls around your data.
  - [2] 2026-11-24: subscription plans carry a 20-million-token daily cap, up to 200M on Scale | capture: sha256:f14219fde36022cc108a385deac0c0615068fb5a9593c05d6dd664e914376bb7 | quote: Yes. You can configure daily token limits for your account and individual API keys. The subscription plans includes a 20-million-token daily cap by default (up to 50M on Boost, up to 100M on Pro, up to 200M on Scale), giving you a built-in safety net against runaway costs. Enterprise customers can set custom thresholds tailored to their workloads.
  - [2] 2026-11-24: Regolo retains no prompts, completions or attached files | capture: sha256:f14219fde36022cc108a385deac0c0615068fb5a9593c05d6dd664e914376bb7 | quote: Zero Data Retention means Regolo does not store, log, or retain any of the data you send through our APIs — including prompts, completions, and any attached files.
  - [3] 2026-11-24: sign-up requires completing a registration form and verifying an email address | capture: sha256:88d95d2dd90530601a28d4c04244b511db1936832714c70ccd262a018ea84c1f | quote: 3. Verify your email address
  - [4] 2026-11-24: the API base URL used by the provider is https://api.regolo.ai/v1 | capture: sha256:bc9322d22dc8bcc212491d9f2404620ad1992172635182f0c3c6e012fc7385da | quote: https://api.regolo.ai/v1
  - probe:https://api.regolo.ai/v1/models 2026-11-24: the model list endpoint answered HTTP 200 without a key | capture: sha256:9b76cf1d2c67a723149c729b6375e9daf55710314bfc197b01a4acd92ebff5fb | quote: "status": 200
- sources:
  - [1] https://regolo.ai/pricing/
  - [2] https://regolo.ai/faq/
  - [3] https://docs.regolo.ai/getting-started/sign-up/
  - [4] https://models.dev/providers/regolo-ai
