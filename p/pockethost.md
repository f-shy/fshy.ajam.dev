# PocketHost

> pockethost.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pockethost/ | JSON https://fshy.ajam.dev/api/v1/entity/pockethost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PocketHost (PocketBase hosting)

- `storage/pockethost` | trial-only | evidence reported | binding per-ip-shaping | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:15.333Z (live) | stale on 2026-12-10
- url https://pockethost.io
- free tier: 10 GB file storage + 250 MB DB per PocketBase slot. Slots are $9.99/mo (or $5/mo annual, or lifetime), with a 7-day trial. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: unverified: the limits page states 10 GB per paid instance, pooled across the account; no per-file size cap is stated there.
- retention: Nothing is deleted. A powered-off instance keeps all of its data, and you can power it back on whenever your plan has room. | source: [2] | note: Nothing is deleted. A powered-off instance keeps all of its data, and you can power it back on whenever your plan has room.
- egress: - Unmetered bandwidth and CPU (fair use) | metered: no
- identity: card
- interface: s3, rest, sftp
- limits:
  - per-ip-shaping (binding): bandwidth could be throttled at sustained high volume [1]
- limits note: Each paid instance adds 10 GB of shared file storage; the current pricing page states a 30-day money-back guarantee on every plan rather than a short trial. Unmetered bandwidth and CPU under fair use. The named plans are USD 9.99 per instance per month, USD 59.99 per instance per year and USD 149.99 once per instance.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: PocketBase REST/realtime API, `pocketbase` JS/Dart SDKs, SFTP file access on PocketHost, S3 storage backend supported (like standalone PocketBase)
- composes with: 10 GB per paid instance, pooled across your account.
- reliability: Run by a single maintainer (benallfree) on DigitalOcean; data volume not encrypted at OS level per their own FAQ. Small-operator risk.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 GB file storage + 250 MB DB per PocketBase slot — slots are $9.99/mo (or $5/mo annual, or lifetime), with a 7-day trial
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Each slot includes 250 MB DB data storage and 10 GB file storage ... Unmetered bandwidth and CPU (fair use)', '$9.99 per PocketBase, per month', '7 day riskfree trial'
  - [3] 2026-10-21: 'While the data volume is not encrypted at the OS level ... you can always back up and download your data via SFTP'
  - [1] 2026-11-19: the pricing page still states a 30-day money-back guarantee on every plan | capture: sha256:1bbdcc88f34196937736222bd15282ef4d14a1b2801a12fd992baeadafe2b746 | quote: Pay per instance. Every plan has a 30-day money-back guarantee.
  - [1] 2026-11-19: the current pricing page describes shared per-instance storage, not a 7-day trial | capture: sha256:1bbdcc88f34196937736222bd15282ef4d14a1b2801a12fd992baeadafe2b746 | quote: Each paid instance adds 10 GB to your account's shared storage.
  - [2] 2026-11-25: the limits page states pooled disk storage but no per-file size cap | capture: sha256:9aa3d8b75f0b56bf6e233b11bb9bac8b9328035c82d28f1335d2e067492d0a87 | quote: 10 GB per paid instance, pooled across your account.
  - [2] 2026-11-25: data is kept when an instance is powered off after a plan reduction | capture: sha256:9aa3d8b75f0b56bf6e233b11bb9bac8b9328035c82d28f1335d2e067492d0a87 | quote: Nothing is deleted. A powered-off instance keeps all of its data, and you can power it back on whenever your plan has room.
  - [2] 2026-11-25: powered-off instances keep their data | capture: sha256:9aa3d8b75f0b56bf6e233b11bb9bac8b9328035c82d28f1335d2e067492d0a87 | quote: Nothing is deleted. A powered-off instance keeps all of its data, and you can power it back on whenever your plan has room.
  - [2] 2026-11-25: the captured page gives no file-expiry period | capture: sha256:9aa3d8b75f0b56bf6e233b11bb9bac8b9328035c82d28f1335d2e067492d0a87 | quote: Nothing is deleted. A powered-off instance keeps all of its data, and you can power it back on whenever your plan has room.
  - [2] 2026-11-25: the limits page states the data-preservation term | capture: sha256:9aa3d8b75f0b56bf6e233b11bb9bac8b9328035c82d28f1335d2e067492d0a87 | quote: Nothing is deleted. A powered-off instance keeps all of its data, and you can power it back on whenever your plan has room.
  - [1] 2026-11-25: the paid plan lists unmetered bandwidth under fair use | capture: sha256:1bbdcc88f34196937736222bd15282ef4d14a1b2801a12fd992baeadafe2b746 | quote: - Unmetered bandwidth and CPU (fair use)
  - [1] 2026-11-25: bandwidth is unmetered under fair use | capture: sha256:1bbdcc88f34196937736222bd15282ef4d14a1b2801a12fd992baeadafe2b746 | quote: - Unmetered bandwidth and CPU (fair use)
  - [2] 2026-11-25: storage from paid instances is pooled across the account | capture: sha256:9aa3d8b75f0b56bf6e233b11bb9bac8b9328035c82d28f1335d2e067492d0a87 | quote: 10 GB per paid instance, pooled across your account.
  - [2] 2026-11-25: paid-instance storage is pooled across the account | capture: sha256:9aa3d8b75f0b56bf6e233b11bb9bac8b9328035c82d28f1335d2e067492d0a87 | quote: 10 GB per paid instance, pooled across your account.
  - [4] 2026-11-25: SFTP access is documented | capture: sha256:f3a4d819436891f6b66f65b0c9dd80962bad9c1479f9b0685edea40c6d274545 | quote: PocketHost provides SFTP access to your instance files.
  - [5] 2026-11-25: S3-compatible storage is documented for the hosted instances | capture: sha256:a0c2963d80d86c320661e15d089fa83b0282b58cf83c5414e4827f37ee57cf4b | quote: S3 storage works seamlessly with PocketBase for the following use cases:
- sources:
  - [1] https://pockethost.io/pricing
  - [2] https://pockethost.io/docs/limits
  - [3] https://pockethost.io/docs/faq
  - [4] https://pockethost.io/docs/ftp
  - [5] https://pockethost.io/docs/s3
