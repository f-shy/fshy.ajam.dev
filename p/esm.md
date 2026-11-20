# esm.sh as a blob store

> esm.sh | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/esm/ | JSON https://fshy.ajam.dev/api/v1/entity/esm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## esm.sh as a blob store

- `storage/esm-sh-as-a-blob-store` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:35.940Z (live) | stale on 2026-12-04
- url https://esm.sh/jquery@3.7.1
- free tier: None. The service returns a re-export stub pointing at a rewritten module path rather than the requested file's bytes, so it offers no general blob storage. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: It is a transform service, not a file server: request any module and you get a 136-byte re-export stub pointing at a rewritten path, not the bytes. Only JS/TS modules are addressable, and
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: It is a transform service, not a file server: request any module and you get a 136-byte re-export stub pointing at a rewritten path, not the bytes. Only JS/TS modules are addressable, and
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: It is a transform service, not a file server: request any module and you get a 136-byte re-export stub pointing at a rewritten path, not the bytes. Only JS/TS modules are addressable, and
  - [2] 2026-10-21: cited as the basis of the rejection: It is a transform service, not a file server: request any module and you get a 136-byte re-export stub pointing at a rewritten path, not the bytes. Only JS/TS modules are addressable, and
  - [3] 2026-10-21: cited as the basis of the rejection: It is a transform service, not a file server: request any module and you get a 136-byte re-export stub pointing at a rewritten path, not the bytes. Only JS/TS modules are addressable, and
  - [1] 2026-11-19: the response body is a re-export stub pointing at a rewritten module path, not a file's bytes | capture: sha256:bad488d5597d0822cdb4bd0eb02463d88d644e2dcdd4c87ee09f286e7ad965aa | quote: export * from "/jquery@3.7.1/es2022/jquery.mjs";
- sources:
  - [1] https://esm.sh/jquery@3.7.1
  - [2] https://esm.sh/jquery@3.7.1/dist/jquery.min.js
  - [3] https://esm.sh/onnxruntime-web@1.30.0
