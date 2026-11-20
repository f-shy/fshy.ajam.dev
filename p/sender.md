# Sender

> sender.net | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sender/ | JSON https://fshy.ajam.dev/api/v1/entity/sender.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sender

- `email/sender-net` | qualifies-with-caveat | evidence documented | binding request-rate | category marketing sender
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://www.sender.net/pricing/
- free tier: up to 2,500 subscribers and 15,000 emails per month, never expires | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not stated | source: [1]
- egress: not applicable: an outbound sender | metered: no | source: [1]
- identity: email | detail: an account; 'no credit card, nothing to activate'
- interface: rest
- limits:
  - request-rate (binding): 15,000 emails per month [1]
- limits note: counts of things, not rates, so no vocabulary kind names them: 2,500 subscribers
- interface detail: the Sender API and SMTP relay
- tooling: curl, any SMTP client
- composes with: 15,000/month against a 2,500-subscriber list, so the list is the smaller cap and the send count is hard to exhaust.
- reliability: free-plan messages carry Sender's branding in the footer
- notes: The same 15,000 emails a month as SendPulse, and the same missing daily cap. The vendor page states the monthly figure, so it is documented; 15,000 in one day is not established.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: 'The Free Forever plan includes up to 2,500 subscribers and 15,000 emails per month, never expires', and 'No credit card, nothing to activate'
- sources:
  - [1] https://www.sender.net/pricing/
