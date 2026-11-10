# IEEE DataPort

> ieee-dataport.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ieee-dataport/ | JSON https://fshy.ajam.dev/api/v1/entity/ieee-dataport.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IEEE DataPort - 2 TB per dataset free upload, but every read costs $40/month

- `storage/ieee-dataport-2-tb-per-dataset-free-upload-but-every-rea` | fails-egress | evidence reported | binding none | category academic
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ieee-dataport.org/
- free tier: 2 TB of AWS S3 cloud storage per dataset for individual users (10 TB for institutional subscribers). No published limit on the number of datasets. Standard (non-Open-Access) deposit is free; making it Open Access costs $1,950. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Gated: 'Must be IEEE Paid DataPort Subscriber to Access Files' on the free Standard tier. Reader pays $40/month individual, or the depositor pays $1,950 once for Open Access so anyone can download. | metered: yes
- identity: email | detail: email
- interface: s3-compatible, rest
- limits note: 2 TB/dataset; read behind subscriber paywall on the free tier; no private-dataset capability on the individual plan.
- interface detail: rest
- tooling: Web upload and DOI minting; no S3 API handed to the depositor despite the S3 backing store.
- composes with: Allows datasets up to 2 TB for submission. Open access publication requires a $1,950 fee per dataset to remove paywall restrictions for readers.
- reliability: Allows free upload of datasets up to 2 TB, but requires paid subscriptions or individual download purchase fees for reader access.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 2 TB of AWS S3 cloud storage per dataset for individual users (10 TB for institutional subscribers). No published limit on the number of datasets. Standard (non-Open-Access) deposit is free; making it Open Access costs $1,950.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '2TB Cloud Storage (AWS) for individual users ... Must be IEEE Paid DataPort Subscriber to Access Files'; Open Access option listed at $1,950
  - [2] 2026-10-21: individual plan '$40/month', 'Data Storage 2TB per dataset', 'Open Access Dataset Upload $1950'
  - [3] 2026-10-21: 'Create a Free Account - Register to view Open Access data files and upload your own research data'
- sources:
  - [1] https://ieee-dataport.org/submit-dataset
  - [2] https://ieee-dataport.org/subscribe
  - [3] https://ieee-dataport.org/

## IEEE DataPort — Data Competition module (the free + public route)

- `storage/ieee-dataport-data-competition-module` | fails-egress | evidence reported | binding per-object-cap | category research-data-repository
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ieee-dataport.org/submit-dataset
- price 0 via Data Competition or IEEE Society membership. Open Access publication is a flat $1,950 per dataset…
- free tier: 2 TB per dataset for individual users, 10 TB for Institutional Subscribers. The Data Competition submission type is listed as FREE and carries the same 2 TB / 10 TB ceilings. 'Dataset files may total up to 2 TB or 10 TB for Institutional Subscribers'. Competition files are stored in Amazon S3 and can be downloaded by any logged-in IEEE DataPort user, and 'If Competition has No Access Restrictions, no entry needs to be made in the Access Control List box and all users of IEEE DataPort that are logged in will have access.' That is the only route on this platform where storage is free AND reads are free, because the two paid routes both gate reads: Standard Dataset (free upload) exposes files only to subscribers, and Open Access Dataset costs $1,950 to make them public. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100 GB/file | bytes: 100000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free in the ordinary sense. Downloads are served from IEEE's own S3 bucket (ieee-dataport.s3.amazonaws.com, which correctly returns 403 to anonymous listing rather than 200-with-empty-body) and there is no egress meter on the participant side. Real ceiling is per-user concurrency, not bytes. | metered: no
- identity: email | detail: email
- interface: s3, cli
- limits:
  - per-object-cap (binding): 100 GB/file [1]
- limits note: Write-gated + read-gated, and the gate differs by route. Standard Dataset: upload free, read requires IEEE DataPort subscription (~$480/yr). Open Access: read free to all, write costs $1,950 per dataset. Competition: both free, but the entry is framed as a time-limited challenge with start and end dates and 'Competitions must meet eligibility requirements and are not intended for general dataset publication'. Per-file cap is not stated; IEEE's own guidance is 'for large datasets, we recommend uploading a series of files that are 100 GB or less'. A soft 100 GB/file figure. Supported formats list is broad (zip, tar, 7z, iso, hdf5, parquet, avro, orc, mat, wav, mp4 …).
- interface detail: web + s3
- tooling: Two real paths. (1) S3: a subscriber gets an AWS access key/secret and the bucket is ieee-dataport, with the dataset path /ieee-dataport/<DATASET TYPE>/<USERID>/<DATASETID>. AWS CLI, boto3, s3cmd, Cyberduck, CrossFTP, S3 Browser all documented. (2) Competition participants read via the 'AWS S3' tab which reveals per-file S3 URIs plus a 'View AWS Security Credentials' dialog with the secret key. Undocumented but usable: the web upload form needs no subscription at all.
- composes with: Datasets are unlimited per account and each carries an independent 2 TB ceiling, so the multiplier is datasets, not accounts. 10 datasets is 20 TB of nominal capacity on one free IEEE web account. Competition module can host several files per competition. Combining the two submission types on one account gives both a subscriber-upload path (S3) and a public-read path (competition).
- reliability: S3 bucket is real and correctly access-controlled (403, not a fake 200). IEEE may unpublish Standard Dataset entries whose files were never uploaded. Competition entries are time-bounded by design, so treat the competition route as a lease with a declared end date rather than an archive.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 2 TB per dataset for individual users, 10 TB for Institutional Subscribers. The Data Competition submission type is listed as FREE and carries the same 2 TB / 10 TB ceilings — 'Dataset files may total up to 2 TB or 10 TB for Institutional Subscribers'. Competition files are stored in Amazon S3 and can be downloaded by any logged-in IEEE DataPort user, and 'If Competition has No Access Restrictions, no entry needs to be made in the Access Control List box and all users of IEEE DataPort that are logged in will have access.' That is the only route on this platform where storage is free AND reads are free, because the two paid routes both gate reads: Standard Dataset (free upload) exposes…
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: 0 via Data Competition or IEEE Society membership. Open Access publication is a flat $1,950 per dataset, not per TB.
- evidence:
  - [1] 2026-10-21: 'Open Access Dataset $1,950'; 'Data Competition FREE … 2 TB Cloud Storage'. This single page proves all three routes and their prices.
  - [2] 2026-10-21: opened: 'Dataset files may total up to 2 TB or 10 TB for Institutional Subscribers'; 'Administrator must either check Restricted Access via Email List or check No Access Restrictions'; 'If Competition has No Access Restrictions … all users of IEEE DataPort that are logged in will have access.'
  - [3] 2026-10-21: opened: bucket name ieee-dataport, path /ieee-dataport/<DATASET TYPE>/<USERID>/<DATASETID>, credentials 'only provided to subscribers', and the note that the web upload form 'does not require a subscription'.
  - [4] 2026-10-21: opened: 'Yes, users need to subscribe to access and/or download Standard datasets … Open Access datasets are available to all registered users.' Confirms the read gate.
  - [5] 2026-10-21: opened: 'Free Account: Download open access datasets, upload standard datasets up to 2TB, and join/host data competitions.' Identity is a plain IEEE web account.
  - [6] 2026-10-21: PROBED: HTTP 200, 94,355 bytes of HTML, DOI 10.21227/dz4t-cm36 rendered, but no direct file link in the markup for a logged-out client — i.e. the open-access landing page is public while the object itself needs a session.
  - [7] 2026-10-21: curl -qsS -D - -> HTTP 403 with a proper <Error><Code>AccessDenied</Code>, not a 200. The bucket is real and locked; no anonymous listing.
  - [8] 2026-10-21: opened: 'All IEEE Society members automatically have a free individual subscription' ($480/yr value) and 'Every IEEE DataPort member is given an AWS access key'. This is the subscription-free shortcut to the S3 path — an IEEE Society membership (student rate is low tens of USD) removes the read gate entirely.
- sources:
  - [1] https://ieee-dataport.org/submit-dataset
  - [2] https://ieee-dataport.org/faq/what-fields-are-available-submit-data-competition-form
  - [3] https://ieee-dataport.org/help/upload-your-files-directly-ieee-dataport-s3-bucket
  - [4] https://ieee-dataport.org/faq/do-i-have-subscribe-ieee-dataport-order-download-datasets-and-tools-ieee-dataport
  - [5] https://ieee-dataport.org/getting-started
  - [6] https://ieee-dataport.org/open-access/heart-disease-dataset-comprehensive
  - [7] https://ieee-dataport.s3.amazonaws.com/?list-type=2&max-keys=2
  - [8] https://ieee-dataport.org/news/ieee-society-members-get-free-ieee-dataport-subscription
