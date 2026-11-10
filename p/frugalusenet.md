# Frugal Usenet

> frugalusenet.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/frugalusenet/ | JSON https://fshy.ajam.dev/api/v1/entity/frugalusenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Frugal Usenet

- `debrid/frugal-usenet` | paid-only | evidence documented | binding none | category usenet provider (NetNews primary + UsenetFarm bonus) | tier Monthly
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T01:52:29.000Z (live) | stale on 2026-11-23
- url https://www.frugalusenet.com/
- price USD 5.99 (monthly)
- free tier: No free tier and no free trial. The homepage sells a USD 5.00/mo entry and a 14-day window is quoted by third-party review sites, not by the vendor page read. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: 5000+ days retention on the primary, stated on the homepage price block | days: 5000 | source: [1]
- egress: Up to 250 connections across 8 server locations on 6 continents | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: Email plus a paid order through billing.frugalusenet.com. No trial; a card is required before the first byte.
- interface: nntp
- limits:
  - request-rate: up to 250 connections [1]
  - volume-quota: the bundled UsenetFarm bonus server has a 1 TB/month cap - reported, not on the vendor page [2]
  - retention-clamped: 5000+ days on the primary [1]
- limits note: USD 5.99/mo monthly; USD 60/year including a Blocknews block account; the billing portal also lists a Yearly Unlimited at USD 35.00/year excluding Blocknews. 8 server locations: 2 US, 1 EU and single servers in Africa, Asia, Australia and South America, plus a bonus/backup EU server.
- binding note: Unlimited volume on the primary NetNews spool. The 1 TB/month cap applies only to the bundled UsenetFarm bonus server, which is a completion aid rather than the main feed.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: One subscription gives a NetNews primary plus a UsenetFarm bonus server, the cheapest two-backbone stack in the sector; add a block only for content older than 5,000 days.
- reliability: Two backbones in one plan: NetNews as primary and UsenetFarm as the bonus EU fill server, which is the cheapest way to get two independent feeds without buying two subscriptions.
- notes: The homepage and the billing portal quote different yearly prices for different bundles ($60 with a Blocknews block, $35 without), which is not a contradiction once the bundle is read, but it reads as one at a glance.
- evidence note: Prices, connections and retention are from the vendor homepage read. The USD 35/year figure is from the vendor's own billing portal, which contradicts the homepage's USD 60/year bundle; both are recorded.
- extras:
  - backbone: NetNews (AS6450) primary + UsenetFarm bonus
  - server_locations: 8
  - yearly_without_block: USD 35.00
- evidence:
  - [1] 2026-10-23: 'As Low As $5.00/Month'; '$5.99 Per Month w/ 5000+ Days Retention'; '$60 per year - incl/ Blocknews block account'; 'Up To 250 Connections'; 8 server locations
  - [3] 2026-10-23: Yearly Unlimited Subscription $35.00 Per Year; 'Blocknews NOT Included'
  - [2] 2026-10-23: Frugal Usenet on NetNews, AS6450; bonus UsenetFarm server capped at 1 TB/month
- sources:
  - [1] https://www.frugalusenet.com/
  - [2] https://www.reddit.com/r/usenet/wiki/providers
  - [3] https://billing.frugalusenet.com/signup/byUkhnlJF
