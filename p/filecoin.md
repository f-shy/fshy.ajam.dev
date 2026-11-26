# Filecoin Onchain

> filecoin.cloud | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filecoin/ | JSON https://fshy.ajam.dev/api/v1/entity/filecoin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filecoin Onchain Cloud (FWSS / Filecoin Pay)

- `storage/filecoin-onchain-cloud` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category contributed storage - on-chain paid deals
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T21:13:26.682Z (live) | stale on 2026-12-04
- url https://docs.filecoin.cloud/cookbooks/payments-and-storage/
- price $2.50/TiB storage + up to $14/TiB egress | parsed USD 2.27/TB-mo
- free tier: $2.50/TiB/month per copy, plus $0.12 per data-set/month proving fee. 20 TiB = $50/mo per copy; two copies = $100/mo | unit: TiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: CDN egress 'up to $14/TiB (about $0.014/GiB) downloaded' via Filecoin Beam, about half that from cache. 1 TiB/day = 30 TiB/mo = up to $420/mo | metered: yes | free allowance: 30 TiB per month
- identity: card | detail: card
- interface: unknown
- limits:
  - per-ip-shaping (binding): 1 TiB/day [1]
- limits note: Storage at $2.50/TiB is genuinely competitive, but total cost of ownership is dominated by egress: $420/mo of CDN to serve 1 TiB/day on top of $100/mo of storage = $520/mo. Also gated on holding USDFC (a stablecoin) and a refundable ~$0.50 lifecycle reserve per data set; each add-pieces call costs $0.008 + $0.003/piece, which is punitive for a 20 TiB corpus of many small objects.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: Synapse SDK; FWSS (Filecoin Warm Storage Service); Filecoin Pay streaming payments
- tooling: synapse-sdk, USDFC deposits, lotus/curio on the provider side
- composes with: Features low-cost on-chain storage capacity paired with metered egress fees, suitable for cold archival storage.
- reliability: Requires a funded stablecoin wallet; deals are 30-day-epoch denominated and stream payments continuously.
- notes: the same as the free tier
- extras:
  - price_verbatim: $2.50/TiB storage + up to $14/TiB egress
- evidence:
  - [1] 2026-10-21: pricing table: 'Storage $2.50/TiB/month per copy'; 'Proving Service $0.12/data set/month'; 'CDN egress up to $14/TiB (≈ $0.014/GiB) downloaded'; 'Add pieces $0.008 + $0.003 per piece'
  - [1] 2026-10-21: 'No CDN ~0.50 USDFC (lifecycle reserve lockup)' minimum to create a data set
  - [2] 2026-10-21: verified deals required allocator approval and DataCap (now historical)
  - [1] 2026-11-19: storage is $2.50/TiB/month per copy plus a $0.12/data set/month proving fee, and CDN egress is up to $14/TiB | capture: sha256:3c5676c8403160f28be32e1840ace063e8025b71a2ba4fcee846b00a3a756945 | quote: | Storage | $2.50/TiB/month per copy | Charged only while pieces exist. Empty data sets have no recurring cost |
- sources:
  - [1] https://docs.filecoin.cloud/cookbooks/payments-and-storage/
  - [2] https://docs.filecoin.io/provide-storage/filecoin-deals/verified-deals

## filecoin pin (pin.filecoin.cloud)

- `storage/filecoin-pin` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:37.562Z (live) | stale on 2026-12-04
- url https://pin.filecoin.cloud/
- free tier: none reachable: the public demo at demopin.filecoin.cloud is an IPFS-pin demo on Filecoin Calibration testnet where data isn't permanent and infrastructure resets regularly; production use requires connecting a funded wallet through 'Filecoin Drive', and the demo upload cap is not stated on the current page. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The old pin.filecoin.cloud page now serves a 'Filecoin Drive' landing page that links to a demopin.filecoin.cloud IPFS-pin demo; the demo states it runs on Calibration testnet where data isn't permanent and infrastructure resets regularly. Production use asks the user to connect a wallet and fund storage.
- notes: The first-party demo at demopin.filecoin.cloud is on Calibration testnet, where data isn't permanent and infrastructure resets regularly; production use requires a funded wallet through Filecoin Drive.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The public demo is Calibration testnet only: 'data isn't permanent and infrastructure resets regularly', and the UI caps uploads at 200 MB. Mainnet use runs through Filecoin Onchain Cloud…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The public demo is Calibration testnet only: 'data isn't permanent and infrastructure resets regularly', and the UI caps uploads at 200 MB. Mainnet use runs through Filecoin Onchain Cloud…
  - [2] 2026-11-19: the first-party demo still states it runs on testnet with non-permanent data and regular resets | capture: sha256:59d373856e2e6c62b1af9e19a50b769e276e2fc0dea18a61f32e48047c92afe6 | quote: This demo runs on Filecoin Calibration testnet, where data isn't permanent and infrastructure resets regularly.
  - [2] 2026-11-19: the first-party demo is testnet only with non-permanent data | capture: sha256:59d373856e2e6c62b1af9e19a50b769e276e2fc0dea18a61f32e48047c92afe6 | quote: This demo runs on Filecoin Calibration testnet, where data isn't permanent and infrastructure resets regularly.
  - [1] 2026-11-19: the original record URL now serves a different first-party product landing page | capture: sha256:4973019b976f5e262f20f46642a47dca2ce8c27b34aee532dddd67d002b2876c | quote: A drive, right in your browser.
  - [2] 2026-11-19: the first-party demo is non-permanent testnet storage | capture: sha256:59d373856e2e6c62b1af9e19a50b769e276e2fc0dea18a61f32e48047c92afe6 | quote: This demo runs on Filecoin Calibration testnet, where data isn't permanent and infrastructure resets regularly.
- sources:
  - [1] https://pin.filecoin.cloud/
  - [2] https://demopin.filecoin.cloud/
