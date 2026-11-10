# blossom.ditto.pub

> ditto.pub | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ditto/ | JSON https://fshy.ajam.dev/api/v1/entity/ditto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## blossom.ditto.pub (Ditto Blossom server)

- `storage/blossom-ditto-pub` | qualifies-with-caveat | evidence reported | binding per-object-cap | category content-addressed blob server
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://blossom.ditto.pub
- free tier: No quota. Live server stats: 1,375,309 total blobs, 781.96 GB storage used, 8,684 uploads/24 h. Max upload size 2 GB, max media size 1 GB, accepted types `*`. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 2 GB/upload | bytes: 2000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free, unauthenticated GET by SHA-256 | metered: no
- identity: anonymous | detail: Anonymous. Nostr keypair (BUD-11 auth token). No email.
- interface: unknown
- limits:
  - per-object-cap (binding): 2 GB/upload [1]
- limits note: 2 GB/upload, 1 GB for /media; images re-encoded to webp @192 by the server's media optimisation (so /media is lossy, but /upload of a raw blob is not)
- interface detail: Blossom / BUD-01 over HTTPS
- tooling: Blossom clients, nostr SDKs, curl
- composes with: 2 GB per object makes it the best per-file ratio in the Blossom set; SHA-256 addressing composes directly with the chunk-and-replicate pattern.
- reliability: Operator-run hobby infrastructure with ~782 GB on disk; a 500 GB deposit would double the server. No published retention, unlike 24242.io.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '1,375,309 Total Blobs / 781.96 GB Storage Used / 8,684 Uploads (24h)'; 'Max upload size 2 GB'; 'Authentication Required'; 'Accepted types *'
  - [2] 2026-10-21: HEAD — 401, X-Reason: 'This needs a Nostr auth token (BUD-11)'
- sources:
  - [1] https://blossom.ditto.pub/
  - [2] https://blossom.ditto.pub/upload
