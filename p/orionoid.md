# Orion

> orionoid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/orionoid/ | JSON https://fshy.ajam.dev/api/v1/entity/orionoid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Orion (orionoid.com)

- `debrid/orionoid` | qualifies-with-caveat | evidence reported | binding volume-quota | category link index for torrent, usenet and hoster links (feeds debrid services; holds no files) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:14.098Z (live) | stale on 2026-11-18
- url https://orionoid.com/
- free tier: A free account gets a few links, hashes and containers per day; a third-party setup guide puts the free limit at 100 links per day. The index holds no files: the bytes come from a debrid service or a torrent client. | unit: requests | metered on: request-count | read on: 2026-11-03 | source: [1] | note: The true unit is link retrievals per day over a 24-hour sliding window, not HTTP requests. The first-party page says 'a few' and gives no number; the 100 comes from a third-party guide.
- per-object cap: not applicable: Orion returns links and metadata, not files; per-file size limits belong to the debrid service or host that serves the bytes | source: [1]
- retention: Community-maintained database; entries stay until removed and links can go stale: 'Orion does not guarantee reliable data.' | source: [1]
- egress: No byte allowance: the API returns text only. Free accounts are limited in daily link, hash and container counts, and in debrid resolving through Orion during times of high demand. | metered: no | free allowance: none published for bytes | source: [1]
- identity: anonymous | detail: Registration takes an email address or only a username; without an email the password cannot be recovered and no support mail arrives. No card, phone or ID on the free account.
- interface: rest
- limits:
  - volume-quota (binding): free account: 100 links per day on a 24-hour sliding window (third-party guide); first-party page says 'a few free links, hashes, and containers per day' [2]
- limits note: Free accounts are also throttled on debrid resolving through Orion during high demand; resolving with the app's own debrid code is not affected. Paid plans: cheapest $0.50 per month for 1000 daily links, Unlimited $199 once (third-party guides; the panel's own price list is rendered by script and was not read).
- binding note: The daily link, hash and container counts decide how many titles a free account can look up; no byte quota applies because no bytes are served.
- interface detail: JSON API at api.orionoid.com with an app key and a user key, or an authentication token, per the developer documentation; a debrid-support endpoint reports which hosters and networks each debrid service handles.
- endpoint: https://panel.orionoid.com/developers/api
- tooling: Integrated into Kodi addons (Gaia, Seren, Open), Wako, Weyd, Syncler and a Stremio addon, per the home page. A custom app key is free on request after login.
- composes with: Query Orion for torrent, usenet or hoster links, then hand the chosen link to a hosted debrid service (Real-Debrid, AllDebrid, Debrid-Link, TorBox, Premiumize, Offcloud, EasyDebrid, Debrider) or to a torrent client.
- reliability: The database is community-submitted: 'Orion does not guarantee reliable data', and the service states it cannot guarantee uptime and gives no refunds for downtime.
- notes: Not a retrieval path on its own: it finds links, and the bytes need a debrid service or a torrent client. Named by the Kodi guide at firestick.io as an addon source beside Real-Debrid. Free-account use needs a hosted debrid service or a torrent client behind it.
- evidence note: The first-party home page and terms were read on 2026-11-03 and establish that it is an index, that free accounts exist and what registration needs; the numeric free limit and paid prices rest on third-party guides.
- extras:
  - free_links_per_day: 100
  - cheapest_paid_usd_month: 0.5
  - lifetime_usd: 199
- evidence:
  - [1] 2026-11-03: Orion is a link index, not a store or a downloader: no per-object cap or byte egress applies | capture: sha256:9692edbcfc6160857aad3051057c6aa63f5363596fe15662a48f145691c13370 | quote: Orion is not a debird service, it does not host or distribute any files.
  - [1] 2026-11-03: a free tier exists with a small unnumbered daily allowance | capture: sha256:9692edbcfc6160857aad3051057c6aa63f5363596fe15662a48f145691c13370 | quote: Yes, we offer free accounts. Once you registered a new account, you will have a few free links, hashes, and containers per day.
  - [1] 2026-11-03: registration needs only an email address or a username | capture: sha256:9692edbcfc6160857aad3051057c6aa63f5363596fe15662a48f145691c13370 | quote: We only require your email address or username in order to create an account.
  - [1] 2026-11-03: free accounts are throttled on debrid resolving through Orion | capture: sha256:9692edbcfc6160857aad3051057c6aa63f5363596fe15662a48f145691c13370 | quote: Orion will limit the number of debrid resolvings that free accounts can make during times of high demand.
  - [2] 2026-11-03: free limit of 100 links per day; cheapest paid plan $0.50 per month (third party) | capture: sha256:0c94cfc1168bc13a1fb2273138983d205000cca004c588f6bfa8520452037368 | quote: If you are using Orion for free, you have a limit of 100 links per day. Their cheapest plan is $0.50 / month for 1000 daily links.
  - [3] 2026-11-03: a second third-party source for the cheapest paid tier at $0.50 per month | capture: sha256:ef332bc29112c2ff95433b5192007f7897d9fd262f5607974e900b8f53d55e3b | quote: Novice ($0.50/month)
- sources:
  - [1] https://orionoid.com/
  - [2] https://guides.viren070.me/stremio/addons/orion-stremio-addon
  - [3] https://troypoint.com/orion/
