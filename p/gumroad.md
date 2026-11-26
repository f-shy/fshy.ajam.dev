# Gumroad

> gumroad.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gumroad/ | JSON https://fshy.ajam.dev/api/v1/entity/gumroad.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gumroad

- `storage/gumroad` | qualifies-with-caveat | evidence reported | binding per-object-cap | category Digital-product fulfilment
- needs card no, phone no, ID no, institution no | verified 2026-11-25T12:15:42.694Z (live) | stale on 2026-12-10
- url https://gumroad.com
- free tier: Free products have a file size limit of 250 MB. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: If you price your product at any number greater than $0.99, the largest single file that you can upload to a product is 20 GB in size. | bytes: 20000000000 | source: [1] | note: 20 GB per file applies to a product priced above $0.99; a free product is limited to 250 MB. The help article words the threshold both as greater than $0.99 and as higher than $1.
- retention: The terms state that Gumroad has no obligation to store any of Your Content that you Make Available on the Services. | source: [2] | note: Unpublishing a product does not delete the product or its data. Deleting a product is permanent and cannot be undone.
- egress: CloudFront in front of S3 (confirmed in their open-source repo: CLOUDFRONT_* + FILE_DOWNLOAD_DISTRIBUTION_URL_PROD). No per-download quota published. | metered: no
- identity: email | detail: an email address and a password, or a Google or X sign-in, on the signup form. No card and no phone number appear on that form, and uploading files needs no payout profile; withdrawing sales runs a Stripe identity check that asks for a date of birth, phone number and possibly a government ID.
- interface: rest, cli
- limits:
  - per-object-cap (binding): largest single file that you can upload to a product is 20 GB [1]
- limits note: Per-object-cap 20 GB (products >$0.99) / 250 MB cumulative (priced $0). 'Download all' button only appears under 500 MB total content, but a single ZIP sidesteps that. Repo shows MAX_EPUB_READER_ARCHIVE_SIZE = 32 MB and thumbnail cap 5 MB. Those are feature caps, not the product-file cap.
- interface detail: Web + documented REST API (products, product_files); the codebase is open source (antiwork/gumroad), so limits are inspectable.
- tooling: REST API with access token; the repo exposes /attachments/... presigned paths via SignedUrlHelper.
- composes with: Pricing a product above $0.99 raises the largest single file to 20 GB, and a product can hold as many files as you want. A product priced at $0 is limited to 250 MB of files in total.
- reliability: Purchases require a payment method on the seller side to withdraw, but uploading does not. Download URLs are presigned CloudFront/S3 and short-lived, so there is no stable hot-link. Archive/delivery tier only.
- notes: Own help centre: 'If you price your product at any number greater than $0.99, the largest single file that you can upload to a product is 20 GB in size... you can add as many files as you want to each product.' Free/$0 products are capped at 250 MB cumulative.
- evidence note: the same as the free tier
- evidence:
  - [1] 2026-10-21: '20 GB File size limit' and '250 MB limit' sections, verbatim
  - withheld 2026-10-21: raw.githubusercontent.com/antiwork/gumroad/main/app/models/product_file.rb — confirms S3/CloudFront storage classes and that 20 GB is not enforced in this model, i.e. it is a policy cap at the uploader
  - withheld 2026-10-21: config/initializers/aws.rb + .env.example in the same repo — CLOUDFRONT_DOWNLOAD_DISTRIBUTION_URL_PROD, FILE_DOWNLOAD_DISTRIBUTION_URL_PROD, S3_BUCKET production 'gumroad'
  - [3] 2026-10-21: 200, 128,717 B (live, not a dead host)
  - [4] 2026-11-01: the signup form offers a Google or X sign-in, or an email address and a password, and asks for nothing else | capture: sha256:8bad6bea609c0f745e7565609629ce67a9960fb50010b2c0507525d9f7416469 | quote: Google X or EmailPassword
  - [1] 2026-11-01: the 20 GB per-file ceiling for a priced product is unchanged | capture: sha256:5b79619742235a4fbd709d7feec6e809374e6250ac0510cb4e2621d0cd7b9d89 | quote: If you price your product at any number greater than $0.99, the largest single file that you can upload to a product is 20 GB in size.
  - [1] 2026-11-09: The help page states the free-product limit this record relies on. | capture: sha256:d2dec94f4238bc306404125c6363eb8ccd01d0a36d56be63383982bad6ef391b | quote: Free products have a file size limit of 250 MB.
  - [1] 2026-11-09: The help page states the priced-product file limit verbatim. | capture: sha256:d2dec94f4238bc306404125c6363eb8ccd01d0a36d56be63383982bad6ef391b | quote: If you price your product at any number greater than $0.99, the largest single file that you can upload to a product is 20 GB in size.
  - [4] 2026-11-09: the page states the confirmed value | capture: sha256:8a6b08707ad916b7b705aa7a310e5aaeda4e663e3c538c5f134ebf5c649cae1b | quote: Email
  - [2] 2026-11-25: the terms disclaim any obligation to store uploaded content | capture: sha256:793c6631b9b3edf2b3191f504ef5b0165d7dcdb748224f3d39171dc0f676815e
  - [2] 2026-11-25: the retention statement is on the terms page, not the file-size article | capture: sha256:793c6631b9b3edf2b3191f504ef5b0165d7dcdb748224f3d39171dc0f676815e
  - [5] 2026-11-25: the help article states that deletion of a product is permanent | capture: sha256:053c275789eccc76ec225eed25daf16244a73aa22aad8490829ed4c45d95824b | quote: Deleting a product is permanent and cannot be undone.
  - [5] 2026-11-25: the help article states that unpublishing keeps the product and its data | capture: sha256:053c275789eccc76ec225eed25daf16244a73aa22aad8490829ed4c45d95824b | quote: Unpublishing does not delete your product or any data associated with it.
  - [1] 2026-11-25: the article gives the 250 MB free-product and 20 GB priced-product limits | capture: sha256:349294412f63d3e28b388836d6f71de1afe2f46e84a321a14ea5b030677619d1 | quote: Free products have a file size limit of 250 MB. Products priced higher than $1 have a file size limit of 20 GB.
  - [1] 2026-11-25: the 20 GB per-file ceiling for a product priced above $0.99 | capture: sha256:349294412f63d3e28b388836d6f71de1afe2f46e84a321a14ea5b030677619d1 | quote: If you price your product at any number greater than $0.99, the largest single file that you can upload to a product is 20 GB in size.
  - [1] 2026-11-25: a product can hold as many files as the seller adds | capture: sha256:349294412f63d3e28b388836d6f71de1afe2f46e84a321a14ea5b030677619d1 | quote: Remember, you can add as many files as you want to each product.
  - [6] 2026-11-25: Gumroad publishes a command-line client over the same API | capture: sha256:101c6f6b97b40d31a49495c2bbb5fec9f0a2a1bd75aeeae7ec3db3d5fb29e2c9 | quote: Prefer a terminal? The Gumroad CLI wraps every endpoint below and is built for humans and AI agents alike.
  - [6] 2026-11-25: the API is REST with JSON responses | capture: sha256:101c6f6b97b40d31a49495c2bbb5fec9f0a2a1bd75aeeae7ec3db3d5fb29e2c9 | quote: The Gumroad OAuth API is based around REST.
  - [1] 2026-11-25: the 20 GB per-file ceiling for a priced product is unchanged | capture: sha256:349294412f63d3e28b388836d6f71de1afe2f46e84a321a14ea5b030677619d1 | quote: If you price your product at any number greater than $0.99, the largest single file that you can upload to a product is 20 GB in size.
- sources:
  - [1] https://gumroad.com/help/article/289-file-size-limits-on-gumroad
  - [2] https://gumroad.com/terms
  - [3] https://gumroad.com/
  - [4] https://gumroad.com/signup
  - [5] https://gumroad.com/help/article/248-delete-a-product
  - [6] https://gumroad.com/api
