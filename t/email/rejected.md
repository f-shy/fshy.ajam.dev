# Email: rejected and dead

> Sending, receiving, forwarding and inbox APIs.

47 records: 30 usable, 3 trial, 9 paid only, 3 rejected, 1 dead; 1 self-hosted of any group, listed last. This page lists the rejected and dead records, each with the evidence that rejected it; the usable, trial and paid-only ones are on https://fshy.ajam.dev/t/email.md. Each line: provider (its page in Markdown), record id (its JSON is https://fshy.ajam.dev/api/v1/record/<id>), verdict, free tier, identity, card, phone, evidence, stale date, parsed price, summary. In full: https://fshy.ajam.dev/t/email/llms-full.txt.

## Rejected (3)

- [MailerSend](https://fshy.ajam.dev/p/mailersend.md) [`email/mailersend`](https://fshy.ajam.dev/api/v1/record/email/mailersend): fails-quota | free tier | card | no phone | documented | stale on 2026-12-05. 500 emails/month on the Free plan once the account is approved, with a daily quota of 100 API and SMTP relay requests; 1 domain, 1 API token, 1 webhook, 1...
- [MailPace](https://fshy.ajam.dev/p/mailpace.md) [`email/mailpace`](https://fshy.ajam.dev/api/v1/record/email/mailpace): fails-quota | free tier | email | no card | no phone | documented | stale on 2026-12-03. Up to 100 emails per month on a free plan granted on request by email to support; public plans start under USD 4 per month for 1,000 emails
- [Postmark](https://fshy.ajam.dev/p/postmark.md) [`email/postmark`](https://fshy.ajam.dev/api/v1/record/email/postmark): fails-quota | free tier | email | no card | no phone | documented | stale on 2026-12-05. 100 emails/month on the free Developer tier, which does not expire

## Dead (1)

- [MailExpire](https://fshy.ajam.dev/p/mailexpire.md) [`email/mailexpire`](https://fshy.ajam.dev/api/v1/record/email/mailexpire): dead | no free tier | email | no card | no phone | documented. A free email alias, valid for a chosen period from 12 hours to 3 months, forwarded to the user's real address; usable as often as the user likes
