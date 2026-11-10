# contentful

> contentful.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/contentful/ | JSON https://fshy.ajam.dev/api/v1/entity/contentful.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## contentful (free / starter space)

- `storage/contentful` | fails-egress | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:23.414Z (live) | stale on 2026-12-04
- url https://www.contentful.com/help/admin/usage/usage-limit/
- free tier: none reachable: Files are capped at 50 MB each and asset bandwidth at 50 GB/month with NO overage purchasable on Free; only 1 Starter space, 100k API calls/month. Storage size itself is not published as a… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Free plan: 50 GB asset bandwidth per month and no additional consumption allowed. Lite plan: 100 GB per month included, extra bandwidth billed at USD / EUR 0.15 per GB. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: the vendor pages of the 2026-11-03 evidence rows were read and captured (https://www.contentful.com/help/admin/usage/usage-limit/); every field that decides the verdict cites one of those captures
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Files are capped at 50 MB each and asset bandwidth at 50 GB/month with NO overage purchasable on Free; only 1 Starter space, 100k API calls/month. Storage size itself is not published as a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Files are capped at 50 MB each and asset bandwidth at 50 GB/month with NO overage purchasable on Free; only 1 Starter space, 100k API calls/month. Storage size itself is not published as a…
  - [1] 2026-11-03: Free plan asset bandwidth is 50 GB per month | capture: sha256:cd6bac4e9c76c99297d3ed67ccc065e41f179899c662ed22d216a49b17e25031 | quote: | Asset bandwidth | 50 | Gigabytes (GB) per month |
  - [1] 2026-11-03: Free plan bandwidth cannot be exceeded | capture: sha256:cd6bac4e9c76c99297d3ed67ccc065e41f179899c662ed22d216a49b17e25031 | quote: Additional API calls and asset bandwidth consumption are not allowed.
  - [1] 2026-11-03: Lite overage bandwidth is priced per GB | capture: sha256:cd6bac4e9c76c99297d3ed67ccc065e41f179899c662ed22d216a49b17e25031 | quote: Extra asset bandwidth consumption will be billed at USD / EUR 0.15 per Gigabyte (GB) monthly.
- sources:
  - [1] https://www.contentful.com/help/admin/usage/usage-limit/
