# Astra DB Serverless

> datastax.com | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datastax/ | JSON https://fshy.ajam.dev/api/v1/entity/datastax.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Astra DB Serverless (DataStax / IBM)

- `databases-kv/astra-db` | qualifies-with-caveat | evidence documented | binding write-gated | category managed Apache Cassandra and vector database | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:19:24.795Z (live) | stale on 2026-12-20
- url https://docs.datastax.com/en/astra-db-serverless/administration/subscription-plans.html
- free tier: Organizations on the Free plan receive a fixed amount of credits each month. No more than five Astra DB Serverless databases. | unit: credits | metered on: request-count | read on: 2026-11-19 | source: [1] | note: The free allowance is a fixed number of credits per month, not a fixed byte count. Unused credits do not roll over and reset on the first of every month. Storage itself has no practical byte limit on a Serverless database.
- per-object cap: There is no practical limit to the number of bytes an Astra DB Serverless database can store. | source: [2] | note: the cap that binds is the monthly credit allowance and the maximum of five databases, not a per-object size
- retention: Inactive Astra DB Serverless databases are automatically hibernated and scheduled for deletion | source: [1] | note: days null is activity-based: hibernation and scheduled deletion follow inactivity, and a database suspended for exhausted credits stays inaccessible until the credits refresh or the plan is upgraded
- egress: Data transfer out of a database, including internet egress and cross-region replication, is billed in credits per GB; the free plan draws from the monthly credit allowance | metered: yes | free allowance: fixed monthly credits | source: [3]
- identity: email | detail: You can create an Astra account manually or use SSO to automatically provision an account through your IdP, Google, GitHub, or IBMid account. Your email address is the unique identifier for your Astra account. The manual route is a username and password; no card is named at signup.
- interface: rest, cli
- limits:
  - volume-quota: No more than five Astra DB Serverless databases on Free [1]
  - write-gated (binding): databases are suspended when the monthly credit allowance is consumed and cannot be accessed until credits refresh or the plan is upgraded [2]
  - retention-clamped: inactive databases are automatically hibernated and scheduled for deletion on the Free plan [1]
- binding note: the fixed monthly credit allowance suspends databases once spent, which binds before the five-database count for an active workload
- interface detail: Data API over HTTP for collections and tables, the DevOps API for management, CQL over the Cassandra wire protocol with a Secure Connect Bundle, and the Astra CLI
- tooling: Astra Data API clients, Cassandra drivers with a Secure Connect Bundle, cqlsh, and the astra CLI
- composes with: a free Serverless database can back an app through the HTTP Data API and be paired with other free hosts; at most five databases and the monthly credit refresh bound the chain
- reliability: a Free database is suspended when monthly credits run out and its data is inaccessible until credits refresh or the plan is upgraded; inactive databases are hibernated and scheduled for deletion. The amount of free credits is not published on the pages read, so the exact ceiling is unknown.
- notes: The numeric amount of free monthly credits is unverified: it is not stated on the DataStax subscription-plans, subscription-usage or FAQ pages read, and the IBM pricing page answered HTTP 403. Astra is a Serverless Cassandra and vector store, not a general object store, so the lack of a byte cap does not make the credit ceiling irrelevant. The interface is set from the Data API, DevOps API, CQL and CLI documented across the first-party pages.
- evidence note: all values are from first-party DataStax docs pages read; the credit amount is not published there and is left unverified, and no probe was run
- evidence:
  - [1] 2026-11-19: the free allowance is a fixed monthly amount of credits | capture: sha256:c809c0a7ba5b6914c8ae06e43af5d718e11f6ff6fa298dd93704843b73d64e49 | quote: Organizations on the Free plan receive a fixed amount of credits each month.
  - [1] 2026-11-19: the Free plan is limited to five Serverless databases | capture: sha256:c809c0a7ba5b6914c8ae06e43af5d718e11f6ff6fa298dd93704843b73d64e49 | quote: No more than five Astra DB Serverless databases.
  - [1] 2026-11-19: inactive free databases are hibernated and scheduled for deletion | capture: sha256:c809c0a7ba5b6914c8ae06e43af5d718e11f6ff6fa298dd93704843b73d64e49 | quote: Inactive Astra DB Serverless databases are automatically [hibernated and scheduled for deletion](https://docs.datastax.com/en/astra-db-serverless/databases/database-statuses.html#hibernated).
  - [2] 2026-11-19: there is no byte cap on a Serverless database | capture: sha256:1f5498aa739ed24d68406a636fd23abe182b0746d396d3244f47d5eeaaace1d0 | quote: There is no practical limit to the number of bytes an Astra DB Serverless database can store.
  - [2] 2026-11-19: exhausted monthly credits suspend the database and block access to its data | capture: sha256:1f5498aa739ed24d68406a636fd23abe182b0746d396d3244f47d5eeaaace1d0 | quote: For Astra organizations on the Free plan, Astra DB Serverless databases are suspended if your monthly credits run out. While suspended, you cannot access the data in the database.
  - [3] 2026-11-19: free credits reset monthly and do not carry over | capture: sha256:489175ecab1619f1c15c99a40479aa89b2d3484cb6bb842da7e20de28624a2f1 | quote: Unused free credits don’t roll over to the next month. Free monthly credits reset on the first of every month for all organizations on the Free plan.
  - [4] 2026-11-19: signup uses email/password or SSO, with no card or phone required | capture: sha256:2bc1e5cd3fd07a9d2513aef127150a6ba66fbba974bd6878d8d2ecdb9fc15583 | quote: You can create an Astra account manually or use SSO to automatically provision an account through your IdP, Google, GitHub, or IBMid account.
- sources:
  - [1] https://docs.datastax.com/en/astra-db-serverless/administration/subscription-plans.html
  - [2] https://docs.datastax.com/en/astra-db-serverless/faqs.html
  - [3] https://docs.datastax.com/en/astra-db-serverless/administration/subscription-usage.html
  - [4] https://docs.datastax.com/en/astra-db-serverless/administration/manage-your-account.html
