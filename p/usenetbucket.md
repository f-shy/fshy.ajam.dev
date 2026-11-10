# UsenetBucket

> usenetbucket.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenetbucket/ | JSON https://fshy.ajam.dev/api/v1/entity/usenetbucket.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UsenetBucket

- `debrid/usenetbucket` | trial-only | evidence documented | binding per-ip-shaping | category Usenet provider (Netherlands, Scandinavia-focused) - €1 trial | tier Ultimate Bucket trial
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:22.000Z (live) | stale on 2026-11-23
- url https://usenetbucket.com/
- free tier: "Curious? Try our Ultimate Bucket for just €1" and "Try our Ultimate Bucket for just €1! 2 days - 400 Mbit* - 25 connections - Unlimited traffic - SSL-support - 1600 days retention". The page's meta description still advertises "Try us 7 days for free, no strings attached!" | unit: hours | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: The meta description and the rendered page disagree: 7 days free in the HTML head, 2 days for €1 in the body. The record keeps the rendered offer, which is the one a buyer sees, and treats the meta sentence as stale SEO. Neither is a free trial: €1 is a payment.
- per-object cap: No per-object cap is published. The unit of retrieval is a Usenet article, roughly 750 KB by convention. | source: [1]
- retention: "1600 days retention" on every Bucket row and in the trial line. | days: 1600 | source: [1]
- egress: "Unlimited traffic" on all four buckets; no overage price is published. | metered: no | free allowance: 2 days at 400 Mbit with 25 connections, for €1 | source: [1]
- identity: card | detail: The €1 trial is bought: the page says "Secure Payments - All payments are safely processed by certified payment providers", and there is no zero-price path on the site. The exact instrument was not read at checkout.
- interface: unknown
- limits:
  - per-ip-shaping (binding): 15 Mbit on Basic, 60 Mbit on Comfort, 400 Mbit on Ultimate [1]
  - retention-clamped: 1600 days [1]
- binding note: The €1 trial is two days with unlimited traffic, so the only cap is 400 Mbit over 48 h: 50 MB/s x 172,800 s = 8.64 TB. The paid 30-day Basic bucket at 15 Mbit is the step that binds at 1 TiB/month (about 4.9 TB/month ceiling).
- interface detail: NNTP over SSL. The schema has no nntp token, so the array says unknown.
- tooling: any NNTP client
- composes with: Two days at 400 Mbit is about 8.6 TB of theoretical ceiling for €1 - the cheapest byte in published records - but it is a purchase, so it belongs behind the payment line, not in the free ladder.
- reliability: Prices are per 30 days, not per calendar month; nothing about suspension was read.
- notes: Repeatability: no vendor sentence exists. A €1 purchase is repeatable only by paying again, so there is nothing to repeat for free. Abandonment: if the €1 line is removed the record becomes paid-only.
- evidence note: The rendered €1 / 2-day offer and the 400 Mbit / 25-connection terms are quoted from the vendor page today. The conflict with the site's own meta description is recorded rather than resolved.
- extras:
  - repeatable: not-applicable
  - repeat_basis: paid trial
  - meta_conflict: meta description: 'Try us 7 days for free, no strings attached!' vs body: '2 days ... for just €1'
- evidence:
  - [1] 2026-10-23: "Try our Ultimate Bucket for just €1", "2 days - 400 Mbit* - 25 connections - Unlimited traffic", "1600 days retention", and the Basic/Comfort/Ultimate price rows at €2.95 / €4.95 / €12.95 per 30 days
  - [2] 2026-10-23: The order page repeats the same €1 line and "All payments are safely processed by certified payment providers"; no 7-day free offer appears in the body
- sources:
  - [1] https://usenetbucket.com/
  - [2] https://usenetbucket.com/order
