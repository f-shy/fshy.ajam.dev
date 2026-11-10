# Box

> box.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/box/ | JSON https://fshy.ajam.dev/api/v1/entity/box.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Box (free developer plan)

- `storage/box` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developer.box.com/
- free tier: 10 GB storage, 250 MB file upload limit, 1 file version | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 250 MB per file | bytes: 250000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Bandwidth is fair-use monitored per account and per shared link, with a monthly reset; exceeding it can disable uploads/downloads. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-ip-shaping: 500 GB/day [1]
  - per-object-cap (binding): 250 MB per file [1]
  - per-object-cap (binding): 250 MB/file [1]
- limits note: 250 MB per file; 1,000 AI units/month; monthly bandwidth fair-use cap; some endpoints paid-only.
- interface detail: rest
- tooling: Native rclone backend 'box' (Tier 1); full REST API with OAuth2 / JWT / Client Credentials Grant on the free dev plan.
- composes with: 10 GB x unlimited free developer accounts (email + app registration). 250 MB per file forces sharding of any real dataset.
- reliability: REST API with 250 MB per-file upload cap and fair-use bandwidth limits on free developer accounts.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 GB storage, 250 MB file upload limit, 1 file version
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '10 GB storage, a 250 MB file upload limit, and 1 file version'
  - [2] 2026-10-21: 'Box monitors Bandwidth for fair use purposes on an account basis and a shared link basis... Exceeding the Box Bandwidth limit may limit or disable uploads and downloads'
- sources:
  - [1] https://developer.box.com/guides/getting-started/free-developer-plan
  - [2] https://support.box.com/hc/en-us/articles/360044194313-Understanding-Box-Bandwidth-Limits
