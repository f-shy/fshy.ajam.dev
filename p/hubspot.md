# HubSpot

> hubspot.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hubspot/ | JSON https://fshy.ajam.dev/api/v1/entity/hubspot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HubSpot (free-tools file manager / hubfs)

- `storage/hubspot` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.hubspot.com
- free tier: Per-file 20 MB on free accounts, 2 GB on paid. No published account total: 'Generally, there is no limit on how many files you can upload.' HubSpot's own catalog does not state a storage figure. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20 MB per file | bytes: 20000000 | source: [1] | note: not stated
- retention: Request-rate: 100 req / 10 s / app and 250,000 / day per account on Free ('Privately distributed apps, Free and Starter, 100/app, 250,000/account'). Retention: none documented. Files persist until deleted. | source: [1] | note: not stated
- egress: Free, Cloudflare-fronted. `hubfs` files are served publicly with `Accept-Ranges: bytes`, `Access-Control-Allow-Origin: *`, `Cache-Control: s-maxage=2592000`. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - request-rate: 5 calls/day [1]
  - per-object-cap (binding): 20 MB per file [1]
- limits note: Per-object-cap: 20 MB per file on free tools (the binding constraint by a wide margin); the docs note 'If a file is 1 GB or more, you may experience issues'. request-rate: 100 req / 10 s / app and 250,000 / day per account on Free ('Privately distributed apps, Free and Starter, 100/app, 250,000/account'). Retention: none documented. Files persist until deleted. Download URLs can 429 if the rate limit is exceeded.
- interface detail: rest
- tooling: Files API (`POST /files/2026-09/files`, multipart), public URL in the response's `defaultHostingUrl` / `url`. Python/Node SDKs. No rclone backend.
- composes with: 20 MB/file x unlimited files x unlimited free HubSpot accounts. Weak on its own; becomes usable only at portal scale or if you can get onto 2 GB/file.
- reliability: The API is genuinely good (2e5 calls/day, 100/10s) but the 20 MB free per-file cap means shard-only. HTML/JS files are served as text/plain on default domains, so binaries only.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Files up to 20 MB for accounts with only access to HubSpot's free tools. Files up to 2 GB for accounts with paid subscriptions.'
  - [2] 2026-10-21: 'Generally, there is no limit on how many files you can upload.'
  - [3] 2026-10-21: Free/Starter '100 / app (per 10 s)', '250,000 / account (per day)'
  - [4] 2026-10-21: probe: GET -> 200, 5,123 bytes, real PNG 288x288; Range: bytes=0-99 -> 206, 100 bytes
- sources:
  - [1] https://knowledge.hubspot.com/files/supported-file-types
  - [2] https://community.hubspot.com/t/maximum-uploads/21271
  - [3] https://developers.hubspot.com/docs/developer-tooling/platform/usage-guidelines
  - [4] https://www.hubspot.com/hubfs/HubSpot_Logos/HubSpot-Inversed-Favicon.png
