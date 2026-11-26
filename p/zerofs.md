# ZeroFS

> zerofs.link | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zerofs/ | JSON https://fshy.ajam.dev/api/v1/entity/zerofs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZeroFS

- `storage/zerofs` | qualifies-with-caveat | evidence documented | binding none | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-11T03:44:15.955Z (live) | stale on 2026-12-12
- url https://zerofs.link
- free tier: Unlimited for active files. | unit: unlimited | metered on: stored-bytes | read on: 2026-11-10 | source: [1]
- per-object cap: No file size limit. | source: [1] | note: the FAQ answers 'File size limit?' with 'None.'
- retention: If a file is inactive for 15 days, it's gone. | days: 15 | source: [1] | note: the FAQ states a file inactive for 15 days is deleted.
- egress: No stated bandwidth cap; no speed limit claimed on the uploader. | metered: no
- identity: anonymous | detail: No account required.
- interface: rest
- limits note: A file inactive for 15 days is deleted.
- interface detail: rest
- tooling: A JSON API answers at https://zerofs.link/api/ with 'files' and 'folders' endpoints.
- composes with: Account-less uploads, so unlimited identities; the binding constraint is the 15-day inactivity deletion, which needs a re-access cron per file. At unlimited file size this is >= 500 GB per 'unit' trivially.
- reliability: Very new, looks like a Buzzheavier-style clone (same 'we only act on local court orders' posture, same lost-ID-never-recovered model). 15-day inactivity window makes it unusable for cold archive without active touching; untested for sustained throughput.
- notes: Unlimited storage for active files; no file size limit.
- evidence note: the FAQ states unlimited storage for active files.
- evidence:
  - [1] 2026-10-21: 'File size limit? None.' / 'How much storage? Unlimited for active files.' / 'Are files deleted? Yes. If a file is inactive for 15 days, it's gone.'
  - [2] 2026-10-21: probe: GET -> 200
  - [1] 2026-11-10: a first-party ZeroFS page states the storage offer | capture: sha256:ad6f42f4bb85ca6734dbbe13fe43edc2c612d7687512fb1b8e3f7bb233f08515 | quote: Unlimited for active files.
  - [1] 2026-11-10: the FAQ answers that there is no file size limit | capture: sha256:ad6f42f4bb85ca6734dbbe13fe43edc2c612d7687512fb1b8e3f7bb233f08515 | quote: File size limit? None.
  - [1] 2026-11-10: a file inactive for 15 days is deleted | capture: sha256:ad6f42f4bb85ca6734dbbe13fe43edc2c612d7687512fb1b8e3f7bb233f08515 | quote: Yes. If a file is inactive for 15 days, it's gone.
  - [2] 2026-11-10: no form and no email are asked for before an upload | capture: sha256:8ada1b7dde14093d88714a8dbb675cb02f2f294c34a89ab970bc91942465c430 | quote: One click. No forms. No email. Just storage.
  - [3] 2026-11-10: the service exposes a REST API with files and folders endpoints | capture: sha256:d3496e0b95a29ef554db4d8eb1af2fddfba18b8d36637f1c7fb2db138bcd1fd9 | quote: {"files":"http://zerofs.link/api/files/","folders":"http://zerofs.link/api/folders/"}
  - [2] 2026-11-11: the ZeroFS home page states that no account is required to use the service | capture: sha256:ad81e8fc0e6a2686f215e3b962edd63f6a7cdc84ee138fee351f2745835bb08c | quote: No account required.
- sources:
  - [1] https://zerofs.link/faq/
  - [2] https://zerofs.link/
  - [3] https://zerofs.link/api
