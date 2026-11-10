# WeTransfer

> wetransfer.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wetransfer/ | JSON https://fshy.ajam.dev/api/v1/entity/wetransfer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WeTransfer

- `storage/wetransfer` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://wetransfer.com
- free tier: Free: 3 GB per transfer AND 10 transfers per rolling 30-day window (a pool, not per-send). Links live up to 3 days. Starter 10 transfers/300 GB. Ultimate unlimited transfers up to 1 TB/transfer. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 3 GB | bytes: 3000000000 | source: [1] | note: not stated
- retention: Retention: 3 days free | days: 3 | source: [1] | note: not stated
- egress: not metered. | metered: yes
- identity: email
- interface: rest
- limits:
  - retention-clamped: Retention: 3 days [1]
  - per-object-cap (binding): per-object-cap: 3 GB [1]
- limits note: per-object-cap: 3 GB free. Retention: 3 days free. request-rate effectively 10 transfers/30 days rolling. Storage (2 TB default) is an account-level concept that does not apply to free transfers.
- interface detail: rest
- tooling: Paid API; no usable free API. The useful artefact here is the help-centre plan-limits page, which states the pool semantics precisely.
- composes with: 3 GB x 10 transfers per 30 days = 30 GB/month per account, at 3-day retention. This is the weakest unit in the niche and the reason the whole category exists.
- reliability: The pricing page is JS-walled and returns 'Uh-oh.. We couldn't load some important parts of our website' through both read and the Wayback capture. The help-centre article is the only reliable source. 3 GB AND 10-per-30-days both apply; the pool is missed by most comparisons.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free: 3 GB per transfer AND 10 transfers per rolling 30-day window (a pool, not per-send). Links live up to 3 days. Starter 10 transfers/300 GB. Ultimate unlimited transfers up to 1 TB/transfer.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: (updated 30 May 2026) — 'Free — send up to 10 transfers (or 3 GB total) in any 30-day rolling window'
  - [2] 2026-10-21: probe: read -> 200 but body 'Uh-oh... We couldn't load some important parts of our website' (0 usable content)
- sources:
  - [1] https://wetransfer.com/help-center/subscriptions/plan-limits
  - [2] https://wetransfer.com/pricing
