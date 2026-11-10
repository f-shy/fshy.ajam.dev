# ogramcloud

> ogramcloud.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ogramcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/ogramcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ogramcloud (ogramcloud.com)

- `storage/ogramcloud` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-30T18:09:49.684Z (inherited) | stale on 2026-11-14
- url https://ogramcloud.com/
- free tier: unverified: https://ogramcloud.com/ gave no HTTP answer on 2026-10-30; a direct GET and a TCP connection both timed out, two page readers answered with gateway errors, and no archived copy was readable (Arquivo.pt holds none, the Wayback Machine was rate-limited) | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: the project README (Sanix-Darker/ocloud) describes Telegram servers as a free cloud storage server and states a 100MB per-upload API limit during beta; it prints no total amount or period
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The repository Sanix-Darker/ogramcloud-cli-client advertises unlimited storage, but the backend host is offline. Connection attempts timed out with HTTP 522.
- notes: the same as reliability
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
- sources:
  - [1] https://ogramcloud.com/
  - [2] https://github.com/Sanix-Darker/ocloud
