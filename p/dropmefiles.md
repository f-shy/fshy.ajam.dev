# DropMeFiles

> dropmefiles.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dropmefiles/ | JSON https://fshy.ajam.dev/api/v1/entity/dropmefiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DropMeFiles

- `storage/dropmefiles` | fails-quota | evidence reported | binding per-ip-shaping | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dropmefiles.com
- free tier: no account; up to 50 GB per transfer | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered but download is a web flow | metered: no
- identity: anonymous
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
- sources:
  - [1] https://dropmefiles.com/
