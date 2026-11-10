# TiDB Cloud Starter

> pingcap.com | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pingcap/ | JSON https://fshy.ajam.dev/api/v1/entity/pingcap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TiDB Cloud Starter

- `databases-kv/tidb-cloud-starter` | qualifies | evidence documented | binding request-rate | category distributed SQL, MySQL compatible
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-22
- url https://www.pingcap.com/pricing/
- price USD 0.10 per million RUs beyond the allowance
- free tier: 25 GiB row storage plus 25 GiB columnar storage and 250 million Request Units per month, per organization across up to five instances | unit: GiB | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: 25 GiB row storage per organization on the allowance; the FAQ states 5 GiB per instance | source: [1] | note: the two first-party pages disagree on whether the allowance is per instance or per org
- retention: an instance persists while the organization is active; no deletion clock published | source: [2]
- egress: no transfer allowance and no per-GB egress rate is published on the pricing page; recorded as a gap. Traffic is billed through the request-unit and storage meters the page does publish | metered: no | source: [1]
- identity: email | detail: email signup for the free allowance; a card only to exceed five instances
- interface: rest, cli
- limits:
  - request-rate (binding): 250 million Request Units per month on the org allowance; the FAQ prints 50 million per instance [1]
  - per-object-cap: 25 GiB row plus 25 GiB columnar per organization; five instances [1]
  - write-gated: a credit card and a spend limit are required to create more than five Starter instances [2]
  - request-rate (binding): 400 concurrent connections per Starter instance, rising to 5,000 with a spending limit; the public-endpoint idle timeout is 340 seconds [3]
- interface detail: the MySQL wire protocol with TLS; a Cloud API and the tiup CLI
- tooling: any MySQL client, the tiup CLI, the Data Migration tool
- composes with: the largest card-free relational allowance found in this class, which is why it is the first row a reader should try
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: The two pages disagree by a factor of five and the direction matters. 25 GiB per org is the number the pricing page states today; 5 GiB per instance is what the FAQ states. Until one is measured, the conservative reading is 5 GiB per instance and 25 GiB per org across five.
- evidence note: two first-party pages were read and they disagree. The record keeps the conservative per-instance reading and names the disagreement.
- extras:
  - page_disagreement: the docs FAQ's figure is the older per-instance plan and the pricing page's is the current org allowance
- evidence:
  - [1] 2026-10-22: Free monthly allowance: 25 GiB row storage, 25 GiB columnar storage, 250M Request Units, per organization across up to five eligible instances; rates beyond from USD 0.10 per million RUs
  - [2] 2026-10-22: 'Always-free monthly quota for up to five TiDB Cloud Starter instances per organization (5 GiB row data + 5 GiB columnar data + 50 million RUs per TiDB Cloud Starter instance)'; 'you can create a maximum of five TiDB Cloud Starter instances by default. To create more ... you need to add a credit card'
- sources:
  - [1] https://www.pingcap.com/pricing/
  - [2] https://docs.pingcap.com/tidbcloud/serverless-faqs/
  - [3] https://docs.pingcap.com/tidbcloud/serverless-limitations/
