# ghproxy mirrors

> ghproxy.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ghproxy/ | JSON https://fshy.ajam.dev/api/v1/entity/ghproxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ghproxy mirrors (ghproxy.net, ghfast.top) — free anonymous GitHub raw/release proxy

- `storage/ghproxy-mirrors-free-anonymous-github-raw-release-proxy` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category cdn
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ghproxy.net/
- free tier: No quota; it proxies raw.githubusercontent.com and release assets, so the ceiling is GitHub's own (100 MiB/repo file, ~1.95 TiB/release). Probed a 50,901,339-byte GitHub file through ghproxy.net: HTTP 200, correct Content-Length. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, anonymous, no key. These are community-run mirrors of the GitHub CDN, funded by volunteers. Hence the polyculture of hostnames (gh-proxy.com, ghproxy.net, ghfast.top, gh.api.99988866.xyz) and the constant churn. | metered: no
- identity: anonymous | detail: anonymous
- interface: rest
- limits:
  - per-ip-shaping (binding): 128 KB/s [1]
  - per-ip-shaping (binding): 11.3 MB/s [1]
- limits note: Per-IP bandwidth shaping restricts download rates. Probes observed approximately 128 KB/s on file retrieval, compared to higher throughput from alternative CDN endpoints.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: Prefix form: https://ghproxy.net/https://raw.githubusercontent.com/<owner>/<repo>/<ref>/<path> and .../https://github.com/<owner>/<repo>/releases/download/<tag>/<asset>. Nothing else to install.
- composes with: Serves as an edge mirror for GitHub release assets alongside raw file mirrors. Proxies allow distributing reads across ghproxy.net, ghfast.top, and other mirrors for public release downloads.
- reliability: Treat as a bandwidth multiplier for large files, never as an availability guarantee. Their own issue trackers document the churn (hunshcn/gh-proxy#116 mirror list, 'ghproxy.com 打不开了').
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
- evidence:
  - [2] 2026-10-21: HTTP 200, Content-Length 50,901,339, correct prefix bytes; throughput ~128 KB/s (probed)
  - [3] 2026-10-21: HTTP 200, 50,901,339 bytes (probed)
  - [4] 2026-10-21: and https://cdn.gitmirror.com/gh/… — connection failed / 0 bytes (probed, dead)
  - withheld 2026-10-21: 
- sources:
  - [1] https://ghproxy.net/
  - [2] https://ghproxy.net/https://raw.githubusercontent.com/P3TERX/GeoLite.mmdb/download/GeoLite2-City.mmdb
  - [3] https://ghfast.top/https://raw.githubusercontent.com/P3TERX/GeoLite.mmdb/download/GeoLite2-City.mmdb
  - [4] https://gh-proxy.com/…
