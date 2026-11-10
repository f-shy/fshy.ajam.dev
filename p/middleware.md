# Middleware

> middleware.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/middleware/ | JSON https://fshy.ajam.dev/api/v1/entity/middleware.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Middleware

- `dev-services/middleware` | qualifies-with-caveat | evidence documented | binding volume-quota | category observability with data ingestion, RUM sessions and synthetic checks, on OpenTelemetry agents | tier Free Forever
- needs card yes, phone no, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://middleware.io/pricing/
- free tier: Free Forever plan, monthly allowances: 100 GB of data ingestion, 1,000 RUM sessions, 20,000 synthetic checks, 10 browser tests and 2 million OpsAI tokens; a credit card is required to activate the plan and only usage above the allowances is charged | unit: mixed | metered on: uploaded-bytes | read on: 2026-11-01 | source: [1] | note: The allowance mixes ingested bytes with counts of sessions, checks, tests and tokens, so no single unit of the vocabulary fits. The pricing page FAQ still describes a 14-day free trial with unlimited data ingestion for the Free tier and was not updated with the plan announced on 9 September 2026; pay as you go is described there as a flat rate for data volume.
- per-object cap: unverified: no per-event or per-log-line size is stated on the pages read
- retention: 14 days on the free tier, against 30 days on pay as you go | days: 14 | source: [2]
- egress: unverified: no egress term on the pages read; on cancellation data is kept 30 days so it can be downloaded | metered: no | source: [2]
- identity: card | detail: A credit card is required to activate the Free Forever plan. The sign-up form asks for a username, an email address, a password and an optional company name, or Google or GitHub sign-in.
- interface: unknown
- limits:
  - volume-quota (binding): 100 GB of data ingestion, 1,000 RUM sessions, 20,000 synthetic checks, 10 browser tests and 2 million OpsAI tokens per month [1]
  - retention-clamped: 14 days of retention on the free tier [2]
- binding note: The 100 GB monthly ingestion is the first ceiling for a logging workload, after the card that activates the plan.
- interface detail: Data is sent by Middleware agents, which use OpenTelemetry as their framework, and by other collectors such as Prometheus and database integrations; no management API is named on the pages read, so the interface is unverified.
- tooling: Middleware agents built on OpenTelemetry, other collectors and the web app
- composes with: Logs, host metrics and traces of a free-hosted app in one place, up to 100 GB of ingestion a month on the plan once a card is on file.
- reliability: only usage above the monthly allowances is charged, so an ingestion spike past 100 GB bills the card on file; data older than the 14-day retention is deleted
- notes: The plan needs a card on file, so it is a free allowance behind a payment method, not a no-card tier.
- evidence note: The plan, its allowances and the card requirement are quoted from the first-party release notes and product update; the retention comes from the pricing page FAQ, which also still describes a 14-day trial. No account was opened, so the card step is unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the Free Forever plan has monthly allowances of 100 GB of ingestion, 1,000 RUM sessions, 20,000 synthetic checks, 10 browser tests and 2 million OpsAI tokens | capture: sha256:6e0ce4f058ddf9147f267d3b4f18bff5d52e5e023893f10118de26031af67313 | quote: - 100 GB of data ingestion - 1,000 RUM sessions - 20,000 synthetic checks - 10 browser tests - 2 million OpsAI tokens
  - [1] 2026-11-01: a credit card is required to activate the plan and only usage above the allowances is charged | capture: sha256:6e0ce4f058ddf9147f267d3b4f18bff5d52e5e023893f10118de26031af67313 | quote: A credit card is required to activate the plan. Only usage above the monthly allowances is charged.
  - [1] 2026-11-01: the Free Forever plan was introduced in release 2.8.2 of 9 September 2026 | capture: sha256:6e0ce4f058ddf9147f267d3b4f18bff5d52e5e023893f10118de26031af67313 | quote: Middleware v2.8.2 introduces the Free Forever plan and updates log anomaly detection, alert configuration, and Node.js exception capture.
  - [3] 2026-11-01: a credit card is required to activate the Free Forever plan | capture: sha256:116b4d0e5593e0dd2513ff0d34e770aa16d9736782e521b560ced002c665559e | quote: A credit card is required to activate the Free Forever plan.
  - [3] 2026-11-01: free usage is excluded from billable usage so charges start only above the included limits | capture: sha256:116b4d0e5593e0dd2513ff0d34e770aa16d9736782e521b560ced002c665559e | quote: Free usage is excluded from billable usage, so you’re only charged when usage exceeds the included monthly limits.
  - [2] 2026-11-01: the free tier retains data 14 days and pay as you go 30 days | capture: sha256:eed361cfdd44557281df89e302396f52335a593578a7d29ac9139aaa8f819730 | quote: Our free tier is 14 days, pay-as-you-go is 30, and custom contracts have custom retention rates.
  - [2] 2026-11-01: the pricing FAQ still describes a 14-day free trial with unlimited data ingestion | capture: sha256:eed361cfdd44557281df89e302396f52335a593578a7d29ac9139aaa8f819730 | quote: Free trial is to use Middleware for 14 days with unlimited data ingestion for free .
  - [2] 2026-11-01: data is kept 30 days after cancellation so it can be downloaded | capture: sha256:eed361cfdd44557281df89e302396f52335a593578a7d29ac9139aaa8f819730 | quote: We keep your data for 30 days from the cancellation date so you can download them.
  - [2] 2026-11-01: agents use OpenTelemetry as their framework and other collectors such as Prometheus are supported | capture: sha256:eed361cfdd44557281df89e302396f52335a593578a7d29ac9139aaa8f819730 | quote: We leverage Otel as a framework for our agents ... We also support many other data collectors and origins like Prometheus, databases, etc.
  - [4] 2026-11-01: the sign-up form asks for a username, an email address, a password and an optional company name, with Google and GitHub sign-in | capture: sha256:ec0a0fd2d352339388bfb52b7247dccb66d7882b82109d67fca202c09158880c | quote: Google Github or Username\* Email Address\* Password\* Company Name (Optional)
- sources:
  - [1] https://docs.middleware.io/release-notes/release-70
  - [2] https://middleware.io/pricing/
  - [3] https://middleware.io/product-updates/september-2026/
  - [4] https://app.middleware.io/auth/register
