# Postmark

> postmark.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/postmark/ | JSON https://fshy.ajam.dev/api/v1/entity/postmark.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Postmark

- `email/postmark` | fails-quota | evidence documented | binding request-rate | category transactional sender
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:33:30.049Z (live) | stale on 2026-12-05
- url https://www.postmark.com/pricing
- free tier: 100 emails/month on the free Developer tier, which does not expire | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: 45 days of activity retention | days: 45 | source: [1]
- egress: not applicable: an outbound sender | metered: no | source: [1]
- identity: email | detail: an account with an email address; no credit card for the free Developer plan
- interface: rest
- limits:
  - request-rate (binding): 100 emails per month with no daily allowance beyond it [1]
  - write-gated: until Postmark approves a new account, it sends only to addresses on domains added to the account and verified; review takes under 24 hours on weekdays [2]
- limits note: no daily allowance exists: 100 emails per month is the whole month, which is 3.3 a day averaged. A verified sender signature or domain is required and a card is not
- interface detail: https://api.postmarkapp.com/email; an SMTP relay at smtp.postmarkapp.com for transactional messages and smtp-broadcasts.postmarkapp.com for broadcast messages, on ports 25, 2525 and 587 with STARTTLS
- tooling: curl, any HTTP client, any SMTP client
- composes with: composes with a domain and with nothing else at this volume.
- reliability: no overage on the free tier
- notes: There is no burst room at all, which distinguishes it from every 100/day product here.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: 'Test your integration with 100 emails/month'
  - probe:smtp://smtp.postmarkapp.com:587 2026-10-22: banner 250, EHLO advertises SIZE and 8BITMIME, STARTTLS completed, and AUTH LOGIN returned 334
  - [1] 2026-10-30: message content history is kept 45 days by default | capture: sha256:4bb4051eb4976bc6ad36bdd799d13e17f7f175eef8251b8ba20e573d817747dc | quote: 45 days worth of full content history by default to help you troubleshoot (customizable from 7 to 365 days if needed).
  - [1] 2026-10-30: the free plan needs no card | capture: sha256:4bb4051eb4976bc6ad36bdd799d13e17f7f175eef8251b8ba20e573d817747dc | quote: Try Postmark Free No Credit Card Required
  - [2] 2026-10-30: a new account is limited to its own verified domains until it is approved | capture: sha256:93eefbc8f9e68af9ea8820060059d2e8fa5525324052e52181888be22969a197 | quote: Until your account is approved, you won’t be able to send to any email address outside the domains you’ve added to your account and verified.
  - [1] 2026-10-30: the free plan allows no overage | capture: sha256:4bb4051eb4976bc6ad36bdd799d13e17f7f175eef8251b8ba20e573d817747dc | quote: No overages allowed in this plan.
  - probe:smtp.postmarkapp.com:587 2026-10-31: the Postmark SMTP relay answers on port 587 with a 220 ESMTP banner | capture: sha256:21ba8b1bab525e6e89e778a2ad76f72cca8dfb34d1db49abb91165c33c3ddcd9 | quote: .smtpservice.postmarkapp.com ESMTP
  - [1] 2026-10-30: the free Developer plan gives 100 emails a month and does not expire | capture: sha256:4bb4051eb4976bc6ad36bdd799d13e17f7f175eef8251b8ba20e573d817747dc | quote: Everyone starts on our free Developer plan, which includes 100 emails every month. And it never expires or runs out.
  - [3] 2026-11-02: the SMTP relay hosts are smtp.postmarkapp.com for transactional and smtp-broadcasts.postmarkapp.com for broadcast messages | capture: sha256:455edad6cdb9b3d582a29c21177d087726331dab89e1dcefba4a5b61c4e04b7f | quote: After enabling access, you will be able to connect to smtp.postmarkapp.com (for transactional messages) or smtp-broadcasts.postmarkapp.com (for broadcast messages).
  - [3] 2026-11-02: the SMTP relay is reached on ports 25, 2525 or 587 | capture: sha256:455edad6cdb9b3d582a29c21177d087726331dab89e1dcefba4a5b61c4e04b7f | quote: Ports - 25, 2525, or 587
  - [3] 2026-11-02: TLS on the SMTP relay is available through STARTTLS | capture: sha256:455edad6cdb9b3d582a29c21177d087726331dab89e1dcefba4a5b61c4e04b7f | quote: TLS is available via the STARTTLS SMTP extension.
  - [3] 2026-11-02: an SMTP client connects to the Postmark relay on ports 25, 2525 or 587 | capture: sha256:455edad6cdb9b3d582a29c21177d087726331dab89e1dcefba4a5b61c4e04b7f | quote: Ports - 25, 2525, or 587
  - [1] 2026-11-02: the pricing page captured on 2026-11-02 states the free Developer plan of 100 emails a month with no expiry | capture: sha256:9fd76073c28fbbbfb6a6d8375a3f603a4b3519fefd9c91105430a290f51994e5 | quote: Everyone starts on our free Developer plan, which includes 100 emails every month. And it never expires or runs out.
  - [1] 2026-11-02: the free plan needs no credit card | capture: sha256:9fd76073c28fbbbfb6a6d8375a3f603a4b3519fefd9c91105430a290f51994e5 | quote: Try Postmark Free No Credit Card Required
  - [1] 2026-11-02: the pricing page was captured on 2026-11-02 and still states the free Developer plan | capture: sha256:9fd76073c28fbbbfb6a6d8375a3f603a4b3519fefd9c91105430a290f51994e5 | quote: Everyone starts on our free Developer plan, which includes 100 emails every month. And it never expires or runs out.
  - [1] 2026-11-02: the pricing page still offers the free plan with no credit card | capture: sha256:9fd76073c28fbbbfb6a6d8375a3f603a4b3519fefd9c91105430a290f51994e5 | quote: Try Postmark Free No Credit Card Required
  - [1] 2026-11-04: the free Developer plan is 100 emails a month with no expiry, unchanged | capture: sha256:4bb4051eb4976bc6ad36bdd799d13e17f7f175eef8251b8ba20e573d817747dc | quote: Everyone starts on our free Developer plan, which includes 100 emails every month. And it never expires or runs out.
- sources:
  - [1] https://www.postmark.com/pricing
  - [2] https://postmarkapp.com/support/article/1084-how-does-the-account-approval-process-work
  - [3] https://postmarkapp.com/developer/user-guide/send-email-with-smtp
