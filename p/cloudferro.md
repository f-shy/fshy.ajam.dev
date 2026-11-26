# CloudFerro Sherlock

> cloudferro.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudferro/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudferro.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudFerro Sherlock

- `compute/cloudferro-sherlock` | paid-only | evidence documented | binding volume-quota | category managed inference API | tier Managed GenAI Services (Sherlock), Pay Per Use
- needs card no, phone no, ID no, institution no | verified 2026-11-24T18:47:20.586Z (live) | stale on 2026-12-25
- url https://www.cloudferro.com/pricing/
- free tier: unverified: no free token allowance for Sherlock is published on the pricing page, which lists per-1M-token rates only. CloudFerro advertises a separate EUR 250 free cloud-credit trial valid for 6 months, applied to standard Pay-Per-Use pricing; whether Sherlock token usage is eligible is unverified: behind a sign-up. | unit: none | metered on: request-count | read on: 2026-11-24 | source: [1] | note: The free-trial page offers EUR 250 in credits valid for 6 months, subject to an application; Sherlock's own page states 'no minimum commitment' and per-token billing, with no always-free token grant.
- per-object cap: not applicable: the unit is tokens sent to an API, not stored objects; Sherlock keeps 'zero logs · zero storage · no model training on prompts' | source: [2]
- retention: Zero logs and zero storage: prompts and outputs are not stored. No retention period applies to request bytes. | source: [2]
- egress: The Sherlock product page publishes no separate egress price; responses are returned over the API from the WAW3-2 region in Poland. CloudFerro's general cloud price list charges EUR 0.0064 per GB for internet transmission out, but that row is for cloud resources, not token responses, so whether it applies to Sherlock is unverified. | metered: no | source: [2]
- identity: email | detail: The registration page asks for 'Email\*', 'First name\*', 'Last name\*', 'Country\*' and 'Password\*' and offers registration through Google, Microsoft, GitHub, LinkedIn, GitLab, yahoo!, BitBucket, X, Creodias, EGI Check In, DUNIA and CODE-DE3. The form asks for no card, phone number or ID document.
- interface: rest, browser
- limits:
  - volume-quota (binding): Per-token billing: the Llama-3.3-70B-Instruct row is EUR 0.35 per 1M input tokens and EUR 0.65 per 1M output tokens; nine models are listed from EUR 0.10 to EUR 0.30 input and EUR 0.15 to EUR 4.00 output per 1M tokens; no free token allowance or minimum commitment is stated [1]
  - write-gated: Code-based access requires an account in My Portal, a Sherlock project, and an API key created in the Sherlock console; the free-trial credits require creating an account and applying [3]
- limits note: Per-token pricing with monthly invoicing and spend alerts; the product page states a 99.9% uptime SLA. The EUR 250 free-trial credit is valid for 6 months and is described as 'considered per applicant and revocable' on the trial page; the identity fields of the My Portal registration form were not readable.
- binding note: Every request spends tokens at the published per-1M-token rates and there is no always-free token allowance, so the token meter is what runs out first for a caller with no trial credit.
- interface detail: OpenAI-compatible REST API (chat, completions, embeddings) at https://api-sherlock.cloudferro.com/openai/v1 plus a web Playground and assistants; a Sherlock API key is created in the console after login.
- endpoint: https://api-sherlock.cloudferro.com/openai/v1/
- tooling: the openai Python and JS SDKs with base_url swapped, LangChain and LlamaIndex via the OpenAI-compatible provider, CloudFerro Jupyter Notebooks, Managed Airflow and Managed Kubernetes; models.dev lists 5 models under id cloudferro-sherlock with package @ai-sdk/openai-compatible.
- composes with: Sherlock completions and embeddings combine with CloudFerro Object Storage and Functions for RAG over document and Earth-observation corpora, all inside the EU WAW3-2 region.
- reliability: The vendor states zero logs, zero storage and no model training on prompts, processing confined to the WAW3-2 region in Poland, and a 99.9% uptime SLA. No throttle or outage was observed; no request was made.
- notes: Sherlock has no published always-free token grant: the first-party price list is per 1M tokens in EUR and the product page states 'no minimum commitment'. The EUR 250 trial credit is a separate, application-gated offer whose eligibility for Sherlock usage was not read. A separate record may be warranted if the trial is confirmed to cover Sherlock.
- evidence note: Rates and the zero-storage policy are quoted from CloudFerro's own pricing and Sherlock product pages read 2026-11-24; the API/account gate is quoted from the Sherlock user guide read the same day. models.dev is a third-party catalogue used only to corroborate the API base and model count. No live request was measured.
- extras:
  - shape.note: a managed token API; no machine shape is published
  - billing_model: pay as you go per 1M input and output tokens, monthly invoicing
  - free_tier_kind: none published for Sherlock; separate EUR 250 six-month credit trial
  - term: no minimum commitment
  - price_arithmetic: EUR 0.35 per 1M input and EUR 0.65 per 1M output tokens for Llama-3.3-70B-Instruct from the CloudFerro price list
  - status: managed service live in WAW3-2 Poland
  - models: 5 models listed in models.dev: Bielik 11B, GLM-5.3, Llama-3.3-70B, MiniMax-M2.5, GPT OSS 120B
- evidence:
  - [1] 2026-11-24: the Sherlock Llama-3.3-70B-Instruct rate is EUR 0.35 per 1M input tokens and EUR 0.65 per 1M output tokens | capture: sha256:278f1c893b33e7fa9c918894de4a3f9b408f6424bda7ba424740c509f35a1831 | quote: | meta-llama/Llama-3.3-70B-Instruct | 0,35 | 0,65 |
  - [1] 2026-11-24: prices are in EUR excluding VAT, and general cloud internet transmission out is EUR 0.0064 per GB | capture: sha256:278f1c893b33e7fa9c918894de4a3f9b408f6424bda7ba424740c509f35a1831 | quote: | Internet transmission out | per GByte | 0,0064 | 0,0064 | 0,0064 | 0,0064 | - |
  - [1] 2026-11-24: CloudFerro states all prices are in EUR excluding VAT | capture: sha256:278f1c893b33e7fa9c918894de4a3f9b408f6424bda7ba424740c509f35a1831 | quote: All prices are in EUR, excluding VAT.
  - [2] 2026-11-24: Sherlock is an OpenAI-compatible REST API at api-sherlock.cloudferro.com/openai/v1 with per-token, pay-as-you-go billing and no minimum commitment | capture: sha256:2f5b14212bc920516eff9587cfb3152e9d3288e3bba6cd903aeebe62a0a72611 | quote: Swap your base_url to https://api-sherlock.cloudferro.com/openai/v1 and insert your API key. Your existing OpenAI SDK code runs unchanged — no refactoring, no new libraries, no workflow disruption.
  - [2] 2026-11-24: Sherlock keeps zero logs and zero storage and processes in the WAW3-2 region in Poland | capture: sha256:2f5b14212bc920516eff9587cfb3152e9d3288e3bba6cd903aeebe62a0a72611 | quote: Zero logs · zero storage · no model training on prompts
  - [2] 2026-11-24: billing is pay-as-you-go per 1M tokens with monthly invoicing, budget caps and no minimum commitment | capture: sha256:2f5b14212bc920516eff9587cfb3152e9d3288e3bba6cd903aeebe62a0a72611 | quote: Per-token pricing, real-time usage dashboards, budget caps, and spend alerts give both engineering and finance teams full control — no surprises, no minimum commitment.
  - [4] 2026-11-24: CloudFerro offers EUR 250 in free cloud credits valid for 6 months under standard Pay-Per-Use pricing | capture: sha256:6b46272a10d04bdd65b3cb0dc3cc7e03aef946478b5f5a5335079f5f7fc75060 | quote: - €250 in free cloud credits\*
  - [3] 2026-11-24: API access needs a Sherlock project and an API key created in the console | capture: sha256:9391fa5081bf7aa2581ac29212e33bce8f97267df2598456181a200345375de8 | quote: Create an API key in the console, then use the getting-started guide to install the client, configure authentication, and send a first request.
  - [5] 2026-11-24: a third-party catalogue lists 5 Sherlock models at this API base with package @ai-sdk/openai-compatible | capture: sha256:890d638202311f2aa8ccbccecc50a080957efc9ec245711955cf7251a33ea251 | quote: https://api-sherlock.cloudferro.com/openai/v1/
  - [6] 2026-11-24: the registration form requires an email, first name, last name and country | capture: sha256:d358b7f7beb3d843e2a69c19a4e313ec04987eafbdd607340160a67727f6f7fc | quote: Email\* First name\* Last name\* Country\*
  - [6] 2026-11-24: an email address is the sign-up gate, with no card, phone or ID field on the form | capture: sha256:d358b7f7beb3d843e2a69c19a4e313ec04987eafbdd607340160a67727f6f7fc | quote: Email\* First name\* Last name\* Country\*
- sources:
  - [1] https://www.cloudferro.com/pricing/
  - [2] https://sherlock.cloudferro.com/en/
  - [3] https://docs.cloudferro.com/en/latest/sherlock/sherlock.html
  - [4] https://www.cloudferro.com/pricing/free-trial/
  - [5] https://models.dev/providers/cloudferro-sherlock/
  - [6] https://portal.cloudferro.com/register/
