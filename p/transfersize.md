# TransferSize

> transfersize.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/transfersize/ | JSON https://fshy.ajam.dev/api/v1/entity/transfersize.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TransferSize

- `debrid/transfersize` | qualifies-with-caveat | evidence documented | binding volume-quota | category file transfer service (free, Premium and Family plans) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://www.transfersize.com/
- price USD 9.99 per month for 1 TB of storage and 10 TB of bandwidth (Premium)
- free tier: Free forever, no card: send files up to 50 GB, 15 GB of storage, 6 GB a day of bandwidth, share links last up to 7 days. | unit: mixed | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1]
- per-object cap: 50 GB per file on Free; 500 GB on Premium and Family | source: [1]
- retention: share links last up to 7 days on Free; deleted-file recovery is 7 days | days: 7 | source: [1]
- egress: 6 GB a day on Free; 10 TB a month on Premium; extra bandwidth is $3.00 per TB and extra storage $5.00 per TB. | metered: yes | free allowance: 6 GB a day | source: [1]
- identity: anonymous | detail: The how-to page states that neither the sender nor the recipient needs an account to send up to 50 GB; Premium is a paid account with a card.
- interface: rest
- limits:
  - per-object-cap: 50 GB per file on Free, 500 GB on Premium and Family [1]
  - volume-quota (binding): 6 GB a day of bandwidth and 15 GB of storage on Free [1]
  - retention-clamped: share links last up to 7 days on Free [1]
- binding note: 6 GB a day of bandwidth is the free tier ceiling that a multi-file retrieval meets first.
- interface detail: Browser uploader with link and email sharing; no API page was read.
- tooling: Browser only on the pages read.
- composes with: Premium is $9.99 per month for 1 TB of storage, 10 TB of monthly bandwidth and files up to 500 GB; extra storage is $5.00 per TB.
- reliability: Share links expire after 7 days on the free tier.
- notes: Annual Premium is $89.99.
- evidence note: Plans read on the vendor pricing and how-to pages. Whether the free uploader works over a scripted client was not probed.
- evidence:
  - [2] 2026-11-03: sending up to 50 GB is free with no account | capture: sha256:f27510611e44b734f5ab1f14559e8ddb19fc785257f897921587413c62ecd0c9 | quote: Send files up to 50 GB for free. Neither you nor your recipient needs an account.
  - [1] 2026-11-03: free storage is 15 GB | capture: sha256:156c209dbde8247c55f9c66e19f422e840c02bcb5387e86faca3c13003e9f05e | quote: | Storage | 15 GB | 1 TB | 1 TB shared |
  - [1] 2026-11-03: free bandwidth is 6 GB a day | capture: sha256:156c209dbde8247c55f9c66e19f422e840c02bcb5387e86faca3c13003e9f05e | quote: | Bandwidth | 6 GB a day | 10 TB a month | 10 TB a month, shared |
  - [1] 2026-11-03: the largest file is 50 GB on Free and 500 GB on Premium | capture: sha256:156c209dbde8247c55f9c66e19f422e840c02bcb5387e86faca3c13003e9f05e | quote: | Largest file | 50 GB | 500 GB | 500 GB |
  - [1] 2026-11-03: free links last up to 7 days | capture: sha256:156c209dbde8247c55f9c66e19f422e840c02bcb5387e86faca3c13003e9f05e | quote: | Share links last up to | 7 days | 1 year | 1 year |
  - [1] 2026-11-03: Premium costs $9.99 per month | capture: sha256:156c209dbde8247c55f9c66e19f422e840c02bcb5387e86faca3c13003e9f05e | quote: | Price | $0 | $9.99/month or $89.99/year | $29.99/month or $289.99/year |
- sources:
  - [1] https://www.transfersize.com/pricing
  - [2] https://www.transfersize.com/how-to/send-large-files
