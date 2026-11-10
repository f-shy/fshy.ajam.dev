# Sia host

> sia.tech | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sia-2/ | JSON https://fshy.ajam.dev/api/v1/entity/sia-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## skynet / siastream

- `storage/skynet-siastream` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.sia.tech/store-your-data/using-sia-storage.md
- free tier: none reachable: Skynet is gone as a free product; Sia's current offering is the 50 GB hosted Sia Storage account recorded above. The Skynet guides that still rank describe a discontinued portal model. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Skynet is gone as a free product; Sia's current offering is the 50 GB hosted Sia Storage account recorded above. The Skynet guides that still rank describe a discontinued portal model.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Skynet is gone as a free product; Sia's current offering is the 50 GB hosted Sia Storage account recorded above. The Skynet guides that still rank describe a discontinued portal model.
- sources:
  - [1] https://docs.sia.tech/store-your-data/using-sia-storage.md

## Sia host (hostd) - supply side / the arbitrage test

- `storage/sia-host-supply-side-the-arbitrage-test` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category contributed storage - become a host
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://sia.tech/provide-storage
- free tier: you set your own price; network median is $1.17/TB/month storage and $2.25/TB download (siascan), $1.30 KS/TB/month | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: you are PAID for egress ($2.25/TB median) rather than charged | metered: yes | price per TB: $2.25/TB
- identity: anonymous | detail: anonymous
- interface: cli
- limits note: THE ARBITRAGE DOES NOT EXIST, and Sia's own numbers show it precisely. A host earns the median $1.17/TB/mo; a renter pays $2-3/TB/mo for the same terabyte (the $3 figure includes 3x redundancy). So contributing N TB of disk buys you N x 1.17/3 = 0.39N TB of retail storage - you must contribute ~2.6x the disk you want to consume, and you must also lock collateral at '2-3x your base storage price' in SC, keep the machine online, and forward ports. Storing 20 TiB on Sia costs $60-70/mo, which means hosting ~51-60 TB of other people's data to break even.
- interface detail: hostd daemon (Docker/Linux/macOS/Windows), open ports, Siacoin wallet
- tooling: hostd desktop app v0.46.1, hostd CLI, siascan for competitor pricing
- composes with: earn SC, buy storage with SC on the same network - the only place where the earn and spend currencies actually match
- reliability: Lose the data or fail a proof and the collateral is burned; a single drive failure is a total loss for that contract.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: you set your own price; network median is $1.17/TB/month storage and $2.25/TB download (siascan), $1.30 KS/TB/month
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Median storage price $1.17/TB/month'; 'Median download price $2.25/TB'; 530 active hosts, 2.19 PB used of 7.12 PB
  - [2] 2026-10-21: 'Network pricing averages around $3 per terabyte per month, including 3x redundancy'
  - [3] 2026-10-21: 'set your collateral to around 2-3x your base storage price ... if you've priced your storage at 50 SC/TB, you should set your collateral at 100-150 SC/TB'
  - [4] 2026-10-21: 'Lose the data, or fail to prove you still have it, and you lose the collateral you put up'; 'Open ports - Renters connect to your host directly ... forwarding hostd's ports'
- sources:
  - [1] https://siascan.com/
  - [2] https://docs.sia.tech/store-your-data/about-renting.md
  - [3] https://docs.sia.tech/provide-storage/about-hosting-on-sia
  - [4] https://sia.tech/provide-storage
