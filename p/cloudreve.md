# Cloudreve

> cloudreve.org | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudreve/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudreve.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cloudreve (cloudreve/Cloudreve)

- `netdisk-pan/cloudreve` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category bridge
- needs card no, phone no, ID no, institution no | verified 2026-10-30T17:26:52.228Z (live) | stale on 2026-11-21
- url https://cloudreve.org/
- free tier: free software, no allowance stated: https://cloudreve.org/ offers the open-source Community Edition to self-host and prints no quota, unit or price; Pro is a paid upgrade | unit: none | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: no cap of its own; the cap is the storage policy's | source: [1]
- retention: as long as the operator keeps it running | source: [1]
- egress: direct client-side upload and download, so the server does not relay the bytes; the egress is the storage provider's | metered: no | source: [1]
- identity: anonymous | detail: the operator installs it; a reader needs no account on the bridge
- interface: rest, webdav, s3
- limits:
  - write-gated (binding): the storage policy decides; the public demo has no filesystem at all [2]
- binding note: Its own documentation says it is not for redistributing other cloud drives, which is exactly the use this topic wants, so the constraint is architectural rather than numeric.
- tooling: a Go binary with a Vue front end; REST v4 under /api/v4/*, WebDAV, and S3-compatible policy backends; the nfd-parser project ships a ce driver for it
- composes with: the alternative bridge, and the better one when the upstream is an object store rather than a consumer pan, because it uploads client-side and does not relay through the VPS
- reliability: The public demo at demo.cloudreve.org answers /api/v4/site/ping with code 0 and data 4.19.1-pro and has no filesystem, so a scan that stopped at the ping would record a live instance and find nothing behind it.
- notes: A v4 instance answers /api/v4/site/ping; v3 answered a different path, and neither exposes an anonymous mount list the way AList does. That is why 1 of 169 hosts classified as Cloudreve and why the class is not a public-instance population at all.
- self hosted: yes
- extras:
  - access_mode: self-hosted-bridge
  - language: Go
  - license: GPL-3.0
  - stars: 28868
  - last_push: 2026-10-20T19:34:33Z
- evidence:
  - [1] 2026-10-22: Community Edition is open source and Pro is a paid upgrade; features include WebDAV access, multi-cloud storage with client-side transfer, and slave storage nodes
  - [3] 2026-10-22: Cloudreve describes itself as a cloud drive rather than a manager for other cloud drives, and lists 'I want to redistribute other cloud storage services to my users' as a scenario it is not suitable for
  - probe:https://demo.cloudreve.org/api/v4/site/ping 2026-10-22: HTTP 200 with {"code":0,"data":"4.19.1-pro"}, which identifies Cloudreve v4 and its Pro build, with no anonymous filesystem
  - [4] 2026-10-22: 28,868 stars, GPL-3.0, last push 2026-10-20
  - [1] 2026-10-30: the Community Edition is open-source software and the page gives it no quota, unit or price | capture: sha256:d2b2da4a43d26c42644ae62b73c633a43791085c78ea5b29351255aa1e6aa0c4 | quote: The open-source Community Edition covers most use cases.
  - [1] 2026-10-30: Pro is sold through a purchase page | capture: sha256:d2b2da4a43d26c42644ae62b73c633a43791085c78ea5b29351255aa1e6aa0c4 | quote: [Buy Pro](https://cloudreve.org/purchase)
  - [1] 2026-10-30: Cloudreve is software the user installs and runs | capture: sha256:d2b2da4a43d26c42644ae62b73c633a43791085c78ea5b29351255aa1e6aa0c4 | quote: Build a self-hosted cloud storage service for personal or public use.
- sources:
  - [1] https://cloudreve.org/
  - [2] https://demo.cloudreve.org/api/v4/site/ping
  - [3] https://docs.cloudreve.org/en/
  - [4] https://api.github.com/repos/cloudreve/Cloudreve
