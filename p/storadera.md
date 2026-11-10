# Storadera Space

> storadera.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/storadera/ | JSON https://fshy.ajam.dev/api/v1/entity/storadera.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Storadera Space Premium

- `storage/storadera-space-premium` | fails-egress | evidence reported | binding none | category S3-compatible object storage (Finland)
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://storadera.com/pricing
- price €7.95/TB/mo flat at the 5 TB and 20 TB tiers ($8.59 at 1.08). at 5 TB: €7.95/TB/mo. at 20 TB: €7.95/TB/mo. Priced like Wasabi, metered like InterServer — dominated on both axes. | parsed USD 8.96/TB-mo
- free tier: €7.95 per TB per month, granular per-byte, no minimum. 50 GB free for 30 days. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: "No download charges*" with the asterisk resolving to "the provider applies. The allowed download amount equals to your stored amount." So egress is capped at exactly 1x stored capacity per month. This is the clearest example of 'no download charges' that is nonetheless metered. | metered: yes
- identity: email | detail: email
- interface: s3-compatible, rclone
- limits note: Egress = 1x storage per month. No minimum storage duration and no minimum file size. Which is genuinely unusual and good for a churning hot set.
- interface detail: S3-compatible API
- tooling: rclone `s3`, any S3 SDK
- composes with: S3 + Cloudflare works, but the 1x egress ceiling means a Cloudflare cache miss storm costs you the month.
- reliability: Finnish storage provider with published public pricing page and standard service tier documentation.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: €7.95 per TB per month, granular per-byte, no minimum. 50 GB free for 30 days.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: €7.95/TB/mo flat at the 5 TB and 20 TB tiers ($8.59 at 1.08). at 5 TB: €7.95/TB/mo. at 20 TB: €7.95/TB/mo. Priced like Wasabi, metered like InterServer — dominated on both axes.
- evidence:
  - [1] 2026-10-21: 
- sources:
  - [1] https://storadera.com/pricing

## storadera

- `storage/storadera` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://storadera.com/pricing
- free tier: none reachable: €7.95/TB/mo with a hard fair-use rule that equals the storage: 'The allowed download amount equals to your stored amount.' That is 1× storage/month, i.e. precisely the 1:1 ratio that fails… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: €7.95/TB/mo with a hard fair-use rule that equals the storage: 'The allowed download amount equals to your stored amount.' That is 1× storage/month, i.e. precisely the 1:1 ratio that fails…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: €7.95/TB/mo with a hard fair-use rule that equals the storage: 'The allowed download amount equals to your stored amount.' That is 1× storage/month, i.e. precisely the 1:1 ratio that fails…
- sources:
  - [1] https://storadera.com/pricing
