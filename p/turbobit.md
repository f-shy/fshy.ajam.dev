# Turbobit

> turbobit.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/turbobit/ | JSON https://fshy.ajam.dev/api/v1/entity/turbobit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Turbobit

- `storage/turbobit` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://turbobit.net
- free tier: Unlimited total: 'The total volume and number of your files are unlimited'. Free unregistered uploads are capped at 200 MB; registered free accounts go much higher (operator advertises up to 100 GB file transfer volume). | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: file size ceiling well above 200 MB | bytes: 200000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free downloads: ~5 GB/day per user with a hard speed cap and IP queueing. Turbo: 40 GB/day and 600 GB/month. No per-GB price. | metered: no | free allowance: 600 GB per month
- identity: anonymous
- interface: rest, ftp, rclone
- limits:
  - per-ip-shaping: 5 GB/day [1]
  - per-ip-shaping: 60 KB/s [1]
  - per-object-cap (binding): file size ceiling well above 200 MB [1]
- limits note: Registered free: file size ceiling well above 200 MB (unregistered 200 MB). Retention: files expire after inactivity ('storage time expiration' is a listed deletion reason). Free download ~5 GB/day, 55-60 KB/s class throttling on the sister host. Turbo 40 GB/day, 600 GB/month.
- interface detail: rest
- tooling: Turbobit Uploader desktop app, FTP upload, and third-party rclone/JDownloader support; no first-party public REST API documented.
- composes with: Unlimited total per account is the headline; with email-only registration the chain is N accounts. The 40 GB/day cap is per download identity, so serving volume scales with IPs, not accounts.
- reliability: Free-tier serving is throttled to dial-up speeds and gated behind a human-verification step and a queue, so it works as storage but not as a fetch origin. Dyna mic Download Splitting means the previous file's size sets your next wait.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Store as many files as you want — The total volume and number of your files are unlimited'
  - [2] 2026-10-21: 'If you are a free user, you may download about 5 Gb a day'; Turbo '40 Gb a day, 600 Gb per month'; 'storage time expiration' is a deletion reason
  - [3] 2026-10-21: plan table 100 GB trial / 600 GB / 3600 GB / 7200 GB / 14400 GB bandwidth blocks
- sources:
  - [1] https://turbobit.net/?site_version=normal
  - [2] https://turbobit.net/faq
  - [3] https://turbobit.net/premium
