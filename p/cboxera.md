# Cboxera

> cboxera.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cboxera/ | JSON https://fshy.ajam.dev/api/v1/entity/cboxera.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cboxera

- `debrid/cboxera` | qualifies-with-caveat | evidence documented | binding volume-quota | category multi-hoster (premium link generator, free plan) | tier Free Plan
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:13.292Z (live) | stale on 2026-12-04
- url https://www.cboxera.com/
- free tier: Free Plan, $0 lifetime: limited hosts, no streaming, 25 GB daily bandwidth, advertisements. | unit: GB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: no per-file cap stated | source: [1]
- retention: unverified: links are proxied, and the home page states no files are stored on its servers | source: [1]
- egress: 25 GB daily bandwidth on the free plan; 150 GB daily on paid plans. | metered: yes | free allowance: 25 GB per day | source: [1]
- identity: email | detail: Registration asks for a username, an email address and a password, and agreement to the terms.
- interface: unknown
- limits:
  - volume-quota (binding): free 25 GB daily bandwidth; paid 150 GB daily bandwidth [1]
- binding note: Daily bandwidth in bytes is the stated cap on both the free and the paid plans.
- interface detail: Web generator after login; links are proxied directly from the file hosts over HTTPS.
- tooling: Browser only on the pages read.
- composes with: Paid plans: 1 month $7, 2 months $13, 3 months $19, each with 50+ hosts and 150 GB daily bandwidth; purchase by Stripe, reseller or PayTM (IN).
- reliability: No outage observed on the day read.
- notes: The paid plans share one 150 GB daily figure across 1, 2 and 3 months.
- evidence note: First-party home page and registration page.
- evidence:
  - [1] 2026-11-03: the free plan is lifetime, limited hosts, no streaming | capture: sha256:446b0d90cc79b20f7c9c722003bf023b29b17ee762a11582b76d05649e4332d4 | quote: ### Free Plan #### $ 0 Lifetime - Lifetime Free - Limited Hosts - No Streaming
  - [1] 2026-11-03: the free plan carries 25 GB daily bandwidth | capture: sha256:446b0d90cc79b20f7c9c722003bf023b29b17ee762a11582b76d05649e4332d4 | quote: - 25 GB Daily Bandwidth
  - [1] 2026-11-03: the 1-month plan is $7 | capture: sha256:446b0d90cc79b20f7c9c722003bf023b29b17ee762a11582b76d05649e4332d4 | quote: ### 1 Month #### $ 7 30 DAYS PREMIUM
  - [1] 2026-11-03: paid plans carry 150 GB daily bandwidth | capture: sha256:446b0d90cc79b20f7c9c722003bf023b29b17ee762a11582b76d05649e4332d4 | quote: - 150 GB Daily Bandwidth
  - [2] 2026-11-03: registration asks for username, email and password | capture: sha256:1a5b59172eb06a46f4fe4cb1da39a46a442d4d330bba1d521d2dedb3b2a2886a
- sources:
  - [1] https://www.cboxera.com/
  - [2] https://www.cboxera.com/register
