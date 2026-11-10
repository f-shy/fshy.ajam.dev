# Supernews

> supernews.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/supernews/ | JSON https://fshy.ajam.dev/api/v1/entity/supernews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Supernews

- `debrid/supernews` | trial-only | evidence documented | binding none | category Usenet provider (United States, 30 connections) - 3-day trial | tier 3-day trial
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:22.000Z (live) | stale on 2026-11-23
- url https://www.supernews.com/newsgroup/
- free tier: "Try Our 3 Day Trial" on the newsgroup page, whose title reads "3 Day Free Trial, Sign up today!". The same page advertises "50% off your first month of Supernews - that's just $5.99 to get started", against a regular "$11.99/MO" on the home page. | unit: unlimited | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: The trial is 3 days with no byte counter: "We do not limit how much Usenet you can access. Unlimited means Unlimited."
- per-object cap: No per-object cap is published. The unit of retrieval is a Usenet article, roughly 750 KB by convention. | source: [1]
- retention: "5+ years Binary and 13+ years text" in the page description; the body says "5+ years Binary and 13+ years text retention". | days: 1825 | source: [1] | note: The 5+ years figure is binary retention; the vendor gives no exact day count on the pages read.
- egress: No traffic meter is published: unlimited access and unlimited speed during the trial, 30 SSL connections. The only published charge is the $5.99 first month that follows the trial. | metered: no | free allowance: 3 days, unlimited volume, at line speed | source: [1]
- identity: card | detail: The signup page at /signup/ renders the validation text of a card form: "Please provide valid card number", "Please provide valid card expiration", "Please provide valid card cvv", plus name, address, city, state and ZIP, and the footer says "Payments by GoCardless". A payment method is therefore captured before the trial starts.
- interface: unknown
- limits:
  - per-ip-shaping: unlimited speed, capped only by the line; 30 SSL connections [1]
  - retention-clamped: 5+ years binary, 13+ years text [1]
- binding note: During the three days nothing in the vocabulary fails: there is no byte counter and no speed throttle. After the trial the $11.99/month plan is still unlimited, so the binding constraint at 1 TiB/month is the local line, not the provider.
- interface detail: NNTP over SSL (30 connections). The schema has no nntp token, so the array says unknown.
- tooling: any NNTP client; the vendor ships no downloader
- composes with: Three days at line speed is the largest single burst available behind a card: on a 100 Mbps line it is 3.24 TB, which is three times the monthly target, so one trial could cover a month if the line is fast and the card exists.
- reliability: The trial converts to $11.99/month unless cancelled; no suspension or throttle report was read.
- notes: Repeatability: no vendor sentence on trial repetition was found; /terms/ answered 404. The card gate plus GoCardless makes a second signup a second payment relationship in practice, which is stated as the mechanism and not as a vendor rule. Abandonment: if the newsgroup page stops advertising the 3-day trial, the record becomes paid-only.
- evidence note: Trial length and the unlimited terms are quoted from the vendor's own page today; the card gate is quoted from the vendor's signup form validation strings. No trial was executed.
- extras:
  - repeatable: unstated
  - repeat_basis: no sentence located; card gate only
  - volume_3d_at_line_speed.100 Mbps: 3.24 TB
  - volume_3d_at_line_speed.50 Mbps: 1.62 TB
  - volume_3d_at_line_speed.20 Mbps: 648 GB
- evidence:
  - [1] 2026-10-23: Page title "3 Day Free Trial, Sign up today!"; body "Try Our 3 Day Trial"; "We do not limit how much Usenet you can access. Unlimited means Unlimited."
  - [2] 2026-10-23: "Please provide valid card number", "Please provide valid card expiration", "Please provide valid card cvv" and "Payments by GoCardless" - a card is required at signup
  - [3] 2026-10-23: Regular price "$11.99/MO", "Unlimited Speed & Access", "30 SSL Connections"
- sources:
  - [1] https://www.supernews.com/newsgroup/
  - [2] https://www.supernews.com/signup/?account=SUPER-UNL-SSL-B
  - [3] https://www.supernews.com/
