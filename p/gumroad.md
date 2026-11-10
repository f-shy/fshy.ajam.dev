# Gumroad

> gumroad.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gumroad/ | JSON https://fshy.ajam.dev/api/v1/entity/gumroad.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gumroad

- `storage/gumroad` | qualifies-with-caveat | evidence reported | binding per-object-cap | category Digital-product fulfilment
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:05:08.102Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://gumroad.com
- free tier: Own help centre: 'If you price your product at any number greater than $0.99, the largest single file that you can upload to a product is 20 GB in size... you can add as many files as you want to each product.' Free/$0 products are capped at 250 MB cumulative. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: largest single file that you can upload to a product is 20 GB | bytes: 20000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: CloudFront in front of S3 (confirmed in their open-source repo: CLOUDFRONT_* + FILE_DOWNLOAD_DISTRIBUTION_URL_PROD). No per-download quota published. | metered: no
- identity: email | detail: an email address and a password, or a Google or X sign-in, on the signup form. No card and no phone number appear on that form, and uploading files needs no payout profile; withdrawing sales runs a Stripe identity check that asks for a date of birth, phone number and possibly a government ID.
- interface: rest
- limits:
  - per-object-cap (binding): largest single file that you can upload to a product is 20 GB [1]
- limits note: Per-object-cap 20 GB (products >$0.99) / 250 MB cumulative (priced $0). 'Download all' button only appears under 500 MB total content, but a single ZIP sidesteps that. Repo shows MAX_EPUB_READER_ARCHIVE_SIZE = 32 MB and thumbnail cap 5 MB. Those are feature caps, not the product-file cap.
- interface detail: Web + documented REST API (products, product_files); the codebase is open source (antiwork/gumroad), so limits are inspectable.
- tooling: REST API with access token; the repo exposes /attachments/... presigned paths via SignedUrlHelper.
- composes with: The $0.99 pricing gate is the mechanism: price at $1, get 20 GB/file, unlimited files per product, unlimited products. A $1 product that never sells still costs the seller ~nothing after fees. 20 GB x N files.
- reliability: Purchases require a payment method on the seller side to withdraw, but uploading does not. Download URLs are presigned CloudFront/S3 and short-lived, so there is no stable hot-link. Archive/delivery tier only.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '20 GB File size limit' and '250 MB limit' sections, verbatim
  - withheld 2026-10-21: raw.githubusercontent.com/antiwork/gumroad/main/app/models/product_file.rb — confirms S3/CloudFront storage classes and that 20 GB is not enforced in this model, i.e. it is a policy cap at the uploader
  - withheld 2026-10-21: config/initializers/aws.rb + .env.example in the same repo — CLOUDFRONT_DOWNLOAD_DISTRIBUTION_URL_PROD, FILE_DOWNLOAD_DISTRIBUTION_URL_PROD, S3_BUCKET production 'gumroad'
  - [2] 2026-10-21: 200, 128,717 B (live, not a dead host)
  - [3] 2026-11-01: the signup form offers a Google or X sign-in, or an email address and a password, and asks for nothing else | capture: sha256:8bad6bea609c0f745e7565609629ce67a9960fb50010b2c0507525d9f7416469 | quote: Google X or EmailPassword
  - [1] 2026-11-01: the 20 GB per-file ceiling for a priced product is unchanged | capture: sha256:5b79619742235a4fbd709d7feec6e809374e6250ac0510cb4e2621d0cd7b9d89 | quote: If you price your product at any number greater than $0.99, the largest single file that you can upload to a product is 20 GB in size.
- sources:
  - [1] https://gumroad.com/help/article/289-file-size-limits-on-gumroad
  - [2] https://gumroad.com/
  - [3] https://gumroad.com/signup
