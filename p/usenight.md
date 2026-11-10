# UseNight

> usenight.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenight/ | JSON https://fshy.ajam.dev/api/v1/entity/usenight.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UseNight

- `debrid/usenight` | paid-only | evidence documented | binding per-ip-shaping | category Usenet provider (Netherlands, off-peak only) - no free trial | tier Nighty
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:22.000Z (live) | stale on 2026-11-23
- url https://usenight.com/en/
- free tier: None on the page read: "Get UseNight - Starting from € 1,64 p/m". No trial, free account or free allowance is offered. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: No per-object cap is published. The unit of retrieval is a Usenet article, roughly 750 KB by convention. | source: [1]
- retention: "High retention (4085 days)" on the home page. | days: 4085 | source: [1]
- egress: Full speed only between 00:00 and 11:00 CET; outside that window the product is off-peak. No byte counter is published on the page read. | metered: no | free allowance: none | source: [1]
- identity: card | detail: The only action is "Get UseNight" into /en/order/; there is no free path. The instrument at checkout was not read.
- interface: unknown
- limits:
  - per-ip-shaping (binding): full speed only 00:00-11:00 CET; no speed figure published [1]
  - retention-clamped: 4085 days [1]
- binding note: The 11-hour window is the constraint that fails first for a scheduled pull, not the byte count: an 11-hour window at 100 Mbps is about 495 GB/day, so 1 TiB of monthly transfer fits inside a few days of the window. The page publishes no speed cap, so this is arithmetic on the window and not on a vendor number.
- interface detail: NNTP over SSL/TLS. The schema has no nntp token, so the array says unknown.
- tooling: any NNTP client; the vendor's Night Finder shows the local window
- composes with: An 11-hour daily window at €1.64/month is the cheapest sustained usenet byte in the set, but it is paid, so it enters the ladder only after a payment relationship already exists.
- reliability: The page computes the local window from IP address and says outright "Of course this is not VPN proof" - a caller behind a VPN sees the wrong window.
- notes: Repeatability: not applicable. Abandonment: if a trial appears, add a tier.
- evidence note: The price, the window and the retention figure are quoted from the vendor page today. The 495 GB/day figure is arithmetic on an assumed 100 Mbps line and is labelled as such.
- extras:
  - repeatable: not-applicable
  - repeat_basis: no free trial
  - window_hours: 11
- evidence:
  - [1] 2026-10-23: "High speeds from 00:00 until 11:00 (CET)", "High retention (4085 days)", "Get UseNight - Starting from € 1,64 p/m", "Disclaimer: This map, timezone and times are calculated based on your IP. Of course this is not VPN proof."
- sources:
  - [1] https://usenight.com/en/
