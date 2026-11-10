# HitNews

> hitnews.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hitnews/ | JSON https://fshy.ajam.dev/api/v1/entity/hitnews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HitNews

- `debrid/hitnews` | trial-only | evidence documented | binding none | category Usenet provider (Netherlands) - €2.50, 3-day trial | tier 3-day trial
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:22.000Z (live) | stale on 2026-11-23
- url https://hitnews.com/
- free tier: "Start 3-day trial - €2.50" on the home page. No free trial is offered; the three-day entry is bought. | unit: hours | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: The trial is a paid product against a Power plan priced at €4.67/month (€14.00 per 3 months).
- per-object cap: No per-object cap is published. The unit of retrieval is a Usenet article, roughly 750 KB by convention. | source: [1]
- retention: "3700+ days of text retention" on the home page; no separate binary retention figure is published there. | days: 3700 | source: [1] | note: The page describes 3700+ days as text completion and says binaries are kept 'as long as possible' with its own algorithm, so the binary depth is not a published number.
- egress: "Every plan is unlimited speed and unlimited data"; no traffic price is published. | metered: no | free allowance: none: the 3-day entry costs €2.50 | source: [1]
- identity: card | detail: The 3-day entry is a €2.50 purchase through /3day.html; no zero-price path is published. The exact instrument at checkout was not read.
- interface: unknown
- limits:
  - per-ip-shaping: unlimited speed; 100 connections on every plan [1]
  - retention-clamped: 3700+ days text retention [1]
- binding note: During the three days no vocabulary constraint fails: unlimited data, unlimited speed, 100 connections. At 1 TiB/month the paid Power plan is also unlimited, so the line is the constraint.
- interface detail: NNTP on news.hitnews.com ports 119 / 563 / 443, 100 connections. The schema has no nntp token, so the array says unknown.
- tooling: any NNTP client; the site supplies server settings only
- composes with: A €2.50 three-day burst at unlimited speed is the cheapest way to test a 400 Mbit line, but it is not part of a free month; it is a payment relationship with a 3-day window.
- reliability: The home page rendered an inline error banner ("Sorry! an error occured. Please contact support") next to the pricing content on the read; the price table itself rendered, so the prices are legible but the site is not clean.
- notes: Repeatability: a paid trial is repeatable only by paying again; no vendor sentence is needed and none was found. Abandonment: if a free trial appears on the home page, this record needs a new tier rather than an edit.
- evidence note: The €2.50 / 3-day line and the plan prices are quoted from the vendor page today. Nothing was purchased.
- extras:
  - repeatable: not-applicable
  - repeat_basis: paid trial
- evidence:
  - [1] 2026-10-23: "Start 3-day trial - €2.50", "3700+ days of text retention, 140,000 newsgroups and 100 connections on every plan", Power €4.67/month, Family €7.00/month, Block from €12.50 per 500 GB
- sources:
  - [1] https://hitnews.com/
