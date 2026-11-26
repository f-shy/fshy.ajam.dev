# BoltzLabs

> boltz.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boltz/ | JSON https://fshy.ajam.dev/api/v1/entity/boltz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BoltzLabs

- `compute/boltz-api` | qualifies-with-caveat | evidence documented | binding write-gated | category inference API | tier API signup credits (Boltz API)
- needs card unknown, phone unknown, ID no, institution yes | verified 2026-11-24T10:11:14.624Z (live) | stale on 2026-12-25
- url https://api.boltz.com/docs/api/
- free tier: After signing up for an account in the API Console you are granted credits to test the API for free; the platform announcement adds 'Users receive free credits every month, enough for hundreds of predictions'. A launch offer gave USD 2,000 in credits to every company and USD 100 to every academic for the first two weeks. The published price is 'from as little as $0.025 a prediction'. | unit: credits | metered on: request-count | read on: 2026-11-24 | source: [1] | note: The exact credit amount, its monthly renewal window and the price beyond the credits are not stated in the public pages read; the USD 2,000 and USD 100 grants were a two-week launch offer.
- per-object cap: not applicable: the unit is a biomolecular prediction, not a stored object
- retention: Default retention is 7 days after a run reaches a terminal state, with a minimum of 1 hour and a maximum of 14 days; the standard policy deletes data 30 days after a run starts and stops active runs at that limit. Results must be downloaded to the user's own storage. | days: 30 | source: [2] | note: The 30-day limit is counted from the run start; the configurable per-workspace window is 7 days by default and caps at 336 hours.
- egress: Result artifacts are fetched through time-limited download URLs with a url_expires_at timestamp; a public share link needs no key, an email-restricted share link needs a verified Boltz OAuth email. No egress price, allowance or metering term is published. | metered: no | free allowance: unpublished | source: [3]
- identity: institution | detail: The Lab request-access form asks for full name, email, organization name, organization type and team size and states 'Use your company or institution email to receive additional free credits'; the login offers Google or email sign-in and email verification is required. The API is reachable with an account API key or a Google OAuth session; a card is not stated for the signup credit and no phone number or ID document is requested.
- interface: rest, cli
- limits:
  - write-gated (binding): Account signup with email verification is required: the console config sets REQUIRE_VERIFIED_EMAIL true and CONSOLE_SIGNUP_ENABLED true, and the Lab request-access form asks for full name, email, organization name and team size [4]
  - retention-clamped: data is deleted 30 days after a run starts, active runs are stopped at that limit, and the configurable retention window is 7 days by default with a 14-day maximum [2]
  - volume-quota: a workspace spending limit is a lifetime cap in milli-USD; a request that does not fit remaining headroom is rejected with workspace_spending_limit_reached [5]
- binding note: A verified account is needed before any credit or paid run can start; the credit amount and the spending cap are only reachable once the signup and email gate is passed.
- interface detail: REST endpoints under https://api.boltz.bio/compute/v1 driven by the boltz-api CLI, a Python SDK and a TypeScript SDK; a CLI device-code login obtains an OAuth token and API keys are passed in the x-api-key header.
- endpoint: part of interface detail
- tooling: the boltz-api CLI installed from install.boltz.bio, the Python or TypeScript SDK, or any HTTP client sending x-api-key; agents use first-party plugins for Claude Code, Codex and Gemini CLI
- composes with: A hosted prediction API for structure, affinity, ADME and molecular design work whose results are downloaded to the user's own storage, so multi-step pipelines need a separate record for durable state.
- reliability: Output data is automatically deleted at the retention deadline and download URLs can expire before that deadline; a lifetime workspace spending limit can reject a job once its headroom is used.
- notes: The credit amount is not published; the price beyond credits is stated only as 'from as little as $0.025 a prediction', and the USD 2,000 and USD 100 grants were a two-week launch promotion. Signup requires a verified email and the request-access form favours a company or institution email for additional credits. A test-mode key runs the full lifecycle for free with synthetic results. The Lab platform record and the API record are separate tiers of the same provider.
- evidence note: The signup credit, the price and the monthly credit claim are quoted from the vendor's API docs, launch announcement and Lab FAQ read on 2026-11-24; the identity fields are quoted from the Lab request-access and login pages, and retention from the API docs, the same day.
- extras:
  - shape.gpu_class: vendor-managed distributed GPUs
  - shape.note: the user submits biomolecular jobs; the hardware is operated by the vendor
  - billing_model: signup credits then usage-based billing per prediction
  - free_tier_kind: recurring-credit
  - term: monthly credits claimed on the Lab FAQ; the exact amount and renewal rule are not published
  - network_out.allow_outbound: yes
  - network_out.ports: HTTPS REST and time-limited download URLs
  - session_cap.restart_required: no
  - session_cap.note: a prediction or pipeline is stopped at the 30-day standard data limit; no per-job wall-clock cap is published
- evidence:
  - [1] 2026-11-24: signing up for an API Console account grants credits to test the API for free | capture: sha256:174888a5086036476096270a4958dc5c6d768ec6544588ed7f10f738b57da1fe | quote: After signing up for an account in the API Console, you’ll be granted credits so you can test the API for free.
  - [6] 2026-11-24: the published price is from USD 0.025 a prediction and a launch offer granted USD 2,000 per company and USD 100 per academic for two weeks | capture: sha256:137e9b71c8652e067ffdf6c02ec30e6fafe910ab7af372f71e29cec2eca790f4 | quote: The Boltz API is a new, highly efficient way to run Boltz models, from as little as $0.025 a prediction.
  - [6] 2026-11-24: the launch credit offer was USD 2,000 per company and USD 100 per academic for the first two weeks | capture: sha256:137e9b71c8652e067ffdf6c02ec30e6fafe910ab7af372f71e29cec2eca790f4 | quote: To celebrate the launch, we are offering $2,000 in credits to every company and $100 to every academic for the first two weeks.
  - [7] 2026-11-24: the Lab platform states users receive free credits every month, enough for hundreds of predictions | capture: sha256:578cec5314f5c9195820ed27071f70aa9f0473593ad68232ba7cf46afea43af4 | quote: You can sign up at lab.boltz.com. Users receive free credits every month, enough for hundreds of predictions.
  - [4] 2026-11-24: the access form requests full name, email, organization, team size and a company or institution email for additional free credits | capture: sha256:b43669425c8b3a0778f25e0f0f5e5b05fa0fbd89b2fb5a229bbd6ab0b78256aa | quote: Tell us about yourself. We'll review your request and get back to you. Use your company or institution email to receive additional free credits.
  - [8] 2026-11-24: the Lab login offers Google or email sign-in | capture: sha256:827be05d1d2a5ec803ac2582b5750e4b76c58bc62f881ca52426ce4e6b8ead75 | quote: Google Continue with Google or sign in with email
  - [9] 2026-11-24: the console enables signup, requires a verified email, enables Google login and uses Cloudflare Turnstile on the signup flow | capture: sha256:eda46878f38a252162efc9266e0259836c767bd0cc0694278573ad36f4b05edd | quote: "CONSOLE_SIGNUP_ENABLED": true, "AUTH_CAPTCHA_ENABLED": true, "AUTH_CAPTCHA_PROVIDER": "cloudflare-turnstile",
  - [2] 2026-11-24: the standard policy deletes data 30 days after a run starts and stops active runs at that limit | capture: sha256:4f0ba0d152b3be1871287a6524c6053d097fd73e105599006a465a92205b6576 | quote: Standard 30-day limit: Under the standard policy, data is deleted 30 days after a run starts. Active runs are stopped at this limit.
  - [2] 2026-11-24: the default retention is 7 days with a minimum of 1 hour and a maximum of 14 days | capture: sha256:4f0ba0d152b3be1871287a6524c6053d097fd73e105599006a465a92205b6576 | quote: - Default: 7 days - Minimum: 1 hour - Maximum: 14 days (336 hours)
  - [10] 2026-11-24: test-mode keys run the full lifecycle with synthetic results, no GPU usage and no billing | capture: sha256:66f8ed06766847f37571ae03bc64e65681e3df4e6dc5ea5c7b6c4e29778d0ee3 | quote: A test-mode API key (`mode: "test"`, prefix `sk_bc_*_test_`) runs the full request → poll → fetch-results lifecycle against the real endpoints but returns synthetic results with no GPU usage and no billing.
  - [3] 2026-11-24: public share links need no key while email-restricted links require a verified Boltz OAuth email | capture: sha256:98db6df569b983413301f19b85af3f94e0bc5b6cb01f5364d45170137e2835c8 | quote: | `public` | No API key or OAuth token; possession of the link is sufficient | Low-friction sharing where anyone who receives the secret URL may view | | `email` | Boltz OAuth sign-in with a verified email in `allowed_emails` | Named collaborators or customer users who should authenticate before viewing |
  - [11] 2026-11-24: the API accepts an x-api-key header or an OAuth bearer token obtained through a CLI device-code login | capture: sha256:4b0b64159c533d539d2f727f1aace76d399dca70b6b282e59637a7c1e2558e2f | quote: Pass the key in the `x-api-key` request header:
  - [5] 2026-11-24: a workspace spending limit is a lifetime cap and a job that does not fit is rejected with workspace_spending_limit_reached | capture: sha256:d3dca178e8a01888471bce1886a8428e57dd93e321b4002ca3d38136fe339087 | quote: Before billable work starts, Boltz reserves its estimated cost against both the organization and workspace ledgers. A request that does not fit the remaining workspace headroom is rejected with the error code `workspace_spending_limit_reached`.
- sources:
  - [1] https://api.boltz.com/docs/api/
  - [2] https://api.boltz.com/docs/api/guides/data-retention/
  - [3] https://api.boltz.com/docs/api/guides/share-links/
  - [4] https://lab.boltz.com/request-access
  - [5] https://api.boltz.com/docs/api/guides/workspace-spending-limits/
  - [6] https://boltz.com/boltzmol-boltzprot-api
  - [7] https://boltz.com/boltzlab
  - [8] https://lab.boltz.com/login
  - [9] https://api.boltz.com/console/signup?redirectTo=%2F
  - [10] https://api.boltz.com/docs/api/guides/costs/
  - [11] https://api.boltz.com/docs/api/guides/authentication/
