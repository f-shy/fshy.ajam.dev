# MaximumUSENET

> maximumusenet.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/maximumusenet/ | JSON https://fshy.ajam.dev/api/v1/entity/maximumusenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MaximumUSENET

- `debrid/maximumusenet` | paid-only | evidence reported | binding volume-quota | category usenet provider (monthly volume plans and block accounts) | tier 200GB monthly
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-11-18
- url https://maximumusenet.com/
- price USD 20 for a 1,000 GB block
- free tier: No free tier and no trial on the home page read; the cheapest paid plan is USD 2.00 a month for 200 GB (third-party index). | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: source: [1]
- retention: unverified: the home page read does not state a number of days | source: [1]
- egress: Metered: monthly plans of 200 GB and 500 GB, and block accounts of 500 GB and 1,000 GB | metered: yes | free allowance: none | source: [2]
- identity: card | detail: unverified: the sign-up was not opened, so the fields it asks for are behind a sign-up.
- interface: nntp
- limits:
  - volume-quota (binding): monthly plans of 200 GB and 500 GB; blocks of 500 GB and 1,000 GB with no expiry [2]
  - request-rate: 50 connections [1]
- limits note: USD 2 a month for 200 GB, USD 3 a month for 500 GB, USD 12 for a 500 GB block and USD 20 for a 1,000 GB block (third-party index; the home page shows the same four prices).
- binding note: Every product is a fixed number of GB; no unlimited plan is listed.
- interface detail: NNTP with 256-bit SSL
- composes with: The 1,000 GB block does not expire, so it works as bulk fill behind another primary at a one-time price.
- reliability: Backbone and retention are not stated on the vendor page read.
- notes: Volume-metered only.
- evidence note: The plan prices come from a third-party index and match the four prices on the vendor home page; the 50-connection figure is on the vendor page.
- evidence:
  - [2] 2026-11-03: monthly plans and non-expiring blocks with their prices | capture: sha256:d0cd834aa0b967ca895160db46b7b0c7a3d37a6c3b5dde695e89f7f3f0c5dfce | quote: Monthly plans: $2/month (200 GB) and $3/month (500 GB). Block accounts: 500 GB ($12) and 1,000 GB ($20, no expiry).
  - [1] 2026-11-03: 50 connections on the vendor page | capture: sha256:cb83572e3698319f4267dbd3694391bfd148a05e5d13272c40297890560f07bf | quote: - 50 Connections
- sources:
  - [1] https://maximumusenet.com/
  - [2] https://www.usenet.org/providers/maximumusenet
