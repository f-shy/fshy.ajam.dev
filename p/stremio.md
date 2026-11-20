# Stremio Web

> stremio.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stremio/ | JSON https://fshy.ajam.dev/api/v1/entity/stremio.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Stremio Web

- `debrid/stremio-web` | qualifies | evidence documented | binding none | category free hosted web client for Stremio addons; no install, no local server | tier web
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://web.stremio.com/
- price USD 0
- free tier: Free, no payment and no install: the app is served from the browser at web.stremio.com. It does require a Stremio account - the vendor's own walkthrough for iOS opens with 'logging in to Stremio Web' and syncing addons through that account. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: a client, not a store | source: [1]
- retention: not applicable: the addon list and library live in the Stremio account, not on the local device | source: [1]
- egress: Stremio does not meter the user. The bytes come from wherever the addon points - the debrid provider or the source host - so no allowance exists at this layer. | metered: no | free allowance: unlimited | source: [2]
- identity: email | detail: A Stremio account is required to hold addons and library, which the vendor's own guide treats as step one ('logging in to Stremio Web'). No card and no phone. | country: None
- interface: rest
- limits:
  - request-rate: no published limit on the web client itself; every limit met here belongs to the installed addon [2]
- limits note: The real limit is a capability gap, not a counter: without a local Stremio Service there is no torrent streaming and no in-browser conversion, so a P2P result set is unplayable in the browser even though it renders in the list.
- binding note: Nothing at the Stremio layer counts bytes or requests; the constraints that fail at 1 TiB/month are governed by the addon (rate limit) and the debrid provider (per-object or traffic cap).
- interface detail: A single-page web app (10,759-byte HTML shell titled 'Stremio - Freedom to Stream') that speaks the Stremio addon protocol to whatever manifests the account has installed. PWA-installable in Safari for iOS/iPadOS.
- tooling: runs in the browser. Its missing half is Stremio Service, the local daemon: 'Stremio Web will still not be fully featured without connecting it to Stremio Service ... some missing features include: converting videos to support the browser, torrent streaming, etc'.
- composes with: The free front end for the whole pipeline: install Torrentio/Comet/MediaFusion/AIOStreams manifest URLs into the account, and a debrid key inside one of them turns Stremio Web into a player that needs no local machine.
- reliability: The vendor's help centre still answers 'Can I run Stremio in my browser?' with 'Not at the moment, but this is coming!' (updated 2026-09-03) while the web app is live and documented on their own blog - the support page is stale, not the product.
- notes: This is the piece that makes the free floor a real floor: a browser tab replaces the user and the media player. What it cannot replace is Stremio Service, and that daemon is what a P2P-only stack needs - so in practice Stremio Web forces the debrid key rather than removing the need for one.
- evidence note: The HTML shell, the vendor blog walkthrough and the help-centre answer were read. Not measured: an actual account login and playback, which needs an account the session did not create.
- extras:
  - service_daemon: https://github.com/Stremio/stremio-service
  - web_app_repo: https://github.com/Stremio/stremio-web
  - install_shape: PWA in Safari on iOS; ordinary tab elsewhere
- evidence:
  - [2] 2026-10-23: HTTP 200, 10,759 bytes of HTML, title 'Stremio - Freedom to Stream' - the app is served, not a landing page
  - [1] 2026-10-23: 'Stremio Web will still not be fully featured without connecting it to Stremio Service', 'torrent streams will still not work, but all other streams will be opened with an external video player', the external-player setting, and that a login is required
  - [3] 2026-10-23: the stale official answer 'Not at the moment, but this is coming!', in a 19,387-byte page dated 2026-09-03 - the support article contradicts the vendor's own live web app
- sources:
  - [1] https://blog.stremio.com/using-stremio-web-on-iphone-ipad/
  - [2] https://web.stremio.com/
  - [3] https://stremio.zendesk.com/hc/en-us/articles/360000281532-Can-I-run-Stremio-in-my-browser
