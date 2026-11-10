# Sellfy

> sellfy.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sellfy/ | JSON https://fshy.ajam.dev/api/v1/entity/sellfy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sellfy

- `storage/sellfy` | qualifies-with-caveat | evidence reported | binding per-object-cap | category Digital-product storefront
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://sellfy.com
- price $22/mo on Starter; 20 GB/file, so ~$22 for unlimited-but-policed TB — priced per plan, not per TB. Effectively $0/TB until policed. | parsed USD 22/mo
- free tier: Their own sell-downloads page: 'Upload unlimited eBooks, music, software, courses, or other digital products packing up to 50 files per product, with each file weighing in at up to 20GB.' FAQ repeats: 'As many as you want! There are no limits to the number of products... Each file can be up to 20GB in size.' | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 20 GB | bytes: 20000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No bandwidth quota published. Assets served from d369wu82uo9y4b.cloudfront.net (CloudFront). | metered: no
- identity: email | detail: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap 20 GB [1]
- limits note: per-object-cap 20 GB; 50 files/product; unlimited products. No aggregate cap stated.
- interface detail: Web upload; REST API on paid plans.
- tooling: Web/API.
- composes with: Allows up to 20 GB per file, supporting 50 files per product and unlimited products on store accounts.
- reliability: No free tier. Plans start at $22/mo with a 14-day trial, so it is paid-only. CloudFront egress is a cost the seller does not see but which the platform will police.
- notes: the same as the free tier
- extras:
  - price_verbatim: $22/mo on Starter; 20 GB/file, so ~$22 for unlimited-but-policed TB — priced per plan, not per TB. Effectively $0/TB until policed.
- evidence:
  - [1] 2026-10-21: 'Unlimited storage ... up to 50 files per product, with each file weighing in at up to 20GB' (quoted from the page's own FAQPage JSON-LD, i.e. structured data the vendor publishes)
  - [2] 2026-10-21: 'Plans From $22/mo', 14-day free trial, no free tier
- sources:
  - [1] https://sellfy.com/sell-downloads/
  - [2] https://sellfy.com/pricing/
