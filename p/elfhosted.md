# ElfHosted

> elfhosted.com | Debrid; 8 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/elfhosted/ | JSON https://fshy.ajam.dev/api/v1/entity/elfhosted.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## StremThru (ElfHosted public instance)

- `debrid/stremthru-elfhosted` | qualifies | evidence documented | binding request-rate | category hosted debrid proxy and companion API for Stremio addons | tier public instance
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://stremthru.elfhosted.com/
- price USD 0
- free tier: Free and accountless: 'This is the public instance of StremThru, sponsored by ElfHosted. Reasonable rate limits apply so it stays fast for everyone.' Served version string 'StremThru v0.105.3'. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: a request proxy, not a store | source: [1]
- retention: not applicable; the proxy holds no library | source: [1]
- egress: Not metered and no figure published. It proxies addon requests, so the bytes it forwards are metadata and link resolution, not video. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: No account to use the public instance. The debrid credentials it proxies are the account's own. | country: None
- interface: rest
- limits:
  - request-rate (binding): unpublished 'reasonable rate limits' on the shared public instance [1]
- limits note: The page publishes no limit figure and no endpoint documentation in the rendered text; the service's API surface was not enumerated.
- binding note: It carries no bytes of its own, so the only thing that can fail first is the shared request rate on the sponsor's instance.
- interface detail: HTTP service titled 'Companion for Stremio'; it sits behind an addon (AIOStreams or Torrentio-style) and forwards store requests through one IP.
- tooling: no install on the public instance; the base URL is pasted into the addon that uses it. Self-hosting is possible but not needed, which is why it is here.
- composes with: The piece that hides the caller's IP from the debrid provider: one exit IP for every addon call, which is what avoids the multi-IP bans Real-Debrid applies to shared or rotating addresses.
- reliability: One sponsor, one instance: if ElfHosted retires it, the addon that depends on it loses its exit IP. Version drifted to v0.105.3, so the public instance tracks upstream closely.
- notes: Cheapest working answer to the multi-IP problem found: the paid version is bundled only, never sold alone at a published price, so a client who needs a stable exit IP either buys the USD 9 bundle or accepts the shared instance's rate limit.
- evidence note: The landing page was read (HTTP 200, 31 words, version string). No request was proxied through it - doing so needs a debrid key - so whether the rate limit bites at 1 TiB/month is unknown.
- extras:
  - version: v0.105.3
  - sponsor: ElfHosted
- evidence:
  - [1] 2026-10-23: HTTP 200: 'StremThru v0.105.3', 'Companion for Stremio', 'This is the public instance of StremThru, sponsored by ElfHosted ❤️. Reasonable rate limits apply so it stays fast for everyone.'
  - [2] 2026-10-23: the paid pairing, USD 9.00 / month: 'Your own private AIOStreams addon with a StremThru instance alongside, so your streams reach every device through your own proxy'
- sources:
  - [1] https://stremthru.elfhosted.com/
  - [2] https://store.elfhosted.com/product/aiostreams-stremthru/

## AIOStreams (ElfHosted public instance)

- `debrid/aiostreams-elfhosted` | qualifies-with-caveat | evidence documented | binding request-rate | category hosted Stremio addon aggregator (combines other addons, filters and sorts, debrid-aware) | tier public instance
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://aiostreams.elfhosted.com/stremio/configure
- price USD 0
- free tier: Free, no account to install: 'Use AIOStreams without hosting it yourself via community-run public instances.' On the ElfHosted instance, 'The most stable option due to being a professional service, but the public instance forcefully excludes P2P, HTTP, and Live stream types.' | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The public instance is deliberately crippled by stream type, not only by rate, which is the opposite of what a free aggregator is wanted for.
- per-object cap: not applicable: the addon aggregates stream descriptors | source: [1]
- retention: not applicable: configuration lives in the browser and the URL; the public instance stores nothing | source: [2]
- egress: No byte allowance published. Proxying is a paid feature ('4K MediaFlow-Proxy'); the public instance returns links only. | metered: no | free allowance: not published | source: [2]
- identity: anonymous | detail: Nothing to install. A debrid key is required to resolve cached streams, and the instance does not log it. | country: None
- interface: rest
- limits:
  - request-rate (binding): the instance's own notice says 'Reasonable rate limits apply so it stays fast for everyone'; the number is unpublished and the notice was read through a search index, not from the served HTML [2]
- limits note: Stream-type exclusion is a second, harder limit that is not a counter: P2P, HTTP and Live results are removed outright on this instance per the official docs. Community instances that do allow them exist (aiostreams.fortheweak.cloud, aiostreams.stremiofr.com, aiostreams.stremio.ru) but were not read, and the 'does not log API keys' reassurance belongs to the stremio.ru instance's notice, not to ElfHosted's.
- binding note: Byte volume never reaches the instance - it returns links - so the first wall is the per-caller request limit, with the stream-type filter removing whole result classes before that.
- interface detail: A configure wizard at /stremio/configure that emits a per-user manifest URL (config encoded in the path), plus a PWA manifest at /manifest.json for the standalone web app. The configure page is a 1,034-byte single-page-app shell, so nothing on it can be read from the HTML: its text was only visible through a search index's rendering, which is where 'Reasonable rate limits apply so it stays fast for everyone' and the Torrentio/AnimeKitsu notice come from.
- tooling: no install: configure in the browser, copy the generated manifest into Stremio. Also ships a browser front end so Stremio itself is optional ('Watch without Stremio').
- composes with: The aggregator layer: it folds Torrentio, Comet, MediaFusion and others into one list with shared filters, so a client with several addons configures one URL. Needs at least one underlying addon and, for cached playback, a debrid key.
- reliability: Public instances are community-run and change: the official docs list only the ElfHosted one and point at a third-party uptime page for the rest. Stream-type filtering differs per instance, so results are not portable between them.
- notes: The Torrentio ban matters for a free-only client: Torrentio is the addon with the best public hit rate, and this instance disables it 'respecting the Torrentio developer's request'. So the free aggregator is the free addon minus the best free source.
- evidence note: The official docs page (read) and the served shell (measured) are the load-bearing sources. The rate-limit sentence and the Torrentio removal come from a search index's rendering of a page that renders client-side, so they are reported rather than read. A configured stream call confirms both and needs a debrid key.
- extras:
  - other_instances_seen: aiostreams.fortheweak.cloud, aiostreams-nightly.fortheweak.cloud, aiostreams.stremiofr.com, aiostreams.stremio.ru, aiostreams.elfhosted.com
  - status_page: https://uptime.ibbylabs.dev/
  - disabled_here: Torrentio, AnimeKitsu (per the configure page)
- evidence:
  - [2] 2026-10-23: HTTP 200, 1,034 bytes: a single-page-app shell titled 'AIOStreams' with an empty root div and three script tags. It proves the route is served and proves nothing about the text on it.
  - [3] 2026-10-23: HTTP 200, 725 bytes: the PWA manifest (name 'AIOStreams', short_name 'AIO', icons), not a Stremio addon manifest - the addon manifest is the per-user URL the wizard generates
  - [1] 2026-10-23: 'There are several public instances run by the community'; ElfHosted's 'forcefully excludes P2P, HTTP, and Live stream types'; the Stable/Nightly channels; the uptime.ibbylabs.dev status page
  - [4] 2026-10-23: the paid tier: 'Your own private AIOStreams addon with a StremThru instance alongside', USD 9.00 / month
- sources:
  - [1] https://docs.aiostreams.viren070.me/getting-started/public-instances/
  - [2] https://aiostreams.elfhosted.com/stremio/configure
  - [3] https://aiostreams.elfhosted.com/manifest.json
  - [4] https://store.elfhosted.com/product/aiostreams-stremthru/

## Comet (ElfHosted public instance)

- `debrid/comet-elfhosted` | qualifies-with-caveat | evidence documented | binding request-rate | category hosted Stremio addon, torrent and debrid search with key passthrough | tier public instance
- needs card no, phone no, ID no, institution no | verified 2026-10-30T13:11:55.961Z (live) | stale on 2026-11-30
- url https://comet.elfhosted.com/configure
- price USD 0
- free tier: Free, no account, no install: the manifest at /manifest.json is served with 'configurationRequired: false' and describes the instance as 'Stremio's fastest torrent/debrid search add-on' (Comet | ElfHosted). 'This is the public instance of Comet, sponsored by ElfHosted ... Reasonable rate limits apply so it stays fast for everyone.' | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The rate limit is not published as a number; the page says only 'reasonable'. The paid instance is sold as the fix, at 10x.
- per-object cap: not applicable: results are stream descriptors, not stored objects | source: [2]
- retention: not applicable: nothing is stored for the caller on the public instance | source: [2]
- egress: Not metered to the caller: the instance returns links and, if proxying is enabled, streams through ElfHosted's IP. The public instance publishes no bandwidth figure and sells none. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: Nothing to register to install the addon. A debrid account (email plus card at Real-Debrid, TorBox or similar) is required only for cached playback. | country: None
- interface: rest
- limits:
  - request-rate (binding): unpublished 'reasonable rate limits' on the shared public instance [1]
- limits note: A debrid key is optional for the addon but load-bearing for the result: without one Comet returns torrents that must be streamed peer-to-peer, which Stremio Web cannot do without a local Stremio Service.
- binding note: No byte counter exists on the public instance; the only cap the vendor names is the shared rate limit, and the paid tier is sold as 10x that.
- interface detail: Stremio addon protocol over HTTPS: GET /manifest.json, GET /{config}/stream/{type}/{id}.json. Configure page renders quality filters, 'Add Debrid Service', 'Show Cached Only', 'Scrape Debrid Account Torrents' and an Install button that pushes the addon into Stremio.
- tooling: works from Stremio Web or any Stremio client with no local server; no addon-side install and no key needed to browse, a debrid key needed to resolve cached streams.
- composes with: Sits between Stremio (or AIOStreams as an aggregator) and the debrid account; pairs with a bundled ElfHosted proxy to hide the caller's IP from the debrid provider.
- reliability: Shared instance: rate limits, and the vendor states 'Shared instances can't stream Usenet'. A 403 was returned for an unconfigured /stream/ call, so the bare default path is not usable without building a config first.
- notes: Comet is the strongest free front-door found that is still alive: manifest served, configure page live, no account. Its two failures are the 403 on the unconfigured path and the absence of any way to stream peer-to-peer from a browser, which pushes the setup back to a debrid key.
- evidence note: The manifest was fetched and an unconfigured stream call was made and returned 403; the configure page was read. What was not measured is a full configured stream with a real debrid key, which needs a paid account. Documented without probe digest: no probe record with status, bytes and digest exists.
- extras:
  - endpoint: https://comet.elfhosted.com
  - paid_upgrade: https://store.elfhosted.com/product/comet/ - USD 9/month, 7-day trial at USD 1
  - proxy: paid variants bundle MediaFlow-Proxy on the vendor IP
- evidence:
  - [2] 2026-10-23: HTTP 200, 549 bytes of JSON: id comet.elfhosted.com, version 2.0.0, 'Stremio's fastest torrent/debrid search add-on', behaviorHints.configurationRequired=false
  - [3] 2026-10-23: 
  - [1] 2026-10-23: 'This is the public instance of Comet, sponsored by ElfHosted ... Reasonable rate limits apply', the debrid field, and 'Try it for $1, 7 days, cancel anytime. ($9/mo after.)'
  - probe:https://comet.elfhosted.com/stream/movie/tt1254207.json 2026-10-30: a GET of the unconfigured stream path /stream/movie/tt1254207.json answered HTTP 403 with a 9-byte body on 2026-10-30 | capture: sha256:2f07d03fd2ad59aea7a04e075ea52d065bd3ae79fdfc5c9211aba968aca1af34 | quote: "status": 403
- sources:
  - [1] https://comet.elfhosted.com/configure
  - [2] https://comet.elfhosted.com/manifest.json
  - [3] https://comet.elfhosted.com/stream/movie/tt1254207.json

## MediaFusion (ElfHosted public instance)

- `debrid/mediafusion-elfhosted` | qualifies-with-caveat | evidence documented | binding request-rate | category hosted Stremio addon, universal torrent/debrid scrapers with live-TV and catalog resources | tier public instance
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://mediafusion.elfhosted.com/
- price USD 0
- free tier: Free and accountless, but the public instance answered an anonymous stream request with a single placeholder stream titled 'MediaFusion public rate-limit exceeded 🐢'. The manifest itself claims 'configurationRequired: false'. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The rate limit is enforced per caller and silently replaces results with one link to a video explaining the limit (https://elfhosted.com/assets/public-rate-limit-exceeded.mp4).
- per-object cap: not applicable: stream descriptors, not objects | source: [2]
- retention: not applicable: the public instance stores nothing for the caller | source: [2]
- egress: Not metered; no bandwidth figure published. Playback is direct from the debrid provider or the source site, not proxied on the free instance. | metered: no | free allowance: not published | source: [3]
- identity: anonymous | detail: Nothing to install the addon. A debrid account is required for cached playback. | country: None
- interface: rest
- limits:
  - request-rate (binding): per-caller public rate limit, enforced; the number is not published and the over-limit response is a single placeholder stream [1]
- limits note: Because the over-limit response is a well-formed 200 with one stream, a client cannot tell a throttled instance from an empty result except by reading the title text.
- binding note: The limit fires before any byte is transferred and it fired on the first anonymous request of on 2026-10-23, which makes it the binding constraint by a wide margin.
- interface detail: Stremio addon protocol: resources include catalog, stream (types movie, series, tv, events; idPrefixes tt, tmdb:, tvdb:, mal:, mf, dl) and meta. Contact address published as abuse@elfhosted.com.
- tooling: no install; add the manifest URL to Stremio. Requires the account's own debrid key for cached playback, and a MediaFlow proxy for household-wide sharing on the paid tier.
- composes with: The broadest scraper of the free hosted addons found - it carries catalogs and live events, not just streams - so it can stand alone as a Stremio front end without AIOStreams in front of it.
- reliability: Throttling is the normal state, not an error: the first anonymous call returned the rate-limit placeholder. The vendor sells a private instance as the fix.
- notes: This is the clearest evidence found that a free hosted endpoint can be alive and useless at the same time: HTTP 200, valid JSON, schema-correct streams, zero content. Any measurement that only checked status or manifest would have scored it as working.
- evidence note: Manifest fetched (669 bytes, HTTP 200) and a stream call made and read. Not measured: a configured instance with a debrid key, and whether the public limit resets hourly or daily. Documented without probe digest: no probe record with status, bytes and digest exists.
- extras:
  - endpoint: https://mediafusion.elfhosted.com
  - rate_limit_video: https://elfhosted.com/assets/public-rate-limit-exceeded.mp4
  - paid_upgrade: https://store.elfhosted.com/product/mediafusion/ and /product/mediafusion-mediaflowproxy/, USD 9/month
- evidence:
  - [2] 2026-10-23: HTTP 200, 669 bytes: id 'stremio.addons.mediafusion|elfhosted', name 'MediaFusion | ElfHosted', resources catalog/stream/meta/events, contactEmail abuse@elfhosted.com
  - [1] 2026-10-23: HTTP 200 with exactly one stream: name '[🐢] MediaFusion', title 'MediaFusion public rate-limit exceeded 🐢', url https://elfhosted.com/assets/public-rate-limit-exceeded.mp4
  - [4] 2026-10-23: the paid escape: 'Your own private MediaFusion addon for Stremio, bundled with a MediaFlow Proxy so the whole household can stream from one debrid account', USD 9.00 / month
- sources:
  - [1] https://mediafusion.elfhosted.com/stream/movie/tt1254207.json
  - [2] https://mediafusion.elfhosted.com/manifest.json
  - [3] https://mediafusion.elfhosted.com/
  - [4] https://store.elfhosted.com/product/mediafusion-mediaflowproxy/

## ElfHosted - Personal Media Stack

- `debrid/elfhosted-personal-media-stack` | paid-only | evidence documented | binding none | category managed media server plus *arr automation, hosted (no client hardware) | tier personal-media-stack (Zurgling USD 24 to Nazgul USD 199)
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://store.elfhosted.com/product-category/personal-stacks/personal-media-stacks/
- free tier: No free tier. The cheapest listed media stack is 'Zurgling - Personal Media Streamer [2xHD / 1x4K, contended, manual] USD 24.00 / month'; Starter (USD 29) and JellyGoblin (USD 24) both render 'Sold out' on the category page. The storefront advertises '7-day trials for $1' site-wide, but the Hobbit product page carries only 'Billing term Monthly' and no trial line, so a trial on a stack is not confirmed. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The home page says 'Build a Personal Stack ... From $19/m'; the only USD 19 item in the personal-stacks range is Tubeling, a YouTube archiver, so the real media-stack floor is USD 24.
- per-object cap: not applicable: the vendor sells apps and streams, not stored objects. 'Library storage: via your chosen provider - not stored on ElfHosted' | source: [2]
- retention: not applicable to ElfHosted: media is held by the debrid or Usenet account behind it, so retention is that provider's policy, not the host's | source: [2]
- egress: No byte allowance is published anywhere in the stack range. What is sold instead is concurrent playback: '4xHD or 2x4K' on Hobbit, 2xHD/1x4K on Zurgling, 8xHD/4x4K on Ranger, 16xHD/8x4K on Halfling. 'No storage limits ... you're never paying us for terabytes.' | metered: no | free allowance: none published | source: [2]
- identity: card | detail: A paid order: ElfHosted account plus a payment method. No identity document. Plex and Emby variations add their own requirement downstream - 'remote streaming requires a PlexPass' or 'Emby Premiere' - while the Jellyfin and Remux variations need no extra subscription. | country: None
- interface: rest
- limits note: Concurrent-stream caps are the real ceiling and the seven-kind vocabulary has no name for them: 2xHD/1x4K (Zurgling, Starter), 4xHD/2x4K (Hobbit, JellyGoblin Pro), 8xHD/4x4K (Ranger), 16xHD/8x4K (Halfling, Nazgul, the last on dedicated hardware). 'Hardware transcoding up to 1080p' on Hobbit. Remux variation is 'Direct play only'.
- binding note: Nothing in the vocabulary fails at 1 TiB/month because the host carries no bytes: the library sits in the debrid account, and the constraint sold is stream count plus tier capacity, which the vocabulary cannot name. The thing that actually fails is availability, not a counter: two of the nine stack products were 'Sold out' on the read date.
- interface detail: Plex, Emby, Jellyfin or Remux as the player; each exposes its own HTTP API. Radarr/Sonarr, Prowlarr, Seerr and Rclone are provisioned alongside. SSO through the ElfHosted account and HTTPS on a vendor subdomain.
- tooling: nothing to install: the stack is provisioned at checkout from three dropdowns (media player, automation, storage provider). No rclone mount, no Docker, no VPS, no reverse proxy. A debrid or Usenet account is still needed except where a TorBox or NzbDAV variation bundles one.
- composes with: The hosted replacement for Zurg + Rclone + Plex on a home box: debrid/Usenet holds the bytes, ElfHosted runs the *arr half, and playback is through Plex/Jellyfin apps from any device.
- reliability: Capacity is spot-sold and disappears: Starter and JellyGoblin showed 'Sold out' on the category page. Switching media player, automation or storage provider later 'requires reprovisioning that part of the stack'. One review-tracked tier range, no published uptime figure.
- notes: This is the only hosted product found that sells the *arr half without selling storage, so its price is comparable to nothing in the storage topic: USD 24 buys 2 concurrent streams and the app stack, and 0 TB. EZ-Homelab's bundle (USD 29, Plex+Jellyfin+8 apps) is the nearer competitor and is recorded separately.
- evidence note: Nine product cards priced on one category page plus the full Hobbit product page read. A purchase would raise it to measured; nothing was bought, so lead times, provisioning failures and actual stream quality are untested.
- extras:
  - tier_table_usd_month: Zurgling 24, JellyGoblin 24, Starter 29, Hobbit 39, JellyGoblin Pro 39, Ranger 59, Halfling 109, Nazgul 199
  - stream_capacity: Zurgling/Starter/JellyGoblin 2xHD-1x4K; Hobbit/JellyGoblin Pro 4xHD-2x4K; Ranger 8xHD-4x4K; Halfling/Nazgul 16xHD-8x4K
  - bundled_accounts: TorBox variations include a TorBox Essential account; NzbDAV variations include a Usenet/NNTP account; RealDebrid variation is BYO
  - billing_terms: Hobbit: monthly only. Add-on products: 3/6/12-month terms at 5/10/20 percent off
- evidence:
  - [1] 2026-10-23: the nine tiers and their prices: Zurgling USD 24, JellyGoblin USD 24, Starter USD 29, Hobbit USD 39, JellyGoblin Pro USD 39, Ranger USD 59, Halfling USD 109, Nazgul USD 199, Tubeling USD 19; and the 'Sold out' state on Starter and JellyGoblin
  - [2] 2026-10-23: the variation set (Plex/Emby/Jellyfin/Remux; Radarr-Sonarr/Seerrbridge/AIOStreams; RealDebrid/TorBox/Debridge/NzbDAV), 'No storage limits', 'Library storage: via your chosen provider', PlexPass for remote streaming and none for Jellyfin, 'Billing term Monthly' with no trial line
  - [3] 2026-10-23: the storefront claim 'From $19/m' for a personal stack and '7-day trials for $1'
- sources:
  - [1] https://store.elfhosted.com/product-category/personal-stacks/personal-media-stacks/
  - [2] https://store.elfhosted.com/product/hobbit/
  - [3] https://store.elfhosted.com/

## ElfHosted - Stremio addon subscriptions

- `debrid/elfhosted-stremio-addons` | paid-only | evidence documented | binding request-rate | category managed private Stremio addon instance (debrid key passthrough, optional proxy streaming) | tier per-addon (USD 9) and Stremio Addons Bundle (USD 29)
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://store.elfhosted.com/product-category/stremio-addons/
- free tier: No free tier for a private instance, but a free public instance of each addon exists with lower limits: 'we offer free highly-available hosting for addons, with rate-limits to prevent abuse ... subscription-based instances are also available with 10 x higher rate-limits'. The paid products carry 'Free trial: 7 days' and 'Sign-up fee: $1.00'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The trial is USD 1 down, not free: 'Try it for $1, 7 days, cancel anytime.'
- per-object cap: not applicable: an addon instance, not a stored object | source: [2]
- retention: not applicable: the instance keeps configuration, not media | source: [2]
- egress: Sold by stream, not by byte: the MediaFlow-Proxy booster is priced as bandwidth, 'Adds 256 Mbps of proxy-streaming bandwidth to your MediaFlow Proxy subscription, enough for 4 concurrent HD streams or 2 concurrent 4K streams' at USD 9/month. Base instances include proxying but publish no bitrate figure. | metered: no | free allowance: none published | source: [2]
- identity: card | detail: Store account plus payment. The addon still needs the account's own debrid key, so a debrid subscription is a second gate that ElfHosted does not remove. | country: None
- interface: rest
- limits:
  - request-rate (binding): subscription instances get 10x the public instance's rate limits; the public figure itself is not published [1]
- limits note: Only 10 addons show per page of 51 products, so the full catalogue was not enumerated. Each product is one instance; stacking Comet + MediaFusion + AIOStreams means stacking USD 9 subscriptions unless the USD 29 bundle covers them.
- binding note: At 1 TiB/month nothing byte-based binds - the bytes come from the debrid account - but every request the addon makes is counted against an unpublished rate limit, and that is the limit ElfHosted itself sells the upgrade on ('10x higher rate-limits').
- interface detail: A private instance reachable at its own HTTPS URL, installed in Stremio by pasting the manifest link; SSO protects the configure page. 'Private add-ons with 10x rate limits, plus bundled TorBox and usenet accounts'.
- tooling: none needed client-side: configure in the browser, paste the manifest URL into Stremio Web or the Stremio app. The addon does the scraping and debrid calls server-side, which is what removes the need for a local streaming server.
- composes with: This is the paid upgrade of the free public addons: it adds 10x rate limits, a dedicated IP for proxying ('protect your debrid account from multi-IP bans') and, in some variants, a bundled TorBox Essential or Usenet account.
- reliability: Public instances are shared and rate-limited, and ElfHosted has retired a public instance before when upstream archived the project (WebStreamr, recorded separately). Private instances are sold as the fix for multi-IP debrid bans, so the ban risk is real on the public ones.
- notes: The bundle is the only place the vendor bundles somebody else's debrid capacity: 'Stremio Addons Bundle includes ... bundled third-party TorBox and Usenet provider accounts', and AIOStreams (with TorBox Essential) is USD 9 with the TorBox account inside. That makes USD 9 the cheapest single purchase found that includes both the addon and a debrid subscription, which is the whole pipeline in one line item.
- evidence note: Category and Flex product pages read; the docs page and the public Comet configure page read. Not measured: a purchased private instance, so the '10x rate limits' and dedicted-IP ban protection are the vendor's claims and the public limit figure is unpublished.
- extras:
  - product_prices_usd_month: AIOStreams 9, AIOStreams+Stremthru 9, AIOStreams+MediaFlow 9, AIOStreams+NzbDAV 9, AIOStreams+TorBox 9, MediaFusion+MediaFlow 9, Comet+proxy 9, Usenet Streamer 9, Stremio Addons Bundle 29, MediaFlow 2x4K booster 9, Prowlarr 9, Jackett 9, NZBHydra 9
- evidence:
  - [2] 2026-10-23: 51 products in the category, 10 shown; AIOStreams, AIOStreams+Stremthru, AIOStreams+MediaFlow, AIOStreams+NzbDAV, AIOStreams+TorBox, MediaFusion+MediaFlow, Comet+proxy and Usenet Streamer each 'USD 9.00 / month'; Stremio Addons Bundle 'USD 29.00 / month'; the MediaFlow Proxy 2x4K booster at USD 9 with '256 Mbps ... 4 concurrent HD streams or 2 concurrent 4K'
  - [1] 2026-10-23: 'we offer free highly-available hosting for addons, with rate-limits to prevent abuse' and 'subscription-based instances are also available with 10 x higher rate-limits'
  - [3] 2026-10-23: the public instance's own upgrade pitch: 'Shared instances can't stream Usenet. Private ones can ... Try it for $1, 7 days, cancel anytime. ($9/mo after.)'
  - [4] 2026-10-23: the billing shape these products share: 'USD 9.00 / month', 'Free trial: 7 days', 'Sign-up fee: USD 1.00', 3/6/12-month terms at USD 25.65 / 48.60 / 86.40, and that Flex's own collection excludes the media apps
  - [5] 2026-10-23: reported, not read: a search index shows 'USD 9.00 / month with a 7-day free trial and a $1.00 sign-up fee'
- sources:
  - [1] https://docs.elfhosted.com/stremio-addons/
  - [2] https://store.elfhosted.com/product-category/stremio-addons/
  - [3] https://comet.elfhosted.com/configure
  - [4] https://store.elfhosted.com/product/flex/
  - [5] https://store.elfhosted.com/product/prowlarr/

## ElfHosted managed Prowlarr

- `debrid/elfhosted-prowlarr` | paid-only | evidence documented | binding write-gated | category Hosted indexer aggregator (managed Prowlarr or NZBHydra 2 instance) | tier paid
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://store.elfhosted.com/product/prowlarr/
- free tier: None free beyond a trial: 'USD 9.00 / month', 'Free trial: 7 days', 'Sign-up fee: USD 1.00', with 3/6/12-month terms at USD 25.65, 48.60 and 86.40. NZBHydra 2 is sold the same way. | unit: none | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: an aggregator in front of indexers, not a store of objects | source: [1]
- retention: not applicable: the instance holds configuration, not content | source: [1]
- egress: No byte metering: the aggregator returns pointers from the indexers already held. | metered: no | source: [1]
- identity: card | detail: A paid order with a card and a USD 1 sign-up fee; a 7-day trial is offered first. Indexer accounts are separate and are the account's own.
- interface: rest
- limits:
  - write-gated (binding): paid app slot: USD 9/month after a 7-day trial and a USD 1 sign-up fee [1]
- binding note: Payment is the gate: the instance does not start without a plan. Nothing in the seven-kind vocabulary describes a subscription, so write-gated is used for the access gate and the price is carried in extras.
- interface detail: A running Prowlarr or NZBHydra 2 served over HTTPS at a private link per user: 'On ElfHosted, it comes pre-configured and connected to your other apps.' The aggregator software itself is unchanged, so it speaks the same Newznab and Torznab API to the user.
- endpoint: https://<instance>.elfhosted.com (per-user)
- tooling: Prowlarr and NZBHydra 2 are the tools; this is only a managed host for them. A client still supplies its own indexer accounts, so the aggregator does not remove the identity cost of any indexer.
- composes with: Replaces a container that would otherwise be run: USD 9/month buys a running Prowlarr with no Docker, no reverse proxy and no TLS, and it then fans out to whatever indexers are held.
- reliability: A managed instance is somebody else's uptime: the aggregator going down stops every indexer at once, which a local install would not.
- notes: Hosted deployment of Prowlarr indexer aggregator. The software provides standard Newznab and Torznab endpoints over HTTPS.
- evidence note: The price, trial and sign-up fee were read on the vendor's own product page. The NZBHydra 2 product was seen in search results but its page was not opened.
- extras:
  - price: USD 9/month (USD 86.40/year)
  - software: Prowlarr / NZBHydra 2, managed
  - note: this is not an indexer; it is a host for the aggregator layer
- evidence:
  - [1] 2026-10-23: vendor page read: 'USD 9.00 / month', 'Free trial: 7 days', 'Sign-up fee: USD 1.00', and 'On ElfHosted, it comes pre-configured and connected to your other apps.'
  - [2] 2026-10-23: search snippet only: a managed NZBHydra 2 product exists alongside Prowlarr; the page itself was not opened
  - [3] 2026-10-23: search snippet: 'ElfHosted hosts NZBHydra 2 as a managed open-source app'
- sources:
  - [1] https://store.elfhosted.com/product/prowlarr/
  - [2] https://store.elfhosted.com/product/nzbhydra/
  - [3] https://docs.elfhosted.com/app/nzbhydra/

## Jackettio (ElfHosted public instance)

- `debrid/jackettio-elfhosted` | fails-quota | evidence documented | binding request-rate | category hosted Stremio addon, private-tracker search via Jackett with debrid delivery | tier public instance
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://jackettio.elfhosted.com/manifest.json
- price USD 0
- free tier: Free and accountless by design, but on the read date the manifest endpoint itself answered with a rate-limit placeholder: one stream titled 'Jackettio public rate-limit exceeded 🐢' pointing at https://elfhosted.com/assets/public-rate-limit-exceeded.mp4. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: A manifest endpoint returning a stream list is malformed for the Stremio protocol: an installer reading this URL gets a bogus addon rather than an error.
- per-object cap: not applicable: stream descriptors | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance or price published; the paid variant adds proxying. | metered: no | free allowance: not published | source: [2]
- identity: anonymous | detail: Nothing to install; a debrid account and, for private trackers, indexer credentials are the real gates. | country: None
- interface: rest
- limits:
  - request-rate (binding): public instance throttled at the time of reading; the number is unpublished [1]
- limits note: Rate limiting here is so tight that even the manifest is replaced, which is a stronger throttle than MediaFusion's (that one still served a valid manifest).
- binding note: Nothing byte-based is exposed; the shared request limiter is the only published constraint and it was already firing.
- interface detail: Stremio addon over HTTPS; underlying indexer access is through Jackett, which ElfHosted also sells as its own USD 9 app.
- tooling: no install; add manifest to Stremio. The private-tracker part needs the account's own Jackett/Indexer credentials - 'Indexer-backed Stremio addon using Jackett, delivered via Real-Debrid, AllDebrid, or Debrid-Link'.
- composes with: The private-tracker route: it reaches indexers Torrentio does not, so it is the addon a client adds when public trackers have gone thin for a title.
- reliability: Public instance was over its limit on first contact. Private trackers additionally require accounts that may not be obtainable, which is an identity cost outside this host's control.
- notes: Documented as fails-quota rather than dead: the host is up and answering, and the failure is the free allowance, not the service. The distinction matters because the subsequent audit should retest rather than skip.
- evidence note: The manifest URL was fetched and returned the placeholder instead of a manifest. Not measured: the paid instance, and whether the public limit resets. Documented without probe digest: no probe record with status, bytes and digest exists.
- extras:
  - endpoint: https://jackettio.elfhosted.com
  - paid_product: https://store.elfhosted.com/product/jackettio/
- evidence:
  - [1] 2026-10-23: HTTP 200, 346 bytes, a streams array containing 'Jackettio public rate-limit exceeded 🐢' instead of an addon manifest
  - [3] 2026-10-23: what the addon is for: 'Indexer-backed Stremio addon using Jackett, delivered via Real-Debrid, AllDebrid, or Debrid-Link'
  - [4] 2026-10-23: the paid tier exists at USD 9.00 / month alongside the rest of the addon line
- sources:
  - [1] https://jackettio.elfhosted.com/manifest.json
  - [2] https://store.elfhosted.com/product/jackettio/
  - [3] https://docs.elfhosted.com/stremio-addons/
  - [4] https://store.elfhosted.com/product-category/stremio-addons/
