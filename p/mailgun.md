# Mailgun

> mailgun.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mailgun/ | JSON https://fshy.ajam.dev/api/v1/entity/mailgun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mailgun

- `email/mailgun` | qualifies-with-caveat | evidence documented | binding request-rate | category transactional sender
- needs card no, phone yes, ID no, institution no | verified 2026-10-30T09:26:49.193Z (live) | stale on 2026-11-30
- url https://www.mailgun.com/pricing/
- free tier: 100 messages/day, 1 custom domain, 1 inbound route, 2 API keys, 1-day log retention | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1] | note: Without a card on file the Free plan sends from the sandbox domain only to authorized recipients: up to 5 addresses, each verified when its owner clicks an invitation link. A card on file allows custom domains, which send to any recipient; a custom domain must be verified through DNS before it sends.
- per-object cap: not applicable
- retention: logs and the Events API keep 1 day | source: [1]
- egress: not applicable: an outbound sender | metered: no | source: [2]
- identity: card | detail: Signup asks for a work email, a full name and a company; every account is then activated by an email link and a mobile phone number verified by an SMS one-time password, and VoIP, virtual and landline numbers are refused. No card is needed to open a Free plan account, but without a card on file it sends only to authorized recipients; a card on file unlocks custom domains, which send to any recipient.
- interface: rest
- limits:
  - request-rate (binding): 100 messages per day [1]
- limits note: counts of things, not rates, so no vocabulary kind names them: 1 custom domain and 1 inbound route per account
- interface detail: https://api.mailgun.net/v3/DOMAIN/messages
- tooling: curl, any HTTP client
- composes with: 100/day out with one domain and one inbound route, so it composes with one domain and with no fan-out.
- reliability: phone verification refuses VoIP, virtual and landline numbers, and repeated code requests can place a temporary hold on the account
- notes: One domain and one inbound route cap the shape rather than the volume.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: '100 messages per day', 1 custom domain, 1 day of data retention, 1 inbound route and 2 API keys; the page returned 403 to the reader but the body extracted
  - [3] 2026-10-30: a Free plan account without a card on file sends only to authorized recipients, so the stated free tier with a custom domain needs a card on file | capture: sha256:a61d8f5e7973d82fdeb914770c587ba67b08ee54076920d2335297a52202d9d4 | quote: If you're on the Free plan without credit card information present or using your sandbox domain for testing, you're restricted to sending just to Authorized Recipients.
  - [4] 2026-10-30: every account is activated by verifying an email address and a phone number by SMS | capture: sha256:3fbb0789add7e163ce7c6a40b0b4ee4ec51db67e18cba13526d910fe279a2a75 | quote: This involves verifying both your email address and a phone number.
  - [4] 2026-10-30: the SMS verification needs a standard mobile number; VoIP, virtual and landline numbers are refused | capture: sha256:3fbb0789add7e163ce7c6a40b0b4ee4ec51db67e18cba13526d910fe279a2a75 | quote: Voice over IP (VoIP), virtual numbers, and landlines cannot be used.
  - [5] 2026-10-30: the free signup form asks for Work Email, Full Name and Company and opens an account without a card, limited to 100 messages per day | capture: sha256:27374037a9d01cfcbd9bf96a06cc50e2728db335d7f8cd0a1008bbafc4535a64 | quote: Free accounts without a credit card are limited to 100 messages per day.
  - [3] 2026-10-30: adding a card allows custom domains, and a custom domain sends to any recipient | capture: sha256:a61d8f5e7973d82fdeb914770c587ba67b08ee54076920d2335297a52202d9d4 | quote: From custom domains, you can send to whomever you like!
  - [3] 2026-10-30: a card-free Free plan account reaches at most 5 authorized recipients, each verified by an activation link | capture: sha256:a61d8f5e7973d82fdeb914770c587ba67b08ee54076920d2335297a52202d9d4 | quote: Up to 5 Authorized Recipients can be added.
  - [6] 2026-10-30: the sandbox domain every account receives sends only to authorized recipients | capture: sha256:571abd44e434b6241764daaf94c4d7b48843af9b76a3460d2654660e36460204 | quote: Sandbox domains can only send to authorized recipients.
  - [7] 2026-10-30: sending to any recipient needs a custom domain the sender controls, verified through DNS | capture: sha256:5a85fdedd9d74349f5540939e74407c8e0f57f517f337ba8c1161b0d49b9180e | quote: To use Mailgun for production, you must create and verify your custom domain(s) with Mailgun to ensure proper authentication and deliverability.
  - [4] 2026-10-30: repeated SMS code requests can place a temporary hold on the account | capture: sha256:3fbb0789add7e163ce7c6a40b0b4ee4ec51db67e18cba13526d910fe279a2a75 | quote: If you've tried multiple times, a temporary hold may be placed on your account.
  - [1] 2026-10-30: the Free plan keeps logs and Events API data for 1 day | capture: sha256:b0043f6547d5a26c1ba38432b4c155e5fc5bb51a7699216a70241ac44a7c9765 | quote: 1 day of data retention for Logs and the Events API
  - [8] 2026-10-30: messages are sent with a POST to api.mailgun.net/v3/DOMAIN/messages | capture: sha256:15ab0f046eb692dc94b8e20ea5f1b1c720413d1987205b5243ab347e9c3befc6 | quote: https://api.mailgun.net/v3/YOUR_SANDBOX_DOMAIN/messages
  - [2] 2026-10-30: the Free plan is still 100 emails per day with 1 custom sending domain, 2 API keys, 1 day log retention and 1 inbound route | capture: sha256:67f330109776d29835b27a7ffcfe9932c7855e9e97119778decd86a7850f7f37 | quote: 100 emails per day
- sources:
  - [1] https://help.mailgun.com/hc/en-us/articles/203068914-What-does-the-Free-plan-offer
  - [2] https://www.mailgun.com/pricing/
  - [3] https://help.mailgun.com/hc/en-us/articles/217531258-Authorized-Recipients
  - [4] https://help.mailgun.com/hc/en-us/articles/37182933150491-Account-Activation
  - [5] https://signup.mailgun.com/new/signup?plan_name=dev_free&currency=USD
  - [6] https://documentation.mailgun.com/docs/mailgun/user-manual/domains/domains-sandbox
  - [7] https://documentation.mailgun.com/docs/mailgun/user-manual/domains/domains-custom
  - [8] https://documentation.mailgun.com/docs/mailgun/quickstart
