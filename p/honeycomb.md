# Honeycomb

> honeycomb.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/honeycomb/ | JSON https://fshy.ajam.dev/api/v1/entity/honeycomb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Honeycomb

- `dev-services/honeycomb` | qualifies-with-caveat | evidence documented | binding volume-quota | category observability: trace, event and metric store with a query engine | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-02T00:37:34.245Z (live) | stale on 2026-12-03
- url https://www.honeycomb.io/pricing
- free tier: Free, 'free forever': up to 20M events per month and up to 100M metrics data points per month, 2 triggers, distributed tracing, BubbleUp, OpenTelemetry support, Honeycomb MCP; no credit card required | unit: mixed | metered on: object-count | read on: 2026-10-30 | source: [1] | note: The allowance counts events and metrics data points, which no single unit of the vocabulary names. Each span of a trace counts as one event, so a trace of 150 spans is 150 events. Pro starts at USD 150 per month for up to 750M events.
- per-object cap: An event may have 2,000 fields and must be less than 1 MB of uncompressed JSON, and a string field is at most 64KB; the single-event endpoint limits its request body to 1MB raw (potentially compressed) | source: [2] | note: A request sent through the OpenTelemetry Collector is limited to 15MB.
- retention: Events and logs: 60-day fixed retention. Time-series metrics datasets: 13-month fixed retention by default. | days: 60 | source: [3]
- egress: unverified: no egress term on the pages read; the Query Data API is listed among Enterprise features | metered: no | source: [1]
- identity: email | detail: Sign-up takes an e-mail address or a Google account, activated by a link sent to the e-mail, then a team name, a role and how the user heard of Honeycomb; the sign-up page states no credit card is required. The data region (US or EU) is chosen at sign-up. Whether a later step asks for a phone number is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 20M events per month (each span is one event) and 100M metrics data points per month [1]
  - request-rate: 2000 events per second on the free tier; traffic above it gets HTTP 429 [4]
  - retention-clamped: 60 days for events and logs [3]
  - volume-quota (binding): 2 triggers [1]
- binding note: Each span is one event, so a trace of 150 spans uses 150 of the 20M a month; the monthly event count binds before the 2000 events-per-second rate or the 60-day retention.
- interface detail: Events and management API under /1/ and /2/ at https://api.honeycomb.io (US) or https://api.eu1.honeycomb.io (EU), keyed by API keys, plus OTLP ingest at the same hosts over gRPC, HTTP/protobuf and HTTP/JSON. A hosted MCP server at https://mcp.honeycomb.io/mcp (US) or https://mcp.eu1.honeycomb.io/mcp (EU) authenticates with OAuth or an API key and is available on every plan, including free. The Query Data API is listed among Enterprise features. api.honeycomb.io answered 401 to /1/auth without a key.
- endpoint: part of interface detail
- tooling: OpenTelemetry SDKs and collectors, the Honeycomb MCP server, and any HTTP client with an API key
- composes with: A trace and event store for free compute services instrumented with OpenTelemetry, 20M spans or events a month kept 60 days.
- reliability: A team over its monthly event limit for a second consecutive month is warned, and after 10 days the Event API accepts one event in ten and rejects the rest.
- notes: The free plan counts events, not bytes, and keeps them 60 days, the longest event retention of the free observability tiers at Better Stack (3 days), Axiom (30 days) and New Relic (at least 8 days).
- evidence note: Every limit is quoted from a first-party page, and the API host answered 401 without a key. No account was opened; an authenticated event send from a free team would move it to measured.
- evidence:
  - [1] 2026-10-30: Free allows up to 20M events and 100M metrics data points a month | capture: sha256:1853c4383341c91c2308d885b31889a491f797ec19f207b3957fbb965628bd8b | quote: Event Volume: Up to 20M per month Metrics Data Points: Up to 100M per month
  - [1] 2026-10-30: the free plan has no end date | capture: sha256:1853c4383341c91c2308d885b31889a491f797ec19f207b3957fbb965628bd8b | quote: Our introductory plan, free forever.
  - [1] 2026-10-30: Free includes 2 triggers | capture: sha256:1853c4383341c91c2308d885b31889a491f797ec19f207b3957fbb965628bd8b | quote: 2 Triggers
  - [1] 2026-10-30: Free includes OpenTelemetry support | capture: sha256:1853c4383341c91c2308d885b31889a491f797ec19f207b3957fbb965628bd8b | quote: OpenTelemetry Support
  - [1] 2026-10-30: Free includes the Honeycomb MCP server | capture: sha256:1853c4383341c91c2308d885b31889a491f797ec19f207b3957fbb965628bd8b | quote: Honeycomb MCP
  - [1] 2026-10-30: Pro starts at USD 150 per month | capture: sha256:1853c4383341c91c2308d885b31889a491f797ec19f207b3957fbb965628bd8b | quote: Starting at $150 per month
  - [1] 2026-10-30: Pro allows up to 750M events a month | capture: sha256:1853c4383341c91c2308d885b31889a491f797ec19f207b3957fbb965628bd8b | quote: Event Volume: Up to 750M per month
  - [1] 2026-10-30: the Query Data API is in the Enterprise feature list | capture: sha256:1853c4383341c91c2308d885b31889a491f797ec19f207b3957fbb965628bd8b | quote: Query Data API
  - [5] 2026-10-30: the sign-up page states no credit card is required | capture: sha256:7e5b57bde23c048e96ab839f80018da6d4ab4fd6e43f8552d8678e38d113e256 | quote: No credit card required.
  - [6] 2026-10-30: sign-up takes an e-mail address or a Google account | capture: sha256:34a9ceaa5ac79d83acefe365ad960a3169451256e9c50fc007d7b420867d0a4d | quote: Sign up with your email or Google account.
  - [6] 2026-10-30: the account is activated by an e-mailed link | capture: sha256:34a9ceaa5ac79d83acefe365ad960a3169451256e9c50fc007d7b420867d0a4d | quote: Activate your account using the activation link sent to your email.
  - [6] 2026-10-30: the team step asks for a team name, a role and a referral answer | capture: sha256:34a9ceaa5ac79d83acefe365ad960a3169451256e9c50fc007d7b420867d0a4d | quote: Give your team a name, choose your occupation/role, and let us know how you heard about Honeycomb.
  - [3] 2026-10-30: events and logs are kept 60 days | capture: sha256:0ba6bff16315ce801ecf9d0e7f9d8be7dc9ccb849104d6d6251513a5b1acdd43 | quote: Events and logs: 60-day fixed retention.
  - [3] 2026-10-30: metrics datasets are kept 13 months by default | capture: sha256:0ba6bff16315ce801ecf9d0e7f9d8be7dc9ccb849104d6d6251513a5b1acdd43 | quote: Time-series metrics datasets: 13-month fixed retention by default.
  - [3] 2026-10-30: each span of a trace counts as one event | capture: sha256:0ba6bff16315ce801ecf9d0e7f9d8be7dc9ccb849104d6d6251513a5b1acdd43 | quote: Honeycomb counts a trace that contains 150 spans as 150 events.
  - [3] 2026-10-30: a team over its limit a second month is warned and has 10 days to correct it | capture: sha256:0ba6bff16315ce801ecf9d0e7f9d8be7dc9ccb849104d6d6251513a5b1acdd43 | quote: warns them that Honeycomb will throttle incoming events unless they correct the overage within 10 days
  - [3] 2026-10-30: throttling keeps one event in ten | capture: sha256:0ba6bff16315ce801ecf9d0e7f9d8be7dc9ccb849104d6d6251513a5b1acdd43 | quote: The Honeycomb Event API randomly accepts one of every ten events and rejects the remaining nine
  - [4] 2026-10-30: the free tier is limited to 2000 events per second | capture: sha256:296a11c8197255c406d9849f61f957574d18d4e11b938741cc1161709c2304fd | quote: Free tier plans are limited to 2000 EPS.
  - [4] 2026-10-30: traffic over the rate limit gets HTTP 429 | capture: sha256:296a11c8197255c406d9849f61f957574d18d4e11b938741cc1161709c2304fd | quote: Honeycomb will rate limit the traffic, emitting a 429
  - [7] 2026-10-30: the US API base URL | capture: sha256:aeea7b53ac9c50c8d2517b89c23f1aa40a014ab822ebe1089a3d00c87c05bc4a | quote: | US | `https://api.honeycomb.io` | `https://ui.honeycomb.io` |
  - [7] 2026-10-30: the EU API base URL | capture: sha256:aeea7b53ac9c50c8d2517b89c23f1aa40a014ab822ebe1089a3d00c87c05bc4a | quote: | EU | `https://api.eu1.honeycomb.io` | `https://ui.eu1.honeycomb.io` |
  - probe:https://api.honeycomb.io/1/auth 2026-10-31: the API host answers 401 without a key | capture: sha256:841c1fbe56c4bec67f95c501ed2675b829018d9d9f130a0da4bf42d096c33048 | quote: "status": 401
  - [2] 2026-11-01: an event has at most 2,000 fields and must be under 1 MB of uncompressed JSON | capture: sha256:b23e3274be120256c38cd584d76436b3c8215cdd9567e251be4f3483e8c63af7 | quote: 2,000 fields per event. The entire event must be less than 1 MB of uncompressed JSON.
  - [2] 2026-11-01: a string field is at most 64KB | capture: sha256:b23e3274be120256c38cd584d76436b3c8215cdd9567e251be4f3483e8c63af7 | quote: String Fields: Each string field has a maximum length of 64KB.
  - [8] 2026-11-01: a request sent to Honeycomb through the OpenTelemetry Collector is limited to 15MB | capture: sha256:9a4b677c85d9529c3290d878fcfcde339de56f659ac5cedffd0f59c14df40c58 | quote: The request size limit is 15MB.
  - [9] 2026-11-01: Honeycomb accepts OTLP over gRPC, HTTP/protobuf and HTTP/JSON | capture: sha256:72b7b30bf5d94b5baa5e6b00b3482ef56c124a94121df53a418127f528d18990 | quote: Honeycomb supports receiving telemetry data via OpenTelemetry's native protocol, OTLP, over gRPC, HTTP/protobuf, and HTTP/JSON.
  - [2] 2026-11-01: the single-event endpoint limits its request body to 1MB raw (potentially compressed) | capture: sha256:b23e3274be120256c38cd584d76436b3c8215cdd9567e251be4f3483e8c63af7 | quote: The request body is limited to raw (potentially compressed) size of 1MB.
  - [10] 2026-11-01: one batch request carries one or more events, so the event count is not a request count | capture: sha256:08fa3159127eb0b035933c8f545a4ade5f1e3dc182d26a3d33cbdeea3c31cf28 | quote: The array should contain one or more JSON objects representing Events.
  - [9] 2026-11-01: the OTLP endpoint of the US region is api.honeycomb.io | capture: sha256:72b7b30bf5d94b5baa5e6b00b3482ef56c124a94121df53a418127f528d18990 | quote: export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.honeycomb.io:443 # US
  - [9] 2026-11-01: the OTLP endpoint of the EU region is api.eu1.honeycomb.io | capture: sha256:72b7b30bf5d94b5baa5e6b00b3482ef56c124a94121df53a418127f528d18990 | quote: #export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.eu1.honeycomb.io:443 # EU
  - [11] 2026-11-01: the US MCP server is at https://mcp.honeycomb.io/mcp and authenticates with OAuth | capture: sha256:b9b0efe54925e3079c1fded18f7f1a5dc7e22b96e84a6c55cb466eb030df2eb6 | quote: Add the Honeycomb MCP server at https://mcp.honeycomb.io/mcp and authenticate with OAuth.
  - [11] 2026-11-01: the EU MCP server is at https://mcp.eu1.honeycomb.io/mcp and authenticates with OAuth | capture: sha256:b9b0efe54925e3079c1fded18f7f1a5dc7e22b96e84a6c55cb466eb030df2eb6 | quote: Add the Honeycomb MCP server at https://mcp.eu1.honeycomb.io/mcp and authenticate with OAuth.
  - [11] 2026-11-01: the MCP server can also authenticate with an API key | capture: sha256:b9b0efe54925e3079c1fded18f7f1a5dc7e22b96e84a6c55cb466eb030df2eb6 | quote: This guide covers the fastest way to connect, manual configuration for specific clients, and authentication with an API key.
  - [12] 2026-11-01: the hosted MCP server is available on every Honeycomb plan, including free, at no charge | capture: sha256:b482c93515ae621fe9a097a6f3b0258438608685b2aacff8cee6ce2060d442f7 | quote: Hosted MCP is available on AWS AI Agents marketplace and for all Honeycomb plans (including our free plan!) at no charge.
- sources:
  - [1] https://www.honeycomb.io/pricing
  - [2] https://docs.honeycomb.io/api/events/create-an-event
  - [3] https://docs.honeycomb.io/get-started/manage-costs/how-honeycomb-calculates-usage
  - [4] https://support.honeycomb.io/articles/2222640834-what-are-honeycomb-s-rate-limits-events-per-second-for-sending-events
  - [5] https://ui.honeycomb.io/signup
  - [6] https://docs.honeycomb.io/get-started/create-account
  - [7] https://docs.honeycomb.io/api/
  - [8] https://docs.honeycomb.io/send-data/opentelemetry/collector
  - [9] https://docs.honeycomb.io/send-data/opentelemetry
  - [10] https://docs.honeycomb.io/api/events/create-events
  - [11] https://docs.honeycomb.io/integrations/mcp/configuration-guide
  - [12] https://www.honeycomb.io/blog/hosted-mcp-now-available
