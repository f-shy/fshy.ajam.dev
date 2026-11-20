# Mailazy

> mailazy.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mailazy/ | JSON https://fshy.ajam.dev/api/v1/entity/mailazy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mailazy

- `email/mailazy` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted newsletter and automation sender, bring-your-own-SMTP | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T01:46:40.588Z (live) | stale on 2026-12-20
- url https://mailazy.com/pricing/
- free tier: Free: $0/month, Free forever, 1 team member, 1,000 contacts, 5,000 emails a month, Newsletters and 1 automation, Docs and community help | unit: mixed | metered on: request-count | read on: 2026-11-19 | source: [1] | note: The headline is two quotas in different units: 5,000 emails a month and 1,000 contacts. Emails are counted per send and contacts per stored address. The schema has no emails unit, so the unit is mixed.
- per-object cap: not applicable: an outbound email sender with no stated per-object storage cap | source: [2]
- retention: Account and customer data are kept while the account is active; after the account is closed the data is deleted or anonymized within a reasonable period, except records the law requires to be kept, such as billing | source: [3] | note: Logs can be filtered over the last 24 hours, 7 days, 30 days or a custom range; no fixed log retention window is stated.
- egress: Contacts are exportable by CSV and readable through GET /contacts/export; send logs are readable through GET /logs. No per-GB egress charge or quota is stated. | metered: no | source: [2]
- identity: email | detail: The live sign-in at portal.mailazy.com asks only for an email address and continues with a link: 'Enter your email to continue to Mailazy.' No card or phone is asked at that step. Further signup fields are unverified: the account was not created.
- interface: rest, browser
- limits:
  - volume-quota (binding): 5,000 emails a month on Free; at the limit all sending stops and does not resume until usage resets on the billing day or the plan is upgraded [4]
  - volume-quota (binding): 1,000 contacts on Free; at the limit new contacts are not added [4]
  - write-gated: Behavioral email rules and AI writing are on Pro and up; on Free their API paths answer 402 and one automation is allowed [4]
- binding note: The 5,000 emails a month cap stops all sending until the billing-day reset, before the 1,000-contact cap or the Pro-gated features bind for a sender.
- interface detail: REST HTTP API under https://api.mailazy.com/api/v1 using X-API-Key and X-API-Secret headers; dashboard at portal.mailazy.com
- endpoint: part of interface detail
- tooling: curl or any HTTP client with an API key pair; the dashboard for lists, templates and schedules
- composes with: A bring-your-own-SMTP sender: the Free plan holds contacts, newsletters and one automation, while delivery goes through a separate SMTP provider the reader connects and pays directly, so the SMTP provider's own sending limits also apply.
- reliability: Mailazy does not run mail servers; email leaves through the SMTP provider the reader connects. Logs store one row per delivery attempt, retries appear as separate rows, and test sends are not logged.
- notes: A hosted send manager with a real free tier of 5,000 emails and 1,000 contacts per month and a REST API. The caveat is structural: the reader must connect and pay a separate SMTP provider for delivery, and the free caps and Pro-gated features bind early.
- evidence note: Free tier, limits, API and sign-in step are stated on first-party pages and quoted; delivery and the post-email signup fields remain unverified.
- evidence:
  - [1] 2026-11-19: Free plan allows 1,000 contacts and 5,000 emails a month | capture: sha256:f0b927967e42aa33d68a025a6eb0879cd7bf7d98a5bd24e737d588e2c01dd07f | quote: Free covers 1,000 contacts and 5,000 emails a month, Pro 25,000 and 100,000.
  - [1] 2026-11-19: delivery goes through an SMTP provider the reader supplies and pays directly | capture: sha256:f0b927967e42aa33d68a025a6eb0879cd7bf7d98a5bd24e737d588e2c01dd07f | quote: Your own SMTP provider, such as Amazon SES, SendGrid, Mailgun, Postmark or Cloudflare. You add its credentials in Settings. You pay that provider directly, at their rates.
  - [1] 2026-11-19: Free plan allows one automation and one team member | capture: sha256:f0b927967e42aa33d68a025a6eb0879cd7bf7d98a5bd24e737d588e2c01dd07f | quote: Free is for newsletters, with one automation and one team member.
  - [5] 2026-11-19: the plan meters Mailazy sends while the reader's SMTP provider handles delivery | capture: sha256:a71632a082ceed727e7de8bd7e0f4df08f3ef7a9f8963975622b6656c7fc3619 | quote: Emails go through your own sending service (SMTP). You pay that provider for delivery, at their rates; the plan sets how many Mailazy sends for you each month.
  - [5] 2026-11-19: monthly email usage resets on the billing day | capture: sha256:a71632a082ceed727e7de8bd7e0f4df08f3ef7a9f8963975622b6656c7fc3619 | quote: Monthly counts (emails, AI credits, AI assistant calls) start again on your billing day
  - [4] 2026-11-19: all sending stops at the monthly email cap and does not resume automatically | capture: sha256:2a5d0253c1bb43c5a1cb1e6badac1709b9862022f626debbdcef8d2cda972ae0 | quote: The monthly email limit stops sending. Your API calls are still accepted, but once the month's emails are used, every email fails in Logs with `Monthly email limit of your plan reached` until usage resets or an upgrade.
  - [4] 2026-11-19: plan-limit and feature errors answer 402 and only clear on upgrade or reset | capture: sha256:2a5d0253c1bb43c5a1cb1e6badac1709b9862022f626debbdcef8d2cda972ae0 | quote: Don't retry a 402. It changes only when someone upgrades, or, for monthly limits, when usage resets on the billing day.
  - [6] 2026-11-19: API calls beyond the plan limits are refused with 402 | capture: sha256:6662f7933e1571f2c3a09e5e7c5edb7cd063c8e61e72cb9d0038f1c9f8350333 | quote: 402 means the plan stops it. Limits belong to the organization's [plan](https://mailazy.com/docs/guide/plans-and-billing).
  - [7] 2026-11-19: the live sign-in asks for an email address only, with no card or phone at that step | capture: sha256:85d7f95caa9c1ab6135a1846c3ceb4ea38a28dc46b3944f979c1e4ac8a8643b0 | quote: Enter your email to continue to Mailazy.
  - [2] 2026-11-19: a REST API is available under a documented base URL | capture: sha256:7dfb905271ddb1f6523df7b0f1403c8079ca7c1d28fbba6d5da538f7c479db66 | quote: The HTTP API your app uses to talk to Mailazy. Every endpoint lives under `https://api.mailazy.com/api/v1`.
  - [8] 2026-11-19: delivery requires an external SMTP provider | capture: sha256:ecbf6a4c6869309888b52c35a9b5e97015e3d659675052c6f70bbe5001ba4ec7 | quote: Mailazy does not run mail servers. It hands your email to one you already pay for — Amazon SES, SendGrid, Postmark, Mailgun, your own relay.
  - [9] 2026-11-19: logs are readable and filterable by time window | capture: sha256:c808aa3d8c3b4e26633f7a23fe0d0e539ffa62b159b3577b63739d9edeece0ee | quote: Filter by contact, by result, or by time (last 24 hours, 7 days, 30 days, or a custom range), or page through.
  - [3] 2026-11-19: customer data is kept while the account is active and cleared after closure with a billing exception | capture: sha256:927fc6a81214e287bc18ede329fb48a18d92a5afbbce1db04caa4ca6d7348122 | quote: After you close your account, we delete or anonymize your data within a reasonable period, except records the law makes us keep, such as billing.
- sources:
  - [1] https://mailazy.com/pricing/
  - [2] https://mailazy.com/docs/api/
  - [3] https://mailazy.com/dpa
  - [4] https://mailazy.com/docs/developer/plan-limits
  - [5] https://mailazy.com/docs/guide/plans-and-billing
  - [6] https://mailazy.com/docs/developer/getting-started
  - [7] https://portal.mailazy.com/
  - [8] https://mailazy.com/docs/guide/account-setup
  - [9] https://mailazy.com/docs/guide/logs-opens-and-clicks
