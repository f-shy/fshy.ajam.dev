# Storj storage node operator

> storj.dev | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/storj-2/ | JSON https://fshy.ajam.dev/api/v1/entity/storj-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Storj storage node operator (supply side)

- `storage/storj-storage-node-operator` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category contributed storage - become an SNO
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:43:31.135Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://storj.dev/node/payouts
- free tier: paid $1.35/TB/month stored + $1.00/TB egress (cut from $1.50/$2.00 on 1 Sep 2026, an 18% total reduction). Paid in USDC on Ethereum, not STORJ. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1] | note: a payout for storing and serving other users' data on a node the user runs, not a free allowance
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: you are paid $1.00/TB for egress; the customer is charged $7/TB | metered: yes | price per TB: $1.00/TB
- identity: email | detail: the node is configured with an email address and an Ethereum wallet address for USDC payouts; no authorization token is needed to join
- interface: unknown
- limits note: Worse ratio than Sia and stated in the same currency, which makes it unambiguous: SNO gets $1.35/TB while Storj charges the customer $7.00/TB for the same terabyte - a 5.2x gap. To fund 20 TiB at $7/TB ($140/mo) plus 30 TiB/mo egress at $7/TB ($210/mo) = $350/mo, you must store $350/1.35 = 259 TB of other people's data. Storj's own forum arithmetic also carries a 2.7x erasure expansion factor, so 1 TB of customer data consumes 2.7 TB of SNO disk - meaning the true disk ratio is ~700 TB contributed to consume 20 TB. This is the clearest negative in the slot.
- interface detail: Docker container, single identity per node, dashboard
- tooling: storagenode Docker image, storj node dashboard, uptime robot
- composes with: USDC payout can be spent on anything, but cannot be converted into Storj storage credit - there is no credit mechanism
- reliability: Node disqualification and held amounts apply for the first months; forum reports of 8.5 TiB stored paying $5.50 indicate realised rates well below list.
- notes: Payout rates since Sep 1st, 2026: USD 1.35 per TB-month stored, USD 1.00 per TB of egress and USD 1.00 per TB of audit and repair traffic, paid in USDC on Ethereum layer 1; zkSync layer 2 payouts ended on September 1, 2026, and a payout is sent only when its transaction fee is at most 25% of its value, so smaller balances roll into later months.
- self hosted: yes
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: paid $1.35/TB/month stored + $1.00/TB egress (cut from $1.50/$2.00 on 1 Sep 2026, an 18% total reduction). Paid in USDC on Ethereum, not STORJ.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: Standard: 'Monthly storage $7/TB', 'Egress $7/TB'; minimum monthly fee $5; 30-day minimum retention with early-deletion fee; 50 KB minimum object size
  - [1] 2026-10-21: rate table: 'Used space (storage) $1.50/TB/month -> $1.35/TB/month -10%'; 'Egress (bandwidth) $2.00/TB -> $1.00/TB -50%'; 'estimated 18% reduction in total payout'
  - [3] 2026-10-21: 'Payouts are made in USD Coin (USDC) ... Earnings are calculated in USD and paid at one USDC per US dollar'
  - [4] 2026-10-21: '$1.5/TB is for a single SNO, but theres 2.7 expansion factor, so 1 TB times 2.7 times $1.5 = $4.05 just a storage cost, per month'
  - [5] 2026-10-21: 'for 2026/09 my node stored 8.5 TiB of data and was paid $5.50'
  - [6] 2026-10-30: the node's run command takes a wallet address and an email address | capture: sha256:88629c023648855cc30a0b09053ede4c5694dfb7ddf60935f035752451f926db | quote: 1. Edit the `WALLET`, `EMAIL`, `ADDRESS`, `STORAGE` and replace the `<identity-dir>`, and `<storage-dir>` with your parameters.
  - [3] 2026-10-30: node operators are paid for the storage and bandwidth their nodes provide | capture: sha256:9cddd3037012872b6941ec4672f6ceceb2f5467cc4d3bec9e5595e131ae390b2 | quote: Storj nodes share underutilized hard drive capacity and bandwidth with the Storj network and are paid when users store and retrieve data.
  - [7] 2026-10-30: the authorization-token step for a new node identity is no longer required | capture: sha256:b38c82aa6f2e6a8c5a53ee674b4f8c03c1fecbcc8b547da1cd22923bee1c9d04 | quote: is not required any more.
  - [3] 2026-10-30: a payout is withheld until its transaction fee is at most 25% of its value | capture: sha256:9cddd3037012872b6941ec4672f6ceceb2f5467cc4d3bec9e5595e131ae390b2 | quote: We will not send a transaction where the fee for the transaction is more than 25% of the value of the transaction.
  - [1] 2026-10-30: the September 1 change cut storage pay from $1.50 to $1.35 per TB-month and egress pay from $2.00 to $1.00 per TB, an estimated 18% total cut | capture: sha256:251083022274b4dbb585181b28d113ce36f58afa3346f82ec0bf203004c05226 | quote: Combined, this represents an estimated 18% reduction in total payout
  - [3] 2026-10-30: node operators are paid $1.35 per TB-month stored and $1.00 per TB of egress, in USDC on Ethereum | capture: sha256:9cddd3037012872b6941ec4672f6ceceb2f5467cc4d3bec9e5595e131ae390b2 | quote: | Storage (per TB per Month) | $1.35 |
  - [3] 2026-11-04: node operator storage payout is $1.35 per TB per month | capture: sha256:9cddd3037012872b6941ec4672f6ceceb2f5467cc4d3bec9e5595e131ae390b2 | quote: | Storage (per TB per Month) | $1.35 |
- sources:
  - [1] https://forum.storj.io/t/rightsizing-storj-network-payout-rates/32391
  - [2] https://www.storj.io/pricing
  - [3] https://storj.dev/node/payouts
  - [4] https://forum.storj.io/t/helping-the-network-become-profitable-what-can-operators-contribute-while-staying-viable-calculator-inside/32104
  - [5] https://forum.storj.io/t/storj-is-moving-node-operator-payouts-and-customer-deposits-to-usdc/32809?page=16
  - [6] https://storj.dev/node/get-started/install-node-software/cli/storage-node
  - [7] https://forum.storj.io/t/identity-signing-identity-authorize-is-not-required-any-more/30581
