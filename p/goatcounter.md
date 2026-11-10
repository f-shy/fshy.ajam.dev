# GoatCounter

> goatcounter.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/goatcounter/ | JSON https://fshy.ajam.dev/api/v1/entity/goatcounter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GoatCounter

- `dev-services/goatcounter` | qualifies-with-caveat | evidence documented | binding volume-quota | category privacy-friendly web analytics (hosted) | tier Free hosted service
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://www.goatcounter.com/
- free tier: Free for reasonable public usage: a personal website or a small-to-medium business is fine, while sending millions of pageviews a day is not; no numeric cap is stated | unit: unlimited | metered on: none | read on: 2026-11-01 | source: [1] | note: Financed by donations through GitHub Sponsors. Several sites can share one account (Settings, sites). The hosted service and the open-source app share the same code; the hosted service is the offer recorded here.
- per-object cap: unverified: no per-pageview or per-request size is stated on the pages read
- retention: unverified: no retention period of the hosted service is stated on the pages read; all data can be exported at any time | source: [1]
- egress: all data can be exported as CSV at any time, through the dashboard or the export endpoints of the API; the API allows 4 requests per second | metered: no | source: [2]
- identity: email | detail: The sign-up form asks for an account name, an optional site domain, an email address and a password of at least 8 characters, plus a human check that asks the visitor to type a shown number; no payment field appears on it.
- interface: rest
- limits:
  - request-rate: API: 4 requests per second, reported in the X-Rate-Limit response headers [2]
  - volume-quota (binding): free for reasonable public usage, with no number stated; millions of pageviews a day are outside it [1]
- limits note: The backend count endpoint has higher rate limits than the browser endpoint and accepts several pageviews in one request.
- binding note: The only quota is the unstated reasonable-use ceiling; the 4-requests-a-second API limit binds only on programmatic reads.
- interface detail: REST API under /api/v0 on the account's own host (CODE.goatcounter.com), authenticated by an API key created in the account as a Bearer token (HTTP Basic also works); POST /api/v0/count sends pageviews from a backend in batches, POST /api/v0/export starts a CSV export, and GET endpoints list sites, paths and statistics. The browser side is one script tag, a no-JavaScript tracking pixel, backend middleware or log file import.
- endpoint: https://CODE.goatcounter.com/api/v0
- tooling: a single script tag, the tracking pixel, middleware or log file import for the data in, and any HTTP client with an API key for the data out. As a last resort the open-source app can be self-hosted: the user installs and runs it on a rented or free machine.
- composes with: Pageview counting for a static site on any free host with one script tag and no cookies, with the numbers readable and exportable through the API.
- reliability: no throttle, ban or data loss is stated on the pages read; the service is financed by donations
- notes: Third-party lists give a monthly pageview cap and a retention period that the first-party pages read do not state, so neither is recorded as a limit.
- evidence note: The free offer, the sign-up fields and the API limits are quoted from first-party pages. No account was opened and no numeric allowance or retention period is published, so both are unverified.
- self hosted: no
- evidence:
  - [1] 2026-11-01: the hosted service is free for reasonable public usage and millions of pageviews a day are outside that | capture: sha256:54855f193d6a7c263b57345d3d86797c318420b584d7d672d9d55e6b069ed421 | quote: GoatCounter.com is currently offered for free for reasonable public usage. Running your personal website or small-to-medium business on it is fine, but sending millions of pageviews/day isn’t.
  - [1] 2026-11-01: the hosted service is financed by donations | capture: sha256:54855f193d6a7c263b57345d3d86797c318420b584d7d672d9d55e6b069ed421 | quote: Donations are accepted via [Github Sponsors](https://github.com/sponsors/arp242/) to cover server costs.
  - [1] 2026-11-01: the app can be self-hosted from its GitHub repository | capture: sha256:54855f193d6a7c263b57345d3d86797c318420b584d7d672d9d55e6b069ed421 | quote: You can [self-host GoatCounter](https://github.com/arp242/goatcounter) easily if you want to use it for more serious purposes.
  - [1] 2026-11-01: data can be exported and the account cancelled at any time | capture: sha256:54855f193d6a7c263b57345d3d86797c318420b584d7d672d9d55e6b069ed421 | quote: Own your data; you can always export all data and cancel at any time.
  - [1] 2026-11-01: the browser side is a single script tag, with a no-JavaScript image tracker, middleware and log file alternatives | capture: sha256:54855f193d6a7c263b57345d3d86797c318420b584d7d672d9d55e6b069ed421 | quote: The JavaScript integration is a good option for most, but you can also use a no-JavaScript image-based tracker, integrate in your backend middleware, or parse log files.
  - [2] 2026-11-01: the API is limited to 4 requests per second | capture: sha256:622f6af9fb98d74ad85f7882c8b6ae0fa541421aa655434aa2650ceb6fd80046 | quote: The rate limit is 4 requests per second; the current values are reported in the response headers:
  - [2] 2026-11-01: the API authenticates with a Bearer API key created in the account | capture: sha256:622f6af9fb98d74ad85f7882c8b6ae0fa541421aa655434aa2650ceb6fd80046 | quote: To use the API create a key in your account (`[Username in top menu] → API`); send the API key in the `Authorization` header as `Authorization: Bearer [token]`.
  - [2] 2026-11-01: HTTP Basic authentication with the API key as the password is also supported | capture: sha256:622f6af9fb98d74ad85f7882c8b6ae0fa541421aa655434aa2650ceb6fd80046 | quote: HTTP Basic auth is also supported; this is mostly useful for testing things from the browser. Leave the username empty and use the API key as the password.
  - [2] 2026-11-01: the count endpoint sends pageviews from a backend with higher rate limits and batching | capture: sha256:622f6af9fb98d74ad85f7882c8b6ae0fa541421aa655434aa2650ceb6fd80046 | quote: This is the same as `/count` that the JavaScript integration uses but has higher rate-limits, allows setting some additional fields, and allows batching multiple pageviews in one request.
  - [2] 2026-11-01: a CSV export is started through the API | capture: sha256:622f6af9fb98d74ad85f7882c8b6ae0fa541421aa655434aa2650ceb6fd80046 | quote: | `POST /api/v0/export` | Create a new CSV export |
  - [3] 2026-11-01: the sign-up form asks for an email address and a password of at least 8 characters | capture: sha256:554115020fe8c3b0b66a951db382a66ed2b5595c87ce50578a3b07e4cd72f8ed | quote: Email address For password resets, important announcements, invoices.
  - [3] 2026-11-01: the password needs at least 8 characters | capture: sha256:554115020fe8c3b0b66a951db382a66ed2b5595c87ce50578a3b07e4cd72f8ed | quote: Password Needs at least 8 characters.
  - [3] 2026-11-01: the sign-up form has a human check that asks the visitor to type a shown number | capture: sha256:554115020fe8c3b0b66a951db382a66ed2b5595c87ce50578a3b07e4cd72f8ed | quote: Fill in 9 here Just a little verification that you’re human :-)
  - [4] 2026-11-01: an email address is required to register an account | capture: sha256:8c98c22d3283e73e1c3159296cd75f5bed811a1caca1e535fa15b512e3f556db | quote: We require an email address to register an account.
- sources:
  - [1] https://www.goatcounter.com/
  - [2] https://www.goatcounter.com/help/api
  - [3] https://www.goatcounter.com/signup
  - [4] https://www.goatcounter.com/terms
