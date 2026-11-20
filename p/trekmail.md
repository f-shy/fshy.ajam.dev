# TrekMail Drive

> trekmail.net | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/trekmail/ | JSON https://fshy.ajam.dev/api/v1/entity/trekmail.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TrekMail Drive

- `netdisk-pan/trekmail-drive` | trial-only | evidence reported | binding per-object-cap | category flat-rate cloud storage with WebDAV, REST and MCP
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:20:59.762Z (inherited) | stale on 2026-11-19
- url https://trekmail.net/cloud-drive
- free tier: 5 GB permanent on the free plan, plus 1 TB for 30 days once per account with no card. Paid storage is sold on a slider from 250 GB to 100 TB, priced per terabyte | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 10 TB per file, with resumable transfers | bytes: 10000000000000 | source: [1] | note: the vendor writes 10 TB; the decimal figure is used as stated
- retention: Permanent on the free plan. The 1 TB trial is 30 days | source: [1]
- egress: No egress line item published; the page states '250 GB to 100 TB, priced by the terabyte and never by the head' | metered: no | source: [1]
- identity: email | detail: an email address. The 1 TB trial is 'one-time offer per account' with no card
- interface: webdav, rest, rclone
- limits:
  - per-object-cap (binding): 10 TB per file, with resumable transfers [1]
- binding note: The trial is 30 days and the free plan is 5 GB, so the clock is what ends it. The per-file ceiling is the number that would decide the plan if the price were known, and the price is behind a slider that the static page does not carry.
- tooling: rclone webdav is named on the page, against https://drive.trekmail.net/dav/files/account/. A REST API and a 42-tool MCP server exist, and per-device WebDAV passwords are issued
- composes with: A 10 TB per-file ceiling with resumable uploads, a REST API and MCP tooling is the only design in this survey aimed at programmatic bulk ingest by an agent rather than a human. The free plan is 5 GB, so the capability is priced and only the trial is free
- reliability: An email host that added a Drive product. drive.trekmail.net/status.php returns 404, so it is not a Nextcloud backend; /dav/files/ returns 401 on GET, so the endpoint exists and is auth-gated. The paid price is behind a slider and absent from the static page, which is why this is medium confidence
- notes: Free allocation provides 5 GB permanent storage and a 30-day temporary 1 TB trial. Paid tier pricing is omitted from static public landing pages, leaving upgrade rates unconfirmed until an order checkout flow is initiated.
- evidence note: Confidence is reported: endpoints and landing pages were documented from research records. Paid rates are omitted from static HTML markup, leaving price_per_tb_month null rather than estimated.
- extras:
  - access_mode: trial
  - free_tier_exists: yes
  - trial_days: 30
  - trial_bytes: 1 TB, one per account
  - per_file_cap_bytes_derived: 10000000000000
  - paid_price_published_in_static_html: no
  - mcp_server_tools: 42
- evidence:
  - [1] 2026-10-21: '250 GB to 100 TB, priced by the terabyte and never by the head'; 'Biggest file 10 TB'; 'Up to 10 TB per file, resumable transfers'
  - [1] 2026-10-21: 'Server URL https://drive.trekmail.net/dav/files/account/'; 'rclone for scheduled backups, Cyberduck for parallel uploads'; 'One password per device'
  - [1] 2026-10-21: FAQ: 'Yes: 1 TB free for 30 days, and no card. It is a one-time offer per account'; free plan 5 GB permanent
  - [2] 2026-10-21: HTTP 401 on GET, so the DAV path exists and is auth-gated; status.php returns 404, so the backend is not Nextcloud
  - [1] 2026-11-03: the page states a 10 TB single-file limit | capture: sha256:cc8a79db2f3eff7d69d751f856d44a7b5de2da22858bc7968659922c0aa82eab | quote: Up to 10 TB in a single file.
  - [1] 2026-11-03: the FAQ states 5 GB included on the free plan | capture: sha256:cc8a79db2f3eff7d69d751f856d44a7b5de2da22858bc7968659922c0aa82eab | quote: Every account starts with space included, from 5 GB on the free plan up to 200 GB on the largest one, shared with your mail if you use it.
  - [1] 2026-11-03: paid storage runs from 250 GB to 100 TB priced by the terabyte | capture: sha256:cc8a79db2f3eff7d69d751f856d44a7b5de2da22858bc7968659922c0aa82eab | quote: 250 GB to 100 TB, priced by the terabyte and never by the head.
  - probe:https://drive.trekmail.net/status.php 2026-11-03: status.php on the drive host answers HTTP 404, so it is not a Nextcloud backend | capture: sha256:56f2aa4d8151e4cca946fbff9fcbbe212d3f90fd9784c9e4b35f7b62ce3d3b48 | quote: "status": 404
  - probe:https://drive.trekmail.net/dav/files/ 2026-11-03: the WebDAV files path answers HTTP 401, an auth-gated endpoint | capture: sha256:436f5e25b572b6398021b67c42bea3a304dcfbdd8366d6c206874b87def1260a | quote: "status": 401
  - [1] 2026-11-03: the 1 TB 30-day trial with no card, once per account, is still offered | capture: sha256:cc8a79db2f3eff7d69d751f856d44a7b5de2da22858bc7968659922c0aa82eab | quote: Yes: 1 TB free for 30 days, and no card. It is a one-time offer per account and it works on every plan including the free one.
- sources:
  - [1] https://trekmail.net/cloud-drive
  - [2] https://drive.trekmail.net/dav/files/
