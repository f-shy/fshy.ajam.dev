# Chroma Cloud

> trychroma.com | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/trychroma/ | JSON https://fshy.ajam.dev/api/v1/entity/trychroma.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Chroma Cloud

- `databases-kv/chroma-cloud` | trial-only | evidence documented | binding volume-quota | category vector database
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:44:00.366Z (live) | stale on 2026-12-03
- url https://www.trychroma.com/pricing
- free tier: Starter plan, $0/month + usage: "per month + $5 in free credits"; "Free credits then usage-based pricing." The $5 is offered to new users and "in most cases your credits do not expire". | unit: credits | metered on: none | read on: 2026-11-01 | source: [1] | note: metered on spend: the USD 5 credit is spent against usage billed on four meters, USD 2.50 per GiB written, USD 0.33 per GiB per month stored, USD 0.0075 per TiB queried and USD 0.09 per GiB returned
- per-object cap: 16,384 bytes per document, a Chroma Cloud quota; the total allowance is the credit | bytes: 16384
- retention: until the credits are spent | source: [1]
- egress: usage-based and metered out of the same USD 5 credit as storage and queries. The credit is the only ceiling, and no separate egress allowance applies | metered: yes | source: [1]
- identity: email | detail: sign-in with a GitHub or Google account; the sign-up page shows no card field; a vendor video posted 2025-06-30 says the USD 5 of free credits needs no credit card and says to add a credit card to keep using the service after the trial; the pricing FAQ lists credit card as the payment method for Starter and Team
- interface: rest, cli
- limits:
  - volume-quota (binding): USD 5 of credits, which is a spend cap and not a tier [1]
- binding note: the one-time USD 5 credit runs out first: it is counted per account across all collections, and at USD 2.50 per GiB written it pays for 2 GiB of writes before any storage, query or returned-data charge
- interface detail: a REST API; Python and JS clients; the open-source server is self-hostable
- tooling: the chromadb client libraries
- composes with: the hosted Starter plan is a USD 5 credit for new accounts with usage-based billing after it; the open-source core, which the user installs and runs on a rented or free machine, is the last resort
- reliability: a usage limit, whether set by the customer or by Chroma, pauses the service until the limit is changed
- notes: Advertised as free and it is a trial. The $5 is a spend cap, and a spend cap that small is a fortnight of a real index rather than a tier.
- evidence note: the pricing page was read.
- evidence:
  - [1] 2026-10-22: Starter is listed at USD 0 plus USD 5 of free credits, with usage-based billing after
  - [1] 2026-10-30: the Starter plan is $0 a month and carries $5 in free credits | capture: sha256:c49f0b333a3fbc2b7e92125e3aed7fc6309d3ef71c25b37f792beab43882df36 | quote: Starter planper month + $5 in free credits
  - [1] 2026-10-30: the Starter plan opens with free credits and bills usage after them | capture: sha256:c49f0b333a3fbc2b7e92125e3aed7fc6309d3ef71c25b37f792beab43882df36 | quote: Get up and running quickly. Free credits then usage-based pricing.
  - [1] 2026-10-30: the pricing FAQ says unused credits do not expire in most cases; only the Team plan's $100 of included usage does not roll over | capture: sha256:43921cc7f783222b515df09cd531d466d63d0278672125408e450bdba254ed86 | quote: Yes, in most cases your credits do not expire.
  - [2] 2026-10-30: the free allowance is $5 of credits given to new users, not a monthly grant | capture: sha256:081c269e256353312de4697e42bf34dc7e4b852b607d502fc671d35ee13cb15c | quote: We offer \$5 in credits to new users.
  - [3] 2026-11-01: the vendor's own video (channel Chroma, posted 2025-06-30) says the $5 of free credits needs no credit card at sign-up | capture: sha256:7db971ba019bc1b1a6dd0b07ffc1e8a9d79edea5677eca36677211e0cdb2533a | quote: Sign up for Chroma Cloud and get $5 in free credits, no credit-card required.
  - [2] 2026-11-01: the docs FAQ states the free allowance is $5 of credits offered to new users | capture: sha256:b7abca4cb0eac61f54dd1b7014b71b91ba4986d7894ee88136381973d2ec1468 | quote: We offer \$5 in credits to new users.
  - [2] 2026-11-01: writes are billed at $2.50 per logical GiB | capture: sha256:b7abca4cb0eac61f54dd1b7014b71b91ba4986d7894ee88136381973d2ec1468 | quote: Chroma Cloud charges \$2.50 per logical GiB written via an add, update, or upsert.
  - [4] 2026-11-01: the quotas page caps a document at 16,384 bytes | capture: sha256:eafa85c0bc726c7d932b6c0dbc71434f4614650e28159f32e40c731cdaa32cb6 | quote: | Maximum document bytes | 16,384 |
  - [1] 2026-11-01: the pricing page lists four usage meters: GiB written, GiB per month stored, TiB queried and GiB returned, with their rates | capture: sha256:c49f0b333a3fbc2b7e92125e3aed7fc6309d3ef71c25b37f792beab43882df36 | quote: Writeper GiB written $2.50 Storageper GiB per month $0.33 Queryper TiB queried $0.0075 Networkper GiB returned $0.09
  - [1] 2026-11-01: a usage limit set by the customer or by Chroma pauses the service until the limit is changed | capture: sha256:12442e9f20d21375035737c06f4d2013019084c374ab064b5012dcb7fa6f1756 | quote: There are 2 kinds of usage-limits. Customer set usage limits and Chroma set usage limits. Both result in a pausing of the service until the limit is changed.
  - [1] 2026-11-01: the Starter plan opens with free credits and bills usage after them | capture: sha256:c49f0b333a3fbc2b7e92125e3aed7fc6309d3ef71c25b37f792beab43882df36 | quote: Get up and running quickly. Free credits then usage-based pricing.
  - [1] 2026-11-01: the Starter plan is listed at $0 a month with $5 in free credits | capture: sha256:c49f0b333a3fbc2b7e92125e3aed7fc6309d3ef71c25b37f792beab43882df36 | quote: Starter planper month + $5 in free credits
  - [3] 2026-11-01: the vendor's video says a credit card is added to keep using Chroma after the trial credits | capture: sha256:d72f753292cffae938c85ceca17b8c89d4705029e6ced744fc1e34c199f0578c | quote: To keep using Chroma after the trial, just add your credit card.
  - [5] 2026-11-01: the sign-up page offers GitHub and Google sign-in and shows no card field | capture: sha256:939d08a1289fd5abed52ff54fa79b7d1776ce524612b0573288b335fee27fb50 | quote: [Continue with Github](https://backend.trychroma.com/api/v1/auth/github/signup)[Continue with Google](https://backend.trychroma.com/api/v1/auth/google/signup)
  - [1] 2026-11-01: the pricing FAQ lists credit card as the payment method for the Starter and Team plans | capture: sha256:12442e9f20d21375035737c06f4d2013019084c374ab064b5012dcb7fa6f1756 | quote: Currently Chroma accepts credit card for Starter and Team plans. Enterprise plans have configurable billing methods.
  - [2] 2026-11-01: billing is per account, with all collections and tenants of an account aggregated | capture: sha256:b7abca4cb0eac61f54dd1b7014b71b91ba4986d7894ee88136381973d2ec1468 | quote: Billing is account-based. All data across your collections and tenants within a Chroma Cloud account is aggregated for pricing.
  - [6] 2026-11-02: the current getting-started docs advertise Chroma Cloud with $5 in free credits included | capture: sha256:601ad5d1f0dc3b9096721f703183e880a3739e64f7989deaf9873b52e1e93c88 | quote: Get started in 30 seconds - \$5 in free credits included.
- sources:
  - [1] https://www.trychroma.com/pricing
  - [2] https://docs.trychroma.com/cloud/pricing
  - [3] https://www.youtube.com/watch?v=CCYpwEV7wVY
  - [4] https://docs.trychroma.com/cloud/quotas-limits
  - [5] https://www.trychroma.com/signup
  - [6] https://docs.trychroma.com/docs/overview/getting-started
