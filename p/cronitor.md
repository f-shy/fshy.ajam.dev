# Cronitor

> cronitor.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cronitor/ | JSON https://fshy.ajam.dev/api/v1/entity/cronitor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cronitor

- `dev-services/cronitor` | qualifies-with-caveat | evidence documented | binding volume-quota | category cron job, heartbeat and uptime monitoring with status pages and web analytics (hosted) | tier Hacker
- identity a placeholder: card and phone unknown | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://cronitor.io/pricing
- free tier: Hacker plan, free forever at USD 0: 5 monitors (jobs, checks and heartbeats) with a fastest check frequency of 5 minutes, 100,000 web analytics and error events free, 1 status page with 50 subscribers, 1 dashboard user, email and Slack alerts; no SMS alerts and no premium integrations | unit: objects | metered on: object-count | read on: 2026-11-01 | source: [1] | note: The unit counted is the monitor. The Business plan is USD 2 a month per monitor plus USD 5 a month per user, with a 14-day free trial.
- per-object cap: unverified: no per-ping or per-event size is stated on the pages read
- retention: unverified: the Hacker retention is not stated on the pricing page, which lists 12 months of data retention for the Business plan | source: [1]
- egress: not applicable: an inbound telemetry and outbound check service; data is read back through the REST API, which is rate limited with a 429 answer | metered: no | source: [2]
- identity: email | detail: unverified: the sign-up page text shows no form fields, and the pricing page states no credit card term for Hacker, whose card has a Get Started button where Business has Start Free Trial.
- interface: rest, cli
- limits:
  - volume-quota (binding): 5 monitors on Hacker [1]
  - volume-quota (binding): 100,000 web analytics and error events free [1]
  - request-rate: fastest check frequency of 5 minutes on Hacker [1]
  - request-rate: REST API rate limits with a 429 answer; the numbers are not stated on the page read [2]
- limits note: Hacker has 1 dashboard user and no SMS alerts.
- binding note: The 5-monitor cap fills first for an account with several scheduled jobs.
- interface detail: A REST API at cronitor.io/api authenticated by HTTP basic auth with an API key as the username, with an OpenAPI 3 description; a Telemetry API on cronitor.link takes a key in the URL; every account starts with a telemetry key and an SDK integration key. An MCP server and CronitorCLI expose the same resources. Whether the API is open to the Hacker plan without a request cap is unverified: the pricing page lists unlimited API requests for Business only.
- endpoint: https://cronitor.io/api/monitors
- tooling: CronitorCLI, the Telemetry API, the REST API with an OpenAPI description, an MCP server and the web app
- composes with: Heartbeat and cron monitoring for up to 5 jobs of free hosts with a status page, plus 100,000 web analytics and error events a month.
- reliability: no throttle, ban or data loss is stated on the pages read
- notes: Cronitor lists cron jobs, heartbeats, website checks and API checks as monitors under one count.
- evidence note: Plan limits are quoted from the first-party pricing page and the API access from its documentation. No account was opened, and the sign-up fields and the card term are unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the Hacker plan is free forever with 5 monitors, email and Slack alerts, a basic status page and no SMS or premium integrations | capture: sha256:0c108023859d57f753af661b3547237340d67875d00b9ade3dfec596e9b20fd9 | quote: Hacker $0free forever Limited monitoring for homelabs and small projects. - 5 monitors - Email and Slack alerts - Basic status page - No SMS alerts - No premium integrations
  - [1] 2026-11-01: every plan includes cron, heartbeat, website and API monitoring | capture: sha256:0c108023859d57f753af661b3547237340d67875d00b9ade3dfec596e9b20fd9 | quote: Every plan includes cron, heartbeat, website, and API monitoring, plus email and chat alerts.
  - [1] 2026-11-01: Hacker includes 100,000 web analytics and error events free | capture: sha256:0c108023859d57f753af661b3547237340d67875d00b9ade3dfec596e9b20fd9 | quote: Web Analytics and Errors | 100,000*events free*
  - [1] 2026-11-01: the fastest check frequency is 5 minutes on Hacker and 30 seconds on Business | capture: sha256:0c108023859d57f753af661b3547237340d67875d00b9ade3dfec596e9b20fd9 | quote: Fastest check frequency | 5*minutes* | 30*seconds* | 30*seconds*
  - [1] 2026-11-01: Hacker has 1 status page with 50 included subscribers | capture: sha256:0c108023859d57f753af661b3547237340d67875d00b9ade3dfec596e9b20fd9 | quote: Included subscribers | 50 | 500 | Unlimited
  - [1] 2026-11-01: Hacker has 1 dashboard user | capture: sha256:0c108023859d57f753af661b3547237340d67875d00b9ade3dfec596e9b20fd9 | quote: Dashboard users | 1 | $5*/mo per user* | Custom
  - [1] 2026-11-01: Business keeps 12 months of data and has unlimited API requests | capture: sha256:0c108023859d57f753af661b3547237340d67875d00b9ade3dfec596e9b20fd9 | quote: - 12 month data retention - Unlimited API requests
  - [1] 2026-11-01: Business is USD 2 a month per monitor plus USD 5 a month per user | capture: sha256:0c108023859d57f753af661b3547237340d67875d00b9ade3dfec596e9b20fd9 | quote: Business $2*/mo per monitor* + $5*/mo per user*
  - [1] 2026-11-01: the Business plan has a 14-day free trial | capture: sha256:0c108023859d57f753af661b3547237340d67875d00b9ade3dfec596e9b20fd9 | quote: 14 day free trial, then pay only for the monitors and users you have.
  - [2] 2026-11-01: the REST API authenticates with an API key as the basic auth username | capture: sha256:567114ee050596e65db413b15cd7408a3a5e54f4a2de7b7edbfd3d815c4f9b5f | quote: Provide your API key as the basic auth username value. You do not need to provide a password.
  - [2] 2026-11-01: the Telemetry API is on the separate domain cronitor.link and takes an API key in the URL | capture: sha256:567114ee050596e65db413b15cd7408a3a5e54f4a2de7b7edbfd3d815c4f9b5f | quote: The [Telemetry API](https://cronitor.io/docs/telemetry-api) is hosted on a separate domain, `cronitor.link`, and uses an API key embedded in the URL to authenticate requests.
  - [2] 2026-11-01: an OpenAPI 3 description of the REST API and the Telemetry API is published | capture: sha256:567114ee050596e65db413b15cd7408a3a5e54f4a2de7b7edbfd3d815c4f9b5f | quote: An OpenAPI 3 description of the REST API and the Telemetry API is published at
  - [2] 2026-11-01: every account starts with two API keys | capture: sha256:567114ee050596e65db413b15cd7408a3a5e54f4a2de7b7edbfd3d815c4f9b5f | quote: Every account starts with two API keys with different permission levels:
  - [2] 2026-11-01: the API is rate limited and answers 429 when a limit is exceeded | capture: sha256:567114ee050596e65db413b15cd7408a3a5e54f4a2de7b7edbfd3d815c4f9b5f | quote: The API has rate limits to ensure fair usage. If you exceed these limits, you'll receive a `429 Too Many Requests` response.
  - [2] 2026-11-01: the same resources are available through an MCP server and CronitorCLI | capture: sha256:567114ee050596e65db413b15cd7408a3a5e54f4a2de7b7edbfd3d815c4f9b5f | quote: The same resources are available to coding agents through the [Cronitor MCP server](https://cronitor.io/docs/mcp-server) and to the shell through [CronitorCLI](https://cronitor.io/docs/using-cronitor-cli).
- sources:
  - [1] https://cronitor.io/pricing
  - [2] https://cronitor.io/docs/api
