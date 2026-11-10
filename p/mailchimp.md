# Mandrill

> mailchimp.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mailchimp/ | JSON https://fshy.ajam.dev/api/v1/entity/mailchimp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mandrill (Mailchimp Transactional)

- `email/mandrill` | trial-only | evidence documented | binding write-gated | category transactional sender
- needs card yes, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://mailchimp.com/pricing/transactional-email/
- free tier: up to 500 free sends to a verified domain, one demonstration block | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable | source: [1]
- egress: not applicable: an outbound sender | metered: no | source: [1]
- identity: card | detail: a Mailchimp account with a payment method
- interface: rest
- limits:
  - request-rate: 500 emails in total, not per month [1]
  - write-gated (binding): sends only to the account's verified domain during the demonstration [1]
- interface detail: https://mandrillapp.com/api/1.0/messages/send
- tooling: curl, any HTTP client
- composes with: 500 sends in total to one verified domain, so it composes with nothing that needs a recipient list.
- reliability: the demonstration block cannot send to arbitrary recipients
- notes: Not a recurring allowance, which is what the '500 free emails' claim in circulation gets wrong.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: 'New transactional email users can get up to 500 free email sends to their verified domain', and paid blocks are USD 20 per 25,000
- sources:
  - [1] https://mailchimp.com/pricing/transactional-email/
