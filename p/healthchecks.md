# Healthchecks.io

> healthchecks.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/healthchecks/ | JSON https://fshy.ajam.dev/api/v1/entity/healthchecks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Healthchecks.io

- `dev-services/healthchecks-io` | qualifies-with-caveat | evidence documented | binding volume-quota | category cron job and background task monitoring (dead man's switch, hosted) | tier Hobbyist
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://healthchecks.io/pricing/
- free tier: Hobbyist plan at USD 0 a month: 20 monitored jobs (checks) per account and 100 log entries per job; the Supporter plan at USD 5 a month has the same limits | unit: objects | metered on: object-count | read on: 2026-11-01 | source: [1] | note: The unit counted is the check, one per monitored job. A check is up while pings arrive within its period plus grace time and goes down, with a notification, when they stop. The Business plan (USD 20 a month, 100 jobs) is offered free of charge to open-source projects and nonprofits on request.
- per-object cap: the first 100 kB of the request body of each received ping is stored; the Ping-Body-Limit response header reports the limit in bytes | bytes: 100000 | source: [2]
- retention: 100 log entries are kept per job on the Hobbyist plan and the oldest entry is removed when the limit is reached; a job that pings every 5 minutes is covered for about 8 hours | source: [1] | note: Paid plans keep 1000 log entries per job. The API lists at most 100 logged pings for a free account.
- egress: not applicable: an inbound ping receiver; the ping log of a check is read back through the API, which returns 100 pings for free accounts and 1000 for paid accounts | metered: no | source: [3]
- identity: email | detail: The login page offers Create Your Account and states that a magic login link is emailed; payment details are entered under Account Settings, Billing, when a paid plan is chosen.
- interface: rest
- limits:
  - volume-quota (binding): 20 checks per account on the Hobbyist plan [3]
  - retention-clamped: 100 log entries kept per check, oldest removed first [1]
  - request-rate: Management API: avoid more than 100 requests per minute; ping endpoints: a check pinged more than 5 times per minute may have requests ignored [3]
  - per-object-cap: 100 kB of ping request body stored per ping [2]
- limits note: Notification credits for SMS, WhatsApp and phone calls are listed on the Business and Business Plus plans only.
- binding note: The 20-check cap is reached before any rate limit by an account that monitors many jobs; the 5-pings-a-minute rule binds only a job that pings in a tight loop.
- interface detail: Ping endpoints at hc-ping.com take HEAD, GET and POST requests with no key in the URL path beyond the check UUID or slug; a Management API v3 at healthchecks.io/api/v3 takes an X-Api-Key header with a project-specific read-write or read-only key.
- endpoint: https://healthchecks.io/api/v3/checks/
- tooling: curl or any HTTP client against the ping URLs and the Management API, and the web dashboard. As a last resort the server is open source under the BSD 3-clause license: the user installs and runs it on a rented or free machine.
- composes with: Dead man's switch for the scheduled jobs of free hosts: a cron line, a CI schedule or a serverless timer sends one HTTP request to a ping URL, and the check alerts by email or chat when the ping stops arriving.
- reliability: Pings above 5 a minute to one check are answered 200 but not recorded; an account inactive for over a year is closed 30 days after an email notice.
- notes: The free plan caps the number of jobs, not the number of pings, so a small set of frequently pinging jobs fits easily; the Business plan at USD 20 a month raises the cap to 100 jobs.
- evidence note: Plan limits, rate limits and the sign-up method are quoted from first-party pages. No account was opened, so whether any later step asks for a phone number is unverified: behind a sign-up. An authenticated API call from a free account would move the record to measured.
- self hosted: no
- evidence:
  - [1] 2026-11-01: the Hobbyist plan costs USD 0 a month and monitors 20 jobs with 100 log entries per job | capture: sha256:beba7838c3d9291779324073380b01187a5f6954dd278017d5238673c3861143 | quote: ## Hobbyist $0 / month - Monitor 20 jobs - 100 log entries per job
  - [1] 2026-11-01: the Business plan costs USD 20 a month with 100 jobs, 1000 log entries per job and SMS, WhatsApp and phone call credits | capture: sha256:beba7838c3d9291779324073380b01187a5f6954dd278017d5238673c3861143 | quote: ## Business $20 / month - Monitor 100 jobs - 1000 log entries per job - 50 SMS & WhatsApp credits - 20 phone call credits
  - [4] 2026-11-01: a check goes down, with a notification, when pings stop arriving within the period plus grace time | capture: sha256:a3ccfe4d843188f5ec1fd3f37413d00202b218be796c8f3d65b8c4b96049432a | quote: Down. The time since the last ping has exceeded Period + Grace. When a check goes from "Late" to "Down", Healthchecks.io sends you a notification.
  - [1] 2026-11-01: the USD 5 Supporter plan does not raise the Hobbyist limits | capture: sha256:beba7838c3d9291779324073380b01187a5f6954dd278017d5238673c3861143 | quote: The "Hobbyist" and "Supporter" plans have the same limits.
  - [1] 2026-11-01: log entries beyond the per-job limit displace the oldest ones | capture: sha256:beba7838c3d9291779324073380b01187a5f6954dd278017d5238673c3861143 | quote: When the limit is reached, the oldest log entries are removed to make room for new ones.
  - [1] 2026-11-01: 100 log entries cover about 8 hours of a job that pings every 5 minutes | capture: sha256:beba7838c3d9291779324073380b01187a5f6954dd278017d5238673c3861143 | quote: if the cron job runs every 5 minutes, the 100 log entries will only cover 8 hours.
  - [1] 2026-11-01: the Business plan is free for open-source projects and nonprofits | capture: sha256:beba7838c3d9291779324073380b01187a5f6954dd278017d5238673c3861143 | quote: We offer the Business plan free of charge for open-source projects and nonprofits.
  - [3] 2026-11-01: free accounts are limited to 20 checks | capture: sha256:08406848438f2fde2996c3c15158baa64977f10ef0cf01e6f68fb25375bdedeb | quote: For free accounts, the limit is 20 checks per account.
  - [3] 2026-11-01: the Management API should not be called more than 100 times a minute | capture: sha256:08406848438f2fde2996c3c15158baa64977f10ef0cf01e6f68fb25375bdedeb | quote: Avoid making more than 100 API requests per minute. If you exceed this limit, you will eventually see HTTP 429 errors.
  - [3] 2026-11-01: the API authenticates with an X-Api-Key header and the keys are project-specific | capture: sha256:08406848438f2fde2996c3c15158baa64977f10ef0cf01e6f68fb25375bdedeb | quote: The client can authenticate itself by including an `X-Api-Key: <your-api-key>` header in an HTTP request.
  - [3] 2026-11-01: the ping log returns 100 pings for free accounts and 1000 for paid accounts | capture: sha256:08406848438f2fde2996c3c15158baa64977f10ef0cf01e6f68fb25375bdedeb | quote: the total number of returned pings depends on the account's billing plan: 100 for free accounts, 1000 for paid accounts.
  - [2] 2026-11-01: ping endpoints take HEAD, GET and POST requests and only the first 100 kB of a ping request body is stored | capture: sha256:fc4bb6307dbf637a365f8b38f357261177f02ccce9b64d3636804716e86cfc30 | quote: HEAD, GET, and POST request methods. For HTTP POST requests, clients can optionally include diagnostic information in the request body. If the request body looks like a UTF-8 string, Healthchecks.io stores the request body (limited to the first 100 kB for each received ping).
  - [2] 2026-11-01: a check pinged more than 5 times a minute may have requests dropped | capture: sha256:fc4bb6307dbf637a365f8b38f357261177f02ccce9b64d3636804716e86cfc30 | quote: If you ping a check more than 5 times per minute, some of the requests may get rate limited and not recorded to the database.
  - [5] 2026-11-01: the account is created from an email address and a magic login link is emailed | capture: sha256:a4438204392ef1c4f5665d7165686d60f992fbf589b10238f74045e2e710acdf | quote: We will email you a magic log in link.
  - [6] 2026-11-01: payment details are entered in the billing settings after the account exists | capture: sha256:75955ff35f79e07819d788598ba5fdb65995822e1e74ee0df5246e649802ebf5 | quote: after register for an account on Healthchecks.io, navigate to Account Settings › Billing, select a plan, and enter your payment details.
  - [7] 2026-11-01: an account inactive for more than a year is closed 30 days after a notice | capture: sha256:248902632e24c826982c2d999e66c2d0e67ceb4bd8582887733a02fc7f9d8e57 | quote: If your Healthchecks.io account is inactive for more than a year, we send an inactive account notification to your email address. If the account is still inactive 30 days after the notification, we close your account automatically.
  - [8] 2026-11-01: the server software is open source under the BSD 3-clause license | capture: sha256:58bc608da38a5e9e27e194fe59dae4db4259f7ca5f051f21f62c8ba1d4188832 | quote: Healthchecks is open-source, and is licensed under the BSD 3-clause license.
- sources:
  - [1] https://healthchecks.io/pricing/
  - [2] https://healthchecks.io/docs/http_api/
  - [3] https://healthchecks.io/docs/api/
  - [4] https://healthchecks.io/
  - [5] https://healthchecks.io/accounts/login/
  - [6] https://healthchecks.io/faq/
  - [7] https://healthchecks.io/privacy/
  - [8] https://healthchecks.io/docs/self_hosted/
