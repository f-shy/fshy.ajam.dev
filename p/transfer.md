# Transfer.it

> transfer.it | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/transfer/ | JSON https://fshy.ajam.dev/api/v1/entity/transfer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Transfer.it (MEGA)

- `storage/transfer-it` | qualifies-with-caveat | evidence reported | binding retention-clamped | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:26.956Z (live) | stale on 2026-12-10
- url https://transfer.it
- disagrees on identity_kind: `storage/transfer-it` says anonymous, `storage/transfer-it-as-a-paid-capacity-route` says email
- disagrees on verdict: `storage/transfer-it` says qualifies-with-caveat, `storage/transfer-it-as-a-paid-capacity-route` says fails-quota
- free tier: No file size limits. Send 100 GB, 1 TB, or even more, all for free. | unit: mixed | metered on: stored-bytes | read on: 2026-11-09 | source: [1]
- per-object cap: Unlimited transfer size. | source: [1] | note: Unlimited number of transfers.
- retention: Transfers expire after 90 days. | days: 90 | source: [2] | note: Transfers expire after 90 days.
- egress: unmetered; direct host-issued CDN URL (gfsXXX.userstorage.mega.co.nz) supports Range and returns 206. Link/bandwidth not metered per-download on the free tier. | metered: no
- identity: anonymous | detail: Use [Transfer.it](https://transfer.it/) without an account, or sign in with your MEGA credentials to manage your transfers in one place.
- interface: rest, git, cli
- limits:
  - per-ip-shaping: 0.29 MB/s [2]
  - per-ip-shaping: 2.73 MB/s [2]
  - retention-clamped (binding): Retention: SERVER CLAMPS EXPIRY TO 90 DAYS [2]
- limits note: Per-object-cap: none advertised per transfer, but the real ceiling is the 20 GiB ephemeral-account storage (mstrg). A transfer larger than the account's remaining space cannot complete. Retention: SERVER CLAMPS EXPIRY TO 90 DAYS. Verified with a:xl on transfers requested at 1d/90d/1y/10y/no-expiry: all returned e = now+90.00 days. The 10-year ceiling in transferit-py's docs (MAX_EXPIRY_SECONDS) is a CLIENT clamp the server silently overrides. Request-rate: not hit in ~10 uploads.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: Transferit-py (PyPI, github.com/viperadnan-git/transferit-py, 20 stars, pushed 2026-04-22). CLI + library, pip install worked and roundtrip verified. Also NTFSvolume/mega.py has a read-only transfer.it client.
- composes with: Each Transferit() upload creates a NEW anonymous MEGA account (a:up + a:us, no email/phone) => 20 GiB x unlimited free accounts. Shard a file into 20 GiB (or 4 GiB) objects, one ephemeral account per shard, one URL per shard. Cost per identity: two unauthenticated API calls.
- reliability: Expiry IS re-settable in place: a:xm with a new 'e' on an existing xh works and returns 0 (verified 1d -> 30d -> 90d). This is the 'transfer as store' trick. An unexpired transfer can be pushed back to the 90-day wall indefinitely without re-uploading, so the object only dies if you stop touching it for 90 days. Parallel ranged GETs scale (0.29 MB/s @1 conn -> 2.73 MB/s @32 conn on a 32 MiB object, 206s throughout); occasional 403 on a range suggests per-connection shaping, not a hard pull cap.
- notes: the same as the free tier
- evidence note: the blog.mega.io page states no file size limits, with 100 GB or 1 TB sent for free
- evidence:
  - [3] 2026-10-21: probe: transferit upload 1 MiB -> , download + sha256 match 66a5b62e...d1637
  - withheld 2026-10-21: probe: a:uq on ephemeral session -> mstrg 21474836480 (20 GiB), identical across two independent sessions
  - withheld 2026-10-21: probe: a:xl after xm e=365d -> e=now+90.00 days (clamped); xm re-set to 30d then 90d both returned 0
  - [4] 2026-10-21: probe: GET -> 200 text/html 900 bytes (JS SPA; the URL is NOT a plain-GET byte link)
  - [1] 2026-10-21: (archived 2025-07-21) — 'No file size limits. Send 100 GB, 1 TB, or even more, all for free'
  - [1] 2026-11-09: the MEGA blog states the free transfer has no file size limit | capture: sha256:4d9b11bab9bfa148998de848daa3b8a2bc806647cba344be6fd8eec501e77b1d | quote: No file size limits. Send 100 GB, 1 TB, or even more, all for free.
  - [1] 2026-11-09: the blog says Transfer.it can be used without an account | capture: sha256:4d9b11bab9bfa148998de848daa3b8a2bc806647cba344be6fd8eec501e77b1d | quote: Use [Transfer.it](https://transfer.it/) without an account, or sign in with your MEGA credentials to manage your transfers in one place.
  - [2] 2026-11-09: the transfer.it response is a 900-byte HTML page | capture: sha256:1e339c391337e73e5de8aa5624b9cfd6b0fd073522757d166db87bb8942cc9ec | quote: content-length: 900
  - [5] 2026-11-25: the first-party comparison states that transfer size is unlimited | capture: sha256:b2421a0530f97fcbf77ab4b49aa42e9616473452a2c17c41944cb3609d40e302 | quote: Unlimited transfer size
  - [5] 2026-11-25: the first-party comparison states that the number of transfers is unlimited | capture: sha256:b2421a0530f97fcbf77ab4b49aa42e9616473452a2c17c41944cb3609d40e302 | quote: Unlimited number of transfers
  - [5] 2026-11-25: the first-party comparison states a 90-day transfer expiry | capture: sha256:b2421a0530f97fcbf77ab4b49aa42e9616473452a2c17c41944cb3609d40e302 | quote: Transfers expire after 90 days
  - [5] 2026-11-25: the first-party comparison states an unlimited transfer size | capture: sha256:b2421a0530f97fcbf77ab4b49aa42e9616473452a2c17c41944cb3609d40e302 | quote: Unlimited transfer size
  - [5] 2026-11-25: the first-party comparison states an unlimited number of transfers | capture: sha256:b2421a0530f97fcbf77ab4b49aa42e9616473452a2c17c41944cb3609d40e302 | quote: Unlimited number of transfers
  - [5] 2026-11-25: the first-party comparison states that transfers expire after 90 days | capture: sha256:b2421a0530f97fcbf77ab4b49aa42e9616473452a2c17c41944cb3609d40e302 | quote: Transfers expire after 90 days
- sources:
  - [1] https://blog.mega.io/introducing-transfer-it
  - [2] https://transfer.it/
  - [3] https://transfer.it/t/JzZzzDxj2JCS
  - [4] https://transfer.it/t/<xh>
  - [5] https://transfer.it/compare

## transfer.it (mega) as a paid capacity route

- `storage/transfer-it-as-a-paid-capacity-route` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:29.437Z (live) | stale on 2026-12-04
- url https://transfer.it/
- disagrees on identity_kind: `storage/transfer-it` says anonymous, `storage/transfer-it-as-a-paid-capacity-route` says email
- disagrees on verdict: `storage/transfer-it` says qualifies-with-caveat, `storage/transfer-it-as-a-paid-capacity-route` says fails-quota
- free tier: None reachable: Transfer.it has no paid tier of its own. It is a sharing front end that requires MEGA storage: 'You can only share files that you have uploaded to MEGA.' Its expiry selector offers up to 1. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Transfer.it has no paid tier of its own — it is a sharing front end that requires MEGA storage: 'You can only share files that you have uploaded to MEGA.' Its expiry selector offers up to 1
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Transfer.it has no paid tier of its own — it is a sharing front end that requires MEGA storage: 'You can only share files that you have uploaded to MEGA.' Its expiry selector offers up to 1
  - [1] 2026-11-19: transfer.it is still a sharing front end that requires MEGA storage, with no storage paid tier of its own | capture: sha256:b65fabdc1753269d3ddb417c107ee31c2caa9d45eb0531f3b7977b038339cd7c | quote: You can only share files that you have uploaded to MEGA
- sources:
  - [1] https://transfer.it/
