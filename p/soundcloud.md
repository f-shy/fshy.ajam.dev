# soundcloud

> soundcloud.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/soundcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/soundcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## soundcloud — basic (free) plan

- `storage/soundcloud-basic-plan` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:27.378Z (live) | stale on 2026-12-04
- url https://soundcloud.com/getstarted/pricing
- free tier: None reachable: Only 2 hours of total upload time (not per month. Lifetime), which at 128 kbps is ~110 MB of audio for the entire account. 4 GB per file and 24 h per track look generous but the 2-hour acco. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Only 2 hours of total upload time (not per month — lifetime), which at 128 kbps is ~110 MB of audio for the entire account. 4 GB per file and 24 h per track look generous but the 2-hour…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Only 2 hours of total upload time (not per month — lifetime), which at 128 kbps is ~110 MB of audio for the entire account. 4 GB per file and 24 h per track look generous but the 2-hour…
  - [2] 2026-10-21: cited as the basis of the rejection: Only 2 hours of total upload time (not per month — lifetime), which at 128 kbps is ~110 MB of audio for the entire account. 4 GB per file and 24 h per track look generous but the 2-hour acco
  - [3] 2026-10-21: cited as the basis of the rejection: Only 2 hours of total upload time (not per month — lifetime), which at 128 kbps is ~110 MB of audio for the entire account. 4 GB per file and 24 h per track look generous but the 2-hour acco
  - [2] 2026-11-19: the Basic plan has a two-hour total upload allowance | capture: sha256:c03d5bdd3928cd26ad177bd648c5540e9e255030bc29cf07be35fb9d1234a2c2 | quote: Basic | Up to 2 hours total
  - [1] 2026-11-19: the pricing page lists a two-hour upload limit for the Basic Free plan | capture: sha256:0c00385c3595dd7de1f246fc4e6852ef7508a5a1f626d43173a05c90998fe3d4 | quote: Upload limit | 2 hours
- sources:
  - [1] https://soundcloud.com/getstarted/pricing
  - [2] https://help.soundcloud.com/hc/en-us/articles/360039171614-Upload-Requirements
  - [3] https://help.soundcloud.com/hc/en-us/articles/31423603670043
