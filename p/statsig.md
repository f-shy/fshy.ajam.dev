# Statsig

> statsig.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/statsig/ | JSON https://fshy.ajam.dev/api/v1/entity/statsig.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Statsig

- `dev-services/statsig` | qualifies-with-caveat | evidence documented | binding volume-quota | category feature flags, experimentation and product analytics (hosted) | tier Developer
- needs card yes, phone unknown, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://www.statsig.com/pricing
- free tier: Developer tier, free: 2 million metered events every calendar month at no charge, with free access to feature gates, dynamic configs, experimentation and core product analytics, and 1 year of analytics data retention; past 2 million events gate and config targeting keeps working and metric lift computation stops | unit: requests | metered on: request-count | read on: 2026-11-01 | source: [1] | note: The unit is the metered event: an SDK call that logs an event, an exposure check with metric lift enabled, an ingested metric or a custom metric. The vocabulary has no events term, so requests is the nearest. An account starts on the Developer tier at sign-up; the Pro tier is USD 150 a month with 5 million metered events.
- per-object cap: unverified: no per-event or per-request size is stated on the pages read
- retention: 1 year of data retention for analysis on the free tier, against unlimited on Pro | days: 365 | source: [1]
- egress: unverified: the pricing page lists a data export API (export exposure, event and result data) but its captured text does not show which tier includes it | metered: no | source: [1]
- identity: email | detail: An account starts on the Developer tier at sign-up and a credit card is asked only when the 2 million events are exceeded. Which sign-in methods the sign-up form offers is unverified: its page text shows no form; any phone step is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 2 million metered events per calendar month on the Developer tier [1]
  - retention-clamped: 1 year of analytics data retention on the free tier [1]
  - request-rate: Console API: about 1,800 request attempts per 15-minute window per project for mutation requests, with burst protection [2]
- limits note: Gates and configs keep evaluating past the monthly events, while metric lift computations stop after warning notifications.
- binding note: The 2 million metered events a month is the ceiling for an app with traffic, and exposure checks count against it as well as logged events.
- interface detail: A Console API at statsigapi.net (CRUD for what the console does) takes a Console API key in the STATSIG-API-KEY header; an HTTP API takes a server-side secret key or a client SDK key in the statsig-api-key header, with every call a POST and a JSON body. SDKs are recommended over the HTTP API.
- endpoint: https://statsigapi.net
- tooling: the SDKs, the HTTP API, the Console API and the web console
- composes with: Feature gates, dynamic configs and experiments for a free-hosted app, with the first 2 million metered events a month free and product analytics in the same project.
- reliability: past the free events, metric lift computations stop after several warning notifications while gate and config targeting continues
- notes: Past the free events the offered upgrade is the Pro tier at USD 150 a month, which includes 5 million metered events a month.
- evidence note: The free allowance, the card prompt and the retention are quoted from the first-party pricing FAQ and the API limits from its documentation. No account was opened, so the sign-up fields are unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: an account starts on the free Developer tier with 2 million metered events a month at no charge | capture: sha256:83599526d3f7cc93166961da7608af9227846c5974f1cef9f74d1ea23fcff248 | quote: When you first sign up for Statsig, you automatically start on Statsig’s Developer Tier, which gives you free access to gates, configs, experimentation and analytics. On this plan, you get 2 million Metered Events (see definition below) every calendar month at no charge.
  - [1] 2026-11-01: a credit card is asked only when the 2 million event limit is exceeded | capture: sha256:83599526d3f7cc93166961da7608af9227846c5974f1cef9f74d1ea23fcff248 | quote: If you exceed the 2 million Developer Tier events limit, you’ll be shown a prompt to enter a credit card to upgrade to Statsig’s Pro tier.
  - [1] 2026-11-01: on the Developer tier gate and config targeting continues while metric lift computations stop | capture: sha256:83599526d3f7cc93166961da7608af9227846c5974f1cef9f74d1ea23fcff248 | quote: If you want to stay on the Developer tier, gate and config targeting will continue to work, but Metric Lift computations will stop.
  - [1] 2026-11-01: warning notifications precede the end of metric lift computations | capture: sha256:83599526d3f7cc93166961da7608af9227846c5974f1cef9f74d1ea23fcff248 | quote: You will be sent multiple warning notifications before Metric Lifts are no longer calculated.
  - [1] 2026-11-01: the free tier includes core product analytics with 1 year of data retention | capture: sha256:83599526d3f7cc93166961da7608af9227846c5974f1cef9f74d1ea23fcff248 | quote: On the free tier that includes our Core Product Analytics features and 1 year of data retention for analysis.
  - [1] 2026-11-01: an exposure check with metric lift and a logged event are metered events | capture: sha256:83599526d3f7cc93166961da7608af9227846c5974f1cef9f74d1ea23fcff248 | quote: Log event: When an application calls the Statsig SDK to log an event or when an event is imported to Statsig from a 3rd party source (e.g. Segment)
  - [1] 2026-11-01: the Pro tier has a baseline fee of USD 150 a month | capture: sha256:83599526d3f7cc93166961da7608af9227846c5974f1cef9f74d1ea23fcff248 | quote: On Statsig’s Pro tier, you will be charged a baseline fee of $150 per month at the start of each billing period.
  - [1] 2026-11-01: the Pro tier includes 5 million metered events a month | capture: sha256:83599526d3f7cc93166961da7608af9227846c5974f1cef9f74d1ea23fcff248 | quote: Statsig’s Pro Tier includes 5 million Metered Events per month.
  - [2] 2026-11-01: the Console API is the CRUD API for what the console does without the web UI | capture: sha256:fe4c1279581873967dc6c0b9a4d0927299edbad392c19eb8b06403683eb75b2e | quote: The Console API is the CRUD API for performing the actions available on console.statsig.com without using the web UI.
  - [3] 2026-11-01: SDKs are recommended over the HTTP API | capture: sha256:19d5f5e4bc68327608b8677532a951b410ef39868f2c1191b8534c64e2e24ca0 | quote: Statsig strongly recommends using an official SDK for your programming language whenever possible.
  - [2] 2026-11-01: the Console API is served at statsigapi.net | capture: sha256:fe4c1279581873967dc6c0b9a4d0927299edbad392c19eb8b06403683eb75b2e | quote: `https://statsigapi.net`
  - [2] 2026-11-01: the Console API takes a key in the STATSIG-API-KEY header | capture: sha256:fe4c1279581873967dc6c0b9a4d0927299edbad392c19eb8b06403683eb75b2e | quote: All requests must include a Console API key in the `STATSIG-API-KEY` header.
  - [2] 2026-11-01: the Console API allows about 1,800 mutation request attempts per 15 minutes per project | capture: sha256:fe4c1279581873967dc6c0b9a4d0927299edbad392c19eb8b06403683eb75b2e | quote: The default quota is approximately 1,800 request attempts per 15-minute window.
  - [3] 2026-11-01: the HTTP API authenticates with a statsig-api-key header and takes POST requests with a JSON body | capture: sha256:19d5f5e4bc68327608b8677532a951b410ef39868f2c1191b8534c64e2e24ca0 | quote: Authenticate using the `statsig-api-key` header. All API requests use the POST method, and you pass parameters as a JSON object in the request body.
  - [3] 2026-11-01: the HTTP API documentation tells the reader to create a free account | capture: sha256:19d5f5e4bc68327608b8677532a951b410ef39868f2c1191b8534c64e2e24ca0 | quote: Create a free account on the [Statsig sign-up page](https://statsig.com).
- sources:
  - [1] https://www.statsig.com/pricing
  - [2] https://docs.statsig.com/console-api/introduction
  - [3] https://docs.statsig.com/http-api
