# Torrentio

> strem.fun | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/strem/ | JSON https://fshy.ajam.dev/api/v1/entity/strem.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Torrentio

- `debrid/torrentio` | qualifies | evidence documented | binding request-rate | category torrent-side aggregator (Stremio addon over multiple public trackers, debrid-aware) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
- url https://torrentio.strem.fun/
- price USD 0 for the add-on
- free tier: Anonymous: GET /stream/movie/tt1254207.json returned 5,709 bytes of JSON with infoHash, fileIdx and per-stream size and seeders, with no key and no account. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: the addon returns magnet hashes, not bytes | source: [2]
- retention: not applicable: results are computed per request; the debrid cache behind them is the provider's retention | source: [2]
- egress: No byte allowance from the addon: it returns magnet links, and the transfer is between the user (or the debrid provider) and the swarm. | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: No account for the P2P path. A debrid key is optional and is the provider's, not Torrentio's.
- interface: rest
- limits:
  - request-rate (binding): no published limit on torrentio.strem.fun; the only published statement is from the operator of a shared public instance, who reports that its traffic to Torrentio was rate-limited [3]
  - request-rate (binding): not published; the add-on is a shared host, so the limit is its capacity rather than a documented number [2]
- limits note: The addon returns a per-title stream list; each title opened is one request. Its own cache headers are explicit: cacheMaxAge 3600, staleRevalidate 14400, staleError 604800, so one title is cheap to ask twice and a shared proxy is what multiplies the rate. Torrentio has also been down for hosting reasons more than once (issues 288 and 370).
- binding note: There is no byte accounting anywhere in the addon; the only thing that breaks at scale is the request rate from one address, which is exactly what the shared-instance reports describe.
- interface detail: Stremio addon protocol over HTTP: /stream/<type>/<imdb>.json, /manifest.json and a /configure page that takes a debrid key. Every response is JSON.
- endpoint: https://torrentio.strem.fun/stream/movie/tt1254207.json
- tooling: Any HTTP client. Stremio or a Kodi addon consumes it directly; AIOStreams, MediaFusion and StremThru chain it behind a single addon. The debrid path needs the provider's API key in the config URL.
- composes with: Torrentio resolves an IMDb id to magnets from public trackers, and with a debrid key it asks the provider which hashes are cached; that cached answer is what makes playback start without seeding.
- reliability: Hosting moves and blocks: the tracker's own issues record the VPS being blocked (issue 288) and a DDoS (issue 370), each taking the public instance down for days. The addon's cacheMaxAge is 3600 s, so a cached stream list can outlive the swarm it describes.
- notes: Stremio addon resolving titles into streamable torrent and debrid cached links. Queries are evaluated per title rather than providing full index scraping.
- evidence note: One stream request was executed on 2026-10-23 and returned real magnets. The rate figure stays reported, because the number came from a third-party operator rather than from Torrentio.
- extras:
  - streams_in_sample: 6
  - debrid_key_optional: yes
  - protocol: stremio-addon
  - cache_max_age_s: 3600
  - stale_error_s: 604800
  - stale_revalidate_s: 14400
  - providers: real-debrid, premiumize, alldebrid, debrid-link, easydebrid, offcloud, torbox, put.io
  - scrapers: YTS, EZTV, RARBG, 1337x, EXT, ThePirateBay, KickassTorrents, TorrentGalaxy, MagnetDL, HorribleSubs, NyaaSi, TokyoTosho, AniDex, nekoBT, Rutor, Rutracker, Comando, BluDV, MicoLeaoDublado, Torrent9, ilCorSaRoNeRo, MejorTorrent, Wolfmax4k, Cinecalidad, BestTorrents
  - alternatives: Comet (cache-first), AIOStreams (multi-addon aggregation), MediaFusion, Jackettio, StremThru (proxy)
- evidence:
  - [1] 2026-10-23: HTTP 200 JSON, 5,709 bytes, streams carrying name 'Torrentio', infoHash f181e166e440b355ce73cc8b988f47ad7e8ea6ab, '7.1 GB' and seed counts, with no key supplied
  - [3] 2026-10-23: a maintainer states the shared public instance 'probably got rate limited by Torrentio' because all its users' requests come from one address
  - [4] 2026-10-23: the addon maintainer wrote that torrentio's VPS was blocked and the addon would be down until a new host was found; read from the issue title and quoted reply in search results, not opened
  - [2] 2026-10-23: version v0.0.15, the scraped provider list, and 'RealDebrid/Premiumize/AllDebrid/DebridLink/EasyDebrid/Offcloud/TorBox/Put.io support' on the configuration page - which came back with upstream_status 403 and full body text
- sources:
  - [1] https://torrentio.strem.fun/stream/movie/tt1254207.json
  - [2] https://torrentio.strem.fun/
  - [3] https://github.com/Viren070/AIOStreams/issues/19
  - [4] https://github.com/TheBeastLT/torrentio-scraper/issues/288
