# SurrealDB Cloud

> surrealdb.com | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/surrealdb/ | JSON https://fshy.ajam.dev/api/v1/entity/surrealdb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SurrealDB Cloud

- `databases-kv/surrealdb-cloud` | qualifies-with-caveat | evidence documented | binding request-rate | category multi-model database (document, graph, vector, time-series), serverless and node hosted | tier Earth Free
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T00:19:24.795Z (live) | stale on 2026-12-20
- url https://surrealdb.com/pricing
- free tier: Free $0/mo 3M requests, 10GB storage, no card | unit: mixed | metered on: request-count | read on: 2026-11-19 | source: [1] | note: Earth Free is a monthly allowance of 3M requests, 10 GB storage and 100 database active hours. A separate always-free Cloud single node (1 GB storage, 0.25 vCPU, 1 GB memory) is also listed.
- per-object cap: no per-object cap published on the pricing or Earth limits pages; records and transactions are metered by request units | source: [2]
- retention: Free pauses at a limit and keeps your data; an idle Earth instance scales to zero about 60 seconds after its last query. No automatic deletion of data on the free plan is stated. | source: [1] | note: days null is indefinite: the page states data is kept when the Free allowance is spent.
- egress: | Egressper month | Unlimited | Unlimited | | metered: no | free allowance: unlimited | source: [1]
- identity: email | detail: Create an account with Google, GitHub or email, and sign in. An account needs no payment details. The free instance type carries no charge, so you can deploy before you add a payment method.
- interface: graph, rest, cli
- limits:
  - request-rate (binding): 3M requests per month on Earth Free; 100 clients connected to one instance at once [1]
  - volume-quota: 10 GB storage and 100 database active hours per month on Earth Free [1]
  - write-gated: 100 Earth instances per organisation on Free; deploying is refused when the organisation already has 100 or has spent the month's allowance [2]
- binding note: the 3M-request monthly allowance and the 100-client connection ceiling are reached before the 10 GB storage cap for a typical interactive workload
- interface detail: SurrealQL over WebSocket (wss://<instance-id>.surrealdb.earth/rpc) and HTTP, plus PostgreSQL and MySQL wire protocols; the surreal cloud management CLI and SurrealDB Studio browser UI
- tooling: SurrealDB Studio, surreal cloud CLI, official SDKs, HTTP queries, and psql or mysql clients over TLS
- composes with: the serverless Earth free tier scales to zero and can be reached from a Worker or a server-side app; when steady capacity is needed the paid Cloud single-node plan is the next step
- reliability: Earth is in beta; features, limits and pricing may change before general availability. Earth takes no snapshots and has no backup schedule, and an instance that reaches its Free allowance pauses until the first of the next month.
- notes: The free allowance is shared across all Earth instances in one organisation, so many small databases do not each get 3M requests. Earth cannot coordinate a transaction across instances and has no change feeds, extensions, JavaScript functions or reliable file buckets, so workloads that need those features must use the paid Start or Scale node plans. The always-free Cloud single node (1 GB, 0.25 vCPU) is a separate free offer from Earth Free.
- evidence note: all figures are from first-party pricing and docs pages read; no public read path was probed, so the rung stays documented
- evidence:
  - [1] 2026-11-19: the Earth Free plan is $0 a month with 3M requests and 10 GB storage and needs no card | capture: sha256:d6c0b28bc7d60f4199260bbff97bf3ba7fe00f44244ccb855f1f469e7c2be8e6 | quote: Free $0/mo 3M requests, 10GB storage, no card
  - [1] 2026-11-19: network egress is unlimited on the Free Earth plan | capture: sha256:d6c0b28bc7d60f4199260bbff97bf3ba7fe00f44244ccb855f1f469e7c2be8e6 | quote: | Egressper month | Unlimited | Unlimited |
  - [1] 2026-11-19: hitting a Free limit pauses the database rather than deleting the data | capture: sha256:d6c0b28bc7d60f4199260bbff97bf3ba7fe00f44244ccb855f1f469e7c2be8e6 | quote: Free pauses at a limit and keeps your data. Pro includes an allowance, then bills each meter by usage.
  - [2] 2026-11-19: the free allowance is monthly and pauses instances until the next month while keeping the data | capture: sha256:2b8c576b43661aa8c1c5d748af5861df67e4851fd8f5fd3a541daa54d383e673 | quote: Earth Free includes a monthly allowance of request units, active hours, storage, live updates and client time. When the allowance is spent, the organisation's Earth instances pause until the first day of the next month (UTC). The data is kept.
  - [2] 2026-11-19: Earth Free allows 100 simultaneous connected clients per instance | capture: sha256:2b8c576b43661aa8c1c5d748af5861df67e4851fd8f5fd3a541daa54d383e673 | quote: | Clients connected to one instance at once | 100 | 10,000 |
  - [3] 2026-11-19: signup needs no card or payment detail | capture: sha256:7292b5aefc509ecf1c87f592e39f75a41d2cd4a336166769eb6f401fc55fbec6 | quote: An account needs no payment details. The free instance type carries no charge, so you can deploy before you add a payment method.
  - [3] 2026-11-19: registration accepts email, Google or GitHub; no phone or ID is named | capture: sha256:7292b5aefc509ecf1c87f592e39f75a41d2cd4a336166769eb6f401fc55fbec6 | quote: Create an account with Google, GitHub or email, and sign in.
- sources:
  - [1] https://surrealdb.com/pricing
  - [2] https://surrealdb.com/docs/operate/instances/earth
  - [3] https://surrealdb.com/docs/cloud/getting-started/create-an-account
