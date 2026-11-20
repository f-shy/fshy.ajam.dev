# Hydra Usenet

> hydrause.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hydrause/ | JSON https://fshy.ajam.dev/api/v1/entity/hydrause.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hydra Usenet

- `debrid/hydra-usenet` | paid-only | evidence reported | binding volume-quota | category usenet provider (new in 2026, non-expiring block accounts) | tier Block accounts
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-11-18
- url https://hydrause.net/
- free tier: No free tier or trial stated on the home page read; access is bought by card checkout or redeemed from a prepaid token. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: source: [1]
- retention: unverified: the home page says 'High retention article storage' without a number of days | source: [1]
- egress: Non-expiring block accounts from 100 GB to 1 TB per a third-party index; the plan prices load by script and were not in the page read | metered: yes | free allowance: none | source: [2]
- identity: card | detail: The home page says 'Buy a plan below with card checkout, or redeem a prepaid token'; payment methods listed by a third-party index are card and crypto. The member signup was not opened: unverified: behind a sign-up.
- interface: nntp
- limits:
  - request-rate: up to 25 concurrent connections [1]
  - volume-quota (binding): non-expiring blocks of 100 GB to 1 TB (third-party index) [2]
- limits note: Block prices: unverified: the plan table is loaded by script and was not in the page read.
- binding note: Every product is a fixed block of GB.
- interface detail: NNTP; servers in the US and the EU
- composes with: Blocks do not expire, so a 1 TB block is a one-time fill account; the vendor also sells prepaid tokens that are redeemed on its member page.
- reliability: A service that launched in 2026 and leaves many details open, per a third-party index; the page shows a 'real completion rate' counter that loaded empty in the capture.
- notes: Prices unread; the verdict rests on there being no free offer on the page.
- evidence note: Connections and checkout route are on the vendor page; the block range is third-party; prices are unread.
- evidence:
  - [1] 2026-11-03: 25 concurrent connections | capture: sha256:84178913a120501ccee6331d59123dc002431035ef832a533334b033e85d7fb2 | quote: Up to 25 concurrent connections
  - [1] 2026-11-03: plans are bought by card checkout or redeemed from a prepaid token | capture: sha256:84178913a120501ccee6331d59123dc002431035ef832a533334b033e85d7fb2 | quote: Buy a plan below with card checkout, or redeem a prepaid token if you already have one.
  - [2] 2026-11-03: a third-party index gives the block range 100 GB to 1 TB, non-expiring | capture: sha256:ebcef3dbf893a2a18fa3e92456a84602e40501f2f1d6b37466bf7fc1750705f3 | quote: Hydra Usenet is a very young Usenet provider that only launched in 2026. Its website sells non-expiring block accounts from 100 GB to 1 TB with 10 to 25 connections, and the servers are in the USA and the EU. Many details are still left open by the provider.
- sources:
  - [1] https://hydrause.net/
  - [2] https://www.usenet.org/providers/hydrausenet
