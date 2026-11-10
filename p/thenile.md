# Nile

> thenile.dev | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thenile/ | JSON https://fshy.ajam.dev/api/v1/entity/thenile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nile

- `databases-kv/nile` | qualifies-with-caveat | evidence documented | binding request-rate | category multi-tenant Postgres
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-22
- url https://thenile.dev/pricing
- free tier: 50 million query tokens a month, unlimited databases and unlimited tenants per workspace, 1 GB storage included, up to 500 connections, in one region, with no pause on the free tier | unit: tokens | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: 1 GB of storage included on Free, then USD 1.50 per additional GB; no per-database cap is published, because the limits are per workspace and split across unlimited databases | bytes: 1000000000 | source: [1]
- retention: no deletion clock is published and the free tier does not pause: 'No, the db never pauses. We don't have any cold start time on the free tier.' The page publishes no inactivity or expiry policy for a free database | source: [1] | note: the free column states 1 day of backup retention; that is a backup window and not a data-retention clock
- egress: no egress allowance and no per-GB transfer line is published; the metered quantity is query tokens and storage | metered: no | source: [1]
- identity: email | detail: email signup; no card stated for the Free plan
- interface: rest, cli
- limits:
  - request-rate (binding): 50 million query tokens a month, then USD 0.06 per million additional tokens [1]
  - per-object-cap: 1 GB of storage included, then USD 1.50 per additional GB [1]
  - request-rate (binding): 500 connections on Free; Pro raises it to 10,000 and Scale to 100,000 [1]
- binding note: the token counter is the only hard meter. Storage and connections overage are both purchasable on the free tier without changing plan, and no pause or deletion is published, so the counter is what a reader designs against.
- interface detail: the Postgres wire protocol plus a control-plane API for tenant provisioning
- tooling: psql and any Postgres client; the Nile SDK
- composes with: a multi-tenant Postgres where the tenant count is free and the query volume is the meter, which is the opposite shape from a per-database free tier
- reliability: no pauses and no cold start are claimed on the free tier, and no suspension, throttle or data-loss event is recorded on the pages read
- notes: A query token is an abstract unit of CPU and memory. The page defines it but does not convert it, so the allowance cannot be expressed in rows or bytes. That is a discretionary meter in the sense that matters. There is no ceiling a reader can design against, only a price per unit. Two properties make the tier more useful than such a ceiling suggests. The limits are per workspace across unlimited databases, so tenant count is not the constraint. Reaching the limit is an overage and not a refusal. No inactivity or expiry policy is published. The free tier is the only one in this topic where the vendor states that it never pauses.
- evidence note: the pricing page was read for the allowances, the overage rates and the connection counts. The 'never pauses' and the overage-rather-than-refusal answers are the page's own FAQ, read through a search snippet because the collapsed answers do not survive extraction.
- evidence:
  - [1] 2026-10-22: Free column: unlimited databases, unlimited tenants, unlimited vector embeddings, 50 million query tokens then USD 0.06 per million, 1 GB storage then USD 1.50 per GB, 500 connections, one region, one branch, 1 day backup retention; Pro USD 15 with 150M tokens, 5 GB and 10,000 connections; Scale USD 350 with 500M tokens, 50 GB and 100,000 connections
  - [2] 2026-10-22: the FAQ answers, captured through the search index because the page renders them collapsed: 'No, the db never pauses. We don't have any cold start time on the free tier.'; 'most limits are per workspace'; 'You can typically pay for additional capacity without having to move to a higher tier. This is true even when you are on the free tier.'
  - [3] 2026-10-22: the architecture claim the free tier rests on: storage and compute are decoupled and the database 'scales to zero with no cold start time'
- sources:
  - [1] https://www.thenile.dev/pricing
  - [2] https://www.thenile.dev/pricing#faq
  - [3] https://thenile.dev/docs/getting-started
