# Forward Email

> forwardemail.net | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/forwardemail/ | JSON https://fshy.ajam.dev/api/v1/entity/forwardemail.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Forward Email

- `email/forward-email` | qualifies-with-caveat | evidence documented | binding retention-clamped | category inbound forwarding
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://forwardemail.net/en/pricing
- free tier: unlimited domains, unlimited aliases, unlimited inbound email, 50 MB attachments, forward-only | unit: unlimited | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: 50 MB attachment limit per message | source: [1]
- retention: the free tier stores nothing; it forwards and keeps no mailbox | source: [1]
- egress: not applicable: the free tier cannot send | metered: no | source: [1]
- identity: email | detail: an account with the domain delegated
- interface: rest
- limits:
  - retention-clamped (binding): the free tier is forwarding only: no sending and no mailbox storage [1]
  - per-object-cap: 50 MB attachment limit [1]
- interface detail: MX records on the domain, plus an API
- tooling: the Forward Email API
- composes with: the widest receiving offer found: unlimited inbound across unlimited domains, forwarded into a mailbox. It composes with any sender and cannot send itself.
- reliability: sending requires the USD 3/month Enhanced Protection tier
- notes: A feature removed rather than a volume capped. Unlimited inbound across unlimited domains is the widest receiving offer found; the cost is that nothing can send.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: 'Unlimited inbound email', '50 MB attachment limit', and 'Limitations: Email forwarding only, which means you cannot send mail'
- sources:
  - [1] https://forwardemail.net/en/pricing
