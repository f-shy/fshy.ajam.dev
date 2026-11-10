# MASV

> masv.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/masv/ | JSON https://fshy.ajam.dev/api/v1/entity/masv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MASV

- `storage/masv` | fails-quota | evidence reported | binding retention-clamped | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://masv.io/pricing
- free tier: 15 GB of free transfer every month plus 5 days of free storage per package. Credit card with a $10 pre-authorisation required at signup. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: request-rate/quota: 15 GB transfer per calendar month; retention: 5 days free storage per file, then per-GB storage billing; per-GB egress $0.25 after the allowance | days: 5 | source: [1] | note: not stated
- egress: Metered after the free allowance: $0.25/GB pay-as-you-go, charged on egress ('when a file exits our network, either as a download to a machine or an upload to connected storage, we apply an egress fee per gigabyte'). | metered: yes
- identity: institution
- interface: s3, rest
- limits:
  - retention-clamped (binding): retention: 5 days [1]
- limits note: Request-rate/quota: 15 GB transfer per calendar month; retention: 5 days free storage per file, then per-GB storage billing; per-GB egress $0.25 after the allowance. The task brief's '100 GB free' is wrong. It is 15 GB/month (100 GB is the Smash API trial, a different vendor).
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest (MASV API / desktop app / S3-adjacent cloud integrations)
- tooling: official MASV desktop app + API; cloud integrations push to S3/GCS/Azure
- composes with: 15 GB/month free credit x unlimited free accounts x a valid card each; the card pre-auth is the anti-multiplication gate. Even at 100 accounts that is 1.5 TB/month of transfer, not storage, and every byte over 15 GB bills at $0.25/GB.
- reliability: Files beyond the 5-day free storage window start accruing charges silently; the account auto-transitions to pay-as-you-go rather than stopping.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 15 GB of free transfer every month plus 5 days of free storage per package. Credit card with a $10 pre-authorisation required at signup.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'New customers can sign up and receive 15 GB of transfers each month. You also receive 5 days of free storage per package'
  - [2] 2026-10-21: 'You receive 15 GB of free data transfer every month ... Pay As You Go at $0.25 USD per GB ... b) You store files beyond the 5 days of free storage per file', 'a valid credit card is required ... $10 pre-authorization charge'
- sources:
  - [1] https://help.massive.io/en/free-tier-pay-as-you-go
  - [2] https://masv.io/pricing

## moveit / serv-u / filecatalyst / progress ws_ftp

- `storage/moveit-serv-u-filecatalyst-progress-ws-ftp` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://masv.io/pricing
- free tier: none reachable: All four are now Progress/Ipswitch enterprise MFT products sold by quote or per-server licence. None of them advertise a free hosted tier; they are the incumbent paid products this niche's… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: All four are now Progress/Ipswitch enterprise MFT products sold by quote or per-server licence. None of them advertise a free hosted tier; they are the incumbent paid products this niche's…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: All four are now Progress/Ipswitch enterprise MFT products sold by quote or per-server licence. None of them advertise a free hosted tier; they are the incumbent paid products this niche's…
- sources:
  - [1] https://masv.io/pricing
