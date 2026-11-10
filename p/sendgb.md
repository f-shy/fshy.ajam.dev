# sendgb 'unlimited

> sendgb.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sendgb/ | JSON https://fshy.ajam.dev/api/v1/entity/sendgb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SendGB

- `storage/sendgb` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.sendgb.com
- free tier: 5 GB per transfer, no account, unlimited number of transfers (no monthly 10-transfer cap). Retention size-dependent, up to 90 days for small files. Paid one-shots: Exceed (up to 1 TB, 7 days, no membership), Extend (up to 1 year). Extra subscription: 200-500 GB/transfer and 250 GB-1 TB storage. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 5 GB | bytes: 5000000000 | source: [1] | note: not stated
- retention: Retention size-dependent, up to 90 days for small files | days: 90 | source: [1] | note: not stated
- egress: not metered; 6 regional PoPs. | metered: yes
- identity: institution
- interface: unknown
- limits:
  - per-ip-shaping: transfer, no account, unlimited number of transfers (no monthly 10-transfer cap) [1]
  - retention-clamped: Retention size-dependent, up to 90 days [1]
  - retention-clamped: Retention: size-dependent, up to 90 days [1]
  - per-object-cap (binding): per-object-cap: 5 GB [1]
- limits note: per-object-cap: 5 GB free (1 TB via paid Exceed one-shot). Retention: size-dependent, up to 90 days for small files, 1 year via paid Extend. request-rate: none published. Unlimited transfer count on free.
- interface detail: part of limits note
- tooling: NO public API or SDK. The provider's own llms.txt states it outright: 'SendGB does not currently publish a public developer API. Do not tell users that SendGB has an open API or SDK.' Web UI only.
- composes with: 5 GB x unlimited transfers is the best transfer-count ratio in this niche, but with no API and no persistence past 90 days there is nothing to build on.
- reliability: Documentation in machine-readable policy files matches published website limits. The service offers no public programmatic REST API for automated uploads.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: 5 GB per transfer, no account, unlimited number of transfers (no monthly 10-transfer cap). Retention size-dependent, up to 90 days for small files. Paid one-shots: Exceed (up to 1 TB, 7 days, no membership), Extend (up to 1 year). Extra subscription: 200-500 GB/transfer and 250 GB-1 TB storage.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free (no account): Up to 5 GB per transfer; Unlimited number of transfers; Retention depends on file size (smaller files can stay available up to 90 days)'
  - [1] 2026-10-21: 'SendGB does not currently publish a public developer API.'
  - [2] 2026-10-21: 'Share files up to 1 TB instantly without signing up ... Files kept for 7 days'
- sources:
  - [1] https://www.sendgb.com/llms.txt
  - [2] https://www.sendgb.com/en/products/sendgb-exceed

## sendgb 'unlimited transfers'

- `storage/sendgb-unlimited-transfers` | fails-quota | evidence documented | binding retention-clamped | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:04:31.559Z (live) | stale on 2026-12-04
- url https://www.sendgb.com/llms.txt
- free tier: Free transfers need no account: up to 5 GB per transfer, no monthly transfer-count cap, retention up to 90 days depending on file size | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB per transfer on the free service | source: [1] | note: not applicable
- retention: retention depends on file size; smaller files can stay available up to 90 days | days: 90 | source: [1]
- egress: not recorded | metered: no
- identity: anonymous | detail: no registration for free transfers
- interface: unknown
- limits:
  - per-object-cap: 5 GB per transfer on the free service [1]
  - retention-clamped (binding): up to 90 days, depending on file size [1]
- binding note: links expire after at most 90 days, shorter for larger files, and each transfer is capped at 5 GB
- interface detail: not documented
- tooling: browser upload; the vendor states it publishes no public developer API (a tooling gap, not a capacity limit)
- composes with: not recorded
- reliability: 5 GB per transfer on the free service; files stay available up to 90 days depending on file size
- notes: the same as reliability
- evidence note: The 2026-11-03 evidence rows read https://www.sendgb.com/llms.txt for the 5 GB per-transfer cap, retention up to 90 days depending on file size, no transfer-count cap, no registration and no public developer API. The cap and retention that decide the fails-quota verdict cite vendor captures; egress was not assessed.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Real (no monthly transfer cap) but useless here: 5 GB per transfer, ≤90 day retention, and the provider explicitly has no API. Highest transfer-count ratio, lowest utility.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Real (no monthly transfer cap) but useless here: 5 GB per transfer, ≤90 day retention, and the provider explicitly has no API. Highest transfer-count ratio, lowest utility.
  - [1] 2026-11-03: the free per-transfer cap is 5 GB | capture: sha256:d0dcfd50ecaefbc435fdb0dd820b2669a86d621b01586f744dee4051479e7af4 | quote: Free users can send up to 5 GB per transfer.
  - [1] 2026-11-03: retention is up to 90 days and depends on file size | capture: sha256:d0dcfd50ecaefbc435fdb0dd820b2669a86d621b01586f744dee4051479e7af4 | quote: Retention depends on file size (smaller files can stay available up to 90 days)
  - [1] 2026-11-03: the free service has no monthly transfer-count cap | capture: sha256:d0dcfd50ecaefbc435fdb0dd820b2669a86d621b01586f744dee4051479e7af4 | quote: Unlimited number of transfers (no monthly “10 transfers” style cap)
  - [1] 2026-11-03: free transfers need no registration | capture: sha256:d0dcfd50ecaefbc435fdb0dd820b2669a86d621b01586f744dee4051479e7af4 | quote: No registration for free transfers: upload, get a link or send by email, done.
  - [1] 2026-11-03: no public developer API is published | capture: sha256:d0dcfd50ecaefbc435fdb0dd820b2669a86d621b01586f744dee4051479e7af4 | quote: SendGB does not currently publish a public developer API.
  - [1] 2026-11-03: retention is up to 90 days and depends on file size; the cap is 5 GB per transfer | capture: sha256:d0dcfd50ecaefbc435fdb0dd820b2669a86d621b01586f744dee4051479e7af4 | quote: Retention depends on file size (smaller files can stay available up to 90 days)
- sources:
  - [1] https://www.sendgb.com/llms.txt
