# SendPulse

> sendpulse.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sendpulse/ | JSON https://fshy.ajam.dev/api/v1/entity/sendpulse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SendPulse

- `email/sendpulse` | qualifies-with-caveat | evidence documented | binding request-rate | category marketing and transactional sender
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://sendpulse.com/pricing
- free tier: up to 15,000 emails per month, 3 sender addresses, 250 MB of image storage | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not stated | source: [1]
- egress: not applicable: an outbound sender | metered: no | source: [1]
- identity: email | detail: an account
- interface: rest
- limits:
  - request-rate (binding): 15,000 emails per month on the free tariff [1]
- limits note: counts of things, not rates, so no vocabulary kind names them: 3 sender email addresses
- interface detail: the SendPulse API and SMTP relay
- tooling: curl, any SMTP client
- composes with: 15,000/month with no stated daily cap, so it is the only free sender here that could in principle burst; whether it does is not established.
- reliability: the free tariff is marketing-shaped and a per-day cap is not stated on the pricing table
- notes: The vendor table states it, so it is documented. No daily cap appears, which is the gap: 15,000 in one day is not established.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: 'Emails | Up to 15,000 per month' in the FREE column, plus 3 sender addresses and 250 MB of image storage
- sources:
  - [1] https://sendpulse.com/pricing
