# 1Cloud File

> 1cloudfile.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/1cloudfile/ | JSON https://fshy.ajam.dev/api/v1/entity/1cloudfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 1Cloud File

- `debrid/1cloudfile` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file host (free upload, premium) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://1cloudfile.com/
- free tier: Uploading and downloading are 100% free; free or non-account files are kept 20 days and each file must be under 10 GB. | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 10 GB per file for free or non-account uploads and for premium | source: [1]
- retention: 20 days for free or non-account files and for premium files | days: 20 | source: [1]
- egress: Premium: $4.99 for 1 month, $13.99 for 3 months, $49.99 for the longest period listed; benefits are direct downloads with no waiting and no advertising. No free download volume is published. | metered: no | free allowance: not published | source: [2]
- identity: anonymous | detail: The FAQ states limits for free or non-account uploads, and the home page has a no-registration upload route. Premium is a paid account.
- interface: rest
- limits:
  - per-object-cap: 10 GB per file on both free and premium [1]
  - retention-clamped (binding): files are kept 20 days on both free and premium [1]
- binding note: Files are removed after 20 days on every tier, so nothing stored here outlasts a month.
- interface detail: Web upload and an API page linked from the footer; the API was not read.
- tooling: Browser upload; the footer links an API page that was not read.
- composes with: Premium does not extend retention: both tiers keep files 20 days, so the paid tier buys speed and no waiting, not storage time.
- reliability: The vendor pages answered HTTP 403 to the page reader while still returning their full content.
- notes: Cheapest paid tier is the $4.99 one-month premium.
- evidence note: FAQ and upgrade page read through a page reader that received HTTP 403 with the page body. The registration form fields are unread.
- evidence:
  - [1] 2026-11-03: the cap is 10 GB per file on free and on premium | capture: sha256:ec8bfc60af7fc47d4654b9b2e9b0d70a26966a20418d9cc7c0fa5df56ba77147 | quote: Each file you upload must be less than 10 GB in size for free/non accounts or less than 10 GB in size for premium accounts.
  - [1] 2026-11-03: retention is 20 days on both tiers | capture: sha256:ec8bfc60af7fc47d4654b9b2e9b0d70a26966a20418d9cc7c0fa5df56ba77147 | quote: Free/non accounts files are kept for 20 days. Premium accounts files are kept for 20 days.
  - [2] 2026-11-03: the 1-month premium period costs $4.99 | capture: sha256:38edf3956a3b0567ef7a5be43d97eafa085559ce253c7bfff5f219f5928e687b | quote: ### $ 4.99
  - [2] 2026-11-03: the 3-month premium period costs $13.99 | capture: sha256:38edf3956a3b0567ef7a5be43d97eafa085559ce253c7bfff5f219f5928e687b | quote: ### $ 13.99
- sources:
  - [1] https://1cloudfile.com/faq
  - [2] https://1cloudfile.com/upgrade
