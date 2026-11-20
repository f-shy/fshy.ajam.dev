# bashupload.com

> bashupload.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bashupload/ | JSON https://fshy.ajam.dev/api/v1/entity/bashupload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bashupload.com

- `storage/bashupload-com` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:38:40.394Z (live) | stale on 2026-12-04
- url https://bashupload.com/
- free tier: None reachable: Domain no longer resolves to an origin. DNS returns only an SOA in the Authority section (NXDOMAIN-equivalent, registrar-servers.com), and the proxy returns HTTP 530. The dataset still list. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: 50G max | source: [1] | note: 50G per-file upload ceiling stated on the archived homepage
- retention: Files are stored for 3 days and can be downloaded only once. | source: [1] | note: 3-day store with a single download
- egress: not stated on the archived bashupload.com homepage | metered: no
- identity: email
- interface: cli
- interface detail: command-line curl -T upload of a file to a share URL
- tooling: curl -T to upload a file
- composes with: single-use share: files stored for 3 days and downloadable only once
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Domain no longer resolves to an origin — DNS returns only an SOA in the Authority section (NXDOMAIN-equivalent, registrar-servers.com), and the proxy returns HTTP 530. The dataset still…
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Domain no longer resolves to an origin — DNS returns only an SOA in the Authority section (NXDOMAIN-equivalent, registrar-servers.com), and the proxy returns HTTP 530. The dataset still…
  - probe:https://bashupload.com/ 2026-11-19: the bashupload.com host does not resolve to an origin | capture: sha256:3f3f6666d30d3666affec4e9378b1471d06ffe65b917d0adec9df369ecb10995 | quote: "error_detail": "URLError: <urlopen error Tunnel connection failed: 502 the name did not resolve>"
  - withheld 2026-11-19: the proxy to bashupload.com returns HTTP 530 with the origin name unresolved, confirming the host is gone | capture: sha256:76cd635ec60aef7f41590c9444d9e9df0c490d1b25d1739f231451376b131d8c | quote: "status": 530
  - [2] 2026-11-19: the upload interface is a command-line curl -T upload | capture: sha256:64988caec8b7ff82b7cd8f246ca11bc37e9ed39eb7185295d7c0e99be801a7e4 | quote: curl bashupload.com -T your_file.txt
  - [2] 2026-11-19: the offer chains by one-time download within a 3-day store | capture: sha256:64988caec8b7ff82b7cd8f246ca11bc37e9ed39eb7185295d7c0e99be801a7e4 | quote: Files are stored for 3 days and can be downloaded only once.
  - [2] 2026-11-19: the per-object upload ceiling is 50G | capture: sha256:64988caec8b7ff82b7cd8f246ca11bc37e9ed39eb7185295d7c0e99be801a7e4 | quote: Upload files from command line to easily share between servers, desktops and mobiles, 50G max.
  - withheld 2026-11-19: the proxy target was unreachable on the read date | capture: sha256:36b513153951cf43e44503eb21fffefeafa569d4489c32b2edfc5b87545a8b5e | quote: "status": 530
  - withheld 2026-11-19: the proxy target failed DNS resolution and returned HTTP 530, so the domain no longer resolves to an origin | capture: sha256:29f5704ae3f07db813769be21eaa86d89eb73c2b331665e44256988064abc1c2 | quote: its name did not resolve (bashupload.com has no A or AAAA record)
- sources:
  - [1] https://bashupload.com/
  - [2] https://web.archive.org/web/20240115205024/https://bashupload.com/?provider=wayback
