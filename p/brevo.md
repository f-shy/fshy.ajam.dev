# Brevo

> brevo.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/brevo/ | JSON https://fshy.ajam.dev/api/v1/entity/brevo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Brevo

- `email/brevo` | qualifies-with-caveat | evidence documented | binding request-rate | category transactional sender
- needs card no, phone unknown, ID no, institution no | verified 2026-10-30T09:26:49.193Z (live) | stale on 2026-11-30
- url https://www.brevo.com/pricing/
- free tier: 300 email sends per day with no time limit; 100,000 contacts stored | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1] | note: Every email sent from the Free plan carries the Sent with Brevo sticker; up to 2,000 unique contacts can enter active automations; one user. Once the 300 daily sends are used, no campaign can be scheduled for the next day. The Free plan's limits page names no restriction on recipients.
- per-object cap: not applicable: a send count rather than an object
- retention: unused sends do not roll over | source: [2]
- egress: not applicable: an outbound sender | metered: no | source: [1]
- identity: email | detail: Signup asks for an email and a password, or a Google or Apple sign-in, with no card; the account then verifies the email and asks for basic business information. Whether a mobile phone number with an SMS code is also required is unverified: behind a sign-up; users on the vendor's community forum report a phone number and SMS code step during registration. A sender on a free domain such as gmail.com cannot be authenticated, and the vendor states that mail from a free address is rejected or filtered to spam, so delivery needs a domain the sender controls.
- interface: rest, cli
- limits:
  - request-rate (binding): 300 sends per day, resetting daily, with no carry-over [2]
  - request-rate (binding): a campaign to more than 300 recipients delivers to 300 that day and needs a manual requeue, so the daily send counter is the campaign's limit too [2]
  - write-gated: transactional sending over SMTP or the API needs a separate activation by the vendor, requested by a support ticket from the account, before the first send; the time it takes is unverified: behind a sign-up [3]
- limits note: counts of things, not rates, so no vocabulary kind names them: 100,000 contacts stored on the free plan. The campaign entry is a rate: the same 300-a-day counter is what a campaign meets, so it stays request-rate
- binding note: 300/day. The campaign path is the trap: a 1,000-contact list takes four days.
- interface detail: the SMTP relay and the transactional API; SMTP is the documented path
- tooling: any SMTP client, or the Brevo API
- composes with: the highest card-free daily cap found: 300/day, which is three times Resend's. It is the outbound half of the inbound-plus-outbound chain and its scarce link is the day.
- reliability: once the daily limit is hit, up to 1,000 transactional emails are held in a retry queue and anything beyond that is not delivered
- notes: The help page states the campaign behaviour explicitly, which is why the 300/day figure is not the whole answer for a marketing send.
- evidence note: no message was sent, so no delivery is proved. The submission path was probed: smtp-relay.brevo.com:587 answered 250, STARTTLS completed against the system trust store, and AUTH LOGIN returned 334
- extras:
  - stale_after_days: 90
- evidence:
  - [2] 2026-10-22: 'The Free plan includes 300 email sends per day', unused sends do not roll over, and a campaign above 300 recipients needs the Requeue option on successive days
  - [4] 2026-10-22: 'Send 300 emails a day with the best free SMTP server'
  - probe:smtp://smtp-relay.brevo.com:587 2026-10-22: banner 250, EHLO advertises SIZE and 8BITMIME, STARTTLS completed against the system trust store, and AUTH LOGIN returned 334. The submission endpoint answers; no message was sent
  - [5] 2026-10-30: the registration form asks for an email and a password, or a Google or Apple sign-in, and no card | capture: sha256:bedc35b85d45d43681738cde4c72b43117fecf4e79f99f97ab88ab4fb50e3e25 | quote: Create your account. No credit card needed.
  - [6] 2026-10-30: after the first form the account verifies the email and asks for basic business information | capture: sha256:3c5192e4e2aeca6304cd39ca6348e5176ad3cbfdd2c9fa7cbf10a9c8863f59ec | quote: You'll be asked to verify your email address and provide some basic information about your business.
  - [7] 2026-10-30: users report a phone number and SMS code step during registration; a user report, not a vendor statement | capture: sha256:a98f4edd332ee21c38fb1e8d0dd629c004f7f037092c3d1cbcca54d049f79993 | quote: In the process of new account registration, the website ask the phone number to setup a two-factor authentication.
  - [8] 2026-10-30: a sender on a free domain such as gmail.com cannot be authenticated | capture: sha256:ec6f9ed0807b65d5f3d18e584de375ff3237a22a25b62d09350c4b4baa1ec7bb | quote: Note that free sender domains cannot be authenticated, so you’ll need to purchase your own domain.
  - [9] 2026-10-30: mail from a free address is rejected or filtered to spam, so the sender needs its own domain | capture: sha256:01c5435176f2f412aee54bf35d4ea30bf964188b5c508d7703d505818b765e10 | quote: Sending from a free email address (@gmail.com, @yahoo.com, @outlook.com, etc.) will cause your emails to be rejected or filtered to spam.
  - [2] 2026-10-30: the Free plan always adds the Sent with Brevo sticker; the same page gives the 2,000-contact automation cap, the single user and the scheduling rule, and lists no recipient restriction | capture: sha256:6132ddcef8072155da48c608bcc35b052d473ab446b40d8a7d6e6f328b33801f | quote: Emails sent from the Free plan always include the Sent with Brevo sticker.
  - [3] 2026-10-30: a new account cannot send transactional mail until the vendor activates the transactional platform on request | capture: sha256:a37ed440dff04247ef626ecd7ed36bb1de4347642cd9db2e0aa556993a8f20d2 | quote: Transactional email sending requires a separate activation step from Brevo. If you've never sent transactional emails from your account, contact our support team by creating a ticket from your account to request activation.
  - [1] 2026-10-30: the Free plan has no time limit and needs no card | capture: sha256:95abab98e579e97f6793282adc571780d960b8cc35c1af70f4289ae8b1bfdbf5 | quote: Free forever, no credit card needed
  - [10] 2026-10-30: the Free plan is 300 sends per day and up to 100,000 contacts | capture: sha256:739ecab960d07828b325802a7d7a83a9b90ae46c86a939d6492ab1e601a46c9d | quote: The Free plan includes 300 daily email sends and storage for up to 100,000 contacts.
  - [2] 2026-10-30: past the daily limit up to 1,000 transactional emails wait in a retry queue and the rest are not delivered | capture: sha256:6132ddcef8072155da48c608bcc35b052d473ab446b40d8a7d6e6f328b33801f | quote: once you reach your daily limit, up to 1,000 additional emails are held in a retry queue. Emails beyond this queue are not delivered.
  - [2] 2026-10-30: the Free plan is still 300 sends per day with no carry-over | capture: sha256:6132ddcef8072155da48c608bcc35b052d473ab446b40d8a7d6e6f328b33801f | quote: The Free plan includes 300 email sends per day. The daily limit resets every day, and unused emails do not roll over to the next day.
- sources:
  - [1] https://www.brevo.com/pricing/
  - [2] https://help.brevo.com/hc/en-us/articles/208580669-FAQs-What-are-the-limits-of-the-Free-plan
  - [3] https://help.brevo.com/hc/en-us/articles/115000188150-Troubleshooting-Issues-with-Brevo-SMTP
  - [4] https://www.brevo.com/free-smtp-server/
  - [5] https://onboarding.brevo.com/account/register
  - [6] https://www.brevo.com/blog/wp-mail-smtp/
  - [7] https://community.brevo.com/t/sms-does-not-arrive-upon-registration/567
  - [8] https://help.brevo.com/hc/en-us/articles/208836149-Create-a-new-sender-From-name-and-From-email
  - [9] https://help.brevo.com/hc/en-us/articles/14925263522578-Comply-with-Gmail-Yahoo-and-Microsoft-s-requirements-for-email-senders
  - [10] https://help.brevo.com/hc/en-us/articles/208589409-About-Brevo-s-pricing-plans
