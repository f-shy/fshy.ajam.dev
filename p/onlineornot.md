# OnlineOrNot

> onlineornot.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/onlineornot/ | JSON https://fshy.ajam.dev/api/v1/entity/onlineornot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OnlineOrNot

- `dev-services/onlineornot` | qualifies-with-caveat | evidence documented | binding volume-quota | category uptime and browser check monitoring with status pages | tier Hobby
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:32.368Z (live) | stale on 2026-12-20
- url https://onlineornot.com/pricing
- free tier: Hobby plan, free: 3 uptime monitors at a 3-minute check interval, 1,000 browser check runs a month, up to 2 users, 1 limited status page with 100 email subscribers, 14 days of data retention, email, Slack, Discord and Telegram alerts and authenticated API and MCP access; no SMS alerts and no webhooks | unit: mixed | metered on: request-count | read on: 2026-11-01 | source: [1] | note: The allowance mixes a count of monitors with a monthly count of browser check runs, so no single unit of the vocabulary fits. The Pro plan starts at USD 25 a month with 35 monitors, 3,000 browser check runs and a 30-second check interval; its button and the Hobby button both read Start trial, and whether Hobby has an end date is unverified: not stated on the pricing page.
- per-object cap: not applicable: a monitor checks a target; nothing is stored per object
- retention: 14 days of data retention on Hobby, against 12 months on Pro | days: 14 | source: [1]
- egress: not applicable: an outbound checker; monitor data is read back through the authenticated API, which the pricing page lists as available on every plan | metered: no | source: [1]
- identity: email | detail: Registration asks for an e-mail address or a Google or GitHub sign-in: 'You can sign up using: - Email (we'll send you a magic link - no password needed) - Google - GitHub'. No card and no phone number are asked for at sign-up, and a first-party comparison page states no credit card is required. The e-mail is verified by a magic link: 'After entering your email, check your inbox for a magic link'. Any phone or card step that appears only after registration is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 3 uptime monitors and 1,000 browser check runs per month on Hobby [1]
  - request-rate: 3-minute check interval on Hobby [1]
  - retention-clamped: 14 days of data retention on Hobby [1]
- limits note: Hobby has up to 2 users, no SMS alerts and no webhooks.
- binding note: The 3-monitor cap is reached first by any app with more than a few endpoints.
- interface detail: The pricing page lists authenticated API and MCP access as available on Hobby, Pro and Enterprise; the API reference page was not found at the address tried, so its host, authentication scheme and limits are unverified.
- tooling: the web app, the authenticated API and an MCP server
- composes with: External uptime and browser checks on up to 3 endpoints of free-hosted services every 3 minutes, with Slack, Discord or Telegram alerts and a status page.
- reliability: no throttle, ban or data loss is stated on the pages read beyond the 14-day data retention
- notes: The pricing page lists the Hobby plan under a Start trial button, the same label as the Pro plan, with no end date for Hobby stated.
- evidence note: Plan limits are quoted from the first-party pricing page. No account was opened, so the sign-up fields, the card term and the API host are unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the Hobby plan is free with up to 2 users, a 3-minute check interval and a limited status page | capture: sha256:24aa61bbacb35aabbaea29cbc19853868a602a394d59235b7a160e3ad78d8d73 | quote: ## Hobby Perfect for home labs and personal projects. Free - Up to 2 users - 3 minute check interval - Limited status page - Basic alerting
  - [1] 2026-11-01: Hobby has 3 uptime monitors against 35 on Pro | capture: sha256:24aa61bbacb35aabbaea29cbc19853868a602a394d59235b7a160e3ad78d8d73 | quote: Uptime monitors 3 35 included +$10 per 25 additional
  - [1] 2026-11-01: Hobby has 1,000 browser check runs a month against 3,000 on Pro | capture: sha256:24aa61bbacb35aabbaea29cbc19853868a602a394d59235b7a160e3ad78d8d73 | quote: Browser check runs 1,000/mo 3,000/mo +$4 per 1k additional
  - [1] 2026-11-01: Hobby keeps data 14 days against 12 months on Pro | capture: sha256:24aa61bbacb35aabbaea29cbc19853868a602a394d59235b7a160e3ad78d8d73 | quote: Data retention 14 days 12 months Custom
  - [1] 2026-11-01: authenticated API and MCP access is available on Hobby | capture: sha256:24aa61bbacb35aabbaea29cbc19853868a602a394d59235b7a160e3ad78d8d73 | quote: Authenticated API and MCP access Hobby: Yes Pro: Yes Enterprise: Yes
  - [1] 2026-11-01: Hobby has Slack, Discord and Telegram alerts and no SMS alerts | capture: sha256:24aa61bbacb35aabbaea29cbc19853868a602a394d59235b7a160e3ad78d8d73 | quote: Slack, Discord, and Telegram Hobby: Yes Pro: Yes Enterprise: Yes #### SMS alerts Hobby: No
  - [1] 2026-11-01: Hobby has no webhooks | capture: sha256:24aa61bbacb35aabbaea29cbc19853868a602a394d59235b7a160e3ad78d8d73 | quote: SMS alerts Hobby: No Pro: Yes Enterprise: Yes #### Webhooks Hobby: No
  - [1] 2026-11-01: Hobby has 1 included status page | capture: sha256:24aa61bbacb35aabbaea29cbc19853868a602a394d59235b7a160e3ad78d8d73 | quote: Included status pages 1 1 +$24/page additional
  - [1] 2026-11-01: Hobby status pages have 100 email subscribers | capture: sha256:24aa61bbacb35aabbaea29cbc19853868a602a394d59235b7a160e3ad78d8d73 | quote: Email subscribers 100 Unlimited Unlimited
  - [1] 2026-11-01: the Pro plan starts at USD 25 a month with 35 monitors and a 30-second check interval | capture: sha256:24aa61bbacb35aabbaea29cbc19853868a602a394d59235b7a160e3ad78d8d73 | quote: from $25/mo - Unlimited users - 30 second check interval - 35 monitors included
  - [2] 2026-11-01: the get-started page creates a monitoring workspace with an agreement to the terms | capture: sha256:d01d52c3d1e149e5724eab28226ed9b38d8a11fdf9dbdc288faea1c719a85dbf | quote: # Create your monitoring workspace
  - [3] 2026-11-19: the sign-up asks for an email (magic link), Google or GitHub, with no card field and no phone field | capture: sha256:25c8a1ea450e0a1e41f52f706a97719f5bb53653f5337a11fac30dad1287df9e | quote: You can sign up using: - Email (we'll send you a magic link - no password needed) - Google - GitHub
  - [3] 2026-11-19: the sign-up form asks for an email address or a social sign-in, so the identity kind is email | capture: sha256:25c8a1ea450e0a1e41f52f706a97719f5bb53653f5337a11fac30dad1287df9e | quote: You can sign up using: - Email (we'll send you a magic link - no password needed) - Google - GitHub
  - [4] 2026-11-19: the first-party page states no credit card is required to sign up | capture: sha256:baaeb5966ef521e478369c759aa37d3361f52c805d56bed4074a31666e5a73ba | quote: Free 14-day trial · No credit card required
  - [3] 2026-11-19: the email given at sign-up is verified by a magic link | capture: sha256:25c8a1ea450e0a1e41f52f706a97719f5bb53653f5337a11fac30dad1287df9e | quote: After entering your email, check your inbox for a magic link
- sources:
  - [1] https://onlineornot.com/pricing
  - [2] https://onlineornot.com/get-started
  - [3] https://onlineornot.com/docs/tutorials/getting-started
  - [4] https://onlineornot.com/alternatives/onlineornot-vs-better-stack
