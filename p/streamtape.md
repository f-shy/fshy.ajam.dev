# Streamtape

> streamtape.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/streamtape/ | JSON https://fshy.ajam.dev/api/v1/entity/streamtape.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Streamtape

- `storage/streamtape` | qualifies-with-caveat | evidence documented | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:23.059Z (live) | stale on 2026-12-26
- url https://streamtape.com
- free tier: Upload as many Videos as you wish. Active files will be saved on a system of safe and secured servers | unit: unlimited | metered on: stored-bytes | read on: 2026-11-09 | source: [1]
- per-object cap: You're allowed to upload a file with up to 15 GB in space | source: [1] | note: The homepage states that a file may be uploaded with up to 15 GB in space.
- retention: source: [1] | note: The homepage states that active files will be saved and gives no retention period.
- egress: Unlimited Bandwidth | metered: no
- identity: email
- interface: rest
- limits note: Video formats only; files are encoded/re-encoded on ingest (lossy for anything not already a video). 'Active files' only are kept. Inactive files are purged. Downloads require a generated ticket.
- interface detail: rest
- tooling: Documented API at https://streamtape.com/api with account info, download ticket, get download link, file info and upload endpoints. Widely integrated into upload bots.
- composes with: the same as the free tier
- reliability: Re-encoding destroys byte fidelity, so it cannot store arbitrary binaries. Ticket-gated downloads and ad-injected players make unattended fetch fragile. Activity requirement is unquantified on the pages read.
- notes: 'Unlimited Storage — Upload as many Videos as you wish. Active files will be saved'.
- evidence note: the streamtape.com homepage states unlimited storage and a 15 GB per-file upload limit
- evidence:
  - [1] 2026-10-21: 'Unlimited Storage ... Active files will be saved on a system of safe and secured servers'
  - [2] 2026-10-21: API sections: Account Infos, generate Download Ticket, get Download Link, check File Info, Upload
  - [1] 2026-10-21: probe: GET -> 200
  - [3] 2026-11-09: the homepage states that users may upload as many videos as they wish and active files are kept | capture: sha256:51b88f2935d9484de5b993efa2ee8739e1827dc69baf89f0e7b6ffc46e848b3e | quote: Upload as many Videos as you wish. Active files will be saved on a system of safe and secured servers
  - [3] 2026-11-09: the homepage caps an uploaded file at 15 GB | capture: sha256:51b88f2935d9484de5b993efa2ee8739e1827dc69baf89f0e7b6ffc46e848b3e | quote: You're allowed to upload a file with up to 15 GB in space
  - [3] 2026-11-09: the homepage lists unlimited bandwidth | capture: sha256:51b88f2935d9484de5b993efa2ee8739e1827dc69baf89f0e7b6ffc46e848b3e | quote: Unlimited Bandwidth
  - [3] 2026-11-09: the homepage states unlimited storage and a 15 GB per-file limit | capture: sha256:51b88f2935d9484de5b993efa2ee8739e1827dc69baf89f0e7b6ffc46e848b3e | quote: Unlimited Storage ... You're allowed to upload a file with up to 15 GB in space
  - [1] 2026-11-25: the homepage states a 15 GB per-file upload limit | capture: sha256:56851f07c36ec3a4fc637acf3ec5c83ad13acc327aa7530d3b3b82fa3b261653 | quote: You're allowed to upload a file with up to 15 GB in space
  - [1] 2026-11-25: the homepage states the 15 GB upload limit | capture: sha256:56851f07c36ec3a4fc637acf3ec5c83ad13acc327aa7530d3b3b82fa3b261653 | quote: You're allowed to upload a file with up to 15 GB in space
  - [1] 2026-11-25: the homepage describes active files being saved and states no retention period | capture: sha256:56851f07c36ec3a4fc637acf3ec5c83ad13acc327aa7530d3b3b82fa3b261653 | quote: Upload as many Videos as you wish. Active files will be saved on a system of safe and secured servers
  - [1] 2026-11-25: the homepage describes active files and states no retention period | capture: sha256:56851f07c36ec3a4fc637acf3ec5c83ad13acc327aa7530d3b3b82fa3b261653 | quote: Upload as many Videos as you wish. Active files will be saved on a system of safe and secured servers
  - [1] 2026-11-25: the homepage states that bandwidth and speed are not limited | capture: sha256:56851f07c36ec3a4fc637acf3ec5c83ad13acc327aa7530d3b3b82fa3b261653 | quote: Stream the videos from anywhere, anytime, with no Bandwidth and speed limit
  - [2] 2026-11-25: the API documentation specifies HTTP requests | capture: sha256:2ae809c77936f9c177bb06decfabe7f06d4b1c5aa1e9edfeee413a71eb051a86 | quote: All requests to the API shall be HTTP
  - [1] 2026-11-25: the homepage states that users may upload as many videos as they wish | capture: sha256:56851f07c36ec3a4fc637acf3ec5c83ad13acc327aa7530d3b3b82fa3b261653 | quote: Upload as many Videos as you wish. Active files will be saved on a system of safe and secured servers
  - [1] 2026-11-25: the homepage still states that users may upload as many videos as they wish | capture: sha256:56851f07c36ec3a4fc637acf3ec5c83ad13acc327aa7530d3b3b82fa3b261653 | quote: Upload as many Videos as you wish. Active files will be saved on a system of safe and secured servers
- sources:
  - [1] https://streamtape.com/
  - [2] https://streamtape.com/api
  - [3] https://streamtape.com
