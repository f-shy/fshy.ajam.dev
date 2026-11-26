# blossom.ditto.pub

> ditto.pub | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ditto/ | JSON https://fshy.ajam.dev/api/v1/entity/ditto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## blossom.ditto.pub (Ditto Blossom server)

- `storage/blossom-ditto-pub` | qualifies-with-caveat | evidence reported | binding per-object-cap | category content-addressed blob server
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:54:53.001Z (live) | stale on 2026-12-10
- url https://blossom.ditto.pub
- free tier: No quota stated. The first-party page publishes a live blob count (2,113,101 blobs) and the Blossom endpoint list; no upload-size, media-size or storage-used figure is published. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: unverified: the 2 GB upload cap is no longer stated on the first-party page, which now lists only protocol endpoints and a blob count | bytes: 2000000000 | source: [1] | note: No upload-size limit is stated on the server page; it publishes a blob count and the Blossom endpoint list.
- retention: source: [1] | note: No retention period is stated; the endpoint list includes DELETE/<sha256> (BUD-12) for deleting a blob.
- egress: unverified: no GET price or authentication term is stated on the first-party server page. | metered: no
- identity: anonymous | detail: Anonymous. Nostr keypair (BUD-11 auth token). No email.
- interface: rest
- limits:
  - per-object-cap (binding): 2 GB/upload [1]
- limits note: 2 GB/upload, 1 GB for /media; images re-encoded to webp @192 by the server's media optimisation (so /media is lossy, but /upload of a raw blob is not)
- interface detail: Blossom / BUD-01 over HTTPS
- tooling: Blossom clients, nostr SDKs, curl
- composes with: 2 GB per object makes it the best per-file ratio in the Blossom set; SHA-256 addressing composes directly with the chunk-and-replicate pattern.
- reliability: Operator-run hobby infrastructure with ~782 GB on disk; a 500 GB deposit would double the server. No published retention, unlike 24242.io.
- notes: No quota. Live server stats: 1,375,309 total blobs, 781.96 GB storage used, 8,684 uploads/24 h. Max upload size 2 GB, max media size 1 GB, accepted types `*`.
- evidence:
  - [1] 2026-10-21: '1,375,309 Total Blobs / 781.96 GB Storage Used / 8,684 Uploads (24h)'; 'Max upload size 2 GB'; 'Authentication Required'; 'Accepted types *'
  - [2] 2026-10-21: HEAD — 401, X-Reason: 'This needs a Nostr auth token (BUD-11)'
  - [1] 2026-11-19: the server is reachable and still serves the Blossom blob protocol | capture: sha256:10ee98f5bb786bf6a05da61ecb15a0b81482e6ab5612c757186927214fc8fa03 | quote: This is a [Blossom](https://github.com/hzrd149/blossom) server: it stores blobs addressed by their SHA-256 hash, for Nostr clients.
  - [1] 2026-11-19: the current first-party page states only a blob count, not the former size or storage figures | capture: sha256:10ee98f5bb786bf6a05da61ecb15a0b81482e6ab5612c757186927214fc8fa03 | quote: 2,057,354 blobs
  - [1] 2026-11-19: the current page does not state an upload size cap | capture: sha256:10ee98f5bb786bf6a05da61ecb15a0b81482e6ab5612c757186927214fc8fa03 | quote: 2,057,354 blobs
  - [1] 2026-11-25: the first-party page documents SHA-256 addressed blobs, a GET fetch endpoint and a PUT upload endpoint requiring a Nostr auth token, with no GET price term | capture: sha256:aeb27747d4c3d045caf3281544dffb42db029212fcd6f0864cba79610cc35e26 | quote: This is a [Blossom](https://github.com/hzrd149/blossom) server: it stores blobs addressed by their SHA-256 hash, for Nostr clients. ... - `GET/<sha256>`Fetch a blob (BUD-01) ... - `PUT/upload`Upload a blob, with a Nostr auth token (BUD-02)
  - [1] 2026-11-25: the blob server documents a SHA-256 GET fetch and a PUT upload that needs a Nostr auth token | capture: sha256:aeb27747d4c3d045caf3281544dffb42db029212fcd6f0864cba79610cc35e26 | quote: `GET/<sha256>`Fetch a blob (BUD-01) - `PUT/upload`Upload a blob, with a Nostr auth token (BUD-02)
  - [1] 2026-11-25: the page publishes a live blob count and protocol endpoints, with no upload-size figure | capture: sha256:aeb27747d4c3d045caf3281544dffb42db029212fcd6f0864cba79610cc35e26 | quote: 2,113,101 blobs ... - `PUT/mirror`Copy a blob from another server (BUD-04)
  - [1] 2026-11-25: the server page lists a blob deletion endpoint and states no retention period | capture: sha256:aeb27747d4c3d045caf3281544dffb42db029212fcd6f0864cba79610cc35e26 | quote: - `DELETE/<sha256>`Delete your blob (BUD-12)
- sources:
  - [1] https://blossom.ditto.pub/
  - [2] https://blossom.ditto.pub/upload
