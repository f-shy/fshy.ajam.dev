# archive.org /download web serving path

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archive-org-download-web-serving-path/ | JSON https://fshy.ajam.dev/api/v1/entity/archive-org-download-web-serving-path.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## archive.org /download web serving path (the free CDN)

- `storage/archive-org-download-web-serving-path` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category academic
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:05:15.762Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://archive.org/download/<identifier>/<filename>
- free tier: Serving is unmetered and free; no per-file download cap and no egress fee. Practical ceiling is throughput, not quota. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free / unmetered. Docs: 'high performance downloads are achieved via the archive web infrastructure'. I.e. GET https://archive.org/download/<item>/<file>, which 302s to an iaNNNNNN.us.archive.org datanode. BitTorrent webseeds supplement it. | metered: no | source: [2]
- identity: anonymous | detail: no credential is needed to read: an anonymous GET of archive.org/download/<identifier>/<filename> redirects once to a datanode and serves the file. Uploading needs an Internet Archive account whose form asks an email address, a screen name and a password, and asks no phone number
- interface: rest, rclone, cli
- limits:
  - per-ip-shaping (binding): 1.19 MB/s [1]
  - per-ip-shaping (binding): 1.66 MB/s [1]
- limits note: Canonical URLs 302 at least once (clients need --location-trusted when sending Authorization); do NOT link iaNNNNNN.us.archive.org directly (nodes move); 429/503 under load; no auth on GET, so everything is world-readable.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: plain HTTPS GET with Range (measured: 206 + accept-ranges: bytes); ia CLI download w/ --checksum resume; rclone 'internetarchive' reads back through the same front end
- composes with: Parallelising across items distributes traffic across different iaNNNNNN datanodes, scaling aggregate throughput with item count rather than single-item connections. Fronting with Cloudflare caching (replay responses carry cache-control: max-age=1800) shields origin nodes from repeated requests.
- reliability: Throughput is shaped server-side: measurements showed 1.19 MB/s on a single stream and 1.66 MB/s aggregate across 8 parallel range requests to a single datanode (~145 GB per day). Local link speed measured at 27.6 MB/s.
- notes: the same as the free tier
- evidence:
  - [3] 2026-10-21: 'Fast GET downloads ... high performance downloads are achieved via the archive web infrastructure: curl --location http://archive.org/download/sam-s3-test-08/demo-intro-to-k.pdf'
  - [1] 2026-10-21: (snapshot 2025-11-08) — 'A particular file can always be downloaded from https://archive.org/download/<identifier>/<filename>'
  - withheld 2026-10-21: probe: curl -r 0-1048575 web.archive.org replay of a 406MB ISO -> HTTP 206, content-range honoured, accept-ranges: bytes, cache-control: max-age=1800
  - withheld 2026-10-21: probe: 8 parallel 5MB range GETs to one replay target -> 40,000,000 bytes in 23s = ~1.7 MB/s aggregate; single 90s stream -> 1.19 MB/s; Cloudflare 50MB control download -> 27.6 MB/s
  - probe:archive.org 2026-11-01: an unauthenticated GET of an archive.org/download URL answered 200 after one redirect | capture: sha256:2344ace3e7bab201e26cff36d7f3fd40f9e4df12bcb0b0420d93f7faa75ffe7b | quote: "status": 200
  - [1] 2026-11-01: the download URL is a public URL, with no account named | capture: sha256:f876449c8138dfef8cb710c3be34f15c757af8eb026d9e538a006f6257df504e | quote: A particular file can always be downloaded from:
  - probe:archive.org 2026-11-01: an unauthenticated GET of an archive.org/download URL answered 200, so the read path needs no identity | capture: sha256:2344ace3e7bab201e26cff36d7f3fd40f9e4df12bcb0b0420d93f7faa75ffe7b | quote: "status": 200
  - [4] 2026-11-01: an upload account asks a screen name, an email address and a password | capture: sha256:b64a400f01d831157d788d8375563bd617f1248e0d53a3cf9f3805097ffce4a2 | quote: Choose a screen name3 to 40 characters
  - [1] 2026-11-01: the download URL redirects to a datanode | capture: sha256:f876449c8138dfef8cb710c3be34f15c757af8eb026d9e538a006f6257df504e | quote: The resultant URL is not a permalink.
- sources:
  - [1] https://archive.org/developers/items.html
  - [2] https://archive.org/download/<item>/<file>
  - [3] https://archive.org/developers/ias3.html
  - [4] https://archive.org/account/signup
