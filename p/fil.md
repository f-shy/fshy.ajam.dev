# Fil

> fil.one | Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fil/ | JSON https://fshy.ajam.dev/api/v1/entity/fil.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fil One (formerly Storacha / web3.storage successor)

- `storage/fil-one` | trial-only | evidence reported | binding retention-clamped | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.fil.one/pricing/
- disagrees on identity_kind: `storage/fil-one` says card, `storage/fil-one-storacha-s3-tier` says email
- free tier: No standing free tier: '1 TB free for 30 days · No credit card required' and '1 TB of storage and 2 TB of egress for 30 days'. After that '$5.99 per TB stored per month' with a 1 TB minimum. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: retention: 30 days (trial) | days: 30 | source: [1] | note: not stated
- egress: '$0 Egress and API requests — Subject to reasonable use.' Explicitly excludes 'CDN-like use cases, where egress runs at many times the amount stored'. | metered: yes
- identity: card
- interface: s3-compatible
- limits:
  - retention-clamped (binding): retention: 30 days [1]
- limits note: per-object-cap: not stated. retention: 30 days (trial). request-rate: none. Binding constraint is the trial clock, then $5.99/TB with a 1 TB billing minimum.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: s3
- tooling: S3-compatible buckets with scoped keys.
- composes with: 30-day trial x unlimited accounts is a treadmill, not storage. The data must be re-uploaded every 30 days and each new account needs a distinct signup.
- reliability: Reasonable-use clause explicitly targets egress-heavy workloads and says they 'will contact you first'. A shaping/ban path for serving use.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: No standing free tier: '1 TB free for 30 days · No credit card required' and '1 TB of storage and 2 TB of egress for 30 days'. After that '$5.99 per TB stored per month' with a 1 TB minimum.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '1 TB free for 30 days · No credit card required'; 'Yes, $5.99 a month. Store under 1 TB and you pay the minimum'
  - [2] 2026-10-21: the older Arweave/Turbo free path: '105 KiB per file', '10 MiB over the lifetime of a wallet, and 10 MiB over the lifetime of an IP range'
- sources:
  - [1] https://www.fil.one/pricing/
  - [2] https://docs.ar.io/sdks/ario-deploy/free-tier/

## fil one / storacha s3 tier

- `storage/fil-one-storacha-s3-tier` | trial-only | evidence documented | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-04T01:24:13.492Z (live) | stale on 2026-12-05
- url https://www.fil.one/pricing/
- disagrees on identity_kind: `storage/fil-one` says card, `storage/fil-one-storacha-s3-tier` says email
- free tier: none reachable: Marketed as cheap S3 ($5.99/TB/month, $0 egress) but the free component is a 30-day 1 TB trial, not a free tier. Below the archive requirement and time-boxed. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: On the paid plan egress costs $0, subject to reasonable use, with no numeric cap stated; the 30-day trial includes 2 TB of egress. | metered: no
- identity: email | detail: the 30-day trial needs no credit card; the other sign-up fields are not stated on the pricing page
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Documented from the vendor page https://www.fil.one/pricing/ re-read on 2026-11-04: 30-day trial of 1 TB storage and 2 TB egress with no credit card; paid egress free subject to reasonable use.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Marketed as cheap S3 ($5.99/TB/month, $0 egress) but the free component is a 30-day 1 TB trial, not a free tier. Below the archive requirement and time-boxed.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Marketed as cheap S3 ($5.99/TB/month, $0 egress) but the free component is a 30-day 1 TB trial, not a free tier. Below the archive requirement and time-boxed.
  - [1] 2026-11-03: paid egress is $0 under a reasonable-use condition with no numeric cap; the trial carries 2 TB of egress | capture: sha256:cb29291eb5c86b092ba095aaa2198f1669502dd053daccd260870c4a3f84f89f | quote: On a paid plan there is no egress charge, subject to reasonable use, and no per-request charges either. The 30-day trial includes 2 TB of egress.
  - [1] 2026-11-03: the free component is a 30-day trial of 1 TB storage and 2 TB egress with no card | capture: sha256:cb29291eb5c86b092ba095aaa2198f1669502dd053daccd260870c4a3f84f89f | quote: 1 TB of storage and 2 TB of egress for 30 days, with no credit card required.
  - [1] 2026-11-04: the free component is a 30-day trial of 1 TB storage and 2 TB egress with no card | capture: sha256:cb29291eb5c86b092ba095aaa2198f1669502dd053daccd260870c4a3f84f89f | quote: 1 TB of storage and 2 TB of egress for 30 days, with no credit card required.
- sources:
  - [1] https://www.fil.one/pricing/

## storacha / fil one

- `storage/storacha-fil-one` | trial-only | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:43.354Z (live) | stale on 2026-12-05
- url https://www.fil.one/pricing
- free tier: none reachable: 1 TB free but for 30 days only, with 2 TB of egress in the trial: '1 TB free for 30 days · No credit card required ... The 30-day trial includes 2 TB of egress.' After that it is… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: No egress charge on a paid plan, subject to reasonable use; the 30-day trial includes 2 TB of egress | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: re-read on 2026-11-03: the vendor pricing page https://www.fil.one/pricing; it states the 30-day trial of 1 TB of storage and 2 TB of egress with no credit card, the $5.99 per TB per month paid rate and no egress charge on a paid plan subject to reasonable use; interface, tooling and per-object cap are not stated there
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 1 TB free but for 30 days only, with 2 TB of egress in the trial: '1 TB free for 30 days · No credit card required ... The 30-day trial includes 2 TB of egress.' After that it is…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 1 TB free but for 30 days only, with 2 TB of egress in the trial: '1 TB free for 30 days · No credit card required ... The 30-day trial includes 2 TB of egress.' After that it is…
  - [1] 2026-11-03: paid egress is not charged, subject to reasonable use; the free offer is a 30-day trial with 2 TB of egress | capture: sha256:cb29291eb5c86b092ba095aaa2198f1669502dd053daccd260870c4a3f84f89f | quote: On a paid plan there is no egress charge, subject to reasonable use, and no per-request charges either. The 30-day trial includes 2 TB of egress.
  - [1] 2026-11-04: the free offer is a 30-day trial of 1 TB storage and 2 TB egress with no card | capture: sha256:cb29291eb5c86b092ba095aaa2198f1669502dd053daccd260870c4a3f84f89f | quote: 1 TB of storage and 2 TB of egress for 30 days, with no credit card required.
- sources:
  - [1] https://www.fil.one/pricing

## nft.storage

- `storage/nft-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.fil.one/pricing/
- free tier: None reachable: Already known to the swarm: the Classic free upload service was decommissioned 2024-06-30. The surviving site sells 'a small one-time fee' per NFT collection with an onchain endowment. No b. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Already known to the swarm: the Classic free upload service was decommissioned 2024-06-30. The surviving site sells 'a small one-time fee' per NFT collection with an onchain endowment — no…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Already known to the swarm: the Classic free upload service was decommissioned 2024-06-30. The surviving site sells 'a small one-time fee' per NFT collection with an onchain endowment — no…
- sources:
  - [1] https://www.fil.one/pricing/
