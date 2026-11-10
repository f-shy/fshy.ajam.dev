# bytesized hosting

> bytesized-hosting.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bytesized-hosting/ | JSON https://fshy.ajam.dev/api/v1/entity/bytesized-hosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bytesized hosting / appbox

- `storage/bytesized-hosting-appbox` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://bytesized-hosting.com/
- free tier: None reachable: No free tier at all. 'From EUR 5/month', 500 GB to 18 TB paid, add-on storage at 6 cent per 10 GB/month. Same for Free Packet ('Starting at $9.00/month') and freepacket.co. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: paid
  - dead_end.why: No free tier at all — 'From EUR 5/month', 500 GB to 18 TB paid, add-on storage at 6 cent per 10 GB/month. Same for Free Packet ('Starting at $9.00/month') and freepacket.co.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No free tier at all — 'From EUR 5/month', 500 GB to 18 TB paid, add-on storage at 6 cent per 10 GB/month. Same for Free Packet ('Starting at $9.00/month') and freepacket.co.
  - [2] 2026-10-21: cited as the basis of the rejection: No free tier at all — 'From EUR 5/month', 500 GB to 18 TB paid, add-on storage at 6 cent per 10 GB/month. Same for Free Packet ('Starting at $9.00/month') and freepacket.co.
- sources:
  - [1] https://bytesized-hosting.com/
  - [2] https://freepacket.co/seedbox.php

## bytesized hosting — appbox range

- `storage/bytesized-hosting-appbox-range` | paid-only | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:26.602Z (live) | stale on 2026-12-04
- url https://bytesized-hosting.com/plans
- free tier: none reachable: Unmetered at every tier but the per-TB rate never improves: €5/500GB (€10/TB) down to €96/18TB (€5.33/TB). Beaten on both axes by HostBrr and PulsedMedia. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Bandwidth is listed as Unmetered on a 10Gbit connection at every plan from Appbox Lite (500 GB) to Appbox +18 (18000 GB) | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: the verdict rests on the vendor plans page, read on 2026-11-03: the plan table quotes Appbox Lite (500 GB, Unmetered, 10Gbit, EUR 5) and Appbox +18 (18000 GB, Unmetered, 10Gbit, EUR 96)
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Unmetered at every tier but the per-TB rate never improves: €5/500GB (€10/TB) down to €96/18TB (€5.33/TB). Beaten on both axes by HostBrr and PulsedMedia.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Unmetered at every tier but the per-TB rate never improves: €5/500GB (€10/TB) down to €96/18TB (€5.33/TB). Beaten on both axes by HostBrr and PulsedMedia.
  - [1] 2026-11-03: the largest plan lists bandwidth as Unmetered on a 10Gbit connection at EUR 96 | capture: sha256:7850e195080f7c9746d96c0bc6a1ca8049b795398846df64fe687cdfcd3f9a95 | quote: | Appbox +18 | 18000 GB | Unmetered | 10Gbit | 10 | No redundancy | €96 |
  - [1] 2026-11-03: the smallest plan also lists bandwidth as Unmetered on a 10Gbit connection | capture: sha256:7850e195080f7c9746d96c0bc6a1ca8049b795398846df64fe687cdfcd3f9a95 | quote: | Appbox Lite | 500 GB | Unmetered | 10Gbit | 2 | No redundancy | €5 |
- sources:
  - [1] https://bytesized-hosting.com/plans
