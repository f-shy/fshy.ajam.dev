# Blossom blob servers

> nostr.build | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nostr/ | JSON https://fshy.ajam.dev/api/v1/entity/nostr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Blossom blob servers (nostr.download, blossom.nostr.build, 24242.io)

- `storage/blossom-blob-servers` | fails-quota | evidence reported | binding retention-clamped | category Nostr media/blob servers (content-addressed, keypair auth)
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://blossom.nostr.build/
- free tier: Per-object caps only, and small: nostr.build free uploads 20 MiB, hard cap 100 MiB, then storage plans 5 GB / $18/yr up to 500 GB / $240/yr. 24242.io: 100 MiB max file, files deleted after 60 days unaccessed. blossom.psbt.me: 1 month hosting, files under 1 MB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 24242.io: 100 MiB max file, files deleted after 60 days unaccessed | days: 60 | source: [1] | note: not stated
- egress: Free CDN, global. | metered: no
- identity: anonymous | detail: anonymous
- interface: rest
- limits:
  - retention-clamped (binding): deleted after 60 days [1]
- limits note: 20 MiB free / 100 MiB absolute on nostr.build; 100 MiB on 24242.io; 1 MB on psbt.me. Auth is a signed event, so 'no account' is real: 401 with x-reason 'Missing Blossom Authorization header'.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: BUD-01/BUD-06 HTTP API: PUT /upload, HEAD /upload, DELETE; auth is a signed Nostr event in the Authorization header, not an account.
- tooling: any Blossom client; curl with a signed event.
- composes with: Content-addressed by sha256, so it chunks naturally into the hoangvu12/free-s3 pattern. But 20 MiB chunks would need ~50,000 objects per TiB.
- reliability: Cryptographic keypair authentication with no registration required. Hosted blossom instances enforce 60-day idle deletion policies.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Per-object caps only, and small: nostr.build free uploads 20 MiB, hard cap 100 MiB, then storage plans 5 GB / $18/yr up to 500 GB / $240/yr. 24242.io: 100 MiB max file, files deleted after 60 days unaccessed. blossom.psbt.me: 1 month hosting, files under 1 MB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'A hard cap of 100 MiB per upload (20 MiB for free uploads), with no limit on the number of uploads or retention'; plans $18/yr 5GB … $240/yr 500GB
  - [2] 2026-10-21: HEAD returns 401, x-reason: 'Missing Blossom Authorization header, authorization required' (i.e. keypair auth, no signup)
  - [3] 2026-10-21: 401, x-reason: 'Auth header not found'
  - [4] 2026-10-21: 'Max file size: 100MiB. Files are deleted if not accessed for 60 days.'
  - [5] 2026-10-21: 'Free Tier: 1-month hosting for files under 1 MB'
- sources:
  - [1] https://blossom.nostr.build/
  - [2] https://blossom.nostr.build/upload
  - [3] https://nostr.download/upload
  - [4] https://24242.io/
  - [5] https://blossom.psbt.me/
