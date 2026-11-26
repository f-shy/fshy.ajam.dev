# Datum Storage

> datum.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datum/ | JSON https://fshy.ajam.dev/api/v1/entity/datum.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Datum Storage

- `storage/datum-storage` | trial-only | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-25T09:54:53.002Z (live) | stale on 2026-12-10
- url https://storage.datum.org
- free tier: Datum Storage gives you one free terabyte of space for the first year; paid additional storage is listed as Coming Soon at US$3.99 per terabyte per month. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [2] | note: No object-size limit is stated on the home or get-started pages; the S3-compatible endpoint is documented without a size clause.
- retention: source: [2] | note: The home page states a free terabyte for the first year and US$3.99 per terabyte per month; no data-retention term is stated.
- egress: unverified: no egress charge or allowance is stated on the home or get-started pages | metered: no
- identity: any-phone
- interface: s3-compatible
- limits note: 1 TB/account; requires the Datum ID mobile app on iOS/Android as the identity provider. There is no web-only path.
- interface detail: s3
- tooling: S3 API only ('designed to be compatible with the Amazon S3 API format'); tested clients Arq Backup, Duplicati/Duplicity/Duplicacy untested
- composes with: 1 TB x N identities, but each identity needs a phone-verified Datum ID, so identity cost is the multiplier
- reliability: app-gated identity makes account automation awkward; the product markets itself as early-stage ('not all [S3 clients] have been tested')
- notes: 1 TB free from signup ('Get 1TB Free Cloud Storage From Datum'), S3-compatible endpoint
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 TB free from signup ('Get 1TB Free Cloud Storage From Datum'), S3-compatible endpoint
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Datum Storage accounts are attached to a Datum Identity... creating a Datum Identity will require verification of your email address and phone number'; 'designed to be compatible with the Amazon S3 API format'
  - [2] 2026-10-21: 'Datum ID on the App Store / Google Play' (no web signup path)
  - [2] 2026-11-19: the first-party get-started page states the email and phone verification gate | capture: sha256:5939a38180f950c8f39152a4cb901d63a5a2939a9a9d4928332a0889c3c8c297 | quote: Please note that creating a Datum Identity will require verification of your email address and phone number.
  - [2] 2026-11-19: the first-party get-started page states S3 API compatibility | capture: sha256:5939a38180f950c8f39152a4cb901d63a5a2939a9a9d4928332a0889c3c8c297 | quote: Datum Storage is designed to be compatible with the Amazon S3 API format.
  - [1] 2026-11-19: the first-party home page states the 1 TB offer is for the first year | capture: sha256:78c6be50d6a64312179d90368c25b320ec414f06d5b1d861a6b1815356974657 | quote: Datum Storage gives you one free terabyte of space for the first year, but soon you'll be able to add as much additional storage as you need.
  - [1] 2026-11-19: the first-party home page carries the current free-tier statement | capture: sha256:78c6be50d6a64312179d90368c25b320ec414f06d5b1d861a6b1815356974657 | quote: Datum Storage gives you one free terabyte of space for the first year, but soon you'll be able to add as much additional storage as you need.
  - [1] 2026-11-25: the home page states the first-year free terabyte and the US$3.99 per terabyte per month price, with no egress or retention term | capture: sha256:78c6be50d6a64312179d90368c25b320ec414f06d5b1d861a6b1815356974657 | quote: Datum Storage gives you one free terabyte of space for the first year, but soon you'll be able to add as much additional storage as you need. Pay just US$3.99 per terabyte per month.
  - [2] 2026-11-25: the get-started page documents the S3-compatible endpoint and states no object-size limit | capture: sha256:5939a38180f950c8f39152a4cb901d63a5a2939a9a9d4928332a0889c3c8c297 | quote: Datum Storage is designed to be compatible with the Amazon S3 API format.
  - [2] 2026-11-25: the get-started page states the mobile-app Datum Identity with email and phone verification and the S3-compatible endpoint | capture: sha256:5939a38180f950c8f39152a4cb901d63a5a2939a9a9d4928332a0889c3c8c297 | quote: Datum Storage accounts are attached to a Datum Identity. To create your Datum Identity, download the Datum ID app and follow the on-screen instructions. ... Please note that creating a Datum Identity will require verification of your email address and phone number. ... Datum Storage is designed to be compatible with the Amazon S3 API format.
- sources:
  - [1] https://storage.datum.org/
  - [2] https://storage.datum.org/getstarted
