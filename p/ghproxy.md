# ghproxy mirrors

> ghproxy.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ghproxy/ | JSON https://fshy.ajam.dev/api/v1/entity/ghproxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ghproxy mirrors (ghproxy.net, ghfast.top) — free anonymous GitHub raw/release proxy

- `storage/ghproxy-mirrors-free-anonymous-github-raw-release-proxy` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category cdn
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:27.695Z (live) | stale on 2026-12-04
- url https://ghproxy.net/
- free tier: GitHub文件链接带不带协议头都可以，支持release、archive以及文件，右键复制出来的链接都是符合标准的，更多用法、clone加速请参考这篇文章。 | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
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
  - [1] 2026-11-11: the page states that GitHub file links are accepted with or without a protocol prefix, and that release, archive and file links are supported | capture: sha256:c90536f6b5791c8178e9310034d74c0f636e6ba7caa4ebadb117a688c57fcae8 | quote: GitHub文件链接带不带协议头都可以，支持release、archive以及文件，右键复制出来的链接都是符合标准的，更多用法、clone加速请参考这篇文章。
  - [1] 2026-11-19: the mirror still accepts GitHub links with or without the protocol prefix and supports release, archive and file links | capture: sha256:4829cb19a0ff44ebf286ed65c94240164d9fe7b2024f46d4a90e4934427e5343 | quote: GitHub文件链接带不带协议头都可以，支持release、archive以及文件，右键复制出来的链接都是符合标准的，更多用法、clone加速请参考
  - [1] 2026-11-19: the mirror states a sponsor and links its open-source project | capture: sha256:4829cb19a0ff44ebf286ed65c94240164d9fe7b2024f46d4a90e4934427e5343 | quote: 服务器由 [WAP.AC](https://wap.ac/) 赞助。项目开源GitHub [hunshcn/gh-proxy](https://github.com/hunshcn/gh-proxy)
- sources:
  - [1] https://ghproxy.net/
  - [2] https://ghproxy.net/https://raw.githubusercontent.com/P3TERX/GeoLite.mmdb/download/GeoLite2-City.mmdb
  - [3] https://ghfast.top/https://raw.githubusercontent.com/P3TERX/GeoLite.mmdb/download/GeoLite2-City.mmdb
  - [4] https://gh-proxy.com/…
