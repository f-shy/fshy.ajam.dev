# filetransfer.io

> filetransfer.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filetransfer/ | JSON https://fshy.ajam.dev/api/v1/entity/filetransfer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## filetransfer.io

- `storage/filetransfer-io` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:38.131Z (live) | stale on 2026-12-04
- url https://filetransfer.io/
- free tier: none reachable: Free tier provides 4 GB per transfer without registration and temporary retention. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: anonymous | detail: Sending and receiving both work without an account; no registration is required to use the free transfer.
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: 4 GB free, no registration, short retention.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 4 GB free, no registration, short retention.
  - [1] 2026-11-19: the first-party page still states a 4 GB per-package cap and 3-day retention | capture: sha256:20a6e08706356d1425adb5ddb1f3687eb029055769dcf6fbb191468ac0cad40b | quote: A package can hold as many files as you like as long as the total stays under 4 GB, and it keeps working for 3 days.
  - [1] 2026-11-19: the first-party FAQ states that sending and receiving require no account | capture: sha256:20a6e08706356d1425adb5ddb1f3687eb029055769dcf6fbb191468ac0cad40b | quote: No. Sending and receiving both work without an account.
  - [1] 2026-11-19: the first-party FAQ states that no account is needed to send or receive | capture: sha256:20a6e08706356d1425adb5ddb1f3687eb029055769dcf6fbb191468ac0cad40b | quote: No. Sending and receiving both work without an account.
- sources:
  - [1] https://filetransfer.io/
