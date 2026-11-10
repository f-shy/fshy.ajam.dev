# MailerLite

> mailerlite.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mailerlite/ | JSON https://fshy.ajam.dev/api/v1/entity/mailerlite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MailerLite

- `email/mailerlite` | qualifies-with-caveat | evidence documented | binding request-rate | category marketing sender
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:33:30.050Z (live) | stale on 2026-12-05
- url https://www.mailerlite.com/pricing
- free tier: 2,500 emails/month, 250 subscribers, 2 user seats | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not stated | source: [1]
- egress: not applicable: an outbound sender. On Free, sending runs from the web app; the API and MCP server cannot send | metered: no | source: [1]
- identity: email | detail: company or organization, name, email address and a password at signup, then email verification
- interface: rest
- limits:
  - request-rate (binding): 2,500 emails per month [1]
  - write-gated: API and MCP sending is available on paid plans only; on Free the API is read-limited [1]
  - write-gated: a new account completes its profile and requests approval before it is validated [2]
- limits note: counts of things, not rates, so no vocabulary kind names them: a 250-active-subscriber ceiling, past which campaigns and automations are locked, and 2 user seats
- binding note: 2,500 sends a month binds first for a sender; the 250-active-subscriber ceiling, which locks sending when passed, is a count no limits kind names
- interface detail: the MailerLite API, which on the free plan is read-limited and cannot send
- tooling: the MailerLite web app sends campaigns and automations on Free; the MailerLite API and MCP server are limited on Free and cannot send, so programmatic sending needs a driver for the web app or a paid plan
- composes with: on Free it composes only through the web app, since the API and MCP server cannot send; a paid plan opens API sending
- reliability: the free plan adds MailerLite branding to messages
- notes: API and MCP sending is a paid feature; the Free plan sends campaigns and automations from the web app, so the 2,500 monthly emails are reachable by driving the web app.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: 'Email sending via the API and MCP server is available on paid plans. On Free, API and MCP access is limited and doesn't include sending'
  - [1] 2026-10-30: the Free plan sends 2,500 emails a month | capture: sha256:ea4036b4dfffbeb546cdf4f396fd5e4ef31e796f8d5ab7fd8b6341a48095db9b | quote: Free includes 2,500 emails per month.
  - [1] 2026-10-30: on Free the API and MCP server cannot send | capture: sha256:ea4036b4dfffbeb546cdf4f396fd5e4ef31e796f8d5ab7fd8b6341a48095db9b | quote: Email sending via the API and MCP server is available on paid plans. On Free, API and MCP access is limited and doesn't include sending.
  - [1] 2026-10-30: API sending is a paid-plan feature | capture: sha256:ea4036b4dfffbeb546cdf4f396fd5e4ef31e796f8d5ab7fd8b6341a48095db9b | quote: Email sending via the API and MCP server is available on paid plans. On Free, API and MCP access is limited and doesn't include sending.
  - [1] 2026-10-30: on Free the API cannot send, so the allowance is reached through the web app | capture: sha256:ea4036b4dfffbeb546cdf4f396fd5e4ef31e796f8d5ab7fd8b6341a48095db9b | quote: Email sending via the API and MCP server is available on paid plans. On Free, API and MCP access is limited and doesn't include sending.
  - [1] 2026-10-30: the Free plan is capped at 2,500 emails a month | capture: sha256:ea4036b4dfffbeb546cdf4f396fd5e4ef31e796f8d5ab7fd8b6341a48095db9b | quote: Free includes 2,500 emails per month.
  - [1] 2026-10-30: sending locks when active subscribers pass 250 | capture: sha256:ea4036b4dfffbeb546cdf4f396fd5e4ef31e796f8d5ab7fd8b6341a48095db9b | quote: For free accounts, when the number of active subscribers exceeds the 250 active subscriber limit, sendings will be locked (campaigns + automation).
  - [2] 2026-10-30: a new account is validated only after profile completion and an approval request | capture: sha256:9580e699f17664e1eaf0ef0556f6795a1341e247e81fa1d58acf7c9602f076e8 | quote: After creating a MailerLite account, you’ll need to complete two steps to validate your account: (i) Complete your profile; (ii) Request approval.
  - [1] 2026-10-30: sending locks past 250 active subscribers | capture: sha256:ea4036b4dfffbeb546cdf4f396fd5e4ef31e796f8d5ab7fd8b6341a48095db9b | quote: For free accounts, when the number of active subscribers exceeds the 250 active subscriber limit, sendings will be locked (campaigns + automation).
  - [3] 2026-10-30: signup asks for company or organization, name, email address and password | capture: sha256:4312e1d503b146b35279f7433508f9faffc434c2bca67f434f5bf59d05229037 | quote: Fill out the information requested, such as Company/Organization, Name, Email address, and create a Password.
  - [1] 2026-10-30: the Free plan signup asks for no card | capture: sha256:ea4036b4dfffbeb546cdf4f396fd5e4ef31e796f8d5ab7fd8b6341a48095db9b | quote: No credit card required.
  - [1] 2026-10-30: the Free plan gives 250 subscribers, 2 seats and 2,500 emails a month | capture: sha256:ea4036b4dfffbeb546cdf4f396fd5e4ef31e796f8d5ab7fd8b6341a48095db9b | quote: You get up to 250 subscribers, 2 user seats, and 2,500 monthly emails, plus campaigns, automations, a website, a landing page, and signup forms
  - [1] 2026-11-04: the Free plan is 2,500 emails a month, unchanged | capture: sha256:ea4036b4dfffbeb546cdf4f396fd5e4ef31e796f8d5ab7fd8b6341a48095db9b | quote: Free includes 2,500 emails per month.
- sources:
  - [1] https://www.mailerlite.com/pricing
  - [2] https://www.mailerlite.com/legal/terms-of-service
  - [3] https://www.mailerlite.com/help/how-to-get-approved
