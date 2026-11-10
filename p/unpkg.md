# unpkg

> unpkg.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unpkg/ | JSON https://fshy.ajam.dev/api/v1/entity/unpkg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## unpkg (npm CDN)

- `storage/unpkg` | qualifies | evidence reported | binding per-object-cap | category cdn
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://unpkg.com/
- free tier: No storage quota of its own. It serves the npm registry, so the ceiling is npm's ~100 MB publish limit. Probed 28.3 MB, 32.2 MB, 54.0 MB and 64.5 MB single files: all HTTP 200, all full length, sha256 identity with hop.js on the 54 MB and 64.5 MB cases. No per-file cap was encountered. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: npm publish-side (~100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, no account, Cloudflare-fronted (cf-cache-status HIT on repeat). No published bandwidth limit. | metered: no
- identity: email | detail: email
- interface: rest, rclone
- limits:
  - per-object-cap (binding): per-object-cap: npm publish-side (~100 MB [1]
- limits note: per-object-cap: npm publish-side (~100 MB tarball, 413 above that). No cap observed on the read side up to 64.5 MB. Version pinning required for immutability.
- interface detail: rest
- tooling: GET https://unpkg.com/<pkg>@<ver>/<path>. Also /<pkg>@<ver>/ (directory listing) and ?meta. Plain curl/rclone.
- composes with: Second mirror in a 3-way npm serving tier (unpkg + hop.js + jsDelivr). Because all three read the same npm tarballs, publishing once to npm gives you three independent free CDNs with different per-file ceilings. JsDelivr 50 MB, unpkg and hop.js effectively npm-bounded. Shard at 45 MB and every mirror serves every shard.
- reliability: Long-running but small-team; Cloudflare absorbs the bandwidth. Was 403 on the .exe? No. Unpkg served it; it is jsDelivr that blocks the extension.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: HTTP 200, 64,458,752 bytes (probed)
  - [3] 2026-10-21: HTTP 200, 53,974,528 bytes (probed)
  - [4] 2026-10-21: HTTP 200, 28,312,028 bytes (probed)
  - [5] 2026-10-21: HTTP 200, 87,533 bytes, sha256 fc9a93dd… matches jsDelivr and githack copies (probed)
- sources:
  - [1] https://unpkg.com/
  - [2] https://unpkg.com/@ffmpeg-installer/win32-x64@4.1.0/ffmpeg.exe
  - [3] https://unpkg.com/@swc/core-win32-x64-msvc@1.7.0/swc.win32-x64-msvc.node
  - [4] https://unpkg.com/onnxruntime-web@1.30.0/dist/ort-wasm-simd-threaded.jsep.wasm
  - [5] https://unpkg.com/jquery@3.7.1/dist/jquery.min.js
