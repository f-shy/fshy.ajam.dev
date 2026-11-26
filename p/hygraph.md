# Hygraph

> hygraph.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hygraph/ | JSON https://fshy.ajam.dev/api/v1/entity/hygraph.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hygraph

- `storage/hygraph` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-25T12:15:44.836Z (live) | stale on 2026-12-10
- url https://hygraph.com
- free tier: Unlimited asset storage on Hobby (free) with a 50 MB per-asset cap; 100 GB asset traffic/month | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 50 MB per asset | bytes: 50000000 | source: [1] | note: Hobby: 50 MB per asset upload size (maximum); the comparison table lists 200 MB per asset for the next plan, Growth.
- retention: The plan comparison lists a version retention period of '-' for Hobby, 14 days for Growth and up to 365 days for the third plan. | source: [1] | note: Plan columns are in the order Hobby, Growth, third plan; the Growth card lists '14-day version retention'..
- egress: 100 GB asset traffic/month on Hobby, served from a global CDN (media.graphassets.com) with image transforms. | metered: no
- identity: email
- interface: rest, graphql
- limits:
  - per-object-cap (binding): 50 MB per asset [1]
- limits note: 50 MB per asset (Free/Hobby; 200 MB on Growth). 100 GB/month traffic. 2 locales, 3 seats, 10 components. Content-model limits, not storage limits. 'Unlimited' is bounded in practice by the 100 GB traffic meter, not by bytes stored.
- interface detail: graphql
- tooling: GraphQL Management API + REST asset upload endpoint, `@hygraph/management-sdk`, asset CDN URLs are public and transformable
- composes with: Asset storage is unmetered in total capacity with a 50 MB file size cap. Bandwidth is limited to 100 GB per month on the Hobby plan.
- reliability: CDN-served, no expiry; the traffic cap is the failure mode (assets stop serving at 100 GB until reset).
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Hobby $0 always ... Unlimited asset storage | 50MB per asset upload size (maximum)'; 'Asset Traffic 100 GB'
  - [1] 2026-11-19: the Hobby plan offers unlimited asset storage with a 50 MB per-asset cap | capture: sha256:9f6d3a8ca4f33fc8aca5363c3f0f44784c5f9d4869c9eb3c830df2cde53be673 | quote: - Unlimited asset storage - 50MB per asset upload size (maximum)
  - [1] 2026-11-25: the Hobby plan caps an asset upload at 50 MB | capture: sha256:9f6d3a8ca4f33fc8aca5363c3f0f44784c5f9d4869c9eb3c830df2cde53be673 | quote: - Unlimited asset storage - 50MB per asset upload size (maximum)
  - [1] 2026-11-25: Hobby has no version retention period listed; Growth 14 days; third plan up to 365 days | capture: sha256:9f6d3a8ca4f33fc8aca5363c3f0f44784c5f9d4869c9eb3c830df2cde53be673 | quote: Version retention period - 14 days Up to 365 days
  - [1] 2026-11-25: the Growth plan card lists 14-day version retention | capture: sha256:9f6d3a8ca4f33fc8aca5363c3f0f44784c5f9d4869c9eb3c830df2cde53be673 | quote: - 14-day version retention
- sources:
  - [1] https://hygraph.com/pricing
