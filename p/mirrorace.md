# MirrorAce

> mirrorace.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mirrorace/ | JSON https://fshy.ajam.dev/api/v1/entity/mirrorace.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MirrorAce

- `debrid/mirrorace` | dead | evidence documented | binding write-gated | category multi-host mirror uploader (dead: uploads disabled) | tier dead
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://mirrorace.com/
- free tier: No service. The site serves its own upload console with 'Uploading has been disabled.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The page also reads 'Upload servers are totally empty. 0.00%'.
- per-object cap: not applicable: no upload path | source: [1]
- retention: not applicable: nothing can be uploaded; the site says 'All the links have been restored' as of 3 Jan 2023, which is the last operational statement | source: [1]
- egress: No new mirrors can be created. Whether existing aggregate links still resolve was not tested. | metered: no | free allowance: none | source: [1]
- identity: email | detail: Historical: registration existed at mirrorace.com/account/types. No account can be created usefully now.
- interface: unknown
- limits:
  - write-gated (binding): 'Uploading has been disabled.' [1]
- binding note: The operator has turned writes off, which is the only constraint that matters; read-side behaviour was not tested.
- interface detail: The upload console renders but the upload action is disabled by the operator.
- tooling: Irrelevant while disabled.
- composes with: Nothing. The working substitute is mirrored.to, which still accepts uploads and performs the same function with 40+ destinations.
- reliability: The news table stops at 3 Aug 2023 with 'We are working on the upload speed issue. It will be fixed soon.', after two maintenance notices in the preceding eight months. No fix arrived.
- notes: Inactive mirror service. New file uploads are disabled and backend servers report empty capacity.
- evidence note: The disabled-upload state and the empty-server counter are read from the live page on 2026-10-23. An existing mirror link confirms whether the read side still works.
- extras:
  - last_news_entry: 2023-08-03
  - substitute: mirrored.to
- evidence:
  - [1] 2026-10-23: 'Uploading has been disabled.', 'Upload servers are totally empty.', '0.00%', and a news table whose last entry is '3 Aug 2023 ... We are working on the upload speed issue.'
- sources:
  - [1] https://mirrorace.com/
