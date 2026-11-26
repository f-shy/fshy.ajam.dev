# oshi.at

> oshi.at | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oshi/ | JSON https://fshy.ajam.dev/api/v1/entity/oshi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## oshi.at

- `storage/oshi-at` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:55.865Z (inherited) | stale on 2026-12-04
- url https://oshi.at/
- free tier: none reachable: Domain has been dropped and is now on a domain auction ('Bid on the domain oshi.at now / nicsell'). Also had an untrusted TLS chain (SEC_E_UNTRUSTED_ROOT). POST returns the auction page. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Domain has been dropped and is now on a domain auction ('Bid on the domain oshi.at now / nicsell'). Also had an untrusted TLS chain (SEC_E_UNTRUSTED_ROOT). POST returns the auction page.
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Domain has been dropped and is now on a domain auction ('Bid on the domain oshi.at now / nicsell'). Also had an untrusted TLS chain (SEC_E_UNTRUSTED_ROOT). POST returns the auction page.
  - probe:https://oshi.at/ 2026-11-19: the domain now redirects to a nicsell domain-auction page; the host no longer serves any storage offer | capture: sha256:18f3beda882571ba31acf30728cc91216cc704c0f396e6ac052c4d35722224a6 | quote: <title>Bid on the domain oshi.at now | nicsell</title>
  - probe:https://oshi.at/ 2026-11-19: the oshi.at domain is on a nicsell auction page, so the storage service is gone | capture: sha256:18f3beda882571ba31acf30728cc91216cc704c0f396e6ac052c4d35722224a6 | quote: <title>Bid on the domain oshi.at now | nicsell</title>
- sources:
  - [1] https://oshi.at/
