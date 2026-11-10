# SMTP2GO

> smtp2go.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/smtp2go/ | JSON https://fshy.ajam.dev/api/v1/entity/smtp2go.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SMTP2GO

- `email/smtp2go` | qualifies-with-caveat | evidence documented | binding request-rate | category transactional sender and SMTP relay
- needs card no, phone yes, ID no, institution no | verified 2026-10-30T09:26:49.192Z (live) | stale on 2026-11-30
- url https://www.smtp2go.com/pricing/
- free tier: 1,000 emails/month, 200/day, and 25/hour until a sender domain is verified | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1] | note: Sends above the daily limit are queued and released as the daily quota allows; past 1,000 in a month further sends are rejected. Up to 5 sender domains or single sender emails can be verified, and while no sender domain is verified the account is held to 25 per hour. A send from an unverified sender is rejected and still counts toward the monthly quota. Reporting covers the past 5 days, and support is ticket-only after 14 days. The free plan's page names no restriction on recipients.
- per-object cap: not applicable
- retention: 5 days of reporting on the free plan, against 30 on paid | source: [2]
- egress: not applicable: an outbound sender | metered: no | source: [2]
- identity: any-phone | detail: The free-plan signup asks for a work email at a private domain (addresses at public domains such as Gmail and Yahoo are refused), a full name, a company, a password and a contact phone number verified by a 5 digit SMS code; no card. Sending needs a verified sender domain or a verified single sender email, and a Gmail address cannot be verified as a single sender, so in practice the account needs a domain the sender controls.
- interface: rest, cli
- limits:
  - request-rate (binding): 200 emails per day [1]
  - request-rate (binding): 25 per hour while no sender domain is verified [1]
  - request-rate (binding): 1,000 emails per month [1]
- binding note: 25/hour is 600/day if sustained and is the first ceiling a new signup meets, before the 200/day or the 1,000/month.
- interface detail: SMTP and the SMTP2GO API
- tooling: any SMTP client
- composes with: a 200/day relay with an hourly floor, so it composes with a sender that bursts rather than one that schedules.
- reliability: new paid accounts are held at 1,000/day during a one-time review
- notes: Three stacked caps on one product, and the hourly one is on the developer page but not on the pricing table.
- evidence note: no message was sent, so no delivery is proved. The submission path was probed: mail.smtp2go.com:2525 answered 250, STARTTLS completed, and AUTH LOGIN returned 334
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: 'The free plan allows 1,000 emails per month and has a limit of 200 emails per day (a 25-per-hour limitation also applies if no sender domains are verified)'
  - [2] 2026-10-22: 'Try SMTP2GO free for as long as you like' and 'over 1,000 emails/month' for paid
  - probe:smtp://mail.smtp2go.com:2525 2026-10-22: banner 250 on port 2525, EHLO advertises SIZE and 8BITMIME, STARTTLS completed, and AUTH LOGIN returned 334. The submission endpoint answers; no message was sent
  - [2] 2026-10-30: the free-account signup form asks for a contact phone number and verifies it with an SMS code | capture: sha256:ff3eb98627168feecf66bd3d54bd2c82d2ee0d7e5f423b5e105523faafbf33ab | quote: We'll send you a 5 digit code via SMS to verify your account.
  - [2] 2026-10-30: the free-account signup refuses an email at a public domain; the same form asks for full name, company, password and a contact phone number with an SMS code | capture: sha256:ff3eb98627168feecf66bd3d54bd2c82d2ee0d7e5f423b5e105523faafbf33ab | quote: Sorry, we don’t allow email addresses at public domains such as Gmail and Yahoo.
  - [3] 2026-10-30: the free plan is opened without a credit card | capture: sha256:948071dde3f95bc7fc158b04e8a69e8ea997bec26dac6647deba14511bb3bc5a | quote: Start free (1,000 emails/month, no credit card)
  - [4] 2026-10-30: an account needs an address at a domain of its own; shared domains such as Gmail, Outlook and Yahoo are not accepted | capture: sha256:66fb8ee707b2e739e920ecaa9b29fe8350e253c771cbdcf0c5aa71c8fff6cbd0 | quote: If you do not have a domain, you will need to purchase one to use with SMTP2GO
  - [4] 2026-10-30: sending is authorised only from a verified sender domain or a verified single sender email | capture: sha256:66fb8ee707b2e739e920ecaa9b29fe8350e253c771cbdcf0c5aa71c8fff6cbd0 | quote: Verifying your senders is mandatory and the way to authorize sending via the account.
  - [5] 2026-10-30: a Gmail address cannot be verified as a single sender email | capture: sha256:a553e1991e8a4f21396fa1876b51536a1d2eccd4015d1472d18e49c9806b159c | quote: Note that this excludes Gmail, due to their DMARC record, which prevents third-party servers from sending emails on their behalf.
  - [6] 2026-10-30: the free plan verifies up to 5 senders; the same page gives the daily queue, the monthly rejection, the 25-per-hour hold, 5 days of reporting and ticket-only support after 14 days, and lists no recipient restriction | capture: sha256:ecac928fdac69dab71085bca3aa45b4cb9f2f9391f8710e68503dbbbcaddf4e6 | quote: The free plan allows up to 5 sender domains or single sender email addresses to be added (paid plans do not have a limit).
  - [5] 2026-10-30: a send from an unverified sender is rejected and counts toward the monthly quota | capture: sha256:a553e1991e8a4f21396fa1876b51536a1d2eccd4015d1472d18e49c9806b159c | quote: It’s important to note that rejected attempts will still count toward the account’s monthly email quota.
  - [6] 2026-10-30: free-plan reporting covers 5 days against 30 on paid plans | capture: sha256:ecac928fdac69dab71085bca3aa45b4cb9f2f9391f8710e68503dbbbcaddf4e6 | quote: Customers on the free plan can access reporting on the Activity page for the past 5 days and paying customers can access reporting for 30 days
  - [1] 2026-10-30: new paid accounts are held at 1,000 per day until the one-time review completes | capture: sha256:7ffa4fdc442a3debb2e3e7dc551a733fcef1d83ebca17124b96e3ee90a1e4604 | quote: The initial sending quota for all new paid accounts is temporarily 1,000 emails per day.
  - [4] 2026-10-30: the account sends over SMTP at mail.smtp2go.com or through the API | capture: sha256:66fb8ee707b2e739e920ecaa9b29fe8350e253c771cbdcf0c5aa71c8fff6cbd0 | quote: The most common form of sending is using SMTP in your existing application.
  - [1] 2026-10-30: the free plan is still 1,000 per month, 200 per day and 25 per hour until a sender domain is verified | capture: sha256:7ffa4fdc442a3debb2e3e7dc551a733fcef1d83ebca17124b96e3ee90a1e4604 | quote: The free plan allows 1,000 emails per month and has a limit of 200 emails per day (a 25-per-hour limitation also applies if no sender domains are verified).
- sources:
  - [1] https://developers.smtp2go.com/docs/rate-limiting
  - [2] https://www.smtp2go.com/pricing/
  - [3] https://www.smtp2go.com/blog/know-your-sending-limits
  - [4] https://support.smtp2go.com/hc/en-gb/articles/12747932085145-Quick-Start-Guide
  - [5] https://www.smtp2go.com/blog/registering-a-verified-sender-is-now-a-required-action/
  - [6] https://support.smtp2go.com/hc/en-gb/articles/223087947-Free-Plan
