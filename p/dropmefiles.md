# DropMeFiles

> dropmefiles.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dropmefiles/ | JSON https://fshy.ajam.dev/api/v1/entity/dropmefiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DropMeFiles

- `storage/dropmefiles` | fails-quota | evidence reported | binding per-ip-shaping | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:34.673Z (live) | stale on 2026-12-04
- url https://dropmefiles.com
- free tier: no account; up to 50 GB per transfer | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered but download is a web flow | metered: no
- identity: anonymous | detail: no account required for upload, stated on the service page
- interface: rest
- limits:
  - per-ip-shaping (binding): transfer 'is limited up to 50 Gb', 'period of storage is up to 14 days', selecta [1]
- limits note: 'is limited up to 50 Gb', 'period of storage is up to 14 days', selectable 1-download / 7-day / 14-day expiry.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: web upload only; no public API documented on the page reached
- composes with: None. 14-day cap, per-transfer.
- reliability: Largest single-file number in the niche (50 GB) but browser-centric; unverified whether a byte path exists without a session.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no account; up to 50 GB per transfer
  - dead_end.first_recorded: 2026-10-21
  - probe_reported: GET https://dropmefiles.com/ -> 200 / 39934 B. No scriptable upload endpoint found; not probed further (would cost the slot).
- evidence:
  - [1] 2026-10-21: 
  - [1] 2026-11-19: the service caps an upload at 50 GB and keeps files up to 14 days | capture: sha256:d4666a08241eac9c38c2737790dcea3ad23b59d1257d12edab9e113e0d1a1cf8 | quote: Maхimum size for the upload is limited up to 50 Gb, period of storage is up to 14 days
  - [1] 2026-11-19: uploading needs no account | capture: sha256:d4666a08241eac9c38c2737790dcea3ad23b59d1257d12edab9e113e0d1a1cf8 | quote: No registration required. Unlimited upload/download speed.
- sources:
  - [1] https://dropmefiles.com/
