# ogramcloud

> ogramcloud.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ogramcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/ogramcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ogramcloud (ogramcloud.com)

- `storage/ogramcloud` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:07.465Z (live) | stale on 2026-12-04
- url https://ogramcloud.com/
- free tier: unverified: on 2026-11-19 the host gave no HTTP answer; a direct GET returned a transport error with status null and a TCP connection failed with a name-resolution error | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: the project README (Sanix-Darker/ocloud) describes Telegram servers as a free cloud storage server and states a 100MB per-upload API limit during beta; it prints no total amount or period
- per-object cap: stated-absent: the first-party host is unreachable today, so no per-object size cap is stated there | source: [1] | note: not applicable
- retention: stated-absent: the first-party host is unreachable today, so no retention period is stated there | source: [1]
- egress: stated-absent: the first-party host is unreachable today, so no egress terms are stated there | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the first-party host is unreachable today, so no storage client interface is stated
- tooling: not documented
- composes with: stated-absent: the first-party host is unreachable today, so no chaining mechanism is stated there
- reliability: On 2026-11-19 the host still gave no HTTP answer: a direct GET returned a transport error and a TCP connection failed with a name-resolution error. The service remains unavailable.
- notes: The repository Sanix-Darker/ogramcloud-cli-client advertises unlimited storage, but the backend host is offline. Connection attempts timed out with HTTP 522.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 
  - probe:https://ogramcloud.com/ 2026-10-30: a direct GET of https://ogramcloud.com/ got no HTTP answer; the connection timed out | capture: sha256:583006c01b78e17e59b2be13791b604dcdd577919a4f2664c7e49d92996c6310 | quote: "error": "timeout"
  - [2] 2026-10-30: the project README states a 100MB per-upload API limit during beta and no total amount or period | capture: sha256:46ec0254263108a6b6425118a4ebd88ccb20e9f2eaabf6f0218a775b28da0487 | quote: Because, it's on a Beta version, I have limited the upload-size to 100MB as a limit for the APi for tests per uploads for now!
  - [2] 2026-10-30: the README describes the service as Telegram servers used as free cloud storage, with no amount | capture: sha256:46ec0254263108a6b6425118a4ebd88ccb20e9f2eaabf6f0218a775b28da0487 | quote: Use Telegram-servers as free "CLOUD-STORAGE-SERVER" !
  - probe:ogramcloud.com:443 2026-10-30: a TCP connection to ogramcloud.com port 443 timed out | capture: sha256:51731a4df17e4e76be8487e9bf72716177a622a5804d959b57e5232f5c1118e9 | quote: "err": "TimeoutError('timed out')"
  - [2] 2026-10-30: the project README names https://ogramcloud.com/ as its hosted demo | capture: sha256:46ec0254263108a6b6425118a4ebd88ccb20e9f2eaabf6f0218a775b28da0487 | quote: [DEMO PROJECT-LINK (ogramcloud)](https://ogramcloud.com/)
  - probe:https://ogramcloud.com/ 2026-11-19: a direct GET on 2026-11-19 again returned no HTTP answer (status null, transport error) | capture: sha256:d58990bca9c6f0f647e78a12e3a6945aa7540312a70f501aefa15c7301017d36 | quote: "error": "transport"
  - probe:ogramcloud.com:443 2026-11-19: a TCP connection to port 443 on 2026-11-19 failed with a name-resolution error | capture: sha256:4c3895926564ed4f98a051de1536ac5ee0456f331c7b5c3646fb7550365e0a3e | quote: "ok": false
  - probe:https://ogramcloud.com/ 2026-11-19: the host still gives no HTTP answer, so its free storage amount cannot be read | capture: sha256:d58990bca9c6f0f647e78a12e3a6945aa7540312a70f501aefa15c7301017d36 | quote: "status": null
  - probe:https://ogramcloud.com/ 2026-11-19: a read-only GET of https://ogramcloud.com/ got no HTTP answer; the transport failed | capture: sha256:96e1296da2ca30c2de9d36924bad0982c0deddf1d0b3ffbd0001edc26abb54fa | quote: "status": null
- sources:
  - [1] https://ogramcloud.com/
  - [2] https://github.com/Sanix-Darker/ocloud
