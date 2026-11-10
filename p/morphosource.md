# MorphoSource

> morphosource.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/morphosource/ | JSON https://fshy.ajam.dev/api/v1/entity/morphosource.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MorphoSource

- `storage/morphosource` | fails-quota | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.morphosource.org
- free tier: 'MorphoSource is able to subsidize or support free contribution of data for most users with 100GB or less.' 100 GB–1 TB is case-by-case (may be fully free); >1 TB is $3.47/GB + $30. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'users are never charged for data consumption. Whether that means viewing or downloading data, there are no costs associated with using data.' | metered: yes
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): application-gated [1]
- limits note: Per-object-cap: none published; the binding cap is a per-identity total of 100 GB free (100 GB–1 TB discretionary). Retention: 'retain all data .. for as long as MorphoSource continues to exist'. No expiry but no endowment either. Contributor status is application-gated.
- interface detail: rest
- tooling: Web upload + batch submission tooling (Duke wiki 'Batch Submission'); no public upload API. Read side serves media files over HTTPS per-record.
- composes with: Per-user total contribution is tracked ('these data size limits apply to the total contribution of data by a user or institution'), so 100 GB is per identity, not per record. Multiple contributor identities multiply it. Read side free regardless.
- reliability: Funding-dependent: the docs themselves state the free 100 GB subsidy is time-limited and will likely fall to ~15 GB within 2–5 years. Treat the current number as decaying.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'MorphoSource is able to subsidize or support free contribution of data for most users with 100GB or less.' 100 GB–1 TB is case-by-case (may be fully free); >1 TB is $3.47/GB + $30.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 100 GB free, 1 TB discretionary, $3.47/GB above, 'likely around 15GB' future model
- sources:
  - [1] https://duke.atlassian.net/wiki/spaces/MD/pages/274268722/Data+Deposit+Costs
