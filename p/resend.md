# Resend

> resend.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/resend/ | JSON https://fshy.ajam.dev/api/v1/entity/resend.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Resend

- `email/resend` | qualifies-with-caveat | evidence documented | binding request-rate | category transactional sender
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://resend.com/pricing
- free tier: 3,000 emails/month and 100/day, 3 domains, 3 inboxes, 30-day retention | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a message count rather than an object
- retention: logs kept 30 days; inbound messages count against the same quota | source: [2]
- egress: not applicable: an outbound sender | metered: no | source: [1]
- identity: email | detail: an account and a verified sending domain; no card on the free plan
- interface: rest
- limits:
  - request-rate (binding): 100 emails per UTC calendar day, resetting at 00:00 UTC [2]
  - request-rate (binding): 10 requests per second per account [2]
  - request-rate (binding): received email counts against both the daily and the monthly quota [2]
- binding note: 100/day rather than 3,000/month: the 30:1 ratio means the monthly figure cannot be spent in a burst, and the page states the UTC boundary explicitly.
- interface detail: https://api.resend.com/emails
- tooling: curl, any HTTP client
- composes with: the outbound half of the free mail chain: unlimited inbound from Cloudflare Email Routing or Forward Email, then 100 messages a day out through Resend. The daily cap is the scarce link.
- reliability: sending pauses above a 4% bounce rate, which is a reputation cap rather than a volume cap
- notes: A spike at 23:50 UTC gets 100 more at midnight, which is the one burst the boundary allows.
- evidence note: no message was sent, so no delivery is proved. The submission path was probed: smtp.resend.com:587 answered 250, STARTTLS completed, and AUTH LOGIN returned 334
- extras:
  - stale_after_days: 90
- evidence:
  - [2] 2026-10-22: 'daily email quota of 100 emails/day and 3,000 emails/month', a UTC calendar day rather than a rolling window, multiple recipients counting separately, 10 requests per second, and received mail counting against the quota
  - probe:smtp://smtp.resend.com:587 2026-10-22: banner 250, EHLO advertises SIZE and 8BITMIME, STARTTLS completed, and AUTH LOGIN returned 334. The submission endpoint answers; no message was sent
- sources:
  - [1] https://resend.com/pricing
  - [2] https://resend.com/docs/knowledge-base/resend-sending-limits
