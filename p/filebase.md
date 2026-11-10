# Filebase

> filebase.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filebase/ | JSON https://fshy.ajam.dev/api/v1/entity/filebase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filebase (IPFS tier)

- `storage/filebase` | fails-quota | evidence reported | binding volume-quota | category p2p
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:46:51.523Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://filebase.com
- free tier: Free: 5 GB of pooled Object Storage and IPFS storage, 500 pinned files, 10 GB a month of IPFS egress and free object egress; Pro $7.50 a month raises storage to 500 GB | unit: GB | metered on: stored-bytes | read on: 2026-11-01 | source: [1] | note: the pricing page was read on 2026-11-01; the binding constraint is the 5 GB volume, which limits[] carries
- per-object cap: the pricing page states no per-object cap; the limits it does state are a bucket count and a pinned-file count | source: [1] | note: not stated
- retention: Pinned content stays on the Filebase node indefinitely and files uploaded to an IPFS bucket stay pinned for as long as they are kept in the bucket; the pricing page states no period, its footnote calling pinned files objects maintained for persistence on the IPFS network | source: [1] | note: indefinite while the file is pinned and kept in the bucket; deleting an object unpins the CID and Filebase stops guaranteeing its availability; the pricing page's footnote describes pinning as persistence with no period
- egress: Split, and the split is the trap. 'For S3-compatible object storage buckets on the non-IPFS tier at s3.filebase.io, egress is free on every paid plan.' But 'IPFS bandwidth is not free.. On the free tier, there is a 5 GB / month egress cap'. And the pricing page states 10 GB IPFS Egress. Either way it is single-digit-to-10 GB/month. | metered: yes | free allowance: 10 GB per month of IPFS egress on Free
- identity: email | detail: the sign-up form asks for a first name, a last name, an email address and a password, with a Google sign-up option; no card, phone or ID field appears on the form
- interface: s3-compatible, rclone, cli
- limits:
  - volume-quota (binding): 5 GB of pooled storage on the Free plan [1]
- limits note: Single PUT 5 GB; multipart total 5 TB (1 TB recommended); 500 req/s S3 API; 1 bucket on Free; 500 pinned files.
- binding note: the free plan's 5 GB of pooled storage is a volume quota and is the constraint that fails first; object egress is free
- interface detail: s3
- tooling: S3 API at s3.filebase.io, region 'auto', SigV4; rclone s3 backend works; IPFS Pinning Service API; dedicated gateways; docs list rclone/boto3/aws-cli explicitly.
- composes with: 1 bucket on Free, no limit on object count within it. 5 GB per account is not repeatable to 500 GB in any practical way, and each account needs its own S3 keys.
- reliability: S3 API held up live: the public gateway served the test CID at 200 (414,201 bytes, Server: Filebase) but throttled during a rapid burst (2 of 8 answered before the burst ran long). The 'no egress fees' headline applies to the S3 tier, not the IPFS tier. A genuinely confusing pricing page and the single most common misread in this niche.
- notes: Free: 5 GB pooled storage across Object Storage and IPFS, 500 pinned files, 10 GB/month IPFS bandwidth, object egress free. Pro $7.50/mo: 500 GB pooled.
- evidence note: the pricing page, the bandwidth docs and the sign-up form were read on 2026-11-01; the identity, interface, retention and per-object fields were re-read, the live probe of the gateway was not repeated
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The free plan holds 5 GB of pooled storage against the 500 GB per unit this topic requires; object egress is free on both plans, so the byte allowance binds and the read path does not
  - dead_end.retry_when: if the free allowance rises to 500 GB of pooled storage on the $0 plan
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free: 'Storage 5 GB', 'Shared across Object Storage and IPFS', 'Pinned Files 500', 'IPFS Egress 10 GB', 'Object Egress Free'
  - [2] 2026-10-21: 'IPFS bandwidth is not free. IPFS buckets, gateways, Bitswap, trustless gateway responses, RPC responses, and Filebase Sites have separate IPFS bandwidth accounting.'
  - [3] 2026-10-21: probe: GET -> 200, 414201 bytes, Server: Filebase
  - [1] 2026-11-01: object egress is free on both plans, so the read path is not the constraint | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | Object EgressObject egress covers delivery from Object Storage. | Free | Free |
  - [1] 2026-11-01: the Free plan stores 5 GB against 500 GB on Pro | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | Storage | 5 GB | 500 GB |
  - [1] 2026-11-01: 500 GB is what the paid plan stores, so it is the retry threshold for a quota failure | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | Storage | 5 GB | 500 GB |
  - [1] 2026-11-01: Free holds 5 GB of pooled storage and Pro 500 GB | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | Storage | 5 GB | 500 GB |
  - [1] 2026-11-01: IPFS bandwidth beyond the allowance is priced at $0.015/GB | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | Additional IPFS Bandwidth | Not included | $0.015/GB |
  - [1] 2026-11-01: the Free plan includes 10 GB of IPFS egress | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | IPFS EgressIPFS egress covers IPFS content delivery and retrieval before additional IPFS egress charges apply. | 10 GB | 250 GB |
  - [4] 2026-11-01: the sign-up form carries an email field and no card, phone or ID field | capture: sha256:4a71616fe2ce5a3c9ec0e348ea612632a0e48a11419795c057b79eff1c3e9221 | quote: id="user_email" name="user[email]" type="email"
  - [4] 2026-11-01: a Google sign-up option sits beside the email form | capture: sha256:4a71616fe2ce5a3c9ec0e348ea612632a0e48a11419795c057b79eff1c3e9221 | quote: Sign up with Google
  - [1] 2026-11-01: the Free plan's storage is a volume allowance of 5 GB | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | Storage | 5 GB | 500 GB |
  - [1] 2026-11-01: 5 GB of free storage is the volume that binds | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | Storage | 5 GB | 500 GB |
  - [1] 2026-11-01: 5 GB is the Free plan's pooled storage allowance | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | Storage | 5 GB | 500 GB |
  - [1] 2026-11-01: the Free and Pro storage allowances are unchanged at 5 GB and 500 GB | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | Storage | 5 GB | 500 GB |
  - [1] 2026-11-01: the pricing page states the Free and Pro storage allowances | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | Storage | 5 GB | 500 GB |
  - [1] 2026-11-01: the Free plan states a bucket count of 1 and no per-object size cap | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: | Bucket Count | 1 | 100 |
  - [1] 2026-11-01: pinning is described as persistence with no retention period | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: Pinned files are IPFS-pinned objects maintained for persistence on the IPFS network.
  - [2] 2026-11-01: the bandwidth docs were read and state that IPFS bandwidth is metered | capture: sha256:2ce4a13b7ab01f81f36e257045883b482547a34f147c260bc7e82b08f76bbe61 | quote: IPFS bandwidth is not free.
  - [1] 2026-11-01: pinning is described as persistence with no retention period stated | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: Pinned files are IPFS-pinned objects maintained for persistence on the IPFS network.
  - [5] 2026-11-02: the docs state an indefinite retention period for pinned content, so 'no period stated' contradicts the docs | capture: sha256:1b5db3dcfbca0a16a037bdf5b23924f0b3001e419ac8871e63848982515a3436 | quote: Pinned content stays on that node indefinitely, regardless of how often it's requested.
  - [5] 2026-11-02: retention lasts while the object stays in the bucket, so deletion is what ends it | capture: sha256:1b5db3dcfbca0a16a037bdf5b23924f0b3001e419ac8871e63848982515a3436 | quote: Files uploaded to a Filebase IPFS bucket are automatically pinned to IPFS and stay pinned for as long as you keep them in the bucket.
  - [6] 2026-11-02: deletion is the event that ends retention, and Filebase then no longer guarantees availability | capture: sha256:3a1bec29e650205d1a043edf5491c49d1375b31289cee43363f3fe3c2fef0430 | quote: Deleting an object from a Filebase IPFS bucket unpins the underlying CID.
  - [1] 2026-11-02: the pricing page footnote describes pinning as persistence and states no period, and the row is the pricing page's own text, not the docs' | capture: sha256:d1c349bb79c31b0687b3a86e07f45c1cb1522442dd2077e81fddda789777a8e7 | quote: Pinned files are IPFS-pinned objects maintained for persistence on the IPFS network.
  - [5] 2026-11-02:  | capture: sha256:1b5db3dcfbca0a16a037bdf5b23924f0b3001e419ac8871e63848982515a3436 | quote: Pinned content stays on that node indefinitely, regardless of how often it's requested.
- sources:
  - [1] https://filebase.com/pricing/
  - [2] https://filebase.com/docs/concepts/bandwidth
  - [3] https://ipfs.filebase.io/ipfs/bafybei...5u4
  - [4] https://console.filebase.com/signup
  - [5] https://filebase.com/docs/ipfs/concepts/what-is-ipfs-pinning
  - [6] https://filebase.com/docs/ipfs/pinning/deleting-files

## infura ipfs

- `storage/infura-ipfs` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://filebase.com/blog/infura-ipfs-is-shutting-down-how-to-migrate/
- free tier: none reachable: Discontinued. New uploads and pinning stopped 2026-08-03; the IPFS API and dedicated gateway ended 2026-08-15, after which unmigrated content is no longer available. Infura's own docs URL… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Discontinued. New uploads and pinning stopped 2026-08-03; the IPFS API and dedicated gateway ended 2026-08-15, after which unmigrated content is no longer available. Infura's own docs URL…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Discontinued. New uploads and pinning stopped 2026-08-03; the IPFS API and dedicated gateway ended 2026-08-15, after which unmigrated content is no longer available. Infura's own docs URL…
- sources:
  - [1] https://filebase.com/blog/infura-ipfs-is-shutting-down-how-to-migrate/

## sia / skynet

- `storage/sia-skynet` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://filebase.com/blog/announcing-automatic-bucket-migration-for-skynet-and-storj-customers/
- free tier: none reachable: Skynet Labs shut down its websites and services in 2023 and Filebase ran a migration for Skynet customers; siasky.net free portal storage is gone. Sia itself survives as a protocol where… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Skynet Labs shut down its websites and services in 2023 and Filebase ran a migration for Skynet customers; siasky.net free portal storage is gone. Sia itself survives as a protocol where…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Skynet Labs shut down its websites and services in 2023 and Filebase ran a migration for Skynet customers; siasky.net free portal storage is gone. Sia itself survives as a protocol where…
  - [2] 2026-10-21: cited as the basis of the rejection: Skynet Labs shut down its websites and services in 2023 and Filebase ran a migration for Skynet customers; siasky.net free portal storage is gone. Sia itself survives as a protocol where you
  - [3] 2026-10-21: cited as the basis of the rejection: Skynet Labs shut down its websites and services in 2023 and Filebase ran a migration for Skynet customers; siasky.net free portal storage is gone. Sia itself survives as a protocol where you
- sources:
  - [1] https://filebase.com/blog/announcing-automatic-bucket-migration-for-skynet-and-storj-customers/
  - [2] https://www.coindesk.com/business/2022/08/12/blockchain-firm-skynet-labs-shutters-after-failing-to-get-new-funding
  - [3] https://docs.sia.tech/
