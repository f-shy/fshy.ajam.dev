# Bulknews

> bulknews.eu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bulknews/ | JSON https://fshy.ajam.dev/api/v1/entity/bulknews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bulknews — free Usenet trial (10 GB)

- `storage/bulknews-free-usenet-trial` | trial-only | evidence reported | binding volume-quota | category messaging
- identity a placeholder: card and phone unknown | verified 2026-11-04T10:28:56.594Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.bulknews.eu/usenet-plans/
- free tier: Trial: 10Gb download volume at no charge, unlimited speed, 30 connections. Paid block ladder: Block 20 (20Gb, EUR 5,00), Block 30 (30Gb, EUR 10,00), Block 100 (100Gb, EUR 15,00), Block 500 (500Gb, EUR 35,00), Block 1000 (1000Gb, EUR 60,00), Block 2500 (2500Gb, EUR 90,00), Block 6000 (6000Gb, EUR 140,00). | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: unverified: the plans page states no article or object size limit | bytes: 750000 | source: [1] | note: not stated
- retention: This is a download-block trial, not free storage: you get 10 GB of retrieval, not 10 GB you can park data in permanently | source: [1] | note: not stated
- egress: Downloads are metered against the block's volume (10Gb trial, 20Gb to 6000Gb paid blocks); the Bulk plans have unlimited download size at a capped speed. | metered: yes
- identity: email
- interface: rest
- limits:
  - per-object-cap: unverified: the plans page states no article or object size limit [1]
  - volume-quota (binding): Block plans meter download volume: 10Gb trial, then 20Gb to 6000Gb blocks (EUR 5,00 to EUR 140,00); all blocks 30 connections. Bulk plans have unlimited download size at capped speed (Bulk 5: 20 Mbit, 10 connections) up to Bulk Unlimited (unlimited speed, 40 connections). [1]
- limits note: Per-object-cap: standard Usenet article size (~750 KB-1 MB practical). Request-rate: 30 connections. Retention: 10 GB is a download volume block, not a storage quota. There is no storage at all here, it is a retrieval service.
- binding note: the 10Gb trial download volume is the binding limit; the plans page states no object size cap
- interface detail: rest
- tooling: Plain NNTP (port 563 SSL), works with any newsreader or an NNTP library.
- composes with: Trial-shaped and single-use: 10 GB once per account, and Usenet accounts are tied to a paid order flow. Not repeatable at scale.
- reliability: This is a download-block trial, not free storage: you get 10 GB of retrieval, not 10 GB you can park data in permanently. Categorically the wrong shape for the workload.
- notes: Trial: 10 GB, unlimited speed, 30 connections, listed as FREE. Paid blocks start at 20 GB.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Trial: 10 GB, unlimited speed, 30 connections, listed as FREE. Paid blocks start at 20 GB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Trial / Unlimited speed / 30 Connections / 10Gb / FREE!'; next tier 'Block 20 / 20Gb'
  - [1] 2026-11-03: the trial is 10Gb, unlimited speed, 30 connections, free | capture: sha256:f605fa56132e17f62a2ce9ad035013e121118c92cb00aecba70a2e3d397b3486 | quote: Trial ### Unlimited speed ### 30 Connections ### 10Gb FREE!
  - [1] 2026-11-03: Block 20 is 20Gb for EUR 5,00 | capture: sha256:f605fa56132e17f62a2ce9ad035013e121118c92cb00aecba70a2e3d397b3486 | quote: Block 20 ### Unlimited speed ### 30 Connections ### 20Gb € 5,00
  - [1] 2026-11-03: Block 6000 is 6000Gb for EUR 140,00 | capture: sha256:f605fa56132e17f62a2ce9ad035013e121118c92cb00aecba70a2e3d397b3486 | quote: Block 6000 ### Unlimited speed ### 30 Connections ### 6000Gb € 140,00
  - [1] 2026-11-03: Bulk Unlimited has no download size limit, 40 connections | capture: sha256:f605fa56132e17f62a2ce9ad035013e121118c92cb00aecba70a2e3d397b3486 | quote: Bulk Unlimited ### Unlimited Speed ### 40 Connections ### Unlimited download size
  - [1] 2026-11-03: Bulk 5 has no download size limit at 20 Mbit, 10 connections | capture: sha256:f605fa56132e17f62a2ce9ad035013e121118c92cb00aecba70a2e3d397b3486 | quote: Bulk 5 ### 20 Mbit ### 10 Connections ### Unlimited download size
  - [1] 2026-11-03: the plans page lists volume, speed and connections per plan and states no article or object size | capture: sha256:f605fa56132e17f62a2ce9ad035013e121118c92cb00aecba70a2e3d397b3486 | quote: Block 6000 ### Unlimited speed ### 30 Connections ### 6000Gb € 140,00
  - [1] 2026-11-03: the trial is capped by a 10Gb download volume | capture: sha256:f605fa56132e17f62a2ce9ad035013e121118c92cb00aecba70a2e3d397b3486 | quote: Trial ### Unlimited speed ### 30 Connections ### 10Gb FREE!
  - [1] 2026-11-04: the top block is 6000Gb at EUR 140,00; ladder as recorded | capture: sha256:f605fa56132e17f62a2ce9ad035013e121118c92cb00aecba70a2e3d397b3486 | quote: Block 6000 ### Unlimited speed ### 30 Connections ### 6000Gb € 140,00
  - [1] 2026-11-04: trial: 10Gb at no charge, unlimited speed, 30 connections | capture: sha256:f605fa56132e17f62a2ce9ad035013e121118c92cb00aecba70a2e3d397b3486 | quote: Trial ### Unlimited speed ### 30 Connections ### 10Gb FREE!
- sources:
  - [1] https://www.bulknews.eu/usenet-plans/
