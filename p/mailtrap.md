# Mailtrap

> mailtrap.io | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mailtrap/ | JSON https://fshy.ajam.dev/api/v1/entity/mailtrap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mailtrap

- `email/mailtrap` | qualifies-with-caveat | evidence documented | binding request-rate | category transactional sender
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://mailtrap.io/pricing/
- free tier: 4,000 emails per month and 150 emails per day on the free tier, 1 user, 1 domain, 3 days of logs | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: 3 days of email logs on the free plan | source: [1]
- egress: not applicable: an outbound sender | metered: no | source: [1]
- identity: email | detail: an account
- interface: rest
- limits:
  - request-rate (binding): 150 emails per day [1]
- limits note: counts of things, not rates, so no vocabulary kind names them: 1 user and 1 domain. The pricing page states 4,000 emails per month and 150 per day on the Email API/SMTP free tab. A footnote adds that the email limit is per month and 'Shares quota between sending and receiving'. The page carries no separate sending sub-allowance. The 1,000 that circulates is the sandbox message-store column and the per-1,000 overage price. It is not a send cap.
- interface detail: the Mailtrap Email API and SMTP, on the Email API tab
- tooling: curl, any SMTP client
- composes with: 150/day out with 4,000 in the pool, so it composes with a domain and with a launch that spikes for one day and then stops.
- reliability: the 4,000 is a sandbox-and-send pool; the pricing page presents the two tabs separately
- notes: The 4,000 headline is the trap: the free tier splits sending from sandbox testing and 150/day is what a launch meets.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: the Free column reads '4,000 emails', '150 emails/day', '1 user', '3 days of email logs' and '1 domain'
- sources:
  - [1] https://mailtrap.io/pricing/
