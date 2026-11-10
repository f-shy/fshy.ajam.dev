# Checkly

> checklyhq.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/checklyhq/ | JSON https://fshy.ajam.dev/api/v1/entity/checklyhq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Checkly

- `dev-services/checkly` | qualifies-with-caveat | evidence documented | binding volume-quota | category uptime and synthetic monitoring (browser and API checks) with status pages, as code | tier Hobby
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://www.checklyhq.com/pricing/
- free tier: Hobby plan at USD 0 a month, free forever with no credit card required: 10 uptime monitors, 1,000 browser check runs and 10,000 API check runs, 1 user, 6 public locations with at most 3 per check, a status page for 20 services and 250 subscribers, 1 dashboard and 10 AI root cause analysis invocations | unit: mixed | metered on: request-count | read on: 2026-11-01 | source: [1] | note: The allowance mixes a count of monitors with counts of check runs, so no single unit of the vocabulary fits. The Starter plan lists overage prices per 1,000 browser runs and per 10,000 API runs; the Hobby column shows none, and what happens when Hobby runs are used up is unverified: not stated on the pages read.
- per-object cap: unverified: no per-check result or payload size is stated on the pages read
- retention: 7 days of raw data and 30 days of aggregated data on Hobby, against 30 days and 1 year on Team | days: 7 | source: [1]
- egress: not applicable: an outbound checker; results are read back through the public API, most routes allow 600 requests per 60 seconds, and the Prometheus endpoint is a Team feature | metered: no | source: [2]
- identity: email | detail: The sign-up page asks for an email address or offers Continue with Google or GitHub, and the pricing page states the Hobby plan needs no credit card. The sign-up page also advertises a 14-day trial of Checkly; how an account moves from that trial to Hobby is unverified: behind a sign-up.
- interface: rest, cli
- limits:
  - volume-quota (binding): 10 uptime monitors [1]
  - volume-quota (binding): 1,000 browser check runs and 10,000 API check runs included on Hobby [1]
  - request-rate: public API: 600 requests every 60 seconds on most routes, with custom limits on some routes [2]
  - retention-clamped: 7 days of raw data, 30 days of aggregated data [1]
- limits note: Hobby has no SMS alerts (0), 1 user and no Prometheus endpoint. A check on Hobby runs from at most 3 of the 6 public locations.
- binding note: The monthly run allowances and the 10-monitor cap set how many checks can run and how often; the API rate limit applies only to programmatic management.
- interface detail: Public API at api.checklyhq.com with an OpenAPI specification at /openapi.json, authenticated by an API key as a Bearer token plus an X-Checkly-Account header; the Checkly CLI, a Terraform provider and a Pulumi provider are listed on every plan, Hobby included; service API keys are an Enterprise feature.
- endpoint: https://api.checklyhq.com/
- tooling: the Checkly CLI (monitoring as code with Playwright and JavaScript), the Terraform and Pulumi providers, any HTTP client with an API key, and the web dashboard
- composes with: External HTTP, TCP, DNS and Playwright browser checks from 6 public locations against free-hosted apps, defined as code in the app repository and alerting by email, Slack or webhook.
- reliability: no throttle, ban or data loss is stated on the pages read beyond the 7-day raw and 30-day aggregated data retention
- notes: Starter, at USD 29 a month for the Detect module, includes 50 monitors, 3,000 browser check runs and 25,000 API check runs.
- evidence note: Plan limits are read from the first-party pricing page and the API limits from its documentation. No account was opened, so the behaviour at the end of the sign-up trial and past the monthly run allowance is unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the Hobby plan costs USD 0 and includes 10 monitors, 1,000 browser check runs and 10,000 API check runs | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Hobby | $0 | $0 | 10 | 1,000 | 10,000 |
  - [1] 2026-11-01: the Hobby plan is free forever and needs no credit card | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: The Hobby plan is free forever with no credit card required.
  - [1] 2026-11-01: the Starter Detect module costs USD 29 a month with 50 monitors, 3,000 browser check runs and 25,000 API check runs | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Starter | $29 | $24 | 50 | 3,000 | 25,000 |
  - [1] 2026-11-01: Hobby has 1 user | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Users | 1 | 3 | 10 | Custom |
  - [1] 2026-11-01: Hobby and Starter use 6 public locations with at most 3 per check | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: 6 locations on Hobby/Starter, all 22 on Team/Enterprise. Hobby and Starter can select a maximum of 3 locations per check.
  - [1] 2026-11-01: Hobby has 1 dashboard | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Dashboards | 1 | 1 | 10 | Custom |
  - [1] 2026-11-01: Hobby status pages hold 20 services | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Services | 20 | 25 | 50 | 100 |
  - [1] 2026-11-01: Hobby status pages allow 250 subscribers | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Subscribers | 250 | 500 | 1,000 | 2,000 |
  - [1] 2026-11-01: Hobby has 10 AI root cause analysis invocations | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | AI RCA Invocations | 10 | 50 | 150 | Custom |
  - [1] 2026-11-01: raw data is kept 7 days on Hobby | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Raw Data Retention | 7 days | 7 days | 30 days | 180 days |
  - [1] 2026-11-01: aggregated data is kept 30 days on Hobby | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Aggregated Data Retention | 30 days | 30 days | 1 year | 25 months |
  - [1] 2026-11-01: the Checkly CLI is available on Hobby | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Checkly CLI | Yes | Yes | Yes | Yes |
  - [1] 2026-11-01: the Terraform provider is available on Hobby | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Terraform Provider | Yes | Yes | Yes | Yes |
  - [1] 2026-11-01: the Pulumi provider is available on Hobby | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Pulumi Provider | Yes | Yes | Yes | Yes |
  - [1] 2026-11-01: service API keys are an Enterprise feature | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Service API Keys | No | No | No | Yes |
  - [1] 2026-11-01: the Prometheus endpoint is not part of Hobby | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Prometheus Endpoint | No | No | Yes | Yes |
  - [1] 2026-11-01: Hobby has no SMS alerts | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | SMS Alerts | 0 | 100/month | 200/month | Custom |
  - [1] 2026-11-01: Hobby has webhook alerts | capture: sha256:1dbfb6c079ca2488e6875abcde88bd4aedda6e19e2049bea19fab590b744d8e3 | quote: | Webhook Alerts | Yes | Yes | Yes | Yes |
  - [2] 2026-11-01: most public API routes allow 600 requests every 60 seconds | capture: sha256:a80538c535f592a65a0deb51d7cbe0ce6c9c814319208d48a3c78c6ca5506267 | quote: For most of our routes, that limit is 600 requests every 60 seconds.
  - [2] 2026-11-01: the public API authenticates with a Bearer API key in the Authorization header and the account ID in an X-Checkly-Account header | capture: sha256:a80538c535f592a65a0deb51d7cbe0ce6c9c814319208d48a3c78c6ca5506267 | quote: Authentication to the API is performed using the Bearer auth method in the Authorization header and using the Account ID. For example, set the `Authorization` and `X-Checkly-Account` headers when using cURL:
  - [2] 2026-11-01: an OpenAPI specification of the public API is published | capture: sha256:a80538c535f592a65a0deb51d7cbe0ce6c9c814319208d48a3c78c6ca5506267 | quote: Use `https://api.checklyhq.com/openapi.json` for the current Checkly Public API specification.
  - [3] 2026-11-01: the sign-up page offers Google and GitHub sign-in beside an email address | capture: sha256:9897b0f8e2b0b44cca0d3ac78bf91ade9579531fb63a659ade2fd785db573075 | quote: Continue with GoogleContinue with GitHub
  - [3] 2026-11-01: the sign-up page advertises a 14-day trial of Checkly | capture: sha256:9897b0f8e2b0b44cca0d3ac78bf91ade9579531fb63a659ade2fd785db573075 | quote: Start with a 14-day trial of Checkly:
- sources:
  - [1] https://www.checklyhq.com/pricing/
  - [2] https://www.checklyhq.com/docs/api-reference/overview/
  - [3] https://app.checklyhq.com/signup
