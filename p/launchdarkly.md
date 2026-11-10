# LaunchDarkly

> launchdarkly.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/launchdarkly/ | JSON https://fshy.ajam.dev/api/v1/entity/launchdarkly.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LaunchDarkly

- `dev-services/launchdarkly` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted feature flags, experimentation and observability | tier Developer
- needs card no, phone unknown, ID no, institution no | verified 2026-11-02T00:37:55.413Z (live) | stale on 2026-12-03
- url https://launchdarkly.com/pricing/
- free tier: Developer: USD 0 a month forever, no credit card; unlimited feature flags and seats, 5 service connections and 1K client-side MAU a month, 100K experimentation MAU, 10M logs and 10M traces, 5K session replays and 5K errors, 5K AI runs a month; 1 project and 3 environments | unit: mixed | read on: 2026-10-30 | source: [1] | note: The allowance is counted in service connections (one server-side SDK connected to one environment for a month), client-side MAU (each unique client-side user or device), log lines, trace spans, session replays, errors and AI runs; no single unit term fits. Sign-up starts a 14-day trial with Enterprise features that converts to Developer. When usage keeps exceeding the Developer entitlements the plan converts to read-only mode.
- per-object cap: unverified: no flag or payload size limit is stated on the pages read
- retention: Logs, traces, session replays and errors are stored one month; AgentControl run and eval data stays 14 days | source: [1]
- egress: not applicable: flag evaluations reach the SDKs over routes that are never rate limited; no traffic allowance is published | metered: no | source: [2]
- identity: email | detail: The sign-up form asks for first name, last name, email and password, or a GitHub sign-in, and states no credit card is required; it starts a 14-day trial that continues on the free Developer plan. The GitHub route shows a Complete profile screen for First name, Last name, Work email and Organization, then sends an email to verify the account. Whether a later step asks for a phone number is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 5 service connections and 1K client-side MAU a month [1]
  - volume-quota (binding): 10M logs and 10M traces a month; 5K session replays and 5K errors a month; 5K AI runs a month [1]
  - write-gated: usage that keeps exceeding the Developer entitlements converts the plan to read-only mode [3]
  - retention-clamped: logs, traces, session replays and errors stored one month; AgentControl data 14 days [1]
- limits note: 1 project and 3 environments on Developer. REST API rate limits are not published; LaunchDarkly returns them in response headers.
- binding note: Each server-side SDK in each environment uses one of the 5 service connections a month, so server-side use meets that count first; client-side apps meet 1K MAU. Continued excess turns the plan read-only.
- interface detail: REST API at https://app.launchdarkly.com/api/v2 with personal or service access tokens (a GET /api/v2/projects without a token answered 401); SDK keys, mobile keys and client-side IDs cannot call the REST API; an OpenAPI specification is published.
- endpoint: part of interface detail
- tooling: 30 SDKs (13 client-side, 13 server-side, 4 edge), the Relay Proxy, or any HTTP client against the REST API with an access token.
- composes with: Feature flags for a few server-side services on free compute, with client-side flags for up to 1K MAU a month.
- reliability: Usage above the Developer entitlements is warned and then turns the plan read-only; Developer support is the Discord community.
- notes: Foundation is pay as you go after a 14-day trial: USD 10 per service connection a month and USD 8.33 per 1K client-side MAU a month billed yearly.
- evidence note: Every value is quoted from the first-party pricing page, plan and billing docs, REST API overview and sign-up page; the REST API host was probed and answered 401 without a token. A flag evaluation through an SDK key on a Developer account would move it to measured.
- evidence:
  - [1] 2026-10-30: Developer needs no credit card | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: [Get started free](https://app.launchdarkly.com/signup) No credit card required
  - [1] 2026-10-30: Developer is USD 0 a month forever | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: $0/ mo, forever
  - [1] 2026-10-30: Developer includes 5 service connections and 1K client-side MAU a month | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: 5 service connections and 1K client-side MAU /mo
  - [1] 2026-10-30: what a service connection and an MAU are | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: A service connection is one server-side SDK connected to one environment for a month. Each unique client-side user or device is one MAU.
  - [1] 2026-10-30: Developer includes 100K experimentation MAU a month | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: Includes 100K experimentation MAU per month at no additional charge.
  - [1] 2026-10-30: Developer includes 10M logs and 10M traces a month | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: 10M logs and 10M traces /mo
  - [1] 2026-10-30: logs and traces are stored one month | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: A log is a single log line and a trace is a single span, each ingested, stored, and searchable for one month.
  - [1] 2026-10-30: Developer includes 5K session replays and 5K errors a month | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: 5K session replays and 5K errors /mo
  - [1] 2026-10-30: session replays and errors are stored one month | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: Each is stored for one month.
  - [1] 2026-10-30: Developer includes 5K AI runs a month | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: 5k AI runs/mo included
  - [1] 2026-10-30: AgentControl data retention is 14 days on Developer | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: 14 days data retention
  - [1] 2026-10-30: the 14 days apply to AgentControl run and eval data | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: How long AgentControl run and eval data stays available.
  - [1] 2026-10-30: Developer has unlimited feature flags | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: Unlimited feature flags
  - [1] 2026-10-30: Developer has unlimited seats | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: Unlimited seats
  - [1] 2026-10-30: 30 SDKs are available | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: 30 idiomatic SDKs
  - [1] 2026-10-30: the SDKs split into 13 client-side, 13 server-side and 4 edge | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: 13 client-side, 13 server-side, and 4 edge SDKs.
  - [1] 2026-10-30: Foundation is a 14-day trial then pay as you go | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: 14-day trial, then pay as you go.
  - [1] 2026-10-30: Foundation charges USD 10 per service connection a month | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: $10per Service Connection / mo
  - [1] 2026-10-30: Foundation charges USD 8.33 per 1K client-side MAU a month billed yearly | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: $8.33per 1k client-side MAU / mo
  - [1] 2026-10-30: Developer support is the Discord community | capture: sha256:96fbff66a5dc31d47bd8c2e5c4ce017d3a80974cc00a9f1e56a2b71c36fb48ba | quote: Discord Community (1 business day outage)
  - [1] 2026-10-30: Developer has 1 project and 3 environments | capture: sha256:dbf7d76579d62e9af27f02a8ca270841c34e65798207b6d8293360349a77082c | quote: 1 project & 3 environments
  - [4] 2026-10-30: Developer plans are free and need no credit card | capture: sha256:39dd22748742f88456b334a8a536103f41c5ecf907ac956ba11fe999527d7426 | quote: Developer plans are free to use and don't require a credit card.
  - [4] 2026-10-30: a Relay Proxy exists | capture: sha256:39dd22748742f88456b334a8a536103f41c5ecf907ac956ba11fe999527d7426 | quote: The [Relay Proxy in offline mode]
  - [3] 2026-10-30: continued excess turns the plan read-only | capture: sha256:2e98f3056274103901c3e4b7f8c58af291485ba1efe49635cb2cf594e5e8f46a | quote: If your usage continues to exceed these entitlements, your plan will convert to read-only mode.
  - [2] 2026-10-31: the REST API takes personal or service access tokens | capture: sha256:bc418ee7cb9647c5da496e935b2838d799e2cc2c31871613a7163247135dfa88 | quote: All REST API resources are authenticated with either [personal or service access tokens](https://launchdarkly.com/docs/home/account/api), or session cookies.
  - [2] 2026-10-31: SDK keys cannot call the REST API | capture: sha256:bc418ee7cb9647c5da496e935b2838d799e2cc2c31871613a7163247135dfa88 | quote: These keys cannot be used to access our REST API.
  - [2] 2026-10-31: the REST API is served under app.launchdarkly.com/api/v2 with an OpenAPI spec | capture: sha256:bc418ee7cb9647c5da496e935b2838d799e2cc2c31871613a7163247135dfa88 | quote: We have a [complete OpenAPI (Swagger) specification](https://app.launchdarkly.com/api/v2/openapi.json) for our API.
  - [2] 2026-10-31: REST API rate limits are not published | capture: sha256:bc418ee7cb9647c5da496e935b2838d799e2cc2c31871613a7163247135dfa88 | quote: We do not publicly document the specific number of calls permitted by any of these limits, and these limits may change.
  - [2] 2026-10-31: SDK routes are never rate limited | capture: sha256:bc418ee7cb9647c5da496e935b2838d799e2cc2c31871613a7163247135dfa88 | quote: LaunchDarkly SDKs are never rate limited and do not use the API endpoints defined here.
  - [5] 2026-10-31: sign-up starts a 14-day trial then Developer, no card | capture: sha256:35b8e5b0030302e94694d4025d1c4c68d8a579d3f47d3112f84a6d9758bc3ec3 | quote: Start with 14 days of full access, then continue on a free [Developer account(Link opens in new tab)](https://launchdarkly.com/pricing/) with limits. No credit card required.
  - [5] 2026-10-31: the sign-up offers GitHub | capture: sha256:35b8e5b0030302e94694d4025d1c4c68d8a579d3f47d3112f84a6d9758bc3ec3 | quote: [Sign up with GitHub](https://app.launchdarkly.com/oauth/github)
  - [5] 2026-10-31: the sign-up asks for first name, last name, email and password | capture: sha256:35b8e5b0030302e94694d4025d1c4c68d8a579d3f47d3112f84a6d9758bc3ec3 | quote: First name \* Last name \* Email \* Password \*
  - probe:https://app.launchdarkly.com/api/v2/projects 2026-10-31: app.launchdarkly.com/api/v2/projects answers 401 without a token | capture: sha256:6e0b536fd6ce46fe182c016488ef874b00c591bcaba64ed101f38764420fc399 | quote: "status": 401
  - [6] 2026-11-01: the GitHub sign-up route shows a Complete profile screen that takes a first and a last name | capture: sha256:eb700bb0a8c513150cfda3749acbb25517b402e7e8b8482bc017fe5be33f4248 | quote: 3. The LaunchDarkly "Complete profile" screen appears. Enter the First name and Last name to use within LaunchDarkly.
  - [6] 2026-11-01: the Complete profile screen asks for an Organization | capture: sha256:eb700bb0a8c513150cfda3749acbb25517b402e7e8b8482bc017fe5be33f4248 | quote: 5. Enter your Organization.
  - [6] 2026-11-01: the GitHub route ends with an email to verify the account | capture: sha256:eb700bb0a8c513150cfda3749acbb25517b402e7e8b8482bc017fe5be33f4248 | quote: 7. In your work email account, find the email titled "Verify your LaunchDarkly account" and click Verify email.
  - [5] 2026-11-01: the sign-up form asks for first name, last name, email and password | capture: sha256:35b8e5b0030302e94694d4025d1c4c68d8a579d3f47d3112f84a6d9758bc3ec3 | quote: First name \* Last name \* Email \* Password \*
- sources:
  - [1] https://launchdarkly.com/pricing/
  - [2] https://launchdarkly.com/docs/api.md
  - [3] https://launchdarkly.com/docs/home/account/calculating-billing.md
  - [4] https://launchdarkly.com/docs/home/account/plans
  - [5] https://app.launchdarkly.com/signup
  - [6] https://launchdarkly.com/docs/home/account/oauth-github
