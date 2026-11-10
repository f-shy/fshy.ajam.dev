# Loops

> loops.so | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/loops/ | JSON https://fshy.ajam.dev/api/v1/entity/loops.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Loops

- `email/loops` | qualifies-with-caveat | evidence documented | binding request-rate | category marketing and transactional sender
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://loops.so/pricing
- free tier: 4,000 sends per rolling 30 days, 1,000 contacts, marketing and transactional combined | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not stated | source: [1]
- egress: not applicable: an outbound sender | metered: no | source: [1]
- identity: email | detail: an account
- interface: rest
- limits:
  - request-rate (binding): 4,000 sends per rolling 30 days [1]
- limits note: counts of things, not rates, so no vocabulary kind names them: 1,000 contacts, which makes 4,000 sends unreachable for a 4,000-person list
- binding note: the 1,000-contact ceiling binds, not the 4,000 sends.
- interface detail: the Loops transactional API
- tooling: curl, any HTTP client
- composes with: 4,000 sends against 1,000 contacts, so the contact ceiling decides and a list of 1,000 can receive four messages a month.
- reliability: sends and contacts are separate caps, so the smaller one decides
- extras:
  - stale_after_days: 90
- evidence:
  - [2] 2026-10-22: the machine-readable pricing file states 4,000 sends per rolling 30 days and a 1,000-contact ceiling
- sources:
  - [1] https://loops.so/pricing
  - [2] https://loops.so/.well-known/pricing.txt
