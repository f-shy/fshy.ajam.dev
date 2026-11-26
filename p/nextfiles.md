# nextfiles.one

> nextfiles.one | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nextfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/nextfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nextfiles.one (managed Nextcloud CE and Seafile Pro)

- `netdisk-pan/nextfiles-one` | qualifies | evidence documented | binding per-object-cap | category managed Nextcloud and Seafile, paid only
- identity a placeholder: card and phone unknown | verified 2026-11-25T14:21:57.881Z (live) | stale on 2026-12-17
- url https://www.nextfiles.one/en/secure-cloud-for-private-customers-and-associations-29/
- price EUR 6.99/TB/month at 1 TB rising to EUR 20.00/TB/month at 5 TB, including VAT, read 2026-11-19 | parsed USD 7.88/TB-mo
- free tier: Test for free for one month and check - cancel anytime | unit: none | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: Not published as a per-file cap on the private-customer plans. The plan table publishes storage, a recommended user count and the storage type ('Cluster') | source: [1]
- retention: Contract term from one month with automatic renewal for the same period; a consumer may cancel any time before a new billing period. Disaster-recovery backups of the last 7 days are kept, with managed or own backups offered for up to 10 years | days: 7 | source: [1]
- egress: No egress price and no traffic quota are published on the private-customer plans, so this field is false by the schema's own definition rather than on a stated guarantee. The features block says 'Unlimited storage space in the Cloud', which is about capacity and not about traffic | metered: no | source: [1]
- identity: card | detail: unverified: the page lists payment options but does not say the trial needs no card
- interface: webdav, rest, rclone
- limits:
  - per-object-cap (binding): not published on the private-customer plans [1]
- binding note: The price curve decides the tier and the tier is small, so the unstated per-file cap is the number a buyer cannot plan around. At EUR 20.00/TB/month on the 5 TB plan the rate is almost three times the 1 TB one, which is why it is recorded as a small-instance option.
- tooling: rclone webdav against any Nextcloud CE plan; the Nextcloud clients; administrator access to the AppStore. The Seafile Pro plans need the Seafile client or the Seafile WebDAV extension, which is a weaker tooling story
- composes with: Reseller providing managed Seafile hosting with library-level client-side encryption. The cost structure is lowest on smaller capacities and increases per terabyte on larger allocations, suiting small-scale deployments rather than bulk archives.
- reliability: Germany, ISO 27001 data centres, renewable power. The per-terabyte price rises with size, which is the opposite of every other reseller here and is the signal that the large tiers are not built for price comparison
- evidence note: The Nextcloud CE plan table was read live. `documented`: no plan was ordered and no WebDAV endpoint was exercised.
- extras:
  - access_mode: paid
  - free_tier_exists: no
  - trial: 1 month free on Nextcloud CE
  - region: Germany
  - price_includes_vat: yes
  - tier_prices_eur_month_inc_vat.silver_1TB: 6.99
  - tier_prices_eur_month_inc_vat.gold_2TB: 19.99
  - tier_prices_eur_month_inc_vat.platin_3TB: 39.99
  - tier_prices_eur_month_inc_vat.max_5TB: 99.99
  - seafile_tiers_seen_live: Business S from EUR 9.90/month up to 3 users, Business M from EUR 29.90 up to 9 users, Business L priced per user
- evidence:
  - [1] 2026-10-22: 'Premium Silver (C) 1 TB storage space ... 4,99 EUR / Month', 'Premium Gold (C) 3 TB ... 14,99 EUR / Month', 'Premium Platinum (C) 5 TB ... 39,99 EUR / Month', 'Premium Max (C) 10 TB ... 99,99 EUR / Month', all 'Storage Type Cluster', 'Server location Germany'
  - [1] 2026-10-22: 'Try now for free for 1 month', 'Test for free for one month and check - cancel anytime', and 'Contract term from one month, with automatic renewal for the same period unless canceled in advance ... Prices incl. VAT'
  - [1] 2026-10-22: 'Unlimited storage space in the Cloud' appears in the Product Features block and nowhere in the plan table, where the four storage sizes are stated explicitly
  - [2] 2026-10-22: 'Business S ... from 9,90 EUR / Month ... Storage space from 500 GB ... up to 3 users', 'Business M ... from 29,90 EUR / Month ... from 500 GB ... up to 9 users', 'Business L ... Price per user ... from 9,90 EUR / Month'
  - [1] 2026-11-19: the 7-day disaster-recovery backup statement is unchanged | capture: sha256:c089e9718589528faa3d6be960e175160179f843d926c33a33eea0b6e1b62b65 | quote: Disaster Recovery data backup with anytime access to the backups of the last 7 days
  - [2] 2026-11-19: the stated payment methods are unchanged | capture: sha256:c35fa33531e5537c84bf473d861e10f9a041969f188a8b3128224966fab422dd | quote: We offer various payment options: invoice, bank transfer, direct debit, PayPal, and credit card.
  - [1] 2026-11-19: the private-customer Nextcloud CE plan table was re-read on 2026-11-19 | capture: sha256:c089e9718589528faa3d6be960e175160179f843d926c33a33eea0b6e1b62b65 | quote: 1 TB storage space
  - [1] 2026-11-25: disaster-recovery backups cover the last 7 days | capture: sha256:906548f2b415285aeaa229b1f2343c031600140c2fa416151a229129f94044f3 | quote: Disaster Recovery data backup with anytime access to the backups of the last 7 days
  - [1] 2026-11-25: the plan table prices storage in TB | capture: sha256:906548f2b415285aeaa229b1f2343c031600140c2fa416151a229129f94044f3 | quote: 1 TB storage space
  - [1] 2026-11-25: the page offers a one-month free trial | capture: sha256:906548f2b415285aeaa229b1f2343c031600140c2fa416151a229129f94044f3 | quote: Test for free for one month and check - cancel anytime
  - [1] 2026-11-25: five payment options are listed | capture: sha256:906548f2b415285aeaa229b1f2343c031600140c2fa416151a229129f94044f3 | quote: We offer various payment options: invoice, bank transfer, direct debit, PayPal, and credit card.
  - probe:https://www.nextfiles.one/en/secure-cloud-for-private-customers-and-associations-29/ 2026-11-25: the plan page is still served | capture: sha256:1150eb4d086fd9fe5671f1c33efd0ad4591c0f8f7263adad3c86fb6a88b50aad | quote: "status": 200
  - [1] 2026-11-25: the one-month trial is attached to the priced Premium Silver plan; no free storage quantity is published | capture: sha256:906548f2b415285aeaa229b1f2343c031600140c2fa416151a229129f94044f3 | quote: 1 Month Free Trial 6,99 € / Month
  - [1] 2026-11-25: the free offer is a one-month trial, cancellable at any time | capture: sha256:906548f2b415285aeaa229b1f2343c031600140c2fa416151a229129f94044f3 | quote: Test for free for one month and check - cancel anytime
- sources:
  - [1] https://www.nextfiles.one/en/secure-cloud-for-private-customers-and-associations-29/
  - [2] https://www.nextfiles.one/en/seafile-pro-82/
