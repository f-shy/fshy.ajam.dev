# Sia Storage

> sia.storage | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sia/ | JSON https://fshy.ajam.dev/api/v1/entity/sia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sia Storage App (sia.storage)

- `storage/sia-storage-app` | qualifies-with-caveat | evidence documented | binding none | category contributed storage - hosted indexer over third-party hosts
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:46:52.675Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://sia.storage/
- price USD 2.00 per TB-month on the Unlimited plan (USD 19.99/mo for 10 TB); USD 4.99 per TB-month for each TB above 10 TB. 20 TiB of storage is 21.99 TB, which is 11.99 TB above the included 10 TB, so USD 79.82/mo. | parsed USD 2/TB-mo
- free tier: Free plan 50 GB, 3 apps, 500 Mbps. Plus USD 7.99/mo: 500 GB, 10 apps, 500 Mbps. Pro USD 14.99/mo: 5 TB, 25 apps, 1 Gbps. Unlimited USD 19.99/mo: 10 TB, 100 apps, 5 Gbps, plus USD 4.99/TB-month for each TB stored above 10 TB. Plan volumes are decimal GB and TB as the plan table states them, not binary. | unit: GB | metered on: unstated | read on: 2026-11-01 | source: [1] | note: the plan table read on 2026-11-01; the included volumes are decimal GB and TB, and the tier above 10 TB bills USD 4.99/TB-month
- per-object cap: Through s3d the largest single object is built from multipart uploads of parts of up to 5 GiB and up to 10,000 parts per upload; the resulting ceiling is far above every plan volume the offer sells. No page states a cap for the SDK upload path. | source: [2] | note: the multipart ceiling belongs to the s3d S3 route; the SDK and app routes state no per-object cap, and every plan volume is reached first
- retention: Trashed files are deleted permanently 30 days after they are trashed, and the storage they used is freed the next time the app runs and syncs. No page states a deletion clock for live objects: they are stored until trashed, until the account is deleted, or until the account is signed out with local data cleared, which keeps the account and the uploaded files. | days: 30 | source: [3] | note: the 30-day clock applies to objects that are trashed; deleting an account, from the app menu, permanently deletes the account and everything stored with it
- egress: Each plan states a transfer speed cap (500 Mbps on Free and Plus, 1 Gbps on Pro, 5 Gbps on Unlimited) and the pricing page lists no per-GB egress price and no egress allowance. | metered: no
- identity: email | detail: email: the Sia Storage Company login page asks for an Email address and links a Sign up page, and the free plan is documented as needing no Siacoin to buy and no server to run; what the signup form asks beyond the email is unverified
- interface: s3-compatible, rclone, cli
- limits note: The plan table is the price: USD 19.99/mo for 10 TB, then USD 4.99 per TB-month for each TB above it, billed in decimal TB, so 20 TiB (21.99 TB) costs USD 79.82/mo. The free plan is 50 GB. Speed is a per-plan cap: 500 Mbps on Free and Plus, 1 Gbps on Pro, 5 Gbps on Unlimited.
- interface detail: The S3 route is s3d, a gateway the user installs and runs on their own machine (macOS, Linux, Windows or Docker) and points at a Sia Storage account; the s3d page calls it 's3d is a self-hosted gateway that speaks the S3 API'. The Sia Storage app for iOS and Android is the other client, and SDKs exist for Rust, Go, Python and JavaScript.
- tooling: rclone, Cyberduck, Nextcloud, Synology Hyper Backup, Arq, AWS CLI - all named on the s3d page
- composes with: s3d on a $3 VPS + rclone = an S3 endpoint whose bytes live on 530 independent hosts; put Cloudflare in front and egress becomes CF's problem
- reliability: Data is erasure-coded across many independent storage providers and repaired when redundancy drops, so the offer depends on those providers staying online. Siascan reported 2.26 PB of storage utilisation against 7.51 PB of provider capacity across 522 active hosts.
- notes: Free 50 GB; Plus USD 7.99/mo for 500 GB; Pro USD 14.99/mo for 5 TB; Unlimited USD 19.99/mo for 10 TB, then USD 4.99 per TB-month above 10 TB. 20 TiB of storage is 21.99 TB, which is 11.99 TB above the included 10 TB and costs USD 19.99 + USD 59.83 = USD 79.82/mo.
- evidence note: the plan table and its speed caps, the S3 route through s3d and siascan's network figures are quoted from captured pages read on 2026-11-01, each page carrying its own evidence row
- extras:
  - price_verbatim: Price - $7.99/mo $14.99/mo $19.99/mo
- evidence:
  - [1] 2026-10-21: pricing table: Free 50 GB / Plus $7.99 500 GB / Pro $14.99 5 TB / Unlimited $19.99 10 TB; '+$4.99/TB-mo over'; speed 500 Mbps / 500 Mbps / 1 Gbps / 5 Gbps
  - [2] 2026-10-21: 's3d is a self-hosted gateway that speaks the S3 API'; lists rclone, Cyberduck, Nextcloud, Synology Hyper Backup, Arq, AWS CLI
  - [4] 2026-10-21: 'Sia Storage ... gives you 50 GB free with nothing to install or maintain'; 'Network pricing averages around $3 per terabyte per month, including 3x redundancy'
  - [5] 2026-10-21: storage utilization 2.19 PB of 7.12 PB; 530 active hosts
  - [1] 2026-11-01: the four plans and their prices, storage volumes, app counts and speed caps | capture: sha256:6832a746ff5596eecdce8233f71d3755e62b0011d6f4c364fcb38e82023dd2fd | quote: Free Plus Pro Unlimited Price - $7.99/mo $14.99/mo $19.99/mo Storage 50 GB 500 GB 5 TB 10 TB +$4.99/TB-mo over Apps 3 10 25 100 Speed 500 Mbps 500 Mbps 1 Gbps 5 Gbps
  - [1] 2026-11-01: Unlimited includes 10 TB and bills USD 4.99 per TB-month above it | capture: sha256:6832a746ff5596eecdce8233f71d3755e62b0011d6f4c364fcb38e82023dd2fd | quote: 10 TB +$4.99/TB-mo over
  - [1] 2026-11-01: each plan states a transfer speed cap and no egress price | capture: sha256:6832a746ff5596eecdce8233f71d3755e62b0011d6f4c364fcb38e82023dd2fd | quote: Speed 500 Mbps 500 Mbps 1 Gbps 5 Gbps
  - [2] 2026-11-01: the S3 route is s3d, which the user installs and runs on their own machine | capture: sha256:dbd6b47039c8934886013a9984f83c10c7c2145ef5361193cc0cad8992d11d40 | quote: s3d is a self-hosted gateway that speaks the S3 API. ... An S3 endpoint on your own machine
  - [5] 2026-11-01: the network reported 2.26 PB of 7.51 PB and 522 active hosts | capture: sha256:8e6aee1839f8d9807a3869f81bb82653683ff827ba771d80bea4fb60099ee9ae | quote: Storage utilization 2.26 PB 7.51 PB ... Active hosts 522 87,156
  - [2] 2026-11-01: s3d runs on macOS, Linux, Windows or Docker | capture: sha256:dbd6b47039c8934886013a9984f83c10c7c2145ef5361193cc0cad8992d11d40 | quote: Runs where you do macOS, Linux, Windows, or Docker. Open source under the MIT license.
  - [1] 2026-11-01: the Sia Storage app is the iOS and Android client | capture: sha256:6832a746ff5596eecdce8233f71d3755e62b0011d6f4c364fcb38e82023dd2fd | quote: Available for iOS and Android
  - [6] 2026-11-01: the Sia Storage app and s3d are the clients of the hosted indexer | capture: sha256:31d8fe5ad1a4b5c87fd5ac82dc4fdc1f8ee162749fa96d1b0b4c17792b3547cd | quote: To actually store and retrieve files, you point a client — the Sia Storage app or s3d — at your Sia Storage account.
  - [3] 2026-11-02: the app FAQ states the 30-day trash clock; it states no deletion clock for live objects | capture: sha256:246d53b9c60a47e6ef4986d371f05fb76d49e43ab20a918071863de1d3fa3795 | quote: Trashed files are deleted permanently 30 days after you trash them, and the storage they used is freed the next time the app runs and syncs.
  - [3] 2026-11-02: trashed objects survive 30 days | capture: sha256:246d53b9c60a47e6ef4986d371f05fb76d49e43ab20a918071863de1d3fa3795 | quote: Trashed files are deleted permanently 30 days after you trash them, and the storage they used is freed the next time the app runs and syncs.
  - [3] 2026-11-02: the retention statement is on the app FAQ, not on the pricing page the field named | capture: sha256:246d53b9c60a47e6ef4986d371f05fb76d49e43ab20a918071863de1d3fa3795 | quote: Trashed files are deleted permanently 30 days after you trash them, and the storage they used is freed the next time the app runs and syncs.
  - [3] 2026-11-02: account deletion removes every stored object; the 30-day clock is the trash path | capture: sha256:246d53b9c60a47e6ef4986d371f05fb76d49e43ab20a918071863de1d3fa3795 | quote: It opens the Sia Storage website, where you sign in and permanently delete your account and everything stored with it.
  - [2] 2026-11-02: the S3 route caps a part at 5 GiB and an upload at 10,000 parts | capture: sha256:dbd6b47039c8934886013a9984f83c10c7c2145ef5361193cc0cad8992d11d40 | quote: Multipart uploads take parts of up to 5 GiB, with up to 10,000 parts per upload.
  - [2] 2026-11-02: the per-object statement is on the s3d page, not on the pricing page the field named | capture: sha256:dbd6b47039c8934886013a9984f83c10c7c2145ef5361193cc0cad8992d11d40 | quote: Multipart uploads take parts of up to 5 GiB, with up to 10,000 parts per upload.
  - [2] 2026-11-02: the stated cap is the multipart ceiling of the S3 gateway | capture: sha256:dbd6b47039c8934886013a9984f83c10c7c2145ef5361193cc0cad8992d11d40 | quote: Multipart uploads take parts of up to 5 GiB, with up to 10,000 parts per upload.
  - [7] 2026-11-02: the login gate is an email field with a sign-up link; no card, phone or identity document is asked for before the account | capture: sha256:b9ea7f7f98fdc445248c558f4ed88843b85db5f7f6365ee794f583613a08cc1c | quote: Email address
  - [7] 2026-11-02: the email login page links a first-party sign-up page | capture: sha256:b9ea7f7f98fdc445248c558f4ed88843b85db5f7f6365ee794f583613a08cc1c | quote: Don't have an account? [Sign up]
  - [3] 2026-11-02: the app FAQ restates the 50 GB free allowance | capture: sha256:246d53b9c60a47e6ef4986d371f05fb76d49e43ab20a918071863de1d3fa3795 | quote: Every Sia Storage account starts with 50GB free.
  - [4] 2026-11-02: the network documentation lists a separate bandwidth charge for transfer on the Sia network | capture: sha256:f8fa9e6da7c3ec5f0383eee13b209b21e0d111d21e238201eea822ee2a0da0f5 | quote: Bandwidth Fees – You pay for the bandwidth you use to upload or download files.
  - [3] 2026-11-02: the free allowance is 50 GB per account, restated on the app FAQ | capture: sha256:246d53b9c60a47e6ef4986d371f05fb76d49e43ab20a918071863de1d3fa3795 | quote: Every Sia Storage account starts with 50GB free.
- sources:
  - [1] https://sia.storage/
  - [2] https://sia.storage/s3d
  - [3] https://sia.storage/app
  - [4] https://docs.sia.tech/store-your-data/about-renting.md
  - [5] https://siascan.com/
  - [6] https://docs.sia.tech/store-your-data/using-sia-storage.md
  - [7] https://sia.storage/auth/login

## Sia Storage (hosted indexer, sia.storage)

- `storage/sia-storage` | fails-quota | evidence reported | binding per-ip-shaping | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://sia.storage
- free tier: 50 GB free. 'The free plan includes 50 GB of storage, up to 3 connected apps, and transfer speeds up to 524 Mbps — with no Siacoin to buy and no server to run.'. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered but rate-shaped by plan: 'transfer speeds up to 524 Mbps' on Free. No per-GB egress line item exists in Sia's model. | metered: no
- identity: email
- interface: s3-compatible, rclone
- limits:
  - per-ip-shaping (binding): 524 Mbps [1]
- limits note: per-object-cap: not stated on the pages read. request-rate / per-ip-shaping: 'transfer speeds up to 524 Mbps' is the explicit Free-plan throttle. retention: not stated; storage is contract-based, so retention is paid-for duration, not decaying.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: s3
- tooling: s3d gateway (github.com/SiaFoundation/s3d) exposes an S3-compatible API; docs name Rclone and Cyberduck explicitly. Python/Go/Rust/JS SDKs also exist. rclone has a native 'sia' backend (rclone.org/sia/).
- composes with: 50 GB x unlimited accounts (signup is free, no Siacoin required). The plan gate is '3 connected apps' per account, and an app is a token. The same wrapper pattern as Google service accounts. 400 accounts = 20 TB, but each is a separate signup.
- reliability: New hosted product (app launched 2026); only paths offered on the free page are the iOS/Android app and the s3d gateway, so scripting depends entirely on s3d working.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 50 GB free — 'The free plan includes 50 GB of storage, up to 3 connected apps, and transfer speeds up to 524 Mbps — with no Siacoin to buy and no server to run.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The free plan includes 50 GB of storage, up to 3 connected apps, and transfer speeds up to 524 Mbps'
  - [2] 2026-10-21: 'Sia Storage ... gives you 50 GB free with nothing to install or maintain'
  - [3] 2026-10-21: page metadata 'Start with 50GB free'; pricing table renders Free / 50 GB / Unlimited
- sources:
  - [1] https://docs.sia.tech/store-your-data/using-sia-storage.md
  - [2] https://docs.sia.tech/store-your-data/about-renting
  - [3] https://sia.storage
