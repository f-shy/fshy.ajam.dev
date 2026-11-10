# Hygraph

> hygraph.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hygraph/ | JSON https://fshy.ajam.dev/api/v1/entity/hygraph.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hygraph

- `storage/hygraph` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://hygraph.com
- free tier: Unlimited asset storage on Hobby (free) with a 50 MB per-asset cap; 100 GB asset traffic/month | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 50 MB per asset | bytes: 50000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
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
- sources:
  - [1] https://hygraph.com/pricing
