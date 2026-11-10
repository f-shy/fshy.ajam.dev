# TransferNow

> transfernow.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/transfernow/ | JSON https://fshy.ajam.dev/api/v1/entity/transfernow.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TransferNow

- `storage/transfernow` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.transfernow.net
- free tier: 5 GB per transfer, no sign-up, 7 days, and the free plan is explicitly labelled 'No storage'. Premium €6/mo = 250 GB/transfer, 365 days, 1 TB storage. A separate API/SDK tier advertises up to 5 TB per file with 365-day retention on a 14-day free trial. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 TB per file | bytes: 5000000000000 | source: [1] | note: not stated
- retention: A separate API/SDK tier advertises up to 5 TB per file with 365-day retention on a 14-day free trial | days: 365 | source: [1] | note: not stated
- egress: not separately metered. | metered: yes
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 5 TB per file [1]
  - retention-clamped: Retention: 7 days [1]
- limits note: per-object-cap: 5 GB free. Retention: 7 days free (365 paid). request-rate: not published. The '5 TB per file' figure belongs to the paid API tier, not to free.
- interface detail: rest
- tooling: REST API + SDK exist (https://www.transfernow.net/en/discover/transfernow-api-sdk). Multipart, notifications, but behind a paid/14-day-trial plan.
- composes with: 5 GB x unlimited free 7-day transfers. Not storage: the free row literally says 'No storage'.
- reliability: Clean, honest pricing page. The free tier is a transfer service only. No free path to durability.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: 5 GB per transfer, no sign-up, 7 days, and the free plan is explicitly labelled 'No storage'. Premium €6/mo = 250 GB/transfer, 365 days, 1 TB storage. A separate API/SDK tier advertises up to 5 TB per file with 365-day retention on a 14-day free trial.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free: '5 GB per transfer ... Files available for 7 days ... No storage'; Premium 250 GB / 365 days / 1 TB storage
  - [1] 2026-10-21: API block: 'Up to 5 TB per file - Files kept up to 365 days ... 14-day free trial'
- sources:
  - [1] https://www.transfernow.net/en/prices
