# MyAirBridge

> myairbridge.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/myairbridge/ | JSON https://fshy.ajam.dev/api/v1/entity/myairbridge.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MyAirBridge

- `storage/myairbridge` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.myairbridge.com/en
- free tier: 20 GiB per transfer free, no registration required; storage ('save to storage') is a paid-plan feature. | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 20 GiB | bytes: 21474836480 | source: [1] | note: not stated
- retention: per-object-cap 20 GiB per transfer; retention 3 days free (2 days for transfers over 2 GB), 10/20/30 days paid, indefinite only in paid storage; per-ip-shaping for >2 GB (deprioritised bandwidth). | days: 3 | source: [1] | note: not stated
- egress: Free for the transfer; free transfers >2 GB are throttled to leftover capacity ('the user can use only available capacity that is not being used at that moment by subscribers'). | metered: no
- identity: anonymous
- interface: s3, webdav
- limits:
  - retention-clamped: retention 3 days [1]
  - per-object-cap (binding): per-object-cap 20 GiB [1]
- limits note: per-object-cap 20 GiB per transfer; retention 3 days free (2 days for transfers over 2 GB), 10/20/30 days paid, indefinite only in paid storage; per-ip-shaping for >2 GB (deprioritised bandwidth).
- interface detail: web-only (no published API/S3/WebDAV)
- tooling: none found
- composes with: Free transfers allow up to 20 GiB per transfer with temporary retention of 3 days (2 days for files over 2 GB).
- reliability: Free data is 'automatically deleted after three days (for transfers over 2 GB, after two days)'; sustained free use competes with subscriber traffic for bandwidth.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 20 GiB per transfer free, no registration required; storage ('save to storage') is a paid-plan feature.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: (title + body) — 'Send or share big files up to 20 GiB for free'
  - [1] 2026-10-21: 'your data will be automatically deleted after three days (for transfers over 2 GB, after two days)', 'Transfers up to 2 GB are given priority free of charge. For transfers over 2 GB, the user can use only available capacity that is not being used at that moment by subscribers', 'Data in your storage does not expire ... as long as your paid profile is active'
- sources:
  - [1] https://info.myairbridge.com/en/faq/
  - [2] https://www.myairbridge.com/en
