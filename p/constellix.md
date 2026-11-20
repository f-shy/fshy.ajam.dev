# Constellix

> constellix.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/constellix/ | JSON https://fshy.ajam.dev/api/v1/entity/constellix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Constellix

- `domains-dns/constellix` | paid-only | evidence documented | binding write-gated | category managed authoritative DNS, GeoDNS | tier Pay-As-You-Go (usage-based)
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T01:43:56.218Z (live) | stale on 2026-12-20
- url https://support.constellix.com/hc/en-us/articles/34574135383323-Billing-in-Constellix
- free tier: no free tier; all services are invoiced monthly on a usage-based unit system, and a credit card is set up during account creation | unit: none | metered on: request-count | read on: 2026-11-19 | source: [1] | note: unverified: a public price list at constellix.com/pricing/faq answered HTTP 503 on 2026-11-19; the unit billing model is from the first-party billing article
- per-object cap: no per-record or per-zone object cap stated on the first-party pages read; quotas exist for particular services but their values are unverified: behind a sign-up and not published | source: [1] | note: the billing page confirms quotas exist but gives no numbers
- retention: records persist while the service is configured; deleting the configured service stops billing, and a card validity fee and monthly invoicing apply | source: [1]
- egress: DNS queries are billed by usage count; each count is an allotment of one million queries, and standard queries use a pricing schedule that lowers the unit cost above one billion queries | metered: yes | source: [1]
- identity: card | detail: By default, all payments within Constellix are made via credit card; setting up a credit card during account setup processes a USD 5 returnable validity fee, and services stay inaccessible until payment details are set up. Email is also required for an account, but the card is the gate that decides access. No free tier is published; the exact signup fields beyond the card are unverified: behind a sign-up.
- interface: rest, cli
- limits:
  - volume-quota: per-service quotas exist to prevent abuse; their numeric values are unverified: quoted nowhere on the first-party pages read [1]
  - write-gated (binding): a payment method must be set up before services can be accessed; a card validity fee of USD 5 is processed at setup [1]
  - volume-quota: all accounts are given a USD 100 credit limit threshold by default; usage above it triggers automatic invoicing [1]
- binding note: there is no free tier and access to services requires a payment method on file, so the card gate binds before any usage quota or query cost is reached
- interface detail: a REST API for domains and DNS records; API v4 docs at api.dns.constellix.com/v4/docs. Client libraries include DNSControl, the Constellix Terraform provider and the lego ACME DNS plugin
- endpoint: https://api.dns.constellix.com/v4/docs
- tooling: DNSControl, the Constellix Terraform provider, lego ACME client, any client that can sign HMAC calls with an API key and secret key
- composes with: an authoritative DNS service with GeoDNS, traffic steering, DNS failover and IP Filter routing, now a DigiCert brand; there is no free tier and a card is required, so a free hosted DNS service is the path for a no-cost stack
- reliability: a 100 percent uptime SLA is offered; no suspension, throttle or data-loss event was found on the pages read
- notes: Documented because every value rests on a first-party capture. The per-unit price list was walled, returning HTTP 503 at constellix.com/pricing/faq on 2026-11-19, so no price number is stated. No public read path was probed, so the rung stays documented.
- evidence note: the first-party billing article, API docs and DigiCert brand page were captured and quoted. The pricing page at constellix.com/pricing/faq answered HTTP 503 on 2026-11-19, so per-unit prices remain unverified; the billing model and card gate are first-party.
- self hosted: no
- evidence:
  - [1] 2026-11-19: a credit card is the default payment method, so registration needs a card | capture: sha256:5da98d8b09e37899f1638b22dc47ef883615c7b4679f5d92759f0ee5a3bcea73 | quote: By default, all payments within Constellix are made via credit card.
  - [1] 2026-11-19: a card validity fee of USD 5 is processed at account setup | capture: sha256:5da98d8b09e37899f1638b22dc47ef883615c7b4679f5d92759f0ee5a3bcea73 | quote: When setting up a credit card in our system through the account setup, a $5 returnable fee is processed to check for the validity of the card.
  - [1] 2026-11-19: services are inaccessible until payment details are set up | capture: sha256:5da98d8b09e37899f1638b22dc47ef883615c7b4679f5d92759f0ee5a3bcea73 | quote: If you find yourself trying to access services within Constellix and running into an “Oops!” response, that could mean that the payment details for this account were not fully set up.
  - [1] 2026-11-19: a default USD 100 credit threshold per account | capture: sha256:5da98d8b09e37899f1638b22dc47ef883615c7b4679f5d92759f0ee5a3bcea73 | quote: By default, all accounts are given a $100 credit limit threshold.
  - [1] 2026-11-19: per-service quotas exist, with no numbers published | capture: sha256:5da98d8b09e37899f1638b22dc47ef883615c7b4679f5d92759f0ee5a3bcea73 | quote: Yes, there are quotas established for particular services to prevent abuse.
  - [1] 2026-11-19: query usage is metered in counts of one million | capture: sha256:5da98d8b09e37899f1638b22dc47ef883615c7b4679f5d92759f0ee5a3bcea73 | quote: For example, allotments for queries are set at one million queries. That means every million queries will equal one count.
  - [1] 2026-11-19: billing is monthly and usage-based | capture: sha256:5da98d8b09e37899f1638b22dc47ef883615c7b4679f5d92759f0ee5a3bcea73 | quote: All users are billed on a monthly basis.
  - [2] 2026-11-19: a REST API exists for programmatic DNS management | capture: sha256:066e8102fbfdf660d0c7a1834c5eba2fb610c964f0dba58fdb683b6fa0449d20 | quote: REST endpoints for interacting with the Constellix DNS services.
  - [2] 2026-11-19: API access uses per-user API and secret keys | capture: sha256:066e8102fbfdf660d0c7a1834c5eba2fb610c964f0dba58fdb683b6fa0449d20 | quote: Authentication with the Constellix API is performed using the API and Secret keys
  - [3] 2026-11-19: Constellix is a DigiCert brand | capture: sha256:e300be1cb2f85e948b08385fb907d9c64b222929744b387cf7199c94ce2fb611 | quote: © 2026 DigiCert, Inc. All rights reserved.
- sources:
  - [1] https://support.constellix.com/hc/en-us/articles/34574135383323-Billing-in-Constellix
  - [2] https://api-docs.constellix.com/
  - [3] https://constellix.digicert.com/
