# Coinbase Commerce

> coinbase.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coinbase/ | JSON https://fshy.ajam.dev/api/v1/entity/coinbase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Coinbase Commerce

- `debrid/coinbase-commerce` | dead | evidence documented | binding none | category crypto payment processor | tier merchant
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:30:43.000Z (live) | stale on 2026-11-23
- url https://help.coinbase.com/en/transitioning-from-coinbase-commerce-to-coinbase-business
- free tier: no free tier; the processor charged '1% transaction fee' and is being withdrawn. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: a processor, not a store. | source: [1]
- retention: not applicable: a processor, not a store. | source: [1]
- egress: not applicable: a processor. | metered: no | source: [1]
- identity: email | detail: On the payer side the processor asked for no account: a checkout address and a wallet. That property is what made it useful to services whose buyers have no card, and it is the property the replacement does not clearly keep, since Coinbase Business is 'stablecoin-first, custodial, compliant'.
- interface: rest
- limits note: no payment-vocabulary limit. The processor-side date is the limit: 'You must complete your transition by March 31, 2026. After this date, the Commerce portal will become permanently inaccessible.'
- binding note: The seven-kind vocabulary does not apply to a processor. The binding fact is a shutdown date, not a quota.
- interface detail: Charge API and payment links; the Charge API is what the migration guide retires
- tooling: hosted checkout and API for merchants; the payer needs a wallet, not an account
- composes with: Payment integration note: Coinbase Commerce withdrew support outside the US and Singapore, requiring merchants to migrate to alternative payment processors.
- reliability: Shut down for merchants outside the US and Singapore on 2026-03-31: 'If you're based outside the United States or Singapore ... you will need to transition to an alternative provider before March 31, 2026'.
- notes: Included because Real-Debrid's mirrored FAQ still names Coinbase as the crypto rail, and because two other services in the sample moved off it (TorBox's changelog records leaving 'PayPal and Coinbase' for Sellix). A processor sunset is exactly the kind of fact that decays a rail claim without touching the service's own page.
- evidence note: Coinbase's own help-centre transition page was read. The payer-side no-account property is inferred from how hosted crypto checkout works, not quoted, and is labelled as such here.
- extras:
  - payment_group: processor
  - shutdown: 2026-03-31 for merchants outside the US and Singapore
  - payer_identity: no account, wallet only (inferred, not quoted)
- evidence:
  - [1] 2026-10-23: 'Coinbase Commerce is being unified with Coinbase Business. You must complete your transition by March 31, 2026. After this date, the Commerce portal will become permanently inaccessible'; merchants outside the US and Singapore must move to another provider
  - [2] 2026-10-23: third-party estimate, read from the search index and not opened: 'roughly 40 percent went to direct custodial alternatives (BitPay, NOWPayments), 35 percent went non-custodial'. Reported, not verified.
- sources:
  - [1] https://help.coinbase.com/en/transitioning-from-coinbase-commerce-to-coinbase-business
  - [2] https://www.plaitr.com/blog/the-coinbase-commerce-migration-where-8000-merchants-went
