# Infisical

> infisical.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/infisical/ | JSON https://fshy.ajam.dev/api/v1/entity/infisical.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Infisical

- `dev-services/infisical` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted secrets management, billed per identity (human and machine) | tier Free
- needs card unknown, phone no, ID no, institution no | verified 2026-11-20T04:15:44.931Z (live) | stale on 2026-12-21
- url https://infisical.com/pricing
- free tier: Secrets Management Free: USD 0 forever, for individuals and personal projects, with 5 identities, unlimited projects, 3 environments and 10 secret syncs | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: The unit counted is the identity, which is any principal that authenticates to Infisical, human or machine. users is the nearest schema term; the true meter is identity-count, named in metered_on. On every plan including Free: unlimited projects, two-factor authentication, secret sharing, community support, pay by card and annual billing. Paid Secrets Management plans add a 30-day free trial with no credit card. The MIT-licensed core can be self-hosted at no cost on any plan; a supported, licensed self-hosting option is available after talking to sales and is not the hosted offer priced here.
- per-object cap: unverified: no per-secret value size or per-object byte cap is stated on the pricing, API reference or rate-limit pages read
- retention: No audit log retention on Free; 30 days on Pro, 90 days on Advanced and custom on Enterprise. Secret retention is until deletion by the user and no automatic secret expiry is stated on the pages read. | source: [1] | note: The days field is null because retention is tiered for audit logs and no automatic secret lifetime is published.
- egress: not applicable: a secrets management service; data is read back through a REST API over HTTPS. No per-GB traffic price or traffic quota is stated on the pricing page; the API enforces per-minute request limits instead. | metered: no | source: [1]
- identity: email | detail: Email and password is the most common method for user identities signing in through the dashboard and CLI. The sign-up page is protected by hCaptcha; GitHub, Google and GitLab sign-in are offered as alternatives. The exact sign-up field list and whether a card is requested are unverified: behind a sign-up.
- interface: rest, cli
- limits:
  - volume-quota (binding): 5 identities on Free [1]
  - volume-quota (binding): 3 environments, 10 secret syncs and up to 3 projects on Free [1]
  - request-rate: a global cap of 600 requests per minute per client IP on Infisical Cloud; Free read 200, write 90, secret 120, identity creation 30 and project creation 30 per minute [2]
- limits note: The older comparison table states a project limit of up to 3 on Free, while the Secrets Management summary on the same page states unlimited projects. The tighter figure is recorded here and the disagreement is unresolved. Exceeding a rate limit returns HTTP 429.
- binding note: The 5-identity cap fills first for a small team plus its CI pipelines: each human and each machine identity counts, so a project with several distinct permission sets reaches the cap before the per-minute rate limits are approached.
- interface detail: A REST API over HTTPS supports every dashboard action: reading and writing secrets, managing projects and machine identities, reading audit logs and configuring resources. Cloud endpoints are app.infisical.com/api (US) and eu.infisical.com/api (EU). An OpenAPI specification is served at /api/docs/json. A CLI and SDKs use the same API.
- endpoint: https://app.infisical.com/api
- tooling: Infisical CLI, SDKs, Kubernetes Operator, Infisical Agent and the REST API, with an OpenAPI specification at /api/docs/json
- composes with: Hosted secrets store for applications and CI pipelines, reached by the CLI, SDKs and REST API; secret syncs and integrations cover AWS, Vercel, GitHub Actions, GitLab CI/CD and Jenkins.
- reliability: The Cloud API returns HTTP 429 with a standard error response and a seconds-until-reset message when a rate limit is exceeded; no ban or data-loss behaviour is stated on the pages read.
- notes: Identity is the binding constraint: the first-party pricing page states per-identity billing and a 5-identity Free cap. Self-hosting the MIT-licensed core is an alternative to the hosted Cloud offer and is not the offer priced in this record; a supported, licensed self-hosting contract is a separate paid option. No API probe of a public read path was run and no account was opened. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Free allowances, per-identity billing, retention tiers and rate limits are quoted from first-party pricing, signup and API documentation pages. No probe of a public read path was run and no account was opened, so signup field details beyond the captured text remain unverified.
- evidence:
  - [1] 2026-11-19: Secrets Management Free is USD 0 forever with 5 identities, unlimited projects, 3 environments and 10 secret syncs | capture: sha256:16f5b78ae64476fc87783c33fc520f83986a4cd5b10d9a45ce805dc69ae64d53 | quote: | Free | $0 forever | Individuals and personal projects | 5 identities, unlimited projects, 3 environments, 10 secret syncs |
  - [1] 2026-11-19: the billing unit is the identity and both human and machine principals count | capture: sha256:16f5b78ae64476fc87783c33fc520f83986a4cd5b10d9a45ce805dc69ae64d53 | quote: Billed per identity per month. An identity is any principal that authenticates to Infisical, human or machine.
  - [1] 2026-11-19: the Free identity cap is 5 against unlimited on paid tiers | capture: sha256:16f5b78ae64476fc87783c33fc520f83986a4cd5b10d9a45ce805dc69ae64d53 | quote: | Identities | 5 | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-19: Free has 3 environments and higher tiers have more | capture: sha256:16f5b78ae64476fc87783c33fc520f83986a4cd5b10d9a45ce805dc69ae64d53 | quote: | Environments | 3 | 6/project | 12/project | Unlimited |
  - [1] 2026-11-19: Free has 10 secret syncs and higher tiers have more | capture: sha256:16f5b78ae64476fc87783c33fc520f83986a4cd5b10d9a45ce805dc69ae64d53 | quote: | Secret syncs | 10 | 25 | 50 | Unlimited |
  - [1] 2026-11-19: Free has no audit log retention; Pro has 30 days, Advanced 90 and Enterprise custom | capture: sha256:16f5b78ae64476fc87783c33fc520f83986a4cd5b10d9a45ce805dc69ae64d53 | quote: | Audit log retention | No | 30 days | 90 days | Custom |
  - [1] 2026-11-19: the paid-tier trial lasts 30 days and asks for no card | capture: sha256:16f5b78ae64476fc87783c33fc520f83986a4cd5b10d9a45ce805dc69ae64d53 | quote: Paid plans include a 30-day free trial with no credit card.
  - [1] 2026-11-19: an MIT-licensed self-hostable core exists alongside the hosted offer | capture: sha256:16f5b78ae64476fc87783c33fc520f83986a4cd5b10d9a45ce805dc69ae64d53 | quote: Each has an open-source core under the MIT license, free forever if you self-host.
  - [2] 2026-11-19: a global 600 requests per minute per client IP cap applies to the Cloud API | capture: sha256:4b318bab958decd1439a83784605c331c0a1695b9befa82b04670ecb47d6b64e | quote: A global cap of 600 requests per minute per client IP applies to every endpoint (the status endpoint is exempt).
  - [2] 2026-11-19: the Free read rate limit is 200 per minute | capture: sha256:4b318bab958decd1439a83784605c331c0a1695b9befa82b04670ecb47d6b64e | quote: * Read: 200 per minute
  - [2] 2026-11-19: the Free write rate limit is 90 per minute | capture: sha256:4b318bab958decd1439a83784605c331c0a1695b9befa82b04670ecb47d6b64e | quote: * Write: 90 per minute
  - [2] 2026-11-19: the Free secret-operation rate limit is 120 per minute | capture: sha256:4b318bab958decd1439a83784605c331c0a1695b9befa82b04670ecb47d6b64e | quote: * Secret: 120 per minute
  - [2] 2026-11-19: exceeding a rate limit returns HTTP 429 | capture: sha256:4b318bab958decd1439a83784605c331c0a1695b9befa82b04670ecb47d6b64e | quote: A request that exceeds the applicable limit returns HTTP `429` with the standard
  - [3] 2026-11-19: the programmatic interface is a REST API over HTTPS | capture: sha256:9e9cf81ac6013043e748809598e9e2a547f9b41371582ed0533814d0858d2e81 | quote: The Infisical API is a REST API served over HTTPS.
  - [3] 2026-11-19: the Cloud API base URLs for the US and EU regions | capture: sha256:9e9cf81ac6013043e748809598e9e2a547f9b41371582ed0533814d0858d2e81 | quote: If you use Infisical Cloud, all endpoints are available under `https://app.infisical.com/api` (US region) or `https://eu.infisical.com/api` (EU region).
  - [4] 2026-11-19: the sign-up page is protected by hCaptcha | capture: sha256:d99c02576fd13422ee73ea94c61ac2311ffbdff1fb379fa78f5d4952e08a46cc
  - [5] 2026-11-19: email and password is a user sign-in method | capture: sha256:d7fbffccc543043a16c14ec412c7e779a68b56c1433735c5edc14ccc34b04cb4 | quote: Email and Password is the most common authentication method that can be used by user identities for authentication into Web Dashboard and Infisical CLI.
  - [6] 2026-11-19: a human user counts as one user identity toward the identity cap | capture: sha256:6f00cd86ce321ce491b0f042b8b12b1ee6fd51d81a11255d8920fee9ff096f5f | quote: User identity count is straightforward—it equals the number of human users who need access to Infisical.
  - [4] 2026-11-20: the first-party sign-up page was read on 2026-11-20; later steps remain behind the sign-up and hCaptcha | capture: sha256:2c5aa2b59c49a0afad961ac26b32b885ef9470c7fcc5620261cb2322bb8fd2f5
- sources:
  - [1] https://infisical.com/pricing
  - [2] https://infisical.com/docs/api-reference/overview/rate-limits
  - [3] https://infisical.com/docs/api-reference/overview/introduction
  - [4] https://app.infisical.com/signup
  - [5] https://infisical.com/docs/documentation/platform/auth-methods/email-password
  - [6] https://infisical.com/docs/documentation/platform/identities/overview
