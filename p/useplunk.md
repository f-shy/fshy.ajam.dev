# Plunk

> useplunk.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/useplunk/ | JSON https://fshy.ajam.dev/api/v1/entity/useplunk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Plunk (hosted)

- `email/plunk-hosted` | qualifies-with-caveat | evidence documented | binding request-rate | category transactional sender
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://www.useplunk.com/
- free tier: 1,000 emails/month with unlimited contacts | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not stated | source: [1]
- egress: not applicable: an outbound sender | metered: no | source: [2]
- identity: email | detail: an account
- interface: rest
- limits:
  - request-rate (binding): 1,000 emails per month [1]
  - request-rate (binding): an attachment costs 2 credits and inbound counts against the same allowance [1]
- interface detail: the Plunk API
- tooling: curl, any HTTP client
- composes with: 1,000/month with unlimited contacts, so a large list is possible and the month is the cap.
- reliability: attachments are double-charged against the monthly allowance
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: the hosted free plan is 1,000 emails/month; the 3,000 figure in circulation is older
- sources:
  - [1] https://docs.useplunk.com/concepts/billing
  - [2] https://www.useplunk.com/
