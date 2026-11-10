# Clever Cloud

> clever.cloud | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clever/ | JSON https://fshy.ajam.dev/api/v1/entity/clever.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Clever Cloud (no free tier)

- `compute/clever-cloud` | paid-only | evidence documented | binding write-gated | category platform host | tier no free tier
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T01:55:00.000Z (live) | stale on 2026-11-24
- url https://www.clever.cloud/pricing/
- free tier: no free tier on the pricing page: every runtime, database and addon bills per second against a funded account balance, and the smallest scalers are sold by the month | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable: the unit is a scaler instance
- retention: an FS Bucket can be mounted into the application folder for persistence; billing continues while an instance exists
- egress: not stated on the pricing page read | metered: no | source: [1]
- identity: card | detail: payment by card, PayPal, bank transfer or SEPA direct debit into an account balance
- interface: unknown
- limits:
  - write-gated (binding): no free plan on the pricing page; consumption is drawn from a funded balance [1]
  - per-object-cap: instances bill per second by scaler size; the smallest is pico at 256 MB, priced historically at EUR 4.50 a month [2]
- binding note: there is nothing free to exhaust: the account must be funded before an instance starts.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: No free row appears on the pricing page, so a free tier of no stated amount is not supported. The historical pico scaler price is from a 2015 post and is not a current price; it is recorded only to size the smallest thing sold.
- evidence note: the absence of a free tier is read from the pricing page, which prices every runtime without a free row; the balance mechanism is from the billing documentation
- extras:
  - keep_rate: 1.0
  - billing_model: per-second
  - shape.ram_gib: 0.25
  - session_cap.restart_required: no
  - session_cap.note: no idle reap; the instance bills while it exists
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: the application port; addons and TCP redirections are separate
  - network_out.static_ip: no
  - network_out.ipv6: no
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.price: FS Bucket mounted into the app
  - ps.durability: FS Bucket
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the bucket exists
  - term: monthly
  - price_arithmetic: not computed: the pricing page read renders prices through a calculator and publishes no figure in text
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Each month, you fund your Clever Cloud account with an amount that reflects your usual consumption' and 'Each instance is billed on a per-second basis' with 'FS Bucket brings the ability to mount a file system within an application folder for file persistence', quoted
  - [1] 2026-10-24: quoted: 'Each month, you fund your Clever Cloud account with an amount that reflects your usual consumption' and, of the runtimes, 'Our pricing depends on the size and the number of instances your application needs'
  - [3] 2026-10-24: quoted: 'Payments: Buy credit by card, PayPal, bank transfer or SEPA direct debit'
- sources:
  - [1] https://www.clever.cloud/pricing/
  - [2] https://www.clever-cloud.com/blog/company/2015/07/22/new-flavours-pricing-update/
  - [3] https://www.clever.cloud/developers/doc/billing/

## Clever Cloud (free)

- `egress/clever-cloud` | paid-only | evidence documented | binding volume-quota | category paas l4 port | tier free
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.clever.cloud/developers/doc/administrate/tcp-redirections
- price USD 0
- free tier: TCP redirections are currently available free of charge as long as the feature is in BETA stage. Once the feature leaves the BETA stage, it won't be free anymore. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No free application tier is published; pricing is pay-as-you-go per scaler and add-on. Free plans exist only for storage products (Cellar first 100 MB).; ingress: tcp | metered: yes | free allowance: No free application tier is published; pricing is pay-as-you-go per scaler and add-on. Free plans exist only for storage products (Cellar first 100 MB). | source: [2]
- identity: card | detail: Pay-as-you-go account with a funded balance; the pricing page says each month you fund your account to reflect your usual consumption. | country: None
- interface: cli, rest
- limits:
  - volume-quota (binding): no free application allowance; TCP redirection free only while in beta [3]
- binding note: The redirection is free but the application it points at is not; the free tier fails before any byte is counted.
- interface detail: Console and API; "From your console, select your application".
- tooling: Console or CLI; the port is assigned by Clever Cloud.
- composes with: With a paid scaler, the redirection is an SSH or database path; no free option.
- reliability: The feature is labelled BETA and the free status is explicitly temporary. Random port above 5000, so the endpoint is not predictable.
- notes: The redirection is a genuinely free L4 path, but only to a paid application. The application must still listen on 8080 regardless of TCP configuration.
- evidence note: The beta statement is dated 2022 on the blog and unversioned in the docs; re-reading it later is what keeps this record honest.
- extras:
  - wg_path: none
  - wg_detail: TCP only: "you can use a TCP redirection to route TCP traffic, through Clever Cloud reverse proxies, to your application." Port is "chosen at random above 5000".
  - ingress: tcp
  - volume_tib_month: 0
  - volume_stated: No free application tier is published; pricing is pay-as-you-go per scaler and add-on. Free plans exist only for storage products (Cellar first 100 MB).
  - bytes_transit: yes
  - transit_note: Clever Cloud reverse proxies carry the TCP stream.
- evidence:
  - [2] 2026-10-23: TCP redirection to port 4040, external port random above 5000
  - [1] 2026-10-23: "TCP redirections are currently available free of charge as long as the feature is in BETA stage."
  - [4] 2026-10-23: "It can be used freely and is not charged." (2022-03-29)
- sources:
  - [1] https://www.clever.cloud/developers/doc/develop/common-configuration/tcp-redirections/
  - [2] https://www.clever.cloud/developers/doc/administrate/tcp-redirections
  - [3] https://www.clever.cloud/pricing/
  - [4] https://www.clever.cloud/blog/features/2022/03/29/tcp-redirections-are-now-available/
