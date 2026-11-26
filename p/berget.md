# Berget.AI

> berget.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/berget/ | JSON https://fshy.ajam.dev/api/v1/entity/berget.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Berget.AI

- `compute/berget-serverless-trial` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API | tier Trial (Serverless Inference)
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T18:27:26.888Z (live) | stale on 2026-12-25
- url https://berget.ai/en/pricing
- free tier: Trial at EUR 0 a month with EUR 5 in starting credits, basic rate limits and community support; the FAQ states 'a card is required at signup to prevent abuse, but nothing is charged', and after the trial an active plan from EUR 25 a month in prepaid credits is required. | unit: credits | metered on: request-count | read on: 2026-11-24 | source: [1] | note: The EUR 5 credit is one-time and the console lists it as valid for three months. Two first-party pages conflict on the card: the pricing FAQ says 'a card is required at signup to prevent abuse, but nothing is charged', while the console bundle's Trial feature list says 'No credit card required'.
- per-object cap: not applicable: the unit is an API request, not a stored object
- retention: Unused prepaid credits roll over to the next month and remain valid for 12 months; after cancellation the remaining credits can be used for 30 days. | source: [1]
- egress: The Serverless Inference page states 'No egress fees' for the inference API: 'Pay per token, or pick a plan for predictable spend. No egress fees.' The 'Data trafficInbound and outbound, not metered' row belongs to the separate managed Kubernetes Cluster price table. | metered: no | free allowance: no egress fees on Serverless Inference, as stated on its own product page | source: [1]
- identity: card | detail: The pricing FAQ states 'a card is required at signup to prevent abuse, but nothing is charged'. The console registration submits a name, email and timezone and accepts terms, privacy and DPA; a card intervention is conditional on bot detection. The console bundle's Trial feature list says 'No credit card required', so the two first-party pages conflict. No phone number or ID document is stated.
- interface: rest
- limits:
  - request-rate: Basic rate limits on Trial, increased on Starter, higher on Team, maximum on Enterprise; the pricing page states 'Rate limits are shared per account' and publishes no number [1]
  - volume-quota (binding): EUR 5 in starting credits on Trial, then an active plan from EUR 25 a month in prepaid credits is required for continued API access [1]
- binding note: The EUR 5 starting credit is a one-time amount that is spent by token usage and gates continued access once exhausted; the rate limit is an unpublished qualifier and is not a number that binds first.
- interface detail: OpenAI-compatible inference API at https://api.berget.ai/v1 for chat completions, embeddings and model discovery; the documented call uses a Bearer API key obtained from the console.
- endpoint: part of interface detail
- tooling: the official OpenAI SDK with base_url set to https://api.berget.ai/v1, or curl against /v1/chat/completions; SDKs are documented for Python and TypeScript
- composes with: A drop-in OpenAI endpoint that a coding agent or an existing OpenAI SDK application can point at; the managed Kubernetes cluster adds object storage and unmetered data traffic for pipelines that need it.
- reliability: Rate limits are shared per account and no numeric ceiling is published; unused credits expire 12 months after they are added and 30 days after cancellation.
- notes: The trial requires a card at signup even though nothing is charged; rate limits are tiered but only as words, with no published number. The managed Kubernetes cluster is a separate paid service with unmetered inbound and outbound data traffic; this record prices the Serverless Inference trial.
- evidence note: The plan prices, the starting credit, the card gate and the unmetered cluster traffic are quoted from the vendor's pricing page read on 2026-11-24; the signup fields and the trial credit validity come from the console bundle read the same day.
- extras:
  - shape.note: serverless inference: no fixed machine shape is exposed
  - billing_model: one-time prepaid credits, then a monthly prepaid plan
  - free_tier_kind: one-time-credit
  - term: the console lists the trial credit as valid for three months
  - network_out.allow_outbound: yes
  - network_out.ports: not stated
  - session_cap.restart_required: no
  - session_cap.note: no per-session time cap is published
- evidence:
  - [1] 2026-11-24: the Trial plan is EUR 0 a month with EUR 5 free starting credits and basic rate limits | capture: sha256:b65e5562d264fc67806875f93c6367d553f336b59c8c1a9e1d73e5f0db4dc6eb | quote: ### Trial €0 / month For the hobbyist - €5 free starting credits - Basic rate limits* - Community support - No monthly cost
  - [1] 2026-11-24: a card is required at signup with no charge, and continued API access needs a plan from EUR 25 a month | capture: sha256:b65e5562d264fc67806875f93c6367d553f336b59c8c1a9e1d73e5f0db4dc6eb | quote: The Trial plan includes €5 in starting credits so you can try the API without a subscription — a card is required at signup to prevent abuse, but nothing is charged. After that, an active plan (from €25 / month in prepaid credits) is required for continued API access — we don't offer pure pay-as-you-go without a plan.
  - [1] 2026-11-24: the published paid plans start at EUR 25 a month and rate limits are shared per account | capture: sha256:b65e5562d264fc67806875f93c6367d553f336b59c8c1a9e1d73e5f0db4dc6eb | quote: ### Starter €25 / month For small projects - €25 monthly top-up - Increased rate limits* - Email support - Automatic billing * Rate limits are shared per account.
  - [1] 2026-11-24: unused credits roll over for 12 months and remain available 30 days after cancellation | capture: sha256:b65e5562d264fc67806875f93c6367d553f336b59c8c1a9e1d73e5f0db4dc6eb | quote: On a paid plan you can add one-off top-ups or set up automatic top-up rules. Unused credits roll over to the next month and remain valid for 12 months.
  - [2] 2026-11-24: the console's trial entitlement is a EUR 5 initial wallet credit, valid for three months and listed without a card requirement | capture: sha256:9abe2a271a50a311feb069075141e23d21876eece631a2514eab5b1d3f3794e9 | quote: features_list:["5€ initial wallet credit","Valid for three months","No credit card required"]
  - [2] 2026-11-24: the console registration submits a name, email and timezone and selects the trial plan | capture: sha256:9abe2a271a50a311feb069075141e23d21876eece631a2514eab5b1d3f3794e9 | quote: b={user:{name:j,email:N,timezone:Intl.DateTimeFormat().resolvedOptions().timeZone},company:H?{name:y.company.name||j,email:y.company.email||N,vatNumber:I?(k=y.company.vatNumber)==null?void 0:k.trim():void 0,address:{street:((R=y.company.address)==null?void 0:R.street)||"",city:((A=y.company.address)==null?void 0:A.city)||"",zip:((O=y.company.address)==null?void 0:O.zip)||"",countryCode:((z=y.company.address)==null?void 0:z.countryCode)||"SE"}}:void 0,individual:H?void 0:{countryCode:y.company.countryCode||"SE",discountCode:y.company.discountCode||void 0},plans:[{id:"trial",quantity:1}]
  - [3] 2026-11-24: the inference API is OpenAI-compatible at https://api.berget.ai/v1 and needs an account and a console API key | capture: sha256:63d2a15dac46092731493c7dac8a39fa58e72ac5432ee403dd7a9be2e604cb74 | quote: Berget AI Serverless Inference is a drop-in replacement for the OpenAI API. Point any OpenAI-compatible SDK or tool at `https://api.berget.ai/v1` and it works.
  - [4] 2026-11-24: the API exposes OpenAI-compatible chat completions, embeddings, transcription and model discovery endpoints | capture: sha256:4ac0fb45db9c115245c78f14c025056b26412d47ed77c32a47776ddeddfe0183 | quote: OpenAI-compatible inference API for chat completions, embeddings, audio transcription, and model discovery.
  - [5] 2026-11-24: the model catalogue reports per-model EUR prices and live status without a request key | capture: sha256:8a90f52ea9b720a6a6699b2b360a723e24f6f8e1f12d8091db8317a42df30786 | quote: "pricing":{"currency":"EUR","input":0.25,"output":0.5,"unit":"€ / M Token"}
  - [6] 2026-11-24: the serverless inference page states the inference API has no egress fees | capture: sha256:5ae68ab29521e4e13b16de00801e6de9bd4f2d772af3cbf28f75a3f603f73879 | quote: Pay per token, or pick a plan for predictable spend. No egress fees.
  - [6] 2026-11-24: the serverless inference page states no egress fees, rather than a Kubernetes traffic allowance | capture: sha256:5ae68ab29521e4e13b16de00801e6de9bd4f2d772af3cbf28f75a3f603f73879 | quote: Pay per token, or pick a plan for predictable spend. No egress fees.
  - [6] 2026-11-24: the serverless inference page's pricing section states no egress fees | capture: sha256:5ae68ab29521e4e13b16de00801e6de9bd4f2d772af3cbf28f75a3f603f73879 | quote: Pay per token, or pick a plan for predictable spend. No egress fees.
- sources:
  - [1] https://berget.ai/en/pricing
  - [2] https://console.berget.ai/assets/index-Bjea3Xay.js
  - [3] https://docs.berget.ai/quickstart
  - [4] https://api.berget.ai/
  - [5] https://api.berget.ai/v1/models/
  - [6] https://berget.ai/en/serverless-inference
