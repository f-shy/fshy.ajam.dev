# Amplitude

> amplitude.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/amplitude/ | JSON https://fshy.ajam.dev/api/v1/entity/amplitude.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Amplitude

- `dev-services/amplitude` | qualifies-with-caveat | evidence documented | binding volume-quota | category product analytics with session replay, feature flags and experimentation (hosted) | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://amplitude.com/pricing
- free tier: Free plan, forever and with no credit card required: 2M events per month, unlimited team members, 10,000 monthly session replays kept 1 month, 5,000 monthly agent sessions, 2,000 monthly AI feedback records, unlimited feature flags and 1 active experiment; analytics data is accessible for 1 year | unit: mixed | metered on: request-count | read on: 2026-11-01 | source: [1] | note: Events are the headline count; session replays, agent sessions and feedback records each have their own monthly count, so no single unit of the vocabulary fits. The FAQ states the Free plan has a fixed limit of 2 million events a month and is not a trial. Plus is described as free for the first 2M events a month but needs a credit card.
- per-object cap: the HTTP V2 API rejects a request larger than 1 MB with a 413 error, and the Free plan is advised to send no more than 10 events per batch; the Batch Event Upload API accepts up to 20 MB per request | source: [2]
- retention: 1 year of data access on Free (2 years on Plus); session replays are kept 1 month; agent session chats are kept 14 days | days: 365 | source: [1]
- egress: unverified: no export allowance or price is stated on the pricing page, which lists developer SDKs and APIs as included on every plan | metered: no | source: [1]
- identity: email | detail: The pricing page states the Free plan needs no credit card; the sign-up page asks for a work email address behind a reCAPTCHA. Any later step, such as a phone number or the choice of region, is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 2M events per month on Free [1]
  - volume-quota (binding): 10,000 session replays, 5,000 agent sessions and 2,000 AI feedback records per month [1]
  - request-rate: HTTP V2 upload on Free: 100 batches per second and 1000 events per second [2]
  - per-object-cap: 1 MB per HTTP V2 request [2]
  - retention-clamped: 1 year of data access, 1 month of session replays, 14 days of agent session chats [1]
- limits note: Free keeps 10 saved charts per organization and has no webhooks.
- binding note: The fixed 2M events a month is the first ceiling for an app with traffic; the 1000-events-a-second upload rate binds only a bulk import.
- interface detail: Event ingestion through the HTTP V2 API at api2.amplitude.com (EU residency: api.eu.amplitude.com), with an API key in the JSON body, and through SDKs; an MCP server connects AI tools to Amplitude data on every plan, Free included. Webhooks are not included on Free.
- endpoint: https://api2.amplitude.com/2/httpapi
- tooling: the web and mobile SDKs, the HTTP V2 and Batch Event Upload APIs, and the web app; an MCP server for AI tools
- composes with: Product analytics for the front end of a free-hosted app, up to 2M events a month, with feature flags, one experiment and 10,000 session replays in the same project.
- reliability: no throttle, ban or data loss is stated on the pages read; user property updates past 1800 an hour for one user may be dropped while events are still ingested
- notes: Startups with under USD 10M in funding and fewer than 20 employees receive one free year of the Growth plan, a separate offer; the Plus plan starts at USD 0 for the first 2M events a month but requires a credit card.
- evidence note: Plan limits are quoted from the first-party pricing page and the API limits from its documentation; the sign-up page was read through a pinned page reader. No account was opened, so what happens past 2M events is unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the Free plan includes 2M events a month forever | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: 2M Events/month forever.
  - [1] 2026-11-01: the Free plan needs no credit card | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: No Credit Card required.
  - [1] 2026-11-01: the Free plan is not a trial and has no time limit | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: It's not a trial. There's no time limit.
  - [1] 2026-11-01: the Free plan has a fixed limit of 2 million events a month | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: Free comes with a fixed limit of 2 million events per month, perfect for learning and finding product-market fit.
  - [1] 2026-11-01: the Free plan counts up to 2M events and Plus requires a credit card | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | MTUs / EV | Up to 2M EV | Up to 700K MTU / 70M EV | Custom | Custom |
  - [1] 2026-11-01: the Plus plan starts at $0 with the first 2M events a month free and requires a credit card | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: Starts at $0 First 2M Events/month free. [Get started](https://app.amplitude.com/signup?next=%2Fcheckout) Credit Card required.
  - [1] 2026-11-01: startups under USD 10M in funding and under 20 employees receive one free year of the Growth plan | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: Startups with under $10M in funding and fewer than 20 employees receive one free year on our Growth plan.
  - [1] 2026-11-01: the Free plan has unlimited team members | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | Team members | Unlimited | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-01: the Free plan allows 10,000 session replays a month | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | Monthly sessions | 10,000 | 10,000 | 20,000 Add-on for more | 50,000 Add-on for more |
  - [1] 2026-11-01: session replays are kept 1 month | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | Replay retention | 1 month | 1 month | 1 month Add-on for more | 1 month Add-on for more |
  - [1] 2026-11-01: the Free plan allows 5,000 agent sessions a month | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | Monthly Agent Sessions | 5,000 | 5,000 | 10,000 Add-on for more | 20,000 Add-on for more |
  - [1] 2026-11-01: agent session chats are kept 14 days on Free | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | Agent Session Chats Retained | 14 days | 14 days | 30 days Add on for 90 days | 30 days Add on for 90 days |
  - [1] 2026-11-01: the Free plan allows 2,000 AI feedback records a month | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | Monthly feedback records | 2,000 | 2,000 | 2,000 Add-on for more | 2,000 Add-on for more |
  - [1] 2026-11-01: feature flags are unlimited on Free | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | Feature flags | Unlimited | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-01: analytics data access is 1 year on Free and 2 years on Plus | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | Data access | 1 year | 2 years | Unlimited | Unlimited |
  - [1] 2026-11-01: Free keeps 10 saved charts per organization | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | Saved charts | 10 per org | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-01: developer SDKs and APIs are included on Free | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | Developer SDKs and APIs | Included | Included | Included | Included |
  - [1] 2026-11-01: webhooks are not included on Free | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: | Webhooks | Not included | Included | Included | Included |
  - [1] 2026-11-01: the MCP connection to AI tools works on every plan including Free | capture: sha256:941153f939b20c7e6584eaddcd8c4be299239860d615c5707663f1cbe0057383 | quote: This works on every plan, including the Free plan.
  - [2] 2026-11-01: on the Free plan uploads are limited to 100 batches and 1000 events per second | capture: sha256:13578badf9d9c94fc04b6f4522b16c294ef54f53a17cbaacc0b691fc03cce586 | quote: Limit your upload to 100 batches per second and 1000 events per second.
  - [2] 2026-11-01: the HTTP V2 API rejects a request larger than 1 MB | capture: sha256:13578badf9d9c94fc04b6f4522b16c294ef54f53a17cbaacc0b691fc03cce586 | quote: The payload size is too big (request size exceeds 1 MB).
  - [2] 2026-11-01: events are ingested at api2.amplitude.com, with an EU host | capture: sha256:13578badf9d9c94fc04b6f4522b16c294ef54f53a17cbaacc0b691fc03cce586 | quote: This API uses the event ingestion host `api2.amplitude.com` (default) or `api.eu.amplitude.com` (EU).
  - [2] 2026-11-01: a user's property updates beyond 1800 an hour can be dropped while events are ingested | capture: sha256:13578badf9d9c94fc04b6f4522b16c294ef54f53a17cbaacc0b691fc03cce586 | quote: Amplitude continues to ingest events, but may drop user property updates for that user.
  - [3] 2026-11-01: both upload APIs take JSON with an api_key and an events array | capture: sha256:f3f0e4e2b8b265aab816af5a7b7566095beba582391421eb63ff05a36c13ddcb | quote: Both APIs accept `application/json` requests with an `api_key` and an `events` array.
  - [3] 2026-11-01: the Batch Event Upload API accepts payloads up to 20MB | capture: sha256:f3f0e4e2b8b265aab816af5a7b7566095beba582391421eb63ff05a36c13ddcb | quote: The JSON serialized payload must not exceed 20MB in size.
  - [4] 2026-11-01: the sign-up page asks for a work email address | capture: sha256:6bc7886a89a27a5e48f3eac6b21eb434cadcbabdb90ec2f4a8059c1a05166e08 | quote: # Log in or Sign up Work Email
- sources:
  - [1] https://amplitude.com/pricing
  - [2] https://amplitude.com/docs/apis/analytics/http-v2
  - [3] https://amplitude.com/docs/apis/analytics/batch-event-upload
  - [4] https://app.amplitude.com/signup
