# Arweave

> ar.io | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ar/ | JSON https://fshy.ajam.dev/api/v1/entity/ar.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ardrive / turbo (arweave free tier)

- `storage/ardrive-turbo` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:55.371Z (live) | stale on 2026-12-04
- url https://docs.ar.io/sdks/ario-deploy/free-tier/
- free tier: none reachable: Free upload allowance is 105 KiB per file, 10 MiB lifetime per wallet, and 10 MiB lifetime per IP range. The IP-range meter prevents multi-account aggregation. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: 105 KiB per file (per data item). A larger file is billed. | source: [1] | note: not applicable
- retention: stated-absent: the free-tier page states no retention period; it describes free uploads to the permaweb | source: [1]
- egress: stated-absent: the free-tier page describes upload allowances and states no download or egress terms | metered: no
- identity: email
- interface: unknown
- interface detail: CLI via ario-deploy for uploads to the Arweave permaweb; no S3 or REST object interface stated
- tooling: not documented
- composes with: stated-absent: the free tier meters both wallet and IP range, so multiple wallets on one network cannot be aggregated; it composes only with added Turbo credits
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free upload allowance is 105 KiB per file, 10 MiB lifetime per wallet AND 10 MiB lifetime per IP range — the IP-range meter makes it un-multipliable, six orders of magnitude.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free upload allowance is 105 KiB per file, 10 MiB lifetime per wallet AND 10 MiB lifetime per IP range — the IP-range meter makes it un-multipliable, six orders of magnitude.
  - [1] 2026-11-19: Turbo's free upload allowance is 105 KiB per file | capture: sha256:bf7febe39d5f1bb134f9ebfe7b3ef42af8f5940460c05ae3788bb0b7f32998eb | quote: 105 KiB per file
  - [1] 2026-11-19: the first-party docs describe an ario-deploy CLI for deploying to the permaweb | capture: sha256:bf7febe39d5f1bb134f9ebfe7b3ef42af8f5940460c05ae3788bb0b7f32998eb | quote: ario-deploy can check the wallet
  - [1] 2026-11-19: the page describes free uploads and states no retention period | capture: sha256:bf7febe39d5f1bb134f9ebfe7b3ef42af8f5940460c05ae3788bb0b7f32998eb | quote: Turbo uploads small files for free.
  - [1] 2026-11-19: the first-party docs state a 105 KiB per-file cap on the free tier | capture: sha256:bf7febe39d5f1bb134f9ebfe7b3ef42af8f5940460c05ae3788bb0b7f32998eb | quote: 105 KiB per file (per data item). A larger file is billed.
  - [1] 2026-11-19: the first-party docs state a wallet cap and an IP-range cap that block multi-wallet aggregation | capture: sha256:bf7febe39d5f1bb134f9ebfe7b3ef42af8f5940460c05ae3788bb0b7f32998eb | quote: 10 MiB over the lifetime of a wallet, and 10 MiB over the lifetime of an IP range. Turbo meters both, and an upload is free only while both have allowance left.
  - [1] 2026-11-19: the page states upload limits and no download or egress allowance | capture: sha256:bf7febe39d5f1bb134f9ebfe7b3ef42af8f5940460c05ae3788bb0b7f32998eb | quote: Turbo uploads small files for free. The limits are:
- sources:
  - [1] https://docs.ar.io/sdks/ario-deploy/free-tier/

## Arweave via ar.io / Turbo (ario-deploy free tier)

- `storage/arweave-via-ar-io-turbo` | fails-quota | evidence reported | binding per-object-cap | category p2p
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:03.371Z (live) | stale on 2026-12-04
- url https://docs.ar.io/sdks/ario-deploy/free-tier/
- free tier: Turbo free tier: 105 KiB per data item, 10 MiB over the lifetime of a wallet AND 10 MiB over the lifetime of an IP range. Larger files are billed. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 105 KiB/file | bytes: 107520 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Arweave reads are effectively unmetered through gateways (arweave.net, ar.io gateways). Genuinely free egress, which is why this would otherwise be interesting. But there is nothing to serve. | metered: no
- identity: email
- interface: rest, cli
- limits:
  - per-object-cap (binding): 105 KiB/file [1]
- limits note: 105 KiB/file; 10 MiB/wallet lifetime; 10 MiB/IP-range lifetime; HTTP 402 past that.
- interface detail: rest
- tooling: ario-deploy CLI, Turbo SDK (@ardriveapp/turbo-sdk), ar.io SDK; arbundles/Irys for direct bundling.
- composes with: Actively defeated by design: the IP-range meter means the entire free allowance for a datacenter is shared. 'ario-deploy can check the wallet's allowance... It cannot check the IP range, so a deploy can pass the credit check and still be refused at upload time with HTTP 402 when other people on the same network have used the range's allowance.'
- reliability: The IP-range metering is the anti-farming mechanism, and it works: this is the one design in the class that explicitly anticipates the 'unlimited wallets' move. Confirms the prior agent's finding, with the mechanism spelled out (dual metering, wallet + range, 402 on the range).
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
  - dead_end.failure_class: quota
  - dead_end.why: Turbo free tier: 105 KiB per data item, 10 MiB over the lifetime of a wallet AND 10 MiB over the lifetime of an IP range. Larger files are billed.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '105 KiB per file (per data item)'; '10 MiB over the lifetime of a wallet, and 10 MiB over the lifetime of an IP range. Turbo meters both'
  - [1] 2026-11-19: Turbo free tier is 105 KiB per file and 10 MiB per wallet and per IP range | capture: sha256:bf7febe39d5f1bb134f9ebfe7b3ef42af8f5940460c05ae3788bb0b7f32998eb | quote: - 105 KiB per file (per data item). A larger file is billed. - 10 MiB over the lifetime of a wallet, and 10 MiB over the lifetime of an IP range. Turbo meters both, and an upload is free only while both have allowance left.
- sources:
  - [1] https://docs.ar.io/sdks/ario-deploy/free-tier/

## Arweave via Turbo / ar.io free tier

- `storage/arweave-via-turbo-ar-io-free-tier` | fails-quota | evidence reported | binding per-object-cap | category blockchain
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:03.371Z (live) | stale on 2026-12-04
- url https://turbo.ar.io
- free tier: Free tier: 105 KiB per data item, and only 10 MiB over the lifetime of a wallet AND 10 MiB over the lifetime of an IP range. Anything larger is billed in Turbo credits. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 105 KiB/file | bytes: 107520 | source: [1] | note: not stated
- retention: | Data is permanent once paid, but the free path is metered by IP range so a datacenter host fails at upload time with 402 regardless of wallet balance. | source: [1] | note: not stated
- egress: Free and permanent by design (Arweave pays storage endowment up front; gateways serve reads without metering). | metered: no
- identity: email
- interface: rest, cli
- limits:
  - per-object-cap (binding): 105 KiB/file [1]
- limits note: 105 KiB/file; 10 MiB/wallet; 10 MiB/IP-range; HTTP 402 over the cap; wallet signing required per item.
- interface detail: rest
- tooling: @ardrive/turbo-sdk, ardrive-cli, arkb, ario-deploy CLI (docs.ar.io), arweave-python-client.
- composes with: The 10 MiB wallet cap is the point: unlimited wallets x 10 MiB = still trivial, and the per-IP-range cap blocks the obvious Sybil route from one host. 20 TiB would need ~2 million wallets x 10 MiB.
- reliability: Data is permanent once paid, but the free path is metered by IP range so a datacenter host fails at upload time with 402 regardless of wallet balance.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
  - dead_end.failure_class: quota
  - dead_end.why: Free tier: 105 KiB per data item, and only 10 MiB over the lifetime of a wallet AND 10 MiB over the lifetime of an IP range. Anything larger is billed in Turbo credits.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '105 KiB per file (per data item)'; '10 MiB over the lifetime of a wallet, and 10 MiB over the lifetime of an IP range'
  - [2] 2026-10-21: 'Files under 105 KiB are completely FREE'
  - [1] 2026-11-19: Turbo free tier is 105 KiB per file and 10 MiB per wallet and per IP range | capture: sha256:bf7febe39d5f1bb134f9ebfe7b3ef42af8f5940460c05ae3788bb0b7f32998eb | quote: - 105 KiB per file (per data item). A larger file is billed. - 10 MiB over the lifetime of a wallet, and 10 MiB over the lifetime of an IP range. Turbo meters both, and an upload is free only while both have allowance left.
- sources:
  - [1] https://docs.ar.io/sdks/ario-deploy/free-tier/
  - [2] https://turbo.ar.io/
