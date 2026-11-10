# ImprovMX

> improvmx.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/improvmx/ | JSON https://fshy.ajam.dev/api/v1/entity/improvmx.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ImprovMX

- `email/improvmx` | qualifies-with-caveat | evidence documented | binding request-rate | category inbound forwarding
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://improvmx.com/pricing/
- free tier: 1 domain, 25 aliases, 500 forwards/day, 7-day logs, API access | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: 7 days of logs | source: [1]
- egress: not applicable: inbound only | metered: no | source: [1]
- identity: email | detail: an account
- interface: rest
- limits:
  - request-rate (binding): 500 forwards per day [1]
- limits note: counts of things, not rates, so no vocabulary kind names them: 1 domain and 25 aliases on the free plan
- interface detail: MX records on the domain, plus a management API
- tooling: the ImprovMX API
- composes with: 500 forwards a day into one mailbox, so it composes with a catch-all and not with a high-volume address.
- reliability: the free plan forwards only; it does not provide a mailbox
- notes: The 500/day figure is the inbound analogue of the outbound daily cap and is the number to check before pointing a busy address at it.
- evidence note: no probe: the inbound path needs a domain delegated to ImprovMX, and no domain was delegated for this record
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: 1 domain, 25 aliases, 500 forwards/day, 7-day logs and API access on the free plan
- sources:
  - [1] https://improvmx.com/pricing/
