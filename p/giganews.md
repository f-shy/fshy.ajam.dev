# Giganews

> giganews.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/giganews/ | JSON https://fshy.ajam.dev/api/v1/entity/giganews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Giganews

- `debrid/giganews` | trial-only | evidence reported | binding retention-clamped | category usenet provider (Certida/Giganews backbone) | tier 1 Year
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T11:28:55.819Z (live) | stale on 2026-11-18
- url https://www.order.giganews.com/signup/
- price USD 8.33 (12-month term)
- free tier: A free trial is attached to every term: 14 days on the 12-month and 6-month prepaid plans and 3 days on the 1-month plan, all reached through a billing redirect. | unit: unlimited | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: The vendor homepage states 'Over 5 Years of Binaries'; the r/usenet map records 550+ days for binaries and 5,800+ days for text on the same backbone. The conservative figure is recorded. | days: 550 | source: [2]
- egress: Unlimited Transfer and Unlimited Speed, 100 connections, SSL, VyprVPN included | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: The trial is entered through a billing redirect, so a payment method is captured at the start. The vendor's own signup page describes the trial as starting from that billing step.
- interface: nntp
- limits:
  - request-rate: 100 connections [1]
  - retention-clamped (binding): 550+ days for binaries against 5,800+ days for text, reported; the vendor states over 5 years of binaries [2]
- limits note: 1 month $9.99, 6 months $9.17/mo, 1 year $8.33/mo billed $100.00 against a stated $217.39 regular price. All terms include VyprVPN. The trial links point at order.giganews.com/signup/billing_redirect.html, which is a payment step.
- binding note: Binary depth is the constraint, not volume: unlimited transfer at 100 connections never runs out, but a 550-day binary spool cannot retrieve a 2019 post however much bandwidth is left.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: Its only stacking value is the bundled VyprVPN; the 550-day binary spool makes it a poor primary beside any Omicron or Abavia plan.
- reliability: Own US and NL infrastructure on AS30094. The vendor states over 5 years of binary retention; the community map records 550 days, a large gap between vendor and mapped figures.
- notes: Where two sources disagree the record keeps the conservative number: 550 days of binaries, not the 'Over 5 Years of Binaries' the vendor states.
- evidence note: Prices, connections and the trial length are vendor-stated and read. Binary retention is third-party and contradicts the vendor's number, so the record keeps 550 days and sits at the reported rung.
- extras:
  - backbone: Giganews / Certida, AS30094
  - retention_conflict: vendor 'Over 5 Years of Binaries' vs mapped 550 days binaries
- evidence:
  - [1] 2026-10-23: 1 Year $8.33/mo billed yearly at $100.00; 6 Months $9.17/mo; 1 Month $9.99/mo; '+ 14 days free trial' and '+ 3 days free trial'; 100 connections; unlimited transfer
  - [2] 2026-10-23: Giganews backbone table: '550+ days (binaries), 5800+ days (text)' on both US and NL
  - [3] 2026-11-03: the vendor homepage states over 5 years of binaries | capture: sha256:a41f6f4e87170c23158ae10d5130e1c3d5cde4455eaababac6f0b3220019d0e1 | quote: Over 5 Years of Binaries
  - [2] 2026-11-03: the map records 550+ days of binaries and 5800+ days of text; the vendor's own statement is a separate evidence row | capture: sha256:ce68343303ed49e39a8c4c999a557b78a25d3f976eb44da979781c00dd669f2c
  - [1] 2026-11-03: 1 Year price unchanged | capture: sha256:54d7c037359326157665c14d0722e17853a28f20d3b4efb97d136f08dbf449b0 | quote: 1 Year $8.33/mo. BILLED YEARLY AT ~~$217.39~~ $100.00
  - [1] 2026-11-03: 14-day trial on the 12-month and 6-month terms unchanged | capture: sha256:54d7c037359326157665c14d0722e17853a28f20d3b4efb97d136f08dbf449b0 | quote: + 14 days free trial
  - [1] 2026-11-03: 3-day trial on the 1-month term unchanged | capture: sha256:54d7c037359326157665c14d0722e17853a28f20d3b4efb97d136f08dbf449b0 | quote: + 3 days free trial
  - [1] 2026-11-03: 100 connections unchanged | capture: sha256:54d7c037359326157665c14d0722e17853a28f20d3b4efb97d136f08dbf449b0 | quote: 100 Connections
- sources:
  - [1] https://www.order.giganews.com/signup/
  - [2] https://www.reddit.com/r/usenet/wiki/providers
  - [3] https://giganews.com/
