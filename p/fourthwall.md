# Fourthwall

> fourthwall.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fourthwall/ | JSON https://fshy.ajam.dev/api/v1/entity/fourthwall.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fourthwall

- `storage/fourthwall` | fails-quota | evidence reported | binding none | category Creator merch + digital products
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://fourthwall.com
- free tier: 1 GB per listing (all files counted together) on paid/members-only products; 25 MB total for free digital products. 50 products on Free, 500 on Pro. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No published egress cap; assets on cdn.fourthwall.com. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: per-listing 1 GB (aggregate across files). 50/500 product caps.
- interface detail: Documented developer API (docs.fourthwall.com) with signed URLs; the `size` you declare is enforced at URL issue time.
- tooling: REST API + signed URLs.
- composes with: 1 GB x 500 products on Pro = 500 GB ceiling. The only provider here where the account product count, not the file size, is the binding number.
- reliability: Developer docs note the declared size is enforced 'both when the URL is issued and by the signed URL itself'. Sending more bytes than declared fails the upload, which is the opposite of the usual under-enforcement pattern.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 GB per listing (all files counted together) on paid/members-only products; 25 MB total for free digital products. 50 products on Free, 500 on Pro.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free digital products have a 25MB total file size limit per listing. Paid digital products support up to 1GB per listing'
  - [2] 2026-10-21: 'Digital files are size-limited per shop: 25 MB on free plans, up to 1 GB otherwise... sending more bytes than declared fails the upload'
  - [3] 2026-10-21: Free 50 products, Pro 500
- sources:
  - [1] https://help.fourthwall.com/frequently-asked-questions/products-and-shop-features/digital-product-file-size-limit
  - [2] https://docs.fourthwall.com/guides/create-digital-products
  - [3] https://help.fourthwall.com/hc/en-us/articles/40316344599707
