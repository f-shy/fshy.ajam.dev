# Groq

> groq.com | Inference, Compute, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/groq/ | JSON https://fshy.ajam.dev/api/v1/entity/groq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Groq

- `inference/groq` | qualifies-with-caveat | evidence documented | binding request-rate | category inference endpoint, keyed free tier
- needs card no, phone no, ID no, institution no | verified 2026-10-31T00:12:52.378Z (live) | stale on 2026-12-01
- url https://console.groq.com/docs/rate-limits
- free tier: a Free Plan per model, printed as RPM / RPD / TPM / TPD in the page's own units: openai/gpt-oss-120b and openai/gpt-oss-20b at 30 / 1K / 8K / 200K, qwen/qwen3.8-27b the same, and openai/gpt-oss-safeguard-20b at 3 / 1K / 2K / 200K. The page writes requests-per-day and tokens-per-day in thousands, so 1K is 1,000 and 200K is 200,000 | unit: tokens | metered on: request-count | read on: 2026-10-22 | source: [1] | note: the Free Plan Limits tab lists 10 model rows, each printed per model id as RPM, RPD, TPM, TPD, ASH and ASD; K means thousands, so 1K is 1,000 and 200K is 200,000. The Developer Plan Limits tab is a separate table
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: one form, Create Account or Login, serves both sign-up and login with Google, GitHub, SSO and email; the served auth config lists only OAuth (Google, GitHub), SSO and email magic links, so the email route is a magic link and there is no password and no SMS method. The sign-up request carries only the session token and an optional referral code, with a Stytch device telemetry ID header: no phone number and no card. A payment method (credit card, US bank account or SEPA debit account) is required only to upgrade from the Free tier to the Developer tier. Creating an API key requires a Cloudflare Turnstile token.
- interface: rest
- limits:
  - request-rate (binding): 30 / 1K / 8K / 200K on the Free plan for openai/gpt-oss-120b and openai/gpt-oss-20b, in the page's own units: 30 requests a minute, 1K requests a day, 8K tokens a minute and 200K tokens a day [1]
  - request-rate (binding): RPM, RPD, TPM, TPD, ASH, ASD, ITPM and OTPM, applied at organisation level and not per user; every dimension is evaluated and the first threshold reached binds. Cached tokens count toward none of them [1]
  - request-rate (binding): Free plan, per model id, in the page's own units where K is thousands: whisper-large-v3 and whisper-large-v3-turbo 20 RPM, 2K RPD, 7.2K ASH and 28.8K ASD; canopylabs/orpheus-arabic-saudi and canopylabs/orpheus-v1-english 10 RPM, 100 RPD, 1.2K TPM and 3.6K TPD; meta-llama/llama-prompt-guard-2-22m and meta-llama/llama-prompt-guard-2-86m 30 RPM, 14.4K RPD, 15K TPM and 500K TPD [1]
- binding note: TPD binds on the workload: 200,000 tokens a day is 6.0M a month, which is 11.4 per cent of a 52.5M-token monthly target. The 30 rpm and 8,000 tpm figures are both workable for an interactive session
- endpoint: https://api.groq.com/openai/v1/chat/completions
- tooling: any OpenAI-compatible client; curl against POST {base}/chat/completions
- composes with: pairs with a free-standing agent as the email-gated fallback when a keyless endpoint's ceiling binds; the 200,000-token daily cap is the scarce link, not the request rate
- reliability: No reliability events were recorded. API keys were not provisioned during evaluation on 2026-10-31.
- notes: Groq specifies six limit dimensions and publishes exact values for free tiers. Pipelines sized primarily on RPM encounter daily token constraints first: an allowance of 200,000 tokens per day yields approximately 6.0M tokens monthly.
- evidence note: the dimensions, the organisation scope and the seven-row free-plan table are all quoted from the served page read. No key was available, so the enforcement of any of the numbers is not measured.
- evidence:
  - [1] 2026-10-22: limits are RPM, RPD, TPM, TPD, ITPM and OTPM, applied at organisation level, evaluated against every dimension with the first reached binding; cached tokens do not count; the Free Plan Limits tab carries seven model rows, of which openai/gpt-oss-120b and openai/gpt-oss-20b are 30 rpm, 1K rpd, 8K tpm and 200K tpd The Free Plan Limits tab prints the cells as 30 / 1K / 8K / 200K, and the page's K suffix means thousands
  - [1] 2026-10-28: the Free Plan Limits table gives openai/gpt-oss-120b and openai/gpt-oss-20b 30 RPM, 1K RPD, 8K TPM and 200K TPD | capture: sha256:76a455bc91d97dec99ddbbeef8e004ff77555860472a6a72491278686ceecbb4 | quote: | openai/gpt-oss-120b | 30 | 1K | 8K | 200K | - | - | | openai/gpt-oss-20b | 30 | 1K | 8K | 200K | - | - |
  - [1] 2026-10-28: the Free Plan Limits table gives openai/gpt-oss-safeguard-20b 3 / 1K / 2K / 200K and qwen/qwen3.8-27b 30 / 1K / 8K / 200K | capture: sha256:76a455bc91d97dec99ddbbeef8e004ff77555860472a6a72491278686ceecbb4 | quote: | openai/gpt-oss-safeguard-20b | 3 | 1K | 2K | 200K | - | - | ... | qwen/qwen3.8-27b | 30 | 1K | 8K | 200K | - | - |
  - [1] 2026-10-28: the page lists RPM, RPD, TPM, TPD, ASH, ASD, ITPM and OTPM, applies limits at organization level, binds on the first threshold reached, and excludes cached tokens | capture: sha256:0ed538b5ae8eb25c29baac2e8fa726d75ebd0a9bbb7ae405247f47053093fb00 | quote: ASH: Audio seconds per hour ... ASD: Audio seconds per day ... do not count towards your rate limits. Rate limits apply at the organization level, not individual users. You can hit any limit type depending on which threshold you reach first.
  - [1] 2026-10-28: the Free Plan Limits table lists whisper, orpheus and llama-prompt-guard rows with these RPM, RPD, TPM, TPD, ASH and ASD cells | capture: sha256:76a455bc91d97dec99ddbbeef8e004ff77555860472a6a72491278686ceecbb4 | quote: | whisper-large-v3 | 20 | 2K | - | - | 7.2K | 28.8K | ... | canopylabs/orpheus-v1-english | 10 | 100 | 1.2K | 3.6K | - | - | ... | meta-llama/llama-prompt-guard-2-22m | 30 | 14.4K | 15K | 500K | - | - |
  - [1] 2026-10-28: the Free Plan Limits tab table prints the cells with a K suffix and one row per model id | capture: sha256:76a455bc91d97dec99ddbbeef8e004ff77555860472a6a72491278686ceecbb4 | quote: | openai/gpt-oss-120b | 30 | 1K | 8K | 200K | - | - |
  - [2] 2026-10-28: a payment method is asked for only at the upgrade from the Free tier, so the Free tier itself needs none | capture: sha256:5a86f7cdf25eebd2b90d0dd4b7c2f280e287afbca704314de363888f7d62d109 | quote: To upgrade from the Free tier to the Developer tier, you'll need to provide a valid payment method (credit card, US bank account, or SEPA debit account).
  - [3] 2026-10-30: one form serves both sign-up and login and offers Google, GitHub, SSO and email; it shows no phone field and no card field | capture: sha256:7b3621cd00d27f9c4912a14a1a6f21e910dcea80c952e9d97bd00c95757af8a1 | quote: Create Account or Login Continue with Google Continue with GitHub Continue with SSO or Continue with email
  - [3] 2026-10-30: the served login page loads the script chunk that holds its auth config and its sign-up request | capture: sha256:d8ac4038467fa4dc242a70ae2c3b582aa50be9617ac375614c68987f28c00c40 | quote: <script src="/_next/static/chunks/3747-f8960cfaa0d0067b.js" async=""></script>
  - [4] 2026-10-30: the login widget's products are OAuth with Google and GitHub, SSO and email magic links; no password product and no SMS product is configured | capture: sha256:44e436cce3539271eb204e6ee4207b1d3d4f9ca70bd517b21c334c9251c00b4d | quote: products:[o.Ll.oauth,o.Ll.sso,o.Ll.emailMagicLinks],oauthOptions:{providers:[{type:"google"},{type:"github"}]
  - [4] 2026-10-30: the sign-up request body holds only the intermediate session token and an optional referral code, so sign-up sends no phone number and no card | capture: sha256:44e436cce3539271eb204e6ee4207b1d3d4f9ca70bd517b21c334c9251c00b4d | quote: let l={};t&&(l.intermediate_session_token=t);... d&&d.createdAt>g&&(l.referral_code=d.source);let f={method:"POST",... body:JSON.stringify(l)},m=await fetch("".concat(s.Ko,"/user/profile/signupb2b"),f)
  - [4] 2026-10-30: the sign-up request carries a Stytch device telemetry ID header | capture: sha256:44e436cce3539271eb204e6ee4207b1d3d4f9ca70bd517b21c334c9251c00b4d | quote: headers:{"content-type":"application/json","x-stytch-telemetry-id":p}
  - [5] 2026-10-30: the API key form refuses to submit without a Cloudflare Turnstile token (cfToken) | capture: sha256:589b494a980ef5a38301f5453513f690320d47b75e7723b75011bfd35fdce5e1 | quote: J=async e=>{try{if(!i)throw Error("No cfToken")
  - [5] 2026-10-30: the key-creation request sends a name, the Turnstile token, a verification token and an expiry; no phone number and no card | capture: sha256:589b494a980ef5a38301f5453513f690320d47b75e7723b75011bfd35fdce5e1 | quote: h=await fetch(p,{method:"POST",body:JSON.stringify({name:r,cf_token:l,vb_token:d,expires_at:null==n?void 0:n.toISOString()}),headers:i})
  - [2] 2026-10-30: a payment method is asked for only at the upgrade from the Free tier to the Developer tier | capture: sha256:d31a821ba5edb28d3d2ecc19b38401c5eba23a86fe0821b589985af4fdffbbce | quote: To upgrade from the Free tier to the Developer tier, you'll need to provide a valid payment method (credit card, US bank account, or SEPA debit account).
  - [6] 2026-10-30: a third-party photo-ID or selfie check is named, with no trigger stated | capture: sha256:b44bc38ee18be9e933405aaa44e755e3dcaaf375b1775f67230ea95ee3844ea4 | quote: We may use third-party identity verification services to verify your identity, secure our Services, and protect against fraud or abuse. When you engage in this process, you provide information, such as a photo ID or selfie, directly to that service.
  - [7] 2026-10-30: a third-party guide reports that sign-up asks for no payment information | capture: sha256:d02def7bb3bc99adeceb39e72661fc724dab888b53fc2a4a05816784f7a3dde7 | quote: No payment information is required. The free tier is immediately active.
  - [8] 2026-10-30: a third-party guide reports the same email, Google, GitHub and SSO sign-up methods | capture: sha256:e1b66c91a55e981fe0d9c9a9a4c7cb200df4ecc252c094211cdcda592e7f2b9e | quote: Go to console.groq.com and sign up with your email address, Google, GitHub, or SSO.
  - probe:https://api.groq.com/openai/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:bb7048d2c555b3b7602cee0b2f5aba0898fbfeb111388e0b979b81f1231000a3 | quote: "status": 401
- sources:
  - [1] https://console.groq.com/docs/rate-limits
  - [2] https://console.groq.com/docs/billing-faqs
  - [3] https://console.groq.com/login
  - [4] https://console.groq.com/_next/static/chunks/3747-f8960cfaa0d0067b.js
  - [5] https://console.groq.com/_next/static/chunks/app/(console)/keys/page-c4f59a80093392e3.js
  - [6] https://groq.com/privacy-policy
  - [7] https://sfailabs.com/guides/how-to-get-groq-api-key
  - [8] https://www.getmaxim.ai/guides/api-keys/how-to-get-a-groq-api-key

## Groq Cloud

- `compute/groq-cloud` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-31T00:12:52.379Z (live) | stale on 2026-12-01
- url https://console.groq.com/docs/rate-limits
- free tier: A free plan per model, printed as RPM / RPD / TPM / TPD: openai/gpt-oss-120b and openai/gpt-oss-20b at 30 requests a minute, 1,000 a day, 8,000 tokens a minute and 200,000 tokens a day, which works out to 6.0M tokens a month per model. Paid Developer rates for the same model are USD 0.15 per 1M input and USD 0.60 per 1M output at 1,000 RPM and 250K TPM. | unit: tokens | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-daily-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: one form, Create Account or Login, serves both sign-up and login with Google, GitHub, SSO and email; the served auth config lists only OAuth (Google, GitHub), SSO and email magic links, so the email route is a magic link and there is no password and no SMS method. The sign-up request carries only the session token and an optional referral code, with a Stytch device telemetry ID header: no phone number and no card. A payment method (credit card, US bank account or SEPA debit account) is required only to upgrade from the Free tier to the Developer tier. Creating an API key requires a Cloudflare Turnstile token.
- interface: rest
- limits:
  - request-rate (binding): the 8,000 tokens a minute binds before the 200,000 a day: at 8K TPM the day's whole allowance is reachable in 25 minutes of continuous traffic, so the pool is spent by mid-morning and the rest of the day is idle unless the job is paced. [1]
- limits note: the 8,000 tokens a minute binds before the 200,000 a day: at 8K TPM the day's whole allowance is reachable in 25 minutes of continuous traffic, so the pool is spent by mid-morning and the rest of the day is idle unless the job is paced.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the daily pool is small but the latency is the point: 500 tokens a second on this model spends the 200K-token day in about 7 minutes of generation, so Groq is the cheap first pass and Cloudflare or DeepSeek takes the volume.
- reliability: no reliability event recorded
- notes: Arithmetic, labelled estimate: 200,000 tokens a day is 6.0M a month per model, and about 24M a month across the four free text models if every model is used. At the Developer rate that 6.0M is worth roughly USD 0.90 to USD 3.60 a month depending on the input/output split. GPU-equivalent, labelled estimate: 6.0M output tokens a month at 500 tokens a second is about 3.3 hours of continuous single-stream generation a month. Confirms earlier readings record (inference/groq): the numbers are unchanged on 2026-10-22. Adds the capacity shape, which that record does not carry.
- extras:
  - facets.class: capacity-shape
  - facets.free_tier_kind: recurring-daily-allowance
  - facets.shape.gpu_class: LPU
- evidence:
  - [1] 2026-10-22: 'openai/gpt-oss-120b | 30 | 1K | 8K | 200K' in the free plan rate limit table, quoted
  - [2] 2026-10-22: Developer plan pricing for gpt-oss-120b at $0.15 input and $0.60 output per 1M tokens with 250K TPM and 1K RPM, quoted
  - [1] 2026-10-22: 'Rate limits apply at the organization level, not individual users. You can hit any limit type depending on which threshold you reach first', quoted
  - [1] 2026-10-28: the served page lists this row under Free Plan Limits, the tab selected by default, and the Developer Plan Limits tab lists 1K RPM, 500K RPD and 250K TPM for the same model | capture: sha256:9015b2d9f7cab6652779f79f09e0d2c86b67f241e9c93ee3f68bc81ba06d5671 | quote: | openai/gpt-oss-120b | 30 | 1K | 8K | 200K | - | - |
  - [2] 2026-10-28: the models page prices openai/gpt-oss-120b at $0.15 input and $0.60 output per 1M tokens with 250K TPM and 1K RPM on the Developer plan | capture: sha256:1156b95194ab22553056a57e793dc84c818cf3b3cc70da351982388b1c49f11a | quote: | [OpenAIGPT OSS 120B](https://console.groq.com/docs/model/openai/gpt-oss-120b)openai/gpt-oss-120b | 500 | $0.15 input$0.60 output | 250K TPM1K RPM | 131,072 | 65,536 | - |
  - [3] 2026-10-28: a payment method is named for the upgrade from the Free tier to the Developer tier | capture: sha256:5a86f7cdf25eebd2b90d0dd4b7c2f280e287afbca704314de363888f7d62d109 | quote: To upgrade from the Free tier to the Developer tier, you'll need to provide a valid payment method (credit card, US bank account, or SEPA debit account).
  - [4] 2026-10-30: one form serves both sign-up and login and offers Google, GitHub, SSO and email; it shows no phone field and no card field | capture: sha256:7b3621cd00d27f9c4912a14a1a6f21e910dcea80c952e9d97bd00c95757af8a1 | quote: Create Account or Login Continue with Google Continue with GitHub Continue with SSO or Continue with email
  - [4] 2026-10-30: the served login page loads the script chunk that holds its auth config and its sign-up request | capture: sha256:d8ac4038467fa4dc242a70ae2c3b582aa50be9617ac375614c68987f28c00c40 | quote: <script src="/_next/static/chunks/3747-f8960cfaa0d0067b.js" async=""></script>
  - [5] 2026-10-30: the login widget's products are OAuth with Google and GitHub, SSO and email magic links; no password product and no SMS product is configured | capture: sha256:44e436cce3539271eb204e6ee4207b1d3d4f9ca70bd517b21c334c9251c00b4d | quote: products:[o.Ll.oauth,o.Ll.sso,o.Ll.emailMagicLinks],oauthOptions:{providers:[{type:"google"},{type:"github"}]
  - [5] 2026-10-30: the sign-up request body holds only the intermediate session token and an optional referral code, so sign-up sends no phone number and no card | capture: sha256:44e436cce3539271eb204e6ee4207b1d3d4f9ca70bd517b21c334c9251c00b4d | quote: let l={};t&&(l.intermediate_session_token=t);... d&&d.createdAt>g&&(l.referral_code=d.source);let f={method:"POST",... body:JSON.stringify(l)},m=await fetch("".concat(s.Ko,"/user/profile/signupb2b"),f)
  - [5] 2026-10-30: the sign-up request carries a Stytch device telemetry ID header | capture: sha256:44e436cce3539271eb204e6ee4207b1d3d4f9ca70bd517b21c334c9251c00b4d | quote: headers:{"content-type":"application/json","x-stytch-telemetry-id":p}
  - [6] 2026-10-30: the API key form refuses to submit without a Cloudflare Turnstile token (cfToken) | capture: sha256:589b494a980ef5a38301f5453513f690320d47b75e7723b75011bfd35fdce5e1 | quote: J=async e=>{try{if(!i)throw Error("No cfToken")
  - [6] 2026-10-30: the key-creation request sends a name, the Turnstile token, a verification token and an expiry; no phone number and no card | capture: sha256:589b494a980ef5a38301f5453513f690320d47b75e7723b75011bfd35fdce5e1 | quote: h=await fetch(p,{method:"POST",body:JSON.stringify({name:r,cf_token:l,vb_token:d,expires_at:null==n?void 0:n.toISOString()}),headers:i})
  - [3] 2026-10-30: a payment method is asked for only at the upgrade from the Free tier to the Developer tier | capture: sha256:d31a821ba5edb28d3d2ecc19b38401c5eba23a86fe0821b589985af4fdffbbce | quote: To upgrade from the Free tier to the Developer tier, you'll need to provide a valid payment method (credit card, US bank account, or SEPA debit account).
  - [7] 2026-10-30: a third-party photo-ID or selfie check is named, with no trigger stated | capture: sha256:b44bc38ee18be9e933405aaa44e755e3dcaaf375b1775f67230ea95ee3844ea4 | quote: We may use third-party identity verification services to verify your identity, secure our Services, and protect against fraud or abuse. When you engage in this process, you provide information, such as a photo ID or selfie, directly to that service.
  - [8] 2026-10-30: a third-party guide reports that sign-up asks for no payment information | capture: sha256:d02def7bb3bc99adeceb39e72661fc724dab888b53fc2a4a05816784f7a3dde7 | quote: No payment information is required. The free tier is immediately active.
  - [9] 2026-10-30: a third-party guide reports the same email, Google, GitHub and SSO sign-up methods | capture: sha256:e1b66c91a55e981fe0d9c9a9a4c7cb200df4ecc252c094211cdcda592e7f2b9e | quote: Go to console.groq.com and sign up with your email address, Google, GitHub, or SSO.
- sources:
  - [1] https://console.groq.com/docs/rate-limits
  - [2] https://console.groq.com/docs/models
  - [3] https://console.groq.com/docs/billing-faqs
  - [4] https://console.groq.com/login
  - [5] https://console.groq.com/_next/static/chunks/3747-f8960cfaa0d0067b.js
  - [6] https://console.groq.com/_next/static/chunks/app/(console)/keys/page-c4f59a80093392e3.js
  - [7] https://groq.com/privacy-policy
  - [8] https://sfailabs.com/guides/how-to-get-groq-api-key
  - [9] https://www.getmaxim.ai/guides/api-keys/how-to-get-a-groq-api-key

## groq files api

- `storage/groq-files-api` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://console.groq.com/docs/api-reference
- free tier: none reachable: Batch-only purpose, .jsonl only, 100 MB max file. No general-purpose storage class. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Batch-only purpose, .jsonl only, 100 MB max file. No general-purpose storage class.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Batch-only purpose, .jsonl only, 100 MB max file. No general-purpose storage class.
  - [2] 2026-10-21: cited as the basis of the rejection: Batch-only purpose, .jsonl only, 100 MB max file. No general-purpose storage class.
- sources:
  - [1] https://console.groq.com/docs/api-reference
  - [2] https://raw.githubusercontent.com/api-evangelist/groq/refs/heads/main/openapi/groq-batch-api-openapi.yml

## Hosted inference APIs (as a compute class)

- `compute/inference-api-hosts` | dead | evidence reported | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22T04:47:11.088Z (live) | stale on 2026-11-06
- url https://groq.com/pricing/
- free tier: grouped row: an inference API answers tokens and is not a machine you can leave running | unit: tokens | metered on: request-count | read on: 2026-10-06 | source: [1] | note: Recorded separately to distinguish API endpoints from hosted compute.
- per-object cap: not applicable
- retention: no machine and no disk | days: 0 | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: an API key from an account
- interface: ssh
- limits:
  - request-rate (binding): per-key and per-minute token limits set by each provider, as the earlier read recorded; this page does not restate them [1]
- limits note: no session, no disk, no SSH: provider listings counts this class by mistake.
- interface detail: an HTTP completion API
- tooling: any OpenAI-compatible client
- composes with: belongs to the inference topic; it cannot run a shell or serve a file
- reliability: no reliability event recorded
- notes: Offering represents an inference API rather than general compute.
- evidence note: the site was read on 2026-10-22 and the extracted body is the marketing page rather than the pricing table, so this grouped record's rate limit statement cannot be re-confirmed here. The record is a grouping row and says so
- extras:
  - billing_model: per-request
  - session_cap.restart_required: no
  - session_cap.note: an inference API answers tokens and holds no machine, which is why the record is a grouping row
  - free_tier_kind: none
- evidence:
  - [1] 2026-10-06: 
  - [1] 2026-10-22: the Groq site was read on 2026-10-22 and carries its funding announcement and a console signup; the pricing table the record's URL names is not in the extracted body
- sources:
  - [1] https://groq.com/pricing/
