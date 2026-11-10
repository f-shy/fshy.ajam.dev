# Arweave

> ar.io | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ar/ | JSON https://fshy.ajam.dev/api/v1/entity/ar.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ardrive / turbo (arweave free tier)

- `storage/ardrive-turbo` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.ar.io/sdks/ario-deploy/free-tier/
- free tier: none reachable: Free upload allowance is 105 KiB per file, 10 MiB lifetime per wallet, and 10 MiB lifetime per IP range. The IP-range meter prevents multi-account aggregation. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: egress
  - dead_end.why: Free upload allowance is 105 KiB per file, 10 MiB lifetime per wallet AND 10 MiB lifetime per IP range — the IP-range meter makes it un-multipliable, six orders of magnitude.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free upload allowance is 105 KiB per file, 10 MiB lifetime per wallet AND 10 MiB lifetime per IP range — the IP-range meter makes it un-multipliable, six orders of magnitude.
- sources:
  - [1] https://docs.ar.io/sdks/ario-deploy/free-tier/

## Arweave via ar.io / Turbo (ario-deploy free tier)

- `storage/arweave-via-ar-io-turbo` | fails-quota | evidence reported | binding per-object-cap | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://docs.ar.io/sdks/ario-deploy/free-tier/

## Arweave via Turbo / ar.io free tier

- `storage/arweave-via-turbo-ar-io-free-tier` | fails-quota | evidence reported | binding per-object-cap | category blockchain
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://docs.ar.io/sdks/ario-deploy/free-tier/
  - [2] https://turbo.ar.io/
