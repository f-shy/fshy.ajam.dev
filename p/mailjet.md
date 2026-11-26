# Mailjet

> mailjet.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mailjet/ | JSON https://fshy.ajam.dev/api/v1/entity/mailjet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mailjet

- `email/mailjet` | qualifies-with-caveat | evidence documented | binding request-rate | category transactional sender
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://www.mailjet.com/pricing/
- free tier: 6,000 emails/month, 200/day, 1,000 contacts | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: over-quota mail is queued for 3 days then discarded | source: [1]
- egress: not applicable: an outbound sender | metered: no | source: [1]
- identity: email | detail: an account; the page states no credit card is required at signup
- interface: rest
- limits:
  - request-rate (binding): 200 emails per day [1]
- limits note: counts of things, not rates, so no vocabulary kind names them: 1,000 contacts stored on the free plan
- interface detail: https://api.mailjet.com/v3.1/send
- tooling: curl, any HTTP client
- composes with: the largest monthly figure in the free sender set at 6,000, cut down to 200/day. It composes with the same domain as Brevo and Resend, which is where the reputation problem starts.
- reliability: over-quota mail is reported to be queued for three days and then discarded, which makes an overrun silent data loss. That sentence is reported and not documented: the knowledge-base article it came from, documentation.mailjet.com article 360043048393, returns 404 on 2026-10-22, and the pricing page does not state it
- notes: The 30:1 monthly-to-daily ratio is the same shape as Resend's. The queue-and-discard behaviour is the technical fact a reader needs before pointing a campaign at it.
- evidence note: no message was sent, so no delivery is proved. The submission path was probed: in-v3.mailjet.com:587 answered 250, STARTTLS completed, and AUTH LOGIN returned 334
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: '6,000 emails/month', '200 emails per day', '1,000 contacts', and 'there is no credit card required for the free plan at sign up'
  - probe:smtp://in-v3.mailjet.com:587 2026-10-22: banner 250, EHLO advertises SIZE and 8BITMIME, STARTTLS completed, and AUTH LOGIN returned 334. The submission endpoint answers; no message was sent
- sources:
  - [1] https://www.mailjet.com/pricing/
