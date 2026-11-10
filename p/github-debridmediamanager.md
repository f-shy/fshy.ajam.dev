# zurg

> github.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-debridmediamanager/ | JSON https://fshy.ajam.dev/api/v1/entity/github-debridmediamanager.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## zurg (Debrid Media Manager webdav server)

- `debrid/zurg` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category client: WebDAV gateway over a debrid library | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:51:00.000Z (live) | stale on 2026-11-23
- url https://github.com/debridmediamanager/zurg-public
- price USD 0 for the gateway; the debrid account is separate
- free tier: The server is a public release on GitHub and costs nothing; the debrid account behind it is the thing that costs. The stable release is Real-Debrid only: 'A self-hosted Real-Debrid webdav server written from scratch.' Nightlies add backends 'beyond Real-Debrid (TorBox, AllDebrid and Usenet)' and need an active sponsorship. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable to the gateway; the source account's cap applies. | source: [1]
- retention: not applicable: the WebDAV tree is a live view of the torrent library. | source: [1]
- egress: No meter of its own; it spends the debrid account's unmetered premium traffic. | metered: no | free allowance: none of its own | source: [1]
- identity: anonymous | detail: No account with the project; it needs a debrid API token, which it stores in config.yml. | country: None
- interface: webdav-proxy, rclone, rest
- limits:
  - request-rate: paces itself to the upstream budget: api_rate_limit_per_minute 250 and torrents_rate_limit_per_minute 75 by default [2]
  - request-rate: paces torrent adds to a 20-second floor it discovered by measurement, because Real-Debrid refuses closer adds [2]
- limits note: The gateway's own throttle exists because the upstream's limit is not the documented one: zurg had to add an add-pacing floor and a repair subsystem for links that stop working while the torrent still reports healthy.
- binding note: A pure client: at 1 TiB/month nothing in zurg fails first, the upstream add floor does. Listed as 'none' because that floor is Real-Debrid's and is recorded there.
- interface detail: Serves the torrent library over WebDAV on localhost:9999 by default, with a per-provider API under /api/providers/realdebrid/ (including /test). rclone mounts the WebDAV; Infuse can read it directly.
- endpoint: http://localhost:9999/
- tooling: Ships a bundle with config.yml, docker-compose.yml, rclone.conf and Plex update scripts; 'rclone and ffprobe are automatically downloaded on first run if not already installed'. Docker image ghcr.io/debridmediamanager/zurg-testing.
- composes with: The bridge that turned debrid into a filesystem for Plex: zurg exposes RD as WebDAV, rclone mounts it, Plex or Jellyfin scans it, and no download ever lands on local disk.
- reliability: The stable line is Real-Debrid only; every other backend is a sponsors-only nightly, so a user on the stable release cannot point it at TorBox or AllDebrid at all.
- notes: Included because it is the de facto answer to 'how does a script get a Real-Debrid library onto a disk without downloading it twice'. Trigger condition: a stable multi-provider release moves this from caveat to plain qualifies.
- evidence note: Repository README and the project's own provider notes were read. Nothing was run: the throughput and mount behaviour are untested here.
- self hosted: yes
- extras:
  - providers_stable: real-debrid
  - providers_nightly: torbox, alldebrid, usenet
  - config_keys: api_rate_limit_per_minute, torrents_rate_limit_per_minute, api_timeout_secs, download_timeout_secs, retries_until_failed, retry_503_errors, fetch_torrents_page_size
- evidence:
  - [1] 2026-10-23: 'A self-hosted Real-Debrid webdav server written from scratch', the rclone+Plex purpose, the requirements (RD account and API token), and that nightlies add 'TorBox, AllDebrid and Usenet' behind sponsorship
  - [2] 2026-10-23: the 20-second add floor and the 250/75 per-minute pacing defaults, plus the repair subsystem's reason for existing
  - [3] 2026-10-23: 'api_rate_limit_per_minute: 250' and 'torrents_rate_limit_per_minute: 75' as documented configuration keys
- sources:
  - [1] https://github.com/debridmediamanager/zurg-public
  - [2] https://notes.debridmediamanager.com/providers/realdebrid/
  - [3] https://github.com/debridmediamanager/zurg-public/wiki/Config
