# Stremio Addons

> stremio-addons.net | Debrid; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stremio-addons/ | JSON https://fshy.ajam.dev/api/v1/entity/stremio-addons.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Aradeb (Arabic Contents Addon)

- `debrid/aradeb` | qualifies-with-caveat | evidence documented | binding write-gated | category Stremio addon (Arabic catalogs + private-tracker streams resolved through the user's own Real-Debrid or TorBox account) | tier addon
- needs card no, phone no, ID no, institution no | verified 2026-11-25T22:12:34.246Z (live) | stale on 2026-12-26
- url https://stremio-addons.net/addons/aradeb
- price USD 0 for the addon; the Real-Debrid or TorBox subscription is the cost
- free tier: Trial keys are issued by the Discord bot and are valid for 90 days; permanent keys are available to donors only and currently do not expire. | unit: mixed | metered on: none | read on: 2026-10-23 | source: [1] | note: The byte volume is not the addon's: it is whatever the user's own debrid subscription allows.
- per-object cap: not applicable: the addon returns streams; the file size ceiling is the linked debrid account's. | source: [1]
- retention: not applicable: nothing is stored by the addon; cache retention is the debrid provider's. | source: [1]
- egress: Discovery uses the user's own paid Debrid service with TorBox, AllDebrid, Premiumize or Real-Debrid; quality and availability depend on sources and the user's paid Debrid provider; Real-Debrid support is being phased out and TorBox or AllDebrid is recommended. | metered: no | source: [1]
- identity: email | detail: A Discord account is required to reach the bot that issues keys; Discord signup itself takes an email. The addon has no separate registration.
- interface: rest
- limits:
  - write-gated (binding): keys are issued by a Discord bot (90-day trials) and permanent access is donation-gated [1]
- limits note: The listing warns the addon 'will not work properly unless it is installed correctly as explained in the Discord server', so the install channel is part of the access condition.
- binding note: No byte quota of its own exists; access is gated by a key that a human issues, and the key can expire while the debrid bill keeps running.
- interface detail: A Stremio addon endpoint configured at https://aradeb.518878.xyz; the Stremio client calls it over HTTP. Installation is via the Discord setup guide; donation and key requests are handled through the configuration page and a Discord support ticket.
- tooling: Stremio desktop and mobile; a Discord bot for keys; no CLI and no API documentation beyond the addon protocol.
- composes with: It is the Arabic-language layer on top of a global debrid subscription: the addon supplies Arabic, Arabic-dubbed and Turkish catalogs, the user's paid debrid account supplies the bytes, and no regional service is bought.
- reliability: Two dependencies must both hold: the debrid account's cache and the private trackers the addon queries. A trial key expires at 90 days, and permanent keys depend on a donation, so the addon can stop resolving for a user who is still paying a debrid subscription.
- notes: This is the clearest evidence that the Arabic market consumes retrieval through a global service rather than a local one: the local layer is an addon, and the paid account is Real-Debrid or TorBox. A separate 'Arab debrid service' was searched for and not found (see findings.md).
- evidence note: The feature list, the 90-day trial, the donor gating and the 4K claim were read on the addon's directory entry. What would raise it: an installed addon returning a playable stream.
- evidence:
  - [1] 2026-10-23: Arabic catalogs, Latin and Arabic search, streams 'provided through your paid Real-Debrid or TorBox account' up to 4K, 90-day trial keys via a Discord bot, permanent keys for donors only, configure page aradeb.518878.xyz
  - [1] 2026-11-25: the addon now names four supported debrid providers and phases out Real-Debrid | capture: sha256:7959bb23c4cdabda0e6919398f3f3dbc1ec9f8c9ffd8dbf9edb0f0d26397b590 | quote: - Discover content using TorBox, AllDebrid, Premiumize, or Real-Debrid. - Quality and availability depend on sources and your paid Debrid provider. *Note: Real-Debrid support is being phased out. TorBox or AllDebrid is recommended.*
  - [1] 2026-11-25: permanent keys are requested through the configuration page and a Discord support ticket | capture: sha256:7959bb23c4cdabda0e6919398f3f3dbc1ec9f8c9ffd8dbf9edb0f0d26397b590 | quote: - Donate through the configuration page and request your key via a Discord support ticket.
  - [1] 2026-11-25: the addon's catalogs cover Arabic, Arabic-dubbed and Turkish titles | capture: sha256:7959bb23c4cdabda0e6919398f3f3dbc1ec9f8c9ffd8dbf9edb0f0d26397b590 | quote: Aradeb is a Stremio addon for discovering Arabic, Arabic-dubbed, and Turkish movies and series in up to 4K, using your own paid Debrid service.
  - [1] 2026-11-25: the listing describes Aradeb as a Stremio addon | capture: sha256:7959bb23c4cdabda0e6919398f3f3dbc1ec9f8c9ffd8dbf9edb0f0d26397b590 | quote: Aradeb is a Stremio addon for discovering Arabic, Arabic-dubbed, and Turkish movies and series in up to 4K, using your own paid Debrid service.
  - [1] 2026-11-25: the listing names four debrid providers, ties availability to the user's paid Debrid provider, phases out Real-Debrid and recommends TorBox or AllDebrid | capture: sha256:7959bb23c4cdabda0e6919398f3f3dbc1ec9f8c9ffd8dbf9edb0f0d26397b590 | quote: using your own paid Debrid service. ... - Discover content using TorBox, AllDebrid, Premiumize, or Real-Debrid. - Quality and availability depend on sources and your paid Debrid provider. *Note: Real-Debrid support is being phased out. TorBox or AllDebrid is recommended.*
  - [1] 2026-11-25: the egress statement still names four debrid providers, ties availability to the user's paid Debrid provider and phases out Real-Debrid | capture: sha256:7959bb23c4cdabda0e6919398f3f3dbc1ec9f8c9ffd8dbf9edb0f0d26397b590 | quote: using your own paid Debrid service. ... - Discover content using TorBox, AllDebrid, Premiumize, or Real-Debrid. - Quality and availability depend on sources and your paid Debrid provider. *Note: Real-Debrid support is being phased out. TorBox or AllDebrid is recommended.*
- sources:
  - [1] https://stremio-addons.net/addons/aradeb

## Stremio Addons

- `debrid/stremio-addons-net` | qualifies-with-caveat | evidence documented | binding none | category addon directory for Stremio (curated list, HTML only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
- url https://stremio-addons.net/
- price USD 0
- free tier: The directory is free to browse with no account. /api/addons returns 404, so there is no machine-readable feed. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: a directory of addon manifests | source: [1]
- retention: listings persist while the addon is maintained; the front page sorts by new, recently updated, top rising and popular | source: [2]
- egress: no byte allowance: the directory links to each addon's own manifest host | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account to read; saving favourites is the only feature the site ties to a sign-in.
- interface: browser
- limits:
  - request-rate: none published; the listing pages answered normally with no 429 [2]
- limits note: No API means no documented quota; the constraint is that enumeration is HTML parsing.
- binding note: Nothing here is metered and no rate was observed; the directory is a discovery surface, not a data source a client would poll.
- interface detail: HTML only: /api/addons 404s and there is no documented JSON endpoint. The addon pages carry an install URL, which is the only machine-usable artefact.
- tooling: A browser, or a scraper over the listing pages; the install URL per addon is a plain stremio:// or https manifest link that a client can consume directly.
- composes with: Use it to enumerate candidate addons, then install the two or three that matter and let AIOStreams collapse them into one request per title.
- reliability: unverified: no literal field value was readable on 2026-11-26; a read-only probe of /api/addons recorded status 404, so the listed fields stay interpretive
- notes: Community addon directory for Stremio indexing streaming resolvers and debrid integrations. No programmatic path found: HTML only: /api/addons 404s and there is no documented JSON endpoint. The addon pages carry an install URL, which is the only machine-usable artefact.
- evidence note: The home page and one sorted listing were read on 2026-10-23, and /api/addons was probed and 404d. A scrape of the full listing confirms how many entries it carries.
- extras:
  - sponsored_placements: yes
- evidence:
  - [1] 2026-10-23: 'Community curated Stremio addons list', new/recently updated/top rising/popular sections, and two sponsored placements above the fold
  - [3] 2026-10-23: HTTP 404, so no JSON API is served at the obvious path
  - probe:https://stremio-addons.net/api/addons 2026-11-26: the endpoint answered HTTP 404 on 2026-11-26 | capture: sha256:2536ee2a42d1cbb153812e42d9473ca46563a026fc6327dcbe3e97ecba05fc33 | quote: "status": 404
- sources:
  - [1] https://stremio-addons.net/
  - [2] https://stremio-addons.net/addons?sort=new
  - [3] https://stremio-addons.net/api/addons
