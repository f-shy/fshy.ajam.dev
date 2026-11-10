# Synology C2 Object Storage

> synology.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/synology/ | JSON https://fshy.ajam.dev/api/v1/entity/synology.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Synology C2 Object Storage

- `storage/synology-c2-object-storage` | qualifies-with-caveat | evidence reported | binding none | category S3-compatible object storage, flat per-TB
- needs card yes, phone unknown, ID no, institution no | verified 2026-11-01T18:05:15.749Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://c2.synology.com/en-us/object-storage/overview
- price $7.99/TB flat at both 5 TB and 20 TB | parsed USD 7.99/TB-mo
- free tier: Sold in whole-TB increments from 1 TB | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'Free data retrieval — Retrieve all the data you have stored for free every month.' Plus 'No API request or data deletion fees'. Note the retrieval-included claim is bounded by 'every month', not stated as unlimited. | metered: no
- identity: email | detail: the account is a Synology Account, reached by email and a password or by Google or Apple sign-in, and the vendor does not list the fields of that sign-up, so whether it asks a phone number is unverified. Every subscription needs a payment method, listed as credit or debit card, SEPA direct debit and ACH direct debit
- interface: s3-compatible, rclone
- limits note: Restructure risk: KB article states 'Effective June 22, 2026, the subscription model for C2 Object Storage will transition to C2 OneStorage'. Pricing and capacity conversion applies. Verify current SKU before committing.
- interface detail: S3-compatible
- tooling: any S3 client; Synology Hyper Backup, rclone generic S3
- composes with: S3 -> AList/rclone/Cloudflare
- reliability: Claims 99.999999999% durability, EU and US data centres. Synology is an established hardware vendor; no data-loss event.
- notes: the same as the free tier
- extras:
  - price_verbatim: $7.99/TB flat at both 5 TB and 20 TB
- evidence:
  - [1] 2026-10-21: 'At just $7.99/TB per month ... Free data retrieval ... No API request or data deletion fees'
  - [2] 2026-10-21: C2 OneStorage transition effective 2026-06-22
  - [3] 2026-11-01: the account is a Synology Account, reached by email or by Google or Apple sign-in | capture: sha256:2daad33baf52cfc71c9a9095666297f383fbd91794ec2b88ccff75c53aa44754 | quote: In your Synology Account, sign in using your Google, Apple, or Synology Account.
  - [4] 2026-11-01: the subscription needs a card, SEPA direct debit or ACH direct debit | capture: sha256:0e96d9a3046ca9890f0b1ba91f84f2c548d52af3b2bb1f46fbcc83bd7fdf3a19 | quote: - Credit or debit card - SEPA direct debit (only for payments in USD or EUR) - ACH direct debit (only for payments in USD or EUR)
  - [3] 2026-11-01: the object storage offer is entered through a Synology Account subscription | capture: sha256:2daad33baf52cfc71c9a9095666297f383fbd91794ec2b88ccff75c53aa44754 | quote: Select C2 OneStorage and follow the wizard to complete the subscription.
- sources:
  - [1] https://c2.synology.com/en-us/object-storage/overview
  - [2] https://kb.synology.com/en-global/C2/tutorial/Plan_Change_2026_C2_Object_Storage
  - [3] https://kb.synology.com/en-us/C2/tutorial/Quick_Start_C2_Object_Storage
  - [4] https://kb.synology.com/en-us/DSM/tutorial/what_can_i_do_Synology_Account_payment_shipment
