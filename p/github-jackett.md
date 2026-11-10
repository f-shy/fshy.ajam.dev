# Jackett

> github.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-jackett/ | JSON https://fshy.ajam.dev/api/v1/entity/github-jackett.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jackett

- `debrid/jackett` | self-hosted, last resort | verdict qualifies | evidence documented | binding request-rate | category self-hosted indexer proxy (Torznab over ~600 trackers) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
- url https://github.com/Jackett/Jackett
- price USD 0
- free tier: The software is free and the API key is generated locally by the instance. The cost is the machine it runs on, not a subscription. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: Torznab results | source: [1]
- retention: the instance caches results per indexer (default 1,000 rows) and can bypass the cache with &cache=false | source: [1]
- egress: no byte allowance: Torznab XML only; the transfer is client-to-swarm | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: Jackett itself needs no account. Individual indexers may need one, and the README marks some as invite-only with no active maintainer.
- interface: rest
- limits:
  - request-rate (binding): no global limit: each indexer carries its own, and the instance absorbs repeats with a per-indexer result cache (default 1,000 rows) [1]
- limits note: The binding constraint is the machine: an instance needs a process that stays up, which means a free compute service rather than local hardware. Trackers marked 'invite needed' in the indexer list 'have no active maintainer and may be broken'.
- binding note: The upstream trackers' own rate limits pass straight through, and the instance's cache is the only thing that reduces how often they are hit.
- interface detail: Torznab and TorrentPotato over HTTP at the instance's own address: /api/v2.0/indexers/all/results/torznab/api?apikey=...&t=search&q=...
- endpoint: http://127.0.0.1:9117/api/v2.0/indexers/all/results/torznab/api
- tooling: A container or a .NET runtime on a free compute instance; Sonarr, Radarr and Prowlarr speak the same Torznab. FlareSolverr is integrated for Cloudflare-walled indexers.
- composes with: One Torznab endpoint in front of every tracker already accessible, which turns a dozen scrapers into one URL that the automation stack and a debrid cache check both use.
- reliability: Cloudflare-walled indexers fail without FlareSolverr, and the README warns that invite-only entries may be broken; a client that only runs Jackett gets partial coverage and does not know which indexer failed unless it reads the dashboard.
- notes: 'public torrent-search API behind Jackett' is really a private Torznab fan-out: Jackett adds no index of its own, it translates scrapers. The nearest hosted equivalent is TorrentClaw's Torznab endpoint, which needs a key and is PRO-gated.
- evidence note: The README was read on 2026-10-23, including the Torznab query syntax, the cache setting and the FlareSolverr note. A running instance on free compute would raise it to measured.
- self hosted: yes
- extras:
  - protocol: torznab
  - indexers: hundreds listed in the README; the exact count was not established
  - requires_host: yes
  - flaresolverr: yes
- evidence:
  - [1] 2026-10-23: Torznab and TorrentPotato endpoints, the /api/v2.0/indexers/all/results/torznab/api path with an apikey, 'Cache max results per indexer: Default is 1000', and the FlareSolverr integration
  - [1] 2026-10-23: 'Trackers marked with (invite needed) have no active maintainer and may be broken or missing features'
- sources:
  - [1] https://github.com/Jackett/Jackett
