# SST

> sst.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sst/ | JSON https://fshy.ajam.dev/api/v1/entity/sst.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SST

- `compute/sst` | paid-only | evidence documented | binding write-gated | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://sst.dev/docs/console/
- free tier: The SST Console is free for workspaces with 350 or fewer active resources a month, with no credit card to start; above that it is USD 0.086 per active resource for the first 2,000 and USD 0.032 beyond. The Console is a dashboard over an app that SST deploys into the customer's own AWS account, so the compute is an AWS bill and the Console contributes no runtime. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-control-plane
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: the card belongs to the AWS account, not to the Console: the record's own limits row reads that "the capacity itself is gated by the AWS account behind it, which needs a card", while the docs state "the Console is completely free to get started and an account can be created without a credit card", with billing details needed only above 350 active resources a month, where production and deployed stages block until they are added. So signing up for the free Console tier takes no card and no hold exists there, and no compute is obtained either, because the Console contributes no runtime; the record does not state what the Console signup asks for — an email or a GitHub account — nor the AWS account's card terms, debit or prepaid acceptance
- interface: unknown
- limits:
  - write-gated (binding): the free tier is a count of 350 active resources a month in the Console, and the capacity itself is gated by the AWS account behind it, which needs a card. [1]
- limits note: the free tier is a count of 350 active resources a month in the Console, and the capacity itself is gated by the AWS account behind it, which needs a card.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: SST is the cheapest way to describe AWS infrastructure in TypeScript and the Console is free at hobby size, but every service it creates bills to AWS; it composes with AWS credits and with nothing else among documented hosts.
- reliability: no reliability event recorded
- notes: SST Ion provides deployment tooling for applications running on AWS infrastructure. The SST Console includes a recurring free tier up to 350 managed resources; AWS compute costs bill separately.
- extras:
  - facets.class: bring-your-own-cloud
  - facets.free_tier_kind: free-control-plane
- evidence:
  - [1] 2026-10-22: 'Free Tier: Workspaces with 350 active resources or fewer'; 351 resources in a month bills USD 30.20 at USD 0.086 per resource; the count resets monthly, quoted
  - [1] 2026-10-22: the Console is completely free to get started and an account can be created without a credit card; going over the free tier blocks production and deployed stages until billing details are added, while personal stages stay accessible, quoted
  - [1] 2026-10-22: a resource is what SST creates in your cloud provider and is active if its stage is at least two weeks old and was updated during the month, quoted
- sources:
  - [1] https://sst.dev/docs/console/
