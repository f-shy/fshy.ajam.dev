# storage boy

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/storage-boy/ | JSON https://fshy.ajam.dev/api/v1/entity/storage-boy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## storage boy (storageboy.com / .net / .jp) and okuriba.jp/.com — aggregator

- `storage/storage-boy-and-okuriba-jp-com-aggregator` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:27.948Z (inherited) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/storage-boy.md
- free tier: None reachable: STORAGE BOY is advertised in a live Japanese aggregator as '登録不要、容量無制限' with 1 GB per file and 7-day retention, but the domain no longer resolves on any TLD. NXDOMAIN on .com, .net and .jp,. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: not stated on https://storageboy.com (the domain does not resolve) | note: not applicable
- retention: not stated on https://storageboy.com (the domain does not resolve)
- egress: not stated on https://storageboy.com (the domain does not resolve) | metered: no
- identity: email
- interface: unknown
- interface detail: not stated on https://storageboy.com (the domain does not resolve)
- tooling: not documented
- composes with: the same as interface detail
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: STORAGE BOY is advertised in a live Japanese aggregator as '登録不要、容量無制限' with 1 GB per file and 7-day retention, but the domain no longer resolves on any TLD — NXDOMAIN on .com, .net and…
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - withheld 2026-10-21: STORAGE BOY is advertised in a live Japanese aggregator as '登録不要、容量無制限' with 1 GB per file and 7-day retention, but the domain no longer resolves on any TLD — NXDOMAIN on .com, .net and .jp
  - probe:storageboy.com 2026-11-19: DNS resolution for the STORAGE BOY domain failed on the check date | capture: sha256:e0b8592d4618e30242032ac710b9c3e6e30d903529d315687142a67cd74f1cfa | quote: the name did not resolve
  - probe:storageboy.net 2026-11-19: DNS resolution for the STORAGE BOY domain failed on the check date | capture: sha256:41ac9f948c789a80785bbfdcb768f04217d5dcbc9f6bb0beee1c5c482c83cc31 | quote: the name did not resolve
  - probe:storageboy.jp 2026-11-19: DNS resolution for the STORAGE BOY domain failed on the check date | capture: sha256:da2fa46cb60a1d41eb0e1ec4beb241e8714afc9e7f580805708157339340b8bc | quote: the name did not resolve
  - probe:https://storageboy.com 2026-11-19: no first-party page is reachable, so no interface can be established | capture: sha256:3c1660ce01e7b66a4f941ccb0dd58979ac6c81c216629c634ce251f9fd311578 | quote: "status": null
  - probe:https://storageboy.net 2026-11-19: the storageboy.net domain returned no HTTP status on 2026-11-19 | capture: sha256:5b94b6ff7062476c8f43203eef9f1c82840481cad0dce13039c730971e9b9133 | quote: "status": null
