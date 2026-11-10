# PocketHost

> pockethost.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pockethost/ | JSON https://fshy.ajam.dev/api/v1/entity/pockethost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PocketHost (PocketBase hosting)

- `storage/pockethost` | trial-only | evidence reported | binding per-ip-shaping | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://pockethost.io
- free tier: 10 GB file storage + 250 MB DB per PocketBase slot. Slots are $9.99/mo (or $5/mo annual, or lifetime), with a 7-day trial. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 10 GB file storage + 250 MB DB per PocketBase slot. Slots are $9.99/mo (or $5/mo annual, or lifetime), with a 7-day trial. | days: 7 | source: [1] | note: not stated
- egress: Unmetered bandwidth and CPU, fair use. This is the standout: storage is paid but egress is genuinely unmetered. | metered: no
- identity: card
- interface: s3, rest, sftp
- limits:
  - per-ip-shaping (binding): bandwidth could be throttled at sustained high volume [1]
- limits note: 7-day risk-free trial only; 10 GB per slot; SFTP access is a real plus for bulk transfer; fair-use bandwidth could be throttled at sustained high volume.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: PocketBase REST/realtime API, `pocketbase` JS/Dart SDKs, SFTP file access on PocketHost, S3 storage backend supported (like standalone PocketBase)
- composes with: Storage pools across slots ('Storage adds to your account pool, shared across every PocketBase you run'), so 10 slots = 100 GB for ~$50-100/mo. Not free, but the only entrant here with unmetered egress. Self-hosting PocketBase is free/MIT. That is the free path, on compute that is already available.
- reliability: Run by a single maintainer (benallfree) on DigitalOcean; data volume not encrypted at OS level per their own FAQ. Small-operator risk.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 GB file storage + 250 MB DB per PocketBase slot — slots are $9.99/mo (or $5/mo annual, or lifetime), with a 7-day trial
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Each slot includes 250 MB DB data storage and 10 GB file storage ... Unmetered bandwidth and CPU (fair use)', '$9.99 per PocketBase, per month', '7 day riskfree trial'
  - [2] 2026-10-21: 'While the data volume is not encrypted at the OS level ... you can always back up and download your data via SFTP'
- sources:
  - [1] https://pockethost.io/pricing
  - [2] https://pockethost.io/docs/faq
