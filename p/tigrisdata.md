# cunofs

> tigrisdata.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tigrisdata/ | JSON https://fshy.ajam.dev/api/v1/entity/tigrisdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tigris

- `storage/tigris` | qualifies-with-caveat | evidence documented | binding volume-quota | category S3-compatible object storage, globally distributed
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:05:15.751Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://www.tigrisdata.com/pricing/
- price USD 20.48 per TiB-month Standard, USD 10.24 Infrequent Access, USD 4.10 Archive or Archive Instant Retrieval (USD 0.02, 0.01 and 0.004 per GB-month of 2^30 bytes, global or single-region); multi-region USD 0.025, 0.015 and 0.006 per GB-month | parsed USD 18.63/TB-mo
- free tier: 5 GB of Standard-tier storage, 10,000 Class A requests (PUT, COPY, POST, LIST) and 100,000 Class B requests (GET, SELECT and all other) a month on every account; the allowance resets monthly, covers the Standard tier only and applies before anything is metered | unit: GB | metered on: stored-bytes | read on: 2026-10-30 | source: [1] | note: storage is billed in binary GB (2^30 bytes) as the average of the daily peak over the month; DELETE and CANCEL requests are free
- per-object cap: large objects up to 5 TB, under standard S3 multipart semantics | source: [2] | note: the page does not say whether 5 TB is decimal or binary
- retention: source: [1] | note: not stated
- egress: Free on every tier and location type: no charge for regional, region-to-region or internet egress, and no ratio or monthly cap is published; the pricing page asks for contact when bandwidth requirements are extraordinary. Reading Infrequent Access and Archive Instant Retrieval objects carries a retrieval fee, separate from egress. | metered: no
- identity: email | detail: the sign-up form asks an email address and a password, with Google and GitHub as alternatives, and shows no phone field and no card field; no card is required to start on the free allowance; a public bucket needs payment-method verification on organisations created after 18 May 2026
- interface: s3-compatible, rclone
- limits:
  - volume-quota (binding): 5 GB of Standard storage, 10,000 Class A and 100,000 Class B requests a month free; above it Standard storage is USD 0.02 per GB-month [1]
  - per-object-cap: 5 TB per object [2]
- limits note: Minimum storage duration: none on Standard, 30 days on Infrequent Access, 90 days on Archive and Archive Instant Retrieval; an object deleted, updated or transitioned earlier is billed for the full minimum, and one kept longer is billed for the days stored. Retrieval fee: USD 0.01 per GB on Infrequent Access, USD 0.03 per GB on Archive Instant Retrieval, free on Standard and Archive. An Archive object is restored before it is read: it moves to the Standard tier for a chosen duration and is billed at the Standard rate meanwhile. Storage is measured in binary GB (2^30 bytes).
- binding note: the free allowance is 5 GB of Standard storage a month; every GB-month above it is billed, so the quota ends the free path before any other limit
- interface detail: S3 API
- tooling: All S3 SDKs, rclone, bucket forking, lifecycle rules, soft deletes
- composes with: S3-compatible origin with no egress charge, usable behind a CDN or proxy front end; anonymous reads from a public bucket need payment-method verification on organisations created after 18 May 2026, so an account with no card keeps its buckets private.
- reliability: Public-bucket access is gated by payment-method verification on organisations created after 18 May 2026, stated as an abuse control; no throttle is published, and extraordinary bandwidth leads to a contact request.
- notes: Per-GB-month, 5 GB free (Standard); tiers Standard / Infrequent Access / Archive Instant Retrieval / Archive
- evidence note: free allowance, sign-up identity, egress, retrieval fees, minimum storage durations and the object cap quoted from the vendor pricing page, its Markdown version and the public-bucket and multipart documentation on 2026-10-30
- extras:
  - price_verbatim: Standard $20.00/TB at 5 TB and 20 TB. Archive $4.00/TB at 20 TB ($80/mo) with free egress and free retrieval — the best cold tier after OVH Cold Archive.
- evidence:
  - [1] 2026-10-21: rate table strings from raw HTML: $0.02/GB/month (Standard), $0.01/GB/month (IA), $0.004/GB/month (Archive Instant Retrieval), $0.004/GB/month (Archive); retrieval $0.01/GB (IA), $0.03/GB (Archive IR), Free (Standard/Archive); "Egress Free" on all tiers
  - [1] 2026-10-21: "A minimum storage retention charge applies to objects stored in the Infrequent Access, Archive, and Archive Instant Retrieval tiers... 30-day storage charge will still apply"
  - [3] 2026-10-21: Tigris included in normalized comparison, checked 17 Oct 2026
  - [1] 2026-10-30: the free allowance is 5 GB of Standard storage, 10,000 Class A and 100,000 Class B requests | capture: sha256:f94a4de1d37844fd69eaf5656fea679db456d2c4a89d168575b5e6160b090dc0 | quote: First 5 GB of Standard storage free. First 10,000 Class A and 100,000 Class B requests free.
  - [1] 2026-10-30: no card is asked to start; the allowance resets monthly and applies before metering | capture: sha256:f94a4de1d37844fd69eaf5656fea679db456d2c4a89d168575b5e6160b090dc0 | quote: No card to start. The allowance below resets monthly and applies before anything is metered.
  - [4] 2026-10-30: storage is metered on stored bytes, as the average of daily peaks over the month | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: A GB/month is determined by averaging the daily peak storage over a billing period (1 month).
  - [4] 2026-10-30: the free allowance was read on 2026-10-30 | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: 5 GB of standard data storage per month
  - [4] 2026-10-30: a billed GB is 2^30 bytes | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: Tigris measures storage in binary gigabytes (GB), where 1 GB equals 2^30 bytes.
  - [4] 2026-10-30: no egress charge of any kind | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: Tigris does not charge for regional data transfer, region-to-region data transfer, or data transfer out to the internet (egress).
  - [4] 2026-10-30: extraordinary bandwidth leads to a contact request; no figure is published | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: If your bandwidth requirements are extraordinary, contact help@tigrisdata.com.
  - [4] 2026-10-30: egress is free on all four tiers | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: | Egress | Free | Free | Free | Free |
  - [4] 2026-10-30: sign-up asks no credit card | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: No credit card required to get started
  - [5] 2026-10-30: a public bucket needs payment-method verification | capture: sha256:729f30c6bb99ca9d33aa7f03aae12e8feb5fe54b5875df9a31c4cc621f1edc50 | quote: However, to prevent abuse, payment method verification is required to use public bucket functionality.
  - [5] 2026-10-30: the public-bucket payment-method gate applies to organisations created after 18 May 2026 | capture: sha256:729f30c6bb99ca9d33aa7f03aae12e8feb5fe54b5875df9a31c4cc621f1edc50 | quote: This requirement applies to all organizations created after May 18, 2026.
  - [6] 2026-10-30: the console sign-in asks an email address and a password, with Google and GitHub as alternatives | capture: sha256:262308829ee7e77fb409f1c93ab1621affe0ec6e1e97e68790d7d50830a3df56 | quote: Please enter an email address
  - [4] 2026-10-30: storage costs USD 0.02, 0.01, 0.004 and 0.004 per GB-month on Standard, Infrequent Access, Archive and Archive Instant Retrieval | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: | Data Storage | $0.02/GB/month | $0.01/GB/month | $0.004/GB/month | $0.004/GB/month |
  - [7] 2026-10-30: the largest object is 5 TB | capture: sha256:770f1696311e5ff5d4968c76b223278fc13dac51a68875325b8396aa8aeb9da5 | quote: Standard S3 multipart semantics apply (e.g., large objects up to 5 TB).
  - [1] 2026-10-30: the free path ends at 5 GB of Standard storage | capture: sha256:f94a4de1d37844fd69eaf5656fea679db456d2c4a89d168575b5e6160b090dc0 | quote: First 5 GB of Standard storage free. First 10,000 Class A and 100,000 Class B requests free.
  - [4] 2026-10-30: minimum storage duration is none on Standard, 30 days on Infrequent Access, 90 days on Archive and Archive Instant Retrieval | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: | Min. Storage Retention | N/A | 30 days | 90 days | 90 days |
  - [4] 2026-10-30: retrieval is free on Standard and Archive, USD 0.01 per GB on Infrequent Access and USD 0.03 per GB on Archive Instant Retrieval | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: | Data Retrieval | Free | $0.01/GB | Free | $0.03/GB |
  - [4] 2026-10-30: an early delete, update or transition is billed for the full minimum | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: If objects are deleted, updated, or transitioned to another storage tier before 30 days, a 30-day storage charge will still apply.
  - [4] 2026-10-30: an Archive object is restored into Standard for a chosen duration before it is read | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: When you restore data from the Archive tier, the data is moved to the Standard tier for the duration you specify.
  - [4] 2026-10-30: the vendor pricing page was read and quoted | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: | Min. Storage Retention | N/A | 30 days | 90 days | 90 days |
  - [4] 2026-10-30: the vendor pricing page was read and quoted | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: 5 GB of standard data storage per month
  - [4] 2026-10-30: the pricing page states the free allowance, tier prices, retrieval fees, minimum durations and free egress | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: 5 GB of standard data storage per month
  - [8] 2026-11-01: the public-bucket payment-method gate applies to organisations created after 18 May 2026 | capture: sha256:729f30c6bb99ca9d33aa7f03aae12e8feb5fe54b5875df9a31c4cc621f1edc50 | quote: This requirement applies to all organizations created after May 18, 2026.
  - [9] 2026-11-01: the sign-up form has an email field and a password field only | capture: sha256:ef4776bd12f67063fc4463e0742761d54e1da68c6940ca778d516eb2e05e3932 | quote: Password \*Show password
  - [8] 2026-11-01: a public bucket needs payment-method verification | capture: sha256:729f30c6bb99ca9d33aa7f03aae12e8feb5fe54b5875df9a31c4cc621f1edc50 | quote: to prevent abuse, payment method verification is required to use public bucket functionality
  - [4] 2026-11-01: no card is needed to start on the free allowance | capture: sha256:e5f984823b107f31e9a0e521d896a0b88340756b1b8e637f2a18cbc9c43d7436 | quote: No credit card required to get started
- sources:
  - [1] https://www.tigrisdata.com/pricing/
  - [2] https://www.tigrisdata.com/docs/objects/multipart-uploads/
  - [3] https://c17.io/compare/object-storage
  - [4] https://www.tigrisdata.com/pricing.md
  - [5] https://www.tigrisdata.com/docs/buckets/public-bucket.md
  - [6] https://console.storage.dev
  - [7] https://www.tigrisdata.com/docs/objects/multipart-uploads.md
  - [8] https://www.tigrisdata.com/docs/buckets/public-bucket/
  - [9] https://console.storage.dev/signup

## cunofs / tigris / garage / hammerspace / weka as free-tier poolers

- `storage/cunofs-tigris-garage-hammerspace-weka-as-free-tier-poole` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.tigrisdata.com/pricing/
- free tier: none reachable: Wrong problem class, and none of them advertises stacking free tiers. cunoFS is an HPC POSIX-on-object mount (docs now 404 at the previously indexed readthedocs paths, and it is a paid… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Wrong problem class, and none of them advertises stacking free tiers. cunoFS is an HPC POSIX-on-object mount (docs now 404 at the previously indexed readthedocs paths, and it is a paid…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Wrong problem class, and none of them advertises stacking free tiers. cunoFS is an HPC POSIX-on-object mount docs now 404 at the previously indexed readthedocs paths, and it is a paid Storj
  - [2] 2026-10-21: cited as the basis of the rejection: Wrong problem class, and none of them advertises stacking free tiers. cunoFS is an HPC POSIX-on-object mount docs now 404 at the previously indexed readthedocs paths, and it is a paid Storj
  - [3] 2026-10-21: cited as the basis of the rejection: Wrong problem class, and none of them advertises stacking free tiers. cunoFS is an HPC POSIX-on-object mount docs now 404 at the previously indexed readthedocs paths, and it is a paid Storj
- sources:
  - [1] https://www.tigrisdata.com/pricing/
  - [2] https://garagehq.deuxfleurs.fr/
  - [3] https://cuno-cunofs.readthedocs-hosted.com/en/stable/user-guide-core-concepts.html
