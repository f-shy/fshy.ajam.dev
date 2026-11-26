# appsumo pcloud

> dealkeep.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dealkeep/ | JSON https://fshy.ajam.dev/api/v1/entity/dealkeep.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## appsumo pcloud 500 gb and icedrive lifetime listings

- `storage/appsumo-pcloud-500-gb-and-icedrive-lifetime-listings` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:55.370Z (live) | stale on 2026-12-04
- url https://www.dealkeep.io/blog/pcloud-lifetime-deal
- free tier: None reachable: Both SOLD OUT / withdrawn. The AppSumo 60-day refund window. The main protection a lifetime buyer had. Is therefore unavailable for storage. pCloud and Icedrive now sell lifetime only dire. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the deal page states no per-object size cap | source: [1] | note: not applicable
- retention: stated-absent: the deal page states no retention period for stored bytes; it mentions only a 14-day money-back window on direct pCloud plans | source: [1]
- egress: stated-absent: the deal page states no egress terms for stored bytes | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the deal page states no storage client interface; it describes a sold-out AppSumo lifetime listing and direct lifetime plans on pcloud.com
- tooling: not documented
- composes with: stated-absent: the deal page states no way to chain this lifetime listing with other services; the AppSumo route is closed and lifetime plans are sold only direct
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Both SOLD OUT / withdrawn. The AppSumo 60-day refund window — the main protection a lifetime buyer had — is therefore unavailable for storage. pCloud and Icedrive now sell lifetime only…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Both SOLD OUT / withdrawn. The AppSumo 60-day refund window — the main protection a lifetime buyer had — is therefore unavailable for storage. pCloud and Icedrive now sell lifetime only…
  - [1] 2026-11-19: the AppSumo 500 GB lifetime listing is still sold out, so the rejection stands | capture: sha256:08caea6483d865be56d565fcb0afb39ca569ecdd767fa2b342f2142770549161 | quote: The listing "pCloud 500 GB lifetime" shows "Sold out" and "This deal is unavailable".
  - [1] 2026-11-19: pCloud's lifetime plans are sold direct, not through AppSumo, so no free AppSumo storage offer exists | capture: sha256:08caea6483d865be56d565fcb0afb39ca569ecdd767fa2b342f2142770549161 | quote: pCloud still sells lifetime storage direct: 500 GB for $219,
  - [1] 2026-11-19: the AppSumo listing is gone and the page states no storage client interface | capture: sha256:08caea6483d865be56d565fcb0afb39ca569ecdd767fa2b342f2142770549161 | quote: The AppSumo route is closed.
  - [1] 2026-11-19: the only period named is a refund window, not a byte-retention term | capture: sha256:08caea6483d865be56d565fcb0afb39ca569ecdd767fa2b342f2142770549161 | quote: 14 days, stated on the pricing page as "14 days money back guarantee"
  - [1] 2026-11-19: the page describes a sold-out lifetime listing and names no per-object cap | capture: sha256:08caea6483d865be56d565fcb0afb39ca569ecdd767fa2b342f2142770549161 | quote: The AppSumo listing shows "Sold out" and "This deal is unavailable".
- sources:
  - [1] https://www.dealkeep.io/blog/pcloud-lifetime-deal

## filen lifetime plans

- `storage/filen-lifetime-plans` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:38.130Z (live) | stale on 2026-12-04
- url https://www.dealkeep.io/blog/lifetime-cloud-storage
- free tier: none reachable: WITHDRAWN. Filen phased out Pro lifetime after Black Friday 2025 and has kept the Starter lifetime unavailable since January 2026, citing hardware costs. Existing holders kept theirs… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: WITHDRAWN. Filen phased out Pro lifetime after Black Friday 2025 and has kept the Starter lifetime unavailable since January 2026, citing hardware costs. Existing holders kept theirs…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: WITHDRAWN. Filen phased out Pro lifetime after Black Friday 2025 and has kept the Starter lifetime unavailable since January 2026, citing hardware costs. Existing holders kept theirs…
  - [2] 2026-10-21: cited as the basis of the rejection: WITHDRAWN. Filen phased out Pro lifetime after Black Friday 2025 and has kept the Starter lifetime unavailable since January 2026, citing hardware costs. Existing holders kept theirs; nobody
  - [1] 2026-11-19: the lifetime tracker still records Filen lifetime plans as withdrawn, with existing holders keeping theirs | capture: sha256:2d5dfa2b0405dc8187e17bef92d98598989ff495fe6766fe264a45343d017658 | quote: No. Filen phased out its Pro lifetime plans after Black Friday 2025 and has kept its Starter lifetime plan unavailable since January 2026 without promising a return. Existing holders keep their plans.
- sources:
  - [1] https://www.dealkeep.io/blog/lifetime-cloud-storage
  - [2] https://filen.io/pricing
