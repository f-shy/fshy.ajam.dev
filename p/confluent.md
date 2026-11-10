# confluent cloud

> confluent.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/confluent/ | JSON https://fshy.ajam.dev/api/v1/entity/confluent.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## confluent cloud (kafka)

- `storage/confluent-cloud` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T11:10:48.000Z (inherited) | stale on 2026-11-07
- url https://forum.confluent.io/t/announcing-our-new-free-trial-for-confluent-cloud/4404/1
- free tier: 'New signups receive $400 to spend during their first 30 days.' The documentation adds 'Your free credit expires 30 days after you receive it.' | unit: mixed | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: not recorded | source: [2] | note: not applicable
- retention: the credit expires 30 days after it is received, or when it is spent, whichever comes first | days: 30 | source: [3]
- egress: not recorded | metered: no
- identity: email | detail: the signup form asks for a full name, a company, an email address and a country, or a Google, GitHub or Marketplace sign-in; a payment method is entered only after the trial credit is spent
- interface: unknown
- limits note: the 60-day figure recorded earlier is contradicted by both the signup page and the documentation, which state 30 days
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: USD 400 in credit, and it expires 30 days after it is received; the credit is denominated in dollars rather than bytes. Kafka is append-only with retention, so the balance is not a storage quota.
- notes: Corrected on 2026-10-23 from 60 days to 30. The credit buys Kafka and the managed connectors, not a machine.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: USD 400 in credit, and it expires 30 days after it is received; the credit is denominated in dollars rather than bytes. Not a free tier; a trial.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-23: quoted: 'New signups receive $400 to spend during their first 30 days.'
  - [3] 2026-10-23: quoted: 'Your free credit expires 30 days after you receive it.'
  - [4] 2026-10-23: quoted tiers: Basic 'Starting at $0/Month', Standard '~$385/Month', eCKU 'First eCKU free, then $0.14'
- sources:
  - [1] https://confluent.cloud/signup
  - [2] https://forum.confluent.io/t/announcing-our-new-free-trial-for-confluent-cloud/4404/1
  - [3] https://docs.confluent.io/cloud/current/get-started/free-trial.html
  - [4] https://www.confluent.io/pricing/
